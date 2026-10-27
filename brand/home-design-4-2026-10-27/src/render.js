// Round 4 renders. Usage: node render.js <out-dir>
// Phone 390 first screen x 4 times of day x (no details, with details); three whole phone pages;
// desktop 1440 morning light and evening night; phone 360 at large text, morning.
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
const { LARGE } = require('./audit-lib');
const OUT = path.resolve(process.argv[2]); fs.mkdirSync(OUT, { recursive: true });
(async () => {
  const b = await chromium.launch();
  async function shot(q, vw, vh, dsf, out, full, large) {
    const p = await b.newPage({ viewport: { width: vw, height: vh }, deviceScaleFactor: dsf });
    await p.goto('file://' + path.resolve(__dirname, 'home.html') + '?' + q);
    await p.evaluate(() => document.fonts.ready); if (large) await p.evaluate(LARGE); await p.waitForTimeout(400);
    await p.screenshot({ path: path.join(OUT, out), fullPage: !!full, type: out.endsWith('.jpg') ? 'jpeg' : 'png', quality: out.endsWith('.jpg') ? 82 : undefined }); await p.close();
  }
  for (const t of ['morning', 'afternoon', 'evening', 'night']) for (const m of [0, 1])
    await shot(`v=phone&tod=${t}&me=${m}`, 390, 844, 2, `phone390-first-${t}-${m ? 'with-details' : 'no-details'}.png`);
  await shot('v=phone&tod=morning&me=0&full=1', 390, 844, 1.5, 'phone390-full-morning-light-no-details.jpg', true);
  await shot('v=phone&tod=morning&me=1&full=1', 390, 844, 1.5, 'phone390-full-morning-light-with-details.jpg', true);
  await shot('v=phone&tod=evening&me=1&full=1', 390, 844, 1.5, 'phone390-full-evening-night-with-details.jpg', true);
  await shot('v=desktop&tod=morning&me=0&full=1', 1440, 900, 1, 'desktop1440-full-morning-light-no-details.jpg', true);
  await shot('v=desktop&tod=evening&me=1&full=1', 1440, 900, 1, 'desktop1440-full-evening-night-with-details.jpg', true);
  await shot('v=desktop&tod=morning&me=0', 1440, 900, 1, 'desktop1440-first-morning-light.png');
  await shot('v=phone&tod=morning&me=1', 360, 800, 2, 'phone360-first-morning-large-text.png', false, true);
  await shot('v=phone&tod=morning&me=1&full=1', 360, 800, 1, 'phone360-full-morning-large-text.jpg', true, true);
  // 4.2: top line (first screens above already carry it), pop-up, streak states
  async function scrolled(q, vw, vh, out) {           // the pop-up as it appears after ~50% scroll, over the remedy, not the panchang
    const p = await b.newPage({ viewport: { width: vw, height: vh }, deviceScaleFactor: vw > 900 ? 1 : 2 });
    await p.goto('file://' + path.resolve(__dirname, 'home.html') + '?' + q); await p.evaluate(() => document.fonts.ready);
    await p.evaluate(() => { const e = [...document.querySelectorAll('.rem')].find(e => e.getBoundingClientRect().width > 0); scrollTo(0, e.getBoundingClientRect().top + scrollY - 60); });
    await p.waitForTimeout(300); await p.screenshot({ path: path.join(OUT, out) }); await p.close();
  }
  await scrolled('v=phone&tod=morning&me=1&popup=1', 390, 844, 'popup-phone390-light.png');
  await scrolled('v=phone&tod=evening&me=1&popup=1', 390, 844, 'popup-phone390-night.png');
  await scrolled('v=desktop&tod=morning&me=0&popup=1', 1440, 900, 'popup-desktop1440-light.png');
  await shot('v=phone&tod=morning&me=1', 390, 844, 2, 'topline-phone390-light.png');
  await shot('v=phone&tod=evening&me=1', 390, 844, 2, 'topline-phone390-night.png');
  await shot('v=desktop&tod=morning&me=1', 1440, 900, 1, 'topline-desktop1440-light.png');
  async function piece(q, out) {
    const p = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
    await p.goto('file://' + path.resolve(__dirname, 'home.html') + '?' + q); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
    const el = await p.evaluateHandle(() => [...document.querySelectorAll('.rem')].find(e => e.getBoundingClientRect().width > 0));
    await el.asElement().screenshot({ path: path.join(OUT, out) }); await p.close();
  }
  await piece('v=phone&tod=morning&me=0&full=1', 'streak-0-new-visitor-light.png');
  await piece('v=phone&tod=morning&me=1&full=1', 'streak-12-days-light.png');
  await piece('v=phone&tod=morning&me=1&streak=21&reached=1&full=1', 'streak-21-lamp-reached-light.png');
  await piece('v=phone&tod=evening&me=1&full=1', 'streak-12-days-night.png');
  await piece('v=phone&tod=morning&me=1&streak=0&again=1&full=1', 'streak-start-again-light.png');
  // 3x views of the whole morning-with-details page, cut to phone-screen parts (see ../view/)
  { const p = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3 });
    await p.goto('file://' + path.resolve(__dirname, 'home.html') + '?v=phone&tod=morning&me=1&full=1'); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
    await p.screenshot({ path: path.join(OUT, 'view-full-3x.png'), fullPage: true }); await p.close(); }
  // logo: warm maroon, decided (4.2); logo-warm-maroon.png is round 3.1's tile
  await b.close(); console.log('done');
})();
