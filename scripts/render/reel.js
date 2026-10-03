#!/usr/bin/env node
// Render a text-only Reel (kinetic typography) from a JSON spec to MP4.
//
// Usage:
//   NODE_PATH=$(npm root -g) FFMPEG=/path/to/ffmpeg \
//     node scripts/render/reel.js <reel-spec.json> <out.mp4>
//
// Pipeline: the spec's cards become one HTML page (brand theme + layout); a
// deterministic seek(t) sets every element's state for time t; Playwright
// screenshots each frame and pipes JPEGs into ffmpeg; scripts/render/sound.py
// composes the soundtrack (music + context SFX); ffmpeg mixes, normalises and
// muxes into <out>.mp4 (full mix) and <out>-sfx-only.mp4 (for a trending IG sound).
//
// Spec (paths relative to the repo root):
// {
//   "duration": 21, "fps": 30, "theme": "brands/lock-in.theme.css",
//   "label": "LOCK IN",                          // small label above each card, optional
//   "cards": [ { "start": 0, "end": 2.5, "top": 620,
//                "elements": [ { "text": "YOU NEVER DOOM-SCROLL", "style": "head cream",
//                                "size": 150, "build": "words", "at": 0, "dur": 1.0 } ],
//                "punch": [ { "at": 1.5, "scale": 1.04 } ] } ],
//   "music": { "bpm": 120, "mood": "dark", "sections": [[0, "intro"], [1.5, "drop"]] },
//   "sfx": [ { "t": 0, "type": "vibrate" } ]   // see scripts/render/sound.py for all types
// }
// build: words | lines | type | slam | fade (default fade). "\n" in text = line break.
// Code-drawn graphic (optional element): { "svg": "<svg ...>...</svg>", "build": "draw", "at": 1, "dur": 1.2 }
//   Shapes with pathLength="1" draw on in document order across "dur"; shapes with class "f" fade in after.
//
// Footage (optional, per card): put a filmed clip behind the card's text.
//   "bg": { "file": "path/to/clip.mov",   // repo-relative or absolute; landscape or portrait, cropped to fill 9:16
//           "in": 2.0,                    // start point in the clip (s), default 0
//           "rate": 0.9,                  // playback speed, <1 = slow motion, default 1
//           "dim": 0.45,                  // darken 0-1 so the type stays readable, default 0.45
//           "push": 0.03,                 // slow zoom-in across the card, default 0.03 (0 = none)
//           "audio": 0.6 }                // mix the clip's own sound in at this gain, default 0 (muted)
//   Cards without "bg" keep a flat background ("bg_color", default #111216). A clip shorter than its
//   card loops. When any card has footage, text frames are captured with transparency and composited
//   over the footage track; specs without footage render exactly as before.

const fs = require("fs");
const path = require("path");
const { spawn, execFileSync } = require("child_process");
const { chromium } = require("playwright");

const ROOT = path.resolve(__dirname, "..", "..");
const W = 1080, H = 1920;

