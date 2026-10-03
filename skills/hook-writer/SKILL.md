---
name: hook-writer
description: Writes and scores 10 Instagram hooks (the first 0–3 seconds of a Reel, carousel cover or post opening) for any brand, B2B or B2C, using the 45 Hook Engineering formulas plus the opening tactics from the Instagram Secrets books. Use this whenever someone wants hooks, opening lines, scroll-stoppers, Reel openers, cover text or "first line" ideas for an Instagram post, or when the content-studio pipeline reaches the hook step, even if they just say "give me angles for this post" or "how should this Reel start".
---

# Hook Writer

Turns a brand profile and a post brief into **10 scored hooks** and a **recommended top 3**. The hook decides whether the post survives the first test audience: most viewers must get past about 3 seconds or distribution stops. So every hook here is built to stop the scroll visually, be understood in about 1 second, and give a reason to keep watching.

All paths are relative to the repo root.

## Inputs
1. **Brand profile**: `brands/<slug>.yaml`. If the user hasn't named a brand, list the files in `brands/` and ask.
2. **Post brief** (fields in `skills/content-studio/references/brief-template.md`): at minimum `product`, `goal` (reach | trust | sale | lead), `format` and `key_fact`. Ask for any that are missing. For B2B brands, also ask what the buyer's *business* pain is if the brief doesn't say.

## Read first
- `knowledge/hook-formulas.md`: formulas, goal → formula table, opening mechanics, rubric. **Required.**
- `knowledge/conflicts-and-exclusions.md`: E-codes (banned tactics) and the self-check. **Required.**
- `knowledge/ranking-signals.md` §1 and §3: which signal each hook should pull. Skim it.

## Process
1. **Pick 6–8 formulas.**
   - Start from the goal row in `hook-formulas.md` §1.
   - Filter by the profile's `buyer_type` using each formula's *Fit* column.
   - For **B2B**, the viewer is a business buyer (e.g. a showroom owner). Aim at *their* business pain from `audience.pains`: margin, returns and complaints from their own customers, batch consistency, delivery, price comparisons.
   - For goal `lead`, H.31 (Reverse Price Engineering) is the first candidate. It reframes unit price as total cost to the buyer.
2. **Write one or two hooks per formula**, 10 in total. Use the brand's real details: products, `assets_available` locations, `proof_points`.
   - Any number must come from `proof_points` or the brief. Otherwise write `[NUMBER NEEDED: what]` (rule E-5).
3. **Language.**
   - Spoken line and on-screen text in `language_mix.lead`, in `language_mix.dialect`. Write the dialect the way people actually speak it, not formal Arabic, when a dialect is set.
   - Add an English gloss in brackets after each non-English line so reviewers and agencies can follow.
4. **Apply the opening mechanics** (`hook-formulas.md` §4) to the first frame:
   - movement or contrast in frame 1
   - topic keyword spoken early
   - direct address
   - any open loop resolved no sooner than ~3 s
5. **Score each hook** on the 6-criterion rubric (`hook-formulas.md` §6, 0–2 each, max 12). A 0 on rule-safety disqualifies the hook. Be honest; an inflated score defeats the purpose.
6. **Recommend the top 3.** For each one, say why it wins and which ending it pairs with (send / save / keyword prompt, from `hook-formulas.md` §5).

## Output
Write to the package folder if one exists (`outputs/<brand>/<date>-<slug>/hooks.md`). Otherwise print the result. Use this structure:

```markdown
# Hooks: <brand> · <post slug>
Goal: <goal> · Buyer: <B2B/B2C> · Format: <format> · Language: <lead (dialect)>

| # | Formula | Spoken line (lead lang) [English gloss] | On-screen text (≤7 words) | First frame (0–1 s) | Signal | Score /12 |
|---|---|---|---|---|---|---|
| 1 | H.31 Reverse Price Engineering | … | … | … | C, P | 10 |
…

Rubric detail: one line per hook, e.g. "1: stop 2 · clarity 2 · specific 2 · keyword 1 · send 1 · safe 2"

## Top 3
1. **#n**: why it wins; paired ending: "<send/save/keyword line>"
…

## Open items
- [NUMBER NEEDED: …] / TODO fields the human must fill before shooting
```

On-screen text has at most 7 words, because it has to be read in about a second on a phone. Prefer on-screen wording that repeats the spoken keyword: the book says the system cross-checks speech, on-screen text and caption [U.ch3].

## Things to avoid
- Generic openers ("amazing tip", "watch this") [H intro]. Greetings or intros before the hook [U.51].
- "Tag someone who…", "link in bio", "buy now" (E-2, E-3).
- Scarcity or urgency the brief can't back up (E-4).
- Hooks that talk to the wrong buyer, e.g. addressing the showroom's end customer when the brand is B2B, unless the brief asks for that.
