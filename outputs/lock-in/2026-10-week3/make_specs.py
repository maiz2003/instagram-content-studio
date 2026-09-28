#!/usr/bin/env python3
"""Writes the week-3 Reel specs (run from the repo root).

Footage comes from the library (assets/footage/lock-in/library/moving/). These are 5 s "moving photos"
with their own camera motion, so "push" is 0 here. Everything is AI imagery: switch on the AI label.
"""
import json, os

OUT = "outputs/lock-in/2026-10-week3/reels"
MOV = "assets/footage/lock-in/library/moving"
W2 = "assets/footage/lock-in/week2"
BASE = {"fps": 30, "theme": "brands/lock-in.theme.css", "label": "LOCK IN",
        "sound_kit": "assets/sounds/lock-in", "sound_style": "minimal",
        "music": {"bpm": 120, "mood": "focus", "sections": [[0, "ambient"]]}}
os.makedirs(OUT, exist_ok=True)


def head(t, style="cream", at=0.0, build="words", size=130, dur=0.5, gap=None):
    e = {"text": t, "style": f"head {style}", "size": size, "build": build, "at": at, "dur": dur}
    if gap is not None: e["gap"] = gap
    return e


def serif(t, at, build="type", size=64, dur=1.0, gap=40, color="cream"):
    return {"text": t, "style": f"serif {color}", "size": size, "build": build, "at": at, "dur": dur, "gap": gap}


def card(start, end, els, punch=None, bg=None, top=430):  # upper third: the photos keep their subject low
    c = {"start": start, "end": end, "top": top, "elements": els}
    if punch is not None: c["punch"] = [{"at": punch, "scale": 1.03}]
    if bg: c["bg"] = bg
    return c


def mov(name, at_in=0.0, **kw):
    """A library moving photo. It already moves, so no extra push."""
    return {"file": f"{MOV}/2026-09-28_{name}.mp4", "in": at_in, "push": 0, "dim": kw.pop("dim", 0.62), **kw}


def w2(name, at_in=0.0, **kw):
    return {"file": f"{W2}/{name}", "in": at_in, **kw}


def loop_card(first, start, end):
    """Last card = first card, already built, so the Reel loops cleanly [U.121]."""
    return card(start, end, [dict(e, at=start - 1.0) for e in first["elements"]], bg=first.get("bg"))


def cta(start, end, bg, line="Comment LOCK → find your door", extra=None, big=("COMMENT", "LOCK")):
    """One amber word per card: the second line of the big text."""
    els = [head(big[0], at=start, size=130), head(big[1], "amber", start + 0.4, "slam", size=170, gap=6),
           serif(line, start + 0.9, build="fade", size=48)]
    if extra: els.append(serif(extra, start + 1.5, build="fade", size=40, gap=24))
    return card(start, end, els, bg=bg)


def save(slug, spec):
    with open(os.path.join(OUT, slug + ".json"), "w") as f:
        json.dump({**BASE, **spec}, f, indent=1, ensure_ascii=False)
        f.write("\n")


LOCK = {"t": 0.0, "type": "lock", "gain": 0.9}


def end_lock(t):
    return {"t": t, "type": "lock", "gain": 0.9}


# ---- Day 15 · "3 blocks" · H.5 Quick Win (how-it-works → saves)
c0 = card(0, 2.5, [head("THE WHOLE", at=-0.12), head("SYSTEM:", "amber", 1.2, "slam", size=160, gap=6)], 1.2,
          mov("timer-closeup"))
save("15-three-blocks", {"duration": 14.0, "cards": [
    c0,
    card(2.5, 5.0, [head("20 MINUTES.", "amber", 2.5, "slam", size=130), serif("phone in another room.\ntimer on.", 3.2, dur=1.0, size=62)],
         bg=mov("r02_timer-dial")),
    card(5.0, 7.5, [head("THREE", at=5.0, size=120), head("BLOCKS.", "amber", 5.6, "slam", size=160, gap=6),
                    serif("that's the whole day.", 6.3, build="fade", size=56)], 5.6, mov("r04_study-tick-list")),
    card(7.5, 10.5, [serif("tick each one.\nmiss a day? fine.", 7.5, build="lines", dur=1.1, size=64), serif("never miss two.", 8.9, size=68, color="amber", gap=30)],
         bg=mov("r17_calendar-x", 0.3, rate=0.9)),
    cta(10.5, 13.0, mov("phone-in-drawer"), extra="save this for tonight"),
    loop_card(c0, 13.0, 14.0)],
    "sfx": [LOCK, {"t": 5.6, "type": "pop", "gain": 0.6}, end_lock(13.0)]})

# ---- Day 16 · Trial A · H.11 Destroying Alternatives (statement → reach)
c0 = card(0, 3.0, [head("AN APP THAT", at=-0.12, size=120), head("BLOCKS YOUR PHONE", "cream", 0.6, size=110, gap=6),
                   head("IS STILL ON YOUR PHONE.", "amber", 1.5, "slam", size=100, gap=6)], 1.5, mov("r14_scroll-drawer-open"))
save("16-trial-blocker-is-still-your-phone", {"duration": 11.0, "trial": True, "cards": [
    c0,
    card(3.0, 6.0, [serif("it's still one reach away.\nit still lights up.", 3.0, build="lines", dur=1.2, size=62), serif("you still check it.", 4.5, size=66, color="amber", gap=30)],
         bg=mov("r10_phone-in-box")),
    card(6.0, 8.5, [head("DISTANCE", at=6.0, size=130), head("WORKS.", "amber", 6.6, "slam", size=170, gap=6),
                    serif("another room. every block.", 7.2, build="fade", size=52)], 6.6, mov("r16_hallway-shelf-charging")),
    cta(8.5, 10.0, mov("story_door-phone-outside")),
    loop_card(c0, 10.0, 11.0)],
    "sfx": [LOCK, end_lock(10.0)]})

