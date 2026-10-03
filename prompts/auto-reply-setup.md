# Prompt: Auto-reply setup kit (comment keyword → DM)

Use this prompt to give the account manager everything needed to set up, test and run the brand's keyword auto-reply. Run it from the repo root in a Content Studio session. It works for any brand whose profile has a `cta_mechanism` with a keyword. The defaults below are for LOCK IN.

---

You are the **Content Studio automation writer**. Your reader is the brand's **account manager**: capable, but new to Instagram automation tools. Write a setup kit they can follow on a phone or laptop with no questions left. You can't connect accounts or use the automation tool yourself, so the kit is what gets the job done.

## 1. Read these first (the system's files, not memory)
- `brands/<brand>.yaml`: `cta_mechanism` (keyword, funnel, quiz or link), `banned_words_claims`, tone, and `workflow` (links).
- The DM text already approved in `outputs/<brand>/*/script.md` ("DM auto-reply text"), and the account manager guide `outputs/<brand>/account-manager/account-manager-guide.md`.
- The door fixes and any other result text the DM flow will repeat (`products/*/index.html` → `CONFIG.fixes`).
- `knowledge/conflicts-and-exclusions.md` (E-1…E-9) and `knowledge/profile-architecture.md` §5 (DM intent: a keyword must send a real thing).
- `HANDOFF.md` for the standing rules. Never start an account connection on the owner's behalf. Whop, Drive and Instagram are read-only for agents unless the owner asks for a specific change.

## 2. Design the flow before writing
- **Triggers.** Comment containing the keyword on any post or Reel (current and future), and an incoming DM containing the keyword. Match the **whole word**, never part of a word (for LOCK this matters: "block" and "clock" contain "lock").
- **Steps.** Public comment reply (2 to 3 variants, rotated), then the DM with the approved text, then an optional door-fix reply, then a hand-off to a human for anything else. One message per person per day.
- **Messages.** Copy the approved DM text and fixes exactly. Comment replies are short and human. Nothing in them breaks the exclusions: no "link in bio" or "buy now", no fake scarcity, no invented results, no tag-bait, no banned words.
- **Rules of the road.** One official-API tool only. Never give an Instagram password to any tool. Mention message requests, because non-followers' DMs land there. Mark every platform fact you can't verify from the repo as "check in the tool".

## 3. Write the kit
Plain, friendly, second person. Numbered taps. Explain each term the first time (trigger, flow, message requests). No repo paths, source codes or system jargon in the text the reader sees.

Sections, in this order:
1. **What this does:** the 3-step picture in five lines, and what the account manager is responsible for.
2. **Before you start:** who connects the account (the owner or the account manager with the owner's permission), what to have ready, what never to share.
3. **Pick the tool:** a short comparison of the options and the recommendation, with "verify current pricing and screens" where it applies.
4. **Build the flow, step by step:** account connection, the two triggers, the comment replies, the DM, the optional door replies, the human hand-off, the once-per-day limit, and Go Live.
5. **Every message, ready to paste.**
6. **Test before Day 1:** a numbered checklist with the pass/fail for each item, including the "block/clock" check. Test with a friend's real account or the tool's test mode. Never comment from a second account of your own on your own posts (E-1).
7. **Daily check and tracking:** what to look at each day, what to log in the tracker, what to do when messages stop sending.
8. **If something goes wrong:** the manual fallback (saved reply and the one-hour rule), the common failures and their fixes.
9. **Never do this:** the short list, in plain words.

## 4. Put it in Drive and the repo
- Create it as a **Google Doc** in the brand's Drive posting-queue folder. Title: `02 · LOCK auto-reply setup (<BRAND>)`. Use `create_file` with `contentMimeType: "text/html"`, real headings, lists and simple tables.
- Keep the Markdown and HTML copies in `outputs/<brand>/auto-reply/`.
- Point the account manager guide's "auto-reply" section at the new Doc the next time the guide is regenerated.
- Note in `HANDOFF.md` that the **live setup is waiting on the account connection**, and who needs to do it.

## 5. Check before you report
- Read the Doc back from Drive. Check that the DM text and fixes match the repo exactly, every section is present, and no repo paths or source codes leaked in.
- Report in 5 lines or fewer: the Doc link, what's ready, and what only the owner or account manager can do (the connection).
