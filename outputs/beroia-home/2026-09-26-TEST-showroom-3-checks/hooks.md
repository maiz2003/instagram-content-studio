> **TEST DATA — not a real post.** Smoke test of the Phase 1 pipeline.

# Hooks: beroia-home · TEST-showroom-3-checks
Goal: lead · Buyer: B2B (showroom owners) · Format: Reel · Language: Arabic (Egyptian), English gloss in brackets

| # | Formula | Spoken line (Egyptian Arabic) [English gloss] | On-screen text (≤7 words) | First frame (0–1 s) | Signal | Score /12 |
|---|---|---|---|---|---|---|
| 1 | H.31 Reverse Price Engineering | "إنت مش بتشتري وحدة حمام أرخص بـ[NUMBER NEEDED] جنيه… إنت بتشتري مرتجع وزبون زعلان." [You're not buying a bathroom unit that's [X] EGP cheaper… you're buying a return and an angry customer.] | الأرخص بيكلفك أكتر [The cheapest costs you more] | QC inspector slaps a red "reject" tag on a unit, hard cut | C, P | 10 |
| 2 | H.1 Precise Diagnosis | "لو الزبون بيرجعلك بعد التركيب بأسبوع يشتكي… المشكلة مش في السبّاك، المشكلة في المصنع اللي جبت منه الوحدة." [If your customer comes back a week after installation complaining… the problem isn't the plumber, it's the factory you bought the unit from.] | مش غلطة السبّاك [Not the plumber's fault] | Extreme close-up of a unit joint under an inspection light | W, S | 10 |
| 3 | H.11 Destroying Alternatives | "وحدتنا ووحدة أرخص… نفس الاختبار. بص حصل إيه عند الثانية العاشرة." [Our unit vs a cheaper one, same test. Watch what happens at second 10.] | نفس الاختبار… نتيجة مختلفة [Same test… different result] | Two unbranded units side by side on the test rig | W, S, V | 10 |
| 4 | H.4 Proving Authority | "قبل ما أي وحدة حمام تخرج من المصنع… لازم تعدّي الاختبار ده." [Before any bathroom unit leaves the factory, it has to pass this test.] | وحدة الحمام قبل ما توصلك [The bathroom unit before it reaches you] | The test already running: [TEST NAME NEEDED] | W, V | 10 |
| 5 | H.17 Precise Inspection | "قبل ما تعرض أي وحدة حمام في معرضك… افحص التلات حاجات دول." [Before you display any bathroom unit in your showroom, check these three things.] | وحدة الحمام: ٣ فحوصات قبل العرض [Bathroom unit: 3 checks before display] | Finger taps the unit's edge; fast push-in | V, S, W | **11** |
| 6 | H.20 Assassinating Discounts | "مش هنقدر ننزّل السعر… وده السبب." [We can't lower the price… and here's why.] | ليه مش بنكسر السعر [Why we don't cut the price] | Raw material going into the line | C, P | 7 |
| 7 | H.24 Upgrading the Customer | "حلوة في المعرض النهارده… ومرتجع عندك بكرة." [Looks good in the showroom today… a return at your door tomorrow.] | حلوة النهارده… مرتجع بكرة [Nice today… returned tomorrow] | Split screen: shiny unit / unit being boxed for return | C, S | 10 |
| 8 | H.43 Firing Customers | "رفضنا طلبية كبيرة… لأن التاجر طلب نقلّل الخامة." [We turned down a big order… because the trader asked us to cut the material.] (**use only if true**: [TRUE STORY NEEDED]) | رفضنا الطلبية دي [We turned this order down] | Owner shaking his head at the camera | C, S | 8 |
| 9 | H.19 Predicting Disaster | "لو الوحدة مش متغلّفة كده… هتوصلك مكسورة." [If the unit isn't packed like this… it reaches you broken.] | كده بتوصل سليمة [This is how it arrives intact] | Packing a corner guard in fast motion | W, V | 9 |
| 10 | H.10 Hidden Shares | "ابعت الفيديو ده لشريكك اللي بيختار المورّد على السعر بس." [Send this to your partner who picks suppliers on price alone.] | لشريكك اللي بيشتري بالسعر بس [For your partner who buys on price alone] | Wide shot of the factory line, fast push-in | S | 9 |

Rubric detail (stop · clarity · specific · keyword · send · safe):
- 1: 2·2·1·1·2·2. Number missing; keyword spoken but not on screen
- 2: 1·2·2·1·2·2
- 3: 2·2·1·1·2·2. Needs a real comparison test the factory can film; no competitor names
- 4: 2·2·1·2·1·2. Test name missing
- 5: 1·2·2·2·2·2
- 6: 1·2·1·0·1·2
- 7: 2·2·1·1·2·2. Needs return footage (not in assets)
- 8: 1·2·2·0·2·1. Safe only if the story is true (E-5)
- 9: 1·2·2·1·1·2
- 10: 1·2·2·0·2·2

## Top 3
1. **#5 H.17 Precise Inspection (11/12).** Speaks straight to the showroom owner's own risk. The content is reference-grade (a checklist, so it earns saves), and it's fully filmable in the QC area. Paired ending: "ابعت الفيديو ده لشريكك اللي بيستلم البضاعة" [send this to your partner who receives the stock] + WhatsApp keyword for the trade price list.
2. **#1 H.31 Reverse Price Engineering (10/12).** The lead-goal pick: it reframes unit price as total cost. Needs a real price gap to be specific. Paired ending: WhatsApp keyword "for the full cost comparison".
3. **#3 H.11 Destroying Alternatives (10/12).** The strongest visual, but only if the factory can run and film an honest side-by-side test. Paired ending: save prompt + send prompt.

**Test run: the orchestrator auto-picked #5**, per the brief note.

## Open items
- [NUMBER NEEDED: typical price gap vs cheaper units] (#1)
- [TEST NAME NEEDED] (#4) · [TRUE STORY NEEDED] (#8)
- Return footage isn't in `assets_available` (#7)
