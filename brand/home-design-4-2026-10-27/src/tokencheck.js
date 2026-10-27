// Lists every colour the page computes that is not in tokens.json (both themes, all four times of day).
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const tok = JSON.parse(fs.readFileSync(path.resolve(__dirname, '../tokens.json')));
const hex = h => { h = h.replace('#', ''); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16)).join(','); };
const allowed = new Set(['0,0,0', '255,255,255']);   // transparent / shadows
for (const g of Object.values(tok)) if (typeof g === 'object') for (const v of Object.values(g)) {
  if (v.startsWith('#')) allowed.add(hex(v)); else { const m = v.match(/[\d.]+/g); if (m) allowed.add(m.slice(0, 3).join(',')); } }
(async () => { const b = await chromium.launch(); const bad = {};
  for (const t of ['morning', 'afternoon', 'evening', 'night']) for (const v of ['phone', 'desktop']) for (const m of [0, 1]) for (const x of ['', '&popup=1', '&story=today&slide=2', '&story=deity&slide=2', '&fest=diwali&story=fest&slide=2']) {
    const p = await b.newPage(); await p.goto('file://' + path.resolve(__dirname, 'home.html') + `?v=${v}&tod=${t}&me=${m}&full=1${x}`);
    const cols = await p.evaluate(() => { const s = new Set(); for (const el of document.querySelectorAll('body *')) { const c = getComputedStyle(el);
      for (const k of ['color', 'backgroundColor', 'borderTopColor']) { const m = c[k].match(/[\d.]+/g); if (m && (m.length < 4 || +m[3] > 0) && !(k === 'borderTopColor' && c.borderTopWidth === '0px')) s.add(m.slice(0, 3).join(',')); } } return [...s]; });
    for (const c of cols) if (!allowed.has(c)) (bad[c] = bad[c] || []).push(`${v}-${t}-${m}`); await p.close(); }
  console.log(Object.keys(bad).length ? bad : 'every colour is a token'); await b.close(); })();
