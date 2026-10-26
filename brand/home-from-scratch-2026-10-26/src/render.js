// Render each direction: phone first screen, phone one scroll down, desktop first screen.
// Usage: node render.js <dir-with-html> <out-dir> [A,B,C] [scrollY per direction as A:780,B:820]
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const [,, SRC, OUT, which = 'A,B,C', scrolls = ''] = process.argv;
const SCROLL = Object.fromEntries(scrolls.split(',').filter(Boolean).map((s) => s.split(':')).map(([k, v]) => [k, +v]));
const NAMES = { A: 'A-temple-morning', B: 'B-the-almanac', C: 'C-the-app' };
(async () => {
  const browser = await chromium.launch();
  for (const d of which.split(',')) {
    const dir = path.join(OUT, NAMES[d]); fs.mkdirSync(dir, { recursive: true });
    const url = 'file://' + path.resolve(SRC, d + '.html');
    const ph = await browser.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
    await ph.goto(url + '?v=phone'); await ph.evaluate(() => document.fonts.ready); await ph.waitForTimeout(300);
    await ph.screenshot({ path: path.join(dir, 'phone-1-first-screen.png') });
    await ph.evaluate((y) => window.scrollTo(0, y), SCROLL[d] || 780); await ph.waitForTimeout(200);
    await ph.screenshot({ path: path.join(dir, 'phone-2-scrolled.png') });
    await ph.close();
    const dk = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    await dk.goto(url + '?v=desktop'); await dk.evaluate(() => document.fonts.ready); await dk.waitForTimeout(300);
    await dk.screenshot({ path: path.join(dir, 'desktop-first-screen.png') });
    await dk.close();
    console.log('rendered', d);
  }
  await browser.close();
})();
