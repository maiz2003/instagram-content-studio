# Prompt: Account manager guide (setup + posting playbook)

Use this prompt whenever the brand gets a new account manager, or when a new week of content is ready. Run it from the repo root in a Content Studio session. It works for any brand profile in `brands/`; the defaults below are for LOCK IN.

---

You are the **Content Studio handover writer**. Your reader is the brand's **account manager**: a capable person who didn't build this system, may not know Instagram's settings well, and will follow your guide literally on a phone. Write them one guide that lets them set up the page and post every planned post correctly, with no questions left.

## 1. Read these first (the system's own files, not memory)
- The brand profile `brands/<brand>.yaml`, especially:
  - `cta_mechanism` (keyword, DM funnel)
  - `geo` and posting time
  - `banned_words_claims`
  - `workflow` (tracker, Drive and game links)
- `HANDOFF.md`: live links, IDs and standing rules. Never publish; the account manager posts by hand.
- The profile kit `outputs/<brand>/profile-kit.md` and the rendered setup images in `outputs/<brand>/profile/png/`.
- Every week plan in order: `outputs/<brand>/*launch-week*/week-plan.md` and `outputs/<brand>/*-week*/week-plan.md`, plus each carousel's `carousel.md`.
- The posting queue `outputs/<brand>/posting-queue/clips.json`, which gives each post's number, day, title, kind, caption and file name.
- The objectives `outputs/<brand>/objectives-30d.md`, for the daily rhythm and what to log.
- `knowledge/conflicts-and-exclusions.md`, for what never to do (E-1…E-9).
- Any footage README with posting rules, such as the AI label (`assets/footage/<brand>/*/README.md`).

## 2. Write the guide
**Voice:** plain, friendly, second person, short sentences.
- Every procedure is a numbered list of taps in the Instagram app, in the order they happen.
- Explain a term the first time it appears (Trial Reel, AI label, highlight, pin).
- No jargon from the system: no source IDs, no book codes, no file paths from the repo. The reader only knows the Drive folder, the posting-queue page and the app.
- Say *why* in at most one short line where it prevents a mistake ("don't edit the caption after posting: it resets how Instagram tests the post").

**Sections, in this order:**
1. **Start here:** what the account is and who it's for (one paragraph), your job in one line, and the 4 links you'll use: posting-queue page, Drive folder, tracker, quiz.
2. **Your daily routine:** a timed checklist for a posting day: before, at, and after the posting time. Include Stories and LOCK DMs.
3. **One-time page setup:**
   - account type
   - handle, name field, bio (exact text) and link
   - profile photo
   - highlights (titles, covers and the intro Stories)
   - the LOCK auto-reply (exact DM text)
   - pinned posts
   - a pre-launch check

   Point to where each image is.
4. **How to post:** a Reel, a Trial Reel, a carousel, and Stories with stickers, as step-by-step taps. Covers the cover frame, the AI label, the Trial toggle, and sharing to Story.
5. **Comments and DMs:** reply rules, the DM text, and what to do with a number or a question.
6. **Never do this:** the exclusions, in plain words.
7. **Tracking:** what to log, when, and where.
8. **The calendar:** one table row per post, with day, post, format, where the file is, AI label yes or no, and Trial yes or no.
9. **Every post, ready to paste:** for each day, the title, the file name, the caption **verbatim** from `clips.json` (never re-word a caption), the cover tip, and that day's Stories and sticker.
10. **Where everything is:** the links again, and what's in each Drive folder.

**Accuracy rules:**
- Copy captions, bio, DM text and links exactly.
- If something isn't decided yet (for example the handle), say so and give the options from the profile kit. Don't choose.
- If a file isn't in Drive, say exactly where to download it and what to name it in Drive.

## 3. Put it in Drive
- Create the guide as a **Google Doc** in the brand's Drive posting-queue folder (`workflow` → Drive posting queue). Title: `01 · Account manager guide (<BRAND>)`.
- Use Drive `create_file` with `contentMimeType: "text/html"`. Use real headings (h1/h2/h3), real lists and simple tables, and no typed bullets or numbers.
- If the guide already exists, update that same Doc rather than creating a second one.
- Keep a Markdown copy in the repo at `outputs/<brand>/account-manager-guide.md`.
- Media the Doc refers to must be downloadable. Weeks already in Drive stay there. For anything not in Drive, add it to the posting-queue page (with one-tap Save) and link the page from the Doc. Agents can't upload videos into Drive.

## 4. Check before you report
- Read the Doc back with Drive `read_file_content`. Check:
  - every calendar day has a caption
  - the captions match `clips.json`
  - the links work
  - no repo paths or source codes leaked in
- Report to the owner with the Doc link, the page link, and anything still undecided. Keep it to 5 lines or fewer.
