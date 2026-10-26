// Render the combined home (and the ePooja page) to PNG.
// Usage: node render.js <out-dir> [pages=home,epooja]
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const OUT = path.resolve(process.argv[2]); fs.mkdirSync(OUT, { recursive: true });
const pages = (process.argv[3] || 'home,epooja').split(',');
(async () => {
  const b = await chromium.launch();
  async function shot(file, q, vw, vh, dsf, out, full) {
    const p = await b.newPage({ viewport: { width: vw, height: vh }, deviceScaleFactor: dsf });
    await p.goto('file://' + path.resolve(__dirname, file) + '?' + q);
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
    await p.screenshot({ path: path.join(OUT, out), fullPage: !!full });
    await p.close();
  }
  for (const pg of pages) {
    for (const th of ['light', 'dark']) {
      await shot(pg + '.html', `v=phone&theme=${th}`, 390, 844, 2, `${pg}-phone-first-screen-${th}.png`);
      await shot(pg + '.html', `v=phone&theme=${th}&full=1`, 390, 844, 2, `${pg}-phone-full-${th}.png`, true);
      await shot(pg + '.html', `v=desktop&theme=${th}`, 1440, 900, 1, `${pg}-desktop-first-screen-${th}.png`);
    }
    await shot(pg + '.html', 'v=desktop&theme=light', 1440, 900, 1, `${pg}-desktop-full-light.png`, true);
    console.log('rendered', pg);
  }
  await b.close();
})();
