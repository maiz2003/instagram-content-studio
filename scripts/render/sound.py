#!/usr/bin/env python3
"""Compose a Reel's soundtrack: beat-synced music + context sound design.

Standard library only (ffmpeg does the reverb/ducking/loudness in reel.js).
Everything is synthesized, so there is nothing to license.

Usage:
    python3 scripts/render/sound.py <reel-spec.json> <out-dir>
Writes <out-dir>/music.wav and <out-dir>/sfx.wav (mono, 44.1 kHz).

Spec keys used:
  "duration": seconds
  "music": {                      # optional; no music key -> sfx only
     "bpm": 120, "mood": "dark" | "warm" | "tense", "groove": "halftime" | "straight",
     "sections": [[t, "intro"|"drop"|"break"|"thin"|"tension"|"build"|"stop"|"stutter"|"outro"], ...]
  }
  "sfx": [{"t": s, "type": name, "gain": 0-1, "dur": s, "rate": x}, ...]
  "auto_sfx": true               # default true: typing clicks under "type" builds,
                                 # an impact under every "slam" (unless an sfx is within 0.1 s)
SFX types: vibrate, knock2, door_close, impact, subdrop, riser, whoosh, clock,
           heartbeat, typing, scratch, tick
"""

import json
import math
import os
import random
import struct
import sys
import wave

SR = 44100
TAU = 2 * math.pi


def mtof(m):
    return 440.0 * 2 ** ((m - 69) / 12.0)


def lp_coef(fc):
    return 1 - math.exp(-TAU * fc / SR)


