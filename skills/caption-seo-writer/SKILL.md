---
name: caption-seo-writer
description: Writes the search-optimised Instagram caption package for a post, following the brand's language mix. The package has the keyword in the first 5 words, a bilingual body built to earn saves and sends, the brand's own CTA (DM keyword, WhatsApp or comment keyword), 0–3 hashtags, about 100 characters of alt text, an exact location tag and a pinned first comment. It also checks that the keyword is consistent across voiceover, on-screen text and caption. Works for any brand, B2B or B2C. Use this whenever someone needs an Instagram caption, alt text, hashtags, keywords or Instagram SEO for a Reel, carousel or post, or when the content-studio pipeline reaches the caption step.
---

# Caption & SEO Writer

The book claims Instagram search now runs on keywords, read from the name field, the caption, on-screen text and speech, rather than on hashtags. It also claims ranking drops when the words contradict what's on screen. This skill writes the caption package and checks that consistency.

All paths are relative to the repo root.

## Inputs
1. **Brand profile**: `brands/<slug>.yaml`, especially `language_mix`, `cta_mechanism`, `geo`, `banned_words_claims`.
2. **Post brief**: `skills/content-studio/references/brief-template.md`.
3. **The script** (`script.md`) or, for non-Reel posts, the slide/visual plan. Its voiceover and on-screen text are needed for the consistency check. If there is no script, write the caption from the brief and mark the consistency check "not run".

## Read first
- `references/seo-zones.md` (in this skill): keyword zones, alt text, hashtags, location. **Required.**
- `knowledge/conflicts-and-exclusions.md`: C-2 (hashtags), C-9 (commercial intent), E-2/E-3/E-4/E-5. **Required.**
- `knowledge/hook-formulas.md` §5: send, save and keyword prompt wording.

## Process
1. **Pick the primary keyword.** It's the phrase this brand's buyer would type into Instagram search. For B2B that's the trade term a showroom owner uses, not the consumer word. Also pick 2–4 supporting keywords.
   - If `language_mix.secondary` is set, pick the primary keyword in both languages.
2. **Line 1.** The primary keyword within the first 5 words, written naturally in the lead language/dialect.
   - It should also work as a second hook, because the first line shows before "more".
3. **Body.** 2–5 short lines:
   - the one idea from the Reel
   - one reference-grade detail worth saving (spec, test, comparison)
   - the specific send prompt ("send this to …")
   - Put the supporting keywords in naturally. No keyword stuffing.
4. **Secondary-language line.** Follow `language_mix.mix_rule`. Typically one short line in the secondary language carrying the primary keyword.
5. **CTA.** Exactly one, from `cta_mechanism`:
   - WhatsApp → "WhatsApp '<keyword>' to <number/handle> for <what they get>"
   - DM keyword → "DM '<keyword>' …"
   - comment keyword → "Comment '<keyword>' …"
   - Never "link in bio" or "buy now" (E-3).
   - If the value is TODO, write `[CTA VALUE NEEDED]`.
6. **Hashtags:** 0–3, specific (niche + place), at the end (C-2).
7. **Alt text:** about 100 characters describing the actual scene, including the primary keyword. Written in the lead language unless the profile says otherwise.
8. **Location tag:** the exact place from `geo.location_tag`. If it's TODO, recommend the most precise real place and flag it.
9. **Pinned first comment:** a genuinely useful add-on (a spec detail, an FAQ answer, or a question that starts a discussion). It must not be a planted fake comment (E-6).
10. **Consistency check.** Confirm the primary keyword appears in (a) the spoken voiceover in the first ~5 s, (b) on-screen text, and (c) the caption's first 5 words. Report pass or fail for each and give the fix for any fail.

## Output
Write `outputs/<brand>/<date>-<slug>/caption.md`:

```markdown
# Caption: <brand> · <slug>
Primary keyword: <lead> / <secondary> · Supporting: …

## Caption (ready to paste)
<line 1 with keyword in first 5 words>
<body>
<secondary-language line>
<CTA>
<0–3 hashtags>

[English gloss of the caption for reviewers, if lead ≠ English]

## Alt text (~100 chars)
## Location tag
## Pinned first comment
## Keyword consistency check
| Zone | Found? | Text | Fix |
| Voiceover (first ~5 s) | ✅/❌ | … | … |
| On-screen text | … |
| Caption first 5 words | … |
## Open items
```

Write in the dialect as people actually speak it. Captions read like a person talking to the buyer, not an ad.
