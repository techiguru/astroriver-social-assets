# Mon 5 Oct 2026 morning: Dashami shradh, Story + WhatsApp Status only (day events are Stories, founder 4 Oct).
# Ivory Pitru Paksha dress, copied from saptami.py. Facts computed this session (Swiss Ephemeris, Lahiri) and matching
# the live article /journal/pitru-paksha-2026 table (Dashami: Mon 5 Oct in India, UK, US East, Australia; Sun 4 Oct on
# the US Pacific coast, starred, with Navami):
#   Krishna Dashami tithi: Mon 5 Oct 03:54 IST -> Tue 6 Oct 02:08 IST.
#   Delhi Mon 5 Oct aparahna 13:19-15:40 IST (article table): Dashami covers all of it.
#   Ekadashi shradh follows on Tue 6 Oct in India (article).
import os, asyncio
from playwright.async_api import async_playwright
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_shared.py')).read())
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)

EXTRA = """
.flow{position:absolute;left:100px;right:100px;display:flex;flex-direction:column;justify-content:center}
.tr2{display:grid;grid-template-columns:1.5fr 1fr;align-items:baseline;padding:24px 0;border-top:1.5px solid #DCCFBA}
.tr2.hd{border-top:0;padding:0 0 14px}
.tr2.hd span{font:600 19px 'IN';letter-spacing:2.5px;color:var(--mut);text-transform:uppercase}
.tr2 span:nth-child(2){text-align:right}
.tr2 .p{font:500 31px 'LO'}
.tr2 .d{font:600 28px 'IN';color:var(--saf2);letter-spacing:.3px}
.tr2 .d small{display:block;font:500 20px 'IN';color:var(--mut);letter-spacing:.2px;margin-top:4px}
.tr2.last{border-bottom:1.5px solid #DCCFBA}
.tr2.hot{background:#FBF1E3;margin:0 -18px;padding-left:18px;padding-right:18px}
.note{font:400 26px/1.45 'LO';color:var(--mut)}
"""

def table():
    rows = [("India, Dubai, Singapore", "Mon 5 Oct", "", True),
            ("UK, USA, Canada", "Mon 5 Oct", "Pacific coast: Sun 4 Oct", False),
            ("Australia", "Mon 5 Oct", "", False)]
    s = '<div class="tr2 hd"><span>Where</span><span>Dashami shradh</span></div>'
    for k, (place, d, sub, hot) in enumerate(rows):
        cls = 'tr2' + (' hot' if hot else '') + (' last' if k == len(rows) - 1 else '')
        sm = f'<small>{sub}</small>' if sub else ''
        s += f'<div class="{cls}"><span class="p">{place}</span><span class="d">{d}{sm}</span></div>'
    return f'<div>{s}</div>'

HEAD = 'Dashami shradh is <em>Monday 5&nbsp;October</em>.'
BODY = 'The Dashami tithi, the tenth day of the dark fortnight, begins at 03:54 IST on Monday and runs through the whole&nbsp;afternoon.'
DELHI = 'Shradh hours in Delhi on Monday: <b style="color:#211B12;font-weight:600">13:19 – 15:40</b>, the&nbsp;aparahna.'
NEXT = 'Ekadashi shradh follows on Tuesday 6 October. Each place is computed by its own&nbsp;afternoon.'

def block(sz):
    return f"""
 <div class="eb" style="font-size:{sz['eb']}px">Pitru Paksha 2026 · The tenth shradh</div>
 <h1 style="font-size:{sz['h1']}px;margin-top:{sz['g1']}px">{HEAD}</h1>
 <div class="b" style="font-size:{sz['b']}px;margin-top:{sz['g2']}px">{BODY}</div>
 <div style="margin-top:{sz['g3']}px">{table()}</div>
 <div class="note" style="font-size:{sz['n']}px;margin-top:{sz['g4']}px;color:#211B12">{DELHI}</div>
 <div class="note" style="font-size:{sz['n2']}px;margin-top:10px">{NEXT}</div>
 <div class="m" style="font-size:{sz['n']}px;margin-top:{sz['g5']}px">The hours for your city:</div>
 <div class="link" style="font-size:{sz['lk']}px;margin-top:4px">astroriver.com/journal/pitru-paksha</div>"""

