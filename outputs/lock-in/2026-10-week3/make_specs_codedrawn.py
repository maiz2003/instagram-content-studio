#!/usr/bin/env python3
"""Code-drawn versions of the week-3 Reels, for comparison with the AI-footage versions (run from the repo root).

Same text, timing and sound as reels/*.json; the AI footage is removed and each card gets a line graphic that
draws itself on (reel.js "draw" build). No AI imagery, so no AI label needed. Output: reels-codedrawn/*.json
"""
import json, os

SRC = "outputs/lock-in/2026-10-week3/reels"
OUT = "outputs/lock-in/2026-10-week3/reels-codedrawn"
os.makedirs(OUT, exist_ok=True)

CREAM, AMBER, GREY, RULE = "#E6E1D5", "#DA9D55", "#8f949c", "#2a2d33"
S = 'fill="none" stroke-linecap="round" stroke-linejoin="round" pathLength="1"'


def svg(body, h=520):
    return f'<svg width="900" height="{h}" viewBox="0 0 900 {h}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'


def line(d, c=CREAM, w=7):
    return f'<path d="{d}" stroke="{c}" stroke-width="{w}" {S}/>'


def text(x, y, t, size=64, c=CREAM, font="Anton", anchor="middle"):
    return f'<text class="f" x="{x}" y="{y}" fill="{c}" font-family="{font}" font-size="{size}" text-anchor="{anchor}" style="opacity:0">{t}</text>'


def rrect(x, y, w, h, r, c=CREAM, sw=7):
    return line(f"M{x+r},{y} H{x+w-r} A{r},{r} 0 0 1 {x+w},{y+r} V{y+h-r} A{r},{r} 0 0 1 {x+w-r},{y+h} H{x+r} "
                f"A{r},{r} 0 0 1 {x},{y+h-r} V{y+r} A{r},{r} 0 0 1 {x+r},{y} Z", c, sw)


def circle(cx, cy, r, c=CREAM, sw=7):
    return line(f"M{cx},{cy-r} A{r},{r} 0 1 1 {cx-0.01},{cy-r}", c, sw)


def tick(x, y, s=1.0, c=AMBER):
    return line(f"M{x},{y} l{28*s},{28*s} l{52*s},{-62*s}", c, 9)


def phone(x, y, w=170, h=320, c=CREAM):
    return rrect(x, y, w, h, 28, c) + line(f"M{x+w/2-22},{y+22} h44", c, 6)


def door(x, y, w=170, h=320, c=CREAM, open_=False):
    g = rrect(x, y, w, h, 6, c) + circle(x + w - 34, y + h / 2, 9, c, 6)
    if open_:
        g += line(f"M{x+w},{y} L{x+w+70},{y+40} V{y+h-40} L{x+w},{y+h}", AMBER)
    return g


def arrow(x1, y, x2, c=AMBER):
    return line(f"M{x1},{y} H{x2} M{x2-34},{y-26} L{x2},{y} L{x2-34},{y+26}", c)


# ---------- the graphics ----------
def three_blocks(ticked):
    g = ""
    for i in range(3):
        x = 80 + i * 270
        g += rrect(x, 120, 200, 200, 22, AMBER if ticked else CREAM)
        if ticked:
            g += tick(x + 52, 220, 1.3)
    return svg(g + text(450, 420, "20 · 20 · 20", 54, GREY, "JetBrains Mono"), 470)


def timer():
    g = circle(450, 260, 210, RULE, 10) + line("M450,50 A210,210 0 1 1 249.6,197.4", AMBER, 12)
    for a in range(12):
        import math
        r1, r2 = 228, 250
        ang = math.radians(a * 30 - 90)
        g += line(f"M{450+r1*math.cos(ang):.1f},{260+r1*math.sin(ang):.1f} L{450+r2*math.cos(ang):.1f},{260+r2*math.sin(ang):.1f}", GREY, 5)
    return svg(g + text(450, 300, "20:00", 110, CREAM), 520)


def calendar():
    g, k = "", 0
    for r in range(4):
        for c in range(7):
            x, y = 95 + c * 102, 40 + r * 102
            g += rrect(x, y, 84, 84, 10, RULE, 4)
    for k in range(12):
        r, c = divmod(k, 7)
        x, y = 95 + c * 102, 40 + r * 102
        g += line(f"M{x+20},{y+20} L{x+64},{y+64} M{x+64},{y+20} L{x+20},{y+64}", CREAM, 6)
    g += circle(95 + 5 * 102 + 42, 40 + 1 * 102 + 42, 52, AMBER, 7)
    return svg(g + text(450, 500, "MISS ONE. NEVER TWO.", 46, GREY, "JetBrains Mono"), 520)


def phone_lock():
    return svg(phone(365, 60) + rrect(415, 230, 70, 60, 8, AMBER) + line("M428,230 v-22 a22,22 0 0 1 44,0 v22", AMBER), 420)


def phone_glow():
    g = phone(365, 80)
    for d in ("M330,120 l-60,-40", "M310,230 h-80", "M330,340 l-60,40", "M570,120 l60,-40", "M590,230 h80", "M570,340 l60,40"):
        g += line(d, AMBER, 6)
    return svg(g, 440)


