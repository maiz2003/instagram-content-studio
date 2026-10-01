#!/usr/bin/env python3
"""Builds the LOCK IN auto-reply setup kit (prompts/auto-reply-setup.md) as HTML (Google Doc) and Markdown.
The DM text comes from the approved script; the door fixes come from the game's CONFIG.
Run from the repo root: python3 outputs/lock-in/auto-reply/build_kit.py"""
import html, os, re

OUT = "outputs/lock-in/auto-reply"
QUIZ = "https://lockin-quiz.netlify.app"
GUIDE = "https://docs.google.com/document/d/1K_aSaWkQAkXMPNxMRpaBRj2TAKQNq1bLMM9eb8JPi5U/edit"
PAGE = "https://lockin-queue-fabacc3e.netlify.app"
TRACKER = "https://claude.ai/artifact/ELpGTnN5BdEksgu9QQSoLY"

script = open("outputs/lock-in/2026-09-26-phone-not-discipline/script.md").read()
DM = re.search(r"DM auto-reply text[^\n]*\n\s*> ([^\n]+)", script).group(1).strip()
cfg = open("products/lock-in-30/index.html").read()
FIX = dict(re.findall(r"^\s{4}(Bored|Stuck|Anxious|Tired): \"(.+?)\",?$", cfg, re.M))
assert DM and len(FIX) == 4, (DM, FIX)
DOORS = [("1", "Bored"), ("2", "Stuck"), ("3", "Anxious"), ("4", "Tired")]
DOOR_MSG = {n: f"{name}, door {n}. The fix: {FIX[name]}" for n, name in DOORS}
COMMENT_REPLIES = ["Sent. Check your DMs (and your message requests).",
                   "On its way. Check your DMs, message requests too.",
                   "Just sent it. Look in your DMs or message requests."]
HANDOFF_NOTE = "Thanks for the message. I'm a real person behind this account, and I'll reply as soon as I can."

H, M = [], []
esc = lambda s: html.escape(s, quote=False)
def h(tag, t, md): H.append(f"<{tag}>{esc(t)}</{tag}>"); M.append(f"{md} {t}\n")
def p(t, raw=None): H.append(f"<p>{raw or esc(t)}</p>"); M.append(t + "\n")
def ol(items): H.append("<ol>" + "".join("<li>" + esc(i).replace("\n", "<br>") + "</li>" for i in items) + "</ol>"); M.append("\n".join(f"{k}. {i}" for k, i in enumerate(items, 1)) + "\n")
def ul(items): H.append("<ul>" + "".join("<li>" + esc(i).replace("\n", "<br>") + "</li>" for i in items) + "</ul>"); M.append("\n".join(f"- {i}" for i in items) + "\n")
def table(head, rows):
    th = "".join(f"<th>{esc(x)}</th>" for x in head)
    tr = "".join("<tr>" + "".join(f"<td>{esc(str(x)).replace(chr(10), '<br>')}</td>" for x in r) + "</tr>" for r in rows)
    H.append(f'<table border="1" cellpadding="6" style="border-collapse:collapse"><tr>{th}</tr>{tr}</table>')
    M.append("| " + " | ".join(head) + " |\n|" + "---|" * len(head) + "\n" + "\n".join("| " + " | ".join(str(x).replace("\n", " / ") for x in r) + " |" for r in rows) + "\n")
def msg(label, text):
    H.append(f"<p><b>{esc(label)}</b></p><p>{esc(text)}</p>"); M.append(f"**{label}**\n\n> {text}\n")

h("h1", "LOCK IN: auto-reply setup", "#")
p("How to set up the automatic reply for everyone who comments LOCK, test it, and keep it running. Follow it in order. If a screen in a tool looks different from what's described here, trust the screen and keep the same settings.")

h("h2", "What this does", "##")
p("Every post ends with \"Comment LOCK\". The auto-reply turns each of those comments into a quiz in the person's DMs within seconds, even at 3 am, so nobody waits for you.")
ol([
    "Someone comments LOCK on any post or Reel.",
    "The tool replies to their comment in public and sends them a DM with the quiz link.",
    "If they answer with their door, the tool sends that door's fix. Anything else goes to you.",
])
p("Your job: connect it once, test it, switch it on before Day 1, check it every day, and answer the people it hands over to you. You still reply to every real comment yourself.")

