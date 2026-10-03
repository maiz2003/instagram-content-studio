# Conflicts & Exclusions

This file is the referee. Every skill checks its output against it, and where another knowledge file disagrees, this file wins.

**Why it exists:** the three books were written at different times and often contradict each other. A few tactics in them are also manipulative, deceptive or against Instagram's terms of use. Copying the books uncritically would produce content that is inconsistent at best and damaging to the account at worst.

**Citations:** `[F<part>.<n>]` Foundational · `[U.n]` 2026 Update · `[H.n]` Hook Engineering · `[U.chN]` a chapter table/section.
**Confidence tags:** everything here is a `book-claim` unless it cites an outside source. **No outside sources have been added yet** (Phase 1). The rulings below are editorial decisions about *how to use* the book claims, not verified facts about Instagram.

---

## 1. Precedence rule

When sources disagree, **U (2026 Update) beats F (Foundational) and H (Hook Engineering)**. U is the latest, and it explicitly supersedes the "old algorithm" F describes [U intro]. If U contradicts itself, the ruling for that case is recorded below.

---

## 2. Conflict rulings (C-codes)

| Code | Topic | What the sources say | Ruling used by skills |
|---|---|---|---|
| **C-1** | Reel length | F: 7–12 s for trends, 17–22 s for educational [F1.4]; each second past 30 s cuts reach 10–15% [F1.20]. U: under 30 s to reach new people, 30–90 s for education, 3 min+ only with a strong story; **total watch time beats completion rate** [U.8], [U.ch2], [U.144] | Use the U length bands by goal (see `ranking-signals.md` §5). F's numbers only as a tie-breaker ("shorter when unsure"). |
| **C-2** | Hashtags | F: hashtags matter less than keywords [F2.42]; local hashtags help [F3.22]. U: "hashtags are dead, keywords are king" [U.6]; use only a small number [U.143]; but U's own Oman example uses 6 [U.ch3] | **0–3 hashtags**, all highly specific (niche + location). Keywords in the caption's first sentence do the real work. |
| **C-3** | Which signal matters most | F: saves are the highest-value signal [F1.14]; a DM after a Reel is the "highest form" [F2.15]. U table: Watch time 35 / Sends 20 / Saves 15 / Conversation depth 15 / Likes 5 [U.ch1]. U also names the top three as watch time, *likes per reach* and sends [U.2], which contradicts the table's 5% for likes | Use the U.ch1 table as the book's weighting, **labelled as the book's figure** (see `ranking-signals.md`). Order of priority: watch time > sends > saves ≈ conversation depth > likes. Don't ask for likes. |
| **C-4** | Posting frequency | F: no more than 1 Reel/day unless you're a major brand [F3.39]; "posting without intent" is punished [F3.15]. U: posting 3×/day with no engagement = "ghost posting", −40% reach [U.ch7]; a few high-quality posts a week [U.126], [U.110], [U.conclusion.3] | **At most 1 Reel/day, and only when it's strong.** Skip a slot rather than post filler. |
| **C-5** | Carousel vs Reel engagement numbers | U says carousels get 10.15% vs 1.23% for Reels [U.7], [U.20], then cites Buffer at 6.9% vs 3.3% [U.case lessons] | Don't quote either number in client-facing copy. Direction agreed by both: carousels drive saves and engagement, Reels drive reach. |
| **C-6** | Editing inside the Instagram camera or the Edits app | F: in-app camera gives a hidden boost [F1.23], [F2.22]. U: Edits gets an extra distribution boost [U.29], **but** "no official confirmation it boosts reach" [U.15]; outside content isn't penalised, only watermarks are [U.37] | Recommend Edits or in-app finishing as *optional good practice* (retention graph, teleprompter). **Never promise a boost.** No watermark is a hard rule. |
| **C-7** | Early-engagement window | 30 min [F1.8]; "first minutes" [F2.19]; 60 min [F2.25]; first hour decides 60% [U.35]; first 20 min [U.157] | Post-publish protocol: engage 10 min **before** posting [U.124], [F2.5]; post ~15 min before audience peak [U.157]; stay active for 60 min after [F2.25], [U.35]. |
| **C-8** | Shadowban | F: silent mutes and flags [F1.6], [F2.21]. U: the shadowban concept is over; check **Account Status**. If it's green, the problem is content or the hook [U.147] | Diagnose with Account Status first (full protocol in Phase 2's `recovery-protocol.md`). |
| **C-9** | Commercial intent | F: phrases like "buy now" or "click the link" reduce organic reach [F1.5], [F1.7]. F: content tied to a commercial *need* gets pushed to shopping audiences [F2.51] | Tie the content to a real need or problem (F2.51), but close with a DM/WhatsApp/comment keyword, **never** "buy now" or "link in bio" (see E-3). |
| **C-10** | Emoji comments vs deep comments | F: emoji-only comments are a strong positive signal [F1.36]. F and U: long, specific comments count more [F3.40], [U.123]; conversation depth is weighted 15% [U.ch1] | Ask questions that need a sentence to answer. Emoji prompts only as a light secondary option. |
| **C-11** | Trending vs original audio | Trending audio reaches followers of that sound [F1.3], [F1.15]. Original voice or voiceover gets a small boost [F1.10]; originality score [U.13]; don't reuse the same sound more than 3 times [F2.20] | **Original voiceover is primary.** Optional low-volume music from Instagram's library. Vary the sounds. |
| **C-12** | Audition thresholds | F: first 150–500 viewers need a 90%+ watch rate [F1.24]; >30% scrolling in 3 s kills it [F1.26]. U: >50% must pass the first 3 s [U.ch2] | Use U's framing: **win the first 3 s**. Don't cite exact percentages to clients. |
| **C-13** | Saying "Instagram"/"AI" in the video | F: naming the platform or AI may reduce reach [F2.29]. No contradiction, but low confidence | Prefer "the platform" / "the algorithm" in voiceover and on-screen text. Low priority. |
| **C-14** | Profile tinkering (renaming, bio swaps every 48 h, total refresh every 10 days) | [F4.18], [F4.32], [F4.41] claim a "re-test" boost; U stresses a **fixed identity** [U.54] | Deferred to Phase 2 (`profile-architecture.md`). Default is a stable identity. |

