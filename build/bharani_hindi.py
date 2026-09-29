# Tue 29 Sep 2026 morning: Maha Bharani in Hindi. Ivory Pitru Paksha dress + हिंदी label.
# Every Hindi line is copied from the approved page content/source/journal-pitru-paksha-2026-hi.md:
#   "महा भरणी — मंगलवार 29 सितंबर, हर जगह।" / "मान्यता है कि पितृ पक्ष में भरणी के दिन किया गया श्राद्ध गया में
#   किए गए श्राद्ध के समान फल देता है।" / Delhi table row 29 सित. / "मुख्य अर्पण इसी समय किया जाता है।"
#   Link line "हर देश की तारीखें, श्राद्ध का समय और विधि:" is the one already used on the 27 Sep Hindi post.
import os, asyncio
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
CSS = f"""
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900;}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900;}}
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-400-normal.woff2');font-weight:400;}}
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-600-normal.woff2');font-weight:600;}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-600-normal.woff2');font-weight:600;}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700;}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:#F3EDE2;overflow:hidden}}
.s{{position:relative;background:#F3EDE2;color:#211B12;font-family:'NSD',serif}}
.tr{{position:absolute;right:102px;font:500 21px 'IN';letter-spacing:2.5px;color:#6B5B4B}}
.wm{{position:absolute;left:70px;font:italic 400 176px 'PF';color:#211B12;opacity:.045;transform:rotate(-13deg);transform-origin:left top;white-space:nowrap}}
.chip{{position:absolute;left:100px;font:600 24px 'NSD';color:#A8590A;border:2px solid #D77B09;border-radius:999px;padding:2px 18px 4px}}
.flow{{position:absolute;left:100px;right:100px;display:flex;flex-direction:column;justify-content:center}}
.eb{{font:600 30px 'NSD';color:#A8590A}}
h1{{font:700 132px/1.2 'NSR';margin-top:4px}}
.when{{font:600 40px/1.4 'NSD';color:#A8590A;margin-top:2px}}
.b{{font:400 35px/1.65 'NSD';margin-top:26px}}
.hd{{font:600 26px 'NSD';color:#6B5B4B;margin-top:44px}}
.hd span{{font:600 21px 'IN';letter-spacing:2.5px}}
.row{{display:flex;justify-content:space-between;align-items:center;padding:16px 0;border-bottom:1.5px solid #E2D7C4}}
.row:first-of-type{{border-top:1.5px solid #E2D7C4}}
.row .t{{font:600 32px 'NSD'}} .row .t small{{display:block;font:400 23px 'NSD';color:#6B5B4B;margin-top:-2px}}
.row .d{{font:600 30px 'IN';color:#6B5B4B;letter-spacing:.3px}}
.row.hot .t,.row.hot .d{{color:#A8590A}} .row.hot .d{{font-size:34px}}
.lk1{{font:400 29px 'NSD';margin-top:44px}}
.lk2{{font:600 30px 'IN';color:#A8590A;margin-top:4px;letter-spacing:.2px}}
.foot{{position:absolute;left:100px;right:102px;display:flex;justify-content:space-between;align-items:baseline}}
.foot .n{{font:italic 500 36px 'PF'}} .foot .u{{font:500 23px 'IN';letter-spacing:2.5px;color:#6B5B4B}}
svg.r{{position:absolute;left:0;top:0}}
.tag{{position:absolute;font:600 17px 'IN';letter-spacing:2.5px;color:#A8590A;background:#F3EDE2;padding:0 10px}}
"""
def river(a, b):
    mid = (a + b) / 2 - 18
    p = f"M100,{a} C300,{a+10} 360,{mid} 540,{mid} C720,{mid} 820,{b} 975,{b}"
    q = f"M100,{a+16} C300,{a+26} 360,{mid+20} 540,{mid+20} C720,{mid+20} 820,{b+16} 975,{b+16}"
    return (f'<path d="{q}" fill="none" stroke="#E2D7C4" stroke-width="3"/><path d="{p}" fill="none" stroke="#D77B09" stroke-width="4.5" stroke-linecap="round"/>'
            f'<circle cx="100" cy="{a}" r="9" fill="#D77B09"/><circle cx="975" cy="{b}" r="22" fill="none" stroke="#D77B09" stroke-width="3"/><circle cx="975" cy="{b}" r="9" fill="#D77B09"/>')

