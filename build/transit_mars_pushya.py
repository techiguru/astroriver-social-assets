# 27 Sep 2026 single image: Mars in Pushya. Same system as the dasha and Pitru Paksha carousels.
# Every date below was computed this session (Swiss Ephemeris, Lahiri, IST) and matches the live
# Journal piece /journal/mars-in-cancer:
#   Mars enters Cancer 18 Sep 16:35 IST · Pushya 24 Sep 05:41 · Ashlesha 17 Oct 12:46
#   Jupiter enters Leo 31 Oct 12:02 · Mars leaves Cancer 12 Nov 20:18
import os, asyncio
from datetime import datetime
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
F = 'file://' + HERE + '/fonts/'

CSS = f"""
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900;}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700;}}
@font-face{{font-family:'LO';src:url('{F}Lora-Italic[wght].ttf');font-weight:400 700;font-style:italic;}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900;}}
:root{{--bg:#F3EDE2;--ink:#211B12;--saf:#D77B09;--saf2:#A8590A;--mut:#6B5B4B;--faint:#E2D7C4;}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:var(--bg);overflow:hidden}}
.s{{position:relative;background:var(--bg);color:var(--ink);font-family:'LO',serif}}
.tr{{position:absolute;right:102px;font:500 21px 'IN';letter-spacing:2.5px;color:var(--mut)}}
.wm{{position:absolute;left:70px;font:italic 400 176px 'PF';color:var(--ink);opacity:.045;transform:rotate(-13deg);transform-origin:left top;white-space:nowrap;pointer-events:none}}
.c{{position:absolute;left:100px;right:100px}}
.eb{{font:600 22px 'IN';letter-spacing:5.5px;color:var(--saf2);text-transform:uppercase}}
h1{{font:700 88px/1.05 'PF';letter-spacing:-.5px;margin-top:26px}}
em{{font-style:italic;color:var(--saf2);font-weight:600}}
.b{{font:400 35px/1.5 'LO';margin-top:32px}}
.m{{font:400 29px/1.5 'LO';color:var(--mut)}}
.foot{{position:absolute;left:100px;right:102px;display:flex;justify-content:space-between;align-items:baseline}}
.foot .n{{font:italic 500 36px 'PF'}}
.foot .u{{font:500 23px 'IN';letter-spacing:2.5px;color:var(--mut)}}
svg.r{{position:absolute;left:0;top:0}}
.tag{{position:absolute;font:600 17px 'IN';letter-spacing:2.5px;color:var(--saf2);background:var(--bg);padding:0 10px}}
"""

def river_single(W, a, b, tag_x, tag_y):
    mid = (a + b) / 2 - 18
    p = f"M100,{a} C300,{a+10} 360,{mid} 540,{mid} C720,{mid} 820,{b} 975,{b}"
    q = f"M100,{a+16} C300,{a+26} 360,{mid+20} 540,{mid+20} C720,{mid+20} 820,{b+16} 975,{b+16}"
    return (f'<path d="{q}" fill="none" stroke="#E2D7C4" stroke-width="3"/>'
            f'<path d="{p}" fill="none" stroke="#D77B09" stroke-width="4.5" stroke-linecap="round"/>'
            f'<circle cx="100" cy="{a}" r="9" fill="#D77B09"/>'
            f'<circle cx="975" cy="{b}" r="22" fill="none" stroke="#D77B09" stroke-width="3"/>'
            f'<circle cx="975" cy="{b}" r="9" fill="#D77B09"/>'), \
           f'<div class="tag" style="left:{tag_x}px;top:{tag_y}px">astroriver.com</div>'


# ---- v4: TRANSIT uniform with a bigger tag that names the kind of transit ----
SAND = "#EADFCB"
CSS3 = CSS.replace('--bg:#F3EDE2', '--bg:' + SAND)
def art_block(file, w, h, top):
    a = open(os.path.join(HERE, file)).read().replace('<svg ', f'<svg width="{w}" height="{h}" ', 1)
    return f'<div style="position:absolute;left:0;top:{top}px;width:{w}px;height:{h}px;overflow:hidden">{a}</div>'
