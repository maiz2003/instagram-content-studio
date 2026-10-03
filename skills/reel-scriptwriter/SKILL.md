---
name: reel-scriptwriter
description: Turns a chosen Instagram hook into a shoot-ready Reel script. It writes a timestamped shot list (shots, on-screen text, voiceover, music/SFX, edit notes), a re-hook, pattern interrupts, a loop or cut-off ending, send/save/CTA lines, a cover-frame spec, production specs and a 60-minute post-publish checklist. Works for any brand and B2B or B2C. Use this whenever someone wants a Reel script, shot list, storyboard, video outline or filming plan for Instagram, or when the content-studio pipeline reaches the script step, even if they only say "turn this hook into a video" or "what do we film".
---

# Reel Scriptwriter

Builds a Reel from one chosen hook, so that the book's highest-weighted signal, watch time, is designed in second by second. It then closes on the send, save and CTA moves that the book says drive distribution.

All paths are relative to the repo root.

## Inputs
1. **Brand profile**: `brands/<slug>.yaml`.
2. **Post brief**: `skills/content-studio/references/brief-template.md`.
3. **The chosen hook.** Usually a row from `hooks.md`. If the user gives none, run the hook-writer skill first or ask.

## Read first
- `knowledge/ranking-signals.md`: §5 length bands, §3 levers, §6 timing, §7 scorecard items. **Required.**
- `knowledge/hook-formulas.md` §5: re-hooks, endings, send/save/keyword prompts. **Required.**
- `knowledge/conflicts-and-exclusions.md`: the E-codes and the self-check. **Required.**
- `knowledge/reel-production.md`: structure, editing, text, sound, people, cover, specs, formats and series. **Required.**

## Process
1. **Set the length** from the goal band (`ranking-signals.md` §5). State the target duration.
   - Content should earn its seconds. Total watch time beats completion rate, but padding kills both.
2. **Beat structure.** Adjust the timings to the length:
   - **0–3 s, hook:** the chosen hook exactly. Key visual in frame 1; topic keyword spoken.
   - **3–8 s, promise/setup:** what the viewer gets, stated plainly.
   - **~8 s, re-hook:** a new question or twist before attention drops.
   - **Body:** one idea, delivered in beats of 3–6 s. Each beat gives a small reward (a new fact, a visual proof, a number) and a pattern interrupt: angle change, cut, zoom, text pop or SFX.
   - **Payoff:** the proof or reveal the hook promised.
   - **Ending:** loop back to the opening line or motion, *or* a smart cut-off, *or* an open question. Never a "bye, see you" outro.
   - **CTA layer:** exactly one primary action, taken from the profile's `cta_mechanism` (e.g. a WhatsApp keyword), plus one specific send prompt and/or save prompt. Put them on screen and in the voiceover. Don't stack more than two asks.
3. **Use the brand's real assets.** Every shot must be filmable with `assets_available`, e.g. real factory areas for a manufacturer. If a shot needs something not listed, flag it in Open items.
4. **B2B framing.** For B2B brands, the proof should answer the buyer's question "will this make or save me money and trouble?" Show tests, consistency, packing and delivery readiness, and the margin logic.
5. **Language.** Voiceover and on-screen text in `language_mix.lead` + dialect, with `[English gloss]` in brackets so the agency and reviewers can follow. On-screen text should have ≤7 words per card and repeat the keyword.
6. **Self-check** against `conflicts-and-exclusions.md` §4. Unverified numbers become `[NUMBER NEEDED: …]`.

## Output
Write `outputs/<brand>/<date>-<slug>/script.md`:

```markdown
# Reel script: <brand> · <slug>
Goal · Buyer type · Target length · Language (dialect) · Hook used (formula ID)

## Shot list
| Time | Shot / visual | On-screen text | Voiceover (lead) [English gloss] | Music / SFX | Edit note |
|---|---|---|---|---|---|
| 0:00–0:03 | … | … | … | … | hard cut in, no intro |
…

## Beat map
Hook → setup → re-hook (0:0x) → beats → payoff → ending type (loop / cut-off / question)

## CTA layer
Primary action (from cta_mechanism) · send prompt · save prompt: exact wording

## Cover frame
Frame/timecode or separate shot · cover text (≤5 words) · face/eye-contact note · dominant colour

## Production specs
1080×1920, 9:16 · resolution/bitrate · no watermark · sound layer · captions burned in or auto · edit/export notes

## Post-publish checklist (first 60 min)
- 10 min before: …  · posting time: … · after: …

## Open items
- [NUMBER NEEDED: …], missing assets, TODO profile fields
```

## Things to avoid
- Talking-head intros, logos or greetings in the first 3 s. The audition happens there.
- Silent stretches or long static shots [U.131].
- More than one idea per Reel [U.97].
- Visuals that contradict the words. The book says the system cross-checks speech, text and picture [U.ch3].
- Banned CTAs and tactics: "link in bio", "buy now", tag-bait, false scarcity (E-2, E-3, E-4).
