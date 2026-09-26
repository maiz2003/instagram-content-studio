#!/usr/bin/env python3
"""Detect a music track's tempo and first downbeat, and re-time a Reel spec to it.

Standard library + ffmpeg (for decoding). Two commands:

  python3 scripts/render/beat.py detect <track.(mp3|wav|m4a)> [--start S]
      -> prints JSON {"bpm": .., "beat": .., "first_beat": .., "downbeat": ..}

  python3 scripts/render/beat.py sync <reel-spec.json> <track> <out-spec.json> [--start S] [--offset S]
      -> writes a copy of the spec whose timings are stretched from its 120 BPM
         (0.5 s) grid onto the track's beat grid, with "music": {"file": ..., "offset": ...}
         so reel.js plays the track instead of the generated score.

Needs FFMPEG in the environment (see agents/video-producer.md).
"""

import json
import math
import os
import struct
import subprocess
import sys

SR = 11025
HOP = 128


def decode(path, start=0.0, dur=60.0):
    ff = os.environ.get("FFMPEG", "ffmpeg")
    raw = subprocess.run([ff, "-loglevel", "error", "-ss", str(start), "-t", str(dur), "-i", path,
                          "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout
    n = len(raw) // 2
    return struct.unpack("<%dh" % n, raw[: n * 2])


def onset_envelope(x):
    # low-passed and full-band energy per hop -> positive flux (kick-weighted)
    env, prev, lp = [], 0.0, 0.0
    for i in range(0, len(x) - HOP, HOP):
        e_full = e_low = 0.0
        for v in x[i:i + HOP]:
            f = v / 32768.0
            lp += 0.08 * (f - lp)
            e_full += f * f
            e_low += lp * lp
        e = math.log1p(200 * (e_full + 3 * e_low))
        env.append(max(0.0, e - prev))
        prev = e
    m = sum(env) / max(1, len(env))
    return [max(0.0, v - m) for v in env]


def detect(path, start=0.0):
    x = decode(path, start)
    env = onset_envelope(x)
    fps = SR / HOP
    # normalised autocorrelation for every integer lag once, then score tempos on it
    n = len(env)
    maxlag = int(fps * 7) + 2                 # up to two bars at 70 BPM
    ac = [0.0] * maxlag
    for L in range(1, maxlag):
        acc = 0.0
        for i in range(n - L):
            acc += env[i] * env[i + L]
        ac[L] = acc / (n - L)

    def AC(L):
        if L < 1 or L >= maxlag - 1:
            return 0.0
        i, fr = int(L), L - int(L)
        return ac[i] * (1 - fr) + ac[i + 1] * fr

    best = (-1.0, 0.0, 0.0)
    for bpm10 in range(700, 1810, 5):                       # 70–181 BPM in 0.5 BPM steps
        bpm = bpm10 / 10
        lag = fps * 60 / bpm
        # bars carry the strongest periodicity in real music (kicks are often syncopated),
        # so weight bar (4 beats) and two-bar lags most, then beat and subdivisions
        score = (0.5 * AC(lag) + 0.8 * AC(2 * lag) + 1.5 * AC(4 * lag) + 1.0 * AC(8 * lag)
                 + 0.4 * AC(lag / 2) + 0.3 * AC(lag / 4))
        score *= math.exp(-0.5 * (math.log2(bpm / 115.0) / 0.9) ** 2)   # mild prior toward common tempos
        if score > best[0]:
            best = (score, bpm, lag)
    _, bpm, lag = best
    # 1) beat phase: the offset inside one beat whose beat grid (and its 8th-note midpoints)
    #    collects the most onset energy -> cuts always land on a real beat
    def grid_energy(o, period, half_w=0.0):
        tot, k = 0.0, 0
        while o + k * period < len(env) - 1:
            p = o + k * period
            tot += env[int(p)] + env[int(p) + 1] * 0.5
            if half_w and p + period / 2 < len(env) - 1:
                tot += half_w * env[int(p + period / 2)]
            k += 1
        return tot / max(1, k)

    phases = [(grid_energy(o, lag, 0.5), o) for o in range(int(lag) + 1)]
    beat_off = max(phases)[1]
    # 2) downbeat: which of the 4 beats starts the bar (strongest bar-periodic onsets)
    bar = 4 * lag
    cands = [(grid_energy(beat_off + d * lag, bar), d) for d in range(4)]
    d = max(cands)[1]
    beat = 60.0 / bpm
    first_beat = beat_off / fps
    downbeat = (beat_off + d * lag) / fps
    return {"bpm": round(bpm, 2), "beat": round(beat, 4), "first_beat": round(first_beat + start, 3),
            "downbeat": round(downbeat + start, 3)}


def fold_bpm(bpm):
    # keep the reel's pacing close to its 120 BPM design: use half/double time if needed
    while bpm < 90:
        bpm *= 2
    while bpm > 180:
        bpm /= 2
    return bpm


def scale_spec(spec, factor):
    def sc(v):
        return round(v * factor, 3)
    out = json.loads(json.dumps(spec))
    out["duration"] = sc(spec["duration"])
    for c in out["cards"]:
        c["start"], c["end"] = sc(c["start"]), sc(c["end"])
        for e in c["elements"]:
            if "at" in e:
                e["at"] = sc(e["at"]) if e["at"] >= 0 else e["at"]
            if "dur" in e:
                e["dur"] = sc(e["dur"])
        for p in c.get("punch", []):
            p["at"] = sc(p["at"])
    for s in out.get("sfx", []):
        s["t"] = sc(s["t"])
        if "dur" in s:
            s["dur"] = sc(s["dur"])
        if "rate" in s:
            s["rate"] = round(s["rate"] / factor, 3)
    return out


def main():
    args = sys.argv[1:]
    start, offset_override = 0.0, None
    if "--offset" in args:                       # manual downbeat (seconds into the track) if detection is off
        i = args.index("--offset")
        offset_override = float(args[i + 1])
        del args[i:i + 2]
    if "--start" in args:
        i = args.index("--start")
        start = float(args[i + 1])
        del args[i:i + 2]
    if args[0] == "detect":
        print(json.dumps(detect(args[1], start)))
    elif args[0] == "sync":
        spec_path, track, out_path = args[1], args[2], args[3]
        spec = json.load(open(spec_path))
        info = detect(track, start)
        bpm = fold_bpm(info["bpm"])
        factor = 120.0 / bpm                    # spec is designed on a 0.5 s (120 BPM) grid
        out = scale_spec(spec, factor)
        off = offset_override if offset_override is not None else info["downbeat"]
        out["music"] = {"file": os.path.abspath(track), "offset": off, "detected": info, "grid_bpm": bpm}
        json.dump(out, open(out_path, "w"), indent=1, ensure_ascii=False)
        print(json.dumps({"bpm": info["bpm"], "grid_bpm": bpm, "factor": round(factor, 4),
                          "duration": out["duration"], "offset": out["music"]["offset"]}))


if __name__ == "__main__":
    main()
