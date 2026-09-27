# Handoff: state of the work (2026-09-27)

This file brings a new session up to date: links, IDs, open items and standing rules. It was written when the work moved from the cloud session to a local one. Everything built so far is in this repo on branch `claude/modest-newton-mssmmm` ([PR #1](https://github.com/maiz2003/instagram-content-studio/pull/1)).

## Standing rules from the owner
- **LOCK IN** is the active brand. **Beroia Home is on hold** until the owner brings it up.
- **No auto-publish.** The owner posts by hand.
- **No Higgsfield credits** without an explicit OK for that specific generation.
- Whop, Drive and Instagram are **read-only for the agents**. Only write there when the owner asks for that specific change.
- Never start account connections on the owner's behalf.
- Target market: Europe + US. Post at **18:05 UK / 19:05 CET / 13:05 ET**. The account is faceless.

## Live things and where they are
| What | Where |
|---|---|
| Book (Whop) | Product `prod_7BAVlob3INIFe` in company `biz_mZWif3gl8Pw3u3` (LOCKING 101). $15, checkout `https://whop.com/checkout/plan_NZkzvqwMgKl2f` |
| Quiz (the funnel: comment LOCK → DM → quiz → Whop) | https://lockin-quiz.netlify.app |
| **LOCK IN 30 game** | **https://lockin-30.netlify.app** · unlock code **`LOCK-KFU9`** · source `products/lock-in-30/` · Netlify site id `f33d47c7-13e3-47f5-a40d-09f80a96b16e` (owner's team; visitor protection switched off) |
| Pinned welcome post in the Lock In Chat | Whop experience `exp_MGFpyqH6ra9w4W`, message `post_1CfTyjkwnvaDkBoGs3gKQ1` (game link + code) |
| 30-day tracker | https://claude.ai/artifact/ELpGTnN5BdEksgu9QQSoLY (source `outputs/lock-in/tracker/`; db collections `posts`, `weeks`, `meta/plan`) |
| Posting queue page | https://claude.ai/artifact/M5LcUCfMyBPWQwYfG9Ynig (source `outputs/lock-in/posting-queue/`) |
| Game preview (old code `LOCKIN30`, testing only) | https://claude.ai/artifact/HSWk7fB2QQQmsbudy4wptv |
| Drive: footage uploads | folder `1fisrKvLQlmEJiZnBW5lGU6rG3uUxg7vH` (week-2 clips are expected in a subfolder `clips-week2`) |
| Drive: posting queue | folder `1aymnlDOmVajd6opoJArAWJ14VzP_SFnr` (all 15 week 1–2 posts, uploaded by the owner and verified) |

These IDs also live in `brands/lock-in.yaml` → `workflow:`.

## Where the content stands
- **Week 1** (days 1–7): done and in the posting queue.
- **Week 2** (days 8–14): the plan and captions are in `outputs/lock-in/2026-10-week2/week-plan.md`.
  - Trial Reels, carousels and the text-version door Reels are rendered.
  - The **footage versions of the 4 door Reels** are waiting for the owner's clips. The shot list is in `outputs/lock-in/2026-10-week2-shot-list.md`.
  - The specs are in `outputs/lock-in/2026-10-week2/reels/*.json`. They expect footage at `assets/footage/lock-in/week2/01_bored.mov` … `05_lockin_night.mov`.
- **Weekly workflow**: the `weekly-cycle` skill plus the agent team in `agents/`, with an owner-approval checkpoint. The review day is Sunday.

## Open items
1. **Week-2 clips.** When they land in Drive, run the footage-reviewer steps, file the clips in `assets/footage/lock-in/week2/`, render the 4 door Reels, run QA, and update the posting-queue page.
2. **Quiz fix texts for Bored, Anxious and Tired.** They're needed for `CONFIG.fixes` in `products/lock-in-30/index.html` and for the door Reels. Only Stuck's fix is known.
3. **Optional daily missions.** The book's 30-day challenge, one line per day, would go into `CONFIG.missions`.
4. **Whop product welcome message.** The owner pastes the game link and code in the Whop dashboard. The API can't edit that text.
5. **Week-1 numbers.** Enter them in the tracker, then run the Sunday review (week 3 planning).
6. **PR #1** is still a draft. Nothing blocks it: there's no CI and no reviews.

## Game: how to change and redeploy
- **Settings:** the `CONFIG` block at the top of `products/lock-in-30/index.html` holds the code, fixes, missions and book URL. See `products/lock-in-30/README.md`.
- **Redeploy:** `netlify deploy --dir products/lock-in-30 --prod --site f33d47c7-13e3-47f5-a40d-09f80a96b16e`. You need `netlify login` first.
  - Deploying the folder publishes `README.md` and `tests/` too. That's harmless, or copy just `index.html manifest.webmanifest sw.js _headers fonts sounds icons` to a temp folder and deploy that.
  - If you changed anything besides `index.html`, bump `VERSION` in `sw.js`.
- **Tests:** `products/lock-in-30/tests/walkthrough.js` runs locally and `live-smoke.js` runs against the live site.
- **Unlock code:** if you change it, everyone already unlocked stays unlocked. Update this file, the pinned chat post and the Whop welcome message.

## Local setup (tools the renderers need)
- **Node 18+** with Playwright:
  - `npm i -g playwright`
  - `npx playwright install chromium`
  - `export NODE_PATH=$(npm root -g)` so the scripts find it.
- **ffmpeg** on PATH, or `export FFMPEG=/path/to/ffmpeg` (the renderers read `FFMPEG`).
- **Python 3** (standard library only for `sound.py` and `beat.py`).
- **Netlify CLI** (`npm i -g netlify-cli`), for the game.
- Full render instructions: `agents/video-producer.md` and `scripts/render/reel.js`.

## Scheduled check-in
A routine named "PR #1 + Drive check-in" (`trig_018MjPdCRRBSr1oLsoe2Ud7M`) wakes the **cloud** session about hourly. It checks PR #1 and looks in Drive for `clips-week2`. It doesn't follow the work to a local session. Delete it once the local session is the main one, or leave it running as a watcher.
