// Render the crest SVGs to PNG with headless Chromium (Playwright).
// Usage: node render.js <crest-redraw folder>
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(process.argv[2]);
const uri = (p) => 'data:image/svg+xml;base64,' + fs.readFileSync(p).toString('base64');
const OPT = [1, 2, 3];

async function shot(page, html, w, h, out) {
  await page.setViewportSize({ width: w, height: h });
  await page.setContent(`<!doctype html><html><head><style>
    html,body{margin:0;padding:0;width:${w}px;height:${h}px;overflow:hidden}
    body{font:500 15px/1.3 "DejaVu Sans",sans-serif;color:#3a3550}
    img{display:block}
  </style></head><body>${html}</body></html>`);
  await page.waitForLoadState('load');
  await page.screenshot({ path: out, omitBackground: false });
}

// one row of round avatars at true pixel size (the browser rasterises
// the vector at each size, as a phone would)
function avatars(src, bg, label) {
  const sizes = [48, 64, 128];
  const cells = sizes.map((s) => `<div style="display:flex;flex-direction:column;align-items:center;gap:8px">
      <img src="${src}" width="${s}" height="${s}" style="border-radius:50%">
      <span style="font-size:12px;color:${bg === '#ffffff' ? '#666' : '#9aa3a8'}">${s} px</span></div>`).join('');
  return `<div style="background:${bg};padding:18px 22px;display:flex;align-items:flex-end;gap:28px;border-radius:10px">
    <span style="width:110px;font-size:13px;align-self:center;color:${bg === '#ffffff' ? '#555' : '#c9c3e0'}">${label}</span>${cells}</div>`;
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 1 });

  for (const n of OPT) {
    const d = path.join(ROOT, `option-${n}`);
    const icon = uri(path.join(d, 'icon.svg'));
    const cream = uri(path.join(d, 'icon-cream.svg'));
    await shot(page, `<img src="${icon}" width="1024" height="1024">`, 1024, 1024, path.join(d, 'icon-1024.png'));
    await shot(page, `<img src="${cream}" width="1024" height="1024">`, 1024, 1024, path.join(d, 'icon-cream-1024.png'));
    await shot(page, `<img src="${uri(path.join(d, 'lockup.svg'))}" width="1200" height="1500">`, 1200, 1500, path.join(d, 'lockup.png'));
    const zoom = `<div style="display:flex;gap:12px;align-items:center;padding:4px 22px 0">
        <span style="width:110px;font-size:13px;color:#555">48 px, enlarged ×4 to inspect</span>
        <canvas id="z" width="192" height="192" style="border-radius:50%"></canvas>
        <canvas id="zc" width="192" height="192" style="border-radius:50%"></canvas></div>`;
    await shot(page, `<div style="background:#ffffff;padding:16px;display:flex;flex-direction:column;gap:14px;width:640px">
        <div style="font-weight:700;font-size:17px;padding:0 6px">Option ${n} — small sizes (true pixels)</div>
        ${avatars(icon, '#ffffff', 'Indigo, on a light chat list')}
        ${avatars(icon, '#111b21', 'Indigo, on a dark chat list')}
        ${avatars(cream, '#ffffff', 'Cream, on a light chat list')}
        ${zoom}</div>
        <script>
        for (const [id,src] of [['z','${icon}'],['zc','${cream}']]) {
          const im=new Image(); im.onload=()=>{const t=document.createElement('canvas');t.width=t.height=48;
            t.getContext('2d').drawImage(im,0,0,48,48);const c=document.getElementById(id).getContext('2d');
            c.imageSmoothingEnabled=false;c.drawImage(t,0,0,192,192);}; im.src=src; }
        </script>`, 672, 860, path.join(d, 'small-test.png'));
    console.log('rendered option', n);
  }

  // compare sheet: today's crest and the three options, large and small
  const cur = 'data:image/jpeg;base64,' + fs.readFileSync(path.join(ROOT, 'inputs/current-crest-card.jpg')).toString('base64');
  const names = ['Today', '1 · Faithful flat', '2 · Minimal monogram', '3 · Classical fine-line'];
  const icons = [null, ...OPT.map((n) => uri(path.join(ROOT, `option-${n}/icon.svg`)))];
  const lockups = [null, ...OPT.map((n) => uri(path.join(ROOT, `option-${n}/lockup.svg`)))];
  const col = (i) => {
    const big = i === 0
      ? `<div style="width:340px;height:425px;display:flex;align-items:center;justify-content:center;background:#2a1760;border-radius:8px;overflow:hidden"><img src="${cur}" style="height:425px;width:auto;object-fit:cover;object-position:center;width:340px"></div>`
      : `<img src="${lockups[i]}" width="340" height="425" style="border-radius:8px">`;
    const sm = i === 0
      ? [48, 64, 128].map((s) => `<div style="width:${s}px;height:${s}px;border-radius:50%;overflow:hidden;background:#2a1760"><img src="${cur}" style="height:${s * 1.3}px;width:auto;margin-left:${-s * 0.738}px;margin-top:${-s * 0.03}px"></div>`).join('')
      : [48, 64, 128].map((s) => `<img src="${icons[i]}" width="${s}" height="${s}" style="border-radius:50%">`).join('');
    return `<div style="display:flex;flex-direction:column;gap:14px;align-items:center">
      <div style="font-weight:700;font-size:18px;color:#efe6c8">${names[i]}</div>${big}
      <div style="display:flex;gap:16px;align-items:flex-end;background:#fff;padding:14px 18px;border-radius:8px">${sm}</div></div>`;
  };
  await shot(page, `<div style="background:#120e30;padding:34px 30px;display:flex;gap:26px;width:1504px;height:700px;box-sizing:border-box">${[0, 1, 2, 3].map(col).join('')}</div>`,
    1504, 700, path.join(ROOT, 'compare.png'));
  console.log('rendered compare');
  await browser.close();
})();
