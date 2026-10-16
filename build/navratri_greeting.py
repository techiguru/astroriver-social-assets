# "Happy Navratri from Astro River" greeting for WhatsApp sharing and Status (founder 11 Oct).
# Our own art: a gold mandala round a lit diya, marigold garlands, a row of diyas, petals. Two sizes: 1080x1350, 1080x1920.
import os, sys, math, random, asyncio
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
def mandala(cx, cy, R):
    g = '#E9B24A'; out = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{g}" stroke-width="3" opacity=".9"/>'
    out += f'<circle cx="{cx}" cy="{cy}" r="{R-18}" fill="none" stroke="{g}" stroke-width="1.5" opacity=".6"/>'
    for k, (n, r1, r2, w) in enumerate([(32, R-30, R-.3*R, 30), (16, R-.33*R, R-.57*R, 52), (12, R-.6*R, R-.78*R, 44)]):
        for i in range(n):
            a = 2 * math.pi * i / n + (math.pi / n if k % 2 else 0)
            x1, y1 = cx + r1 * math.cos(a), cy + r1 * math.sin(a); x2, y2 = cx + r2 * math.cos(a), cy + r2 * math.sin(a)
            nx, ny = -math.sin(a) * w / 2, math.cos(a) * w / 2; mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            out += (f'<path d="M{x1:.1f},{y1:.1f} Q{mx+nx:.1f},{my+ny:.1f} {x2:.1f},{y2:.1f} Q{mx-nx:.1f},{my-ny:.1f} {x1:.1f},{y1:.1f} Z" '
                    f'fill="{["#F2B544","#E07A1F","#C9452A"][k]}" opacity="{[.9,.85,.8][k]}"/>')
        out += f'<circle cx="{cx}" cy="{cy}" r="{r2-6}" fill="none" stroke="{g}" stroke-width="1.5" opacity=".7"/>'
    for i in range(48):
        a = 2 * math.pi * i / 48
        out += f'<circle cx="{cx+(R-9)*math.cos(a):.1f}" cy="{cy+(R-9)*math.sin(a):.1f}" r="3.2" fill="{g}"/>'
    return out
def diya(cx, cy, s, glow=True):
    out = ''
    if glow: out += f'<circle cx="{cx}" cy="{cy-60*s}" r="{90*s}" fill="url(#flameglow)"/>'
    out += (f'<path d="M{cx-70*s},{cy-12*s} Q{cx},{cy+52*s} {cx+70*s},{cy-12*s} Q{cx+40*s},{cy-4*s} {cx},{cy-6*s} Q{cx-40*s},{cy-4*s} {cx-70*s},{cy-12*s} Z" fill="#B5532A"/>'
            f'<path d="M{cx-70*s},{cy-12*s} Q{cx},{cy+52*s} {cx+70*s},{cy-12*s}" fill="none" stroke="#F2B544" stroke-width="{3*s}"/>'
            f'<ellipse cx="{cx}" cy="{cy-10*s}" rx="{58*s}" ry="{8*s}" fill="#6B2412"/>'
            f'<path d="M{cx},{cy-82*s} C{cx+18*s},{cy-52*s} {cx+14*s},{cy-24*s} {cx},{cy-16*s} C{cx-14*s},{cy-24*s} {cx-18*s},{cy-52*s} {cx},{cy-82*s} Z" fill="#FFB238"/>'
            f'<path d="M{cx},{cy-62*s} C{cx+8*s},{cy-44*s} {cx+7*s},{cy-28*s} {cx},{cy-22*s} C{cx-7*s},{cy-28*s} {cx-8*s},{cy-44*s} {cx},{cy-62*s} Z" fill="#FFF3C4"/>')
    return out
def garland(x0, y0, x1, y1, sag, n=17):
    out = ''
    for i in range(n):
        t = i / (n - 1); x = x0 + (x1 - x0) * t; y = y0 + (y1 - y0) * t + sag * 4 * t * (1 - t)
        out += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="19" fill="{["#F7A11A","#FFC23D","#E8780B"][i%3]}"/><circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="#C9520A" opacity=".5"/>'
    return out
