# "Happy Navratri from Astro River" greeting, v2 (founder 11 Oct: "I don't like this dark post. Use our crest... brand it properly").
# Bright and festive: cream-to-saffron light, marigold toran, rangoli corners, a row of diyas, and the gold AR crest
# (the founder's crest, purple glow removed on 9 Oct) as the centre of the card, with the institute's name under it.
import os, sys, math, random, base64, asyncio
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
CREST = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(HERE, 'out/navratri/crest-gold-900.png'), 'rb').read()).decode()
def diya(cx, cy, s):
    return (f'<circle cx="{cx}" cy="{cy-60*s}" r="{80*s}" fill="url(#flameglow)"/>'
            f'<path d="M{cx-70*s},{cy-12*s} Q{cx},{cy+52*s} {cx+70*s},{cy-12*s} Q{cx+40*s},{cy-4*s} {cx},{cy-6*s} Q{cx-40*s},{cy-4*s} {cx-70*s},{cy-12*s} Z" fill="#C2521F"/>'
            f'<path d="M{cx-70*s},{cy-12*s} Q{cx},{cy+52*s} {cx+70*s},{cy-12*s}" fill="none" stroke="#E9A23B" stroke-width="{3*s}"/>'
            f'<ellipse cx="{cx}" cy="{cy-10*s}" rx="{58*s}" ry="{8*s}" fill="#7A2A10"/>'
            f'<path d="M{cx},{cy-82*s} C{cx+18*s},{cy-52*s} {cx+14*s},{cy-24*s} {cx},{cy-16*s} C{cx-14*s},{cy-24*s} {cx-18*s},{cy-52*s} {cx},{cy-82*s} Z" fill="#FF9F1C"/>'
            f'<path d="M{cx},{cy-62*s} C{cx+8*s},{cy-44*s} {cx+7*s},{cy-28*s} {cx},{cy-22*s} C{cx-7*s},{cy-28*s} {cx-8*s},{cy-44*s} {cx},{cy-62*s} Z" fill="#FFF0B8"/>')
def toran(W):
    out = ''
    for i in range(25):
        x = 10 + i * (W - 20) / 24; y = 30 + 26 * math.sin(math.pi * (i % 6) / 5)
        out += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="22" fill="{["#F7A11A","#FFC23D","#E8780B"][i%3]}"/><circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="#C9520A" opacity=".5"/>'
        if i % 3 == 1:
            out += f'<path d="M{x:.0f},{y+18:.0f} C{x+18:.0f},{y+50:.0f} {x+10:.0f},{y+92:.0f} {x:.0f},{y+112:.0f} C{x-10:.0f},{y+92:.0f} {x-18:.0f},{y+50:.0f} {x:.0f},{y+18:.0f} Z" fill="#3E7A2C"/>'
    return out
def rangoli(cx, cy, R, rot=0):
    out = ''
    for k, (n, r, w, c) in enumerate([(12, R, R*.34, '#E8572A'), (12, R*.66, R*.26, '#F2A21C'), (8, R*.36, R*.2, '#B8235A')]):
        for i in range(n):
            a = 2 * math.pi * i / n + math.radians(rot) + (math.pi / n if k == 1 else 0)
            x, y = cx + r * .55 * math.cos(a), cy + r * .55 * math.sin(a)
            out += f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{r*.45:.1f}" ry="{w/2:.1f}" fill="{c}" opacity=".85" transform="rotate({math.degrees(a):.1f} {x:.1f} {y:.1f})"/>'
    return out + f'<circle cx="{cx}" cy="{cy}" r="{R*.14}" fill="#F7C548"/>'
