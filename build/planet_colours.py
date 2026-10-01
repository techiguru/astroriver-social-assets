# Planet series in the planets' own colours (founder's idea, 1 Oct 2026). Muted, pigment-like tones so the
# grid stays calm: Sun copper red, Moon pearl, Mars blood red, Mercury durva green, Jupiter turmeric gold,
# Venus white (warm, to tell it from the Moon), Saturn black, Rahu blue, Ketu smoke (founder: "smoke is
# Ketu, Rahu is blue, Saturn is black"). Same fonts, saffron river line, tags and footer as every series.
# Writes out/colours-sheet.png, out/colours-ketu-smoke.png and out/colours-grid-ketu-smoke.png.
import os, asyncio, math
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
POSTS = os.path.join(os.path.dirname(HERE), 'posts')
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
IV, INK, SAF, SAF2 = '#F3EDE2', '#211B12', '#D77B09', '#A8590A'

# name, Sanskrit, tradition, ground, text, accent
PLANETS = [
    ('Sun', 'Surya', 'copper red', '#8F3F26', IV, '#F0B061'),
    ('Moon', 'Chandra', 'pearl white', '#E9E6E0', INK, SAF2),
    ('Mars', 'Mangal', 'blood red', '#7A2620', IV, '#F0A050'),
    ('Mercury', 'Budh', 'durva green', '#4F6B45', IV, '#F2C46A'),
    ('Jupiter', 'Guru', 'yellow, gold', '#C8962F', INK, '#5A3A08'),
    ('Venus', 'Shukra', 'white', '#F1E6DA', INK, SAF2),
    ('Saturn', 'Shani', 'black', '#1C1B1D', IV, '#E3901F'),
    ('Rahu', 'Rahu', 'blue', '#1E2A47', IV, '#E8A040'),
    ('Ketu', 'Ketu', 'smoke', '#5E5954', IV, '#F0B061'),
]
FONTS = f"""
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900;}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700;}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900;}}
*{{margin:0;padding:0;box-sizing:border-box}}"""

