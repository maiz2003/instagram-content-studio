#!/usr/bin/env python3
"""Build the Postiz loading queue for LOCK IN weeks 1-3 (run from the repo root).

Every post with its public media URLs (the guided posting site), caption, day, time and the switches Postiz may not
be able to set (AI label, Trial). The postiz-scheduler skill reads this file. Nothing here posts anything.
"""
import ast, json, os

SITE = "https://lockin-guide-92d3ef56.netlify.app"
clips = json.load(open("outputs/lock-in/posting-queue/clips.json"))
src = open("outputs/lock-in/account-manager/build_guide.py").read()
tree = ast.parse(src)
STORIES = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and n.targets[0].id == "STORIES")
posts = [c for c in clips if isinstance(c.get("week"), int)]
AI = {9, 11, 14, 15} | {c["n"] for c in posts if c["week"] == 3}
TRIAL = {10, 13, 17, 20}

queue = []
for c in posts:
    media = [f"{SITE}/{c['file']}"] if c["type"] == "reel" else [f"{SITE}/{s}" for s in c["slides"]]
    queue.append({
        "n": c["n"], "day": c["day"], "time_uk": "18:05", "channel": "instagram",
        "format": "trial_reel" if c["n"] in TRIAL else c["type"],
        "title": c["title"], "caption": c["caption"], "media": media,
        "cover_hint": "frame where the orange word has fully appeared, about 2 s in" if c["type"] == "reel" else "slide 1",
        "ai_label": c["n"] in AI, "trial": c["n"] in TRIAL,
        "stories_today": STORIES.get(c["day"], ""),
        "approved": False, "postiz_id": None, "status": "not loaded",
    })
json.dump({"brand": "LOCK IN", "site": SITE, "start_date": None, "tz": "Europe/London", "posts": queue},
          open("outputs/lock-in/postiz/queue.json", "w"), indent=1, ensure_ascii=False)
print(len(queue), "posts;", sum(p["ai_label"] for p in queue), "need AI label;", sum(p["trial"] for p in queue), "trial")
