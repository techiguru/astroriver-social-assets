# Pitru Paksha 2026, Hindi: the India shradh dates as one image. Same "dress" as the 26 Sep
# Pitru Paksha carousel. Every Hindi word below is copied from the founder-approved Hindi page
# (content/source/journal-pitru-paksha-2026-hi.md, live at /hi/journal/pitru-paksha), except the
# three short lines marked NEW, which he must approve.
import os, asyncio
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
F = 'file://' + HERE + '/fonts/'

CSS = f"""
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900;}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700;}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900;}}
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-400-normal.woff2');font-weight:400;}}
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-600-normal.woff2');font-weight:600;}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-600-normal.woff2');font-weight:600;}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700;}}
:root{{--bg:#F3EDE2;--ink:#211B12;--saf:#D77B09;--saf2:#A8590A;--mut:#6B5B4B;--faint:#E2D7C4;}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:var(--bg);overflow:hidden}}
.s{{position:relative;background:var(--bg);color:var(--ink);font-family:'NSD','LO',serif}}
.tr{{position:absolute;right:102px;font:500 21px 'IN';letter-spacing:2.5px;color:var(--mut)}}
.wm{{position:absolute;left:70px;font:italic 400 176px 'PF';color:var(--ink);opacity:.045;transform:rotate(-13deg);transform-origin:left top;white-space:nowrap;pointer-events:none}}
.c{{position:absolute;left:100px;right:100px}}
.chip{{position:absolute;left:100px;font:600 24px 'NSD';color:var(--saf2);border:2px solid var(--saf);border-radius:999px;padding:2px 18px 4px}}
.eb{{font:600 28px 'NSD','IN';color:var(--saf2);letter-spacing:.5px}}
h1{{font:700 76px/1.3 'NSR','PF';margin-top:6px}}
.m{{font:400 29px/1.55 'NSD','LO';color:var(--mut)}}
.row{{display:flex;justify-content:space-between;align-items:baseline;padding:13px 0;border-bottom:1.5px solid #E2D7C4}}
.row .t{{font:600 30px 'NSD'}}
.row .d{{font:600 26px 'NSD','IN';color:var(--saf2)}}
.foot{{position:absolute;left:100px;right:102px;display:flex;justify-content:space-between;align-items:baseline}}
.foot .n{{font:italic 500 36px 'PF'}}
.foot .u{{font:500 23px 'IN';letter-spacing:2.5px;color:var(--mut)}}
svg.r{{position:absolute;left:0;top:0}}
.tag{{position:absolute;font:600 17px 'IN';letter-spacing:2.5px;color:var(--saf2);background:var(--bg);padding:0 10px}}
"""

# India, Dubai column of the approved Hindi table (tithi names without the word "श्राद्ध")
L = [("पूर्णिमा", "शनि 26 सित."), ("प्रतिपदा", "रवि 27 सित."), ("द्वितीया", "सोम 28 सित."), ("तृतीया", "मंगल 29 सित."),
     ("चतुर्थी", "बुध 30 सित.*"), ("पंचमी", "बुध 30 सित.*"), ("षष्ठी", "गुरु 1 अक्टू."), ("सप्तमी", "शुक्र 2 अक्टू.")]
R = [("अष्टमी", "शनि 3 अक्टू."), ("नवमी", "रवि 4 अक्टू."), ("दशमी", "सोम 5 अक्टू."), ("एकादशी", "मंगल 6 अक्टू."),
     ("द्वादशी", "बुध 7 अक्टू."), ("त्रयोदशी", "गुरु 8 अक्टू."), ("चतुर्दशी", "शुक्र 9 अक्टू."), ("अमावस्या", "शनि 10 अक्टू.")]
col = lambda items: "".join(f'<div class="row"><span class="t">{t}</span><span class="d">{d}</span></div>' for t, d in items)

