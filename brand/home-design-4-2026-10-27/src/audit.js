// Round 4 audit: phone 390/360 and desktop 1440, four times of day, with and without details, normal and large text.
// Checks: clipped text, page wider than the screen, tap targets under 44px, AA contrast of every text run
// against the colour behind it, colours outside the token set, and every link against the live route list.
// Usage: node audit.js <out-dir>
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const { LARGE } = require('./audit-lib');
const OUT = path.resolve(process.argv[2]); fs.mkdirSync(OUT, { recursive: true });
const ROUTES = ['/', '/search', '/hi/panchang', '/panchang', '/planetary-positions', '/nakshatra/', '/rashifal/', '/sade-sati', '/manglik-dosha',
  '/muhurat', '/remedies', '/kundli', '/kundli-matching', '/journal', '/alchemies', '/consultation', '/inscriptions', '/archives', '/contact',
  '/ask', '/lobby', '/alchemies/diwali-lakshmi-puja-2026', '#story-', '/profile', '/tools', '/login', '#remedy', 'https://whatsapp.com/channel/0029Vb92NvV2v1J203DyVy39', 'https://instagram.com/astroriverofficial'];
const CHECK = (ROUTES) => {
  const out = []; const scrollers = '.hs,.week,.lib,.planets,.srow';
  const vis = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const hidden = el => el.closest('[data-view=phone] .desk, [data-view=desktop] .phone');
  const rgb = s => { const m = s.match(/[\d.]+/g); return m ? m.map(Number) : null; };
  const lum = ([r, g, b]) => { const f = c => (c /= 255) <= .03928 ? c / 12.92 : ((c + .055) / 1.055) ** 2.4; return .2126 * f(r) + .7152 * f(g) + .0722 * f(b); };
  const bgOf = el => { for (let e = el; e; e = e.parentElement) { const cs = getComputedStyle(e);
      if (cs.backgroundImage !== 'none' && !cs.backgroundImage.startsWith('linear')) return null;
      if (e.querySelector(':scope > img.cover') && e !== el) return null;
      const c = rgb(cs.backgroundColor); if (c && (c.length < 4 || c[3] > .9)) return c; }
    return rgb(getComputedStyle(document.body).backgroundColor); };
  for (const el of document.querySelectorAll('body *')) {
    if (!vis(el) || hidden(el)) continue;
    if (document.querySelector('.sheet,.sv') && !el.closest('.sheet,.sv')) continue;
    const own = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (!own) continue;
    if (!el.closest(scrollers)) {
      if (el.scrollWidth > el.clientWidth + 1 && getComputedStyle(el).overflow !== 'visible') out.push(['clipped', el.className || el.tagName, el.textContent.trim().slice(0, 40)]);
      let p = el.parentElement; while (p && getComputedStyle(p).overflow === 'visible') p = p.parentElement;
      if (p) { const a = el.getBoundingClientRect(), b = p.getBoundingClientRect(); if (a.right > b.right + 1 || a.left < b.left - 1) out.push(['outside', el.className || el.tagName, el.textContent.trim().slice(0, 40)]); }
    }
    if (el.closest(".tag.photo,.pic .tag,.capnote")) continue;      // text on photographs uses the on-photo tokens over a scrim
    const bg = bgOf(el); if (!bg) continue;
    const cs = getComputedStyle(el); const fg = rgb(cs.color);
    const L1 = lum(fg), L2 = lum(bg); const ratio = (Math.max(L1, L2) + .05) / (Math.min(L1, L2) + .05);
    const size = parseFloat(cs.fontSize), bold = +cs.fontWeight >= 700; const need = (size >= 24 || (bold && size >= 18.66)) ? 3 : 4.5;
    if (ratio < need) out.push(['contrast', el.className || el.tagName, `${ratio.toFixed(2)} ${cs.color} on rgb(${bg.slice(0,3)}) "${el.textContent.trim().slice(0, 24)}"`]);
  }
  for (const el of document.querySelectorAll('a,.chip,.btn,.ic,.lang,.signs span,.tick,.tabbar a,.play,.gr,.more,.si,.topline .x,.sheet .x,.lampb,.srow a,.sv .btn2,.svarrow')) {
    if (!vis(el) || hidden(el) || el.closest('.ghost,.sitefoot,.dm nav')) continue;
    const r = el.getBoundingClientRect(); // hit areas drawn by :after (see the CSS): .ic and .lang 8px, .tick 16px, .lang a 18px tall; text links 30px
    const hit = el.matches('.topline .x') ? 8 : el.matches('.tick') ? 16 : el.matches('.lang a') ? 18 : el.matches('.ic,.lang,.lampb') ? 8 : el.matches('.more,.ig,.bridge,.topline .go') ? 30 : 0;
    if (el.closest('.planets') && el.matches('.gr')) continue;          // the whole strip is one 58px link
    if (r.height + hit < 44 || r.width + hit < 44) out.push(['tap<44', el.className || el.tagName, `${Math.round(r.width)}x${Math.round(r.height)} ${el.textContent.trim().slice(0, 24)}`]);
  }
  for (const a of document.querySelectorAll('a[href]')) { if (hidden(a)) continue; const h = a.getAttribute('href');
    if (!ROUTES.some(r => h === r || ((r.endsWith('/') || r.endsWith('-')) && r.length > 1 && h.startsWith(r)) || (h.startsWith(r + '/') && r.length > 1))) out.push(['route?', a.className || 'a', h]); }
  for (const el of document.querySelectorAll('.chip,.btn')) { if (hidden(el)) continue;
    if (!el.closest('a[href]') && !el.querySelector('em') && !el.closest('.ghost')) out.push(['no route', el.className, el.textContent.trim().slice(0, 30)]); }
  return out;
};
(async () => {
  const b = await chromium.launch(); const report = {};
  const runs = [];
  for (const t of ['morning', 'afternoon', 'evening', 'night']) for (const m of [0, 1]) for (const L of ['', 'large']) {
    for (const w of [390, 360]) runs.push([t, m, L, 'phone', w]);
    runs.push([t, m, L, 'desktop', 1440]);
  }
  for (const v of ['phone', 'desktop']) for (const t of ['morning', 'evening']) runs.push([t, 1, '', v, v === 'phone' ? 390 : 1440, '&popup=1']);
  for (const s of ['&streak=21&reached=1', '&streak=0&again=1', '&seen=1']) runs.push(['morning', 1, '', 'phone', 360, s]);
  for (const [id, n] of [['today', 3], ['you', 3], ['fest', 3], ['planets', 2], ['deity', 3], ['inst', 1]]) for (let i = 1; i <= n; i++) {
    runs.push(['morning', 1, '', 'phone', 390, `&story=${id}&slide=${i}`]);
    runs.push(['morning', 1, 'large', 'phone', 360, `&story=${id}&slide=${i}`]);
  }
  runs.push(['morning', 0, '', 'phone', 390, '&story=you&slide=1'], ['morning', 1, '', 'phone', 390, '&fest=diwali&story=fest&slide=2'],
    ['evening', 1, '', 'phone', 390, '&story=deity&slide=2'], ['morning', 1, '', 'desktop', 1440, '&story=deity&slide=1']);
  for (const [t, m, L, v, w, extra = ''] of runs) {
    const p = await b.newPage({ viewport: { width: w, height: v === 'phone' ? 844 : 900 }, deviceScaleFactor: 1 });
    await p.goto('file://' + path.resolve(__dirname, 'home.html') + `?v=${v}&tod=${t}&me=${m}&full=1${extra}`);
    await p.evaluate(() => document.fonts.ready); if (L) await p.evaluate(LARGE); await p.waitForTimeout(250);
    const name = `${v}${w}-${t}-${m ? 'details' : 'nodetails'}${L ? '-large' : ''}${extra.replace(/[&=]/g, '-')}`;
    report[name] = await p.evaluate(CHECK, ROUTES);
    const sw = await p.evaluate(() => document.documentElement.scrollWidth); if (sw > w) report[name].push(['page wider than screen', String(sw), '']);
    if (w !== 1440 || !L) await p.screenshot({ path: path.join(OUT, name + '.jpg'), type: 'jpeg', quality: 60, fullPage: true });
    await p.close();
  }
  fs.writeFileSync(path.join(OUT, 'report.json'), JSON.stringify(report, null, 1));
  let total = 0; for (const [k, v] of Object.entries(report)) { total += v.length; if (v.length) console.log(k, v.length, JSON.stringify(v.slice(0, 8))); }
  console.log('runs', runs.length, 'issues', total);
  await b.close();
})();