# ---- Day 18 · "Someone who notices" · H.10 Taste of Hidden Shares (call-out → sends)
c0 = card(0, 2.5, [head("YOU DON'T NEED", at=-0.12, size=120), head("A STUDY BUDDY.", "amber", 1.2, "slam", size=120, gap=6)], 1.2,
          mov("laptop-closed-handwriting"))
save("18-someone-who-notices", {"duration": 12.5, "cards": [
    c0,
    card(2.5, 5.0, [serif("you need someone", 2.5, dur=0.6, size=66), serif("who notices when you stop.", 3.3, dur=0.9, size=66, color="amber", gap=10)], bg=mov("r15_tear-page")),
    card(5.0, 7.5, [head("\"DAY 4.", at=5.0, size=120), head("YOU IN?\"", "amber", 5.6, "slam", size=150, gap=6),
                    serif("one message. every day.", 6.3, build="fade", size=52)], 5.6, mov("r13_library-highlighter")),
    cta(7.5, 11.5, mov("r01_phone-face-down"), line="send this to the one who'd notice",
        extra="then comment LOCK → find your door", big=("SEND", "THIS")),
    loop_card(c0, 11.5, 12.5)],
    "sfx": [LOCK, end_lock(11.5)]})

# ---- Day 19 · Trial B · H.7 Attraction Through Rejection (sale-adjacent → comments/DMs)
c0 = card(0, 2.5, [head("DON'T TAKE", at=-0.12), head("THIS QUIZ", "cream", 0.5, gap=6),
                   head("FOR MOTIVATION.", "amber", 1.3, "slam", size=110, gap=6)], 1.3, mov("four-doors-page"))
save("19-trial-not-for-motivation", {"duration": 10.5, "trial": True, "cards": [
    c0,
    card(2.5, 5.5, [serif("it won't hype you up.", 2.5, dur=0.7, size=64), serif("it tells you which door\nyou leave through.", 3.5, build="lines", dur=1.1, size=64, color="amber", gap=30)],
         bg=mov("r06_restless-hands-clock")),
    card(5.5, 8.0, [head("4 QUESTIONS.", at=5.5, size=120), head("ONE FIX.", "amber", 6.1, "slam", size=160, gap=6)], 6.1,
         mov("four-doors-page", 1.5)),
    cta(8.0, 9.5, mov("never-miss-twice-page"), line="Comment LOCK → I'll DM you the quiz"),
    loop_card(c0, 9.5, 10.5)],
    "sfx": [LOCK, end_lock(9.5)]})

# ---- Day 20 · "Morning or night?" · opinion → comments (H.3 Against the Current)
c0 = card(0, 2.5, [head("MORNING OR", at=-0.12), head("NIGHT?", "amber", 1.0, "slam", size=170, gap=6)], 1.0,
          mov("r09_kitchen-mug"))
save("20-morning-or-night", {"duration": 12.0, "cards": [
    c0,
    card(2.5, 4.5, [head("WRONG", at=2.5, size=130), head("QUESTION.", "amber", 3.1, "slam", size=150, gap=6)], 3.1,
         mov("story_night-desk-space")),
    card(4.5, 7.5, [serif("it doesn't matter when you study.", 4.5, dur=0.9, size=58), serif("it matters where your phone is.", 5.7, dur=0.9, size=62, color="amber", gap=30)],
         bg=mov("phone-into-drawer")),
    cta(7.5, 11.0, mov("r16_hallway-shelf-alt"), line="morning or night person? tell me below.",
        extra="Comment LOCK → find your door", big=("WHERE'S", "YOURS?")),
    loop_card(c0, 11.0, 12.0)],
    "sfx": [LOCK, end_lock(11.0)]})

# ---- Day 21 · "15 minutes for 'so behind'" · H.5 Quick Win on the door-3 fix (how-it-works → saves)
c0 = card(0, 2.5, [head("\"I'M SO", at=-0.12, size=140), head("BEHIND.\"", "amber", 1.0, "slam", size=170, gap=6)], 1.0,
          w2("03_anxious.mov", 0))
save("21-fifteen-minutes-so-behind", {"duration": 14.0, "cards": [
    c0,
    card(2.5, 5.0, [serif("behind on what, exactly?", 2.5, dur=0.7, size=60), serif("if you can't say,\nthat's the problem.", 3.5, build="lines", dur=0.9, size=62, color="amber", gap=30)],
         bg=w2("03_anxious.mov", 2.0, rate=0.9)),
    card(5.0, 8.0, [head("15 MINUTES.", at=5.0, size=120), head("3 PRIORITIES.", "amber", 5.7, "slam", size=120, gap=6),
                    serif("written down, before the week starts.", 6.5, build="fade", size=48)], 5.7, mov("r07_sunday-this-week")),
    card(8.0, 10.5, [head("THEN", at=8.0, size=130), head("START.", "amber", 8.5, "slam", size=170, gap=6),
                     serif("the list does the worrying for you.", 9.2, build="fade", size=50)], 8.5, mov("r07_sunday-this-week-alt")),
    cta(10.5, 13.0, mov("r04_study-tick-list"), extra="save it for sunday"),
    loop_card(c0, 13.0, 14.0)],
    "sfx": [LOCK, {"t": 5.7, "type": "pop", "gain": 0.6}, end_lock(13.0)]})

print("specs written:", sorted(os.listdir(OUT)))