def river(a, b, tx, ty):
    mid = (a + b) / 2 - 18
    p = f"M100,{a} C300,{a+10} 360,{mid} 540,{mid} C720,{mid} 820,{b} 975,{b}"
    q = f"M100,{a+16} C300,{a+26} 360,{mid+20} 540,{mid+20} C720,{mid+20} 820,{b+16} 975,{b+16}"
    return (f'<path d="{q}" fill="none" stroke="#E2D7C4" stroke-width="3"/>'
            f'<path d="{p}" fill="none" stroke="#D77B09" stroke-width="4.5" stroke-linecap="round"/>'
            f'<circle cx="100" cy="{a}" r="9" fill="#D77B09"/>'
            f'<circle cx="975" cy="{b}" r="22" fill="none" stroke="#D77B09" stroke-width="3"/>'
            f'<circle cx="975" cy="{b}" r="9" fill="#D77B09"/>'), f'<div class="tag" style="left:{tx}px;top:{ty}px">astroriver.com</div>'

W, H = 1080, 1350
rv, tg = river(1212, 1196, 610, 1168)
feed = f"""<!doctype html><html lang="hi"><head><meta charset="utf-8"><style>{CSS}
html,body{{width:{W}px;height:{H}px}} .s{{width:{W}px;height:{H}px}}</style></head><body><div class="s">
<div class="wm" style="top:560px">astroriver.com</div><div class="tr" style="top:58px">astroriver.com</div>
<div class="chip" style="top:48px">हिंदी</div>
<div class="c" style="top:150px">
 <div class="eb">पितृ पक्ष 2026</div>
 <h1>श्राद्ध 2026 की तिथियां</h1>
 <div class="m" style="margin-top:4px">भारत, दुबई · अपनी तिथि ढूंढें</div>
 <div style="display:flex;gap:56px;margin-top:34px">
  <div style="flex:1">{col(L)}</div><div style="flex:1">{col(R)}</div>
 </div>
 <div class="m" style="margin-top:18px;font-size:25px">* एक ही दिन दो श्राद्ध।</div>
 <div class="m" style="margin-top:36px;font-size:28px;color:#211B12">हर देश की तारीखें, श्राद्ध का समय और विधि:</div>
 <div style="font:600 29px 'IN';color:#A8590A;margin-top:6px;letter-spacing:.2px">astroriver.com/hi/journal/pitru-paksha</div>
</div>
<svg class="r" width="{W}" height="{H}">{rv}</svg>{tg}
<div class="foot" style="bottom:56px"><span class="n">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

SW, SH = 1080, 1920
rv2, tg2 = river(1742, 1728, 470, 1680)
story = f"""<!doctype html><html lang="hi"><head><meta charset="utf-8"><style>{CSS}
html,body{{width:{SW}px;height:{SH}px}} .s{{width:{SW}px;height:{SH}px}}
.row{{padding:14px 0}} .row .t{{font-size:34px}} .row .d{{font-size:29px}}</style></head><body><div class="s">
<div class="wm" style="top:820px">astroriver.com</div><div class="tr" style="top:90px">astroriver.com</div>
<div class="chip" style="top:80px">हिंदी</div>
<div class="c" style="top:250px">
 <div class="eb" style="font-size:32px">पितृ पक्ष 2026</div>
 <h1 style="font-size:88px">श्राद्ध 2026 की तिथियां</h1>
 <div class="m" style="margin-top:6px;font-size:32px">भारत, दुबई · अपनी तिथि ढूंढें</div>
 <div style="display:flex;gap:56px;margin-top:40px">
  <div style="flex:1">{col(L)}</div><div style="flex:1">{col(R)}</div>
 </div>
 <div class="m" style="margin-top:22px;font-size:28px">* एक ही दिन दो श्राद्ध।</div>
 <div class="m" style="margin-top:44px;font-size:32px;color:#211B12">हर देश की तारीखें, श्राद्ध का समय और विधि:</div>
 <div style="font:600 32px 'IN';color:#A8590A;margin-top:8px">astroriver.com/hi/journal/pitru-paksha</div>
</div>
<svg class="r" width="{SW}" height="{SH}">{rv2}</svg>{tg2}
<div class="foot" style="bottom:90px"><span class="n">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

async def main():
    out = os.path.join(HERE, 'out'); os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html, w, h in [('post-1080x1350', feed, W, H), ('status-1080x1920', story, SW, SH)]:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            fn = os.path.join(HERE, name + '.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=os.path.join(out, name + '.png'))
        await b.close()
asyncio.run(main())
print('done')
