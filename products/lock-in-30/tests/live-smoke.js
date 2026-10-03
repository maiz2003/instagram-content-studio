// Smoke test against the live site: node live-smoke.js  (uses the current unlock code)
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await (await b.newContext({ viewport: { width: 400, height: 860 }, ignoreHTTPSErrors: true })).newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('https://lockin-30.netlify.app/'); await p.waitForTimeout(800);
  await p.fill('#code', 'lock kfu9'); await p.click('button.primary'); await p.waitForTimeout(300);
  console.log('unlocked:', await p.evaluate(() => S.unlocked), 'fonts:', await p.evaluate(() => document.fonts.check('40px Anton')));
  await p.click('[data-door="Tired"]'); await p.click('#go'); await p.waitForTimeout(300);
  await p.screenshot({ path: './shots-live-today.png' });
  console.log('sw:', await p.evaluate(async () => !!(await navigator.serviceWorker.getRegistration())));
  console.log('errors', JSON.stringify(errs)); await b.close();
})();
