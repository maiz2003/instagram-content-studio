#!/usr/bin/env python3
"""Writes the week-2 Reel specs (run from the repo root). Door Reels use the owner's week-2 clips
(assets/footage/lock-in/week2/, names from the shot list); render_text_only strips "bg" for the fallback."""
import json, os

OUT = "outputs/lock-in/2026-10-week2/reels"
FOOT = "assets/footage/lock-in/week2"
BASE = {"fps": 30, "theme": "brands/lock-in.theme.css", "label": "LOCK IN",
        "sound_kit": "assets/sounds/lock-in", "sound_style": "minimal",
        "music": {"bpm": 120, "mood": "focus", "sections": [[0, "ambient"]]}}

def head(t, style="cream", at=0.0, build="words", size=130, dur=0.5, gap=None):
    e = {"text": t, "style": f"head {style}", "size": size, "build": build, "at": at, "dur": dur}
    if gap is not None: e["gap"] = gap
    return e

def serif(t, at, build="type", size=64, dur=1.0, gap=40):
    return {"text": t, "style": "serif cream", "size": size, "build": build, "at": at, "dur": dur, "gap": gap}

def card(start, end, els, punch=None, bg=None, top=620):
    c = {"start": start, "end": end, "top": top, "elements": els}
    if punch is not None: c["punch"] = [{"at": punch, "scale": 1.03}]
    if bg: c["bg"] = bg
    return c

def clip(name, at_in=0.0, **kw):
    return {"file": f"{FOOT}/{name}", "in": at_in, **kw}

def loop_card(first, start, end):
    """Last card = first card, already fully built, so the Reel loops cleanly [U.121]."""
    els = [dict(e, at=start - 1.0) for e in first["elements"]]
    c = card(start, end, els, bg=first.get("bg"))
    return c

def cta(start, end, bg, extra=None):
    els = [head("WHICH DOOR\nIS YOURS?", at=start, size=120),
           serif("Comment LOCK → the 4-question quiz", start + 1.0, build="fade", size=48)]
    if extra: els.append(serif(extra, start + 1.6, build="fade", size=40, gap=24))
    return card(start, end, els, bg=bg)

def save(slug, spec):
    spec = {**BASE, **spec}
    with open(os.path.join(OUT, slug + ".json"), "w") as f:
        json.dump(spec, f, indent=1, ensure_ascii=False)
        f.write("\n")

# Footage: AI-generated faceless POV clips (Higgsfield: Nano Banana Pro stills -> Kling 3.0), one consistent
# person/desk/phone, graded together; see assets/footage/lock-in/week2/README.md. Clip lengths: 01 5.0 s, 02 5.0 s,
# 03 4.2 s, 04 8.1 s (bed 0-5.0, hallway 5.0-8.1), 05_night 3.2 s. "in"/"rate" are set so no clip loops.
NIGHT = clip("05_lockin_night.mov", 0, rate=0.9)

# ---- Door 1 · BORED (writing -> the hand drifts to the phone)
c0 = card(0, 2.5, [head("20 MINUTES IN,", at=-0.12), head("IT GOES FLAT.", "amber", 1.3, "slam", gap=10)], 1.3,
          clip("01_bored.mov", 0))
save("09-door-1-bored", {"duration": 10.5, "cards": [
    c0,
    card(2.5, 5.0, [serif("your hand goes to the phone\nbefore you decide to.", 2.5, dur=1.2, size=68)],
         bg=clip("01_bored.mov", 2.5, rate=0.9)),
    card(5.0, 7.0, [head("DOOR 1:", at=5.0, size=110), head("BORED.", "amber", 5.6, "slam", size=170, gap=6)], 5.6),
    cta(7.0, 9.5, NIGHT, "part 1 of 4 · the fix is in the quiz"),
    loop_card(c0, 9.5, 10.5)],
    "sfx": [{"t": 0.0, "type": "lock", "gain": 0.9}, {"t": 9.5, "type": "lock", "gain": 0.9}]})

# ---- Door 2 · STUCK (blank page -> reaching to shut the laptop); the fix is the quiz's own STUCK result
c0 = card(0, 2.5, [head("YOU DIDN'T GET", at=-0.12), head("DISTRACTED.", "amber", 1.2, "slam", gap=10)], 1.2,
          clip("02_stuck.mov", 0, rate=0.9))
save("11-door-2-stuck", {"duration": 13.5, "cards": [
    c0,
    card(2.5, 4.5, [head("YOU GOT", at=2.5), head("STUCK.", "amber", 3.1, "slam", size=170, gap=6)], 3.1),
    card(4.5, 7.5, [serif("you hit something\nyou can't do.", 4.5, dur=1.0, size=66),
                    serif("\"i'll ask someone tomorrow.\"", 5.9, dur=0.9, size=66)],
         bg=clip("02_stuck.mov", 2.25, rate=0.9)),
    card(7.5, 10.5, [head("THE FIX:", "amber", 7.5, size=110),
                     serif("the step is too big,\nnot beyond you.\ncome back with the next line,\nnot the whole problem.",
                           8.0, build="lines", dur=1.6, size=62)]),
    cta(10.5, 12.5, NIGHT, "part 2 of 4"),
    loop_card(c0, 12.5, 13.5)],
    "sfx": [{"t": 0.0, "type": "lock", "gain": 0.9}, {"t": 12.5, "type": "lock", "gain": 0.9}]})

