# Maha Bharani for X, 1600x900, ivory Pitru Paksha dress. Words and times from the approved 28 Sep English post.
import os, asyncio
from playwright.async_api import async_playwright
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_shared.py')).read())
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
XW, XH = 1600, 900
def river_x(a, b):
    mid = (a + b) / 2 - 14
    p = f"M100,{a} C420,{a+12} 560,{mid} 800,{mid} C1060,{mid} 1200,{b} 1495,{b}"
    q = f"M100,{a+14} C420,{a+26} 560,{mid+18} 800,{mid+18} C1060,{mid+18} 1200,{b+14} 1495,{b+14}"
    return (f'<path d="{q}" fill="none" stroke="#E2D7C4" stroke-width="3"/><path d="{p}" fill="none" stroke="#D77B09" stroke-width="4.5" stroke-linecap="round"/>'
            f'<circle cx="100" cy="{a}" r="9" fill="#D77B09"/><circle cx="1495" cy="{b}" r="20" fill="none" stroke="#D77B09" stroke-width="3"/><circle cx="1495" cy="{b}" r="8" fill="#D77B09"/>')
rows = """
 <div class="row"><span class="k">Moon in Bharani<small>India time</small></span><span class="v">Tue 29 Sep, 09:04<small>to Wed 30 Sep, 07:37</small></span></div>
 <div class="row"><span class="k">Shradh hours in Delhi<small>Aparahna, the afternoon</small></span><span class="v">13:22 – 15:45</span></div>
 <div class="row" style="border-bottom:1.5px solid #DCCFBA"><span class="k">UK, USA, Canada, Australia</span><span class="v">Also Tuesday</span></div>"""
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
html,body{{width:{XW}px;height:{XH}px}} .s{{width:{XW}px;height:{XH}px}}
.row{{padding:18px 0}} .row .k{{font-size:29px}} .row .v{{font-size:27px}}</style></head><body><div class="s">
<div class="wm" style="top:330px;left:260px">astroriver.com</div><div class="tr" style="top:52px">astroriver.com</div>
<div style="position:absolute;left:100px;right:100px;top:100px;bottom:190px;display:flex;align-items:center;gap:70px">
 <div style="flex:1.05">
  <div class="eb" style="font-size:20px">Pitru Paksha 2026</div>
  <h1 style="font-size:84px;margin-top:20px">Maha Bharani is <em>today</em>.</h1>
  <div class="b" style="font-size:31px;margin-top:24px">The tradition holds that a shradh done on Bharani in this fortnight carries the merit of one done at Gaya.</div>
  <div class="m" style="font-size:26px;margin-top:26px">The hours for your city:</div>
  <div class="link" style="margin-top:2px;font-size:29px">astroriver.com/journal/pitru-paksha</div>
 </div>
 <div style="flex:1">{rows}</div>
</div>
<svg class="r" width="{XW}" height="{XH}">{river_x(794, 782)}</svg>
<div class="tag" style="left:700px;top:746px">astroriver.com</div>
<div class="foot" style="bottom:26px"><span class="n" style="font-size:32px">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': XW, 'height': XH})
        fn = os.path.join(HERE, 'bharani-x-1600x900.html'); open(fn, 'w').write(html)
        await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
        await pg.screenshot(path=os.path.join(HERE, 'out', 'bharani-x-1600x900.png')); await b.close()
asyncio.run(main()); print('ok')