content = """
 <div class="eb">पितृ पक्ष 2026</div>
 <h1>महा भरणी</h1>
 <div class="when">मंगलवार 29 सितंबर, हर जगह।</div>
 <div class="b">मान्यता है कि पितृ पक्ष में भरणी के दिन किया गया श्राद्ध गया में किए गए श्राद्ध के समान फल देता है।</div>
 <div class="hd">श्राद्ध का समय · <span>दिल्ली, IST</span></div>
 <div style="margin-top:12px">
  <div class="row"><span class="t">कुतुप</span><span class="d">11:47 – 12:35</span></div>
  <div class="row"><span class="t">रौहिण</span><span class="d">12:35 – 13:22</span></div>
  <div class="row hot"><span class="t">अपराह्न<small>मुख्य अर्पण इसी समय किया जाता है।</small></span><span class="d">13:22 – 15:45</span></div>
 </div>
 <div class="lk1">हर देश की तारीखें, श्राद्ध का समय और विधि:</div>
 <div class="lk2">astroriver.com/hi/journal/pitru-paksha</div>
"""
def doc(w, h, top, bottom, extra_css, chip_top, tr_top, wm_top, river_ab, tag_xy, foot_b):
    return f"""<!doctype html><html lang="hi"><head><meta charset="utf-8"><style>{CSS}
html,body{{width:{w}px;height:{h}px}} .s{{width:{w}px;height:{h}px}} {extra_css}</style></head><body><div class="s">
<div class="wm" style="top:{wm_top}px">astroriver.com</div><div class="tr" style="top:{tr_top}px">astroriver.com</div>
<div class="chip" style="top:{chip_top}px">हिंदी</div>
<div class="flow" style="top:{top}px;bottom:{bottom}px">{content}</div>
<svg class="r" width="{w}" height="{h}">{river(*river_ab)}</svg>
<div class="tag" style="left:{tag_xy[0]}px;top:{tag_xy[1]}px">astroriver.com</div>
<div class="foot" style="bottom:{foot_b}px"><span class="n">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

feed = doc(1080, 1350, 100, 170, "h1{font-size:122px} .when{font-size:42px} .b{font-size:34px;margin-top:20px} .hd{margin-top:38px;font-size:27px} .row{padding:15px 0} .row .t{font-size:34px} .row .d{font-size:31px} .row.hot .d{font-size:36px} .lk1{margin-top:36px;font-size:29px} .lk2{font-size:31px}",
           48, 58, 560, (1212, 1196), (610, 1168), 56)
story = doc(1080, 1920, 170, 250, "h1{font-size:172px} .eb{font-size:36px} .when{font-size:52px} .b{font-size:43px;margin-top:34px} .hd{margin-top:60px;font-size:32px} .hd span{font-size:25px} .row{padding:26px 0} .row .t{font-size:44px} .row .t small{font-size:28px} .row .d{font-size:40px} .row.hot .d{font-size:46px} .lk1{margin-top:60px;font-size:36px} .lk2{font-size:38px}",
            80, 90, 820, (1742, 1728), (470, 1680), 90)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html, w, h in [('bharani-hi-post-1080x1350', feed, 1080, 1350), ('bharani-hi-status-1080x1920', story, 1080, 1920)]:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            fn = os.path.join(HERE, name + '.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(500)
            r = await pg.evaluate("() => { const d=document.querySelector('.flow'); const k=[...d.children]; return [Math.round(k[0].getBoundingClientRect().top), Math.round(k[k.length-1].getBoundingClientRect().bottom)] }")
            print(name, 'content spans', r)
            await pg.screenshot(path=os.path.join(HERE, 'out', name + '.png'))
        await b.close()
asyncio.run(main())