# ---- Door 3 · ANXIOUS (restless scrolling; the repeat on card 3 is the loop)
c0 = card(0, 2.5, [head("CHECKING ISN'T", at=-0.12), head("RELIEF.", "amber", 1.3, "slam", size=160, gap=6)], 1.3,
          clip("03_anxious.mov", 0))
save("13-door-3-anxious", {"duration": 12.5, "cards": [
    c0,
    card(2.5, 4.5, [head("IT'S THE", at=2.5), head("LOOP.", "amber", 3.1, "slam", size=170, gap=6)], 3.1,
         clip("03_anxious.mov", 2.5, rate=0.85)),
    card(4.5, 7.0, [serif("you feel behind\nbefore you've even started.", 4.5, dur=1.2, size=68)],
         bg=clip("03_anxious.mov", 0, rate=0.9)),
    card(7.0, 9.0, [head("DOOR 3:", at=7.0, size=110), head("ANXIOUS.", "amber", 7.6, "slam", size=160, gap=6),
                    serif("the one nobody admits.", 8.2, build="fade", size=52)], 7.6),
    cta(9.0, 11.5, NIGHT, "send this to whoever's always \"so behind\""),
    loop_card(c0, 11.5, 12.5)],
    "sfx": [{"t": 0.0, "type": "lock", "gain": 0.9}, {"t": 11.5, "type": "lock", "gain": 0.9}]})

# ---- Door 4 · TIRED (23:40 in bed -> the phone left outside the bedroom)
c0 = card(0, 2.5, [head("\"I'LL DO IT PROPERLY", at=-0.12, size=110), head("IN THE MORNING.\"", "amber", 1.4, "slam", size=110, gap=6)], 1.4,
          clip("04_tired.mov", 0))
save("14-door-4-tired", {"duration": 11.0, "cards": [
    c0,
    card(2.5, 5.0, [serif("it's after 10.\nyou're fading.\nso you open the phone.", 2.5, build="lines", dur=1.5, size=68)],
         bg=clip("04_tired.mov", 2.5)),
    card(5.0, 7.5, [head("DOOR 4:", at=5.0, size=110), head("TIRED.", "amber", 5.6, "slam", size=170, gap=6),
                    serif("you are solving sleep with a screen.", 6.3, build="fade", size=50)], 5.6,
         clip("04_tired.mov", 5.0, rate=1.0)),
    cta(7.5, 10.0, NIGHT, "part 4 of 4"),
    loop_card(c0, 10.0, 11.0)],
    "sfx": [{"t": 0.0, "type": "lock", "gain": 0.9}, {"t": 10.0, "type": "lock", "gain": 0.9}]})

# ---- Trial A · H.16 Cognitive Contradiction (clip bank #10 "Start tonight, not Monday", #14 "you'll start monday")
save("10-trial-dont-wait-for-monday", {"duration": 8.0, "trial": True, "cards": [card(0, 8.0, [
    head("DON'T WAIT", at=-0.12), head("FOR MONDAY.", "amber", 1.2, "slam", gap=6),
    serif("you said that last monday.", 2.5, dur=0.9, size=66),
    head("START TONIGHT.", "cream", 4.2, "slam", size=110, gap=50),
    serif("20 minutes. phone in another room.\nComment LOCK → find your door", 5.4, build="fade", size=46)], 1.2)],
    "sfx": [{"t": 0.0, "type": "lock", "gain": 0.9}]})

# ---- Trial B · H.fomo + H.6 hidden cost (clip bank #02 "Fake work", #12, #16, #17)
save("12-trial-fake-work", {"duration": 10.0, "trial": True, "cards": [card(0, 10.0, [
    head("NO ONE TELLS YOU", at=-0.12, size=120), head("ABOUT FAKE WORK.", "amber", 1.3, "slam", size=120, gap=6),
    serif("rewriting the same notes.\nmaking a timetable\ninstead of starting.\nopening 14 tabs to \"research\".", 2.6, build="lines", dur=2.4, size=54, gap=50),
    serif("it feels like work. it isn't.", 6.0, dur=0.9, size=62, gap=50),
    serif("Comment LOCK → find your door", 7.6, build="fade", size=46)], 1.3)],
    "sfx": [{"t": 0.0, "type": "lock", "gain": 0.9}]})
print("specs written:", sorted(os.listdir(OUT)))