h("h2", "Before you start", "##")
ul([
    "The Instagram account must be a professional (Creator) account. The page setup in the account manager guide already covers that.",
    "Who connects the account: the owner, or you with the owner's permission. Connecting means logging in through the tool's own Instagram screen and approving access.",
    "Never type the Instagram password into any tool or send it to anyone. Use only tools that connect through the official Instagram login screen. A tool that asks for your password is not safe. Stop and tell the owner.",
    "Have the DM text and replies from the section Every message, ready to paste open in another tab.",
    "Do all of this before posting Day 1.",
])

h("h2", "Pick the tool", "##")
p("Recommendation: use a tool built on Instagram's official connection that supports a comment keyword trigger. ManyChat is the most common one. Check the current plan and price on its own site before signing up. A free plan may be enough to start, but plans and limits change.")
table(["Option", "What it does", "When to use it"], [
    ["ManyChat (recommended)", "Comment keyword → public reply → DM, with test mode and stats.", "The main setup. This kit describes it."],
    ["Another official-connection tool", "Does the same job with different screens.", "If the owner already uses one. Use the same settings."],
    ["Instagram's own tools", "Saved replies, a greeting, and any automations Instagram offers in Settings → Creator tools or Business tools. Check whether it offers a comment keyword trigger.", "If Instagram's own option supports the trigger, it can replace a third-party tool. Otherwise use it only for the backup below."],
    ["By hand", "You watch for comments and send the DM from a saved reply.", "The backup. Also what to do while the tool is being set up."],
])

h("h2", "Build the flow, step by step", "##")
p("The names below follow ManyChat. Other tools use the same ideas with different labels.")
h("h3", "1. Connect the account (once)", "###")
ol([
    "Sign up for the tool with the owner's email or a shared brand email.",
    "Choose Instagram as the channel and tap Connect Instagram. Log in on the official Instagram screen and approve. If the tool asks you to link a Facebook Page, follow its screen. Ask the owner if you don't have one.",
    "If the tool says it can't send messages, open Instagram → Settings → Messages and story replies → Connected tools (the label may differ) and switch on Allow access to messages.",
    "Tell the owner which tool you used, which email it is under and the date, so they can find it later.",
])
h("h3", "2. Create the comment flow", "###")
ol([
    "Create a new automation and name it: LOCK → quiz.",
    "Trigger: an Instagram comment. Choose Any post or Reel (current and future), so every new post works without touching the flow again.",
    "Keyword: LOCK. Set it to match the whole word and to ignore capital letters. Don't use \"contains\" matching, because \"block\" and \"clock\" contain \"lock\". If the tool only offers \"contains\", add a filter that requires spaces or punctuation around the word, or tell the owner.",
    "Add a public comment reply. If the tool allows several, add all three variants from Every message, ready to paste, so the replies don't look identical.",
    "Add the DM message with the quiz text and link.",
    "Add a limit: one run per person per day. This stops repeated comments from sending repeated messages.",
])
h("h3", "3. Create the DM keyword trigger", "###")
ol([
    "Create a second automation: LOCK by DM.",
    "Trigger: an incoming Instagram DM containing the word LOCK (whole word).",
    "Action: send the same DM text. Same one-per-day limit.",
    "This catches people who message you the word instead of commenting it.",
])
h("h3", "4. Add the door replies (optional, recommended)", "###")
ol([
    "Create a third automation: Door fix.",
    "Trigger: an incoming DM that contains a door name (Bored, Stuck, Anxious, Tired) or a number 1 to 4 on its own.",
    "Action: send that door's fix from Every message, ready to paste. One rule for each door.",
    "Only run it for people who received the quiz DM in the last 24 hours, if the tool can filter that. If it can't, keep the rule anyway: the replies are harmless.",
])
h("h3", "5. Hand anything else to a human", "###")
ol([
    "For any other incoming DM, don't send an automatic reply. Turn on the tool's notification to your phone or email for new messages that didn't match a rule.",
    "Optional: send the holding message from Every message, ready to paste, once per person per day.",
])
h("h3", "6. Turn it on", "###")
ol([
    "Finish the test below first.",
    "Switch each automation from Draft to Live.",
    "Tell the owner the date it went live.",
])

