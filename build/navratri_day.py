# Navratri 2026, our own daily Reel (founder 10 Oct: "depending on gemini is hurting us... make something of our own").
# One form per day, drawn by us: a festive maroon frame, a marigold toran, a temple arch opening onto her world and
# symbols, her name, and her dhyana shloka with its meaning. No AI pictures.
# Dates (Swiss Ephemeris, Lahiri, Delhi sunrise): Pratipada Sun 11 Oct (ends 21:31 IST) ... Saptami runs over two
# sunrises (17 and 18 Oct), Navami Tue 20 Oct. Day 1 = Sun 11 Oct, Maa Shailaputri.
import os, sys, math, random, asyncio, subprocess
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
sys.path.insert(0, HERE)
import navdurga_art as A
W, H, FPS, DUR = 1080, 1920, 30, 12.0
AX, AY, AW, AH = 190, 300, 700, 820            # the arch opening

def arch_path(x, y, w, h, r=None):
    r = w / 2
    return f'M{x},{y+h} L{x},{y+r} A{r},{r} 0 0 1 {x+w},{y+r} L{x+w},{y+h} Z'

def toran():
    out, n = '', 23
    for i in range(n):                          # marigold string, scalloped, with mango leaves
        x = 20 + i * (W - 40) / (n - 1); y = 40 + 34 * math.sin(math.pi * (i % 6) / 5)
        col = ['#F7A11A', '#FFC23D', '#E8780B'][i % 3]
        out += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="21" fill="{col}"/><circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="#C9520A" opacity=".55"/>'
        if i % 3 == 1:
            out += (f'<path d="M{x:.0f},{y+18:.0f} C{x+18:.0f},{y+50:.0f} {x+10:.0f},{y+92:.0f} {x:.0f},{y+112:.0f} C{x-10:.0f},{y+92:.0f} {x-18:.0f},{y+50:.0f} {x:.0f},{y+18:.0f} Z" fill="#3E7A2C"/>'
                    f'<path d="M{x:.0f},{y+22:.0f} L{x:.0f},{y+106:.0f}" stroke="#6FA84E" stroke-width="2"/>')
    return f'<g class="sway">{out}</g>'

def petals(seed=7, n=34):
    random.seed(seed); out = ''
    for _ in range(n):
        x = random.uniform(30, W - 30); d = random.uniform(7, 12); dl = -random.uniform(0, d)
        c = random.choice(['#F7A11A', '#FFC23D', '#E8780B', '#D9461E']); s = random.uniform(.7, 1.3)
        out += (f'<div class="pt" style="left:{x:.0f}px;animation-duration:{d:.1f}s;animation-delay:{dl:.1f}s">'
                f'<div style="width:{18*s:.0f}px;height:{11*s:.0f}px;background:{c};border-radius:50%;opacity:.85;'
                f'transform:rotate({random.uniform(0,180):.0f}deg)"></div></div>')
    return out

def shailaputri_world():
    x, y, w, h = AX, AY, AW, AH
    d = A.lin('sky', [(0, '#2B3B6B'), (.42, '#B9708A'), (.72, '#F0A877'), (1, '#FCE0B4')])
    a = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#sky)"/>'
         f'<g class="sun"><circle cx="540" cy="{y+640}" r="130" fill="#FFE2A8" opacity=".9" filter="url(#soft)"/><circle cx="540" cy="{y+640}" r="80" fill="#FFF3D6"/></g>'
         + A.crescent(540, y + 150, 40, '#FFF6EA', '#33416E')
         + A.ridge(3, y + 690, 260, '#8E7C9C', x0=x - 20, x1=x + w + 20, snow='#F4ECF4')
         + A.ridge(5, y + 760, 190, '#5F4E6E', x0=x - 20, x1=x + w + 20, snow='#E4D8E8')
         + A.ridge(9, y + 830, 110, '#3B2E45', x0=x - 20, x1=x + w + 20)
         + f'<g class="glow">{A.trishul(540, y + 400, 1.05, "#FFE9C4")}</g>')
    return d, a

DAYS = {1: dict(slug='shailaputri', world=shailaputri_world,
                eb='नवरात्रि · पहला दिन', name='माँ शैलपुत्री', en='Maa Shailaputri · Day 1 of Navratri',
                shloka=['वन्दे वाञ्छितलाभाय चन्द्रार्धकृतशेखराम्।', 'वृषारूढां शूलधरां शैलपुत्रीं यशस्विनीम्॥'],
                mean='I bow to glorious Shailaputri, the daughter of the mountain, who grants what we long for. The half-moon crowns her; she rides the bull and holds the trishul.')}