FEED_SZ = dict(eb=21, h1=80, g1=22, b=32, g2=26, g3=40, n=27, n2=24, g4=30, g5=28, lk=30)
feed = page(W, H, f'<div class="flow" style="top:110px;bottom:210px">{block(FEED_SZ)}</div>',
            river_path(1212, 1196, 1186, True, True), (610, 1168), 58, 560, 56).replace('</style>', EXTRA + '</style>', 1)

ST_SZ = dict(eb=25, h1=108, g1=30, b=40, g2=36, g3=60, n=33, n2=29, g4=44, g5=50, lk=36)
story = page(1080, 1920, f'<div class="flow" style="top:170px;bottom:250px">{block(ST_SZ)}</div>',
             river_path(1742, 1728, 1716, True, True), (470, 1680), 90, 820, 90).replace(
             '</style>', EXTRA + ".tr2{padding:32px 0} .tr2.hot{padding-left:18px;padding-right:18px} .tr2.hd{padding:0 0 16px} .tr2 .p{font-size:36px} .tr2 .d{font-size:32px} .tr2 .d small{font-size:23px} .tr2.hd span{font-size:22px}</style>", 1)

XW, XH = 1600, 900
def river_x(a, b):
    mid = (a + b) / 2 - 14
    p = f"M100,{a} C420,{a+12} 560,{mid} 800,{mid} C1060,{mid} 1200,{b} 1495,{b}"
    q = f"M100,{a+14} C420,{a+26} 560,{mid+18} 800,{mid+18} C1060,{mid+18} 1200,{b+14} 1495,{b+14}"
    return (f'<path d="{q}" fill="none" stroke="#E2D7C4" stroke-width="3"/><path d="{p}" fill="none" stroke="#D77B09" stroke-width="4.5" stroke-linecap="round"/>'
            f'<circle cx="100" cy="{a}" r="9" fill="#D77B09"/><circle cx="1495" cy="{b}" r="20" fill="none" stroke="#D77B09" stroke-width="3"/><circle cx="1495" cy="{b}" r="8" fill="#D77B09"/>')
x = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{EXTRA}
html,body{{width:{XW}px;height:{XH}px}} .s{{width:{XW}px;height:{XH}px}}
.tr2{{padding:18px 0}} .tr2.hot{{padding-left:18px;padding-right:18px}} .tr2.hd{{padding:0 0 12px}} .tr2 .p{{font-size:27px}} .tr2 .d{{font-size:25px}} .tr2 .d small{{font-size:18px}} .tr2.hd span{{font-size:17px}}</style></head><body><div class="s">
<div class="wm" style="top:330px;left:260px">astroriver.com</div><div class="tr" style="top:52px">astroriver.com</div>
<div style="position:absolute;left:100px;right:100px;top:100px;bottom:190px;display:flex;align-items:center;gap:64px">
 <div style="flex:1">
  <div class="eb" style="font-size:19px">Pitru Paksha 2026</div>
  <h1 style="font-size:66px;margin-top:18px">{HEAD}</h1>
  <div class="b" style="font-size:26px;margin-top:20px">The Dashami tithi begins at 03:54 IST on Monday and runs through the whole&nbsp;afternoon.</div>
  <div class="m" style="font-size:24px;margin-top:22px">The hours for your city:</div>
  <div class="link" style="margin-top:2px;font-size:27px">astroriver.com/journal/pitru-paksha</div>
 </div>
 <div style="flex:1.05">{table()}
  <div class="note" style="font-size:23px;margin-top:20px;color:#211B12">{DELHI}</div>
 </div>
</div>
<svg class="r" width="{XW}" height="{XH}">{river_x(794, 782)}</svg>
<div class="tag" style="left:700px;top:746px">astroriver.com</div>
<div class="foot" style="bottom:26px"><span class="n" style="font-size:32px">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

async def main():
    jobs = [('dashami-post-1080x1350', feed, W, H), ('dashami-status-1080x1920', story, 1080, 1920),
            ('dashami-x-1600x900', x, XW, XH)]
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html, w, h in jobs:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            fn = os.path.join(HERE, name + '.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            r = await pg.evaluate("() => { const d=document.querySelector('.flow'); if(!d) return null; const k=[...d.children]; return [Math.round(k[0].getBoundingClientRect().top), Math.round(k[k.length-1].getBoundingClientRect().bottom)] }")
            print(name, 'content spans', r)
            await pg.screenshot(path=os.path.join(HERE, 'out', name + '.png'))
        await b.close()
asyncio.run(main())
