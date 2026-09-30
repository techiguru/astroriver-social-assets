# Planet series: three light looks for the founder to choose from (1 Oct 2026). The 29 Sep Rahu post
# stays as it is; the dark ground is retired for the series from the Ketu post on. Same fonts, ink,
# saffron and river line as every other series; the series is told apart by one signature each:
#   A "Dawn glow"  - ivory warming to a pale saffron glow at the top, where the eclipse sits.
#   B "Frame"      - flat ivory inside a fine saffron double frame; the eclipse large and centred.
#   C "Window"     - ivory, with one rounded ink window at the top that holds the eclipse.
# Cover copy is the approved Ketu cover. Writes out/looks-*.png and out/looks-grid.png.
import os, asyncio, math
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
POSTS = os.path.join(os.path.dirname(HERE), 'posts')
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
IV, INK, SAF, SAF2, MUT, LINE = '#F3EDE2', '#211B12', '#D77B09', '#A8590A', '#6B5B4B', '#E2D7C4'
W, H = 1080, 1350

CSS = f"""
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900;}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700;}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900;}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
.s{{position:relative;width:{W}px;height:{H}px;color:{INK};font-family:'LO',serif;overflow:hidden}}
.tr{{position:absolute;right:102px;top:58px;font:500 21px 'IN';letter-spacing:2.5px;color:{MUT}}}
.wm{{position:absolute;left:70px;top:560px;font:italic 400 176px 'PF';color:{INK};opacity:.045;transform:rotate(-13deg);transform-origin:left top;white-space:nowrap}}
.flow{{position:absolute;left:100px;right:100px;top:510px;bottom:220px;display:flex;flex-direction:column}}
.eb{{font:600 22px 'IN';letter-spacing:5px;color:{SAF2};text-transform:uppercase}}
h1{{font:700 98px/1.06 'PF';letter-spacing:-.5px;margin-top:24px}}
em{{font-style:italic;color:{SAF2};font-weight:600}}
.b{{font:400 38px/1.5 'LO';margin-top:34px}}
.sw{{font:400 29px 'LO';color:{SAF2};margin-top:22px}}
.foot{{position:absolute;left:100px;right:102px;bottom:56px;display:flex;justify-content:space-between;align-items:baseline}}
.foot .n{{font:italic 500 36px 'PF'}} .foot .u{{font:500 23px 'IN';letter-spacing:2.5px;color:{MUT}}}
svg.r{{position:absolute;left:0;top:0}}
.tag{{position:absolute;left:640px;top:1150px;font:600 17px 'IN';letter-spacing:2.5px;color:{SAF2};padding:0 10px}}
"""

def ring_text(cx, cy, R, fs, color, op):
    pid = f'ring{int(cx)}{int(cy)}{int(R)}'
    return (f'<defs><path id="{pid}" d="M{cx-R},{cy} a{R},{R} 0 1,1 {2*R},0 a{R},{R} 0 1,1 {-2*R},0"/></defs>'
            f'<text font-family="IN" font-weight="600" font-size="{fs:.1f}" fill="{color}" fill-opacity="{op}">'
            f'<textPath href="#{pid}" textLength="{2*math.pi*R-2:.1f}" lengthAdjust="spacing">{"ASTRORIVER.COM · "*4}</textPath></text>')

def eclipse(cx, cy, r, cover, ring_col, ring_op=.55):
    # Ketu: the saffron Sun with the shadow moving off to the lower right; bright edge upper left
    return (f'<defs><radialGradient id="g{int(cx)}" cx="50%" cy="50%" r="50%"><stop offset="55%" stop-color="{SAF}" stop-opacity=".45"/>'
            f'<stop offset="100%" stop-color="{SAF}" stop-opacity="0"/></radialGradient></defs>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*1.75}" fill="url(#g{int(cx)})" opacity=".5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SAF}"/>'
            f'<circle cx="{cx + r*0.16}" cy="{cy + r*0.10}" r="{r*0.985}" fill="{cover}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*1.28}" fill="none" stroke="{SAF}" stroke-opacity=".40" stroke-width="1.5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*1.55}" fill="none" stroke="{SAF}" stroke-opacity=".22" stroke-width="1.5"/>'
            + ring_text(cx, cy, r*1.415, max(13, r*0.115), ring_col, ring_op))

def river(ground):
    a, b, mid = 1212, 1178, 1179
    p = f"M100,{a} C300,{a+14} 360,{mid} 540,{mid} C720,{mid} 820,{b} 1080,{b}"
    q = f"M100,{a+16} C300,{a+30} 360,{mid+20} 540,{mid+20} C720,{mid+20} 820,{b+16} 1080,{b+16}"
    return (f'<path d="{q}" fill="none" stroke="{LINE}" stroke-width="3"/>'
            f'<path d="{p}" fill="none" stroke="{SAF}" stroke-width="4.5" stroke-linecap="round"/><circle cx="100" cy="{a}" r="9" fill="{SAF}"/>')

