# Navratri 2026, Day Reel built on the founder's own picture of the form (founder 10 Oct: the drawn version "is weak").
# Our motion and words on his picture: slow push-in, drifting snow and mist, warm light, then her name, her dhyana
# shloka and its meaning. The picture is used as made, never edited to change what it shows.
import os, sys, random, asyncio, subprocess
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
W, H, FPS, DUR = 1080, 1920, 30, 13.0

DAYS = {1: dict(slug='shailaputri', img='out/navratri/shail-bg.jpg', ox=-54, oy=-120, fx=611, fy=640,
                eb='नवरात्रि · पहला दिन', day='दिन 1', name='माँ शैलपुत्री', en='Maa Shailaputri · Day 1 of Navratri',
                shloka=['वन्दे वाञ्छितलाभाय चन्द्रार्धकृतशेखराम्।', 'वृषारूढां शूलधरां शैलपुत्रीं यशस्विनीम्॥'],
                mean='Daughter of the mountain. The half-moon crowns her; she rides the bull and holds the trishul.'),
        # Day 2, Mon 12 Oct (Dwitiya at Delhi sunrise; ends 22:13 IST). Dhyana shloka: two arms, akshamala and kamandalu.
        2: dict(slug='brahmacharini', img='out/navratri/brahma-bg.jpg', ox=-54, oy=-120, fx=611, fy=640,
                eb='नवरात्रि · दूसरा दिन', day='दिन 2', name='माँ ब्रह्मचारिणी', en='Maa Brahmacharini · Day 2 of Navratri',
                shloka=['दधाना करपद्माभ्यामक्षमालाकमण्डलू।', 'देवी प्रसीदतु मयि ब्रह्मचारिण्यनुत्तमा॥'],
                mean='The goddess of tapasya. In her two lotus hands, the rosary and the water pot. May she be gracious to us.'),
        # Day 3, Tue 13 Oct (Tritiya at Delhi sunrise; ends 23:28 IST). Bell-shaped half-moon on her brow; rides the tiger.
        3: dict(slug='chandraghanta', img='out/navratri/chandra-bg.jpg', ox=0, oy=-8, fx=540, fy=520,
                eb='नवरात्रि · तीसरा दिन', day='दिन 3', name='माँ चन्द्रघण्टा', en='Maa Chandraghanta · Day 3 of Navratri',
                shloka=['पिण्डजप्रवरारूढा चण्डकोपास्त्रकैर्युता।', 'प्रसादं तनुते मह्यं चन्द्रघण्टेति विश्रुता॥'],
                mean='Riding the finest of beasts, bearing fierce weapons, renowned as Chandraghanta. May she extend her grace to us.')}

def snow(n=70, seed=4):
    random.seed(seed); out = ''
    for _ in range(n):
        x = random.uniform(0, W); d = random.uniform(9, 16); dl = -random.uniform(0, d); r = random.uniform(2, 5)
        dx = random.uniform(-60, 60); op = random.uniform(.35, .9)
        out += (f'<div class="sn" style="left:{x:.0f}px;--dx:{dx:.0f}px;animation-duration:{d:.1f}s;animation-delay:{dl:.1f}s">'
                f'<div style="width:{2*r:.0f}px;height:{2*r:.0f}px;border-radius:50%;background:#fff;opacity:{op:.2f};filter:blur({r/3:.1f}px)"></div></div>')
    return out

def page(day, cover=False):
    D = DAYS[day]; img = 'file://' + os.path.join(HERE, D['img'])
    sh = ''.join(f'<div>{l}</div>' for l in D['shloka'])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-style:italic;font-weight:400 900}}
@font-face{{font-family:'PFR';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700}}
@font-face{{font-family:'NSR6';src:url('{F}noto-serif-devanagari-devanagari-600-normal.woff2');font-weight:600}}
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-600-normal.woff2');font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:{W}px;height:{H}px;overflow:hidden;background:#120806}}
.ph{{position:absolute;left:{D['ox']}px;top:{D['oy']}px;transform-origin:{D['fx']}px {D['fy']}px;animation:push {DUR}s linear both}}
@keyframes push{{from{{transform:scale(1.0)}} to{{transform:scale(1.13)}}}}
.ray{{position:absolute;right:-260px;top:-200px;width:900px;height:900px;border-radius:50%;
 background:radial-gradient(circle,rgba(255,214,150,.55),rgba(255,180,90,.18) 40%,rgba(255,170,80,0) 70%);mix-blend-mode:screen;animation:breathe 5s ease-in-out infinite alternate}}
