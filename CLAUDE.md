# Content Studio — project context

## Mission
A permanent, reusable **Instagram growth system built as Claude Code skills**. It turns a brand profile plus a post brief into ready-to-shoot content: hooks, Reel scripts, captions, scorecards and agency briefs. It is **brand-agnostic**: it serves any account, any niche, B2B or B2C, and every format (Reels, carousels, Stories, static posts). Beroia Home is only the first trial profile, not the target.

**Scope: plan + produce + score. No auto-publish.** There is no Instagram/Meta publishing connector in this environment. The human posts or schedules in the Instagram app. Higgsfield (connected) is for generating draft visuals/video in Phase 2. Whop's Meta Business connection can read existing posts (Phase 2, read-only audit use).

## The 3 source books (Ahmed Shoman, @a7medshoman1)
The English translations are the source of truth. Do not re-OCR or re-translate. They live in `knowledge/_sources/` once Phase 1 step 2 lands.

| ID | Book | Contents | Numbering |
|---|---|---|---|
| **F** | *Instagram Secrets — Foundational* (اسرار الانستغرام – النسخة التأسيسية) | 183 secrets in 4 parts: P1 algorithm/Reels (45), P2 desktop signals, Creator tools, post-publish behaviour (53), P3 comments, bio links, new-account boost, posting frequency (41), P4 profile architecture (44) | **Renumbered per part in the translation.** Not traceable 1:1 to Arabic source pages. |
| **U** | *Instagram Secrets — 2026 Update* (اسرار الانستغرام – اخر تحديث) | Muse Spark, signal-weight table, 8 chapters, case studies (Huda Beauty, Joelle, Indriya, Momya, Nike, Starbucks, Daniel Wellington, Zara, Gymshark×Whitney Simmons, Under Armour×John's Style, Oysho×Li Lin) | Original book numbering 1–158. **Numbers 22–26 do not exist**, so there are 153 real items. |
| **H** | *Hook Engineering 2026* (هندسة الهوكات 2026) | 45 hook/copy formulas plus 3 collections: Common Hooks, FOMO Curiosity Hooks, Calls to Action | Numbered 1–45 in the translation. |

If exact Arabic page traceability for F or H ever matters, that is a re-extraction task. Don't assume it exists.

## Knowledge rules (enforced in every knowledge file and skill)
- **Cite every claim with its source ID.** Formats:
  - `[F1.24]` = F Part One #24
  - `[U.36]` = U #36
  - `[H.31]` = H formula #31
  - `[U.ch2]` = a table or section in U Chapter 2
  - `[U.case:Indriya]` = a U case study
- **Confidence tags:**
  - `platform-confirmed` only when there is a source **outside the books** (Instagram/Meta docs or announcements), cited with a link.
  - Anything the book merely *attributes* to Mosseri or Meta is `book-claim`.
  - Default is `book-claim`.
- **Signal weights (Watch 35 / Sends 20 / Saves 15 / Conversation depth 15 / Likes 5) are the book's figures [U.ch1].** They have no outside source. Anything that uses them (scorecards) must say so, and must not present itself as a reach prediction.
- **Conflict precedence:** when sources disagree, **U (2026) beats F and H**. Examples:
  - Reel length follows the goal-based bands and "total watch time beats completion" [U.ch2, U.144], not [F1.4, F1.20].
  - Hashtags: 0–3, keywords first [U.6, U.143].
- **CTA rules:**
  - Specific send prompts that name who benefits are allowed [H.10, U.36].
  - Generic "tag someone who…" bait is banned [U.ch7].
  - CTAs are a DM keyword, WhatsApp, or a comment keyword. Never "buy now" or "link in bio" [F1.5, H.18, H.29].
- **Excluded tactics.** Never recommend these; keep them listed with reasons in `knowledge/conflicts-and-exclusions.md`:
  - self-engagement via fake or secondary accounts [F1.42]
  - planted early comments [F1.38]
  - invisible white bio text [F4.16]
  - false scarcity [F4.29]
  - any engagement pods or bought engagement [U.100, U.138]

## Brand profiles are inputs, never hardcoded
- Every skill reads a profile from `brands/<slug>.yaml`, built from `brands/_template.yaml`.
- Key fields:
  - `buyer_type` (B2B/B2C/both)
  - `audience`
  - `language_mix` (lead / secondary / dialect)
  - `cta_mechanism` (dm_keyword / whatsapp / comment_keyword / shop / website)
  - `goals_allowed` (reach / trust / sale / lead)
  - `assets_available`
  - `agency`
- **No brand-specific facts go in skills or knowledge files.**
- Trial profile, Beroia Home:
  - B2B wholesaler selling to showroom owners
  - Egyptian Arabic lead, English secondary
  - CTA is WhatsApp
  - can film inside its bathroom-units factory
  - agency is Attract

## Build phases — Phase 1 ONLY until the owner approves
**Phase 1 (current):**
- `knowledge/_sources/`
- `knowledge/hook-formulas.md`, `knowledge/ranking-signals.md`, `knowledge/conflicts-and-exclusions.md`
- `brands/_template.yaml`, `brands/beroia-home.yaml`
- skills: `content-studio` (thin orchestrator), `hook-writer`, `reel-scriptwriter`, `caption-seo-writer`
- `scripts/check_coverage.py` (reports gaps and **never fails the build**)
- README

Phase 1 runs end-to-end on one real upcoming post. The output is shown to the owner **before anything else is touched**. Each package includes an `agency-brief.md` for the agency.

**Gate:** nothing in Phase 2 starts until the owner says Phase 1 output is something they'd actually post ("I'd post this"). Full knowledge coverage also waits until then.

**Phase 2 (not yet):**
- knowledge: algorithm-mechanics, reel-production, visual-seo, profile-architecture, stories-playbook, recovery-protocol, case-studies
- skills: carousel-builder, story-sequencer, profile-auditor, growth-recovery-doctor, case-study-matcher
- `agents/`: `video-producer` (Higgsfield) and `growth-recovery-doctor`
- until then, knowledge not yet distilled is read directly from `knowledge/_sources/`

Don't scaffold Phase 2 pieces early. Don't install packages without asking; scripts use the Python standard library only.

## Repo layout
```
CLAUDE.md
README.md
knowledge/            distilled domain files + _sources/ (verbatim translations; repo is private, books are "All Rights Reserved")
brands/               _template.yaml + one YAML per brand
skills/<name>/        canonical skill folders (SKILL.md + references/), scaffolded with the skill-creator skill
.claude/skills/<name> symlinks → ../../skills/<name> so Claude Code auto-loads them
outputs/<brand>/<YYYY-MM-DD>-<slug>/   hooks.md, script.md, caption.md, scorecard.md, agency-brief.md
scripts/              check_coverage.py
agents/               Phase 2
```

## Working conventions
- Develop on a feature branch and open a draft PR into `main`.
- Keep SKILL.md files short. Point to `knowledge/` instead of copying from it.
- Label test data as test data. Never present an invented brief as a real post.
