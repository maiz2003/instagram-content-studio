---
name: content-sprint
description: One command, four agents. Runs trend-scout → ghostwriter → hook-critic → repurposer on a topic and hands back finished files for the owner to approve. Use when the owner types /content-sprint <topic>, gives a topic to "run", or says "plan my week" (then run it for each planned post).
---

# Content sprint (LOCK IN)

The owner's "Agentic OS / content unit", set up 3 Oct 2026. It lives in this repo so it works in every session, local or cloud.

1. **Scout**: run the `trend-scout` agent on the topic. It returns 5 angles and picks the strongest.
2. **Draft**: run `ghostwriter` on that angle. It saves `content/drafts/<date>-<slug>.md`.
3. **Critique**: run `hook-critic` on the draft.
   - FIX: the critic edits the draft and checks it once more.
   - SCRAP: back to step 2 with the scout's next angle, once.
4. **Repurpose**: run `repurposer` on the SHIP version.
5. **You**: show the owner the finished piece and its versions. Nothing goes out without "approve".

**Posting:** after "approve", the `postiz-scheduler` skill loads Instagram posts into Postiz and schedules only the approved numbers. Video and images are made with the repo's renderers (`scripts/render/`). Instagram and TikTok posts need media before they can be loaded.

**"Plan my week"**: follow `studio/TEAM.md` → Weekly routine. That's 5 posts a week at 19:00 UK from week 4, and each post goes through this sprint.

Voice: `studio/BRAND.md`, with owner overrides in `studio/DECISIONS.md`.
