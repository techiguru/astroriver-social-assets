# Planet colours, third pass (founder, 1 Oct 2026): the haldi read dull, so Jupiter gets three cleaner golds to
# choose from. Draws (1) the colour sheet, (2) nine sample covers, one per planet, and (3) the three Jupiter
# golds as covers. Headings on the sample covers name each planet's best-known signification and are for the
# colour test only; they are not posts.
import os, asyncio
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'planet_colours_v2.py')).read().split('async def main():')[0]
v2 = {'__file__': os.path.join(HERE, 'planet_colours_v2.py')}; exec(src, v2)
cover, FONTS, IV, INK, SAF2, contrast = v2['cover'], v2['FONTS'], v2['IV'], v2['INK'], v2['SAF2'], v2['contrast']
out = os.path.join(HERE, 'out')

GOLDS = [('jupiter', 'Jupiter', 'Guru', 'yellow', 'marigold gold', '#E2A93E', INK, '#5A3A08'),
         ('jupiter', 'Jupiter', 'Guru', 'yellow', 'pitambar yellow', '#EBC458', INK, '#6A4508'),
         ('jupiter', 'Jupiter', 'Guru', 'yellow', 'champagne gold', '#E6CC8A', INK, '#7A5210')]
P = [p for p in v2['P']]
P[4] = GOLDS[1]   # pitambar yellow as the working choice
HEAD = {'sun': ('Surya, the <em>soul</em>.', 'The Sun stands for the self, the father and authority.'),
        'moon': ('Chandra, the <em>mind</em>.', 'The Moon stands for the mind, the mother and feeling.'),
        'mars': ('Mangal, the <em>courage</em>.', 'Mars stands for courage, land and brothers.'),
        'mercury': ('Budh, the <em>speech</em>.', 'Mercury stands for speech, trade and learning.'),
        'jupiter': ('Guru, the <em>teacher</em>.', 'Jupiter stands for wisdom, children and good fortune.'),
        'venus': ('Shukra, the <em>beloved</em>.', 'Venus stands for love, beauty and comfort.'),
        'saturn': ('Shani, the <em>time</em>.', 'Saturn stands for time, work and patience.'),
        'rahu': ('Rahu, the <em>hunger</em>.', 'Rahu is desire that never feels full.'),
        'ketu': ('Ketu, the <em>letting&nbsp;go</em>.', 'Ketu is the past already lived.')}

def board(imgs, title, cols=3, labels=None):
    cells = ''
    for i, im in enumerate(imgs):
        lab = f'<div style="font:600 20px IN;color:{INK};padding:10px 2px 0">{labels[i]}</div>' if labels else ''
        cells += f'<div><img src="file://{im}" style="width:340px;height:425px;display:block;border-radius:6px">{lab}</div>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{background:{IV};width:{cols*340+(cols-1)*24+120}px}}</style></head><body><div style="padding:56px 60px">
<div style="font:600 20px IN;letter-spacing:5px;color:{SAF2}">THE PLANET SERIES</div>
<div style="font:700 52px/1.1 PF;color:{INK};margin:12px 0 34px">{title}</div>
<div style="display:grid;grid-template-columns:repeat({cols},340px);gap:30px 24px">{cells}</div></div></body></html>"""

def sheet(planets, title):
    cells = ''
    for k, n, s, t, tone, g, tx, ac in planets:
        cells += (f'<div><div style="background:{g};border-radius:20px;height:190px"></div>'
                  f'<div style="font:700 34px PF;color:{INK};margin-top:14px">{n} <span style="font:italic 400 26px LO;color:#6B5B4B">· {s}</span></div>'
                  f'<div style="font:400 24px LO;color:#6B5B4B;margin-top:2px">{tone} <span style="font:500 18px IN;letter-spacing:1px;color:#9A8B78">{g}</span></div></div>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{background:{IV};width:1080px}}</style></head><body><div style="padding:70px 70px 60px">
<div style="font:600 20px IN;letter-spacing:5px;color:{SAF2}">THE PLANET SERIES · THE NINE COLOURS</div>
<div style="font:700 56px/1.1 PF;color:{INK};margin:14px 0 40px">{title}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:34px 24px">{cells}</div></div></body></html>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        async def shot(name, html, w=1080, h=1350, full=False):
            await pg.set_viewport_size({'width': w, 'height': h})
            fn = os.path.join(HERE, name + '.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=os.path.join(out, name + '.png'), full_page=full)
        imgs = []
        for pl in P:
            h, sub = HEAD[pl[0]]
            name = f'colours3-cover-{pl[1].lower()}'
            await shot(name, cover(pl, f'The planet series · {pl[1]}', h, sub))
            imgs.append(os.path.join(out, name + '.png'))
            print(f'{pl[1]:8s} {pl[5]}  text contrast {contrast(pl[5], pl[6]):.1f}:1')
        gimgs = []
        for i, gl in enumerate(GOLDS):
            name = f'colours3-gold-{i+1}'
            await shot(name, cover(gl, 'The planet series · Jupiter', *HEAD['jupiter']))
            gimgs.append(os.path.join(out, name + '.png'))
        await shot('colours3-sheet', sheet(P, 'Each planet in its own colour.'), 1080, 1000, True)
        await shot('colours3-covers', board(imgs, 'Nine sample covers, one per planet.', 3, [f'{x[1]} · {x[4]}' for x in P]), 1260, 1500, True)
        await shot('colours3-golds', board(gimgs, 'Three golds for Jupiter.', 3, [f'{g[4]} {g[5]}' for g in GOLDS]), 1260, 700, True)
        await b.close()
asyncio.run(main())
