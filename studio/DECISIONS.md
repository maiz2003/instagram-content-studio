# Owner decisions on BRAND.md / TEAM.md (2026-10-03)

The owner added `BRAND.md`, `TEAM.md` and `PROJECT-INSTRUCTIONS.md` (copied here unchanged). Where they clash with what was already built, these are the owner's answers. They override the matching lines in BRAND.md for LOCK IN.

| Topic | BRAND.md says | Decision |
|---|---|---|
| Call to action | "link in bio" | **Keep "Comment LOCK"** on Instagram (comment → DM with the quiz → Whop). The Whop link also goes in the bio. X and other link-friendly channels use the direct link. |
| Schedule | 5 posts a week, 7pm local | **Weeks 1–3 stay daily at 18:05 UK** (already made). **From week 4: 5 posts a week at 19:00 UK.** |
| Channels | blank | **Instagram, TikTok, X**, plus one more the owner hasn't named yet (ask). |
| AI imagery | "Graphics are code-drawn. No AI photos." | **Keep using the AI footage until the library is used up** (AI label on). Then switch to **real filmed footage of the same shots** (`outputs/lock-in/real-footage-shot-list.md`) **or code-drawn graphics** (style: `outputs/lock-in/2026-10-week3/reels-codedrawn/`, comparison https://claude.ai/artifact/MbV4H8aC2W35KwJK3h2e6s). Track what's left with `python3 scripts/footage_usage.py`. No new AI imagery is generated (Higgsfield cancelled). |

Other BRAND.md values to fill in or confirm with the owner:
- Whop link: `https://whop.com/checkout/plan_NZkzvqwMgKl2f` (already in `brands/lock-in.yaml`).
- Audience: BRAND.md guesses 15–24; `brands/lock-in.yaml` says about 16–26.
- Fonts and colours: BRAND.md names Newsreader for body text and slightly different hex values (#0E0F12 / #EDE7DC / #E0A254 / #7A8089 / #24272D). Everything rendered so far uses `brands/lock-in.theme.css` (Spectral, #111216 / #E6E1D5 / #DA9D55). Switch the theme when the owner confirms.
- **Auto-posting (2026-10-03): the owner wants posts to go out through Postiz.** The connector is installed but needs reconnecting (claude.ai → Settings → Connectors, then a new session). Queue: `outputs/lock-in/postiz/queue.json`. Skill: `skills/postiz-scheduler/`. Approval by number still comes first.

## 2026-10-03: launch status
- Instagram Day 1 = 1 Oct 2026; TikTok Day 1 = 3 Oct 2026 (#01 Four Doors), same post order, one a day at 18:05 UK.
- Scheduled in Postiz: Instagram #03–#08, #10, #12, #13. TikTok: #01–#22 except #18 (3–24 Oct; #01 Four Doors added for today because TikTok Day 1 hadn't actually gone up).
- Manual: Instagram #09, #11, #14–#22 (AI label). TikTok #18 on 20 Oct (AI photos). Stories every day.
- **LOCK auto-reply: not set up.** The owner replies to LOCK comments by hand until they hit a limit, then pays for an automation tool (kit: Drive Doc "02 · LOCK auto-reply setup"). TikTok LOCK comments are always answered by hand.