TEXT = """<div class="flow"><div class="eb">The planet series · Ketu</div>
<h1>Why does the one beside you feel so <em>far&nbsp;away</em>?</h1>
<div class="b">Sometimes it is distance. Sometimes it&nbsp;is&nbsp;Ketu.</div><div class="sw">Swipe &#8594;</div></div>"""

def page(bg_css, under_svg, art_svg, text=TEXT, tag_bg=IV, extra=''):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{extra}</style></head><body>
<div class="s" style="background:{bg_css}">
<svg class="r" width="{W}" height="{H}">{under_svg}</svg>
<div class="wm">astroriver.com</div><div class="tr">astroriver.com</div>
<svg class="r" width="{W}" height="{H}">{art_svg}</svg>
{text}
<svg class="r" width="{W}" height="{H}">{river(IV)}</svg>
<div class="tag" style="background:{tag_bg}">astroriver.com</div>
<div class="foot"><span class="n">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

# A: Dawn glow - ivory with a pale saffron glow rising behind the eclipse
GLOW = '#F1D3A6'
A = page(f'radial-gradient(ellipse 900px 700px at 800px 250px, {GLOW} 0%, #F2DDBE 38%, {IV} 78%), {IV}',
         '', eclipse(800, 290, 124, '#F2DCBD', SAF2, .6))

# B: Frame - flat ivory, a fine saffron double frame, the eclipse centred and large
FRAME = (f'<rect x="36" y="36" width="{W-72}" height="{H-72}" rx="6" fill="none" stroke="{SAF}" stroke-width="2.5"/>'
         f'<rect x="50" y="50" width="{W-100}" height="{H-100}" rx="4" fill="none" stroke="{SAF}" stroke-opacity=".45" stroke-width="1.2"/>')
B = page(IV, FRAME, eclipse(540, 290, 128, IV, SAF2, .6), extra='.tr{top:78px}')

# C: Window - ivory, one rounded ink window at the top right holding the eclipse
WIN = f'<rect x="560" y="40" width="480" height="440" rx="44" fill="{INK}"/>'
C = page(IV, WIN, eclipse(800, 262, 112, INK, SAF, .55), extra='.tr{left:100px;right:auto}')

def grid(tiles, label):
    cells = ''.join(f'<img src="file://{t}" style="width:360px;height:450px;object-fit:cover;display:block">' for t in tiles)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900;}}
body{{margin:0;background:#fff;width:1092px}} .g{{display:grid;grid-template-columns:repeat(3,360px);gap:6px}}
.l{{font:600 26px 'IN';padding:18px 8px;color:#211B12}}</style></head><body><div class="l">{label}</div><div class="g">{cells}</div></body></html>"""

async def main():
    out = os.path.join(HERE, 'out')
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': W, 'height': H})
        for k, html in (('a-glow', A), ('b-frame', B), ('c-window', C)):
            fn = os.path.join(HERE, f'looks-{k}.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=os.path.join(out, f'looks-{k}.png'))
        # the grid as it will read on 1 Oct evening, newest first
        rest = ['2026-10-01-shashthi/post-1080x1350.png', '2026-09-30-money-houses/slide-1-of-5.png',
                '2026-09-30-chaturthi-panchami/post-1080x1350.png', '2026-09-29-rahu-wrong-person/slide-1-of-5.png',
                '2026-09-29-maha-bharani-hi/post-1080x1350.png', '2026-09-28-sade-sati/slide-1-of-5.png',
                '2026-09-28-maha-bharani/post-1080x1350.png', '2026-09-27-mars-pushya/post-1080x1350.png']
        rest = [os.path.join(POSTS, r) for r in rest]
        gp = await b.new_page(viewport={'width': 1092, 'height': 1440})
        for k, name in (('a-glow', 'A · Dawn glow'), ('b-frame', 'B · Frame'), ('c-window', 'C · Window')):
            fn = os.path.join(HERE, f'looks-grid-{k}.html')
            open(fn, 'w').write(grid([os.path.join(out, f'looks-{k}.png')] + rest, name))
            await gp.goto('file://' + fn); await gp.evaluate('document.fonts.ready'); await gp.wait_for_timeout(500)
            await gp.screenshot(path=os.path.join(out, f'looks-grid-{k}.png'), full_page=True)
        await b.close()
asyncio.run(main())
