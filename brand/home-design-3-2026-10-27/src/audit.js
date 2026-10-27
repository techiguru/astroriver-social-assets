// Audit: every page at phone 390/360 and desktop 1440, light and night, normal and large text (~130%).
// Writes full-page screenshots and a list of clipped text and small tap targets.
// Usage: node audit.js <out-dir>
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const OUT = path.resolve(process.argv[2]); fs.mkdirSync(OUT, { recursive: true });
const LARGE = () => {           // body text x1.3, tapering to x1.0 for display type of 40px and up
  for (const el of document.querySelectorAll('body *')) {
    if (el.closest('.top,.tabbar,.status,.dm,.bar .t')) continue;   // app chrome keeps its size, as on iOS
    const fs = parseFloat(getComputedStyle(el).fontSize);
    const k = fs <= 18 ? 1.3 : fs >= 40 ? 1 : 1.3 - 0.3 * (fs - 18) / 22;
    el.dataset.fs = fs * k;
  }
  for (const el of document.querySelectorAll('[data-fs]')) el.style.fontSize = el.dataset.fs + 'px';
};
const CHECK = () => {
  const out = []; const scrollers = '.hs,.stories,.week,.lib,.chips-row';
  const vis = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  for (const el of document.querySelectorAll('body *')) {
    if (!vis(el) || el.closest(scrollers) || el.closest('[data-view=phone] .desk, [data-view=desktop] .phone')) continue;
    const own = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (own && (el.scrollWidth > el.clientWidth + 1) && getComputedStyle(el).overflow !== 'visible') out.push(['clipped', el.className || el.tagName, el.textContent.trim().slice(0, 40)]);
    if (own) {
      let p = el.parentElement; while (p && getComputedStyle(p).overflow === 'visible') p = p.parentElement;
      if (p) { const a = el.getBoundingClientRect(), b = p.getBoundingClientRect();
        if (a.right > b.right + 1 || a.left < b.left - 1) out.push(['outside', el.className || el.tagName, el.textContent.trim().slice(0, 40)]); }
    }
  }
  for (const el of document.querySelectorAll('.chip,.btn,.ic,.lang,.signs span,.week>div,.story,.tabbar a,.play,.cats>div,.st,.nav span,.fields div,.papers div,.lib span,.si')) {
    if (!vis(el) || el.closest('[data-view=phone] .desk, [data-view=desktop] .phone')) continue;
    const r = el.getBoundingClientRect(); const hit = el.classList.contains('ic') || el.closest('.lang') ? 8 : 0;
    if (r.height + hit < 44 || r.width + hit < 44) out.push(['tap<44', el.className || el.tagName, `${Math.round(r.width)}x${Math.round(r.height)} ${el.textContent.trim().slice(0, 24)}`]);
  }
  return out;
};
(async () => {
  const b = await chromium.launch(); const report = {};
  const runs = [];
  for (const pg of ['home', 'epooja']) for (const th of ['light', 'dark']) for (const t of ['', 'large']) {
    for (const w of [390, 360]) runs.push([pg, th, t, 'phone', w]);
    runs.push([pg, th, t, 'desktop', 1440]);
  }
  for (const [pg, th, t, v, w] of runs) {
    const p = await b.newPage({ viewport: { width: w, height: v === 'phone' ? 844 : 900 }, deviceScaleFactor: 1 });
    await p.goto('file://' + path.resolve(__dirname, pg + '.html') + `?v=${v}&theme=${th}&full=1`);
    await p.evaluate(() => document.fonts.ready); if (t) await p.evaluate(LARGE); await p.waitForTimeout(300);
    const name = `${pg}-${v}${w}-${th === 'dark' ? 'night' : 'light'}${t ? '-large' : ''}`;
    report[name] = await p.evaluate(CHECK);
    const sw = await p.evaluate(() => document.documentElement.scrollWidth); if (sw > w) report[name].push(['page wider than screen', String(sw), '']);
    await p.screenshot({ path: path.join(OUT, name + '.png'), fullPage: true }); await p.close();
  }
  fs.writeFileSync(path.join(OUT, 'report.json'), JSON.stringify(report, null, 1));
  for (const [k, v] of Object.entries(report)) console.log(k, v.length, JSON.stringify(v.slice(0, 12)));
  await b.close();
})();
