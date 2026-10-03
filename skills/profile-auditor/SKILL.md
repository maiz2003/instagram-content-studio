---
name: profile-auditor
description: Audits or designs an Instagram profile for any brand, as a conversion page. It scores an existing profile on a 15-item checklist and writes a ready-to-paste profile kit - keyword name field, 150-character bio options, link setup, highlight plan with covers, first-highlight intro story, 3 pinned posts and a first-9-tiles grid plan. Use this whenever someone is setting up a new Instagram account, rewriting a bio, choosing highlights or pinned posts, asking why profile visitors don't follow, or wants a profile audit or "make my page convert", even if they only say "what should my bio say".
---

# Profile Auditor

The profile decides in about 3 seconds whether a visitor follows [F4.1]. It's also the page the system reads to decide who to suggest you to [U.ch5]. This skill makes that page do its job, for any brand in `brands/`.

All paths are relative to the repo root.

## Inputs
1. **Brand profile**: `brands/<slug>.yaml`.
2. **Mode:**
   - **Setup** (new or empty account): design the profile from scratch.
   - **Audit** (existing account): the user supplies the current profile. That can be screenshots, pasted bio text, a list of highlights and pinned posts, or read-only post data from a connected account if one is available. Score it, then rewrite it.

## Read first
- `knowledge/profile-architecture.md`: the whole file. **Required.** The checklist is in §12.
- `knowledge/conflicts-and-exclusions.md`: E-4, E-5 and E-7 matter most for profiles. **Required.**
- Existing packages in `outputs/<brand>/`: pinned posts and grid should use real content that already exists or is planned.

## Process
1. **Keyword.** Pick the search phrase the target audience would type (e.g. "discipline", "study focus"). It goes in the name field and bio line 1 (§2, §4).
2. **Name field** (≤30 characters): 2–3 options in the form "Name | keyword".
   - **Handle:** only suggest options if the brand has none. Say they must be checked for availability in the app.
3. **Bio.** Write 3 options, each ≤150 characters (count them and show the count). Each follows a different structure from §4: core formula, 3-line story, direct address. Rules:
   - every option ends with one honest tap/DM trigger that matches `cta_mechanism`
   - no invented proof (E-5)
   - no fake scarcity (E-4)
   Recommend one option, and suggest an A/B plan for the runner-up [F4.23].
4. **Link.** Recommend the single bio link, e.g. the brand's quiz or landing page. Check it's trusted and readable [F3.2], [F4.9]. Flag it if it doesn't load for part of the audience.
5. **Photo.** Give a spec. For faceless brands: a logo mark, contrast colour, legible at 110 px.
6. **Highlights.** Plan 3–5 in the §6 order. For each: a title (≤10 characters so it isn't cut off), cover design notes, and the stories it should hold.
   - Script the **first highlight's intro story** (≤15 s, 3–5 frames).
   - Only real testimonials. Until they exist, swap that slot for "How it works" or a free sample.
7. **Pinned posts.** Pick 3 from existing or planned posts in `outputs/<brand>/` (or the brand's clip bank), in the §7 slots. Say which post goes in which slot and why.
8. **Grid.** Plan the first 9 tiles in posting order, following §8: varied tile types, readable covers, on-pillar. Remember the newest post shows top-left.
9. **Audit mode only:** score the current profile 0/1/2 on the §12 checklist (max 30). List the fixes by impact, then deliver the rewritten kit.
10. **Self-check** against `conflicts-and-exclusions.md` §4 and the §11 table in `profile-architecture.md`.

## Output
Write `outputs/<brand>/profile-kit.md`, with an ISO date suffix if one already exists:

```markdown
# Profile kit: <brand> (<setup|audit>) · <date>
## Keyword
## Name field (options)
## Handle (only if needed)
## Bio (3 options, char counts) → recommended + A/B plan
## Link
## Profile photo spec
## Highlights (order, titles, covers, contents) + first-highlight intro script
## Pinned posts (3 slots)
## First 9 grid tiles (posting order)
## Audit score (audit mode) / Setup checklist (setup mode)
## Before you post the first Reel (ordered to-do)
## Open items
```

Bios must be pasted exactly, so line breaks matter. Show each bio inside a code block to keep them.
