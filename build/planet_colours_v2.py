# Planet colours, second pass (founder, 1 Oct 2026): "colours which decorate the profile elegantly; red need
# not be blood red, black need not be deep black". The tradition's colour is suggested, not stated: nine soft,
# desaturated tones of similar quietness that sit well beside ivory and sand. Text is ivory or ink, whichever
# reads better on the ground (contrast printed when run).
# Writes out/colours2-sheet.png, out/colours2-<planet>.png and out/colours2-grid.png.
import os, asyncio, math
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
POSTS = os.path.join(os.path.dirname(HERE), 'posts')
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
IV, INK, SAF, SAF2 = '#F3EDE2', '#211B12', '#D77B09', '#A8590A'

# key, name, Sanskrit, tradition, tone name, ground, text, accent
P = [
    ('sun', 'Sun', 'Surya', 'copper red', 'terracotta', '#B4674C', IV, '#FBE3C4'),
    ('moon', 'Moon', 'Chandra', 'white', 'moonstone', '#DEDDD8', INK, SAF2),
    ('mars', 'Mars', 'Mangal', 'red', 'red earth', '#9C5048', IV, '#F7CFA0'),
    ('mercury', 'Mercury', 'Budh', 'green', 'durva sage', '#8E9C7C', INK, '#3E4A2E'),
    ('jupiter', 'Jupiter', 'Guru', 'yellow', 'haldi', '#D7AD5B', INK, '#5A3A08'),
    ('venus', 'Venus', 'Shukra', 'white', 'rose cream', '#EBD9CF', INK, SAF2),
    ('saturn', 'Saturn', 'Shani', 'black', 'slate', '#4E4D52', IV, '#E9A85A'),
    ('rahu', 'Rahu', 'Rahu', 'blue', 'dusk indigo', '#4B5675', IV, '#F0B061'),
    ('ketu', 'Ketu', 'Ketu', 'smoke', 'smoke', '#8A847E', IV, '#FBE0B8'),
]
FONTS = f"""
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900;}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700;}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900;}}
*{{margin:0;padding:0;box-sizing:border-box}}"""

