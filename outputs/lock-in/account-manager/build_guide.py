#!/usr/bin/env python3
"""Builds the LOCK IN account-manager guide (prompts/account-manager-guide.md) as HTML (for the Google Doc)
and Markdown (repo copy). Captions come verbatim from outputs/lock-in/posting-queue/clips.json.
Run from the repo root: python3 outputs/lock-in/account-manager/build_guide.py"""
import html, json, os

OUT = "outputs/lock-in/account-manager"
PAGE = "https://claude.ai/artifact/M5LcUCfMyBPWQwYfG9Ynig"
DRIVE = "https://drive.google.com/drive/folders/1aymnlDOmVajd6opoJArAWJ14VzP_SFnr"
TRACKER = "https://claude.ai/artifact/ELpGTnN5BdEksgu9QQSoLY"
QUIZ = "https://lockin-quiz.netlify.app"
GAME = "https://lockin-30.netlify.app"
DM_TEXT = "Here's the quiz → https://lockin-quiz.netlify.app. Four questions, about a minute. Tell me which door you got."

clips = [c for c in json.load(open("outputs/lock-in/posting-queue/clips.json")) if c.get("week") != "setup"]
AI = {9, 11, 14, 15} | {c["n"] for c in clips if c["week"] == 3}      # posts with AI-generated footage or photos
TRIAL = {10, 13, 17, 20}
NEW_DOOR = {9, 11, 14, 15}                                              # Drive copies are the old text versions

STORIES = {
    0: "Before Day 1: post the 4 START HERE intro Stories (Page setup kit), add a Link sticker to the quiz on Story 4, then save all 4 to the START HERE highlight.",
    1: "Post the 6 Day 1 Stories (Page setup kit), in order. Stickers: Poll on Story 1 (\"Where is your phone?\"), Emoji slider on Story 3, reshare the Four Doors Reel on Story 4, Quiz sticker (Door 1 / 2 / 3 / 4) on Story 5, Link sticker to the quiz on Story 6.",
    2: "Morning: Question box \"What's the one thing you'll do tonight?\". Evening: reshare the Day 2 Reel.",
    3: "7 pm: Poll \"You sat down yet?\" (Yes / Not yet). 11:40 pm: Poll \"Still on it?\". Reshare the Day 3 Reel.",
    4: "Share 3 slides of the carousel as Stories. Quiz sticker \"Where was your phone today?\" (Hand / Face down / Desk / Another room). Link sticker to the quiz.",
    5: "Run a real 20-minute session: post a Countdown sticker called \"Minute two\" at the start, and a screenshot of the finished timer at the end.",
    6: "Emoji slider \"How many days was your longest streak?\". Reshare the Day 6 Reel. Text Story: \"Never miss twice.\"",
    7: "Night: Poll \"Phone going to another room now. Who's in?\". Then a faceless photo of the phone outside the room, with a Link sticker to the quiz.",
    8: "Share 3 slides of What's Inside as Stories with the text \"pinned to the top\". Link sticker to the quiz.",
    9: "Poll \"20 minutes in. Where's your hand?\" (Book / Phone). Reshare the Door 1 Reel.",
    10: "Morning: Question box \"What are you starting tonight?\". Evening: a faceless photo of the phone outside the room.",
    11: "Reshare the Door 2 Reel. Quiz sticker \"What makes you stuck most?\" (Maths / Writing / Memorising / Starting).",
    12: "Share 3 slides of The 3 Ugly Minutes as Stories. Emoji slider \"How ugly is minute two?\".",
    13: "Text Story \"Door 3 people, this one's for you\", then reshare the Door 3 Reel. Anonymous Question box \"What are you behind on?\".",
    14: "Reshare the Door 4 Reel with \"All four doors are out. Which is yours?\" and a Quiz sticker (the 4 doors) plus a Link sticker to the quiz. Night: \"Phone going outside the bedroom now. Who's in?\".",
    15: "Poll \"Block 1 tonight. Who's in?\" (In / Tomorrow) on a still from today's Reel. Reshare the Reel.",
    16: "Emoji slider \"How many blocker apps have you deleted and reinstalled?\". Only reshare the Trial Reel once it has been shared to followers.",
    17: "Share slides 2, 4 and 6 of the carousel as Stories with \"Screenshot step 5\". Link sticker to the quiz.",
    18: "Text Story \"Who notices when you stop?\" with a Question box \"Who's your one person?\".",
    19: "\"Guess your door before the quiz\" with a Quiz sticker (the 4 doors) and a Link sticker to the quiz.",
    20: "Morning: \"Morning people?\". Night: \"Night people?\". Use one Poll (Morning / Night) on each.",
    21: "Question box \"Your 3 priorities for this week. Go.\" on a still from today's Reel.",
}


