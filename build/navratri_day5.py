# Navratri 2026, Day 5 (Thu 15 Oct, Panchami): Maa Skandamata, on the founder's approved picture (14 Oct, second
# version: baby Skanda with vibhuti and a vel). Founder 14 Oct: "Go ahead". Same idea as Day 4: the picture is never
# redrawn. It is split into layers (navratri_layers.py, then prep() below); the lake ripples gently around the lotus
# seat, while she, the baby, the lotus seat, the lion, the rock and the floating leaves and flowers stay still. Sunbeams
# from the top right breathe, mist drifts along the far shore and low over the water, her halo glows, gold dust rises.
# Layout differs from Day 4 because the lion's face sits where Day 4's name was: the name is at the top, in the sky.
# The cover moves the picture down (the plain misty sky is extended upwards) so her name sits inside the 3:4 crop
# that the Instagram profile grid shows, above her crown, as on Days 1-4.
# Usage: python3 navratri_day5.py prep          (once: water, floaters and sky layers from fg/bg)
#        python3 navratri_day5.py <absolute outdir> [check]
import os, sys, random, asyncio, subprocess
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
LD = HERE + '/out/navratri/d5/'; L = 'file://' + LD
W, H, FPS = 1080, 1920, 30
PH = 1935                              # the picture at 1080 wide
HZ = 404                               # far shore of the lake, in picture pixels: no ripples above it
HALO = (543, 372)                      # centre of her halo, in picture pixels
ORIGIN = '540px 470px'                 # the camera moves in towards her face
EXT = 260                              # sky added above the picture (only the cover uses most of it)
COVER_SHIFT = 170                      # the cover places the picture this much lower
T = dict(full=dict(dur=13.0, en=.2, nm=1.2, band=2.6, sh=3.0, mn=4.8, end=10.4),
         short=dict(dur=8.0, en=0, nm=.6, band=1.2, sh=1.5, mn=2.7, end=6.2))
TXT = dict(day='दिन 5', name='माँ स्कन्दमाता', en='Maa Skandamata · Day 5 of Navratri',
           shloka=['या देवी सर्वभूतेषु माँ स्कन्दमाता रूपेण संस्थिता।', 'नमस्तस्यै नमस्तस्यै नमस्तस्यै नमो नमः॥'],
           mean='To the Goddess who dwells in all beings as Maa Skandamata: salutations to her, again and again.')


