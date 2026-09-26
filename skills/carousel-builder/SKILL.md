---
name: carousel-builder
description: Plans, writes and renders Instagram carousels for any brand. It produces a slide-by-slide plan (hook cover, one idea per slide, a save-worthy summary, a keyword CTA), then renders finished 1080x1350 PNG slides in the brand's own style, plus a caption. Use this whenever someone wants a carousel, slides, a swipe post, a multi-image post, an infographic post, or wants to turn a diagram, list, framework, guide, comparison or a Reel into slides, even if they only say "make this a post people save".
---

# Carousel Builder

The book treats carousels as the save-and-depth format: people linger, swipe back and save them, while Reels are the reach format [U.7], [U.case lessons] (see C-5 for the conflicting numbers). This skill turns one idea into a carousel people keep.

All paths are relative to the repo root.

## Inputs
1. **Brand profile**: `brands/<slug>.yaml`. If `visual_identity.theme_css` is set, slides are rendered. Otherwise the output is a plan plus text for a designer.
2. **Brief**: `skills/content-studio/references/brief-template.md` with `format: carousel`. The typical goal is trust or saves. Source material can be a diagram, list, framework, existing Reel or product page.

## Read first
- `references/carousel-rules.md` (in this skill). **Required.**
- `knowledge/hook-formulas.md` §1, §2 and §6: the cover slide is the hook. Score cover options on the same rubric.
- `knowledge/conflicts-and-exclusions.md`: E-2, E-3, E-4, E-5.
- For rendering: `skills/carousel-builder/assets/layouts.css`. A worked example is `outputs/lock-in/2026-09-26-phone-exile-carousel/carousel/slides.html` (slide structure, icon tiles, ladder summary, CTA).

## Process
1. **Pick the one idea** and the viewer who should save it. If the source holds several ideas, split them into separate carousels.
2. **Cover (slide 1).** Write 3 cover options from different formulas, score them on the hook rubric and use the best one. Rules:
   - ≤8 words, big type
   - the keyword visible on the slide
   - a swipe cue ("→" or "swipe")
3. **Slide 2 = the promise, or a second hook.** The book says unseen carousels get re-shown [U.7], so slide 2 must also work as an opener.
4. **Body slides: one idea each.** Each slide gets a headline of ≤6 words plus at most 2 short support lines [U.72], [U.41]. Build tension slide to slide (an open loop, then the payoff). **6–10 slides in total**; 20 is the maximum [U.7].
5. **Summary slide.** The whole idea on one screenshot-worthy slide (a list, table or ladder) plus a save line [U.149], [H.cta].
6. **CTA slide.** One action from `cta_mechanism` (e.g. "Comment LOCK") plus one specific send line [U.36], [H.10]. Never "link in bio" (E-3).
7. **Render** (only if `theme_css` exists):
   - Write `outputs/<brand>/<pkg>/carousel/slides.html`. It links `../../../../brands/<slug>.theme.css` and `../../../../skills/carousel-builder/assets/layouts.css`, and has one `.frame.slide` per slide (see the worked example above).
   - Run `NODE_PATH=$(npm root -g) node scripts/render/render.js <slides.html> <pkg>/carousel/png slide`.
   - Look at every PNG. Check that nothing overflows, text is readable at phone size, the key content sits inside the 3:4 grid crop, and the amber (accent) is used on exactly one key word per slide.
8. **Caption.** Run the caption-seo-writer skill with this carousel's slide text as the "script": keyword in the first 5 words, a save + send line, the CTA, 0–3 hashtags. Write one line of alt text per slide.
9. **Self-check:** `conflicts-and-exclusions.md` §4. Real facts only: book content, product facts and the brand's proof points.

## Output
`outputs/<brand>/<date>-<slug>/`:
- `carousel.md`: goal · viewer · cover options with scores · the slide table (slide # | headline | support lines | visual | alt text) · caption · posting notes (music from the Instagram library [F3.11], [U.7]; reorder after 48 h if weak [U.18]; which highlight to add it to)
- `carousel/slides.html` + `carousel/png/slide-XX.png` (when rendered)