def write_wav(path, buf):
    peak = max(1e-9, max(abs(x) for x in buf))
    g = 0.95 / peak if peak > 0.95 else 1.0
    with wave.open(path, "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(b"".join(struct.pack("<h", int(max(-1.0, min(1.0, x * g)) * 32767)) for x in buf))


def add(buf, samples, start, gain=1.0):
    s = int(start * SR)
    n = len(buf)
    for i, v in enumerate(samples):
        j = s + i
        if 0 <= j < n:
            buf[j] += v * gain


# ---------------------------------------------------------------- drum/one-shot synthesis
def kick(dur=0.45):
    out, ph = [], 0.0
    for i in range(int(dur * SR)):
        t = i / SR
        f = 45 + 110 * math.exp(-t / 0.035)
        ph += f / SR
        s = math.sin(TAU * ph) * math.exp(-t / 0.18)
        s += 0.35 * math.sin(TAU * ph * 2) * math.exp(-t / 0.05)      # phone-audible harmonic
        out.append(math.tanh(1.8 * s))
    return out


def snare(dur=0.3, seed=3):
    rng = random.Random(seed)
    out, lp = [], 0.0
    for i in range(int(dur * SR)):
        t = i / SR
        n = rng.random() * 2 - 1
        lp += 0.35 * (n - lp)
        hp = n - lp
        tone = math.sin(TAU * 185 * t) * math.exp(-t / 0.05)
        out.append(0.75 * hp * math.exp(-t / 0.09) + 0.5 * tone)
    return out


def hat(dur=0.06, seed=5):
    rng = random.Random(seed)
    out, lp = [], 0.0
    for i in range(int(dur * SR)):
        t = i / SR
        n = rng.random() * 2 - 1
        lp += 0.6 * (n - lp)
        out.append((n - lp) * math.exp(-t / 0.018) * 0.6)
    return out


def pluck(midi, dur=0.35):
    f = mtof(midi)
    out, ph, lp = [], 0.0, 0.0
    for i in range(int(dur * SR)):
        t = i / SR
        ph += f / SR
        tri = 4 * abs((ph % 1) - 0.5) - 1
        sq = 1.0 if (ph % 1) < 0.5 else -1.0
        raw = 0.7 * tri + 0.3 * sq
        c = lp_coef(900 + 3500 * math.exp(-t / 0.06))
        lp += c * (raw - lp)
        out.append(lp * math.exp(-t / 0.16))
    return out


def bass_note(midi, dur):
    f = mtof(midi)
    out, ph = [], 0.0
    for i in range(int(dur * SR)):
        t = i / SR
        ph += f / SR
        env = min(1.0, t / 0.01) * math.exp(-t / (dur * 0.9))
        s = math.sin(TAU * ph) + 0.45 * math.sin(TAU * ph * 2) + 0.2 * math.sin(TAU * ph * 3)
        out.append(math.tanh(1.4 * s) * env)
    return out


# ---------------------------------------------------------------- context SFX
def sfx_vibrate(dur=0.9):
    rng = random.Random(11)
    out = []
    for i in range(int(dur * SR)):
        t = i / SR
        on = 1.0 if (t % 0.42) < 0.26 else 0.0
        motor = math.sin(TAU * 155 * t) * (0.6 + 0.4 * math.sin(TAU * 31 * t))
        rattle = (rng.random() * 2 - 1) * 0.35 * (1 if math.sin(TAU * 155 * t) > 0.7 else 0)
        out.append((motor * 0.7 + rattle) * on)
    return out


def _knock(seed):
    rng = random.Random(seed)
    out, lp = [], 0.0
    for i in range(int(0.16 * SR)):
        t = i / SR
        n = rng.random() * 2 - 1
        lp += 0.25 * (n - lp)
        body = math.sin(TAU * 118 * t) * math.exp(-t / 0.045) + 0.5 * math.sin(TAU * 236 * t) * math.exp(-t / 0.02)
        out.append(0.9 * body + 0.8 * lp * math.exp(-t / 0.012))
    return out


def sfx_knock2(dur=None):
    a, b = _knock(21), _knock(22)
    out = [0.0] * int(0.42 * SR)
    for i, v in enumerate(a):
        out[i] += v
    off = int(0.17 * SR)
    for i, v in enumerate(b):
        out[off + i] += 0.85 * v
    return out


def sfx_door_close(dur=None):
    rng = random.Random(31)
    out, lp = [], 0.0
    for i in range(int(0.9 * SR)):
        t = i / SR
        n = rng.random() * 2 - 1
        lp += 0.08 * (n - lp)
        thump = math.sin(TAU * (70 - 20 * min(1, t / 0.2)) * t) * math.exp(-t / 0.22)
        latch = (math.sin(TAU * 2600 * t) * math.exp(-(t - 0.06) / 0.008) if t > 0.06 else 0) * 0.35
        out.append(1.1 * thump + 0.9 * lp * math.exp(-t / 0.05) + latch)
    return out


def sfx_impact(dur=None):
    k = kick(0.8)
    rng = random.Random(41)
    out, lp = [], 0.0
    for i in range(int(0.8 * SR)):
        t = i / SR
        n = rng.random() * 2 - 1
        lp += 0.12 * (n - lp)
        sub = math.sin(TAU * (60 - 25 * min(1, t / 0.5)) * t) * math.exp(-t / 0.35)
        out.append(0.8 * k[i] + 0.6 * sub + 0.5 * lp * math.exp(-t / 0.08))
    return out


def sfx_subdrop(dur=0.9):
    out, ph = [], 0.0
    for i in range(int(dur * SR)):
        t = i / SR
        ph += (85 - 55 * (t / dur)) / SR
        out.append((math.sin(TAU * ph) + 0.4 * math.sin(TAU * ph * 2)) * math.exp(-t / (dur * 0.6)))
    return out


def sfx_riser(dur=1.5):
    rng = random.Random(51)
    out, lp, ph = [], 0.0, 0.0
    n = int(dur * SR)
    for i in range(n):
        x = i / n
        noise = rng.random() * 2 - 1
        lp += lp_coef(300 + 7000 * x * x) * (noise - lp)
        ph += (200 + 900 * x * x) / SR
        out.append((0.6 * lp + 0.25 * math.sin(TAU * ph)) * (x ** 1.6))
    return out


def sfx_whoosh(dur=0.6):
    rng = random.Random(61)
    out, lp = [], 0.0
    n = int(dur * SR)
    for i in range(n):
        x = i / n
        noise = rng.random() * 2 - 1
        lp += lp_coef(400 + 5000 * math.sin(math.pi * x)) * (noise - lp)
        out.append(lp * math.sin(math.pi * x) ** 1.5)
    return out


def sfx_clock(dur=2.0, rate=2.0):
    out = [0.0] * int(dur * SR)
    k, t = 0, 0.0
    while t < dur:
        f = 3100 if k % 2 == 0 else 2300
        for i in range(int(0.03 * SR)):
            j = int(t * SR) + i
            if j < len(out):
                tt = i / SR
                out[j] += (math.sin(TAU * f * tt) * 0.5 + math.sin(TAU * f * 0.37 * tt) * 0.4) * math.exp(-tt / 0.006)
        k += 1
        t += 1.0 / rate
    return out


def sfx_heartbeat(dur=2.0, rate=1.25):
    out = [0.0] * int(dur * SR)
    beat = 0.0
    while beat < dur:
        for off, g in ((0.0, 1.0), (0.22, 0.7)):
            s0 = int((beat + off) * SR)
            for i in range(int(0.18 * SR)):
                j = s0 + i
                if j < len(out):
                    tt = i / SR
                    out[j] += g * (math.sin(TAU * 55 * tt) + 0.5 * math.sin(TAU * 110 * tt)) * math.exp(-tt / 0.06)
        beat += 1.0 / rate
    return out


def sfx_typing(dur=0.7, rate=14.0):
    rng = random.Random(71)
    out = [0.0] * int(dur * SR + 0.05 * SR)
    t = 0.0
    while t < dur:
        f = 1800 + rng.random() * 1400
        for i in range(int(0.018 * SR)):
            j = int(t * SR) + i
            if j < len(out):
                tt = i / SR
                out[j] += ((rng.random() * 2 - 1) * 0.6 + math.sin(TAU * f * tt) * 0.4) * math.exp(-tt / 0.004) * 0.6
        t += (1.0 / rate) * (0.7 + rng.random() * 0.6)
    return out


def sfx_scratch(dur=0.5):
    rng = random.Random(81)
    out, lp = [], 0.0
    n = int(dur * SR)
    for i in range(n):
        x = i / n
        noise = rng.random() * 2 - 1
        wob = 0.5 + 0.5 * math.sin(TAU * 7 * x * dur)
        lp += lp_coef(600 + 3000 * wob) * (noise - lp)
        out.append(lp * (1 - x) * 1.3)
    return out


def sfx_tick(dur=None):
    return [math.sin(TAU * 2400 * i / SR) * math.exp(-(i / SR) / 0.008) * 0.6 for i in range(int(0.05 * SR))]


SFX = {
    "vibrate": sfx_vibrate, "knock2": sfx_knock2, "door_close": sfx_door_close, "impact": sfx_impact,
    "subdrop": sfx_subdrop, "riser": sfx_riser, "whoosh": sfx_whoosh, "clock": sfx_clock,
    "heartbeat": sfx_heartbeat, "typing": sfx_typing, "scratch": sfx_scratch, "tick": sfx_tick,
    # aliases for older specs
    "buzz": sfx_vibrate, "knock": sfx_knock2, "hit": sfx_impact,
}


def render_sfx(spec, n):
    buf = [0.0] * n
    events = list(spec.get("sfx", []))
    if spec.get("auto_sfx", True):
        explicit = [e["t"] for e in events]
        for c in spec.get("cards", []):
            for e in c.get("elements", []):
                at = e.get("at", c["start"])
                if e.get("build") == "type":
                    events.append({"t": max(0.0, at), "type": "typing", "dur": max(0.2, e.get("dur", 0.6) + min(0, at)), "gain": 0.35})
                if e.get("build") == "slam" and not any(abs(t - at) < 0.1 for t in explicit):
                    events.append({"t": at, "type": "impact", "gain": 0.7})
    for ev in events:
        fn = SFX[ev["type"]]
        kwargs = {}
        if "dur" in ev:
            kwargs["dur"] = ev["dur"]
        if "rate" in ev:
            kwargs["rate"] = ev["rate"]
        try:
            smp = fn(**kwargs)
        except TypeError:
            smp = fn()
        add(buf, smp, ev["t"], ev.get("gain", 0.8))
    return buf, events


# ---------------------------------------------------------------- music
MOODS = {
    # i–VI–iv–V in A minor (dark, cinematic)
    "dark": [[57, 60, 64], [53, 57, 60], [50, 53, 57], [52, 56, 59]],
    # i–VI–III–VII (warmer, resolving)
    "warm": [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]],
    # phrygian i–bII (tense)
    "tense": [[57, 60, 64], [58, 62, 65], [57, 60, 64], [58, 62, 65]],
}
ARP = [0, 1, 2, 1, 2, 3, 2, 1, 0, 2, 1, 3, 2, 1, 2, 0]         # index into chord (3 = root + octave)
GROOVES = {  # step (of 16) positions per bar
    "halftime": ({0, 7, 10}, {8}),          # dark trap feel: snare on beat 3
    "straight": ({0, 6, 8}, {4, 12}),       # kick on 1 & 3 (+ push), snare on 2 & 4
}
HAT_VEL = [1, .35, .7, .35, 1, .35, .7, .5, 1, .35, .7, .35, 1, .5, .8, .6]

