---
name: story-sequencer
description: Plans and renders Instagram Stories sequences for any brand. It writes daily 6–8-frame Story sets built on the 4-linked-Stories arc (curiosity → problem → solution → CTA), with one interactive sticker every day, Reel-reshare frames, launch/teaser sequences and highlight intro stories. Frames are rendered 1080x1920 in the brand's style, with sticker placement notes. Use this whenever someone wants Stories, a Story plan, daily Stories, polls or question boxes, a launch/teaser Story, a highlight intro, or asks how to warm up followers before a post, even if they just say "what should I post on my story today".
---

# Story Sequencer

Stories are the relationship channel. Every sticker tap, reply and DM tells the system the follower cares, which lifts your next posts in their Feed [U.ch6], [F3.31]. This skill produces Story sets that earn those signals every day, for any brand.

All paths are relative to the repo root.

## Inputs
1. **Brand profile**: `brands/<slug>.yaml` (`cta_mechanism`, `content_pillars`, `visual_identity.theme_css`).
2. **What the Stories are for** (ask if not given):
   - `daily`: an ordinary day
   - `reel-support`: warm up before a Reel, or push it after
   - `launch`: a product or offer launch, or a teaser
   - `highlight-intro`: the ≤15 s first story of a highlight
   - `week`: a 7-day plan
3. **Linked posts:** which Reel or carousel from `outputs/<brand>/` this supports, if any.

## Read first
- `knowledge/stories-playbook.md`: the whole file. **Required.**
- `knowledge/profile-architecture.md` §6: highlights and the intro story.
- `knowledge/conflicts-and-exclusions.md`: E-4 (countdowns only for real dates), E-5, E-2.

## Process
1. **Arc.** Map the frames onto the 4-linked-Stories rule (curiosity → deeper problem → solution → CTA) [U.ch6]. Daily sets: 6–8 frames, within the 6–13 range [U.11]. Highlight intro: 3–5 frames, ≤15 s [F4.25].
2. **Stickers.** Put at least one interactive sticker in every daily set: poll, slider, question or quiz, chosen from the §3 toolkit [U.ch6], [F3.23]. Poll wording is a real either/or in the audience's words.
3. **Reel support:**
   - *Before a Reel*, in the morning or a few hours ahead: a poll or question on the Reel's topic [F1.9], [F3.14].
   - *After posting*: reshare the Reel immediately, with a line that makes people tap [F1.11], [F2.25].
   - *~12 h later*: reshare again from a new angle [F2.14].
4. **One ask per set.** A link sticker or DM keyword from `cta_mechanism`, never both in the same frame. The keyword must deliver something real.
5. **Text.** Short: ≤12 words per frame. Keep it in the top ~70% of the frame, clear of Instagram's reply bar. Leave a marked empty zone where the sticker goes.
6. **Render** (if `theme_css` exists):
   - Write `outputs/<brand>/<pkg>/stories/stories.html`: one `.frame` per story, 1080×1920, linking the brand theme.
   - Draw a dashed **sticker zone** box labelled with the sticker type. It's a placeholder only; stickers are added in the app.
   - Render with `NODE_PATH=$(npm root -g) node scripts/render/render.js <stories.html> <pkg>/stories/png story`.
   - Look at every PNG.
7. **Self-check:** real facts only; no fake countdowns or scarcity; poll options are neutral (not manipulative).

## Output
`outputs/<brand>/<date>-<slug>/stories.md` with:
- purpose and linked post
- a frame table: # · time of day · frame text · visual · sticker (type + exact wording) · link/keyword
- reply plan: how to answer sticker responses and DMs within the hour
- highlight: which highlight to save which frames to

Plus `stories/png/story-XX.png` when rendered.
