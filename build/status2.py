# Sade Sati WhatsApp status, v2: one flowing block with even gaps, centred in the safe area
# (content no longer pinned to fixed heights). Same words as the published carousel.
import os, asyncio
from playwright.async_api import async_playwright
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_shared.py')).read())
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)

SW, SH = 1080, 1920
diagram = f'<svg width="880" height="480" viewBox="100 0 880 480" style="display:block;margin-top:34px">{three_signs(100, 112, 266, 224, 41, big=True)}</svg>'
body = f"""
<div style="position:absolute;left:100px;right:100px;top:170px;bottom:250px;display:flex;flex-direction:column;justify-content:center">
 <div class="eb" style="font-size:24px">River Journal · Sade Sati</div>
 <h1 style="font-size:124px;margin-top:24px">Is Sade Sati<br>on <em>you</em>?</h1>
 <div class="b" style="font-size:37px;margin-top:34px;color:#211B12">Saturn&#8217;s seven and a half years: about two and a half years each in the sign before your Moon, on your Moon, and the sign after it.</div>
 <div class="m" style="font-size:35px;margin-top:56px;color:#A8590A;font-weight:500">Saturn is in Pisces. Find your Moon sign:</div>
 {diagram}
 <div style="margin-top:44px;padding-top:34px;border-top:1.5px solid #DCCFBA">
  <div class="m" style="font-size:32px;color:#211B12">Capricorn Moon: Sade Sati ended on 29 March 2025.</div>
  <div class="m" style="font-size:32px;margin-top:30px">Phases, dates and remedies:</div>
  <div class="link" style="margin-top:4px;font-size:36px">astroriver.com/journal/sade-sati</div>
 </div>
</div>"""
html = page(SW, SH, body, river_path(1742, 1728, 1716, True, True), (470, 1680), 90, 820, 90)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': SW, 'height': SH})
        fn = os.path.join(HERE, 'sadesati-status-v2.html'); open(fn, 'w').write(html)
        await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
        box = await pg.evaluate("""() => { const d = document.querySelector('.s > div[style*="flex"]');
            const kids=[...d.children].map(k=>{const r=k.getBoundingClientRect();return [Math.round(r.top),Math.round(r.bottom)]});
            return kids; }""")
        print('blocks top/bottom:', box)
        await pg.screenshot(path=os.path.join(HERE, 'out', 'sadesati-status-1080x1920-v3.png'))
        await b.close()
asyncio.run(main())