def page(W, H):
    random.seed(11)
    tall = H > 1500
    cy = int(H * (.38 if tall else .335)); R = 300 if tall else 250
    petals = ''.join(f'<ellipse cx="{random.uniform(0,W):.0f}" cy="{random.uniform(0,H):.0f}" rx="{random.uniform(6,11):.0f}" ry="{random.uniform(4,7):.0f}" '
                     f'fill="{random.choice(["#F7A11A","#FFC23D","#E8780B","#D9461E"])}" opacity=".7" transform="rotate({random.uniform(0,180):.0f})" style="transform-box:fill-box;transform-origin:center"/>' for _ in range(40))
    row = ''.join(diya(W/2 + (i - 3) * 138, H - (330 if H > 1500 else 132), .7 if H > 1500 else .55) for i in range(7))
    svg = (f'<svg width="{W}" height="{H}" style="position:absolute;left:0;top:0"><defs>'
           f'<radialGradient id="bg" cx=".5" cy=".38" r=".8"><stop offset="0" stop-color="#8E1B2A"/><stop offset=".5" stop-color="#5A0C1A"/><stop offset="1" stop-color="#22050B"/></radialGradient>'
           f'<radialGradient id="flameglow"><stop offset="0" stop-color="#FFD27A" stop-opacity=".75"/><stop offset="1" stop-color="#FFB238" stop-opacity="0"/></radialGradient>'
           f'<radialGradient id="halo"><stop offset="0" stop-color="#FFCF70" stop-opacity=".45"/><stop offset=".6" stop-color="#F2A040" stop-opacity=".12"/><stop offset="1" stop-color="#F2A040" stop-opacity="0"/></radialGradient></defs>'
           f'<rect width="{W}" height="{H}" fill="url(#bg)"/>{petals}'
           f'<circle cx="{W/2}" cy="{cy}" r="{R+120}" fill="url(#halo)"/>{mandala(W/2, cy, R)}'
           f'<circle cx="{W/2}" cy="{cy}" r="{R*.2}" fill="#3A0712"/>{diya(W/2, cy+38*R/300, 1.15*R/300)}'
           f'{garland(-10, 10, W*.42, 40, 140)}{garland(W*.58, 40, W+10, 10, 140)}{row}'
           f'<rect x="26" y="26" width="{W-52}" height="{H-52}" rx="18" fill="none" stroke="#E9B24A" stroke-width="2" opacity=".55"/>'
           f'<rect x="38" y="38" width="{W-76}" height="{H-76}" rx="12" fill="none" stroke="#E9B24A" stroke-width="1" opacity=".35"/></svg>')
    tt = cy + R + (70 if tall else 44)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'PFR';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-style:italic;font-weight:400 900}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}} body{{width:{W}px;height:{H}px;overflow:hidden;background:#22050B}}
.c{{position:absolute;left:60px;right:60px;text-align:center}}
.hi{{top:{tt}px;font:700 {96 if tall else 84}px/1.25 'NSR';color:#FFE3A3;text-shadow:0 0 30px rgba(255,190,90,.45),0 3px 18px rgba(0,0,0,.5)}}
.en{{top:{tt+(128 if tall else 110)}px;font:italic 600 {58 if tall else 50}px 'PF';color:#F5D58A}}
.wish{{top:{tt+(214 if tall else 182)}px;font:italic 400 {32 if tall else 28}px/1.45 'PF';color:#FBE8C8;left:90px;right:90px}}
.from{{top:{H-(130 if H > 1500 else 84)}px;font:600 22px 'IN';letter-spacing:6px;color:#E9B24A}}
</style></head><body>{svg}
<div class="c hi">शुभ नवरात्रि</div><div class="c en">Happy Navratri</div>
<div class="c wish">May Maa Durga bless your home with strength, peace and joy.</div>
<div class="c from">FROM ASTRO RIVER INSTITUTE · ASTRORIVER.COM</div></body></html>"""
async def main(out):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for W, H, name in [(1080, 1350, 'happy-navratri-share-1080x1350'), (1080, 1920, 'happy-navratri-status-1080x1920')]:
            pg = await b.new_page(viewport={'width': W, 'height': H}); fn = os.path.join(out, name + '.html'); open(fn, 'w').write(page(W, H))
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=os.path.join(out, name + '.png'))
        await b.close()
asyncio.run(main(sys.argv[1]))