SECTION = {  # pad_cut, pad_gain, kick, snare, hats, bass, arp
    "intro":   (650, 0.55, 0, 0, 0.5, 0, 0),
    "thin":    (380, 0.35, 0, 0, 0,   0, 0),
    "break":   (500, 0.5,  0, 0, 0,   1, 0),
    "tension": (900, 0.5,  0, 0, 0.6, 1, 0),
    "build":   (1400, 0.5, 0, 1, 1,   1, 1),
    "drop":    (2200, 0.5, 1, 1, 1,   1, 1),
    "outro":   (1600, 0.45, 1, 1, 0.7, 1, 1),
    "stop":    (2200, 0.5, 1, 1, 1,   1, 1),   # tape-stop applied afterwards; follow it with a "thin" section so it is never silent
    "stutter": (2200, 0.5, 1, 1, 1,   1, 1),   # slice-repeat applied afterwards
}


def section_at(sections, t):
    cur = sections[0][1]
    for st, name in sections:
        if t >= st:
            cur = name
    return cur


def render_music(m, n):
    bpm = m.get("bpm", 120)
    beat = 60.0 / bpm
    step = beat / 4
    bar = beat * 4
    prog = MOODS[m.get("mood", "dark")]
    secs = sorted([tuple(s) for s in m.get("sections", [[0, "drop"]])])
    kick_steps, snare_steps = GROOVES[m.get("groove", "halftime")]
    buf = [0.0] * n
    dur = n / SR

    # pad: 3 chord tones x 2 detuned saws, smoothed low-pass whose cutoff follows the section
    phases = [0.0] * 6
    lp1 = lp2 = 0.0
    cut = 600.0
    for i in range(n):
        t = i / SR
        sec = SECTION[section_at(secs, t)]
        chord = prog[int(t / bar) % len(prog)]
        target = sec[0]
        cut += (target - cut) * 0.0004
        c = lp_coef(cut)
        s = 0.0
        for k in range(3):
            f = mtof(chord[k])
            for d, det in enumerate((0.997, 1.004)):
                idx = k * 2 + d
                phases[idx] += f * det / SR
                s += 2 * (phases[idx] % 1) - 1
        s /= 6.0
        lp1 += c * (s - lp1)
        lp2 += c * (lp1 - lp2)
        swell = 0.85 + 0.15 * math.sin(TAU * t / (bar * 2))
        buf[i] = lp2 * sec[1] * swell

    # step sequencer: drums, bass, arp
    kick_s, snare_s, hat_s = kick(), snare(), hat()
    pl_cache = {}
    total_steps = int(dur / step) + 1
    duck = [1.0] * n
    for st in range(total_steps):
        t = st * step
        if t >= dur:
            break
        sec = SECTION[section_at(secs, t)]
        s16 = st % 16
        chord = prog[int(t / bar) % len(prog)]
        if sec[2] and s16 in kick_steps:
            add(buf, kick_s, t, 0.9)
            j0 = int(t * SR)
            for i in range(int(0.22 * SR)):              # sidechain-style duck of pad/bass
                if j0 + i < n:
                    duck[j0 + i] = min(duck[j0 + i], 0.55 + 0.45 * (i / (0.22 * SR)))
        if sec[3] and s16 in snare_steps:
            add(buf, snare_s, t, 0.55)
        if sec[4]:
            add(buf, hat_s, t, 0.22 * sec[4] * HAT_VEL[s16])
        if sec[5] and (s16 in kick_steps or (section_at(secs, t) in ("break", "tension") and s16 % 8 == 0)):
            root = chord[0] - 24
            add(buf, bass_note(root, step * 3), t, 0.55)
        if sec[6] and s16 % 2 == 0:
            idx = ARP[s16]
            note = chord[idx] + 12 if idx < 3 else chord[0] + 24
            if note not in pl_cache:
                pl_cache[note] = pluck(note)
            add(buf, pl_cache[note], t, 0.28)
    for i in range(n):
        buf[i] *= duck[i]

    # section effects: tape stop and stutter
    for k, (st, name) in enumerate(secs):
        end = secs[k + 1][0] if k + 1 < len(secs) else dur
        a, b = int(st * SR), min(n, int(end * SR))
        if name == "stop":
            L = min(b - a, int(0.7 * SR))
            src = buf[a:a + L * 2] + [0.0] * (L * 2)
            pos = 0.0
            for i in range(b - a):
                if i < L:
                    rate = 1.0 - i / L
                    pos += rate
                    j = int(pos)
                    buf[a + i] = src[j] * (1 - 0.3 * i / L) if j < len(src) else 0.0
                else:
                    buf[a + i] = 0.0
        if name == "stutter":
            sl = int(step * 2 * SR)
            piece = buf[a:a + sl]
            for i in range(b - a):
                buf[a + i] = piece[i % sl] * (1.0 if (i // sl) % 2 == 0 else 0.8) if piece else 0.0

    # loop-friendly edges
    fade = int(0.03 * SR)
    for i in range(min(fade, n)):
        buf[i] *= i / fade
        buf[n - 1 - i] *= i / fade
    return buf


def main():
    spec_path, out_dir = sys.argv[1], sys.argv[2]
    spec = json.load(open(spec_path))
    os.makedirs(out_dir, exist_ok=True)
    n = int(spec["duration"] * SR)
    sfx, _ = render_sfx(spec, n)
    write_wav(os.path.join(out_dir, "sfx.wav"), sfx)
    m = spec.get("music")
    music = render_music(m, n) if (m and not m.get("file")) else [0.0] * n   # a supplied track is mixed in reel.js
    write_wav(os.path.join(out_dir, "music.wav"), music)
    print(out_dir)


if __name__ == "__main__":
    main()
