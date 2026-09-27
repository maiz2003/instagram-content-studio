const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 400, height: 860 }, deviceScaleFactor: 1 });
  const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.stack)); p.on('console', m => m.type()==='error' && errs.push(m.text()));
  // Run from this folder: (cd .. && python3 -m http.server 8765) &  then  node walkthrough.js
const U = 'http://127.0.0.1:8765/index.html', out = './shots-';
  await p.goto(U); await p.waitForTimeout(400);
  await p.screenshot({ path: out+'01-unlock.png', fullPage: true });
  await p.fill('#code', 'wrong'); await p.click('button.primary'); 
  console.log('err shown', await p.isVisible('#err'));
  await p.fill('#code', (await p.evaluate(() => CONFIG.unlockCode)).toLowerCase().replace('-', ' ')); await p.click('button.primary'); await p.waitForTimeout(200);
  await p.click('[data-door="Stuck"]'); await p.fill('#name', 'Sam');
  await p.screenshot({ path: out+'02-onboard.png', fullPage: true });
  await p.click('#go'); await p.waitForTimeout(200);
  await p.screenshot({ path: out+'03-today.png', fullPage: true });
  await p.click('#start'); await p.check('#phone'); await p.fill('#note', 'chapter 4');
  await p.screenshot({ path: out+'04-pre.png', fullPage: true });
  await p.click('#go'); await p.waitForTimeout(700);
  // jump to minute 1:30
  await p.evaluate(() => { S.active.startedAt = Date.now() - 90e3; save(); });
  await p.waitForTimeout(700);
  await p.screenshot({ path: out+'05-session.png', fullPage: true });
  // reload mid-session: must survive
  await p.reload(); await p.waitForTimeout(600);
  console.log('after reload clock', await p.textContent('#clock'));
  // finish it
  await p.evaluate(() => { S.active.startedAt = Date.now() - 21*60e3; save(); });
  await p.reload(); await p.waitForTimeout(700);
  await p.screenshot({ path: out+'06-reward.png', fullPage: true });
  await p.click('#ok');
  // a slip
  await p.click('#start'); await p.click('#go'); await p.waitForTimeout(300);
  await p.click('#stop'); await p.screenshot({ path: out+'07-slip.png', fullPage: true });
  await p.click('[data-door="Stuck"]'); await p.waitForTimeout(300);
  await p.screenshot({ path: out+'08-slipdone.png', fullPage: true });
  await p.click('#ok');
  // seed history: 12 days back with a two-day miss
  await p.evaluate(() => {
    const t = today(); S.start = addDays(t, -12);
    const add = (off, n, phone) => { for (let i=0;i<n;i++) S.sessions.push({ d: addDays(t, off), t: 0, mins: 20, phoneOut: phone, done: true, door: null, note: '' }); };
    add(-12,3,true); add(-11,2,true); add(-10,1,false); add(-7,3,true); add(-6,1,true); add(-5,2,false); add(-3,3,true); add(-2,1,true);
    for (const d of ['Bored','Bored','Tired','Anxious']) S.sessions.push({ d: addDays(t,-4), t:0, mins:20, phoneOut:false, done:false, door:d, note:'' });
    save(); render();
  });
  await p.waitForTimeout(300);
  await p.screenshot({ path: out+'09-today-seeded.png', fullPage: true });
  await p.click('[data-tab="map"]'); await p.waitForTimeout(300); await p.screenshot({ path: out+'10-map.png', fullPage: true });
  await p.click('[data-tab="doors"]'); await p.waitForTimeout(300); await p.screenshot({ path: out+'11-doors.png', fullPage: true });
  await p.click('[data-tab="me"]'); await p.waitForTimeout(300); await p.screenshot({ path: out+'12-me.png', fullPage: true });
  const D = await p.evaluate(() => { const D = derive(); return { chain: D.chain, best: D.best, xp: D.xp, level: D.level, doneDays: D.doneDays, comebacks: D.comebacks, badges: D.badges }; });
  console.log(JSON.stringify(D));
  // backup code round trip into a fresh context
  const code = await p.evaluate(() => "LOCKIN1:" + btoa(unescape(encodeURIComponent(JSON.stringify({ ...S, active: null })))));
  const c2 = await b.newContext({ viewport: { width: 400, height: 860 } }); const q = await c2.newPage(); q.on('pageerror', e => errs.push('Q '+e.stack));
  await q.goto(U); await q.fill('#code', await q.evaluate(() => CONFIG.unlockCode)); await q.click('button.primary'); await q.click('[data-door="Bored"]'); await q.click('#go');
  await q.click('[data-tab="me"]'); await q.click('summary'); await q.fill('#restore', code); await q.click('#doRestore'); await q.waitForTimeout(300);
  console.log('restored xp', await q.evaluate(() => derive().xp), 'name', await q.evaluate(() => S.name));
  // reset flow
  await p.click('#reset'); await p.click('#yes'); console.log('after reset sessions', await p.evaluate(() => S.sessions.length, ), 'unlocked', await p.evaluate(()=>S.unlocked));
  console.log('errors', JSON.stringify(errs));
  await b.close();
})();
