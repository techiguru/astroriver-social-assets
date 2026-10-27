// Make social posts from the templates. Usage:
//   node make.js                 every post in posts/*.json
//   node make.js posts/x.json    one post
// Each post file names its formats (feed 1080×1350, story 1080×1920, square 1080×1080) and its content;
// see README.md for the fields. Output: out/<post>-<format>.png, and out/contact.png (every image on one sheet).
// After a render, make.js checks that no text runs outside its box and that, in a story, nothing but the
// picture enters the top 250 px or the bottom 250 px.
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const DIR = __dirname, OUT = path.join(DIR, 'out'); fs.mkdirSync(OUT, { recursive: true });
const SIZE = { feed: [1080, 1350], story: [1080, 1920], square: [1080, 1080] };
const files = process.argv.length > 2 ? process.argv.slice(2).map(f => path.resolve(f))
  : fs.readdirSync(path.join(DIR, 'posts')).filter(f => f.endsWith('.json')).sort().map(f => path.join(DIR, 'posts', f));
(async () => {
  const b = await chromium.launch(); const made = []; let problems = 0;
  for (const f of files) {
    const post = JSON.parse(fs.readFileSync(f, 'utf8')); const name = path.basename(f, '.json');
    for (const fmt of post.formats) {
      const [w, h] = SIZE[fmt]; const p = await b.newPage({ viewport: { width: w, height: h } });
      await p.goto('file://' + path.join(DIR, 'post.html') + '?fmt=' + fmt + '&d=' + encodeURIComponent(JSON.stringify(post.content)));
      await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(250);
      const bad = await p.evaluate(({ fmt, h }) => {
        const out = []; const txt = document.querySelector('.txt').getBoundingClientRect(), sig = document.querySelector('.sig').getBoundingClientRect();
        const gap = sig.top - txt.bottom;
        if (gap < 24) out.push(`text runs into the signature (gap ${Math.round(gap)} px): shorten the text`);
        if (gap > 60) out.push(`empty band above the signature (gap ${Math.round(gap)} px, most 60)`);
        if (document.querySelector('.art').getBoundingClientRect().height < 260) out.push('picture squeezed under 260 px: shorten the text');
        const h1 = document.querySelector('h1'), hs = parseFloat(getComputedStyle(h1).fontSize);
        if (hs < 80 || hs > 96) out.push('headline size ' + hs + ' px (80 to 96)');
        if (window.headLines(h1) > 2) out.push('headline runs to three lines: shorten it');
        for (const e of document.querySelectorAll('.txt *')) {
          if (e.closest('h1')) continue;
          const own = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
          if (!own) continue;
          const px = parseFloat(getComputedStyle(e).fontSize), min = e.classList.contains('over') ? 30 : 40;
          if (px < min) out.push(`text under ${min} px (${px}): "${e.textContent.trim().slice(0, 30)}"`);
        }
        if (fmt === 'story') for (const e of document.querySelectorAll('.txt *, .sig')) { const r = e.getBoundingClientRect(); if (!r.width && !r.height) continue; if (r.top < 250 || r.bottom > h - 250 + 1) out.push('outside the story safe zone: ' + (e.className || e.tagName) + ' top ' + Math.round(r.top) + ' bottom ' + Math.round(r.bottom)); }
        return out;
      }, { fmt, h });
      for (const m of bad) { console.log(`${name} ${fmt}: ${m}`); problems++; }
      const file = `${name}-${fmt}.png`; await p.screenshot({ path: path.join(OUT, file) }); made.push(file); await p.close();
    }
  }
  // contact sheet
  const p = await b.newPage({ viewport: { width: 2400, height: 800 } });
  await p.setContent(`<body style="margin:0;padding:40px;background:#efe6d4;display:flex;flex-wrap:wrap;gap:28px;align-items:flex-start;width:2400px;font:600 16px Inter,sans-serif;color:#645a6c">${made.map(m => `<div><img src="file://${OUT}/${m}" style="width:${m.includes('-story') ? 300 : 360}px;display:block;box-shadow:0 8px 20px rgba(0,0,0,.15)"><div style="margin-top:8px">${m}</div></div>`).join('')}</body>`);
  await p.waitForTimeout(600); await p.screenshot({ path: path.join(OUT, 'contact.png'), fullPage: true });
  await b.close(); console.log(`${made.length} images, ${problems} problems`);
})();
