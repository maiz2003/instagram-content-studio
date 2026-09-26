#!/usr/bin/env node
// Render every `.frame` element in an HTML file to its own PNG.
//
// Usage:
//   NODE_PATH=$(npm root -g) node scripts/render/render.js <page.html> <out-dir> [prefix]
//
// Each .frame sets its own pixel size via inline style (e.g. 1080x1350 carousel
// slide, 1080x1080 avatar). Output: <out-dir>/<prefix>-01.png, -02.png, ...
// or <out-dir>/<data-name>.png when the frame has a data-name attribute.
// Needs Playwright (global npm install) and its bundled Chromium.

const path = require("path");
const fs = require("fs");
const { chromium } = require("playwright");

async function main() {
  const [html, outDir, prefix = "frame"] = process.argv.slice(2);
  if (!html || !outDir) {
    console.error("usage: render.js <page.html> <out-dir> [prefix]");
    process.exit(2);
  }
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 1 });
  await page.goto("file://" + path.resolve(html), { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  const frames = await page.$$(".frame");
  let i = 0;
  for (const el of frames) {
    i += 1;
    const name = (await el.getAttribute("data-name")) || `${prefix}-${String(i).padStart(2, "0")}`;
    const out = path.join(outDir, `${name}.png`);
    await el.screenshot({ path: out });
    console.log(out);
  }
  const missing = await page.evaluate(() =>
    [...document.fonts].filter((f) => f.status === "error").map((f) => f.family));
  if (missing.length) console.error("WARNING fonts failed to load:", [...new Set(missing)].join(", "));
  await browser.close();
}

main().catch((e) => { console.error(e); process.exit(1); });
