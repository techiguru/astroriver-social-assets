// quick look: node shot.js "<query>" out.png [w] [full]
const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const [q, out, w = 390, full] = process.argv.slice(2);
  const p = await b.newPage({ viewport: { width: +w, height: +w > 900 ? 900 : 844 }, deviceScaleFactor: 1 });
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + path.resolve(__dirname, 'home.html') + '?' + q); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  await p.screenshot({ path: out, fullPage: !!full }); await b.close(); })();
