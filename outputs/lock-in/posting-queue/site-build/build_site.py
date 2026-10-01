"""Build the standalone posting-queue site (no Claude sign-in, real downloads) from the artifact source in this folder."""
import json, os, re, shutil, zipfile

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SRC, "..", "site")
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
for d in ("clips", "carousels", "setup", "stories"):
    shutil.copytree(os.path.join(SRC, d), os.path.join(OUT, d))

html = open(os.path.join(SRC, "index.html")).read()
m = re.search(r"const CLIPS = (\[.*?\]);\n", html, re.S)
clips = json.loads(m.group(1))

# zips for every carousel / setup kit
for c in clips:
    if c.get("zip"):
        with zipfile.ZipFile(os.path.join(OUT, c["zip"]), "w", zipfile.ZIP_STORED) as z:
            for s in c["slides"]:
                z.write(os.path.join(OUT, s), os.path.basename(s))

NEW_JS = r'''const IS_PHONE = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent) || (navigator.maxTouchPoints > 1 && /Mac/.test(navigator.platform));
function triggerDownload(blob, name) {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob); a.download = name;
  document.body.appendChild(a); a.click();
  setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 1500);
}
async function saveFile(path, st, btn) {
  const name = path.split("/").pop();
  if (btn) btn.disabled = true; st.textContent = "Preparing…";
  try {
    const blob = await (await fetch(path)).blob();
    const type = blob.type || (name.endsWith(".mp4") ? "video/mp4" : name.endsWith(".zip") ? "application/zip" : "image/png");
    const file = new File([blob], name, { type });
    if (IS_PHONE && navigator.canShare && navigator.canShare({ files: [file] })) {
      try { await navigator.share({ files: [file] }); st.textContent = "Choose Save Video / Save Image"; }
      catch (e) { if (e && e.name === "AbortError") st.textContent = "Cancelled"; else { triggerDownload(blob, name); st.textContent = "Saved to Downloads"; } }
    } else { triggerDownload(blob, name); st.textContent = "Saved to Downloads"; }
  } catch (e) {
    st.innerHTML = 'Couldn\'t save. <a href="' + path + '" download style="color:var(--amber)">Open the file</a>, then long-press and Save.';
  }
  if (btn) btn.disabled = false;
}
'''
# 1) replace the old downloads code (from "let downloads = null;" to just before "function card(")
a = html.index("let downloads = null;")
b = html.index("function card(c)")
html = html[:a] + NEW_JS + html[b:]
# 2) button handlers
html = html.replace('btn.addEventListener("click", () => (c.type === "carousel" ? saveZip(c, st, btn) : saveFile(c.file, st, btn)));',
                    'btn.addEventListener("click", () => saveFile(c.type === "carousel" ? c.zip : c.file, st, btn));')
# 3) drop the claude init block and the note
html = re.sub(r"\(async \(\) => \{\n  downloads = window\.claude.*?\}\)\(\);\n", "", html, flags=re.S)
html = re.sub(r'  <div class="note" id="dlNote" hidden>.*?</div>\n', "", html)
html = html.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>\n', "")
assert "downloads" not in html.replace("Downloads", ""), "leftover claude downloads code"
assert "window.claude" not in html and "saveZip" not in html
# 4) proper HTML skeleton
title = '<title>LOCK IN Posting Queue</title>\n'
html = html.replace(title, "")
html = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex,nofollow">' + title) + html.split("\n", 0)[0] if False else (
    '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1">'
    '<meta name="robots" content="noindex,nofollow">' + title)  + html
# split head content (link + style) from body: everything up to </style> is head, rest is body
i = html.index("</style>") + len("</style>")
html = html[:i] + "\n</head><body>\n" + html[i:] + "\n</body></html>\n"
# the intro should say it opens for anyone
html = html.replace("<b>Save</b> puts the video on your phone.", "<b>Save</b> puts the video on your phone or computer.")
open(os.path.join(OUT, "index.html"), "w").write(html)
open(os.path.join(OUT, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
open(os.path.join(OUT, "_headers"), "w").write("/*\n  X-Robots-Tag: noindex, nofollow\n")
print("site built;", sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(OUT) for f in fs) // 1024 // 1024, "MB;",
      len([1 for dp, _, fs in os.walk(OUT) for f in fs if f.endswith(".zip")]), "zips")