def distance():
    return svg(phone(60, 80, 150, 280) + arrow(260, 220, 600) + door(650, 50, 180, 340, CREAM, True)
               + text(430, 450, "ANOTHER ROOM", 50, GREY, "JetBrains Mono"), 480)


def desk_alone():
    g = line("M90,380 H810", CREAM) + line("M160,380 v110 M740,380 v110", CREAM)
    g += line("M620,380 v-170 l-60,-40", GREY, 6) + line("M520,150 l90,-40 l30,60 z", AMBER, 6)
    g += rrect(250, 300, 230, 80, 8, CREAM, 6)
    return svg(g, 500)


def eye():
    g = line("M150,250 Q450,20 750,250 Q450,480 150,250 Z", CREAM) + circle(450, 250, 85, AMBER) + circle(450, 250, 25, AMBER, 9)
    return svg(g, 500)


def chat():
    g = line("M120,80 H780 a30,30 0 0 1 30,30 V330 a30,30 0 0 1 -30,30 H260 L170,430 L190,360 H120 a30,30 0 0 1 -30,-30 V110 a30,30 0 0 1 30,-30 Z", CREAM)
    return svg(g + text(450, 255, "DAY 4. YOU IN?", 92, AMBER), 460)


def four_doors(open_i=None):
    g = ""
    for i in range(4):
        x = 40 + i * 215
        g += door(x, 60, 150, 290, AMBER if i == open_i else CREAM, i == open_i)
        g += text(x + 75, 420, ["BORED", "STUCK", "ANXIOUS", "TIRED"][i], 40, AMBER if i == open_i else GREY, "JetBrains Mono")
    return svg(g, 450)


def questions_fix():
    g = ""
    for i in range(4):
        g += rrect(60 + i * 120, 170, 90, 90, 12, CREAM, 6) + text(105 + i * 120, 232, str(i + 1), 52, GREY)
    g += arrow(560, 215, 680) + rrect(710, 140, 150, 150, 20, AMBER) + tick(752, 222, 1.2)
    return svg(g, 420)


def sun_moon(strike=False):
    import math
    g = circle(250, 230, 90, AMBER)
    for a in range(8):
        ang = math.radians(a * 45)
        g += line(f"M{250+120*math.cos(ang):.1f},{230+120*math.sin(ang):.1f} L{250+160*math.cos(ang):.1f},{230+160*math.sin(ang):.1f}", AMBER, 6)
    g += line("M700,120 A115,115 0 1 0 760,330 A90,90 0 1 1 700,120 Z", CREAM)
    if strike:
        g += line("M80,430 L830,40", GREY, 10)
    return svg(g, 460)


def clock():
    return svg(circle(450, 250, 210, CREAM) + line("M450,250 V120", CREAM, 9) + line("M450,250 L560,320", AMBER, 9)
               + circle(450, 250, 10, AMBER, 8), 500)


def question_list():
    g = rrect(200, 40, 500, 420, 18, CREAM)
    for i in range(3):
        g += line(f"M260,{140+i*100} H640", RULE, 6)
    return svg(g + text(450, 330, "?", 220, AMBER), 500)


def priorities(ticked=0):
    g = rrect(160, 30, 580, 440, 18, CREAM)
    for i in range(3):
        y = 120 + i * 120
        g += rrect(220, y - 40, 70, 70, 10, AMBER if i < ticked else GREY, 6)
        g += line(f"M330,{y} H660", CREAM, 8)
        if i < ticked:
            g += tick(232, y - 8, 0.9)
    return svg(g, 500)


G = {  # slug → graphic per card index (CTA cards stay text-only; the loop card reuses card 0)
    "15-three-blocks": [three_blocks(False), timer(), three_blocks(True), calendar()],
    "16-trial-blocker-is-still-your-phone": [phone_lock(), phone_glow(), distance()],
    "18-someone-who-notices": [desk_alone(), eye(), chat()],
    "19-trial-not-for-motivation": [four_doors(), four_doors(2), questions_fix()],
    "20-morning-or-night": [sun_moon(), sun_moon(True), distance()],
    "21-fifteen-minutes-so-behind": [clock(), question_list(), priorities(0), priorities(1)],
}

for slug, graphics in G.items():
    spec = json.load(open(f"{SRC}/{slug}.json"))
    cards = spec["cards"]
    for i, c in enumerate(cards):
        c.pop("bg", None)
        c["top"] = 330
        g = graphics[i] if i < len(graphics) else (graphics[0] if i == len(cards) - 1 else None)
        if g:
            at = c["start"] + 0.35 if i < len(cards) - 1 else c["start"] - 2.0   # loop card: already drawn
            c["elements"].append({"svg": g, "build": "draw", "at": round(at, 2), "dur": 1.1, "gap": 70})
    spec.pop("trial", None)
    with open(f"{OUT}/{slug}.json", "w") as f:
        json.dump(spec, f, indent=1, ensure_ascii=False)
        f.write("\n")
print("code-drawn specs:", sorted(os.listdir(OUT)))