def lum(h):
    c = [int(h[i:i+2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + .05) / (lb + .05)

def sheet():
    cells = ''
    for k, n, s, t, tone, g, tx, ac in P:
        cells += (f'<div style="background:{g};color:{tx};border-radius:22px;padding:30px 32px 28px;height:300px;display:flex;flex-direction:column;justify-content:flex-end">'
                  f'<div style="font:600 17px IN;letter-spacing:4px;color:{ac};text-transform:uppercase">{s} · {t}</div>'
                  f'<div style="font:700 54px/1.05 PF;margin-top:8px">{n}</div>'
                  f'<div style="font:italic 400 26px LO;margin-top:8px;opacity:.85">{tone}</div></div>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
html,body{{width:1080px;background:{IV};color:{INK}}}</style></head><body><div style="padding:80px 70px 70px">
<div style="font:600 22px IN;letter-spacing:5px;color:{SAF2}">THE PLANET SERIES · THE NINE COLOURS, SOFTENED</div>
<div style="font:700 64px/1.08 PF;margin:18px 0 44px">The tradition&#8217;s colour, <em style="color:{SAF2}">suggested</em>.</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px">{cells}</div>
<div style="font:400 26px/1.5 LO;color:#6B5B4B;margin-top:40px">Nine quiet tones of the same strength, made to sit beside the ivory and sand posts.</div>
</div></body></html>"""

def ring_text(cx, cy, R, fs, color, op):
    pid = f'r{int(cx)}{int(cy)}'
    return (f'<defs><path id="{pid}" d="M{cx-R},{cy} a{R},{R} 0 1,1 {2*R},0 a{R},{R} 0 1,1 {-2*R},0"/></defs>'
            f'<text font-family="IN" font-weight="600" font-size="{fs:.1f}" fill="{color}" fill-opacity="{op}">'
            f'<textPath href="#{pid}" textLength="{2*math.pi*R-2:.1f}" lengthAdjust="spacing">{"ASTRORIVER.COM · "*4}</textPath></text>')

def shade(h, f):
    c = [int(h[i:i+2], 16) for i in (1, 3, 5)]
    return '#' + ''.join(f'{max(0, min(255, int(x * f))):02X}' for x in c)

def cover(p, eyebrow, head, sub):
    k, n, s, t, tone, g, tx, ac = p
    cx, cy, r = 800, 290, 124
    disc = shade(g, .9)
    if k == 'rahu':   off = (-0.16, -0.10)
    elif k == 'ketu': off = (0.16, 0.10)
    else:             off = None
    art = (f'<defs><radialGradient id="g" cx="50%" cy="50%" r="50%"><stop offset="55%" stop-color="{ac}" stop-opacity=".40"/>'
           f'<stop offset="100%" stop-color="{ac}" stop-opacity="0"/></radialGradient></defs>'
           f'<circle cx="{cx}" cy="{cy}" r="{r*1.75}" fill="url(#g)" opacity=".45"/>')
    if off:
        art += (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ac}"/>'
                f'<circle cx="{cx + r*off[0]}" cy="{cy + r*off[1]}" r="{r*0.985}" fill="{disc}"/>')
    else:
        art += f'<circle cx="{cx}" cy="{cy}" r="{r*0.62}" fill="{ac}" fill-opacity=".9"/>'
    art += (f'<circle cx="{cx}" cy="{cy}" r="{r*1.28}" fill="none" stroke="{ac}" stroke-opacity=".45" stroke-width="1.5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*1.55}" fill="none" stroke="{ac}" stroke-opacity=".25" stroke-width="1.5"/>'
            + ring_text(cx, cy, r*1.415, 14.3, ac, .7))
    a, b, mid = 1212, 1178, 1179
    river = (f'<path d="M100,{a+16} C300,{a+30} 360,{mid+20} 540,{mid+20} C720,{mid+20} 820,{b+16} 1080,{b+16}" fill="none" stroke="{shade(g, 1.12)}" stroke-width="3"/>'
             f'<path d="M100,{a} C300,{a+14} 360,{mid} 540,{mid} C720,{mid} 820,{b} 1080,{b}" fill="none" stroke="{SAF}" stroke-width="4.5" stroke-linecap="round"/>'
             f'<circle cx="100" cy="{a}" r="9" fill="{SAF}"/>')
    light = lum(g) > .35
    mute = '#5C5248' if light else shade(IV, .88)
    bg = f'radial-gradient(ellipse 800px 520px at 820px 280px, {shade(g, 1.06)}, {g} 70%), {g}'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
html,body{{width:1080px;height:1350px;overflow:hidden}}
.s{{position:relative;width:1080px;height:1350px;background:{bg};color:{tx};font-family:'LO',serif;overflow:hidden}}
.tr{{position:absolute;right:102px;top:58px;font:500 21px 'IN';letter-spacing:2.5px;color:{mute}}}
.wm{{position:absolute;left:70px;top:560px;font:italic 400 176px 'PF';color:{tx};opacity:{'.05' if light else '.07'};transform:rotate(-13deg);transform-origin:left top;white-space:nowrap}}
.flow{{position:absolute;left:100px;right:100px;top:510px;bottom:220px;display:flex;flex-direction:column}}
.eb{{font:600 22px 'IN';letter-spacing:5px;color:{ac};text-transform:uppercase}}
h1{{font:700 98px/1.06 'PF';letter-spacing:-.5px;margin-top:24px}}
em{{font-style:italic;color:{ac};font-weight:600}}
.b{{font:400 38px/1.5 'LO';margin-top:34px}}
.foot{{position:absolute;left:100px;right:102px;bottom:56px;display:flex;justify-content:space-between;align-items:baseline}}
.foot .n{{font:italic 500 36px 'PF'}} .foot .u{{font:500 23px 'IN';letter-spacing:2.5px;color:{mute}}}
svg{{position:absolute;left:0;top:0}}
.tag{{position:absolute;left:640px;top:1150px;font:600 17px 'IN';letter-spacing:2.5px;color:{ac};background:{g};padding:0 10px}}
</style></head><body><div class="s">
<div class="wm">astroriver.com</div><div class="tr">astroriver.com</div>
<svg width="1080" height="1350">{art}</svg>
<div class="flow"><div class="eb">{eyebrow}</div><h1>{head}</h1><div class="b">{sub}</div>
<div style="font:400 29px LO;color:{ac};margin-top:22px">Swipe &#8594;</div></div>
<svg width="1080" height="1350">{river}</svg>
<div class="tag">astroriver.com</div>
<div class="foot"><span class="n">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

KETU = ('The planet series · Ketu', 'Why does the one beside you feel so <em>far&nbsp;away</em>?', 'Sometimes it is distance. Sometimes it&nbsp;is&nbsp;Ketu.')
SAMPLE = 'Sample heading for the mock-up only'

def grid(tiles, label):
    cells = ''.join(f'<img src="file://{t}" style="width:360px;height:450px;object-fit:cover;display:block">' for t in tiles)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{background:#fff;width:1092px}} .g{{display:grid;grid-template-columns:repeat(3,360px);gap:6px}}</style></head>
<body><div style="font:600 26px IN;padding:18px 8px;color:{INK}">{label}</div><div class="g">{cells}</div></body></html>"""

async def main():
    out = os.path.join(HERE, 'out')
    for k, n, *_rest in P:
        g, tx = _rest[3], _rest[4]
        print(f'{n:8s} ground {g}  text {tx}  contrast {contrast(g, tx):.1f}:1')
    by = {p[0]: p for p in P}
    jobs = [('colours2-sheet', sheet()),
            ('colours2-ketu', cover(by['ketu'], *KETU)),
            ('colours2-rahu', cover(by['rahu'], 'The planet series · Rahu', 'A sample Rahu <em>cover</em>.', SAMPLE)),
            ('colours2-jupiter', cover(by['jupiter'], 'The planet series · Jupiter', 'A sample Jupiter <em>cover</em>.', SAMPLE)),
            ('colours2-saturn', cover(by['saturn'], 'The planet series · Saturn', 'A sample Saturn <em>cover</em>.', SAMPLE))]
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        for name, html in jobs:
            fn = os.path.join(HERE, name + '.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=os.path.join(out, name + '.png'), full_page=True)
        # a future grid: a planet tile every third post, between ivory and sand posts (mock-up)
        po = lambda r: os.path.join(POSTS, r)
        tiles = [os.path.join(out, 'colours2-ketu.png'), po('2026-10-01-shashthi/post-1080x1350.png'), po('2026-09-30-money-houses/slide-1-of-5.png'),
                 po('2026-09-27-mars-pushya/post-1080x1350.png'), os.path.join(out, 'colours2-jupiter.png'), po('2026-09-30-chaturthi-panchami/post-1080x1350.png'),
                 po('2026-09-28-sade-sati/slide-1-of-5.png'), po('2026-09-28-maha-bharani/post-1080x1350.png'), os.path.join(out, 'colours2-rahu.png')]
        gp = await b.new_page(viewport={'width': 1092, 'height': 1440})
        fn = os.path.join(HERE, 'colours2-grid.html'); open(fn, 'w').write(grid(tiles, 'Mock-up: a planet tile every third post (Ketu, Jupiter, Rahu)'))
        await gp.goto('file://' + fn); await gp.evaluate('document.fonts.ready'); await gp.wait_for_timeout(500)
        await gp.screenshot(path=os.path.join(out, 'colours2-grid.png'), full_page=True)
        await b.close()
asyncio.run(main())