@keyframes breathe{{from{{opacity:.55;transform:scale(.95)}} to{{opacity:1;transform:scale(1.06)}}}}
.mist{{position:absolute;width:1400px;height:260px;border-radius:50%;background:radial-gradient(ellipse,rgba(255,255,255,.35),rgba(255,255,255,0) 70%);filter:blur(10px)}}
.m1{{top:880px;left:-500px;animation:drift 14s linear both}} .m2{{top:1120px;left:200px;animation:drift2 14s linear both}}
@keyframes drift{{from{{transform:translateX(0)}} to{{transform:translateX(320px)}}}} @keyframes drift2{{from{{transform:translateX(0)}} to{{transform:translateX(-300px)}}}}
.sn{{position:absolute;top:-20px;animation:fall linear infinite}}
@keyframes fall{{from{{transform:translate(0,0)}} to{{transform:translate(var(--dx),{H+40}px)}}}}
.vig{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(0,0,0,0) 55%,rgba(10,4,2,.55) 100%)}}
.top{{position:absolute;left:0;right:0;top:0;height:300px;background:linear-gradient(rgba(12,6,4,.7),rgba(12,6,4,0))}}
.bot{{position:absolute;left:0;right:0;bottom:0;height:1000px;background:linear-gradient(rgba(14,6,3,0),rgba(14,6,3,.78) 38%,rgba(14,6,3,.94));animation:in 1.2s 1.4s ease-out both}}
.t{{position:absolute;left:70px;right:70px;text-align:center}}
.mk{{top:46px;font:600 25px 'PFR';letter-spacing:9px;color:#F5D58A;text-shadow:0 2px 12px rgba(0,0,0,.6)}}
.eb{{top:104px;font:600 36px 'NSD';color:#FFD98A;letter-spacing:1px;text-shadow:0 2px 14px rgba(0,0,0,.6)}}
.ebl{{top:158px;left:420px;right:420px;height:2px;background:linear-gradient(90deg,rgba(255,217,138,0),#FFD98A,rgba(255,217,138,0))}}
.nm{{top:1150px;font:700 128px/1.25 'NSR';color:#FFE3A3;text-shadow:0 0 40px rgba(255,190,90,.45),0 4px 24px rgba(0,0,0,.6)}}
.en{{top:1322px;font:italic 500 40px 'PF';color:#FBE8C8}}
.sh{{top:1406px;font:600 36px/1.6 'NSR6';color:#F5C566}}
.mn{{top:1540px;left:120px;right:120px;font:400 29px/1.45 'LO';color:#EBDCC8}}
.end{{position:absolute;inset:0;background:rgba(14,6,3,.9);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;animation:fi 1s 10.4s ease-out both}}
.end .a{{font:600 70px 'PFR';letter-spacing:16px;color:#F5D58A}} .end .l{{width:280px;height:2px;background:linear-gradient(90deg,rgba(245,213,138,0),#F5D58A,rgba(245,213,138,0))}}
.end .b{{font:600 24px 'IN';letter-spacing:5px;color:#FBE8C8}} .end .c{{font:600 32px 'IN';letter-spacing:4px;color:#E9B24A;margin-top:14px}}
.cover .en,.cover .sh,.cover .mn,.cover .end,.cover .eb,.cover .ebl{{display:none}} .dy{{display:none}} .cover .dy{{display:block;top:1350px;font:600 40px 'NSD';color:#F5D58A;letter-spacing:1px}}
.cover .nm{{top:1400px}} .cover .bot{{height:900px}}
.in{{animation:in 1.3s ease-out both}} @keyframes in{{from{{opacity:0;transform:translateY(22px)}} to{{opacity:1;transform:none}}}}
.fadein{{animation:fi 1.4s ease-out both}} @keyframes fi{{from{{opacity:0}} to{{opacity:1}}}}
</style></head><body class="{'cover' if cover else ''}">
<img class="ph" src="{img}">
<div class="ray"></div><div class="mist m1"></div><div class="mist m2"></div>
{snow()}
<div class="vig"></div><div class="top"></div><div class="bot"></div>
<div class="t mk">ASTRO RIVER</div>
<div class="t dy">{D['day']}</div>
<div class="t eb in" style="animation-delay:.2s">{D['eb']}</div><div class="ebl fadein" style="animation-delay:.6s"></div>
<div class="t nm in" style="animation-delay:1.8s">{D['name']}</div>
<div class="t en in" style="animation-delay:2.8s">{D['en']}</div>
<div class="t sh in" style="animation-delay:4.0s">{sh}</div>
<div class="t mn in" style="animation-delay:5.8s">{D['mean']}</div>
<div class="end"><div class="a">ASTRO RIVER</div><div class="l"></div><div class="b">INSTITUTE · EST. 2008 · JALANDHAR, INDIA</div><div class="c">astroriver.com</div></div>
</body></html>"""

async def main(day, out, check=False):
    D = DAYS[day]; os.makedirs(out, exist_ok=True)
    fn = os.path.join(out, f'navratri-day{day}-{D["slug"]}-photo.html'); open(fn, 'w').write(page(day))
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': W, 'height': H})
        await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(600)
        await pg.evaluate('document.getAnimations().forEach(a=>a.pause())')
        async def at(t): await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.currentTime={t*1000}}})')
        if check:
            for t in (2, 13.9):
                await at(t); await pg.screenshot(path=os.path.join(out, f'_photo-check-{t}.png'))
        else:
            mp4 = os.path.join(out, f'navratri-day{day}-{D["slug"]}-reel-v4.mp4')
            ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(FPS), '-i', '-', '-c:v', 'libx264',
                                   '-pix_fmt', 'yuv420p', '-crf', '17', '-preset', 'medium', '-movflags', '+faststart', mp4], stdin=subprocess.PIPE)
            for i in range(int(DUR * FPS)):
                await at(i / FPS); ff.stdin.write(await pg.screenshot(type='jpeg', quality=95))
            ff.stdin.close(); ff.wait()
            await at(9.5); await pg.screenshot(path=os.path.join(out, f'navratri-day{day}-{D["slug"]}-lastframe-v4.png'))
            cf = os.path.join(out, f'navratri-day{day}-{D["slug"]}-cover.html'); open(cf, 'w').write(page(day, True))
            await pg.goto('file://' + cf); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.evaluate('document.getAnimations().forEach(a=>{a.pause();a.currentTime=13000})')
            await pg.screenshot(path=os.path.join(out, f'navratri-day{day}-{D["slug"]}-cover-v4.png'))
            await at(1.2); await pg.screenshot(path=os.path.join(out, f'navratri-day{day}-{D["slug"]}-story-v4.png'))
        await b.close()
if __name__ == '__main__':
    asyncio.run(main(int(sys.argv[1]), sys.argv[2], len(sys.argv) > 3))