---

## 3. Excluded tactics (E-codes): never recommend

These stay listed so nobody "rediscovers" them from the source files. Skills must not recommend them, and must reject a brief that asks for them. When rejecting, explain why and offer the compliant alternative.

| Code | Excluded tactic | Source | Why excluded | Compliant alternative |
|---|---|---|---|---|
| **E-1** | Secondary or fake accounts that watch, rewatch, comment, save and DM your own Reel | [F1.42] | Inauthentic behaviour against Instagram's terms; U itself says artificial engagement is detected and penalised [U.100], [U.138] | Real audience priming: a teaser Story or poll before posting [F1.9]; close-friends early access [U.12] |
| **E-2** | Generic engagement bait: "tag someone who loves their mom", guilt lines ("don't scroll without helping it spread", as in F1.43's "like beggars do" example) | [U.ch7], [F1.43] | U says bait is detected and hidden from Explore [U.ch7]; it also cheapens the brand | A **specific** send prompt that names who benefits and why [H.10], [U.36] |
| **E-3** | "Buy now", "click the link", "link in bio" as the main CTA | [F1.5], [F1.7], [H.18], [H.29] | Commercial wording and sending users off-app reduce reach (book-claim) | DM keyword, WhatsApp keyword, or comment keyword per the brand's `cta_mechanism` |
| **E-4** | False scarcity or urgency ("only 3 left" when untrue; "link active 2 days only" when it isn't) | [F4.29] ("even if it's not entirely true"), [F4.12] | Deceptive to buyers; can break consumer-protection law; destroys B2B trust | Real limits only (a real production run, real deadline, real MOQ), stated exactly [U.55], [U.70] |
| **E-5** | Invented numbers, results, testimonials or case studies presented as the brand's own | Pattern risk in [H.2], [H.8], [U.74] | Fabricated proof is deceptive | Use `products[].proof_points` from the brand profile. If a hook needs a number the profile lacks, output `[NUMBER NEEDED: …]` as a placeholder for the human to fill |
| **E-6** | Engagement pods, bought likes/followers/views, coordinated planted early comments | [F1.38] (secondary accounts leaving comments), [U.100] | Against Instagram's terms; U says it's penalised | Reply fast to *real* comments; pin a genuinely useful comment [F3.34]; ask real questions |
| **E-7** | Invisible white text in the bio to stuff keywords | [F4.16] | Hidden manipulation; keyword stuffing | Put keywords visibly in the name field and bio's first line [F4.2], [U.6], [U.ch3] |
| **E-8** | Reposting other creators' content (even with watermarks stripped) as your own | [F1.6] (tooling), [U.5], [U.13], [U.ch7 aggregator penalty] | Unoriginal content is penalised; also a copyright issue | Film your own version, or use Remix and add your own analysis [U.146] |
| **E-9** | Content designed to trigger reports or outrage for reach | Implied risks in [F1.25], [F2.21], [U.56] | "Not interested" taps and reports suppress reach | Organised critique that always ends in a solution [U.56] |

---

## 4. Self-check before any output leaves a skill

1. Does anything match E-1 … E-9? If yes, rewrite it.
2. Does any number, result or testimonial lack a source in the brand profile? If so, replace it with `[NUMBER NEEDED: …]` (E-5).
3. Is the CTA the brand's `cta_mechanism`, with no "link in bio" or "buy now"? (E-3)
4. Is every share prompt specific (who + why), not "tag someone"? (E-2)
5. Did any conflicting guidance get used? Apply the C-ruling.
