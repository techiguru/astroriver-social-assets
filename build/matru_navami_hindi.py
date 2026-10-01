# Sun 4 Oct 2026: Matru Navami in Hindi (founder: "matru navami should get a hindi version"; he approves every word
# before it goes out). Ivory Pitru Paksha dress + हिंदी label, the site's Pitru Paksha drawing on the cover.
# Every Hindi line is copied from the approved page content/source/journal-pitru-paksha-2026-hi.md (site repo):
#   l.117 "मातृ नवमी (अविधवा नवमी) — रविवार 4 अक्टूबर।" / "नवमी का श्राद्ध माताओं के लिए, और उन सौभाग्यवती स्त्रियों
#   के लिए किया जाता है जिनका देहांत पति के जीवित रहते हुआ।"
#   l.88 Delhi row "4 अक्टू. | 11:46–12:33 | 12:33–13:20 | 13:20–15:41"; "मुख्य अर्पण इसी समय किया जाता है।"
#   l.130 "दक्षिण दिशा की ओर मुख करें — यह पितरों की दिशा है। काले तिल मिला जल अर्पित करें, हो सके तो कुशा के साथ"
#   l.131 "ॐ पितृभ्यः स्वधा नमः"
#   Link line "हर देश की तारीखें, श्राद्ध का समय और विधि:" as on the 27 and 29 Sep Hindi posts.
import os, asyncio
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
ART = 'file://' + os.path.join(HERE, 'art-journal-pitru-tarpan.svg')
art = lambda top, w=1080, left=0: f'<img src="{ART}" style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{w*388/800:.0f}px;z-index:-1">'
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
.s{{position:relative;z-index:0;background:#F3EDE2;color:#211B12;font-family:'NSD',serif}}
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


COVER = """
 <div class="eb">पितृ पक्ष 2026</div>
 <h1>मातृ नवमी</h1>
 <div class="when">रविवार 4 अक्टूबर।</div>
 <div class="b">नवमी का श्राद्ध माताओं के लिए, और उन सौभाग्यवती स्त्रियों के लिए किया जाता है जिनका देहांत पति के जीवित रहते हुआ।</div>
"""
TIMES = """
 <div class="hd" style="margin-top:0">श्राद्ध का समय · <span>दिल्ली, IST</span></div>
 <div style="margin-top:12px">
  <div class="row"><span class="t">कुतुप</span><span class="d">11:46 – 12:33</span></div>
  <div class="row"><span class="t">रौहिण</span><span class="d">12:33 – 13:20</span></div>
  <div class="row hot"><span class="t">अपराह्न<small>मुख्य अर्पण इसी समय किया जाता है।</small></span><span class="d">13:20 – 15:41</span></div>
 </div>
"""
TARPAN = """
 <div class="hd">तर्पण</div>
 <div class="b" style="margin-top:8px">दक्षिण दिशा की ओर मुख करें — यह पितरों की दिशा है। काले तिल मिला जल अर्पित करें, हो सके तो कुशा के साथ।</div>
 <div class="when" style="margin-top:14px">ॐ पितृभ्यः स्वधा नमः</div>
"""
LINK = """
 <div class="lk1">हर देश की तारीखें, श्राद्ध का समय और विधि:</div>
 <div class="lk2">astroriver.com/hi/journal/pitru-paksha</div>
"""
def river2(a, b, start_dot, end_ring):
    # a carousel's river: slide 1 starts with the dot and runs off the right edge; slide 2 comes in from the left edge
    xs = 100 if start_dot else 0
    xe = 975 if end_ring else 1080
    mid = (a + b) / 2 - 18
    p = f"M{xs},{a} C{xs+200},{a+10} 360,{mid} 540,{mid} C720,{mid} 820,{b} {xe},{b}"
    q = f"M{xs},{a+16} C{xs+200},{a+26} 360,{mid+20} 540,{mid+20} C720,{mid+20} 820,{b+16} {xe},{b+16}"
    e = f'<circle cx="100" cy="{a}" r="9" fill="#D77B09"/>' if start_dot else ''
    if end_ring:
        e += f'<circle cx="975" cy="{b}" r="22" fill="none" stroke="#D77B09" stroke-width="3"/><circle cx="975" cy="{b}" r="9" fill="#D77B09"/>'
    return f'<path d="{q}" fill="none" stroke="#E2D7C4" stroke-width="3"/><path d="{p}" fill="none" stroke="#D77B09" stroke-width="4.5" stroke-linecap="round"/>{e}'

def doc(w, h, content, top, bottom, extra_css, chip_top, tr_top, wm_top, river_ab, tag_xy, foot_b, pic=''):
    return f"""<!doctype html><html lang="hi"><head><meta charset="utf-8"><style>{CSS}
html,body{{width:{w}px;height:{h}px}} .s{{width:{w}px;height:{h}px}} {extra_css}</style></head><body><div class="s">
{pic}
<div class="wm" style="top:{wm_top}px">astroriver.com</div><div class="tr" style="top:{tr_top}px">astroriver.com</div>
<div class="chip" style="top:{chip_top}px">हिंदी</div>
<div class="flow" style="top:{top}px;bottom:{bottom}px">{content}</div>
<svg class="r" width="{w}" height="{h}">{river2(*river_ab) if len(river_ab) == 4 else river(*river_ab)}</svg>
<div class="tag" style="left:{tag_xy[0]}px;top:{tag_xy[1]}px">astroriver.com</div>
<div class="foot" style="bottom:{foot_b}px"><span class="n">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

FEED_CSS = "h1{font-size:118px} .when{font-size:42px} .b{font-size:34px;margin-top:18px} .hd{margin-top:40px;font-size:28px} .row{padding:15px 0} .row .t{font-size:34px} .row .d{font-size:31px} .row.hot .d{font-size:36px} .lk1{margin-top:40px;font-size:29px} .lk2{font-size:31px}"
cover = doc(1080, 1350, COVER + '<div style="font:400 44px IN;color:#A8590A;margin-top:18px">&#8594;</div>', 600, 220, FEED_CSS + " .flow{justify-content:flex-start}",
            48, 58, 700, (1212, 1178, True, False), (640, 1150), 56, art(20))
inner = doc(1080, 1350, TIMES + TARPAN + LINK, 110, 210, FEED_CSS, 48, 58, 560, (1178, 1196, False, True), (620, 1162), 56)
TIMES_SHORT = TIMES.replace('margin-top:0', 'margin-top:40px').replace('  <div class="row"><span class="t">कुतुप</span><span class="d">11:46 – 12:33</span></div>\n', '').replace('  <div class="row"><span class="t">रौहिण</span><span class="d">12:33 – 13:20</span></div>\n', '')
story = doc(1080, 1920, COVER + TIMES_SHORT + LINK, 760, 250,
            "h1{font-size:150px} .eb{font-size:34px} .when{font-size:50px} .b{font-size:40px;margin-top:24px} .hd{font-size:31px} .hd span{font-size:24px} .row{padding:20px 0} .row .t{font-size:40px} .row .t small{font-size:26px} .row .d{font-size:37px} .row.hot .d{font-size:42px} .lk1{margin-top:44px;font-size:34px} .lk2{font-size:36px}",
            80, 90, 980, (1742, 1728), (470, 1680), 90, art(150))

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html, w, h in [('matru-navami-hi-slide-1-of-2', cover, 1080, 1350), ('matru-navami-hi-slide-2-of-2', inner, 1080, 1350),
                                 ('matru-navami-hi-status-1080x1920', story, 1080, 1920)]:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            fn = os.path.join(HERE, name + '.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(500)
            r = await pg.evaluate("() => { const d=document.querySelector('.flow'); const k=[...d.children]; return [Math.round(k[0].getBoundingClientRect().top), Math.round(k[k.length-1].getBoundingClientRect().bottom)] }")
            print(name, 'content spans', r)
            await pg.screenshot(path=os.path.join(HERE, 'out', name + '.png'))
        await b.close()
asyncio.run(main())
