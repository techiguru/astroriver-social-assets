// Round-2 renders: light, night A (lamp-black) and night B (temple maroon).
// Usage: node render.js <out-dir>
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
  const themes = [['light', 'theme=light'], ['night-a', 'theme=dark'], ['night-b', 'theme=dark&night=maroon']];
  for (const pg of ['home', 'epooja']) for (const [n, q] of themes) {
    await shot(pg + '.html', `v=phone&${q}`, 390, 844, 2, `${pg}-phone-first-screen-${n}.png`);
    await shot(pg + '.html', `v=phone&${q}&full=1`, 390, 844, 2, `${pg}-phone-full-${n}.png`, true);
    await shot(pg + '.html', `v=desktop&${q}`, 1440, 900, 1, `${pg}-desktop-first-screen-${n}.png`);
  }
  await shot('home.html', 'v=desktop&theme=light', 1440, 900, 1, 'home-desktop-full-light.png', true);
  await shot('home.html', 'v=desktop&theme=dark', 1440, 900, 1, 'home-desktop-full-night-a.png', true);
  await b.close(); console.log('done');
})();
