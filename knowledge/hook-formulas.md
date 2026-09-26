# Hook Formulas

This is the hook library that `hook-writer` reads, and that `reel-scriptwriter` reads for re-hooks and endings. It restructures **H** (all 45 formulas plus the 3 closing collections) together with the hook and opening tactics scattered through **F** and **U**.

**Citations:** `[H.n]` = Hook Engineering formula n · `[F<part>.<n>]` = Foundational, Part, item · `[U.n]` = 2026 Update, item n · `[U.chN]` = Update chapter table or section.
**Confidence:** every entry here is a `book-claim` unless it is explicitly tagged otherwise. Percentages quoted from the books are the author's figures and have not been verified. Treat them as flavour, never as promises in client-facing copy.
**Precedence and bans:** see `conflicts-and-exclusions.md`. Where it disagrees with this file, that file wins.

## Contents
1. [How to pick a formula](#1-how-to-pick-a-formula)
2. [The 45 formulas (H.1–H.45)](#2-the-45-formulas)
3. [Closing collections (H.common, H.fomo, H.cta)](#3-closing-collections)
4. [Opening mechanics from F and U: first 0.5–5 seconds](#4-opening-mechanics-from-f-and-u)
5. [Re-hooks, endings and send/save prompts](#5-re-hooks-endings-and-sendsave-prompts)
6. [Hook quality rubric](#6-hook-quality-rubric)

---

## 1. How to pick a formula

Why the hook matters: every new Reel is first shown to a small test audience. If most of that audience doesn't get past the first ~3 seconds, distribution stops [U.ch2 "audition"; F1.24; F1.26]. The hook is judged on (a) whether it stops the scroll visually, (b) whether it is understood instantly, and (c) whether it creates a reason to keep watching.

**Step 1: filter by goal.** The brief's `goal` is one of `reach | trust | sale | lead`.

| Goal | What the hook must do | Strongest formulas (try first) | Also good |
|---|---|---|---|
| **reach** | Stop strangers; be sendable | H.3, H.2, H.16, H.10, H.6 | H.12, H.19, H.28, H.fomo |
| **trust** | Prove competence visibly | H.4, H.17, H.11, H.8, H.19 | H.9, H.14, H.37, H.40, H.43 |
| **sale** | Move a warm viewer to act *inside the app* | H.18, H.40, H.29, H.22 | H.26, H.20, H.36 |
| **lead** | Get a qualified buyer to start a conversation (DM/WhatsApp) | **H.31**, H.20, H.24, H.36, H.1, H.33 | H.15, H.35, H.39, H.25, H.22, H.18 |

**Step 2: filter by buyer type** (brand profile `buyer_type`). The *Fit* column in section 2 marks each formula `B2B`, `B2C` or `both`.
- **B2B viewers are resellers, buyers or operators.** Their pains are margin, returns and complaints from *their* customers, stock-outs and lead times, consistency between batches, price per unit versus quality, and looking good in front of *their* client. So rewrite each formula's "customer" as "your customer" (the end buyer) and speak to the *business* outcome [H.1 insight: precise pain]. Formulas that sell a lifestyle feeling (H.21, H.44) only work for B2B when reframed as "what your customers feel when they walk into your showroom".
- **B2C viewers are end users.** Speak to comfort, taste, status, identity and occasions.

**Step 3: pick 6–8 candidate formulas, write one hook per formula, then score them all with the rubric in section 6.**

**Step 4: attach the right ending.** Every hook implies an ending: a send prompt, a save prompt, or a DM/WhatsApp keyword. See section 5.

---

## 2. The 45 formulas

Format for each entry: **Idea** · **Why it works** · **Template** (fill the brackets) · **Source example** (one per formula, lightly compressed) · **Fit** · **Signal it mainly serves** (W = watch time, S = sends, V = saves, C = conversation depth, P = profile visit / DM).

### H.1 Precise Diagnosis
- **Idea:** Name the viewer's *exact* daily pain, not a generic one ("are your sales low?").
- **Why:** A precise diagnosis feels like being watched; trust and attention follow.
- **Template:** "If [very specific symptom], your problem isn't [obvious blame] — it's [hidden cause]."
- **Source example:** "If your customers order one coffee and sit four hours, your problem isn't overcrowding — it's your dessert menu design."
- **Fit:** both (B2B: the symptom happens in *their* business) · **Signal:** W, S

### H.2 Result First (transparency & numbers)
- **Idea:** Put the shocking result in second one, then explain how.
- **Why:** Numbers create instant trust plus curiosity about the method.
- **Template:** "[Change] → [number] [result] in [time]."
- **Source example:** A restaurant redesigned its lighting and menu → appetizer orders +47% in one month.
- **Fit:** both · **Signal:** W, V
- **Use only real numbers from the brand's proof points.** Never invent them (`conflicts-and-exclusions.md` E-5).

### H.3 Against the Current (breaking assumptions)
- **Idea:** Contradict a popular belief with strong logic; this positions you as the expert.
- **Template:** "Everyone says [belief]. In [year] that's exactly what [bad outcome]. The smarter move is [counter-move]."
- **Source example:** "Constant discounting is the fastest path to bankruptcy in 2026."
- **Fit:** both · **Signal:** W, C, S

### H.4 Proving Authority Practically
- **Idea:** Don't claim expertise; show it on camera, behind the scenes.
- **Why:** "Show them how you make it, and they'll choose what you make."
- **Template:** Open on the process or test, with on-screen text "[the test/step] before [we ship/finalise]".
- **Source example:** Filming the scratch-resistance test on leather before approving a bag design.
- **Fit:** both, **very strong for B2B/manufacturers** · **Signal:** W, V

### H.5 Quick Win (immediate implementation)
- **Idea:** A tiny tip the viewer can apply the instant the video ends.
- **Template:** "Do this one thing [before X] and [immediate benefit]."
- **Source example:** Spray perfume on two specific points before leaving the house.
- **Fit:** B2C mainly (B2B: a quick tip the reseller can use on their sales floor) · **Signal:** V, S

### H.6 The Hidden Cost of Bad Habits
- **Idea:** Show how an everyday habit quietly costs money, quality or comfort.
- **Template:** "[Common habit] is quietly costing you [money/quality] — here's [wrong vs right]."
- **Source example:** Delivery apps that use stock photos lose up to 50% of late-night customers.
- **Fit:** both · **Signal:** W, S, V

### H.7 Attraction Through Rejection
- **Idea:** "Not for everyone." This pulls in exactly the high-quality segment you want.
- **Template:** "This [product] isn't for [wrong customer]. It's made for [right customer] who [value]."
- **Source example:** A café that refuses Wi-Fi so people can disconnect.
- **Fit:** both (B2B: "we don't supply showrooms that compete on the cheapest price") · **Signal:** C, P

### H.8 The Simplified Case Study
- **Idea:** Dissect a *failure* and its fix rather than a plain success. The brain attends to risk.
- **Template:** "[Thing] was failing because [cause]. We changed [one thing] → [result]."
- **Source example:** A dessert display re-lit with warm biophilic lighting → +63% sales in a month.
- **Fit:** both · **Signal:** W, V

### H.9 The Tactical Lever
- **Idea:** A small tip today, a big result tomorrow (care, handling, usage).
- **Template:** "Don't [common action] — it [damage]. Do [correct action] instead."
- **Source example:** Keep steamed milk below 65 °C or it burns and ruins the flavour.
- **Fit:** both (B2B: handling, installation or storage tips resellers pass on) · **Signal:** V

### H.10 The Taste of Hidden Shares
- **Idea:** Write the opening line so the viewer thinks of a specific person and sends it by DM.
- **Template:** "Send this to your [specific person-type] who always [specific behaviour]."
- **Source example:** "Send this to your friend whose bag is always a mess."
- **Fit:** both (B2B: "send this to your partner who handles purchasing") · **Signal:** **S (top)**
- **Must name a specific person-type tied to the content.** Generic "tag someone" is banned (E-2).

### H.11 Destroying Alternatives
- **Idea:** A comparison or at-home test that exposes cheap or fake alternatives.
- **Template:** "[Real] vs [cheap]: [simple test] — watch what happens at [moment]."
- **Source example:** A metal zip pull vs a painted plastic one, 20 pulls each.
- **Fit:** both, **very strong for B2B quality proof** · **Signal:** W, S, V

### H.12 High Focus
- **Idea:** Tell the viewer to give full attention (a "secret method"); this raises completion.
- **Template:** "The [factory/pro] method to [result] in [short time] — watch to the end."
- **Source example:** A factory method that makes white shoes look new in three minutes.
- **Fit:** both · **Signal:** W

### H.13 Reverse Growth (trend resistance)
- **Idea:** Show you pick quality over hype by dropping a trendy item.
- **Template:** "We stopped [selling/making] [trendy item] because [quality reason]."
- **Source example:** Cancelling a best-selling mojito because the syrup masked real fruit.
- **Fit:** both · **Signal:** C, trust

### H.14 The Gap Hook (what happens after the sale)
- **Idea:** Focus on what happens *after* purchase.
- **Template:** "Most [sellers] disappear after payment. Here's what happens after you order from us: [step]."
- **Source example:** Thermal delivery packaging so food arrives crispy.
- **Fit:** both (B2B: after-sales, replacements, delivery handling) · **Signal:** trust, V

### H.15 Aggressive Reduction
- **Idea:** Fewer options prove mastery.
- **Template:** "We cut [N] options down to [n] — here's why that's better for you."
- **Source example:** Only 4 fragrances instead of 50.
- **Fit:** both · **Signal:** C

### H.16 Cognitive Contradiction (advice that seems crazy)
- **Idea:** Open with "don't buy this" or "don't do this"; the shock forces viewers to stay for the reason.
- **Template:** "Don't [buy/order] this if [condition] — it's made for [other use]."
- **Source example:** "Don't buy this bag if you need laptop space — it's for evenings only."
- **Fit:** both · **Signal:** W, C

### H.17 Precise Inspection (the smart buyer)
- **Idea:** Teach the small details that reveal real quality.
- **Template:** "Before you buy [product], check [detail] — [what good vs bad looks like]."
- **Source example:** The sole-bend test for real arch support; the paper test for perfume concentration.
- **Fit:** both, **top pick for B2B buyers** · **Signal:** V, S

### H.18 Frictionless Selling (link in bio, reimagined)
- **Idea:** Keep the whole purchase inside Instagram. Comment or DM a word and get the offer in DM.
- **Why:** The book says pushing users out of the app is penalised [H.18; U.5].
- **Template:** "Comment/DM '[word]' and we'll send you [offer/catalogue/price list] directly."
- **Source example:** "Send the word 'winter' via DM" → an automated, secure payment link valid 24 h.
- **Fit:** both · **Signal:** P, C
- WhatsApp variant for brands whose `cta_mechanism` is `whatsapp`: "Message '[word]' on WhatsApp". Say the number or show it on screen; don't say "link in bio".

### H.19 Predicting Disaster (warning backed by expertise)
- **Idea:** Warn about a mistake that will ruin the experience; you become their guardian.
- **Template:** "[Mistake] will [consequence] within [time] — most people don't notice until it's too late."
- **Source example:** Synthetic leather cracks within about three months.
- **Fit:** both · **Signal:** W, S

### H.20 Assassinating Discounts
- **Idea:** Use quality as a weapon: repel bargain hunters, attract buyers who value quality.
- **Template:** "This can't be sold at half price — here's what goes into it: [inputs/process]."
- **Source example:** A croissant made with European butter and three-day fermentation; no BOGO.
- **Fit:** both, **strong for B2B lead gen** (filters out price-only buyers) · **Signal:** C, P

### H.21 Engineering Absolute Loyalty
- **Idea:** "We're not just a store." Build belonging, not a transaction.
- **Template:** "[Environment/ritual] that makes your [customers] feel [emotion] the moment they [arrive/use it]."
- **Source example:** Biophilic décor and dim lighting that lower stress; a VIP early-preview list.
- **Fit:** B2C mainly (B2B: a VIP trade list with first access to new collections) · **Signal:** P

### H.22 Hidden Paths (the hidden sales structure)
- **Idea:** Sell quietly through a DM system (password word → qualify → personalised offer → close).
- **Components:** follow-up, a personalised solution, qualification, automated keyword replies, a smart invitation, cinematic content, smooth closing.
- **Template:** "Type '[word]' and [assistant/our team] will [recommend/send] [specific thing] in [time]."
- **Fit:** both · **Signal:** P, C

### H.23 The Illusion of Physical Assets
- **Idea:** The customer's experience starts at the first click, not in the physical space.
- **Template:** "You spent [on physical thing] — but your [online touchpoint] is losing them before they arrive."
- **Source example:** Luxury packaging is worthless if the online store is full of errors.
- **Fit:** both · **Signal:** C

### H.24 Upgrading the Customer
- **Idea:** Wait for customers frustrated by cheap options, then show the upgrade.
- **Template:** "'[Beautiful today], [problem tomorrow]' vs '[lasting benefit]'. Come to us when [trigger]."
- **Source example:** "Beautiful shoe today, pain tomorrow" vs "elegant medical comfort".
- **Fit:** both, **strong for B2B** (the reseller whose customers keep complaining) · **Signal:** C, P

### H.25 Quality Audience vs Fake Numbers
- **Idea:** The right audience beats big numbers.
- **Template:** "[Big vanity number] brought [nothing]. [Small right audience] brought [contracts/sales]."
- **Fit:** B2B mainly · **Signal:** C

### H.26 Intentional Friction
- **Idea:** Add a deliberate, meaningful step (waitlist, fixed size, limited run) to raise perceived value.
- **Template:** "You can't just [order X]. [Step] — because [quality reason]."
- **Source example:** A handmade bag with a waitlist and 8 hours of craft per piece.
- **Fit:** both (B2B: a minimum order or a showroom-qualification step, **only if true**) · **Signal:** P

### H.27 The Human Touch vs the Machine
- **Idea:** Human craft plus technology beats soulless automation.
- **Template:** "A machine can [fast/uniform thing]. Only [human craftsman] can [nuanced thing]."
- **Source example:** A hand-blended perfume vs a data-built formula.
- **Fit:** both · **Signal:** C, V

### H.28 Approved Fraud in Reports
- **Idea:** Expose number manipulation (vanity metrics vs acquisition cost, ROAS, LTV).
- **Template:** "If [supplier/agency] shows you [vanity metric] while [real cost] keeps rising — [action]."
- **Fit:** B2B · **Signal:** C, S

### H.29 Selling Without Clicks
- **Idea:** Put selling and payment inside the DM conversation.
- **Why:** The book claims forcing customers off-platform loses up to 40% of sales.
- **4 steps:** chat path/bot → present products in chat → payment in chat → confirm and deliver.
- **Template:** "Never say 'link in bio' — say '[word]' in the comments and get [offer] in your DMs."
- **Fit:** both · **Signal:** P

### H.30 The Silent Assassination of Free Services
- **Idea:** Free attracts the curious, not buyers. Replace "free" with a paid diagnosis.
- **Template:** "We stopped offering free [X]. Now [paid diagnosis] — and only serious [buyers] come."
- **Fit:** B2B / services · **Signal:** C

### H.31 Reverse Price Engineering (escaping the price-comparison trap)
- **Idea:** Customers compare prices when your offer looks like a commodity. Sell an integrated *solution*, not a part.
- **Why:** Integrated solutions can't be compared line by line.
- **Template:** "You're not buying [a commodity unit] — you're buying [complete solution: X + Y + Z] that saves you [pain/cost]."
- **Source example:** "Clients don't pay for 'a consultation' — they pay for 'a system that saves them from financial bleeding'."
- **Fit:** **B2B top pick for price-led lead generation** · **Signal:** C, P
- **B2B use:** reframe price per unit as total cost to the reseller (returns, complaints, installation issues, delivery damage, dead stock).

### H.32 The Futility of Individual Talent
- **Idea:** Engineered systems outperform a human army.
- **Template:** "More [staff] won't fix [problem]. [System] does it [faster/without errors]."
- **Fit:** B2B · **Signal:** C

### H.33 Pre-Diagnosis
- **Idea:** Predict with authority where the business will stall.
- **Template:** "Give me [5 minutes] with your [numbers/showroom] and I'll tell you [exactly where you're losing money]."
- **Fit:** B2B · **Signal:** P, C

### H.34 Building Independent Assets
- **Idea:** 100% dependence on a platform is fragile. Build an owned list (email/WhatsApp).
- **Template:** "If all your [sales] depend on [platform], you don't own your business — [owned channel] does."
- **Fit:** both · **Signal:** P
- Pairs naturally with a WhatsApp CTA.

### H.35 Focus on Net Profit, Not Gross Sales
- **Idea:** Talk margin, not revenue.
- **Template:** "[Big revenue] with [thin margin] because [waste/low-margin mix]. Fix [lever] → margin [up]."
- **Fit:** B2B · **Signal:** V, C

### H.36 You're Not Selling an Ordinary Product
- **Idea:** Premium experience vs commodity comparison.
- **Template:** "We're not selling [commodity] — we're selling [lasting outcome/experience]."
- **Source example:** "Not a hoodie for one season — armour for successive seasons."
- **Fit:** both · **Signal:** C

### H.37 Systems Outperform Individuals
- **Idea:** Consistent quality comes from systems, not moods.
- **Template:** "The secret to [consistent result] isn't [talented person] — it's [system/QC step]."
- **Fit:** both, **strong for manufacturers** (QC, batch consistency) · **Signal:** trust

### H.38 Building Your Own Community
- **Idea:** Drive people to your own list or group; members get new releases first.
- **Template:** "New [collections] go to our [WhatsApp list] first — before any public post."
- **Fit:** both · **Signal:** P

### H.39 Reducing Waste
- **Idea:** Cutting losses raises profit more than adding volume.
- **Template:** "Celebrating more [orders]? [Hidden leak] eats up to [x]% of it."
- **Fit:** B2B · **Signal:** V, C

### H.40 Pre-Purchase
- **Idea:** People decide to buy from what they *see* before the price.
- **Template:** Open with the proof visual (e.g. water sliding off fabric) and on-screen text "this is where the decision happens".
- **Source example:** A clean-kitchen behind-the-scenes video before customers ever smell the food.
- **Fit:** both · **Signal:** W, P

### H.41 Simplicity as Luxury
- **Idea:** Fewer options mean more clarity and more confidence.
- **Template:** "We cut from [20] to [4] [options] that [match everything]."
- **Fit:** both · **Signal:** V

### H.42 Focus on the Loyal/Repeat Customer
- **Idea:** Repeat customers are the real metric.
- **Template:** "[Viral number] didn't matter. [Specific repeat customer] who [ritual] does."
- **Fit:** both · **Signal:** C

### H.43 The Protocol of Firing Customers
- **Idea:** Refusing bad-fit orders proves you're strong and in demand.
- **Template:** "Why did we turn down [a big order]? Because they asked us to [lower quality]."
- **Fit:** both, **strong for B2B** · **Signal:** C, S

### H.44 You're Not Just a Store
- **Idea:** Tie the product to identity; customers become defenders.
- **Template:** "We don't sell [product] — we sell [identity/feeling]."
- **Fit:** B2C mainly · **Signal:** C, S

### H.45 The Post-Purchase Void
- **Idea:** Care after payment creates advocates.
- **Template:** "After you [receive it], you'll get [care card/video message] showing [how to keep it perfect]."
- **Fit:** both · **Signal:** trust, P

---

## 3. Closing collections

### H.common — Common Hooks (quick reference)
Short before/after hooks:
- "The fault isn't [obvious blame] — it's [cheap component]." (the thermal packaging example)
- "[Common method to go faster] is actually the fastest way to destroy [product]. Here's the engineered method."
- "Everyone orders [X] but no one tells you the real difference between it and [Y]."
- Save/share lines: "Save this reference." · "Share this with your [person] who always asks about [topic]." · "Screenshot this [chart/table] before ordering tonight."

### H.fomo — Curiosity hooks driven by fear of missing out
Short, urgent openers, each paired with a one-line consequence:
- "No one tells you the truth about [overlooked problem]." → "Ignore it now and regret it later."
- "Do you know what happens if you [common mistake]?" → "One simple mistake ruins [the expensive thing]!"
- "I tried [X this way] — the result was shocking." → "Avoid this common mistake!"
- "What if you missed [rare thing] and never noticed the difference?" → "A chance that may not repeat!" (only if genuinely limited: E-4)
- "Most people [choose X] wrong — here's the secret." → "Most people order it wrong!"
- **Closing insight:** "What will it cost me to ignore this information?"

### H.cta — Calls to action (closing page)
- **Reference-card CTA:** a complete, precise reference (recipe, size chart, spec table) plus "Save this reference to apply it [next occasion]."
- **Builder CTA:** "Click here to build a complete [capsule/set]."
- **Comparison CTA:** commercial vs specialty table plus "Send this analysis to your [friend-type] if [pain]."
- **Screenshot CTA:** hours and size chart plus "Screenshot this and apply it tonight." (This also matches the screenshot signal [U.149].)

---

## 4. Opening mechanics from F and U

These are the craft rules for the first 0.5–5 seconds. Apply them on top of whichever formula is chosen.

| Rule | Detail | Source |
|---|---|---|
| Win the first ~0.5–1.7 s | Viewers decide to stay or scroll almost instantly. Open on movement, colour, or a shocking line; no intros or greetings | [U.118], [U.20], [U.51] |
| Pass the ~3 s audition | Put the single most important piece of information or visual in the first 3 s | [U.ch2], [F1.26], [F1.24] |
| The first 5 s decide the fate | A strong line plus striking motion or a lighting change | [U.44], [U.131] |
| Instant clarity (≤1 s to understand) | One idea, large text, no complex graphics | [U.41], [U.89], [U.127], [U.49] |
| Explicit promise | State what the viewer gains, on screen, from second one | [U.50], [U.125] |
| Open loop / mental tension | An unresolved question or incomplete fact; the answer lands **no sooner than ~3 s** in | [U.45], [F2.6] |
| Paradox / belief-shaking | A title that defies expectation, backed by evidence | [U.46], [U.53], [U.61], [U.128], [F2.50] |
| Loss framing | Fear of loss beats desire for gain; name the costly mistake | [U.104], [U.99], [H.19] |
| "You" in the first 5 words | Direct address raises comments | [F2.34], [U.117] (speak to one person with one problem) |
| Spoken keyword early | Say the topic keyword aloud in the first seconds; transcripts feed search and categorisation | [U.40], [U.143], [F2.16], [F2.36] |
| Strong movement or hard cut in frame 1 | Classified as high-attraction | [F1.13], [F2.17], [U.137] |
| Strongest moment first | Put the best 3–5 s shot up front as a preview, then continue | [F1.31], [F2.38], [U.125] |
| Visual pattern break | Unexpected text or an odd visual so the thumb pauses | [F1.43], [F2.45] |
| Early save trigger | "You'll need this later — save it now" | [F1.45], [U.67] |
| Sound-on bait | An intriguing visual plus text that makes viewers turn the sound on | [U.151] |
| Face, expression, gesture | Front camera, raised brows, hand gestures in the opening | [F2.18], [F2.33], [F2.52], [U.68], [U.137] |
| Emotional charge | Charged words beat neutral ones ("a disaster most commit" > "a common mistake") | [U.99] |
| FOMO / insider secret | "Most people don't know…" (true claims only) | [U.129], [U.55], [H.fomo] |
| Self-reflection | "Are you ignoring…?" drives saves | [U.48], [U.135] |
| Expectation → outcome → shock | Promise N steps, deliver them, then add a surprising extra at the end | [U.93] |
| Direct, wrong vs right | Lead with the outcome, then the context; "don't do X if you want Y, here's why" | [U.136] |
| Experiential authority | "Here's what I did… and here's the result" beats theory | [U.86], [U.57] (the sacrifice/investment made) |
| Failure first | Open on the failure, then the turnaround | [U.76], [F2.38], [H.8] |
| Micro-story | Problem + feeling + solution, told candidly | [U.130], [U.107], [U.74] |
| Comparison | "X or Y — which one actually wins?" drives discussion | [U.73], [H.11] |
| Rapid-fire Q&A | Fast question → answer beats | [U.94] |
| Familiar thing, unfamiliar angle | Avoid recycled trend angles; show the flaw or the hidden side | [U.96], [U.101] |
| Intentional mystery / series | "More in the next part" gives a reason to follow | [U.75], [U.85], [F1.17] |
| On-screen commentary | "My reaction when I found out…" text beside your face | [F2.39] |
| Surprise interactive element | "Tap to find out" / "zoom in to see it" | [U.59], [U.148] |

---

## 5. Re-hooks, endings and send/save prompts

**Re-hook at ~8 s.** Re-spark curiosity before focus drops ("but first you need to understand this…") [F2.26]. Add a "small reward" every few seconds [U.92], [U.106].

**Endings** (choose one per Reel):
- **Loop:** the last line or motion sets up the first, so the Reel replays [U.121], [F2.27], [U.ch2 "Hook and Loop"].
- **Smart cut-off:** cut before the meaning completes; the caption says "watch from the start" [F1.44], [U.155] (avoid a "goodbye" ending, which triggers a fast swipe).
- **Open question:** a debatable, specific question that invites long replies [F2.41], [U.60], [U.123], [U.42].
- **Decisive action:** "Now try X and tell us the result" [U.114], [U.132].

**Send prompts** (the heaviest distribution signal in the book's table; see `ranking-signals.md`):
- "Send this to [specific person-type] who [specific need]" [H.10], [U.36], [F1.34], [F2.15], [U.case:Indriya].
- B2B: "Send this to whoever handles purchasing at your showroom", "Send this to your partner before your next order".
- Must be specific. "Tag someone who…" is bait and banned (E-2).

**Save prompts:** "Save this to check before your next order" [U.67], [U.105], [U.142]. Save prompts work best on reference-grade content: specs, checklists, comparisons [H.cta], [U.83].

**DM / WhatsApp / comment keyword prompts:** "DM '[word]'" or "WhatsApp '[word]'" for [the price list/catalogue] [F1.33], [H.18], [H.22], [H.29]. Prefer these to "link in bio" (E-3).

**Comments-open trigger:** "Notice the detail at 0:04? Tell me in the comments" [F1.32], [U.34].

**Screenshot prompt:** "Screenshot this spec table" [U.149], [H.cta].

---

## 6. Hook quality rubric

`hook-writer` scores every candidate hook from 0 to 2 on each criterion. The maximum is 12.

| # | Criterion | 0 | 1 | 2 | Source |
|---|---|---|---|---|---|
| 1 | **Scroll-stop (visual, 0–1.7 s)** | Static or talking-head intro | Some motion | Strong motion, contrast, or unusual first frame | [U.118], [F1.13] |
| 2 | **1-second clarity** | Needs context | Clear after reading twice | Instantly understood | [U.41] |
| 3 | **Specificity** | Generic ("amazing tip") | Semi-specific | Exact symptom, number or object | [H.1], [H intro] |
| 4 | **Keyword early** | Topic keyword absent | In on-screen text only | Spoken *and* on screen in the first 3 s | [U.40], [U.ch3] |
| 5 | **Send-ability** | No one to send it to | Vague audience | Obvious specific recipient | [U.36], [H.10] |
| 6 | **Rule-safe** | Bait, false claim, or "buy now / link in bio" | Borderline wording | Clean | `conflicts-and-exclusions.md` |

**A hook with a 0 on criterion 6 is disqualified** whatever its total. Recommend the top 3 by total; break ties on criteria 1 and 5.