def prep():
    """water.jpg: the background with floating leaves, flowers and the rock filled in with water, for the ripples.
    floaters.png: those leaves, flowers and the rock, cut out, laid back on top so they never wobble.
    sky-ext.jpg: plain misty sky continued above the picture's top edge."""
    import numpy as np, cv2
    from PIL import Image
    bg = np.asarray(Image.open(LD + 'bg.jpg').convert('RGB')).astype(np.uint8)
    fga = np.asarray(Image.open(LD + 'fg.png'))[..., 3].astype(np.float32) / 255
    h, w = bg.shape[:2]
    hsv = cv2.cvtColor(bg, cv2.COLOR_RGB2HSV); Hh, S, V = hsv[..., 0].astype(int), hsv[..., 1].astype(int), hsv[..., 2].astype(int)
    yy = np.arange(h)[:, None] * np.ones((1, w), int)
    lake = yy > HZ + 30
    leaf = (Hh >= 25) & (Hh <= 75) & (S > 55) & (V > 70)                    # lily pads
    flower = ((Hh >= 140) | (Hh <= 12)) & (S > 35) & (V > 150)              # lotus flowers and buds
    # the rock under the lion is one solid object: drawn by hand from the picture (its waterline), never classified
    rock = np.zeros((h, w), np.uint8)
    cv2.fillPoly(rock, [np.array([(522, 1640), (560, 1600), (620, 1575), (1080, 1555), (1080, 1745), (950, 1752), (800, 1750),
                                  (700, 1742), (620, 1730), (570, 1705), (535, 1675)], np.int32)], 1)
    m = (((leaf | flower) & lake) | (rock > 0)).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    keep = np.zeros(n, bool); keep[1:] = st[1:, cv2.CC_STAT_AREA] > 60; m = keep[lab].astype(np.uint8)
    # fill holes inside each leaf or flower so their inner shadows do not ripple
    ff = m.copy(); cv2.floodFill(ff, None, (0, h - 1), 1); holes = (ff == 0).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(holes); small = np.zeros(n, bool); small[1:] = st[1:, cv2.CC_STAT_AREA] < 900
    m = (m | small[lab]).astype(np.uint8)                                     # only small holes: open water keeps rippling
    m = cv2.dilate(m, np.ones((3, 3), np.uint8))
    a = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 1.0)
    a = a * (1 - cv2.erode((fga > .5).astype(np.uint8), np.ones((13, 13), np.uint8)))   # under the figures: their own layer
    Image.fromarray(np.dstack([bg, (a * 255).astype(np.uint8)]), 'RGBA').save(LD + 'floaters.png')
    # water: the floaters (and a margin) replaced by surrounding water, so a ripple never drags their colour around
    hole = cv2.dilate(m, np.ones((9, 9), np.uint8))
    s = 2; small = cv2.resize(bg, (w // s, h // s), interpolation=cv2.INTER_AREA)
    hs = cv2.resize(hole, (w // s, h // s), interpolation=cv2.INTER_NEAREST)
    fill = cv2.resize(cv2.inpaint(small, hs, 7, cv2.INPAINT_TELEA), (w, h), interpolation=cv2.INTER_CUBIC)
    k = cv2.GaussianBlur(hole.astype(np.float32), (0, 0), 2)[..., None]
    water = bg * (1 - k) + fill * k
    Image.fromarray(np.clip(water, 0, 255).astype(np.uint8)).save(LD + 'water.jpg', quality=95)
    Image.fromarray((m * 255).astype(np.uint8)).save(LD + '_floaters-mask.png')
    # sky above the top edge: the top rows mirrored (soft mist has no direction), blurred more the further up,
    # drifting towards the smooth colour of the top edge
    src = np.asarray(Image.open(LD + 'bg.jpg').convert('RGB')).astype(np.float32)
    mir = src[:EXT][::-1]
    base = cv2.GaussianBlur(src[:24].mean(0, keepdims=True).repeat(EXT, 0), (0, 0), 30)
    out = np.zeros_like(mir)
    for i, sig in enumerate((2, 6, 12, 22)):
        b = cv2.GaussianBlur(mir, (0, 0), sig); lo, hi = i * EXT // 4, (i + 1) * EXT // 4
        out[EXT - hi:EXT - lo] = b[EXT - hi:EXT - lo]
    out = cv2.GaussianBlur(out, (0, 0), 3)
    out[-6:] = mir[-6:]
    t = (np.linspace(1, 0, EXT) ** 1.4)[:, None, None]                         # 1 at the very top
    out = out * (1 - .55 * t) + base * .55 * t
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(LD + 'sky-ext.jpg', quality=95)
    print('prep done', int(m.sum()), 'floater px')


def dust(n, seed, front, y0=180, y1=1500):
    random.seed(seed); out = ''
    for _ in range(n):
        x = random.uniform(30, W - 30); y = random.uniform(y0, y1); d = random.uniform(10, 18); dl = -random.uniform(0, d)
        r = random.uniform(1.4, 3.2) * (1.25 if front else 1); rise = random.uniform(220, 520); dx = random.uniform(-45, 45)
        tw = random.uniform(1.6, 3.2); twd = -random.uniform(0, tw); op = random.uniform(.5, .95)
        out += (f'<div class="du" style="left:{x:.0f}px;top:{y:.0f}px;--rise:-{rise:.0f}px;--dx:{dx:.0f}px;animation-duration:{d:.1f}s;'
                f'animation-delay:{dl:.1f}s"><div class="tw" style="width:{2*r:.1f}px;height:{2*r:.1f}px;opacity:{op:.2f};'
                f'animation-duration:{tw:.1f}s;animation-delay:{twd:.1f}s"></div></div>')
    return out


def glints(n, seed):
    # small sun glints on the open water, twinkling (sunlight comes from the top right)
    random.seed(seed); out = ''
    while n:
        x = random.uniform(40, W - 40); y = random.uniform(HZ + 20, 1150)
        if random.random() > (x / W) ** 0.6: continue                          # more on the sunlit right
        n -= 1; w_ = random.uniform(8, 22) * (0.5 + (y - HZ) / 900); d = random.uniform(1.4, 3.4); dl = -random.uniform(0, d)
        out += (f'<div class="gl" style="left:{x:.0f}px;top:{y:.0f}px;width:{w_:.0f}px;height:{max(1.5, w_ / 9):.1f}px;'
                f'animation-duration:{d:.1f}s;animation-delay:{dl:.1f}s"></div>')
    return out


def page(mode='full', cover=False, x=False):
    # x: the 1080 x 1350 picture for X, a still from the crown down to the lion's face, her name small in the sky
    t = T[mode]; D = t['dur']; sh = ''.join(f'<div>{l}</div>' for l in TXT['shloka'])
    hx, hy = HALO; shift = COVER_SHIFT if cover else (-110 if x else 0); HH = 1350 if x else H
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-style:italic;font-weight:400 900}}
@font-face{{font-family:'PFR';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700}}
@font-face{{font-family:'NSR6';src:url('{F}noto-serif-devanagari-devanagari-600-normal.woff2');font-weight:600}}
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-600-normal.woff2');font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:{W}px;height:{HH}px;overflow:hidden;background:#E9EEE8}}
.cam{{position:absolute;inset:0;transform-origin:{ORIGIN};animation:cam {D}s linear both}} .x .cam,.x .fgw{{animation:none}}
@keyframes cam{{from{{transform:scale(1)}} to{{transform:scale(1.04)}}}}
.stage{{position:absolute;left:0;top:{shift - 8}px;width:{W}px;height:{PH}px}}
.fgw{{position:absolute;inset:0;transform-origin:{ORIGIN};animation:fgp {D}s linear both}}
@keyframes fgp{{from{{transform:scale(1)}} to{{transform:scale(1.025)}}}}
.pic{{position:absolute;left:0;top:0;width:{W}px}} .ext{{position:absolute;left:0;top:-{EXT}px;width:{W}px;height:{EXT}px}}
#wv{{position:absolute;left:0;top:0;width:{W}px;height:{PH}px}}
.glow{{position:absolute;left:{hx-360}px;top:{hy-360}px;width:720px;height:720px;border-radius:50%;
 background:radial-gradient(circle,rgba(255,250,232,.85) 0,rgba(255,236,190,.45) 30%,rgba(255,220,160,.12) 50%,rgba(255,220,160,0) 66%);
 mix-blend-mode:screen;animation:breathe 4.6s ease-in-out infinite alternate}}
@keyframes breathe{{from{{opacity:.35;transform:scale(.95)}} to{{opacity:.85;transform:scale(1.05)}}}}
.rays{{position:absolute;left:{hx-900}px;top:{hy-900}px;width:1800px;height:1800px;border-radius:50%;
 background:repeating-conic-gradient(from 0deg,rgba(255,244,214,0) 0deg,rgba(255,244,214,.5) 2.4deg,rgba(255,244,214,0) 5.5deg,rgba(255,244,214,0) 12deg);
 -webkit-mask-image:radial-gradient(circle,rgba(0,0,0,.9) 8%,rgba(0,0,0,.35) 20%,rgba(0,0,0,0) 38%);
 filter:blur(4px);mix-blend-mode:screen;opacity:.3;animation:spin {D}s linear both,rb 6s ease-in-out infinite alternate}}
@keyframes spin{{from{{transform:rotate(0deg)}} to{{transform:rotate({6 if mode == 'full' else 4}deg)}}}}
@keyframes rb{{from{{opacity:.2}} to{{opacity:.38}}}}
.beam{{position:absolute;top:-300px;height:2000px;transform-origin:50% 0;mix-blend-mode:screen;filter:blur(16px);
 background:linear-gradient(rgba(255,246,220,.55),rgba(255,240,205,.22) 45%,rgba(255,240,205,0) 85%);animation:bm ease-in-out infinite alternate}}
@keyframes bm{{from{{opacity:.25}} to{{opacity:.85}}}}
.mist{{position:absolute;pointer-events:none}}
.ma{{left:-260px;top:{HZ - 210}px;width:1700px;height:380px;opacity:.75;animation:drl {D}s linear both}}
.mb{{left:-420px;top:{HZ + 170}px;width:1700px;height:300px;opacity:.42;animation:drr {D}s linear both}}
@keyframes drl{{from{{transform:translateX(0)}} to{{transform:translateX(-{200 if mode == 'full' else 125}px)}}}}
@keyframes drr{{from{{transform:translateX(0)}} to{{transform:translateX({180 if mode == 'full' else 110}px)}}}}
.gl{{position:absolute;border-radius:50%;background:radial-gradient(ellipse,rgba(255,252,236,.95) 0,rgba(255,240,200,.5) 45%,rgba(255,240,200,0) 75%);
 mix-blend-mode:screen;animation:gt ease-in-out infinite alternate}}
@keyframes gt{{from{{opacity:0}} to{{opacity:.9}}}}
.du{{position:absolute;animation:rise linear infinite}}
@keyframes rise{{from{{transform:translate(0,0)}} to{{transform:translate(var(--dx),var(--rise))}}}}
.tw{{border-radius:50%;background:radial-gradient(circle,#FFF8E0 0,#FFD98A 45%,rgba(255,200,110,0) 72%);
 box-shadow:0 0 8px 2px rgba(255,215,130,.5);animation:twk ease-in-out infinite alternate}}
@keyframes twk{{from{{filter:brightness(.7)}} to{{filter:brightness(1.35)}}}}
.top{{position:absolute;left:0;right:0;top:0;height:330px;background:linear-gradient(rgba(252,246,236,.66),rgba(252,246,236,.34) 55%,rgba(252,246,236,0))}}
.bot{{position:absolute;left:0;right:0;top:1392px;bottom:0;
 background:linear-gradient(rgba(251,245,232,0),rgba(251,245,232,.84) 96px,rgba(251,245,232,.94) 200px);animation:in 1.1s {t['band']}s ease-out both}}
.t{{position:absolute;left:70px;right:70px;text-align:center}}
.glowtxt{{text-shadow:0 0 14px rgba(255,250,238,.95),0 0 4px rgba(255,250,238,.9)}}
.mk{{top:34px;font:600 25px 'PFR';letter-spacing:9px;color:#7A1F2B}}
.en{{top:66px;font:italic 500 32px 'PF';color:#5A2614}}
.nm{{top:126px;font:700 100px/1.22 'NSR';color:#7A1F2B;text-shadow:0 0 26px rgba(255,250,238,.95),0 0 8px rgba(255,250,238,.95)}}
.sh{{top:1500px;font:600 35px/1.55 'NSR6';color:#9E3E0E}}
.mn{{top:1620px;left:110px;right:110px;font:400 28px/1.42 'LO';color:#3B2417}}
.end{{position:absolute;inset:0;background:rgba(251,245,232,.96);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;animation:fi 1s {t['end']}s ease-out both}}
.end .a{{font:600 70px 'PFR';letter-spacing:16px;color:#7A1F2B}} .end .l{{width:280px;height:2px;background:linear-gradient(90deg,rgba(201,151,58,0),#C9973A,rgba(201,151,58,0))}}
.end .b{{font:600 24px 'IN';letter-spacing:5px;color:#6B4A2E}} .end .c{{font:600 32px 'IN';letter-spacing:4px;color:#B5651D;margin-top:14px}}
.dy{{display:none}}
.cover .en,.cover .sh,.cover .mn,.cover .end,.cover .bot{{display:none}}
.cover .mk{{top:46px}} .cover .top{{height:470px;background:linear-gradient(rgba(252,246,236,.6),rgba(252,246,236,.36) 60%,rgba(252,246,236,0))}}
.cover .dy{{display:block;top:250px;font:600 38px 'NSD';color:#8E2B12;letter-spacing:1px}}
.cover .nm{{top:284px;font-size:116px}}
.x .en,.x .sh,.x .mn,.x .end,.x .bot,.x .dy{{display:none}} .x .mk{{top:8px;font-size:21px}} .x .nm{{top:52px;font-size:68px}}
.x .top{{height:300px}}
.in{{animation:in 1.3s ease-out both}} @keyframes in{{from{{opacity:0;transform:translateY(22px)}} to{{opacity:1;transform:none}}}}
.fadein{{animation:fi 1.4s ease-out both}} @keyframes fi{{from{{opacity:0}} to{{opacity:1}}}}
</style></head><body class="{'cover' if cover else ('x' if x else '')}">
<div class="cam"><div class="stage">
  <img class="ext" src="{L}sky-ext.jpg">
  <canvas id="wv" width="{W}" height="{PH}"></canvas>
  <img class="pic" src="{L}floaters.png">
  {glints(30, 5)}
  <img class="mist ma" src="{L}mist-a.png">
  <div class="beam" style="left:860px;width:120px;transform:rotate(24deg);animation-duration:5.2s;animation-delay:-1s"></div>
  <div class="beam" style="left:960px;width:170px;transform:rotate(30deg);animation-duration:6.4s;animation-delay:-3.5s"></div>
  <div class="beam" style="left:1060px;width:140px;transform:rotate(37deg);animation-duration:4.6s;animation-delay:-2s"></div>
  <div class="glow"></div><div class="rays"></div>
  <img class="mist mb" src="{L}mist-b.png">
  {dust(22, 3, False)}
  <div class="fgw"><img class="pic" src="{L}fg.png"></div>
</div></div>
{dust(12, 9, True, 300, 1400)}
<div class="top"></div><div class="bot"></div>
<div class="t mk glowtxt">ASTRO RIVER</div>
<div class="t dy glowtxt">{TXT['day']}</div>
<div class="t en glowtxt in" style="animation-delay:{t['en']}s">{TXT['en']}</div>
<div class="t nm in" style="animation-delay:{t['nm']}s">{TXT['name']}</div>
<div class="t sh in" style="animation-delay:{t['sh']}s">{sh}</div>
<div class="t mn in" style="animation-delay:{t['mn']}s">{TXT['mean']}</div>
<div class="end"><div class="a">ASTRO RIVER</div><div class="l"></div><div class="b">INSTITUTE · EST. 2008 · JALANDHAR, INDIA</div><div class="c">astroriver.com</div></div>
<script>
// the lake: each row of the water picture is slid sideways a little, by waves that are finer towards the far shore
const HZ = {HZ}, PH = {PH}, W = {W};
const img = new Image(); img.src = '{L}water.jpg';
window.ready = img.decode();
const cv = document.getElementById('wv'), cx = cv.getContext('2d');
const phase = new Float32Array(PH); let acc = 0;
for (let y = 0; y < PH; y++) {{ const d = Math.max(0, (y - HZ) / (PH - HZ)); acc += 1 / (5 + 46 * d); phase[y] = acc * 2 * Math.PI; }}
window.drawWater = (t) => {{
  cx.drawImage(img, 0, 0);
  for (let y = HZ; y < PH; y++) {{
    const d = (y - HZ) / (PH - HZ), ramp = Math.min(1, (y - HZ) / 70);
    const A = ramp * (0.35 + 2.6 * Math.pow(d, 1.1));
    const dx = A * (0.65 * Math.sin(phase[y] - 2 * Math.PI * t / 2.3) + 0.35 * Math.sin(1.73 * phase[y] + 2 * Math.PI * t / 3.4));
    cx.drawImage(img, 0, y, W, 1, dx, y, W, 1);
  }}
}};
</script>
</body></html>"""


async def render(out, check=False):
    os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': W, 'height': H})
        async def load(html, name):
            fn = os.path.join(out, name); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.evaluate('window.ready')
            await pg.wait_for_timeout(800)
            await pg.evaluate('document.getAnimations().forEach(a=>a.pause())')
        async def at(s):
            await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.currentTime={s*1000}}}); drawWater({s})')
        if check:
            await load(page('full'), 'navratri-day5-skandamata-photo.html')
            for s in (0.0, 1.0, 1.033, 6.6, 9.8, 12.9):
                await at(s); await pg.screenshot(path=os.path.join(out, f'_d5-check-{s}.png'))
            await load(page('full', cover=True), 'navratri-day5-skandamata-cover.html')
            await at(13); await pg.screenshot(path=os.path.join(out, '_d5-check-cover.png'))
            await b.close(); return
        for mode in ('full', 'short'):
            D = T[mode]['dur']; tag = 'reel' if mode == 'full' else 'short-8s'
            await load(page(mode), f'navratri-day5-skandamata-{tag}.html')
            mp4 = os.path.join(out, f'navratri-day5-skandamata-{tag}.mp4')
            ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(FPS), '-i', '-', '-c:v', 'libx264',
                                   '-pix_fmt', 'yuv420p', '-crf', '16', '-preset', 'slow', '-movflags', '+faststart', mp4], stdin=subprocess.PIPE)
            for i in range(int(D * FPS)):
                await at(i / FPS); ff.stdin.write(await pg.screenshot(type='jpeg', quality=95))
            ff.stdin.close(); ff.wait()
            if mode == 'full':
                await at(9.8); await pg.screenshot(path=os.path.join(out, 'navratri-day5-skandamata-lastframe.png'))
        await load(page('full', cover=True), 'navratri-day5-skandamata-cover.html')
        await at(13); await pg.screenshot(path=os.path.join(out, 'navratri-day5-skandamata-cover.png'))
        await pg.add_style_tag(content='.dy{display:none!important}')
        await at(1.2); await pg.screenshot(path=os.path.join(out, 'navratri-day5-skandamata-status.png'))
        await pg.set_viewport_size({'width': W, 'height': 1350})
        await load(page('full', x=True), 'navratri-day5-skandamata-x.html')
        await at(13); await pg.screenshot(path=os.path.join(out, 'navratri-day5-skandamata-x.png'))
        await b.close()

if __name__ == '__main__':
    if sys.argv[1] == 'prep': prep()
    else: asyncio.run(render(sys.argv[1], len(sys.argv) > 2))
