# Algorithm Mechanics

This is the book's model of how Instagram decides who sees what: the systems, how an account is classified, the behaviours it rewards and the claims about hidden mechanics. It's context for every skill, and the diagnostic base for `growth-recovery-doctor`. Signal weights and scoring live in `ranking-signals.md`.

**Citations:** `[F<part>.<n>]` · `[U.n]` · `[U.chN]`. **Everything is a `book-claim`.** Many items are "leaks" or tests the book reports; none has been verified. Confidence notes: **(low)** = a mechanism the book asserts with little support, so only use it where it's harmless.

## 1. The big picture
- **Meaningful distribution:** the platform rewards content that keeps people in the app, sending, returning and talking, not noise [U.intro], [U.ch1], [U.conclusion]. "The algorithm doesn't love good content. It loves content that keeps people inside the app" [U.closing].
- **Cooperate; don't cheat.** The algorithm is a mirror of content quality and human behaviour. Hacks backfire [U.115], [U.116], [U.138].
- **The multimodal model ("Muse Spark")** reads frames, objects, text and speech to match content to precise audiences [U.ch1], [U.117]. Design for one person with one problem [U.117], [U.ch1 tactic].

## 2. Four separate systems [U.1], [F3.32]
| Surface | Ranks mainly on | What to post there |
|---|---|---|
| Feed | Relationship + recency with accounts you follow | Personal / behind the scenes; carousels |
| Reels | Watch time + sends | Short hooks built to be shared |
| Stories | Recency + relationship strength | Daily life, polls, DMs |
| Explore | Interests + general popularity; non-follower engagement | Broad or trending angles within the niche [F1.30] |

The same post can do well in one surface and badly in another [F3.32].

## 3. Distribution flow
- **The audition:** a small test audience (including non-followers), then waves if the first seconds hold [U.ch2], [U.119], [F1.24].
- **Seed content (low):** some accounts' first Reel gets pushed to a test audience whatever their follower count; the chance doesn't repeat unless performance is strong [F1.2].
- **Early velocity:** engagement in the first minutes to hour multiplies the push [F2.19], [U.35], [U.157] (low: the "CDN migration" framing).
- **Pattern doubling / fatigue:** winning patterns get repeated to the audience; repetitive style gets reduced [U.43], [U.122].
- **Dynamic audience fingerprint:** changing setting and style reaches new segments [U.47]. Bridging two niches makes you a pivot node [U.153].

## 4. How the account is classified
- **Niche identity:** stay within ≤3 related topics. Users can remove topics from "Your Algorithm" [U.4]. Niche drift can cost up to 40% of reach [F2.13]. Keep a fixed visual and tonal identity [U.54].
- **Content type classification:** entertainment / educational / ad [F2.24]. Commercial intent is detected [F1.5], [F1.7], [F2.51] (C-9).
- **Account type:** Creator is favoured for reach; Business for ads/shop control [F2.30], [F2.3]. Temporarily removing contact buttons when not selling (low) [F2.3].
- **Desktop views read as business content (low)** [F2.1].
- **Off-app browsing informs interest classification (low)** [F2.46].
- **Faces:** the book claims facial recognition boosts familiar accounts (low) [F3.26]. Image emotion classification [F3.25].
- **Language/dialect → geographic circles** [F1.37], [F3.41], [F4.11].

## 5. Behaviour the system rewards (the account, not just the post)
- **Social activity:** replying, commenting on others, watching Stories and using features. The book frames it as earning "points"; accounts inactive with followers for 24 h are down-ranked [F2.5].
- **Before-posting warmth:** ~10 minutes of genuine engagement before posting [U.124].
- **After posting:** stay for 60 minutes, share to Story, reply fast [F2.25], [U.35].
- **Using native tools:** in-app camera, Edits, AR effects, templates, stickers, Notes, Live (all low as boosts) [F1.23], [F2.22], [F2.11], [F3.19], [F4.40], [F3.29].
- **Live:** regular Lives lift the visibility of other content [F3.29]; live Q&A raises watch time [F3.17].
- **Story ↔ Feed linkage:** any Story interaction links the two accounts and raises future Feed visibility [F3.31], [F3.33], [U.ch6]. Morning Story engagement lifts same-day Reels [F3.14]. Linking Reels and Stories raises total engagement time [F3.24].
- **Allow resharing to Story:** disabling it reduces natural spread [F2.8].
- **Stable engagement rate (4–6%)** keeps an account in continuous organic distribution (book's figure) [F3.6], [F3.36].
- **Notifications:** followers with post notifications on give fast early engagement; the book mentions a tested "personalised notifications" feature (low) [F3.5].
- **Video over photo** since 2023; photos compete only when rare, story-driven or set to music [F3.30]. Carousels beat single images and get shown more than once to the same user [F3.11].

## 6. Hidden-mechanic claims (low confidence; use only where harmless)
| Claim | Source |
|---|---|
| A cumulative creator "points" programme unlocks free visibility and partner offers for clean, consistent accounts | [F2.2] |
| Meta ad performance affects organic reach (good campaigns lift it, bad ones hurt) | [F3.12] |
| Device motion, zooming, sound-on and clipboard/screenshot actions count as signals | [U.148], [U.151], [U.149], [U.34] |
| Same-network / nearby sharing counts as the strongest social signal | [U.156] |
| File bitrate/metadata is read as a quality signal | [U.150] |
| Naming "Instagram" or "AI" in a Reel can reduce reach | [F2.29] (C-13) |

## 7. Platform features the book documents (2025–2026)
| Feature | What it does | Source |
|---|---|---|
| Trial Reels | 24 h test with non-followers before release | [U.3] |
| "Your Algorithm" topic controls | Users see and remove the topics the app assigned them | [U.4] |
| Reset suggested content | Users refresh recommendations in 24–48 h | [U.10] |
| Early access (close friends) | 24 h pre-release to an inner circle | [U.12] |
| Instagram Plus (paid) | Anonymous Story views, rewatch counts, audience lists, extended Stories, Spotlight | [U.17] |
| Carousel reordering after posting | Long-press and drag; edit the cover without losing data | [U.18] |
| In-app scheduling for everyone | Plan the week in the app | [U.19] |
| Friends Map | Precisely geotagged posts show on the map | [U.27] |
| AI comment suggestions | Clear visual elements → better suggested comments | [U.30] |
| Interactive links inside Reels | Link to the next video or a playlist | [U.32] |
| Cross-posting via Accounts Center | FB + Threads engagement feeds the IG "signal cluster" | [U.39] |
| Edits app | Retention graph, teleprompter; no confirmed reach boost | [U.15], [U.29] |
| Account Status page | Shows restrictions; if it's green, the problem is content | [U.147] |

## 8. Numbers the book cites (book's figures; never quote to clients as fact)
- The decision to stay happens within 1.7 s; 60% retention in the first 3 s doubles spread; ~694,000 Reels are sent by DM per minute; users spend half their time on Reels [U.20], [U.2].
- Carousels 10.15% vs Reels 1.23% engagement [U.7], [U.20], contradicted by 6.9% vs 3.3% [U.case lessons] (C-5).
- Accounts under 10k get higher reach rates; Stories for small accounts +35% [U.31], [U.11].
