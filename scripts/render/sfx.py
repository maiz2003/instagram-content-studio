#!/usr/bin/env python3
"""Synthesize a Reel's sound layer (SFX hits + optional low drone bed) as a WAV.

Standard library only. Everything is generated, so there's nothing to license.
Music is still added in the Instagram editor when posting (library tracks).

Usage:
    python3 scripts/render/sfx.py <reel-spec.json> <out.wav>

Reads from the spec: "duration", "sfx": [{"t": seconds, "type": name, "gain": 0-1}],
optional "bed": {"type": "drone", "gain": 0-1}.
SFX types: knock, hit, buzz, tick, whoosh.
"""

import json
import math
import random
import struct
import sys
import wave

RATE = 44100


def env(i, n, attack=0.004, decay=0.25):
    t = i / RATE
    a = min(1.0, t / attack) if attack > 0 else 1.0
    return a * math.exp(-t / decay)


def knock(n=int(0.35 * RATE)):
    # low wooden thud: two damped sines + a click of noise
    rng = random.Random(1)
    out = []
    for i in range(n):
        t = i / RATE
        s = 0.8 * math.sin(2 * math.pi * 95 * t) * math.exp(-t / 0.09)
        s += 0.35 * math.sin(2 * math.pi * 190 * t) * math.exp(-t / 0.05)
        s += 0.25 * (rng.random() * 2 - 1) * math.exp(-t / 0.008)
        out.append(s)
    return out


def hit(n=int(0.8 * RATE)):
    # soft low boom for the amber-word landing
    out = []
    for i in range(n):
        t = i / RATE
        f = 70 - 25 * min(1, t / 0.3)
        out.append(0.9 * math.sin(2 * math.pi * f * t) * env(i, n, 0.005, 0.28))
    return out


def buzz(n=int(0.9 * RATE)):
    # phone vibration: 3 pulses of a rough 170 Hz tone
    out = []
    for i in range(n):
        t = i / RATE
        on = (t % 0.3) < 0.18
        s = math.copysign(1, math.sin(2 * math.pi * 170 * t)) * 0.25 + 0.3 * math.sin(2 * math.pi * 340 * t)
        out.append(s * (0.7 if on else 0.0))
    return out


def tick(n=int(0.06 * RATE)):
    return [0.5 * math.sin(2 * math.pi * 2200 * i / RATE) * math.exp(-(i / RATE) / 0.01) for i in range(n)]


def whoosh(n=int(0.5 * RATE)):
    rng = random.Random(2)
    out, prev = [], 0.0
    for i in range(n):
        x = i / n
        prev = 0.85 * prev + 0.15 * (rng.random() * 2 - 1)
        out.append(prev * math.sin(math.pi * x) * 0.9)
    return out


SFX = {"knock": knock, "hit": hit, "buzz": buzz, "tick": tick, "whoosh": whoosh}


def main():
    spec_path, out_path = sys.argv[1], sys.argv[2]
    spec = json.load(open(spec_path))
    total = int(spec["duration"] * RATE) + RATE // 2
    mix = [0.0] * total
    bed = spec.get("bed")
    if bed and bed.get("type") == "drone":
        g = bed.get("gain", 0.08)
        for i in range(total):
            t = i / RATE
            fade = min(1.0, t / 1.0, (total / RATE - t) / 1.0)
            s = math.sin(2 * math.pi * 55 * t) + 0.5 * math.sin(2 * math.pi * 82.5 * t) + 0.25 * math.sin(2 * math.pi * 110.3 * t)
            mix[i] += g * s * (0.85 + 0.15 * math.sin(2 * math.pi * 0.2 * t)) * max(0.0, fade)
    for ev in spec.get("sfx", []):
        samples = SFX[ev["type"]]()
        start = int(ev["t"] * RATE)
        g = ev.get("gain", 0.8)
        for j, s in enumerate(samples):
            if start + j < total:
                mix[start + j] += g * s
    peak = max(1e-9, max(abs(x) for x in mix))
    norm = 0.89 / peak if peak > 0.89 else 1.0
    with wave.open(out_path, "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        w.writeframes(b"".join(struct.pack("<h", int(max(-1, min(1, x * norm)) * 32767)) for x in mix))
    print(out_path)


if __name__ == "__main__":
    main()
