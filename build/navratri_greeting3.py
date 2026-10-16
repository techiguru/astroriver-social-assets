# "Happy Navratri from Astro River" greeting, v3 (founder 11 Oct: brand it properly, "but that does not mean you take it
# away from Navratri"). Navratri leads: the greeting and a Ghatasthapana kalash (brass pot, mango leaves, coconut in red
# cloth, marigolds) with diyas. Our crest and name sign it at the bottom.
import os, sys, math, base64, asyncio
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
sys.path.insert(0, HERE); import navratri_greeting2 as G
CREST = G.CREST
def kalash(cx, by, s):
    """brass kalash standing on a base, mango leaves fanned at the mouth, a coconut wrapped in red cloth with a gold band"""
    o = ''
    o += f'<ellipse cx="{cx}" cy="{by+6*s}" rx="{190*s}" ry="{26*s}" fill="#B5532A" opacity=".25"/>'
    # mango leaves behind the coconut
    for ang in (-62, -40, -18, 18, 40, 62, -80, 80):
        L = 190 * s if abs(ang) < 70 else 150 * s
        o += (f'<g transform="rotate({ang} {cx} {by-330*s})"><path d="M{cx},{by-330*s} C{cx+34*s},{by-330*s-L*.35} {cx+26*s},{by-330*s-L*.8} {cx},{by-330*s-L} '
              f'C{cx-26*s},{by-330*s-L*.8} {cx-34*s},{by-330*s-L*.35} {cx},{by-330*s} Z" fill="{"#2F6B2A" if ang % 2 == 0 else "#3E8A34"}"/>'
              f'<path d="M{cx},{by-336*s} L{cx},{by-330*s-L*.95}" stroke="#7FB65A" stroke-width="{2.5*s}"/></g>')
    # coconut in red cloth
    o += (f'<ellipse cx="{cx}" cy="{by-400*s}" rx="{78*s}" ry="{96*s}" fill="#C4202B"/>'
          f'<path d="M{cx-78*s},{by-400*s} Q{cx},{by-360*s} {cx+78*s},{by-400*s}" fill="none" stroke="#F2B544" stroke-width="{9*s}"/>'
          f'<path d="M{cx-30*s},{by-490*s} C{cx-10*s},{by-470*s} {cx+10*s},{by-470*s} {cx+30*s},{by-490*s} L{cx+18*s},{by-505*s} C{cx+5*s},{by-495*s} {cx-5*s},{by-495*s} {cx-18*s},{by-505*s} Z" fill="#7A4A1E"/>'
          f'<ellipse cx="{cx-26*s}" cy="{by-430*s}" rx="{14*s}" ry="{34*s}" fill="#FFFFFF" opacity=".18"/>')
    # pot
    o += (f'<path d="M{cx-92*s},{by-330*s} L{cx+92*s},{by-330*s} L{cx+72*s},{by-296*s} C{cx+200*s},{by-250*s} {cx+215*s},{by-90*s} {cx+120*s},{by-28*s} '
          f'L{cx+80*s},{by} L{cx-80*s},{by} L{cx-120*s},{by-28*s} C{cx-215*s},{by-90*s} {cx-200*s},{by-250*s} {cx-72*s},{by-296*s} Z" fill="url(#brass)"/>'
          f'<rect x="{cx-100*s}" y="{by-344*s}" width="{200*s}" height="{22*s}" rx="{10*s}" fill="#D9A441"/>'
          f'<path d="M{cx-178*s},{by-170*s} Q{cx},{by-120*s} {cx+178*s},{by-170*s}" fill="none" stroke="#C4202B" stroke-width="{10*s}"/>'
          f'<path d="M{cx-150*s},{by-230*s} Q{cx},{by-200*s} {cx+150*s},{by-230*s}" fill="none" stroke="#F2B544" stroke-width="{4*s}"/>'
          f'<ellipse cx="{cx-70*s}" cy="{by-170*s}" rx="{26*s}" ry="{80*s}" fill="#FFFFFF" opacity=".22"/>')
    # marigold string round the neck
    for i in range(11):
        t = i / 10; x = cx - 92 * s + 184 * s * t; y = by - 300 * s + 26 * s * math.sin(math.pi * t)
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{13*s:.1f}" fill="{["#F7A11A","#FFC23D","#E8780B"][i%3]}"/>'
    return o
def rays(cx, cy, R, n=28):
    out = ''
    for i in range(n):
        a = 2 * math.pi * i / n; a2 = a + math.pi / n * .45
        out += (f'<path d="M{cx},{cy} L{cx+R*math.cos(a):.0f},{cy+R*math.sin(a):.0f} L{cx+R*math.cos(a2):.0f},{cy+R*math.sin(a2):.0f} Z" '
                f'fill="#F7C548" opacity=".16"/>')
    return out
def petals(cx, y, s):
    import random; random.seed(5); out = ''
    for _ in range(26):
        x = cx + random.uniform(-300, 300) * s
        out += f'<circle cx="{x:.0f}" cy="{y + random.uniform(-6, 2) * s:.0f}" r="{random.uniform(7, 12) * s:.1f}" fill="{random.choice(["#F7A11A","#FFC23D","#E8780B"])}"/>'
    return out
