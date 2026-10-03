#!/usr/bin/env python3
"""Which AI library clips are already used in Reel specs, and which are left. Run from the repo root."""
import glob, json, os

used = {}
for f in glob.glob("outputs/lock-in/*/reels/*.json"):
    for c in json.load(open(f))["cards"]:
        if c.get("bg"):
            used.setdefault(c["bg"]["file"], set()).add(os.path.basename(f).split("-")[0])
lib = sorted(glob.glob("assets/footage/lock-in/library/moving/*.mp4") + glob.glob("assets/footage/lock-in/library/*.mov")
             + glob.glob("assets/footage/lock-in/week2/*.mov"))
left = [l for l in lib if l not in used]
print(f"{len(lib) - len(left)} of {len(lib)} clips used; {len(left)} left")
for l in left:
    print("  unused:", os.path.basename(l))
