// Round-3 renders: light and Night A (lamp-black), phone 390 and 360, desktop 1440.
// Usage: node render.js <out-dir>       (audit.js covers large text and the full check matrix)
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
const OUT = path.resolve(process.argv[2]); fs.mkdirSync(OUT, { recursive: true });
(async () => {
  const b = await chromium.launch();
  async function shot(file, q, vw, vh, dsf, out, full) {
    const p = await b.newPage({ viewport: { width: vw, height: vh }, deviceScaleFactor: dsf });
    await p.goto('file://' + path.resolve(__dirname, file) + '?' + q);
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
    await p.screenshot({ path: path.join(OUT, out), fullPage: !!full }); await p.close();
  }
  for (const pg of ['home', 'epooja']) for (const [n, q] of [['light', 'theme=light'], ['night', 'theme=dark']]) {
    for (const w of [390, 360]) await shot(pg + '.html', `v=phone&${q}`, w, 844, 2, `${pg}-phone${w}-first-screen-${n}.png`);
    await shot(pg + '.html', `v=phone&${q}&full=1`, 390, 844, 2, `${pg}-phone390-full-${n}.png`, true);
    await shot(pg + '.html', `v=desktop&${q}`, 1440, 900, 1, `${pg}-desktop-first-screen-${n}.png`);
    if (pg === 'home') await shot(pg + '.html', `v=desktop&${q}&full=1`, 1440, 900, 1, `${pg}-desktop-full-${n}.png`, true);
  }
  for (const n of ['light', 'dark']) await shot('home.html', `v=phone&theme=${n}&seal=warm`, 390, 844, 2, `logo-warm-${n === 'dark' ? 'night' : 'light'}.png`);
  await b.close(); console.log('done');
})();
