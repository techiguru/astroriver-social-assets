// node overview.js <out.png>
const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 3000, height: 1000 } });
  await p.goto('file://' + path.resolve(__dirname, 'overview.html')); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  await p.screenshot({ path: process.argv[2], fullPage: true }); await b.close(); })();
