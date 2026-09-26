#!/usr/bin/env node
// Render a text-only Reel (kinetic typography) from a JSON spec to MP4.
//
// Usage:
//   NODE_PATH=$(npm root -g) FFMPEG=/path/to/ffmpeg \
//     node scripts/render/reel.js <reel-spec.json> <out.mp4>
//
// Pipeline: the spec's cards become one HTML page (brand theme + layout); a
// deterministic seek(t) sets every element's state for time t; Playwright
// screenshots each frame and pipes JPEGs into ffmpeg; scripts/render/sfx.py
// synthesises the sound layer; ffmpeg muxes both into 1080x1920 H.264/AAC.
//
// Spec (paths relative to the repo root):
// {
//   "duration": 21, "fps": 30, "theme": "brands/lock-in.theme.css",
//   "label": "LOCK IN",                          // small label above each card, optional
//   "cards": [ { "start": 0, "end": 2.5, "top": 620,
//                "elements": [ { "text": "YOU NEVER DOOM-SCROLL", "style": "head cream",
//                                "size": 150, "build": "words", "at": 0, "dur": 1.0 } ],
//                "punch": [ { "at": 1.5, "scale": 1.04 } ] } ],
//   "sfx": [ { "t": 0, "type": "buzz" } ], "bed": { "type": "drone", "gain": 0.07 }
// }
// build: words | lines | type | slam | fade (default fade). "\n" in text = line break.

const fs = require("fs");
const path = require("path");
const { spawn, execFileSync } = require("child_process");
const { chromium } = require("playwright");

const ROOT = path.resolve(__dirname, "..", "..");
const W = 1080, H = 1920;

