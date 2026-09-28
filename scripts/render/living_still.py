#!/usr/bin/env python3
"""Living still: turn one photo into a short, phone-like moving clip.

It uses no AI and no credits. It makes a slow push-in, pull-back or drift toward
a focus point, adds a slight handheld sway and roll, and applies the LOCK IN
footage grade with film grain. Motion is sub-pixel (Pillow affine plus bicubic),
so it doesn't jitter the way ffmpeg's zoompan does.

Usage:
  living_still.py --in photo.png --out clip.mp4 [--motion push] [--focus 0.5,0.5]
                  [--dur 5] [--zoom 0.07] [--sway 1.0] [--seed 1]
  living_still.py --batch plan.json      # a list of objects with the same keys

Motions:
- push: zoom in toward the focus point
- pull: start zoomed in and ease back
- drift-left / drift-right / rise: a slow pan at a steady slight zoom

Needs Pillow, numpy and ffmpeg (from $FFMPEG or PATH).
"""
import argparse, json, math, os, random, shutil, subprocess, sys

import numpy as np
from PIL import Image

W, H, FPS = 1080, 1920, 30
GRADE = ("eq=contrast=1.04:saturation=0.9:gamma=0.98,"
         "colorbalance=rs=0.02:bs=-0.02:rm=0.01:bm=-0.01,noise=alls=4:allf=t")


def ease(t):  # smooth in-out
    return t * t * (3 - 2 * t)


def ffmpeg_bin():
    return os.environ.get("FFMPEG") or shutil.which("ffmpeg") or sys.exit("ffmpeg not found: set $FFMPEG")


def render(src, out, motion="push", focus=(0.5, 0.5), dur=5.0, zoom=0.07, sway=1.0, seed=1, crf=21, **_):
    im = Image.open(src).convert("RGB")
    sw, sh = im.size
    # Largest 9:16 window that fits the source, centred on the focus (cover crop).
    bw = min(sw, sh * W / H)
    bh = bw * H / W
    fx, fy = focus[0] * sw, focus[1] * sh
    rng = random.Random(seed)
    ph = [rng.uniform(0, 2 * math.pi) for _ in range(6)]
    n = int(round(dur * FPS))
    cmd = [ffmpeg_bin(), "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
           "-r", str(FPS), "-i", "-", "-vf", GRADE, "-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
           "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", out]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n):
        t = i / max(1, n - 1)
        e = ease(t)
        if motion == "push":
            z, pan = 1 + zoom * e, (0, 0)
        elif motion == "pull":
            z, pan = 1 + zoom * (1 - e), (0, 0)
        else:  # drifts hold a slight zoom so there is room to move
            z = 1 + zoom
            d = (e - 0.5) * zoom * 0.9
            pan = {"drift-left": (-d, 0), "drift-right": (d, 0), "rise": (0, -d)}.get(motion, (0, 0))
        cw, ch = bw / z, bh / z
        # Move the window centre from the frame centre toward the focus as it zooms in.
        k = (z - 1) / zoom if zoom else 0
        cx0 = min(max(fx, bw / 2), sw - bw / 2)
        cy0 = min(max(fy, bh / 2), sh - bh / 2)
        cx = cx0 + (fx - cx0) * 0.6 * k + pan[0] * bw
        cy = cy0 + (fy - cy0) * 0.6 * k + pan[1] * bh
        # Handheld: two slow sines per axis, amplitude in output pixels, plus a tiny roll.
        ts = i / FPS
        sx = sway * (2.2 * math.sin(2 * math.pi * 0.23 * ts + ph[0]) + 0.9 * math.sin(2 * math.pi * 0.61 * ts + ph[1]))
        sy = sway * (2.6 * math.sin(2 * math.pi * 0.19 * ts + ph[2]) + 0.8 * math.sin(2 * math.pi * 0.53 * ts + ph[3]))
        rot = math.radians(sway * (0.10 * math.sin(2 * math.pi * 0.17 * ts + ph[4]) + 0.04 * math.sin(2 * math.pi * 0.47 * ts + ph[5])))
        s = cw / W  # source px per output px
        cx += sx * s
        cy += sy * s
        cx = min(max(cx, cw / 2 + 2), sw - cw / 2 - 2)
        cy = min(max(cy, ch / 2 + 2), sh - ch / 2 - 2)
        # Output pixel (x, y) -> source (a*x + b*y + c, d*x + e*y + f), rotated about the frame centre.
        cr, sr = math.cos(rot), math.sin(rot)
        a, b = s * cr, -s * sr
        d_, e_ = s * sr, s * cr
        c = cx - (a * W / 2 + b * H / 2)
        f = cy - (d_ * W / 2 + e_ * H / 2)
        frame = im.transform((W, H), Image.AFFINE, (a, b, c, d_, e_, f), resample=Image.BICUBIC)
        proc.stdin.write(np.asarray(frame, dtype=np.uint8).tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        sys.exit(f"ffmpeg failed for {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src")
    ap.add_argument("--out")
    ap.add_argument("--motion", default="push")
    ap.add_argument("--focus", default="0.5,0.5")
    ap.add_argument("--dur", type=float, default=5.0)
    ap.add_argument("--zoom", type=float, default=0.07)
    ap.add_argument("--sway", type=float, default=1.0)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--batch")
    a = ap.parse_args()
    if a.batch:
        jobs = json.load(open(a.batch))
        base = os.path.dirname(os.path.abspath(a.batch))
        for j in jobs:
            j = dict(j)
            j["focus"] = tuple(j.get("focus", (0.5, 0.5)))
            src = j.pop("in")
            out = j.pop("out")
            src = src if os.path.isabs(src) else os.path.join(base, src)
            out = out if os.path.isabs(out) else os.path.join(base, out)
            print("render", os.path.basename(out), flush=True)
            render(src, out, **j)
    else:
        render(a.src, a.out, a.motion, tuple(float(v) for v in a.focus.split(",")), a.dur, a.zoom, a.sway, a.seed)


if __name__ == "__main__":
    main()