function esc(s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function buildHtml(spec, footage) {
  const theme = path.join(ROOT, spec.theme);
  const cards = spec.cards.map((c, ci) => {
    const els = c.elements.map((e, ei) => {
      const lines = String(e.text).split("\n");
      let inner;
      if (e.svg) {
        inner = e.svg;
      } else if (e.build === "words") {
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
    return `<div class="card${c.bg ? " onfoot" : ""}" id="c${ci}" style="top:${c.top || 620}px">${label}${els}</div>`;
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
  ${footage ? `html,body,#stage.frame{background:transparent !important}
  .card.onfoot .el,.card.onfoot .clabel{text-shadow:0 2px 18px rgba(0,0,0,.6),0 0 2px rgba(0,0,0,.5)}` : ""}
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
      } else if (b === "draw") {
        const strokes = el.querySelectorAll("[pathLength],[pathlength]"), n = strokes.length;
        strokes.forEach((s, k) => {
          const p = ease((t - (at + (k * dur) / Math.max(1, n))) / Math.max(0.15, dur / Math.max(1, n)));
          s.style.strokeDasharray = "1"; s.style.strokeDashoffset = String(1 - p);
        });
        el.querySelectorAll(".f").forEach((f) => { f.style.opacity = ease((t - at - dur) / 0.3); });
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

// Footage track: one segment per card (its clip, or a flat colour), frame-exact, concatenated.
// Returns {video: bg.mp4, audio: clips.wav | null}.
function buildFootage(spec, fps, frames, ff, tmp) {
  const color = spec.bg_color || "#111216";
  const cards = [...spec.cards].sort((a, b) => a.start - b.start);
  const spans = [];                                    // [startFrame, endFrame, card|null]
  let cursor = 0;
  for (const c of cards) {
    const a = Math.max(cursor, Math.round(c.start * fps)), b = Math.min(frames, Math.round(c.end * fps));
    if (a > cursor) spans.push([cursor, a, null]);
    if (b > a) spans.push([a, b, c]);
    cursor = Math.max(cursor, b);
  }
  if (cursor < frames) spans.push([cursor, frames, null]);

  const vList = [], aList = [];
  let anyAudio = false;
  spans.forEach(([a, b, c], i) => {
    const n = b - a, len = n / fps;
    const v = path.join(tmp, `bg${i}.mp4`), w = path.join(tmp, `bg${i}.wav`);
    const bg = c && c.bg;
    const out = ["-an", "-frames:v", String(n), "-r", String(fps), "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p", v];
    if (bg) {
      const file = path.isAbsolute(bg.file) ? bg.file : path.join(ROOT, bg.file);
      if (!fs.existsSync(file)) throw new Error(`footage not found: ${bg.file}`);
      const rate = bg.rate || 1, dim = bg.dim == null ? 0.45 : bg.dim, push = bg.push == null ? 0.03 : bg.push;
      const k = (1 - dim).toFixed(3);
      // slow push-in: zoompan on a 2x upscale so the sub-pixel steps don't jitter
      const zoom = push ? `,scale=${2 * W}:${2 * H},zoompan=z='1+${push}*on/${n}':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=${W}x${H}:fps=${fps}` : "";
      const vf = `setpts=(PTS-STARTPTS)/${rate},fps=${fps},scale=${W}:${H}:force_original_aspect_ratio=increase,crop=${W}:${H}` +
        `${zoom},colorchannelmixer=rr=${k}:gg=${k}:bb=${k},setsar=1`;
      execFileSync(ff, ["-loglevel", "error", "-y", "-stream_loop", "-1", "-ss", String(bg.in || 0), "-i", file, "-vf", vf, ...out]);
      if (bg.audio) {
        anyAudio = true;
        execFileSync(ff, ["-loglevel", "error", "-y", "-stream_loop", "-1", "-ss", String(bg.in || 0), "-i", file,
          "-af", `atempo=${Math.min(2, Math.max(0.5, rate))},volume=${bg.audio},afade=t=in:d=0.02,afade=t=out:st=${Math.max(0, len - 0.04)}:d=0.04`,
          "-t", len.toFixed(4), "-ac", "1", "-ar", "44100", w]);
      }
    } else {
      execFileSync(ff, ["-loglevel", "error", "-y", "-f", "lavfi", "-i", `color=c=${color}:s=${W}x${H}:r=${fps}`, ...out]);
    }
    if (!fs.existsSync(w)) {
      execFileSync(ff, ["-loglevel", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", len.toFixed(4), w]);
    }
    vList.push(`file '${v}'`);
    aList.push(`file '${w}'`);
  });
  const vTxt = path.join(tmp, "bg.txt"), aTxt = path.join(tmp, "bga.txt");
  fs.writeFileSync(vTxt, vList.join("\n"));
  fs.writeFileSync(aTxt, aList.join("\n"));
  const video = path.join(tmp, "bg.mp4");
  execFileSync(ff, ["-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", vTxt, "-c", "copy", video]);
  let audio = null;
  if (anyAudio) {
    audio = path.join(tmp, "clips.wav");
    execFileSync(ff, ["-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", aTxt, "-ac", "1", "-ar", "44100", audio]);
  }
  return { video, audio };
}

async function main() {
  const [specPath, outPath] = process.argv.slice(2);
  if (!specPath || !outPath) { console.error("usage: reel.js <spec.json> <out.mp4>"); process.exit(2); }
  const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));
  const fps = spec.fps || 30, frames = Math.round(spec.duration * fps);
  const ff = process.env.FFMPEG || "ffmpeg";
  const tmp = fs.mkdtempSync(path.join(require("os").tmpdir(), "reel-"));
  const footage = spec.cards.some((c) => c.bg);
  const htmlPath = path.join(tmp, "reel.html");
  fs.writeFileSync(htmlPath, buildHtml(spec, footage));

  // soundtrack stems: music.wav (beat-synced score) + sfx.wav (context sound design)
  execFileSync("python3", [path.join(__dirname, "sound.py"), specPath, tmp], { stdio: "inherit" });
  const music = path.join(tmp, "music.wav");
  let sfx = path.join(tmp, "sfx.wav");

  let bgVideo = null;
  if (footage) {
    const bg = buildFootage(spec, fps, frames, ff, tmp);
    bgVideo = bg.video;
    if (bg.audio) {   // clips' own sound joins the SFX layer, so the music ducks under it too
      const mixed = path.join(tmp, "sfx-clips.wav");
      execFileSync(ff, ["-loglevel", "error", "-y", "-i", sfx, "-i", bg.audio, "-filter_complex",
        "[0:a][1:a]amix=inputs=2:normalize=0:duration=first", "-ac", "1", "-ar", "44100", mixed]);
      sfx = mixed;
    }
  }

  const silent = path.join(tmp, "video.mp4");
  const encArgs = footage
    ? ["-loglevel", "error", "-y", "-i", bgVideo, "-f", "image2pipe", "-vcodec", "png", "-framerate", String(fps), "-i", "-",
       "-filter_complex", "[0:v][1:v]overlay=0:0:format=auto:shortest=1,format=yuv420p[v]", "-map", "[v]",
       "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "18", "-r", String(fps), silent]
    : ["-loglevel", "error", "-y", "-f", "image2pipe", "-vcodec", "mjpeg", "-r", String(fps), "-i", "-",
       "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "18", "-r", String(fps), silent];
  const enc = spawn(ff, encArgs, { stdio: ["pipe", "inherit", "inherit"] });

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  await page.goto("file://" + htmlPath, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  for (let f = 0; f < frames; f++) {
    await page.evaluate((t) => seek(t), f / fps);
    const buf = footage
      ? await page.screenshot({ type: "png", omitBackground: true, clip: { x: 0, y: 0, width: W, height: H } })
      : await page.screenshot({ type: "jpeg", quality: 93, clip: { x: 0, y: 0, width: W, height: H } });
    if (!enc.stdin.write(buf)) await new Promise((r) => enc.stdin.once("drain", r));
    if (f % (fps * 5) === 0) process.stderr.write(`frame ${f}/${frames}\n`);
  }
  await browser.close();
  enc.stdin.end();
  await new Promise((r, j) => enc.on("close", (c) => (c === 0 ? r() : j(new Error("ffmpeg exit " + c)))));

  // Full mix: music with a little room, ducked under every SFX hit, loudness-normalised for Instagram.
  const full = "[0:a]aecho=0.8:0.6:45|90:0.18|0.10,highpass=f=30[m];[1:a]asplit=2[s1][s2];" +
    "[m][s1]sidechaincompress=threshold=0.04:ratio=5:attack=5:release=200[md];" +
    "[md][s2]amix=inputs=2:weights=0.8 1.0:normalize=0,loudnorm=I=-13:TP=-1.2:LRA=11,alimiter=limit=0.85:level=disabled[a]";
  const mixWav = path.join(tmp, "mix.wav"), sfxWav = path.join(tmp, "sfx-only.wav");
  // A supplied track (spec.music.file, e.g. from beat.py sync) replaces the generated score.
  const track = spec.music && spec.music.file;
  const musicIn = track
    ? ["-ss", String(spec.music.offset || 0), "-t", String(spec.duration), "-i", track]
    : ["-i", music];
  const fullMix = track
    ? full.replace("[0:a]aecho=0.8:0.6:45|90:0.18|0.10,highpass=f=30[m]",
        `[0:a]aformat=channel_layouts=mono,afade=t=in:d=0.05,afade=t=out:st=${Math.max(0, spec.duration - 0.6)}:d=0.6[m]`)
    : full;
  execFileSync(ff, ["-loglevel", "error", "-y", ...musicIn, "-i", sfx, "-filter_complex", fullMix, "-map", "[a]", "-ar", "44100", mixWav]);
  // SFX-only: for pairing with a trending Instagram sound added in the app.
  execFileSync(ff, ["-loglevel", "error", "-y", "-i", sfx, "-af", "loudnorm=I=-18:TP=-1.5,alimiter=limit=0.85:level=disabled", "-ar", "44100", sfxWav]);
  const mux = (wav, out) => execFileSync(ff, ["-loglevel", "error", "-y", "-i", silent, "-i", wav, "-c:v", "copy",
    "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], { stdio: "inherit" });
  mux(mixWav, outPath);
  const sfxOut = outPath.replace(/\.mp4$/, "-sfx-only.mp4");
  mux(sfxWav, sfxOut);
  console.log(outPath);
  console.log(sfxOut);
}

main().catch((e) => { console.error(e); process.exit(1); });
