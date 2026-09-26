---
name: growth-recovery-doctor
description: Diagnoses why an Instagram account's reach, views or growth dropped, or never took off, and prescribes a recovery plan. It checks Account Status first, then compares recent posts against the account's own baseline, maps symptoms to causes (weak hooks, niche drift, ghost posting, bait, watermarks, reports, off-brand followers), and writes a dated 14-day recovery plan. Use this whenever someone says their reach dropped, views died, they think they're shadowbanned, growth stalled, a new account isn't getting views, or asks "what's wrong with my account", even if they don't use the word "recovery".
---

# Growth-Recovery Doctor

The book's stance: the algorithm doesn't punish at random; it responds to signals the account has piled up [U.ch7]. So diagnose first, then treat. For a hands-off audit that gathers the data itself, use the `growth-recovery-doctor` agent (`agents/growth-recovery-doctor.md`). This skill is the method.

All paths are relative to the repo root.

## Inputs
- A brand profile (`brands/<slug>.yaml`).
- **Evidence, as much as is available:**
  - an Account Status screenshot or answer
  - Insights for the last 10–20 posts: views, reach, % non-followers, average watch time, 3-second hold if shown, likes, comments, shares/sends, saves, follows
  - posting dates and times
  - what changed recently (topic, format, frequency, tools)
  - screenshots or links to the posts themselves
  If a connected read-only data source is available (e.g. Whop's `social-accounts_posts` for a connected Instagram account), use it and say that you did.

## Read first
- `knowledge/recovery-protocol.md`: the whole file. **Required.**
- `knowledge/ranking-signals.md` §3–4 and `knowledge/algorithm-mechanics.md` §4–5.
- `knowledge/hook-formulas.md` §6, to re-score the weakest posts' hooks.
- `knowledge/conflicts-and-exclusions.md`: never prescribe E-1 … E-9.

## Process
1. **Account Status first** (C-8). If restricted, the plan starts with resolving that.
2. **Baseline vs recent.** Tabulate the posts, and compute each metric's median for the earlier and recent windows. Name the metric that fell first; that's where the problem entered the funnel (hook → hold → send/save → follow).
3. **Symptom → cause.** Use the `recovery-protocol.md` §1 table. Give each cause a confidence level (high/med/low) and cite the evidence (post numbers).
4. **Check the content itself:**
   - re-score the 3 weakest and 3 strongest hooks with the rubric
   - check for niche drift against `content_pillars`
   - look for watermarks, bait lines, reposts, and "posting-and-leaving" gaps
5. **Prescribe.** Follow `recovery-protocol.md` §3, adapted to what you found:
   - 48 h pause
   - Reset suggested content
   - Trial Reels
   - fix the cause
   - smart consistency
   - daily relationship work
   - recycle winners
   - archive weak posts
   Give **dated steps for 14 days**, and name which skill produces each piece (hook-writer, carousel-builder, story-sequencer…).
6. **Define success signals** to check on day 7 and day 14 (`recovery-protocol.md` §4), with target directions.
7. **Honesty:** separate the evidence from the book's claims; label every percentage as the book's figure. If the data can't support a diagnosis, say which data is missing.

## Output
`outputs/<brand>/recovery-<date>.md`:
Status · data table · the funnel stage that broke · causes ranked (with confidence + evidence) · 14-day plan (a dated table) · day-7 / day-14 checks · what data would sharpen the diagnosis.

**New accounts with no history:** there's nothing to recover. Produce a "clean start" checklist instead: profile-kit complete, first-week plan, no deleting or editing after posting [F3.16], small-account advantages [U.31], and the metrics to watch from post 1.
