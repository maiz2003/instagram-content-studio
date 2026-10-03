---
name: postiz-scheduler
description: Load LOCK IN posts into Postiz as drafts and schedule only the ones the owner approved, by number. Use when the owner says "approve", asks to auto-post or schedule through Postiz, or at the "Load" step of the weekly routine (studio/TEAM.md).
---

# Postiz scheduler (LOCK IN)

The owner asked on 2026-10-03 for posts to go out automatically through Postiz. The approval rule in `studio/PROJECT-INSTRUCTIONS.md` still holds: **nothing is scheduled until the owner says "approve"** (all, or by number).

## Before anything
1. Check that the Postiz tools are in this session (search tools for "postiz"). If they aren't, say so in one line: the owner reconnects Postiz at claude.ai → Settings → Connectors, then starts a new session. Stop.
2. List the connected channels in Postiz. Instagram must be there, and TikTok or X only if those posts are in the queue. If a channel is missing, say which one and stop for that channel.
3. Read each channel's settings in Postiz before the first post on it (TEAM.md, "Load"): post type (post/Reel/Story), whether a cover or first comment can be set, and the time zone.

## The queue
- `outputs/lock-in/postiz/queue.json`, built by `build_queue.py` from the posting queue. Every post has its day, its 18:05 UK time, its caption, public media URLs, `ai_label`, `trial` and that day's Stories.
- `start_date` is the date Day 1 (Four Doors) goes live. Ask the owner if it's empty. Post date = `start_date` + (day − 1). From week 4 the schedule is 5 posts a week at 19:00 UK (`studio/DECISIONS.md`).

## Load and schedule
1. **Drafts:** create each post as a **draft** in Postiz. Use the caption exactly, attach the media URLs in order (carousel slides 1→N), and set the date and time. Don't schedule yet. Save the Postiz id and `status: "draft"` in queue.json.
2. **Approval:** show the owner a numbered table (number, day, date and time, title, format, AI label, Trial). Wait for "approve all" or "approve 1, 2, 5". Set `approved: true` only on those.
3. **Schedule:** schedule only the approved numbers, then report each one's channel, time and status as Postiz returns it. Update queue.json and commit.

## What the Postiz Instagram channel supports (checked 2026-10-03)
- Channel: **"Lock in"**, platform `instagram-standalone`, integration id `cmus88r3800ualh0y6dotclsl`. TikTok and X aren't connected yet.
- Settings: `post_type` (`post` or `story`), `is_trial_reel` with `graduation_strategy` (`MANUAL` or `SS_PERFORMANCE`), collaborators, audio. Caption max 2,200 characters, and at least one attachment.
- **Trial Reels can be automated**: `is_trial_reel: true` with `graduation_strategy: "MANUAL"`. The owner decides after 24 h whether to share it to followers, as the guide says.
- **No AI-label setting and no cover setting.**
- Posts can't be deleted through the tools. A wrong post is removed by hand in the Postiz app.

## What Postiz can't do
- **AI label** (11 posts: #09, #11, #14–#22). If Postiz has no AI-label option for Instagram, don't schedule those posts. Leave them as drafts, mark them `manual`, and tell the owner they're posted by hand from the posting page with the label on.
- **Trial Reels** (#10, #13, #17, #20) are supported (see above). #17 and #20 also need the AI label, so they stay manual.
- **Reel cover:** if a cover can't be picked, Instagram uses the first frame, which is already the hook card. That's fine.
- **Story stickers** (polls, quiz, link) can't be added through an API. Stories stay manual, and the daily Stories text is in each queue entry.

## Never
- Schedule anything the owner hasn't approved by number.
- Edit or delete a post after it's live (it resets how Instagram tests it).
- Post more than one Reel a day.
- Change captions while loading. If a caption needs changing, ask the owner first.