h("h2", "Every message, ready to paste", "##")
H.append("<p><b>Public comment reply (use all three, rotated)</b></p>"); M.append("**Public comment reply (use all three, rotated)**\n")
ol(COMMENT_REPLIES)
msg("The DM (sent for every LOCK)", DM)
for n, name in DOORS:
    msg(f"Door reply: {name} (the person sends \"{name}\" or \"{n}\")", DOOR_MSG[n])
msg("Holding message (for anything else, optional)", HANDOFF_NOTE)
p("Don't change these. The DM text and the fixes are the approved words. If they need to change, ask the owner, and the change is made in one place and copied here.")

h("h2", "Test before Day 1", "##")
p("Test with a friend's real Instagram account, or with the tool's own test mode. Never comment from a second account of your own on your own posts: that counts as fake engagement and isn't allowed.")
table(["#", "Test", "Pass if"], [
    ["1", "A friend comments LOCK on a test post (or the tool's test mode does).", "Within 30 seconds a public reply appears, and the DM arrives (check message requests if they don't follow the account)."],
    ["2", "They comment lock in small letters, and Lock.", "Same result."],
    ["3", "They comment the word block, and the word clock.", "No reply, no DM. If either sends one, the keyword is matching part of a word: fix it (step 2 of the flow)."],
    ["4", "They comment LOCK twice in a row.", "Only one DM."],
    ["5", "They open the DM and tap the quiz link.", "The quiz opens. (Also ask someone in the UK or the US to check.)"],
    ["6", "They reply Bored, then 2.", "They get the Bored fix, then the Stuck fix."],
    ["7", "They send any other message, for example \"hello\".", "No automatic reply (or only the holding message), and you get a notification."],
    ["8", "They message the word LOCK in DM.", "They get the quiz DM."],
    ["9", "Delete the test comments afterwards.", "The test post is clean."],
])

h("h2", "Daily check and tracking", "##")
ol([
    "Every day, open the tool and look at the last 24 hours: comments matched, DMs sent, and any errors.",
    "Compare it with the post's LOCK comments. If people commented and the DM count is lower, something failed. See If something goes wrong.",
    "Answer every message the tool handed to you within the hour.",
    "Log the LOCK comments and quiz link taps for each post in the tracker, 48 hours after it goes live. The link is in the account manager guide.",
    "Once a week, read a few of the DMs as they were sent. Make sure the text still looks right and the link still works.",
])

h("h2", "If something goes wrong", "##")
table(["What you see", "Do this"], [
    ["No DMs are going out.", "Open the tool and check that Instagram is still connected. The connection can expire and ask you to log in again. Reconnect through the official screen."],
    ["People say they got no DM.", "Ask them to look in message requests. If it's there, add \"check message requests\" to the public reply (already in the replies above)."],
    ["The tool stops at its free limit.", "Tell the owner. Until it's fixed, use the backup below."],
    ["A test or a real person gets the DM twice.", "Check the one-per-day limit on each automation."],
    ["Someone replies with a question or a complaint.", "Answer it yourself, in your own words, politely. Never paste the auto text as an answer."],
])
p("Backup when the tool is down: save the DM as a Saved reply in Instagram (shortcut: lock). When someone comments LOCK, send that saved reply by hand, and reply to their comment with one of the three public replies. Do it within the hour.")

h("h2", "Never do this", "##")
ul([
    "Give an Instagram password to any tool or person.",
    "Comment from a second account of your own to test or boost posts.",
    "Send a second or third message to someone who didn't answer. One message per person per day.",
    "Put a purchase link or \"buy now\" in the first DM. The DM sends the quiz. The quiz leads to the book.",
    "Say anything is running out, or invent results, reviews or numbers.",
    "Change the approved DM text or fixes without asking the owner.",
])
p("Related links: the account manager guide, the posting queue page and the tracker.",
  f'Related links: <a href="{GUIDE}">account manager guide</a>, <a href="{PAGE}">posting queue page</a>, <a href="{TRACKER}">tracker</a>.')

os.makedirs(OUT, exist_ok=True)
open(f"{OUT}/auto-reply-setup.html", "w").write("<html><body>" + "\n".join(H) + "</body></html>")
open(f"{OUT}/auto-reply-setup.md", "w").write("\n".join(M))
print("ok", len("\n".join(H)), "bytes;", DM)
