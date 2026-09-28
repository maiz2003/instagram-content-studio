---
name: daily-footage
description: The LOCK IN daily footage mission. Each day it generates 2-3 new faceless POV clips with Higgsfield (same hands, hoodie, desk and phone as the week-2 door Reels), reviews them frame by frame, grades them, files them in the footage library and reports to the owner. Use it when the daily routine fires or when the owner asks for more library clips.
---

# Daily footage mission (LOCK IN)

The owner set this up on 2026-09-28: "generate 2-3 clips every day with the most usage possible". The same day they added: "every day use all credit on Higgsfield". That is a **standing credit OK for this mission only**: spend the whole balance each day on this backlog. It is not an OK for any other Higgsfield spending. The mission never posts anything.

## Budget (check first, every run)
- Call `mcp__Higgsfield__balance`. **Spend all of it today, in this order:**
  1. **Clips first: 3 clips, or 2 if the balance is short.**
     - Each costs **7.5 credits** (Kling 3.0 pro, 5 s) when the backlog row already has an approved start frame, which is the `Still` column in `backlog.md`.
     - Without one, it costs **11.5**: 2 Nano Banana Pro 2K stills at 2 each, plus the video.
  2. **Then photos with everything left, at 2 credits each** (Nano Banana Pro 2K), until less than 2 remains:
     - start frames for backlog rows that don't have one
     - carousel covers (4:5) and Story backgrounds (9:16) with space for text
     - brand-message notebook shots (see `photos.md`)
- If the balance is under 7.5, make photos only. Under 2, generate nothing: tell the owner the balance is empty and that it resumes when credits are added or the plan refills.
- Credits don't refill daily; the Pro plan refills monthly. On most days after a big spend, the balance will be near 0, and the run is just a short "nothing to spend" note.
- A failed or rejected generation is not retried beyond the balance. Note it in the backlog.

## Pick the shots
1. Open `assets/footage/lock-in/library/backlog.md`.
2. Take the next 2-3 rows with status `todo`, top to bottom.
   - "Most usage" means shots that serve many posts: they fit the four doors, the fixes and the CTA, and are generic enough to reuse.
   - Prefer rows marked **★** first.
3. Mark them `in progress` with today's date.

## Make each clip (the method that worked in week 2)
All generations go in the Higgsfield project "LOCK IN week 2 footage":
- folder_id `d2664efa-0c76-4008-b2fe-65e8769be8aa`
- workspace `a918e19b-2a8e-459f-aebe-99397adf7ba7`

1. **Stills.** Use `generate_image_batch` to make 2 variants per shot:
   - model `nano_banana_pro`, resolution `2k`, aspect `9:16`, `use_unlim: false`
   - `image_references`: the **master** `367aa497-44a1-4862-90d9-a579da621607` first. Add a composition reference second only if the row names one.
   - Prompt: `Scene: <row's scene>.` + the identity block below.
     - If there's a second reference, add: "Use the SECOND reference image only for the camera angle and composition."
     - End with: "First-person POV, no faces, no logos, no brand marks, no watermark, anatomically correct hands."
2. **Pick a still** (skip steps 1–2 if the row already has an approved start frame). Download both with `show_generation_by_ids` and curl, and look at them. Reject any still with:
   - odd or extra hands, claw-like fingers
   - logos, including Apple logos
   - duplicated objects (two timers, a doubled laptop lid)
   - a torso or face instead of POV
   - scene items in the wrong place, like desk items in bed
   If both fail, the shot goes back to `todo` with a note. Don't regenerate.
3. **Motion.** Use `generate_video_batch`:
   - model `kling3_0`, mode `pro`, `sound: "off"`, duration 5, aspect `9:16`, same folder_id
   - `medias: [{role: "start_image", value: <still job id>}]`
   - Prompt: the row's **one** action + the motion block below.
   - If a preset recommendation blocks the call, retry with `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`.
   - Use `jobs_wait`, then `show_generation_by_ids`, then download.
