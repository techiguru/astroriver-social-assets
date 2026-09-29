# Wed 30 Sep 2026 morning: Chaturthi and Panchami shradh on one day. Ivory Pitru Paksha dress.
# Facts computed this session (Swiss Ephemeris, Lahiri), each city by its own aparahna, and matching the
# live article /journal/pitru-paksha table:
#   Krishna Chaturthi tithi: Tue 29 Sep 17:10 IST -> Wed 30 Sep 14:55 IST (Panchami begins 14:55:51 IST).
#   Delhi Wed 30 Sep aparahna 13:22-15:44 IST: Chaturthi covers 66%, Panchami 34% -> both shradhs Wed 30.
#   London, New York, Toronto, San Francisco, Vancouver: Chaturthi Tue 29, Panchami Wed 30.
#   Sydney and Singapore: Chaturthi Wed 30, Panchami Thu 1 Oct. Guwahati: Panchami Thu 1 Oct.
import os, asyncio
from playwright.async_api import async_playwright
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_shared.py')).read())
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)

EXTRA = """
.flow{position:absolute;left:100px;right:100px;display:flex;flex-direction:column;justify-content:center}
.tr3{display:grid;grid-template-columns:1.3fr 1fr 1fr;align-items:baseline;padding:22px 0;border-top:1.5px solid #DCCFBA}
.tr3.hd{border-top:0;padding:0 0 14px}
.tr3.hd span{font:600 19px 'IN';letter-spacing:2.5px;color:var(--mut);text-transform:uppercase}
.tr3 span:nth-child(n+2){text-align:right}
.tr3 .p{font:500 31px 'LO'}
.tr3 .d{font:600 28px 'IN';color:var(--saf2);letter-spacing:.3px}
.tr3.last{border-bottom:1.5px solid #DCCFBA}
.tr3.hot{background:#FBF1E3;margin:0 -18px;padding-left:18px;padding-right:18px}
.note{font:400 26px/1.45 'LO';color:var(--mut)}
"""

def table():
    rows = [("India, Dubai", "Wed 30 Sep", "Wed 30 Sep", True),
            ("UK, USA, Canada", "Tue 29 Sep", "Wed 30 Sep", False),
            ("Australia, Singapore", "Wed 30 Sep", "Thu 1 Oct", False)]
    s = '<div class="tr3 hd"><span>Where</span><span>Chaturthi</span><span>Panchami</span></div>'
    for k, (place, c, p, hot) in enumerate(rows):
        cls = 'tr3' + (' hot' if hot else '') + (' last' if k == len(rows) - 1 else '')
        s += f'<div class="{cls}"><span class="p">{place}</span><span class="d">{c}</span><span class="d">{p}</span></div>'
    return f'<div>{s}</div>'

HEAD = 'Chaturthi and Panchami shradh, <em>both on Wednesday 30&nbsp;September</em>.'
BODY = 'In India this year the two shradhs share one afternoon. The Chaturthi tithi ends at 14:55 IST on Wednesday, and Panchami&nbsp;begins.'
DELHI = 'Shradh hours in Delhi on Wednesday: <b style="color:#211B12;font-weight:600">13:22 – 15:44</b>, the&nbsp;aparahna.'
GUW = 'In Guwahati, Panchami moves to Thursday 1&nbsp;October. Each place is computed by its own afternoon.'

def block(sz):
    return f"""
 <div class="eb" style="font-size:{sz['eb']}px">Pitru Paksha 2026 · Two shradhs, one day</div>
 <h1 style="font-size:{sz['h1']}px;margin-top:{sz['g1']}px">{HEAD}</h1>
 <div class="b" style="font-size:{sz['b']}px;margin-top:{sz['g2']}px">{BODY}</div>
 <div style="margin-top:{sz['g3']}px">{table()}</div>
 <div class="note" style="font-size:{sz['n']}px;margin-top:{sz['g4']}px;color:#211B12">{DELHI}</div>
 <div class="note" style="font-size:{sz['n2']}px;margin-top:10px">{GUW}</div>
 <div class="m" style="font-size:{sz['n']}px;margin-top:{sz['g5']}px">The hours for your city:</div>
 <div class="link" style="font-size:{sz['lk']}px;margin-top:4px">astroriver.com/journal/pitru-paksha</div>"""

FEED_SZ = dict(eb=21, h1=66, g1=22, b=31, g2=24, g3=34, n=27, n2=24, g4=26, g5=26, lk=30)
feed = page(W, H, f'<div class="flow" style="top:110px;bottom:210px">{block(FEED_SZ)}</div>',
            river_path(1212, 1196, 1186, True, True), (610, 1168), 58, 560, 56).replace('</style>', EXTRA + '</style>', 1)

ST_SZ = dict(eb=25, h1=94, g1=30, b=39, g2=34, g3=56, n=33, n2=29, g4=40, g5=48, lk=36)
story = page(1080, 1920, f'<div class="flow" style="top:170px;bottom:250px">{block(ST_SZ)}</div>',
             river_path(1742, 1728, 1716, True, True), (470, 1680), 90, 820, 90).replace(
             '</style>', EXTRA + ".tr3{padding:30px 0} .tr3.hot{padding-left:18px;padding-right:18px} .tr3.hd{padding:0 0 16px} .tr3 .p{font-size:36px} .tr3 .d{font-size:32px} .tr3.hd span{font-size:22px}</style>", 1)

XW, XH = 1600, 900
def river_x(a, b):
    mid = (a + b) / 2 - 14
    p = f"M100,{a} C420,{a+12} 560,{mid} 800,{mid} C1060,{mid} 1200,{b} 1495,{b}"
    q = f"M100,{a+14} C420,{a+26} 560,{mid+18} 800,{mid+18} C1060,{mid+18} 1200,{b+14} 1495,{b+14}"
    return (f'<path d="{q}" fill="none" stroke="#E2D7C4" stroke-width="3"/><path d="{p}" fill="none" stroke="#D77B09" stroke-width="4.5" stroke-linecap="round"/>'
            f'<circle cx="100" cy="{a}" r="9" fill="#D77B09"/><circle cx="1495" cy="{b}" r="20" fill="none" stroke="#D77B09" stroke-width="3"/><circle cx="1495" cy="{b}" r="8" fill="#D77B09"/>')
x = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{EXTRA}
html,body{{width:{XW}px;height:{XH}px}} .s{{width:{XW}px;height:{XH}px}}
.tr3{{padding:17px 0}} .tr3.hot{{padding-left:18px;padding-right:18px}} .tr3.hd{{padding:0 0 12px}} .tr3 .p{{font-size:27px}} .tr3 .d{{font-size:25px}} .tr3.hd span{{font-size:17px}}</style></head><body><div class="s">
<div class="wm" style="top:330px;left:260px">astroriver.com</div><div class="tr" style="top:52px">astroriver.com</div>
<div style="position:absolute;left:100px;right:100px;top:100px;bottom:190px;display:flex;align-items:center;gap:64px">
 <div style="flex:1">
  <div class="eb" style="font-size:19px">Pitru Paksha 2026</div>
  <h1 style="font-size:60px;margin-top:18px">{HEAD}</h1>
  <div class="b" style="font-size:26px;margin-top:20px">The Chaturthi tithi ends at 14:55 IST on Wednesday, and Panchami&nbsp;begins.</div>
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
    jobs = [('chaturthi-panchami-post-1080x1350', feed, W, H), ('chaturthi-panchami-status-1080x1920', story, 1080, 1920),
            ('chaturthi-panchami-x-1600x900', x, XW, XH)]
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
