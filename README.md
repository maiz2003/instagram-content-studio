# Content Studio

A reusable **Instagram content system built as Claude Code skills**. You give it a brand profile and a post idea. It produces a ready-to-shoot package: scored hooks, a Reel script and shot list, an SEO caption, a pre-publish scorecard and a one-page brief for your production agency. It works for any brand, B2B or B2C.

> **Scope: plan + produce + score. It does not publish.** No Instagram/Meta publishing connector is available, so you post or schedule the result in the Instagram app yourself.

The method comes from three books by Ahmed Shoman: *Instagram Secrets — Foundational*, *Instagram Secrets — 2026 Update* and *Hook Engineering 2026*. They were translated to English and restructured by domain. Every rule the skills apply cites its source item, e.g. `[H.31]`, `[U.36]`, `[F2.25]`.

**Status: Phase 1 approved (2026-09-26); Phase 2 built.** All planned skills, both agents and the full knowledge base exist. New work is driven by brand needs.

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

### Skills (`skills/`, auto-loaded via `.claude/skills/`)
| Skill | What it does |
|---|---|
| `content-studio` | Orchestrator: brief → hooks → **you pick** → script / carousel / Stories → caption → scorecard → agency brief; routes to every other skill |
| `hook-writer` | 10 hooks from the 45 formulas, scored on a 12-point rubric, top 3 recommended |
| `reel-scriptwriter` | Timestamped shot list, re-hook, pattern interrupts, loop ending, CTA layer, cover, specs, 60-minute post-publish checklist |
| `caption-seo-writer` | Keyword-first caption (bilingual when set), alt text, 0–3 hashtags, location, pinned comment, keyword consistency check |
| `carousel-builder` | Slide plan → rendered 1080×1350 slides in the brand's style → caption and alt text |
| `story-sequencer` | Daily / launch / Reel-support / highlight-intro Story sets on the 4-linked-Stories arc, rendered with sticker zones |
| `profile-auditor` | Profile setup or audit: name field, bios, link, highlights + covers, pins, first 9 tiles, 15-item score |
| `growth-recovery-doctor` | Reach-drop diagnosis (Account Status → baseline vs recent → cause) and a dated 14-day recovery plan |
| `case-study-matcher` | Closest precedents among the 11 documented cases, with an honest "what transfers" |

### Agents (`agents/`, auto-loaded via `.claude/agents/`)
| Agent | What it does |
|---|---|
| `video-producer` | Renders a script to a finished MP4 (type mode, local), or drafts footage with Higgsfield (only after you OK the credits); checks every render |
| `growth-recovery-doctor` | Hands-off account audit: gathers data read-only (a connected account's post list, or your Insights screenshots) and writes the recovery plan |

### Knowledge (`knowledge/`: all 384 book items cited)
`hook-formulas` · `ranking-signals` · `conflicts-and-exclusions` · `algorithm-mechanics` · `reel-production` · `visual-seo` · `profile-architecture` · `stories-playbook` · `recovery-protocol` · `case-studies` · `_sources/` (the three translations, unchanged; the repo is private and the books are "All Rights Reserved")

### Everything else
| Path | What it is |
|---|---|
| `CLAUDE.md` | Project rules that every Claude session loads automatically |
| `brands/` | `_template.yaml` + one profile per brand (`lock-in.yaml`, `beroia-home.yaml`) + optional `<slug>.theme.css` for rendering |
| `outputs/` | One folder per package: brief, hooks, script, caption, scorecard, `carousel/`, `stories/`, `video/` |
| `scripts/render/` | `render.js` (HTML → PNG), `reel.js` (spec → MP4), `sound.py` (composed soundtrack + scene sound design; outputs a full mix and an SFX-only version) · `beat.py` (detects a supplied track's BPM and downbeat, and re-times a Reel to it) |
| `scripts/check_coverage.py` | Reports which book items are cited in `knowledge/`; never fails |
| `assets/fonts/` | OFL fonts used by brand themes, with their licences |
| `assets/sounds/<brand>/` | A brand's own sound kit (WAVs + `kit.json`), used instead of the synthesized sounds when a Reel spec sets `sound_kit` |

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

## Rendering
`scripts/render/` needs the Playwright + Chromium already in the environment, plus a session-only ffmpeg (`pip install --target /tmp/ffmpeg-lib imageio-ffmpeg`; details in `agents/video-producer.md`). Videos get a composed, beat-synced soundtrack with scene sound design (`sound.py`), plus an SFX-only version for pairing with a trending Instagram sound. Brand styles live in `brands/<slug>.theme.css` (LOCK IN's colours were sampled from its own clips).

## Current brand work
- **LOCK IN** (`outputs/lock-in/`):
  - profile kit + rendered avatar and highlight covers
  - Four Doors package + MP4
  - launch week: 5 more MP4s, Stories, `week-plan.md` with every caption
  - 3 carousels: Phone Exile, What's Inside, The 3 Ugly Minutes
  - clip review and case matches
  - 30-day objectives (`objectives-30d.md`) + tracker page (`tracker/`, published privately on claude.ai)
- **Beroia Home**: on hold (the trial profile and TEST DATA smoke test are kept).