def esc(s):
    return html.escape(s, quote=False)


def where(c):
    name = os.path.basename(c.get("file") or c.get("zip") or "")
    if c["type"] == "carousel":
        folder = name.replace(".zip", "")
        return (f"Drive → Clips → folder {folder}" if c["week"] < 3 else "Posting-queue page → Week 3 (Save all slides)")
    if c["n"] in NEW_DOOR:
        return f"Posting-queue page → {name} (the Drive copy is an old version: replace it)"
    return f"Drive → Clips → {name}" if c["week"] < 3 else f"Posting-queue page → {name}"


H, M = [], []                                   # html parts, markdown parts


def h(tag, text, md_prefix):
    H.append(f"<{tag}>{esc(text)}</{tag}>"); M.append(f"{md_prefix} {text}\n")


def p(text, raw_html=None):
    H.append(f"<p>{raw_html if raw_html else esc(text)}</p>"); M.append(text + "\n")


def ol(items):
    H.append("<ol>" + "".join("<li>" + esc(i).replace("\n", "<br>") + "</li>" for i in items) + "</ol>")
    M.append("\n".join(f"{k}. {i}" for k, i in enumerate(items, 1)) + "\n")


def ul(items):
    H.append("<ul>" + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>")
    M.append("\n".join(f"- {i}" for i in items) + "\n")


def table(head, rows):
    th = "".join(f"<th>{esc(x)}</th>" for x in head)
    tr = "".join("<tr>" + "".join(f"<td>{esc(str(x))}</td>" for x in r) + "</tr>" for r in rows)
    H.append(f'<table border="1" cellpadding="6" style="border-collapse:collapse">{"<tr>" + th + "</tr>"}{tr}</table>')
    M.append("| " + " | ".join(head) + " |\n|" + "---|" * len(head) + "\n" + "\n".join("| " + " | ".join(str(x) for x in r) + " |" for r in rows) + "\n")


def link(label, url):
    return f'<a href="{url}">{esc(label)}</a>'


# ---------------------------------------------------------------- 1
h("h1", "LOCK IN: account manager guide", "#")
p("Everything you need to set up the LOCK IN Instagram page and post every planned post, step by step. Follow it in order. If something here doesn't match what you see in the app, message the owner before improvising.")
h("h2", "Start here", "##")
p("LOCK IN is a faceless Instagram account for people aged about 16 to 26 in Europe and the US who lose their evenings to doom scrolling. It sells a $15 e-book on discipline, but the account's job this month is audience first: reach new people, get them to watch to the end, send and save the posts, and comment LOCK to get a free 4-question quiz. The quiz leads to the book.")
p("Your job: post one thing a day at 18:05 UK time, post Stories every day, answer every comment and LOCK message within the hour, and log the numbers.")
p("The four links you'll use:")
H.append("<ul>"
         f"<li>{link('Posting-queue page', PAGE)}: every post with one-tap Save and Copy caption, plus the Page setup kit.</li>"
         f"<li>{link('Drive posting-queue folder', DRIVE)}: this guide, plus the weeks 1 and 2 files in the Clips folder.</li>"
         f"<li>{link('Tracker', TRACKER)}: where you log each post's numbers.</li>"
         f"<li>{link('The quiz', QUIZ)}: the link you send to everyone who comments LOCK.</li></ul>")
M.append(f"- Posting-queue page: {PAGE}\n- Drive posting-queue folder: {DRIVE}\n- Tracker: {TRACKER}\n- The quiz: {QUIZ}\n")

# ---------------------------------------------------------------- 2
h("h2", "Your daily routine", "##")
p("Post time is 18:05 UK (19:05 Central Europe, 13:05 US Eastern). Don't post more than one Reel a day.")
table(["When", "What to do"], [
    ["17:50", "Spend 10 minutes leaving real comments (a full sentence, not an emoji) on 5 to 10 study or discipline accounts."],
    ["18:00", "Open the posting-queue page, find today's post, tap Save, then Copy caption."],
    ["18:05", "Post it (see How to post). Double-check the AI label and Trial settings in the calendar."],
    ["18:05 to 19:05", "Stay in the app. Reply to every comment. Send the quiz DM to everyone who comments LOCK."],
    ["During the day", "Post that day's Stories with one sticker. Reply to every sticker answer and DM within the hour."],
    ["48 hours later", "Log the post's numbers in the tracker."],
    ["Sunday", "Fill in the tracker's weekly row: followers, profile visits and link taps."],
])

# ---------------------------------------------------------------- 3
h("h2", "One-time page setup", "##")
p("Do all of this before posting Day 1. The images are on the posting-queue page, in the Page setup kit at the top. Copy caption on the first card copies the name, bio and link below.")
h("h3", "Account", "###")
ol([
    "Create the Instagram account. The handle isn't decided yet. Check which of these is free and ask the owner to choose: @lockin.system, @lockin.playbook, @locking101, @lockin.daily.",
    "Switch it to a professional account, type Creator: Settings → Account type and tools → Switch to professional account → Creator.",
    "Name field (Edit profile → Name): LOCK IN | Discipline System",
    "Bio (Edit profile → Bio), exactly three lines:\nDiscipline for people who doom-scroll.\nNot motivation. A setup that works when you don't feel like it.\nWhich door is yours? Free quiz ↓",
    f"Link (Edit profile → Links → Add external link): {QUIZ}",
    "Profile photo: image 1 of the Profile kit (LOCK / IN on dark).",
    "Before Day 1, ask someone in the UK, Europe or the US to open the quiz link on their phone and confirm it loads.",
])
h("h3", "The LOCK auto-reply", "###")
p("Every post ends with \"Comment LOCK\". Everyone who does must get this message in their DMs, word for word:")
p(DM_TEXT, f"<b>{esc(DM_TEXT)}</b>")
ol([
    "Best: set up a keyword auto-DM tool that connects to Instagram (for example ManyChat) with the keyword LOCK and the message above. Test it from a second phone before Day 1.",
    "Also save the message as a Saved reply (Settings → Business tools / Creator tools → Saved replies, shortcut: lock), so you can send it by hand in seconds if the tool fails.",
    "Reply to the comment itself too, for example: \"Sent, check your DMs.\"",
])
h("h3", "Highlights", "###")
ol([
    "Post the 4 START HERE intro Stories (Page setup kit), in order. Add a Link sticker to the quiz on Story 4, inside the dashed box.",
    "On your profile, tap New (the + under the bio), select those 4 Stories, name the highlight START HERE, and set the cover to image 2 of the Profile kit (GO).",
    "Create the other highlights once there's something to put in them, in this order: THE SYSTEM (cover 4: reshare every how-it-works Reel and carousel), THE BOOK (cover 61: What's Inside slides, price $15 one time, link sticker), 30 DAYS (cover 30: how the 30-day challenge works). Covers are images 3, 4 and 5 of the Profile kit.",
    "Add the Day 17 carousel and The 3 Ugly Minutes to THE SYSTEM when they go out.",
])
h("h3", "Pinned posts", "###")
p("After Day 8, pin three posts (open the post → … → Pin to your profile): What's Inside LOCK IN (Day 8), Four Doors (Day 1), and You don't need discipline (Day 2). After week 1, the owner may swap slot 1 for the best performer.")

# ---------------------------------------------------------------- 4
h("h2", "How to post", "##")
h("h3", "A Reel", "###")
ol([
    "On the posting-queue page, find the post and tap Save. On iPhone choose Save Video. Then tap Copy caption.",
    "In Instagram tap + → Reel, and pick the video from your gallery.",
    "Don't add filters, text, stickers or music. The video already has its text and sound. Tap Next.",
    "Paste the caption. Check it's complete, with the hashtags at the end.",
    "Tap Edit cover and pick the frame where the orange (amber) word has fully appeared, about 2 seconds in.",
    "Only if the calendar says AI label: Yes → open Advanced settings and turn on Add AI label.",
    "Only if the calendar says Trial: Yes → turn on Trial (see Trial Reels below).",
    "Tap Share. Don't edit the caption or cover, and don't delete the post afterwards: that resets how Instagram tests it.",
])
h("h3", "A Trial Reel", "###")
p("A Trial Reel is shown to non-followers first, so you can test an idea without it appearing to your followers. Post it like a normal Reel with Trial switched on. After about 24 hours, compare its views with the week 1 median in the tracker. If it did better, open the Reel and choose Share to followers. Either way, log it and tick Trial Reel in the tracker.")
h("h3", "A carousel", "###")
ol([
    "On the posting-queue page tap Save all slides (a .zip file). Or tap each slide to save it as a photo, which is easiest on a phone.",
    "In Instagram tap + → Post, tap the multiple-select icon, and select the slides in number order (slide 1 first).",
    "Keep the 4:5 crop. Tap Next. Soft background music at low volume is fine, but it's optional.",
    "Paste the caption, turn on the AI label if the calendar says so, then tap Share.",
])
h("h3", "Stories and stickers", "###")
ol([
    "Tap + → Story and pick the image (or take a faceless photo, for example of the phone in another room).",
    "Tap the sticker icon and add the sticker named in the calendar: Poll, Quiz, Question, Emoji slider, Countdown or Link. For designed Story images, put it inside the dashed box.",
    f"For a Link sticker, paste {QUIZ}.",
    "Tap Your story. Reply to every answer within the hour.",
    "To reshare a Reel to Stories, open the Reel, tap the paper-plane icon, then Add to story.",
])

# ---------------------------------------------------------------- 5
h("h2", "Comments and DMs", "##")
ul([
    "Reply to every comment in the first hour after posting, with a real sentence.",
    "Comment says LOCK: send the quiz DM (auto or by hand), then reply to the comment \"Sent, check your DMs.\"",
    "Comment is a door number (1, 2, 3 or 4): ask what they were doing the last time it happened.",
    "Someone shares which door the quiz gave them: reply with that door's fix, word for word. Bored: It's withdrawal. It passes in about ninety seconds. Look at the clock and keep writing. Stuck: The step is too big, not beyond you. Come back with the next line, not the whole problem. Anxious: Fifteen minutes on Sunday, three priorities, then start. Tired: You're solving sleep with a screen. Tonight: phone outside the bedroom.",
    f"Someone buys the book: the buyers' game is at {GAME}. The unlock code is inside the book, so never post it publicly.",
    "Don't argue. Delete and report only spam or abuse.",
])

# ---------------------------------------------------------------- 6
h("h2", "Never do this", "##")
ul([
    "Buy followers, likes or views, or join engagement groups (pods).",
    "Use a second account to like, comment on or watch our posts.",
    "Write \"link in bio\" or \"buy now\" in a caption. The only call to action is \"Comment LOCK\".",
    "Invent results, reviews, testimonials or member numbers, or claim anything is running out when it isn't.",
    "Write \"tag a friend\" style bait. Our share lines always say who to send it to and why.",
    "Edit the caption or cover, or delete a post, after it's live.",
    "Repost other creators' content.",
    "Use hype words: grind, unstoppable, change your life forever.",
    "Post more than one Reel a day.",
])

# ---------------------------------------------------------------- 7
h("h2", "Tracking", "##")
ol([
    "Ask the owner for edit access to the tracker if the link doesn't let you type in it.",
    "When Day 1 (Four Doors) goes live, enter that date in the tracker as the start date.",
    "About 48 hours after each post, open Insights on the post and log: views, % of views from non-followers, average watch time, shares, saves, LOCK comments and follows.",
    "Every Sunday, fill in the weekly row: followers, profile visits and link taps.",
    "Tell the owner when a week is logged. The next week's posts are planned from these numbers.",
])

# ---------------------------------------------------------------- 8
h("h2", "The calendar", "##")
p("Days count from the day Four Doors goes live. Day 12 has two posts: the carousel first, then the Trial Reel. Before Day 9, replace posts 09, 11, 14 and 15 in Drive with the new versions from the posting-queue page (same file names): the Drive copies are old versions.")
table(["Day", "#", "Post", "Format", "Where the file is", "AI label", "Trial"],
      [[c["day"], f"{c['n']:02d}", c["title"], c["kind"].split(" · ")[0], where(c),
        "Yes" if c["n"] in AI else "No", "Yes" if c["n"] in TRIAL else "No"] for c in clips])

# ---------------------------------------------------------------- 9
h("h2", "Every post, ready to paste", "##")
p("The captions below are final. Paste them exactly; the posting-queue page's Copy caption button gives you the same text.")
p("Day 0 (before launch). Stories: " + STORIES[0])
for c in clips:
    h("h3", f"Day {c['day']} · #{c['n']:02d} · {c['title']}", "###")
    flags = [c["kind"].replace(" · turn on AI label", "")] + (["AI label: ON"] if c["n"] in AI else []) + (["Trial: ON"] if c["n"] in TRIAL else [])
    p("Format: " + " · ".join(flags))
    p("File: " + where(c))
    if c["type"] == "reel":
        p("Cover: the frame where the orange word has fully appeared, about 2 seconds in.")
    else:
        p("Cover: slide 1. Post the slides in number order.")
    H.append("<p><b>Caption:</b></p><p>" + "<br>".join(esc(l) for l in c["caption"].split("\n")) + "</p>")
    M.append("**Caption:**\n```\n" + c["caption"] + "\n```\n")
    if c["day"] in STORIES and not (c["day"] == 12 and c["type"] == "reel"):
        p("Stories today: " + STORIES[c["day"]])

# ---------------------------------------------------------------- 10
h("h2", "Where everything is", "##")
table(["What", "Where"], [
    ["Every post (Save + Copy caption), Page setup kit", PAGE],
    ["Weeks 1 and 2 files", DRIVE + " → Clips"],
    ["This guide", DRIVE + " → 01 · Account manager guide (LOCK IN)"],
    ["Tracker", TRACKER],
    ["Quiz (bio link, LOCK DMs)", QUIZ],
    ["Buyers' game (for book buyers only)", GAME],
])
p("New weeks are added to the posting-queue page and to this guide as they're made.")

os.makedirs(OUT, exist_ok=True)
open(f"{OUT}/account-manager-guide.html", "w").write("<html><body>" + "\n".join(H) + "</body></html>")
open(f"{OUT}/account-manager-guide.md", "w").write("\n".join(M))
print("posts:", len(clips), "html bytes:", len(open(f'{OUT}/account-manager-guide.html').read()))