def sheet():
    cells = ''
    for n, s, t, g, tx, ac in PLANETS:
        cells += (f'<div style="background:{g};color:{tx};border-radius:22px;padding:34px 34px 30px;height:300px;display:flex;flex-direction:column;justify-content:flex-end">'
                  f'<div style="font:600 18px IN;letter-spacing:4px;color:{ac};text-transform:uppercase">{s}</div>'
                  f'<div style="font:700 56px/1.05 PF;margin-top:8px">{n}</div>'
                  f'<div style="font:italic 400 27px LO;margin-top:8px;opacity:.85">{t}</div></div>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
html,body{{width:1080px;background:{IV};color:{INK}}}</style></head><body><div style="padding:80px 70px 70px">
<div style="font:600 22px IN;letter-spacing:5px;color:{SAF2}">THE PLANET SERIES · THE NINE COLOURS</div>
<div style="font:700 64px/1.08 PF;margin:18px 0 44px">Each planet in its <em style="color:{SAF2}">own</em> colour.</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px">{cells}</div>
<div style="font:400 26px/1.5 LO;color:#6B5B4B;margin-top:40px">Muted, pigment-like tones. The frame, fonts, saffron river line and footer stay the same on every one.</div>
</div></body></html>"""

def ring_text(cx, cy, R, fs, color, op):
    pid = f'r{int(cx)}{int(cy)}'
    return (f'<defs><path id="{pid}" d="M{cx-R},{cy} a{R},{R} 0 1,1 {2*R},0 a{R},{R} 0 1,1 {-2*R},0"/></defs>'
            f'<text font-family="IN" font-weight="600" font-size="{fs:.1f}" fill="{color}" fill-opacity="{op}">'
            f'<textPath href="#{pid}" textLength="{2*math.pi*R-2:.1f}" lengthAdjust="spacing">{"ASTRORIVER.COM · "*4}</textPath></text>')

def ketu_smoke():
    G, MUTE, ACC = '#5E5954', '#D9D2C8', '#F0B061'
    cx, cy, r = 800, 290, 124
    art = (f'<defs><radialGradient id="g" cx="50%" cy="50%" r="50%"><stop offset="55%" stop-color="{ACC}" stop-opacity=".45"/>'
           f'<stop offset="100%" stop-color="{ACC}" stop-opacity="0"/></radialGradient></defs>'
           f'<circle cx="{cx}" cy="{cy}" r="{r*1.75}" fill="url(#g)" opacity=".45"/>'
           f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ACC}"/>'
           f'<circle cx="{cx + r*0.16}" cy="{cy + r*0.10}" r="{r*0.985}" fill="#57524D"/>'
           f'<circle cx="{cx}" cy="{cy}" r="{r*1.28}" fill="none" stroke="{ACC}" stroke-opacity=".40" stroke-width="1.5"/>'
           f'<circle cx="{cx}" cy="{cy}" r="{r*1.55}" fill="none" stroke="{ACC}" stroke-opacity=".22" stroke-width="1.5"/>'
           + ring_text(cx, cy, r*1.415, 14.3, ACC, .6))
    a, b, mid = 1212, 1178, 1179
    river = (f'<path d="M100,{a+16} C300,{a+30} 360,{mid+20} 540,{mid+20} C720,{mid+20} 820,{b+16} 1080,{b+16}" fill="none" stroke="#77716B" stroke-width="3"/>'
             f'<path d="M100,{a} C300,{a+14} 360,{mid} 540,{mid} C720,{mid} 820,{b} 1080,{b}" fill="none" stroke="{SAF}" stroke-width="4.5" stroke-linecap="round"/>'
             f'<circle cx="100" cy="{a}" r="9" fill="{SAF}"/>')
    # smoke: soft drifting haze, lighter wisps over the warm grey ground
    haze = ('radial-gradient(ellipse 700px 380px at 820px 300px, rgba(255,250,242,.10), transparent 70%),'
            'radial-gradient(ellipse 900px 300px at 200px 820px, rgba(255,250,242,.07), transparent 70%),'
            'radial-gradient(ellipse 600px 260px at 900px 1050px, rgba(0,0,0,.10), transparent 70%),'
            f'linear-gradient(170deg, #67625C 0%, {G} 45%, #55504B 100%)')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
html,body{{width:1080px;height:1350px;overflow:hidden}}
.s{{position:relative;width:1080px;height:1350px;background:{haze};color:{IV};font-family:'LO',serif;overflow:hidden}}
.tr{{position:absolute;right:102px;top:58px;font:500 21px 'IN';letter-spacing:2.5px;color:{MUTE}}}
.wm{{position:absolute;left:70px;top:560px;font:italic 400 176px 'PF';color:{IV};opacity:.07;transform:rotate(-13deg);transform-origin:left top;white-space:nowrap}}
.flow{{position:absolute;left:100px;right:100px;top:510px;bottom:220px;display:flex;flex-direction:column}}
.eb{{font:600 22px 'IN';letter-spacing:5px;color:{ACC};text-transform:uppercase}}
h1{{font:700 98px/1.06 'PF';letter-spacing:-.5px;margin-top:24px}}
em{{font-style:italic;color:{ACC};font-weight:600}}
.b{{font:400 38px/1.5 'LO';margin-top:34px}}
.foot{{position:absolute;left:100px;right:102px;bottom:56px;display:flex;justify-content:space-between;align-items:baseline}}
.foot .n{{font:italic 500 36px 'PF'}} .foot .u{{font:500 23px 'IN';letter-spacing:2.5px;color:{MUTE}}}
svg{{position:absolute;left:0;top:0}}
.tag{{position:absolute;left:640px;top:1150px;font:600 17px 'IN';letter-spacing:2.5px;color:{ACC};background:#5A5550;padding:0 10px}}
</style></head><body><div class="s">
<div class="wm">astroriver.com</div><div class="tr">astroriver.com</div>
<svg width="1080" height="1350">{art}</svg>
<div class="flow"><div class="eb">The planet series · Ketu</div>
<h1>Why does the one beside you feel so <em>far&nbsp;away</em>?</h1>
<div class="b">Sometimes it is distance. Sometimes it&nbsp;is&nbsp;Ketu.</div>
<div style="font:400 29px LO;color:{ACC};margin-top:22px">Swipe &#8594;</div></div>
<svg width="1080" height="1350">{river}</svg>
<div class="tag">astroriver.com</div>
<div class="foot"><span class="n">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

def grid(tiles, label):
    cells = ''.join(f'<img src="file://{t}" style="width:360px;height:450px;object-fit:cover;display:block">' for t in tiles)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{background:#fff;width:1092px}} .g{{display:grid;grid-template-columns:repeat(3,360px);gap:6px}}</style></head>
<body><div style="font:600 26px IN;padding:18px 8px;color:{INK}">{label}</div><div class="g">{cells}</div></body></html>"""

async def main():
    out = os.path.join(HERE, 'out')
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html, w, h in (('colours-sheet', sheet(), 1080, 1350), ('colours-ketu-smoke', ketu_smoke(), 1080, 1350)):
            pg = await b.new_page(viewport={'width': w, 'height': h})
            fn = os.path.join(HERE, name + '.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=os.path.join(out, name + '.png'), full_page=True)
        rest = ['2026-10-01-shashthi/post-1080x1350.png', '2026-09-30-money-houses/slide-1-of-5.png',
                '2026-09-30-chaturthi-panchami/post-1080x1350.png', '2026-09-29-rahu-wrong-person/slide-1-of-5.png',
                '2026-09-29-maha-bharani-hi/post-1080x1350.png', '2026-09-28-sade-sati/slide-1-of-5.png',
                '2026-09-28-maha-bharani/post-1080x1350.png', '2026-09-27-mars-pushya/post-1080x1350.png']
        tiles = [os.path.join(out, 'colours-ketu-smoke.png')] + [os.path.join(POSTS, r) for r in rest]
        gp = await b.new_page(viewport={'width': 1092, 'height': 1440})
        fn = os.path.join(HERE, 'colours-grid.html'); open(fn, 'w').write(grid(tiles, 'Ketu in smoke, in tonight’s grid'))
        await gp.goto('file://' + fn); await gp.evaluate('document.fonts.ready'); await gp.wait_for_timeout(500)
        await gp.screenshot(path=os.path.join(out, 'colours-grid-ketu-smoke.png'), full_page=True)
        await b.close()
asyncio.run(main())
