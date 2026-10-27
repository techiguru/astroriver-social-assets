// node piece.js "<query>" <selector> <out.png> [width] [dsf] — screenshot of one element (first visible match)
const { chromium } = require('playwright'); const path = require('path');
(async () => { const [q, sel, out, w = 390, dsf = 2] = process.argv.slice(2); const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +w, height: +w > 900 ? 900 : 844 }, deviceScaleFactor: +dsf });
  await p.goto('file://' + path.resolve(__dirname, 'home.html') + '?' + q); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  const el = await p.evaluateHandle(s => [...document.querySelectorAll(s)].find(e => e.getBoundingClientRect().width > 0), sel);
  await el.asElement().screenshot({ path: out }); await b.close(); })();