def page(day):
    D = DAYS[day]; defs, world = D['world']()
    clip = f'<clipPath id="arch"><path d="{arch_path(AX, AY, AW, AH)}"/></clipPath>'
    art = (f'<svg width="{W}" height="{H}" style="position:absolute;left:0;top:0">'
           f'<defs>{defs}{clip}<filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="16"/></filter>'
           f'<filter id="halo" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="22"/></filter>'
           + A.rad('bg', [(0, '#7A1A1E', 1), (.55, '#4A0C12', 1), (1, '#1C0407', 1)], .5, .38, .85) + '</defs>'
           f'<rect width="{W}" height="{H}" fill="url(#bg)"/>'
           f'<path d="{arch_path(AX-26, AY-26, AW+52, AH+52)}" fill="#F2B544" opacity=".35" filter="url(#halo)"/>'
           f'<g clip-path="url(#arch)">{world}</g>'
           f'<path d="{arch_path(AX-14, AY-14, AW+28, AH+28)}" fill="none" stroke="#E9B24A" stroke-width="10"/>'
           f'<path d="{arch_path(AX-30, AY-30, AW+60, AH+60)}" fill="none" stroke="#E9B24A" stroke-width="3" opacity=".7"/>'
           f'{toran()}</svg>')
    sh = ''.join(f'<div>{l}</div>' for l in D['shloka'])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-style:italic;font-weight:400 900}}
@font-face{{font-family:'PFR';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700}}
@font-face{{font-family:'NSR6';src:url('{F}noto-serif-devanagari-devanagari-600-normal.woff2');font-weight:600}}
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-600-normal.woff2');font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:{W}px;height:{H}px;overflow:hidden;background:#1C0407}}
.t{{position:absolute;left:70px;right:70px;text-align:center}}
.eb{{top:1168px;font:600 34px 'NSD';color:#F2B544;letter-spacing:1px}}
.nm{{top:1222px;font:700 112px/1.25 'NSR';color:#FFF3DF;text-shadow:0 4px 30px rgba(0,0,0,.45)}}
.en{{top:1392px;font:italic 500 38px 'PF';color:#F7D9A6}}
.sh{{top:1480px;font:600 36px/1.6 'NSR6';color:#F2B544}}
.mn{{top:1610px;left:110px;right:110px;font:400 27px/1.5 'LO';color:#EBD3B6}}
.ft{{top:1800px;font:600 24px 'IN';letter-spacing:9px;color:#E9B24A;opacity:.9}}
.pt{{position:absolute;top:-40px;animation:fall linear infinite}}
@keyframes fall{{from{{transform:translateY(0) rotate(0)}} to{{transform:translateY({H+80}px) rotate(540deg)}}}}
.sway{{transform-origin:540px 0;animation:sway 6s ease-in-out infinite alternate}}
@keyframes sway{{from{{transform:rotate(-.6deg)}} to{{transform:rotate(.6deg)}}}}
.sun{{animation:rise 4s cubic-bezier(.2,.7,.3,1) both}} @keyframes rise{{from{{transform:translateY(140px);opacity:.3}} to{{transform:none;opacity:1}}}}
.glow{{animation:glow 3s 1.2s ease-out both}} @keyframes glow{{from{{opacity:0;transform:translateY(30px)}} to{{opacity:1;transform:none}}}}
.in{{animation:in 1.2s ease-out both}} @keyframes in{{from{{opacity:0;transform:translateY(24px)}} to{{opacity:1;transform:none}}}}
.zoom{{position:absolute;inset:0;animation:zm {DUR}s linear both;transform-origin:540px 700px}} @keyframes zm{{from{{transform:scale(1.06)}} to{{transform:scale(1)}}}}
</style></head><body>
<div class="zoom">{art}</div>
<div style="position:absolute;inset:0;opacity:.75">{petals()}</div>
<div class="t eb in" style="animation-delay:2.4s">{D['eb']}</div>
<div class="t nm in" style="animation-delay:3.0s">{D['name']}</div>
<div class="t en in" style="animation-delay:3.8s">{D['en']}</div>
<div class="t sh in" style="animation-delay:5.2s">{sh}</div>
<div class="t mn in" style="animation-delay:7.0s">{D['mean']}</div>
<div class="t ft in" style="animation-delay:8.4s">ASTRO RIVER</div>
</body></html>"""

async def main(day, out):
    D = DAYS[day]; os.makedirs(out, exist_ok=True)
    fn = os.path.join(out, f'navratri-day{day}-{D["slug"]}.html'); open(fn, 'w').write(page(day))
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': W, 'height': H})
        await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(500)
        await pg.evaluate('document.getAnimations().forEach(a=>a.pause())')
        async def at(t):
            await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.currentTime={t*1000}}})')
        mp4 = os.path.join(out, f'navratri-day{day}-{D["slug"]}-reel.mp4')
        ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(FPS), '-i', '-',
                               '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-movflags', '+faststart', mp4], stdin=subprocess.PIPE)
        for i in range(int(DUR * FPS)):
            await at(i / FPS); ff.stdin.write(await pg.screenshot(type='png'))
        ff.stdin.close(); ff.wait()
        await at(DUR - .01); await pg.screenshot(path=os.path.join(out, f'navratri-day{day}-{D["slug"]}-story.png'))
        await b.close()
if __name__ == '__main__':
    asyncio.run(main(int(sys.argv[1]), sys.argv[2]))
