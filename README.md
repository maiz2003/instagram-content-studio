# Content Studio

A reusable **Instagram content system built as Claude Code skills**. You give it a brand profile and a post idea. It produces a ready-to-shoot package: scored hooks, a Reel script and shot list, an SEO caption, a pre-publish scorecard and a one-page brief for your production agency. It works for any brand, B2B or B2C.

> **Scope: plan + produce + score. It does not publish.** No Instagram/Meta publishing connector is available, so you post or schedule the result in the Instagram app yourself.

The method comes from three books by Ahmed Shoman: *Instagram Secrets — Foundational*, *Instagram Secrets — 2026 Update* and *Hook Engineering 2026*. They were translated to English and restructured by domain. Every rule the skills apply cites its source item, e.g. `[H.31]`, `[U.36]`, `[F2.25]`.

**Status: Phase 1 approved (2026-09-26); Phase 2 in progress.** Built so far: the hook → script → caption pipeline, profile setup, the carousel builder, and the video producer, which renders finished text Reels to MP4.

## How to use it

Open Claude Code in this repo and ask in plain language, for example:

> Let's make the next Beroia Home post: a Reel about our bathroom units for showroom owners. Goal: leads.

Claude picks up the **content-studio** skill. You can also type `/content-studio`. It then:
1. loads `brands/beroia-home.yaml` and asks, in one batch, for any missing facts this post needs;
2. fills in a post brief;
3. writes 10 scored hooks and **asks you to pick one**;
4. writes the Reel script, the caption, the scorecard and the agency brief;
5. saves everything to `outputs/<brand>/<date>-<slug>/`.

Each skill also works on its own: `/hook-writer`, `/reel-scriptwriter`, `/caption-seo-writer`.

### Adding another brand
Copy `brands/_template.yaml` to `brands/<your-brand>.yaml` and fill it in. Unknown fields can stay `TODO`; the skills ask when a field matters. Key fields:

| Field | What it controls |
|---|---|
| `buyer_type` | B2B / B2C. Who the hooks speak to (e.g. a showroom owner vs an end customer) |
| `language_mix` | Lead language + dialect for voiceover and on-screen text; optional secondary language for the caption |
| `cta_mechanism` | The single call to action: DM keyword, **WhatsApp**, comment keyword, shop or website |
| `goals_allowed` | reach, trust, sale, **lead** |
| `products[].proof_points` | The only numbers the skills may use in hooks. Anything else becomes `[NUMBER NEEDED]` |
| `assets_available` | What can actually be filmed. Shot lists stick to it |
| `agency` | Who receives the one-page agency brief |

## What's in the repo

| Path | What it is |
|---|---|
| `CLAUDE.md` | Project rules that every Claude session loads automatically |
| `skills/content-studio/` | Orchestrator: brief → hooks → **you pick** → script → caption → scorecard → agency brief |
| `skills/hook-writer/` | 10 hooks from the 45 formulas, scored on a 12-point rubric, top 3 recommended |
| `skills/reel-scriptwriter/` | Timestamped shot list, re-hook, pattern interrupts, loop ending, CTA layer, cover, specs, 60-minute post-publish checklist |
| `skills/caption-seo-writer/` | Keyword-first bilingual caption, alt text, 0–3 hashtags, location tag, pinned comment, keyword consistency check |
| `.claude/skills/` | Symlinks to `skills/` so Claude Code auto-loads them |
| `knowledge/hook-formulas.md` | All 45 hook formulas + 3 collections, goal and buyer-type selection, opening mechanics, scoring rubric |
| `knowledge/ranking-signals.md` | The book's signal weights (labelled as unverified), positive and negative signals, length bands, timing, scorecard |
| `knowledge/conflicts-and-exclusions.md` | Rulings where the books disagree (the 2026 Update wins) and tactics that are never recommended |
| `knowledge/_sources/` | The three English translations, unchanged (private repo; the books are "All Rights Reserved") |
| `brands/` | `_template.yaml` + one profile per brand (`beroia-home.yaml` is the Phase 1 trial) |
| `outputs/` | One folder per post package |
| `scripts/check_coverage.py` | Reports which book items are cited in `knowledge/`; never fails |

## Ground rules the skills follow
- **Confidence.** Claims are `book-claim` unless an outside Instagram/Meta source is cited (`platform-confirmed`). None are confirmed yet. The scorecard's weights (Watch time 35 / Sends 20 / Saves 15 / Conversation 15 / Likes 5) are **the book's figures**, and the scorecard says so. It is a checklist, not a reach prediction.
- **Never recommended.** Fake or secondary-account engagement, pods, invisible bio text, false scarcity, generic "tag someone" bait, "link in bio" / "buy now" CTAs, invented numbers. Details and alternatives are in `knowledge/conflicts-and-exclusions.md`.
- **Brand facts come only from the brand profile.** Missing facts become visible placeholders, never guesses.

## Coverage check
```bash
python3 scripts/check_coverage.py          # per-book coverage + list of uncited items
python3 scripts/check_coverage.py --quiet  # summary only
```
Phase 1 cites all 48 Hook Engineering items and part of the other two books on purpose. Phase 2 fills in the rest.

## Phase 2 tools

| Piece | What it does | How to use it |
|---|---|---|
| `skills/profile-auditor` | Designs or audits a profile: name field, 3 bios with character counts, link, highlights with covers, 3 pins, first 9 grid tiles | "Set up the profile for <brand>" → `outputs/<brand>/profile-kit.md` |
| `skills/carousel-builder` | Slide plan → rendered 1080×1350 PNG slides in the brand's style → caption and alt text | "Make a carousel about <idea>" → `outputs/<brand>/<pkg>/carousel/png/` |
| `agents/video-producer` | Type mode: renders a script's text-card version to MP4 (text builds, punch zooms, synthesized SFX, loop), then checks frames and audio. AI-visual mode: Higgsfield footage, only after you OK the credits | "Render the video for <package>" → `outputs/<brand>/<pkg>/video/` |

**Render tools** (`scripts/render/`): `render.js` (HTML `.frame` elements → PNG), `reel.js` (JSON spec → MP4), `sfx.py` (synthesized sound layer; add licensed music in Instagram's editor). They need the Playwright + Chromium already in the environment and a session-only ffmpeg; setup is in `agents/video-producer.md`.

**Brand themes:** `brands/<slug>.theme.css` holds a brand's rendering style. LOCK IN's colours were sampled from its existing clips, with OFL fonts in `assets/fonts/`.

## Roadmap (remaining)
- **Knowledge files:** algorithm mechanics, reel production, visual SEO, Stories playbook, recovery protocol, case studies.
- **Skills:** story sequencer, growth-recovery doctor, case-study matcher.
- **Agent:** `growth-recovery-doctor` (audits a real account against the suppression checklist).