def chip(text, size):
    return (f'<div style="display:inline-block;font:700 {size}px \'IN\';letter-spacing:4px;color:#FFF8EE;'
            f'background:#A8590A;border-radius:999px;padding:11px 24px 10px">{text}</div>')

def feed(tag, art, h1, body, cta, link):
    W, H = 1080, 1350
    riv, tg = river_single(W, 1212, 1196, 610, 1168)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS3}
html,body{{width:{W}px;height:{H}px}} .s{{width:{W}px;height:{H}px}}
.tr{{background:{SAND};padding:2px 10px;border-radius:4px}}</style></head><body><div class="s">
{art_block(art, W, 540, 40)}
<div class="wm" style="top:700px">astroriver.com</div><div class="tr" style="top:40px;right:92px">astroriver.com</div>
<div class="c" style="top:596px">
 {chip(tag, 22)}
 <h1 style="font-size:78px;margin-top:22px">{h1}</h1>
 <div class="b" style="font-size:34px;margin-top:24px">{body}</div>
 <div class="m" style="margin-top:30px;font-size:28px">{cta}</div>
 <div style="font:600 29px 'IN';color:#A8590A;margin-top:6px;letter-spacing:.2px">{link}</div>
</div>
<svg class="r" width="{W}" height="{H}">{riv}</svg>{tg}
<div class="foot" style="bottom:56px"><span class="n">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

def story(tag, art, h1, body, cta, link):
    SW, SH = 1080, 1920
    riv, tg = river_single(SW, 1742, 1728, 470, 1680)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS3}
html,body{{width:{SW}px;height:{SH}px}} .s{{width:{SW}px;height:{SH}px}}
.tr{{background:{SAND};padding:2px 10px;border-radius:4px}}</style></head><body><div class="s">
{art_block(art, SW, 660, 170)}
<div class="wm" style="top:980px">astroriver.com</div><div class="tr" style="top:104px;right:92px">astroriver.com</div>
<div class="c" style="top:880px">
 {chip(tag, 26)}
 <h1 style="font-size:96px;margin-top:26px">{h1}</h1>
 <div class="b" style="font-size:40px;margin-top:34px">{body}</div>
 <div class="m" style="margin-top:46px;font-size:33px">{cta}</div>
 <div style="font:600 33px 'IN';color:#A8590A;margin-top:8px">{link}</div>
</div>
<svg class="r" width="{SW}" height="{SH}">{riv}</svg>{tg}
<div class="foot" style="bottom:90px"><span class="n">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

MARS = ("NAKSHATRA TRANSIT", "art-pushya-mars-sand.svg",
        "Mars is in Pushya until <em>17&nbsp;October</em>.",
        "A good time for steady, patient work: for your home, your family and your long-term plans. The results come later.",
        "What it means for you, sign by sign:", "astroriver.com/journal/mars-in-cancer")
# Example only, to show the other tag. Dates computed this session (Jupiter enters Leo 31 Oct 12:02 IST);
# wording from /journal/jupiter-in-leo-2026.
JUP = ("SIGN TRANSIT", "art-jupiter-sand.svg",
       "Jupiter enters Leo on <em>31&nbsp;October</em>.",
       "A first look at Jupiter in Leo, three months long. Then Jupiter returns to Cancer until June 2027.",
       "What it means for you, sign by sign:", "astroriver.com/journal/jupiter-in-leo-2026")

async def main():
    out = os.path.join(HERE, 'out4'); os.makedirs(out, exist_ok=True)
    jobs = [('mars-post-1080x1350', feed(*MARS), 1080, 1350), ('mars-status-1080x1920', story(*MARS), 1080, 1920),
            ('example-jupiter-sign-1080x1350', feed(*JUP), 1080, 1350)]
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html, w, h in jobs:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            fn = os.path.join(HERE, 'v4-' + name + '.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=os.path.join(out, name + '.png'))
        await b.close()
asyncio.run(main())
print('done')