def page(W, H):
    tall = H > 1500
    cw = 720 if tall else 520; ctop = 230 if tall else 150
    cy_text = ctop + cw * 0.85 + (70 if tall else 34)
    row_y = H - (340 if tall else 140)
    svg = (f'<svg width="{W}" height="{H}" style="position:absolute;left:0;top:0"><defs>'
           f'<radialGradient id="bg" cx=".5" cy=".32" r=".9"><stop offset="0" stop-color="#FFF8EA"/><stop offset=".45" stop-color="#FCE7C4"/><stop offset="1" stop-color="#F4B860"/></radialGradient>'
           f'<radialGradient id="flameglow"><stop offset="0" stop-color="#FFD27A" stop-opacity=".8"/><stop offset="1" stop-color="#FFB238" stop-opacity="0"/></radialGradient>'
           f'<radialGradient id="sun"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/><stop offset=".55" stop-color="#FFF1CF" stop-opacity=".6"/><stop offset="1" stop-color="#FFE3A8" stop-opacity="0"/></radialGradient></defs>'
           f'<rect width="{W}" height="{H}" fill="url(#bg)"/>'
           f'<circle cx="{W/2}" cy="{ctop+cw*.42}" r="{cw*.72}" fill="url(#sun)"/>'
           f'{rangoli(0, H, 260)}{rangoli(W, H, 260, 15)}'
           f'{toran(W)}'
           + ''.join(diya(W/2 + (i - 2) * 150, row_y, .62) for i in range(5)) +
           f'<rect x="24" y="24" width="{W-48}" height="{H-48}" rx="20" fill="none" stroke="#B8862E" stroke-width="2.5" opacity=".7"/>'
           f'<rect x="38" y="38" width="{W-76}" height="{H-76}" rx="14" fill="none" stroke="#B8862E" stroke-width="1" opacity=".45"/></svg>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'PFR';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-style:italic;font-weight:400 900}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}} body{{width:{W}px;height:{H}px;overflow:hidden;background:#FCE7C4}}
.crest{{position:absolute;left:{(W-cw)/2}px;top:{ctop}px;width:{cw}px;filter:drop-shadow(0 10px 18px rgba(120,60,10,.35))}}
.c{{position:absolute;left:60px;right:60px;text-align:center}}
.inst{{top:{cy_text}px;font:700 {46 if tall else 40}px 'PFR';letter-spacing:{8 if tall else 7}px;color:#7A2A10}}
.sub{{top:{cy_text+(62 if tall else 54)}px;font:600 {22 if tall else 20}px 'IN';letter-spacing:5px;color:#A8590A}}
.hi{{top:{cy_text+(150 if tall else 112)}px;font:700 {104 if tall else 86}px/1.25 'NSR';color:#B3261E;text-shadow:0 2px 0 rgba(255,255,255,.5)}}
.en{{top:{cy_text+(290 if tall else 228)}px;font:italic 700 {60 if tall else 50}px 'PF';color:#8A3A12}}
.wish{{top:{cy_text+(380 if tall else 304)}px;font:italic 500 {33 if tall else 28}px/1.45 'PF';color:#5A3418;left:{60 if tall else 110}px;right:{60 if tall else 110}px}}
.url{{top:{H-(150 if tall else 74)}px;font:700 {26 if tall else 22}px 'IN';letter-spacing:4px;color:#7A2A10}}
</style></head><body>{svg}
<img class="crest" src="{CREST}">
<div class="c inst">ASTRO RIVER INSTITUTE</div><div class="c sub">EST. 2008 · JALANDHAR, INDIA</div>
<div class="c hi">शुभ नवरात्रि</div><div class="c en">Happy Navratri</div>
<div class="c wish">May Maa Durga bless your home with strength, peace and joy.</div>
<div class="c url">astroriver.com</div></body></html>"""
async def main(out):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for W, H, name in [(1080, 1350, 'happy-navratri-v2-share-1080x1350'), (1080, 1920, 'happy-navratri-v2-status-1080x1920')]:
            pg = await b.new_page(viewport={'width': W, 'height': H}); fn = os.path.join(out, name + '.html'); open(fn, 'w').write(page(W, H))
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=os.path.join(out, name + '.png'))
        await b.close()
if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