function esc(s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function buildHtml(spec) {
  const theme = path.join(ROOT, spec.theme);
  const cards = spec.cards.map((c, ci) => {
    const els = c.elements.map((e, ei) => {
      const lines = String(e.text).split("\n");
      let inner;
      if (e.build === "words") {
        let k = 0;
        inner = lines.map((ln) => ln.split(" ").map((w) => `<span class="u" data-k="${k++}">${esc(w)}</span>`).join(" ")).join("<br>");
      } else if (e.build === "lines") {
        inner = lines.map((ln, k) => `<span class="u ln" data-k="${k}">${esc(ln)}</span>`).join("");
      } else if (e.build === "type") {
        inner = `<span class="typed" data-full="${esc(String(e.text).replace(/\n/g, " "))}"></span>`;
      } else {
        inner = lines.map(esc).join("<br>");
      }
      const size = e.size ? `font-size:${e.size}px;` : "";
      const mt = e.gap != null ? `margin-top:${e.gap}px;` : "";
      return `<div class="el ${e.style || ""}" id="c${ci}e${ei}" style="${size}${mt}">${inner}</div>`;
    }).join("");
    const label = spec.label ? `<div class="label clabel">${esc(spec.label)}</div>` : "";
    return `<div class="card" id="c${ci}" style="top:${c.top || 620}px">${label}${els}</div>`;
  }).join("");
  const foot = spec.label ? `<div class="foot" style="left:90px;top:1740px;font-size:24px">${esc(spec.label)}</div>` : "";
  return `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="file://${theme}">
<style>
  body{margin:0;background:var(--bg)}
  #stage{width:${W}px;height:${H}px}
  .card{position:absolute;left:90px;right:90px;display:none;transform-origin:0% 30%}
  .clabel{font-size:24px;margin-bottom:28px}
  .el{white-space:normal}
  .el.serif{font-size:54px}
  .u{display:inline-block;opacity:0}
  .ln{display:block}
  .typed{white-space:pre-wrap}
</style></head><body><div id="stage" class="frame">${cards}${foot}</div>
<script>
const SPEC = ${JSON.stringify(spec)};
const clamp = (x) => Math.max(0, Math.min(1, x));
const ease = (x) => 1 - Math.pow(1 - clamp(x), 3);
function seek(t) {
  SPEC.cards.forEach((c, ci) => {
    const card = document.getElementById("c" + ci);
    const on = t >= c.start && t < c.end;
    card.style.display = on ? "block" : "none";
    if (!on) return;
    const lt = t - c.start, len = c.end - c.start;
    let scale = 1 + 0.02 * (lt / len);                        // slow push, like the house clips
    (c.punch || []).forEach((p) => { if (t >= p.at) scale *= 1 + (p.scale - 1) * ease((t - p.at) / 0.15); });
    card.style.transform = "scale(" + scale.toFixed(4) + ")";
    // hard cuts between cards (house style); no card-level fade, so frame 1 is never blank
    c.elements.forEach((e, ei) => {
      const el = document.getElementById("c" + ci + "e" + ei);
      const at = e.at != null ? e.at : c.start, dur = e.dur || 0.6;
      const b = e.build || "fade";
      if (b === "words" || b === "lines") {
        const units = el.querySelectorAll(".u"), n = units.length;
        units.forEach((u, k) => {
          const p = ease((t - (at + (k * dur) / Math.max(1, n))) / 0.12);
          u.style.opacity = p; u.style.transform = "translateY(" + ((1 - p) * 18).toFixed(1) + "px)";
        });
      } else if (b === "type") {
        const s = el.querySelector(".typed"), full = s.dataset.full.replace(/\\u2028/g, "\\n");
        s.textContent = full.slice(0, Math.round(full.length * clamp((t - at) / dur)));
      } else if (b === "slam") {
        const p = ease((t - at) / 0.12);
        el.style.opacity = p; el.style.transform = "scale(" + (1.15 - 0.15 * p).toFixed(3) + ")"; el.style.transformOrigin = "0% 50%";
      } else {
        el.style.opacity = ease((t - at) / 0.3);
      }
    });
  });
}
</script></body></html>`;
}

async function main() {
  const [specPath, outPath] = process.argv.slice(2);
  if (!specPath || !outPath) { console.error("usage: reel.js <spec.json> <out.mp4>"); process.exit(2); }
  const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));
  const fps = spec.fps || 30, frames = Math.round(spec.duration * fps);
  const ff = process.env.FFMPEG || "ffmpeg";
  const tmp = fs.mkdtempSync(path.join(require("os").tmpdir(), "reel-"));
  const htmlPath = path.join(tmp, "reel.html");
  fs.writeFileSync(htmlPath, buildHtml(spec));

  const wav = path.join(tmp, "sound.wav");
  execFileSync("python3", [path.join(__dirname, "sfx.py"), specPath, wav], { stdio: "inherit" });

  const silent = path.join(tmp, "video.mp4");
  const enc = spawn(ff, ["-loglevel", "error", "-y", "-f", "image2pipe", "-vcodec", "mjpeg", "-r", String(fps), "-i", "-",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "18", "-r", String(fps), silent],
    { stdio: ["pipe", "inherit", "inherit"] });

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  await page.goto("file://" + htmlPath, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  for (let f = 0; f < frames; f++) {
    await page.evaluate((t) => seek(t), f / fps);
    const buf = await page.screenshot({ type: "jpeg", quality: 93, clip: { x: 0, y: 0, width: W, height: H } });
    if (!enc.stdin.write(buf)) await new Promise((r) => enc.stdin.once("drain", r));
    if (f % (fps * 5) === 0) process.stderr.write(`frame ${f}/${frames}\n`);
  }
  await browser.close();
  enc.stdin.end();
  await new Promise((r, j) => enc.on("close", (c) => (c === 0 ? r() : j(new Error("ffmpeg exit " + c)))));

  execFileSync(ff, ["-loglevel", "error", "-y", "-i", silent, "-i", wav, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
    "-shortest", "-movflags", "+faststart", outPath], { stdio: "inherit" });
  console.log(outPath);
}

main().catch((e) => { console.error(e); process.exit(1); });
