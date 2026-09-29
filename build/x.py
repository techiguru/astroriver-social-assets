# Sade Sati image for X, 1600x900 (16:9 shows uncropped on X, phone and desktop).
import os, asyncio
from playwright.async_api import async_playwright
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_shared.py')).read())
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)

XW, XH = 1600, 900
def river_x(a, b):
    mid = (a + b) / 2 - 14
    p = f"M100,{a} C420,{a+12} 560,{mid} 800,{mid} C1060,{mid} 1200,{b} 1495,{b}"
    q = f"M100,{a+14} C420,{a+26} 560,{mid+18} 800,{mid+18} C1060,{mid+18} 1200,{b+14} 1495,{b+14}"
    return (f'<path d="{q}" fill="none" stroke="#E2D7C4" stroke-width="3"/>'
            f'<path d="{p}" fill="none" stroke="#D77B09" stroke-width="4.5" stroke-linecap="round"/>'
            f'<circle cx="100" cy="{a}" r="9" fill="#D77B09"/>'
            f'<circle cx="1495" cy="{b}" r="20" fill="none" stroke="#D77B09" stroke-width="3"/>'
            f'<circle cx="1495" cy="{b}" r="8" fill="#D77B09"/>')

BW, GAP = 228, 30
DW = 3 * BW + 2 * GAP
diagram = f'<svg width="{DW}" height="450" viewBox="100 0 {DW} 450" style="display:block">{three_signs(100, 112, BW, 196, GAP)}</svg>'
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
html,body{{width:{XW}px;height:{XH}px}} .s{{width:{XW}px;height:{XH}px}}</style></head><body><div class="s">
<div class="wm" style="top:330px;left:260px">astroriver.com</div><div class="tr" style="top:52px">astroriver.com</div>
<div style="position:absolute;left:100px;right:100px;top:100px;bottom:190px;display:flex;align-items:center;justify-content:space-between;gap:60px">
 <div style="flex:1">
  <div class="eb" style="font-size:21px">River Journal · Sade Sati</div>
  <h1 style="font-size:96px;margin-top:20px">Is Sade Sati<br>on <em>you</em>?</h1>
  <div class="m" style="font-size:31px;margin-top:26px;color:#A8590A;font-weight:500">Saturn is in Pisces. Find your Moon sign.</div>
  <div class="m" style="font-size:28px;margin-top:34px;color:#211B12"><span style="font-weight:600">Capricorn Moon:</span><br>Sade Sati ended on 29&nbsp;March&nbsp;2025.</div>
  <div class="m" style="font-size:27px;margin-top:22px">Phases, dates and remedies:</div>
  <div class="link" style="margin-top:2px;font-size:31px">astroriver.com/journal/sade-sati</div>
 </div>
 {diagram}
</div>
<svg class="r" width="{XW}" height="{XH}">{river_x(794, 782)}</svg>
<div class="tag" style="left:700px;top:746px">astroriver.com</div>
<div class="foot" style="bottom:26px"><span class="n" style="font-size:32px">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': XW, 'height': XH})
        fn = os.path.join(HERE, 'sadesati-x-1600x900.html'); open(fn, 'w').write(html)
        await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
        await pg.screenshot(path=os.path.join(HERE, 'out', 'sadesati-x-1600x900.png'))
        await b.close()
asyncio.run(main())
print('x done')