def page(W, H):
    tall = H > 1500; s = 1.22 if tall else .78
    kb = 1330 if tall else 880           # kalash base
    svg = (f'<svg width="{W}" height="{H}" style="position:absolute;left:0;top:0"><defs>'
           f'<radialGradient id="bg" cx=".5" cy=".5" r=".9"><stop offset="0" stop-color="#FFF8EA"/><stop offset=".5" stop-color="#FCE3B8"/><stop offset="1" stop-color="#F2A94E"/></radialGradient>'
           f'<radialGradient id="flameglow"><stop offset="0" stop-color="#FFD27A" stop-opacity=".85"/><stop offset="1" stop-color="#FFB238" stop-opacity="0"/></radialGradient>'
           f'<radialGradient id="halo"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/><stop offset=".5" stop-color="#FFF1CF" stop-opacity=".55"/><stop offset="1" stop-color="#FFE3A8" stop-opacity="0"/></radialGradient>'
           f'<linearGradient id="brass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8A5A12"/><stop offset=".3" stop-color="#E8B44A"/><stop offset=".55" stop-color="#F7D27A"/><stop offset="1" stop-color="#9A6414"/></linearGradient></defs>'
           f'<rect width="{W}" height="{H}" fill="url(#bg)"/>'
           f'<circle cx="{W/2}" cy="{kb-300*s}" r="{430*s}" fill="url(#halo)"/>' + rays(W/2, kb-300*s, 520*s) + f'<path d="M{W/2-330*s},{kb+4*s} L{W/2+330*s},{kb+4*s} L{W/2+290*s},{kb+60*s} L{W/2-290*s},{kb+60*s} Z" fill="#B3261E"/>'f'<path d="M{W/2-322*s},{kb+16*s} L{W/2+322*s},{kb+16*s}" stroke="#F2B544" stroke-width="{5*s}"/><path d="M{W/2-300*s},{kb+48*s} L{W/2+300*s},{kb+48*s}" stroke="#F2B544" stroke-width="{3*s}"/>' + petals(W/2, kb+2*s, s) +
           f'{G.rangoli(0, H, 230)}{G.rangoli(W, H, 230, 15)}{G.toran(W)}'
           f'{kalash(W/2, kb, s)}{G.diya(W/2-300*s, kb, .9*s)}{G.diya(W/2+300*s, kb, .9*s)}'
           f'<rect x="24" y="24" width="{W-48}" height="{H-48}" rx="20" fill="none" stroke="#B8862E" stroke-width="2.5" opacity=".7"/>'
           f'<rect x="38" y="38" width="{W-76}" height="{H-76}" rx="14" fill="none" stroke="#B8862E" stroke-width="1" opacity=".45"/></svg>')
    cw = 230 if tall else 170
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'PFR';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-style:italic;font-weight:400 900}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}} body{{width:{W}px;height:{H}px;overflow:hidden;background:#FCE3B8}}
.c{{position:absolute;left:60px;right:60px;text-align:center}}
.hi{{top:{170 if tall else 130}px;font:700 {124 if tall else 96}px/1.25 'NSR';color:#B3261E;text-shadow:0 2px 0 rgba(255,255,255,.6)}}
.en{{top:{350 if tall else 266}px;font:italic 700 {66 if tall else 52}px 'PF';color:#8A3A12}}
.wish{{top:{kb+110 if tall else kb+66}px;font:italic 500 {34 if tall else 28}px/1.45 'PF';color:#5A3418;left:70px;right:70px}}
.sig{{position:absolute;left:0;right:0;bottom:{120 if tall else 70}px;display:flex;align-items:center;justify-content:center;gap:{28 if tall else 20}px}}
.sig img{{width:{cw}px;filter:drop-shadow(0 6px 10px rgba(120,60,10,.3))}}
.sig .t{{text-align:left}} .sig .a{{font:700 {38 if tall else 30}px 'PFR';letter-spacing:{6 if tall else 5}px;color:#7A2A10}}
.sig .b{{font:600 {20 if tall else 16}px 'IN';letter-spacing:4px;color:#A8590A;margin-top:6px}} .sig .u{{font:700 {24 if tall else 19}px 'IN';letter-spacing:3px;color:#7A2A10;margin-top:12px}}
</style></head><body>{svg}
<div class="c hi">शुभ नवरात्रि</div><div class="c en">Happy Navratri</div>
<div class="c wish">May Maa Durga bless your home with strength, peace and joy.</div>
<div class="sig"><img src="{CREST}"><div class="t"><div class="a">ASTRO RIVER INSTITUTE</div><div class="b">EST. 2008 · JALANDHAR, INDIA</div><div class="u">astroriver.com</div></div></div>
</body></html>"""
async def main(out):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for W, H, name in [(1080, 1350, 'happy-navratri-v3-share-1080x1350'), (1080, 1920, 'happy-navratri-v3-status-1080x1920')]:
            pg = await b.new_page(viewport={'width': W, 'height': H}); fn = os.path.join(out, name + '.html'); open(fn, 'w').write(page(W, H))
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=os.path.join(out, name + '.png'))
        await b.close()
if __name__ == '__main__':
    asyncio.run(main(sys.argv[1]))
