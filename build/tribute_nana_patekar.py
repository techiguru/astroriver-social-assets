# Thu 8 Oct 2026 evening: a quiet tribute Story for Nana Patekar (died early Thursday 8 Oct in Goa, aged 75; reported
# by AP via NBC News and ANI). Founder 8 Oct: Story only, text only (no photo), no astrology and no link to Pitru Paksha.
# Ivory card with a small diya, his name, the years and Om Shanti. Writes out/tribute-nana-patekar-1080x1920.png.
import os, asyncio
from playwright.async_api import async_playwright
import pitra_dosh as P, pitra_dosh_reel as R
F = P.F
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{P.CSS}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-600-normal.woff2');font-weight:600;}}
html,body{{width:1080px;height:1920px}} .s{{width:1080px;height:1920px}}
.c{{position:absolute;left:100px;right:100px;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
</style></head><body><div class="s">
<div style="position:absolute;inset:0;transform:translateY(120px) scale(.62);transform-origin:540px 300px">{R.DIYA}</div>
<div class="c" style="top:300px">
 <div style="font:700 104px/1.05 'PF';color:{P.IV}">Nana Patekar</div>
 <div style="font:500 40px 'IN';letter-spacing:6px;color:{P.MUT};margin-top:30px">1951 – 2026</div>
 <div style="width:120px;height:2px;background:{P.RIVER};margin:56px 0 50px"></div>
 <div style="font:600 54px 'NSR';color:{P.SAF}">ॐ शान्ति</div>
 <div style="font:italic 400 40px 'LO';color:{P.MUT};margin-top:14px">Om Shanti</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:300px;text-align:center;font:italic 500 34px 'PF';color:{P.MUT}">Astro River</div>
</div></body></html>"""
async def main():
    fn = os.path.join(P.HERE, 'out', 'tribute-nana-patekar.html'); open(fn, 'w').write(html)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
        await pg.screenshot(path=os.path.join(P.HERE, 'out', 'tribute-nana-patekar-1080x1920.png')); await b.close()
asyncio.run(main())
