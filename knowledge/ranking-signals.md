# Ranking Signals

This file covers what the books say decides reach, and how the Phase 1 skills turn it into content choices and the pre-publish scorecard.

**Citations:** `[F<part>.<n>]` Foundational · `[U.n]` 2026 Update · `[H.n]` Hook Engineering · `[U.chN]` chapter table/section.
**Confidence:** everything in this file is a **`book-claim`**. The books attribute several of these points to Adam Mosseri or Meta, but no outside source has been checked yet, so none of them is `platform-confirmed`. Conflicts are ruled in `conflicts-and-exclusions.md` (C-codes).

## Contents
1. [The signal-weight table (book's figures)](#1-the-signal-weight-table)
2. [How distribution unfolds](#2-how-distribution-unfolds)
3. [Positive signals: levers a post can pull](#3-positive-signals)
4. [Negative signals: what suppresses a post](#4-negative-signals)
5. [Length bands by goal](#5-length-bands-by-goal)
6. [Timing: before, at and after posting](#6-timing)
7. [The pre-publish scorecard](#7-the-pre-publish-scorecard)

---

## 1. The signal-weight table

> **Source: the book's figures (U, Chapter 1).** The book attributes this restructuring to Adam Mosseri. **This has not been verified against any Instagram or Meta source.** Use it as the book's model of priorities, not as a measured fact.

| Signal | Book weight | What it means | Book's role label |
|---|---|---|---|
| **Watch time** | 35% | Holding attention to the end; total seconds watched | Primary reach driver |
| **Sends per reach** | 20% | How often the post is sent by DM | Viral-spread trigger |
| **Saves** | 15% | Kept as a future reference | Authority signal |
| **Conversation depth** | 15% | Chained comment replies (more than 3 exchanges) | Community signal |
| **Likes** | 5% | Shallow interest | Secondary / vanity |

Source: [U.ch1]. U is inconsistent here: [U.2] lists watch time, *likes per reach* and sends as the top three. The ruling (C-3) is to use the table and never spend a CTA on likes.

The book's summary is that the platform treats content as "social currency": content that makes someone message a friend counts most, because it strengthens connections on the platform [U.ch1], [U.36] (claimed "5× ordinary engagement"), [U.conclusion.1] ("before posting, ask: who would a follower rush to send this to? If you can't answer, don't post").

---

## 2. How distribution unfolds

- **The audition.** A new Reel is first shown to a small group, including non-followers. If most of them get past about 3 s, it expands in waves. If they don't, distribution shrinks, even to your own followers [U.ch2], [U.119], [F1.24] (claims a first wave of 150–500 people), [F1.26].
- **Separate systems.** Feed (relationships and recency), Reels (watch time and sends), Stories (recency and relationship), Explore (interests and popularity) each rank differently [U.1], [F3.32]. The same Reel can do well in one and badly in another.
- **Smart matching.** The model "sees" frames, reads on-screen text and transcribes speech to decide who the post is for. Design each video for one person with one specific problem [U.ch1 Muse Spark], [U.117], [U.47].
- **Reaching non-followers needs five conditions:** no watermark, no guideline violations, high quality, not pushing users out of the app, and originality [U.5], [U.13]. Engagement from non-followers is the route into Explore [F1.30].
- **Early velocity.** Exceptional engagement in the first ~20 min supposedly moves a video onto faster "viral" servers [U.157]. This is low confidence; the practical rule is in §6.
- **Pattern doubling.** When a pattern works, the system pushes more of it to that audience, so repeat the winning pattern with variation [U.43], [U.134]. Repeating it too rigidly triggers user fatigue [U.122].

---

## 3. Positive signals

Grouped under the table signal each one feeds. Skills use this list to pick levers.

**Watch time (35%)**
- Re-watches and loops [F1.21], [F1.44], [U.121], [F2.27]
- Pausing, slowing the scroll, zooming in, device-motion "zoom" moments [F1.1], [U.34], [U.148]
- Turning the volume up manually [F1.1], [U.151]
- Re-hook at ~8 s and small rewards every few seconds [F2.26], [U.92], [U.106]
- Pattern interrupts every 4–6 s; cuts every 1–3 s where it suits [F2.45], [F2.49], [U.71], [U.131]
- Watchable without sound: on-screen text and captions, while keeping a sound layer [F1.19], [F2.12], [F2.28], [F2.48], [U.121] (the book claims 80%+ watch muted)
- Varied voice (whisper to strong, short pauses) [U.152]; a tone gradient across the video [F2.53]
- Total watch time beats completion: a longer Reel that holds attention wins [U.144]

**Sends (20%)**
- A specific send prompt naming who benefits [H.10], [U.36], [F1.34], [F2.15], [U.case:Indriya]
- Social-currency content that people share because it reflects their identity or expertise [U.88]
- "Ask the person next to you" prompts [U.156] (low-confidence mechanism, harmless prompt)

**Saves (15%)**
- Reference-grade content: specs, checklists, comparisons, steps [U.83], [U.105], [U.142], [H.cta]
- An explicit save prompt, early or at the end [F1.45], [U.67]
- Screenshot-worthy frames [U.149]

**Conversation depth (15%)**
- Open questions that need a sentence to answer [F2.41], [U.60], [U.123], [F3.1]
- Reply to every early comment with a follow-up question [U.35], [F2.25]
- Pin a useful comment [F3.34]
- The first ~10 comments carry extra weight [F1.38]. Earn them with real questions, never planted ones (E-6)
- Opening the comments counts even without typing [F1.32]

**Profile / DM intent (not in the table, but the book stresses it)**
- Profile visit and browsing after the Reel; "part 2 is on my page" [U.120], [F1.41], [F1.29]
- Tapping the DM button, keyword DMs [F1.33], [H.18], [H.22]
- Follower gain from the post [F3.9], but only followers who stay engaged [U.158]

---

## 4. Negative signals

| Signal | Effect claimed | Source | How skills avoid it |
|---|---|---|---|
| Fast scroll in the first seconds | Distribution stops | [F1.26], [U.51], [U.155] | Strong 0–3 s hook; no intros |
| "Not interested" taps | Sharp negative | [F1.25] | Avoid needless provocation (E-9) |
| Reports | Temporary visibility drop | [F2.21] | No misleading claims |
| Watermarks from other apps | Muted or reduced reach | [F1.6], [U.37], [U.5] | Clean exports only |
| Engagement bait | Hidden from Explore | [U.ch7] | Specific send prompts (E-2) |
| Ghost posting (volume without engagement) | Up to −40% reach | [U.ch7], [F3.15] | ≤1 strong Reel/day (C-4) |
| Aggregator reposting | Removed from recommendations | [U.ch7], [U.146] | Original content (E-8) |
| Niche drift | Up to −40% reach; users remove your topic | [F2.13], [U.4], [U.54] | Stay within the brand's `content_pillars` (max 3) |
| Off-niche followers who then ignore you | Account penalised | [U.158] | Content always serves the target buyer |
| Words contradicting the visuals | Ranking drops | [U.ch3] | Keyword consistency check (caption-seo-writer) |
| Excess complexity | Early drop-off | [U.41], [U.98], [U.49] | One idea per Reel [U.97] |

---

## 5. Length bands by goal

Ruling C-1: U beats F.

| Goal | Length | Why | Source |
|---|---|---|---|
| reach (new audience) | **7–30 s** | High completion on short Reels | [U.ch2], [U.8] |
| trust / education | **30–90 s** | Enough value without boredom | [U.ch2], [U.8] |
| lead / sale | **20–60 s** | Enough proof to earn a DM; still short enough for non-followers (editorial choice within U's bands) | [U.ch2], [U.144] |
| existing audience, strong story | 3–20 min | Won't reach Explore unless watch rate is high; the book says Reels over 3 min generally aren't recommended to non-followers | [U.ch2] |

If unsure, go shorter [F1.4], [F1.20].

---

## 6. Timing

- **Before posting:** 10 minutes of genuine activity: reply to comments, react to Stories in the niche [U.124], [F2.5]. A teaser Story or poll warms up the audience [F1.9], [F3.14].
- **When to post:**
  - About 15 minutes before the audience's peak [U.157].
  - At an odd minute (7:05 rather than 7:00) [U.21].
  - Emotional content at night or on weekend afternoons [F1.22].
  - Then adjust to your own Insights [F3.3], [U.21].
- **After posting (first 60 min):**
  - Share to Story straight away [F2.25], [F1.11].
  - Reply to the first comments with a follow-up question [U.35].
  - Stay in the app [F2.25].
  - Reshare to Story about 12 h later with a new angle [F2.14].

---

## 7. The pre-publish scorecard

`content-studio` writes `scorecard.md` for every package using this checklist. Each signal gets a score from 0 to 1, from the items met for it (count met ÷ count listed). The weighted total = Σ(book weight × score), out of 100.

**Mandatory disclaimer.** Copy it verbatim at the top of every scorecard:
> *These weights (Watch time 35 / Sends 20 / Saves 15 / Conversation depth 15 / Likes 5) are the figures from the source book (Instagram Secrets — 2026 Update, Ch. 1), which attributes them to Instagram. They have not been verified against any Instagram or Meta source. This is a pre-publish checklist of how well the package applies the book's model. It is not a prediction of reach.*

| Signal (book weight) | Checklist items |
|---|---|
| **Watch time (35)** | (1) Hook scores ≥ 9/12 on the rubric in `hook-formulas.md` §6 · (2) key visual in 0–3 s · (3) re-hook around 8 s · (4) pattern interrupt every 4–6 s · (5) length inside the goal band (§5) · (6) loop or cut-off ending · (7) works muted (on-screen text) *and* has a sound layer |
| **Sends (20)** | (1) Specific send prompt naming who benefits · (2) the content has an obvious recipient (the "who would they send it to" test [U.conclusion.1]) · (3) no generic tag-bait |
| **Saves (15)** | (1) At least one reference-grade element (spec, checklist, comparison) · (2) explicit save prompt · (3) a screenshot-worthy frame |
| **Conversation depth (15)** | (1) Open question that needs a sentence to answer · (2) pinned-comment plan · (3) 60-minute reply plan with follow-up questions |
| **Likes (5)** | (1) No CTA wasted on likes (the item is met when the package does *not* ask for likes) |

**Always add below the table, unscored:**
- Rule-safety pass (E-codes)
- Keyword consistency pass (voiceover, on-screen text and caption)
- Every `[NUMBER NEEDED]` placeholder still open
