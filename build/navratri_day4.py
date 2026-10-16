# Navratri 2026, Day 4 (Wed 14 Oct, Chaturthi): Maa Kushmanda, on the founder's approved picture (13 Oct, with kamandalu).
# Founder 13 Oct: add movement, "You do it. Make it impeccable." The picture is never redrawn: it is split into layers
# (navratri_layers.py) that move apart slightly for depth, the sun behind her breathes and sends slow rays, cloud mist
# drifts across the cloud sea and gold dust rises. Light theme: this picture is bright, so the text sits on cream, not
# on a dark band; her name sits in the open sky above her crown, so her face and the lion stay clear.
# Usage: python3 navratri_day4.py <absolute outdir> [check]
import os, sys, random, asyncio, subprocess
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'; L = 'file://' + HERE + '/out/navratri/d4/'
W, H, FPS = 1080, 1920, 30
SUN = (554, 562)                      # sun centre on the frame (picture 1080 x 1935 placed at top -8)
ORIGIN = '540px 760px'                # the camera moves in towards her chest and face
T = dict(full=dict(dur=13.0, eb=.2, ebl=.6, nm=1.8, band=2.5, en=2.8, sh=4.0, mn=5.8, end=10.4),
         short=dict(dur=8.0, eb=0, ebl=.3, nm=.9, band=1.3, en=1.6, sh=2.4, mn=3.6, end=6.2))
TXT = dict(eb='नवरात्रि · चौथा दिन', day='दिन 4', name='माँ कूष्माण्डा', en='Maa Kushmanda · Day 4 of Navratri',
           shloka=['या देवी सर्वभूतेषु माँ कूष्माण्डा रूपेण संस्थिता।', 'नमस्तस्यै नमस्तस्यै नमस्तस्यै नमो नमः॥'],
           mean='To the Goddess who dwells in all beings as Maa Kushmanda: salutations to her, again and again.')

def dust(n, seed, front):
    random.seed(seed); out = ''
    for _ in range(n):
        x = random.uniform(30, W - 30); y = random.uniform(500, H + 80); d = random.uniform(9, 17); dl = -random.uniform(0, d)
        r = random.uniform(1.6, 3.6) * (1.3 if front else 1); rise = random.uniform(260, 620); dx = random.uniform(-50, 50)
        tw = random.uniform(1.6, 3.2); twd = -random.uniform(0, tw); op = random.uniform(.55, 1)
        out += (f'<div class="du" style="left:{x:.0f}px;top:{y:.0f}px;--rise:-{rise:.0f}px;--dx:{dx:.0f}px;animation-duration:{d:.1f}s;'
                f'animation-delay:{dl:.1f}s"><div class="tw" style="width:{2*r:.1f}px;height:{2*r:.1f}px;opacity:{op:.2f};'
                f'animation-duration:{tw:.1f}s;animation-delay:{twd:.1f}s"></div></div>')
    return out

def page(mode='full', cover=False):
    t = T[mode]; D = t['dur']; sh = ''.join(f'<div>{l}</div>' for l in TXT['shloka'])
    sx, sy = SUN
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-style:italic;font-weight:400 900}}
@font-face{{font-family:'PFR';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700}}
@font-face{{font-family:'NSR6';src:url('{F}noto-serif-devanagari-devanagari-600-normal.woff2');font-weight:600}}
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-600-normal.woff2');font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:{W}px;height:{H}px;overflow:hidden;background:#F6E2C2}}
.cam{{position:absolute;inset:0;transform-origin:{ORIGIN};animation:cam {D}s linear both}}
@keyframes cam{{from{{transform:scale(1)}} to{{transform:scale(1.05)}}}}
.fgw{{position:absolute;inset:0;transform-origin:{ORIGIN};animation:fgp {D}s linear both}}
@keyframes fgp{{from{{transform:scale(1)}} to{{transform:scale(1.03)}}}}
.pic{{position:absolute;left:0;top:-8px;width:{W}px}}
.glow{{position:absolute;left:{sx-430}px;top:{sy-430}px;width:860px;height:860px;border-radius:50%;
 background:radial-gradient(circle,rgba(255,249,228,.9) 0,rgba(255,230,170,.5) 28%,rgba(255,205,130,.16) 48%,rgba(255,200,120,0) 64%);
 mix-blend-mode:screen;animation:breathe 4.6s ease-in-out infinite alternate}}