4. **Review.** Make a 1-fps contact sheet plus 8 frames around any motion, and **look at every frame**. Check for:
   - hands morphing or gaining or losing fingers
   - the phone changing model or case
   - people or heads appearing
   - duplicated objects
   - on-screen text or clock digits changing
   Trim to the clean span (at least 2.0 s). If less than 2.0 s is clean, reject the clip and note why in the backlog.
5. **Grade** (the same look as week 2):
   ```
   $FF -y -ss <in> -to <out> -i raw.mp4 -an -vf "fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,eq=contrast=1.04:saturation=0.9:gamma=0.98,colorbalance=rs=0.02:bs=-0.02:rm=0.01:bm=-0.01,noise=alls=5:allf=t" -c:v libx264 -crf 19 -pix_fmt yuv420p -movflags +faststart out.mov
   ```
   To find ffmpeg: `$FFMPEG`, then `which ffmpeg`. Otherwise run `pip install --target <scratchpad>/pylib imageio-ffmpeg` and use the binary under `imageio_ffmpeg/binaries/`.
6. **File it** as `assets/footage/lock-in/library/<YYYY-MM-DD>_<slug>.mov`, plus a small `…_thumb.jpg` taken 1 s in.
7. **Clip card.** Run `skills/daily-footage/clip-card-prompt.md` on the graded clip. Use its contact sheet, its frames and the job ids. Save the card as `…/<YYYY-MM-DD>_<slug>.md`. If the card's verdict is **reject**, delete the file and set the backlog row to `rejected (reason)`.

### Identity block (paste into every still prompt)
> Use the FIRST reference image as the identity and set reference: the exact same person's hands (same light olive skin tone, same short natural nails, same hand shape), the exact same charcoal-black hoodie sleeves, the exact same dark near-black wooden desk with the same worn edge, the exact same cream lamp, the exact same white spiral notebook with the same handwriting, and the same black smartphone in a plain matte black case with no visible logo. Keep the same warm evening colour grade and the same camera (iPhone main lens, same slight grain).

For daytime or other-room rows, keep the hands, hoodie, phone and notebook, and let the row's scene set the room and light.

### Motion block (append to every video prompt)
> Handheld first-person phone footage with very subtle natural camera sway, real-time speed, natural physics, hands keep correct anatomy with five fingers throughout, the phone keeps the same plain matte black case and never changes model, no morphing, no new objects or people appearing, light stays constant.

## Record and report
- **Photos:** save approved photos as `assets/footage/lock-in/library/photos/<YYYY-MM-DD>_<slug>.jpg` (JPEG at Instagram size: 1080×1920 for 9:16, 1080×1350 for 4:5). Log them in `photos.md` with: file, what it shows, best use (cover, Story background, start frame for row N) and job id. Rejected ones get one line with the reason.
- **`library/catalog.md`**: paste the card's section 11 row for each clip:
  - file, date, length, what it shows
  - **best uses**: which door, fix or CTA, and suggested post types
  - Higgsfield job ids (still and video)
  - credits spent
- **`backlog.md`**: mark the rows `done` or `rejected (reason)`.
- **Commit** with a message like "Footage library: <date>, N clips". Push to the working branch. Use the attribution lines from the session.
- **Tell the owner** in one short message:
  - the clips, sent with `SendUserFile` (display `render`)
  - one line per clip: what it shows, its reuse score and its best use, taken from the card
  - credits spent today and left
  - the reminder that these clips need Instagram's **AI label** when posted
- **Backlog.** If it has fewer than 6 `todo` rows, add new ones that fit the next week's plan (`outputs/lock-in/*/week-plan.md`). Base them on the book's ideas: the four doors, phone in another room, the three ugly minutes, never miss twice, Sunday planning.

## Never
- Publish or schedule posts.
- Spend on anything besides this backlog, the photo list and their start frames.
- Show a face, a real person, a real result or a testimonial (E-5).
- Show readable app UI, notifications or brand logos.
- Write to Whop, Drive or Instagram.
