# 8 Oct 2026: founder: "It's getting so boring... the two reels look like two black spots on the grid". Samples in bold
# colour: a new tribute Story for Nana Patekar (charcoal with marigold) and custom Reel covers (uploaded in the
# Instagram app as the cover image), each in its own colour so the grid has contrast. The grid shows the middle of a
# Reel cover, so the title sits inside the centre 1080x1350.
import os, math, asyncio
from playwright.async_api import async_playwright
import pitra_dosh as P, pitra_dosh_reel as R
F = P.F
FONTS = f"""
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-600-normal.woff2');font-weight:600;}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700;}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-600-normal.woff2');font-weight:600;}}
"""
def wrap(bg, inner, art=''):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{P.CSS}{FONTS}
html,body{{width:1080px;height:1920px;background:{bg}}} .s{{width:1080px;height:1920px;background:{bg};overflow:hidden}}
.c{{position:absolute;left:90px;right:90px;display:flex;flex-direction:column;align-items:center;text-align:center}}
</style></head><body><div class="s"><svg class="r" width="1080" height="1920">{art}</svg>{inner}</div></body></html>"""
def brand(color, line='#D77B09', top=200):
    return (f'<div style="position:absolute;left:0;right:0;top:{top}px;text-align:center;color:{color}"><div style="font:600 32px PF;letter-spacing:14px;padding-left:14px">ASTRO RIVER</div>'
            f'<svg width="200" height="24" style="display:block;margin:8px auto 0"><path d="M12,14 C55,4 82,22 100,12 C118,3 146,20 188,10" fill="none" stroke="{line}" stroke-width="3" stroke-linecap="round"/></svg></div>')
def garland(y, n=23, col1='#E8A33D', col2='#D9701E'):
    out = ''
    for i in range(n):
        x = 40 + i * (1000 / (n - 1)); yy = y + 60 * math.sin(math.pi * i / (n - 1))
        out += f'<circle cx="{x:.0f}" cy="{yy:.0f}" r="21" fill="{col1 if i % 2 else col2}"/><circle cx="{x:.0f}" cy="{yy:.0f}" r="8" fill="#F6D27A" opacity=".8"/>'
    return out
def stars(seed, n, y0, y1, col):
    import random; random.seed(seed)
    return ''.join(f'<circle cx="{random.randint(40,1040)}" cy="{random.randint(y0,y1)}" r="{random.choice([1.6,2.2,3])}" fill="{col}" opacity="{random.choice([.35,.6,.9])}"/>' for _ in range(n))

# 1. tribute: charcoal, a marigold string, a lit diya, the name in ivory
CH = '#1D1B1A'
tribute = wrap(CH, f"""
<div style="position:absolute;inset:0;transform:translateY(250px) scale(.7);transform-origin:540px 300px;filter:drop-shadow(0 0 40px rgba(232,163,61,.35))">{R.DIYA.replace(P.GLYPH_RING, '#2A2624')}</div>
<div class="c" style="top:930px">
 <div style="font:700 112px/1.05 PF;color:#F3EDE2">Nana Patekar</div>
 <div style="font:500 40px IN;letter-spacing:7px;color:#B9AFA5;margin-top:30px">1951 – 2026</div>
 <div style="width:120px;height:2px;background:#E8A33D;margin:54px 0 48px"></div>
 <div style="font:700 60px NSR;color:#E8A33D">ॐ शान्ति</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:250px;text-align:center;font:italic 500 32px PF;color:#8F857C">Astro River</div>""",
 garland(250))

# 2. pitru dosha (Hindi) cover: Sun terracotta ground, eclipse in ivory and ink, big Hindi title
SUN = '#B4674C'
ecl = (f'<circle cx="540" cy="640" r="250" fill="#C47C61"/><circle cx="540" cy="640" r="205" fill="none" stroke="#FBE3C4" stroke-opacity=".35" stroke-width="2"/>'
       + ''.join(f'<line x1="540" y1="{640-160}" x2="540" y2="{640-200}" stroke="#FBE3C4" stroke-width="10" stroke-linecap="round" opacity=".7" transform="rotate({d} 540 640)"/>' for d in range(0, 360, 30))
       + '<circle cx="540" cy="640" r="128" fill="#FBE3C4"/><circle cx="590" cy="620" r="122" fill="#2A1A14"/>')
cover_pd = wrap(SUN, brand('#FBE3C4', '#FBE3C4') + f"""
<div class="c" style="top:930px">
 <div style="font:700 150px/1.25 NSR;color:#FFF6EA">पितृ दोष</div>
 <div style="font:600 56px/1.4 NSR;color:#2A1A14;margin-top:6px">भाग्य पर ग्रहण?</div>
 <div style="font:600 34px NSD;color:#FBE3C4;margin-top:34px">कारण · लक्षण · उपाय</div>
</div>""", ecl)

# 3. Sarva Pitru Amavasya (English) cover: night indigo, a silver new moon with its rim, stars, gold title
NIGHT = '#1F2A47'
moon = (stars(4, 70, 120, 1700, '#F3EDE2') + '<circle cx="540" cy="660" r="215" fill="none" stroke="#C9D1E6" stroke-opacity=".18" stroke-width="40"/>'
        '<circle cx="540" cy="660" r="160" fill="#141B30" stroke="#DCE2F0" stroke-width="5"/><path d="M 655 550 A 160 160 0 0 1 655 770 A 190 190 0 0 0 655 550 Z" fill="#DCE2F0" opacity=".9"/>')
cover_am = wrap(NIGHT, brand('#F3EDE2') + f"""
<div class="c" style="top:940px">
 <div style="font:600 30px IN;letter-spacing:6px;color:#F0B061">THE LAST DAY OF PITRU PAKSHA</div>
 <div style="font:700 112px/1.02 PF;color:#F3EDE2;margin-top:24px">Sarva Pitru <em style="color:#F0B061;font-style:italic">Amavasya</em></div>
 <div style="font:400 46px/1.4 LO;color:#C9D1E6;margin-top:30px">Don&#8217;t know their tithi? This day is for&nbsp;them.</div>
</div>""", moon)

# 4. Sarva Pitru Amavasya (Hindi) cover: marigold ground, ink new moon, deep maroon title
MARI = '#E39A3B'
moon2 = ('<circle cx="540" cy="660" r="235" fill="#EBB15E"/><circle cx="540" cy="660" r="160" fill="#3A1712"/>'
         '<circle cx="540" cy="660" r="168" fill="none" stroke="#FFF1D6" stroke-width="3" opacity=".8"/>' + garland(1660, 23, '#C9581A', '#F2C14E'))
cover_amh = wrap(MARI, brand('#3A1712', '#3A1712') + f"""
<div class="c" style="top:940px">
 <div style="font:600 38px NSD;color:#5A2418">पितृ पक्ष का अंतिम दिन</div>
 <div style="font:700 128px/1.25 NSR;color:#3A1712;margin-top:10px">सर्वपितृ अमावस्या</div>
 <div style="font:600 48px/1.45 NSD;color:#5A2418;margin-top:14px">तिथि याद नहीं? यह दिन उनके लिए&nbsp;है।</div>
</div>""", moon2)

async def main():
    jobs = [('tribute-nana-patekar-v2', tribute), ('cover-pitru-dosha-hindi', cover_pd), ('cover-amavasya-english', cover_am), ('cover-amavasya-hindi', cover_amh)]
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        for name, html in jobs:
            fn = os.path.join(P.HERE, 'out', name + '.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=os.path.join(P.HERE, 'out', name + '.png'))
        await b.close()
asyncio.run(main())