@keyframes breathe{{from{{opacity:.42;transform:scale(.95)}} to{{opacity:.92;transform:scale(1.06)}}}}
.rays{{position:absolute;left:{sx-1150}px;top:{sy-1150}px;width:2300px;height:2300px;border-radius:50%;
 background:repeating-conic-gradient(from 0deg,rgba(255,241,206,0) 0deg,rgba(255,241,206,.55) 2.6deg,rgba(255,241,206,0) 6deg,rgba(255,241,206,0) 13deg);
 -webkit-mask-image:radial-gradient(circle,rgba(0,0,0,.95) 10%,rgba(0,0,0,.45) 24%,rgba(0,0,0,0) 50%);
 filter:blur(4px);mix-blend-mode:screen;opacity:.42;animation:spin {D}s linear both,rb 6s ease-in-out infinite alternate}}
@keyframes spin{{from{{transform:rotate(0deg)}} to{{transform:rotate({7 if mode == 'full' else 4.5}deg)}}}}
@keyframes rb{{from{{opacity:.28}} to{{opacity:.5}}}}
.mist{{position:absolute;pointer-events:none}}
.ma{{left:-260px;top:1210px;width:1700px;opacity:.88;animation:drl {D}s linear both}}
.mb{{left:-420px;top:1390px;width:1700px;opacity:.72;animation:drr {D}s linear both}}
@keyframes drl{{from{{transform:translateX(0)}} to{{transform:translateX(-{220 if mode == 'full' else 140}px)}}}}
@keyframes drr{{from{{transform:translateX(0)}} to{{transform:translateX({200 if mode == 'full' else 125}px)}}}}
.du{{position:absolute;animation:rise linear infinite}}
@keyframes rise{{from{{transform:translate(0,0)}} to{{transform:translate(var(--dx),var(--rise))}}}}
.tw{{border-radius:50%;background:radial-gradient(circle,#FFF8E0 0,#FFD98A 45%,rgba(255,200,110,0) 72%);
 box-shadow:0 0 8px 2px rgba(255,215,130,.55);animation:twk ease-in-out infinite alternate}}
@keyframes twk{{from{{filter:brightness(.7)}} to{{filter:brightness(1.35)}}}}
.top{{position:absolute;left:0;right:0;top:0;height:380px;background:linear-gradient(rgba(252,244,230,.62),rgba(252,244,230,.3) 55%,rgba(252,244,230,0))}}
.bot{{position:absolute;left:0;right:0;top:1290px;bottom:0;
 background:linear-gradient(rgba(251,243,228,0),rgba(251,243,228,.84) 80px,rgba(251,243,228,.94) 260px);animation:in 1.1s {t['band']}s ease-out both}}
.t{{position:absolute;left:70px;right:70px;text-align:center}}
.glowtxt{{text-shadow:0 0 14px rgba(255,248,232,.95),0 0 4px rgba(255,248,232,.9)}}
.mk{{top:46px;font:600 25px 'PFR';letter-spacing:9px;color:#7A1F2B}}
.eb{{top:100px;font:600 34px 'NSD';color:#8E2B12;letter-spacing:1px}}
.ebl{{position:absolute;top:150px;left:420px;right:420px;height:2px;background:linear-gradient(90deg,rgba(122,31,43,0),#7A1F2B,rgba(122,31,43,0))}}
.nm{{top:162px;font:700 112px/1.22 'NSR';color:#7A1F2B;text-shadow:0 0 28px rgba(255,247,230,.95),0 0 8px rgba(255,247,230,.95)}}
.en{{top:1372px;font:italic 500 40px 'PF';color:#5A2614}}
.sh{{top:1436px;font:600 35px/1.6 'NSR6';color:#9E3E0E}}
.mn{{top:1566px;left:110px;right:110px;font:400 29px/1.45 'LO';color:#3B2417}}
.end{{position:absolute;inset:0;background:rgba(251,243,228,.96);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;animation:fi 1s {t['end']}s ease-out both}}
.end .a{{font:600 70px 'PFR';letter-spacing:16px;color:#7A1F2B}} .end .l{{width:280px;height:2px;background:linear-gradient(90deg,rgba(201,151,58,0),#C9973A,rgba(201,151,58,0))}}
.end .b{{font:600 24px 'IN';letter-spacing:5px;color:#6B4A2E}} .end .c{{font:600 32px 'IN';letter-spacing:4px;color:#B5651D;margin-top:14px}}
.dy{{display:none}}
.cover .en,.cover .sh,.cover .mn,.cover .end,.cover .eb,.cover .ebl{{display:none}}
.cover .dy{{display:block;top:1352px;font:600 40px 'NSD';color:#8E2B12;letter-spacing:1px}}
.cover .nm{{top:1398px;font-size:128px;text-shadow:none}} .cover .bot{{top:1200px;background:linear-gradient(rgba(251,243,228,0),rgba(251,243,228,.86) 130px,rgba(251,243,228,.94) 320px)}}
.in{{animation:in 1.3s ease-out both}} @keyframes in{{from{{opacity:0;transform:translateY(22px)}} to{{opacity:1;transform:none}}}}
.fadein{{animation:fi 1.4s ease-out both}} @keyframes fi{{from{{opacity:0}} to{{opacity:1}}}}
</style></head><body class="{'cover' if cover else ''}">
<div class="cam">
  <img class="pic" src="{L}bg.jpg">
  <div class="glow"></div><div class="rays"></div>
  <img class="mist ma" src="{L}mist-a.png">
  {dust(34, 3, False)}
  <div class="fgw"><img class="pic" src="{L}fg.png"></div>
</div>
<img class="mist mb" src="{L}mist-b.png">
{dust(28, 9, True)}
<div class="top"></div><div class="bot"></div>
<div class="t mk glowtxt">ASTRO RIVER</div>
<div class="t dy">{TXT['day']}</div>
<div class="t eb glowtxt in" style="animation-delay:{t['eb']}s">{TXT['eb']}</div><div class="ebl fadein" style="animation-delay:{t['ebl']}s"></div>
<div class="t nm in" style="animation-delay:{t['nm']}s">{TXT['name']}</div>
<div class="t en in" style="animation-delay:{t['en']}s">{TXT['en']}</div>
<div class="t sh in" style="animation-delay:{t['sh']}s">{sh}</div>
<div class="t mn in" style="animation-delay:{t['mn']}s">{TXT['mean']}</div>
<div class="end"><div class="a">ASTRO RIVER</div><div class="l"></div><div class="b">INSTITUTE · EST. 2008 · JALANDHAR, INDIA</div><div class="c">astroriver.com</div></div>
</body></html>"""

async def render(out, check=False):
    os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': W, 'height': H})
        async def load(html, name):
            fn = os.path.join(out, name); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(800)
            await pg.evaluate('document.getAnimations().forEach(a=>a.pause())')
        async def at(s): await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.currentTime={s*1000}}})')
        if check:
            await load(page('full'), 'navratri-day4-kushmanda-photo.html')
            for s in (0.0, 2.2, 6.6, 9.8, 12.9):
                await at(s); await pg.screenshot(path=os.path.join(out, f'_d4-check-{s}.png'))
            await load(page('full', cover=True), 'navratri-day4-kushmanda-cover.html')
            await at(13); await pg.screenshot(path=os.path.join(out, '_d4-check-cover.png'))
            await b.close(); return
        for mode in ('full', 'short'):
            D = T[mode]['dur']; tag = 'reel' if mode == 'full' else 'short-8s'
            await load(page(mode), f'navratri-day4-kushmanda-{tag}.html')
            mp4 = os.path.join(out, f'navratri-day4-kushmanda-{tag}.mp4')
            ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(FPS), '-i', '-', '-c:v', 'libx264',
                                   '-pix_fmt', 'yuv420p', '-crf', '16', '-preset', 'slow', '-movflags', '+faststart', mp4], stdin=subprocess.PIPE)
            for i in range(int(D * FPS)):
                await at(i / FPS); ff.stdin.write(await pg.screenshot(type='jpeg', quality=95))
            ff.stdin.close(); ff.wait()
            if mode == 'full':
                await at(9.8); await pg.screenshot(path=os.path.join(out, 'navratri-day4-kushmanda-lastframe.png'))
        await load(page('full', cover=True), 'navratri-day4-kushmanda-cover.html')
        await at(13); await pg.screenshot(path=os.path.join(out, 'navratri-day4-kushmanda-cover.png'))
        await pg.add_style_tag(content='.dy{display:none!important}')
        await at(1.2); await pg.screenshot(path=os.path.join(out, 'navratri-day4-kushmanda-status.png'))
        await b.close()

if __name__ == '__main__':
    asyncio.run(render(sys.argv[1], len(sys.argv) > 2))
