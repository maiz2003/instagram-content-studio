---
name: case-study-matcher
description: Finds the closest real Instagram precedents for a brand or a post idea among the 11 documented case studies (Huda Beauty, Joelle, Indriya Jewelry, Momya, Nike, Starbucks, Daniel Wellington, Zara, Gymshark x Whitney Simmons, Under Armour x John's Style, Oysho x Li Lin). It explains what to copy, what doesn't transfer, and the first concrete step. Use this whenever someone asks "who has done this well", wants examples or proof for a strategy, is planning a launch, collab or influencer campaign, or asks which brand to model their account on, even if they don't say "case study".
---

# Case-Study Matcher

It matches a brand's situation to the documented case studies by **mechanism first**, then sector, then size, and turns the match into moves this brand can actually make.

All paths are relative to the repo root.

## Inputs
- A brand profile (`brands/<slug>.yaml`), and optionally a specific goal or post idea (launch, collab, new account, sales push, etc.).

## Read first
- `knowledge/case-studies.md`: the whole file, especially the tag vocabulary and the matching guidance. **Required.**
- `knowledge/conflicts-and-exclusions.md` E-5: the case numbers are the book's figures. Never present them as verified, or as the brand's own results.

## Process
1. **Describe the brand's situation in tags:** buyer type, sector, account size (a new account counts as small), goal, assets (face or faceless, budget for influencers, shop or DM sales).
2. **Score every case** 0–3 on each dimension:
   - **mechanism overlap** (the tactics this brand can use), weighted ×2
   - **stage/size similarity**
   - **sector similarity**
   Pick the top 2–3.
3. **For each match:**
   - what they did (with the source tag)
   - **the transferable move**, restated for this brand in one sentence
   - **what doesn't transfer**: budget, existing fame, audience size, sector norms
   - **the first concrete step** this week, tied to a skill (e.g. "carousel-builder: a 'send this to…' series")
4. **B2B brands:** all 11 cases are B2C. Say so, and match on mechanism only (e.g. Indriya's send-CTA → "send this to your purchasing partner"; DW's partner network → a reseller/showroom network).
5. **Honesty line:** quote the case numbers as "the book reports…" and never promise similar results.

## Output
`outputs/<brand>/case-matches-<date>.md`, or inline if the user just wants an answer:
a match table (case · score · why) → per-match cards (move / doesn't transfer / first step) → one-paragraph recommendation.
