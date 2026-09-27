# LOCK IN posting queue (weeks 1–2)

This folder holds the source of the posting-queue page: https://claude.ai/artifact/M5LcUCfMyBPWQwYfG9Ynig

The page has a player and save buttons for every post, plus its caption. It is published as a claude.ai artifact with the `downloads` capability.

| File | What it is |
|---|---|
| `index.html` | The page. Carousels are zipped in the browser with JSZip, because the artifact host doesn't serve `.zip` files. |
| `clips.json` | The posts in posting order, with captions and file paths. |
| `files_map.json` | The published-path → local-file map used when publishing. |
| `order.txt` | The posting order and captions as plain text. The same text is in the Drive posting-order doc. |

The media aren't in this folder. They're the renders in `outputs/lock-in/…`, renamed `NN_dayDD_slug`, and the owner's copies are in the Drive folder `LOCK IN posting queue (weeks 1-2)` (`workflow.posting_queue_folder_id`).

To republish, rebuild `clips/` and `carousels/` from the renders using the names in `files_map.json`. Then publish `index.html` with that map to the same artifact URL.
