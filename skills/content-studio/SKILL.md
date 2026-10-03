---
name: content-studio
description: The Content Studio orchestrator. It takes any brand (B2B or B2C) from a post idea to a finished Instagram post package in outputs/, in this order - brand profile → brief → 10 scored hooks → the user picks one → Reel script → caption & SEO → pre-publish scorecard → one-page agency brief. Use this whenever someone wants to plan, make or prepare an Instagram post, Reel or content for a brand or account (e.g. "let's do the next Beroia post", "make a Reel for our new collection", "prepare this week's post for the agency"), or asks to use the content studio, even if they only name the product and the brand.
---

# Content Studio (orchestrator)

Runs the post pipeline end to end and writes one package folder per post. It stays thin on purpose: the craft lives in the sub-skills and in `knowledge/`. This skill handles ordering, hand-offs, the human checkpoint, the scorecard and the agency brief.

**Scope: plan + produce + score. It never publishes.** No Instagram/Meta publishing connector is available. The human posts or schedules in the Instagram app.

All paths are relative to the repo root.

## Pipeline
1. **Brand profile.** Load `brands/<slug>.yaml`. If there's no profile, copy `brands/_template.yaml`, fill it in with the user and save it.
   - Note which TODO fields matter for *this* post: CTA value, products, proof points, assets. Ask about them now, in one batch.
2. **Brief.** Fill in `references/brief-template.md` from the conversation. Ask once, in one batch, for any required field that's missing.
   - Check that `goal` is in the profile's `goals_allowed` and that the topic fits a `content_pillar`. Off-pillar posts hurt reach [U.4], [F2.13], so if the topic is off-pillar, say so and ask.
   - Create the folder `outputs/<brand-slug>/<publish-date or today, YYYY-MM-DD>-<short-slug>/` and save `brief.md` there.
3. **Hooks.** Follow `skills/hook-writer/SKILL.md` → `hooks.md`.
4. **Checkpoint: the human picks the hook.** Show the top 3 (with English glosses) and ask which one to use. They may pick another row or ask for edits. Don't continue until a hook is chosen.
   - Exception: if the user explicitly said to run everything without stopping, pick the top-scored hook and say so in the package.
5. **Script.** Follow `skills/reel-scriptwriter/SKILL.md` → `script.md`.
   - **Carousel or static post:** follow `skills/carousel-builder/SKILL.md` instead, using the chosen hook as the cover.
   - **Stories:** follow `skills/story-sequencer/SKILL.md`.
   - **Finished video:** once the script is approved, hand the package to the `video-producer` agent (`agents/video-producer.md`).
6. **Caption.** Follow `skills/caption-seo-writer/SKILL.md` → `caption.md`, including the keyword consistency check against the script.
7. **Scorecard.** Write `scorecard.md` using `knowledge/ranking-signals.md` §7.
   - Include the mandatory disclaimer verbatim: the weights are the book's figures, unverified, and this is a checklist, not a reach prediction.
   - Score honestly. Each item scores 1 only if it is really in the package.
   - List the open items: `[NUMBER NEEDED]`, `[CTA VALUE NEEDED]`, TODOs.
8. **Agency brief.** Write `agency-brief.md` from `references/agency-brief-template.md` for the agency named in `agency.name`. Skip this step if it's empty or in-house. **It must fit on one page** (roughly 350–450 words): the agency needs to shoot from it, not read it twice.
9. **Final rule check.** Run `knowledge/conflicts-and-exclusions.md` §4 across all files, then summarise for the user:
   - the chosen hook
   - duration
   - the scorecard total
   - open items the human must resolve before shooting or posting
   - paths to the files

## Package contents
```
outputs/<brand>/<date>-<slug>/
  brief.md          the filled brief
  hooks.md          10 scored hooks + top 3
  script.md         shot list, beats, CTA layer, cover, specs, 60-min checklist
  caption.md        caption, alt text, location, pinned comment, keyword check
  scorecard.md      book-weighted pre-publish checklist (with disclaimer)
  agency-brief.md   one page for the production agency
```

## Other entry points
- Profile setup or audit → `skills/profile-auditor`
- Reach dropped / account diagnosis → `skills/growth-recovery-doctor` (or the `growth-recovery-doctor` agent for a hands-off audit)
- "Who has done this well?" / choosing a model → `skills/case-study-matcher`
- Story plans → `skills/story-sequencer`

## Principles
- **The brand profile is the only source of brand facts.** Never carry facts from one brand into another's package. If a needed fact is missing, ask for it or leave a visible placeholder. Don't invent it (E-5).
- **The human decides.** Show the hook choice and open items clearly. The pass bar for Phase 1 is the owner saying "I'd post this".
- **Test data is labelled.** If a brief is invented for testing, put `TEST DATA — not a real post` at the top of every file in that package.
