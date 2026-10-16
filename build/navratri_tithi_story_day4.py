# Navratri 2026 midday Story: today's tithi and tomorrow's form (founder 11 Oct: plan approved).
# Tithi ends (Swiss Ephemeris, Lahiri; the end moment is the same everywhere, shown in IST):
#   Day 4: Chaturthi ends Thu 15 Oct 01:13 IST (Wednesday night); Panchami at Delhi sunrise Thu 15 Oct (Maa Skandamata).
import os, sys, asyncio
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
sys.path.insert(0, HERE); import navratri_day as N
W, H = 1080, 1920
EN = dict(eb='NAVRATRI · DAY 4 · WEDNESDAY 14 OCTOBER', k1='Today', v1='Chaturthi', s1='until 1:13 am IST, Thursday',
          k2='Tomorrow · Thursday 15 October', v2='Panchami', s2='Maa Skandamata', f="ASTRO RIVER", lang='en')
HI = dict(eb='नवरात्रि · चौथा दिन · बुधवार 14 अक्टूबर', k1='आज', v1='चतुर्थी', s1='रात 01:13 (IST) तक',
          k2='कल · गुरुवार 15 अक्टूबर', v2='पंचमी', s2='माँ स्कंदमाता', f="ASTRO RIVER", lang='hi')
def page(L):
    hi = L['lang'] == 'hi'
    big = "'NSR'" if hi else "'PFR'"; small = "'NSD'" if hi else "'IN'"
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'PFR';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-style:italic;font-weight:400 900}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700}}
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-600-normal.woff2');font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;overflow:hidden;background:radial-gradient(ellipse at 50% 38%,#7A1A1E,#4A0C12 55%,#1C0407);color:#FFF3DF;font-family:{small}}}
.c{{position:absolute;left:110px;right:110px;text-align:center}}
.eb{{top:420px;font:600 {30 if hi else 26}px {small};letter-spacing:{1 if hi else 5}px;color:#F2B544}}
.k{{margin-bottom:{26 if hi else 6}px;font:600 {34 if hi else 28}px {small};letter-spacing:{0 if hi else 4}px;color:#E9C79A;{'' if hi else 'text-transform:uppercase;'}}}
.v{{font:700 {150 if hi else 140}px/1.2 {big};color:#FFE3A3;text-shadow:0 0 40px rgba(255,190,90,.35)}}
.s{{font:{'600 46px' if hi else 'italic 500 46px'} {"'NSD'" if hi else "'PF'"};color:#FBE8C8}}
.rule{{width:220px;height:2px;margin:90px auto;background:linear-gradient(90deg,rgba(242,181,68,0),#F2B544,rgba(242,181,68,0))}}
.ft{{top:1760px;font:600 23px 'IN';letter-spacing:9px;color:#E9B24A}}
</style></head><body>
<svg width="{W}" height="300" style="position:absolute;left:0;top:0">{N.toran()}</svg>
<div class="c eb">{L['eb']}</div>
<div class="c" style="top:600px"><div class="k">{L['k1']}</div><div class="v">{L['v1']}</div><div class="s">{L['s1']}</div>
<div class="rule"></div><div class="k">{L['k2']}</div><div class="v">{L['v2']}</div><div class="s">{L['s2']}</div></div>
<div class="c ft">{L['f']}</div></body></html>"""
async def main(out):
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': W, 'height': H})
        for name, L in [('navratri-day4-tithi-story-en', EN), ('navratri-day4-tithi-story-hi', HI)]:
            fn = os.path.join(out, name + '.html'); open(fn, 'w').write(page(L))
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=os.path.join(out, name + '.png'))
        await b.close()
asyncio.run(main(sys.argv[1]))
