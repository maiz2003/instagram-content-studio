const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, 'site');
const types = { '.html': 'text/html', '.mp4': 'video/mp4', '.png': 'image/png', '.zip': 'application/zip' };
const srv = http.createServer((q, r) => {
  const f = path.join(ROOT, decodeURIComponent(q.url.split('?')[0]).replace(/\/$/, '/index.html'));
  if (!fs.existsSync(f) || fs.statSync(f).isDirectory()) { r.writeHead(404); return r.end(); }
  r.writeHead(200, { 'Content-Type': types[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(r);
}).listen(8899);
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 400, height: 900 }, acceptDownloads: true });
  const p = await ctx.newPage(); const errs = [];
  p.on('pageerror', e => errs.push(e.message)); p.on('requestfailed', r => { if (!/fonts\.g/.test(r.url())) errs.push('REQ ' + r.url()); });
  await p.goto('http://127.0.0.1:8899/'); await p.waitForTimeout(1000);
  const counts = await p.evaluate(() => ['wsetup', 'wstories', 'w1', 'w2', 'w3'].map(id => id + ':' + document.getElementById(id).children.length).join(' '));
  const disabled = await p.evaluate(() => [...document.querySelectorAll('.save,.slide')].filter(b => b.disabled).length);
  console.log(counts, '| disabled buttons:', disabled);
  const results = [];
  for (const [sel, label] of [['#w3 article:nth-child(1) .save', 'week-3 Reel'], ['#w1 article:nth-child(4) .save', 'week-1 carousel zip'], ['#wstories article:nth-child(1) .save', 'story background'], ['#wsetup article:nth-child(1) .save', 'setup kit zip']]) {
    const [dl] = await Promise.all([p.waitForEvent('download', { timeout: 20000 }).catch(() => null), p.click(sel)]);
    if (!dl) { results.push(label + ': NO DOWNLOAD'); continue; }
    const f = await dl.path(); results.push(label + ': ' + dl.suggestedFilename() + ' ' + Math.round(fs.statSync(f).size / 1024) + ' KB');
  }
  console.log(results.join('\n'));
  // copy caption
  await ctx.grantPermissions(['clipboard-read', 'clipboard-write']);
  await p.click('#w3 article:nth-child(1) .copy'); await p.waitForTimeout(300);
  console.log('clipboard starts:', (await p.evaluate(() => navigator.clipboard.readText())).slice(0, 50));
  console.log('errors:', errs);
  await b.close(); srv.close();
})();
