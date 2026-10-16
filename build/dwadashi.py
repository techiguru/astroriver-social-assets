# Wed 7 Oct 2026 morning: Dwadashi shradh, Story + WhatsApp Status only (day events are Stories, founder 4 Oct), in
# English and Hindi, plus an X image. Same dress as ekadashi.py. Facts computed this session (Swiss Ephemeris, Lahiri)
# and matching the live article table (/journal/pitru-paksha: Dwadashi Wed 7 Oct in India, UK, Australia; Tue 6 Oct in
# the USA and Canada, starred on the East coast):
#   Krishna Dwadashi tithi: Wed 7 Oct 00:35 IST -> Wed 7 Oct 23:17 IST.
#   Delhi Wed 7 Oct aparahna 13:18-15:39 IST (article table): Dwadashi covers all of it.
#   Indira Ekadashi was kept on Tue 6 Oct; the fast is broken on Wednesday morning after sunrise.
import os, asyncio
from playwright.async_api import async_playwright
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_shared.py')).read())
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)

EXTRA = """
.flow{position:absolute;left:100px;right:100px;display:flex;flex-direction:column;justify-content:center}
.tr2{display:grid;grid-template-columns:1.5fr 1fr;align-items:baseline;padding:24px 0;border-top:1.5px solid #DCCFBA}
.tr2.hd{border-top:0;padding:0 0 14px}
.tr2.hd span{font:600 19px 'IN';letter-spacing:2.5px;color:var(--mut);text-transform:uppercase}
.tr2 span:nth-child(2){text-align:right}
.tr2 .p{font:500 31px 'LO'}
.tr2 .d{font:600 28px 'IN';color:var(--saf2);letter-spacing:.3px}
.tr2 .d small{display:block;font:500 20px 'IN';color:var(--mut);letter-spacing:.2px;margin-top:4px}
.tr2.last{border-bottom:1.5px solid #DCCFBA}
.tr2.hot{background:#FBF1E3;margin:0 -18px;padding-left:18px;padding-right:18px}
.note{font:400 26px/1.45 'LO';color:var(--mut)}
"""

def table(L):
    rows = L["rows"]
    s = f'<div class="tr2 hd"><span>{L["where"]}</span><span>{L["col"]}</span></div>'
    for k, (place, d, sub, hot) in enumerate(rows):
        cls = 'tr2' + (' hot' if hot else '') + (' last' if k == len(rows) - 1 else '')
        sm = f'<small>{sub}</small>' if sub else ''
        s += f'<div class="{cls}"><span class="p">{place}</span><span class="d">{d}{sm}</span></div>'
    return f'<div>{s}</div>'

EN = dict(
    eb='Pitru Paksha 2026 · Wednesday 7 October',
    head='Today is <em>Dwadashi&nbsp;shradh</em>.',
    body='The Dwadashi tithi began at 00:35 IST, just after midnight, and runs until 23:17 tonight. The shradh for those who passed on a Dwadashi is done this&nbsp;afternoon.',
    where='Where', col='Dwadashi shradh',
    rows=[("India, Dubai, Singapore", "Wed 7 Oct", "", True), ("UK", "Wed 7 Oct", "", False),
          ("USA, Canada", "Tue 6 Oct", "Already yesterday there", False), ("Australia", "Wed 7 Oct", "", False)],
    delhi='Shradh hours in Delhi today: <b style="color:#211B12;font-weight:600">13:18 – 15:39</b>, the&nbsp;aparahna.',
    indira='Kept the <b style="color:#211B12;font-weight:600">Indira Ekadashi</b> fast yesterday? It is broken this morning, after&nbsp;sunrise.',
    more='The hours for your city:', link='astroriver.com/journal/pitru-paksha')
HI = dict(
    eb='पितृ पक्ष 2026 · बुधवार 7 अक्टूबर',
    head='आज द्वादशी का <em>श्राद्ध</em>&nbsp;है।',
    body='द्वादशी तिथि आधी रात के बाद 00:35 बजे (IST) शुरू हुई और आज रात 23:17 बजे तक रहेगी। जिनका देहांत द्वादशी को हुआ था, उनका श्राद्ध आज दोपहर किया जाता&nbsp;है।',
    where='कहां', col='द्वादशी श्राद्ध',
    rows=[("भारत, दुबई, सिंगापुर", "बुधवार 7 अक्टूबर", "", True), ("ब्रिटेन", "बुधवार 7 अक्टूबर", "", False),
          ("अमेरिका, कनाडा", "मंगलवार 6 अक्टूबर", "वहां यह कल था", False), ("ऑस्ट्रेलिया", "बुधवार 7 अक्टूबर", "", False)],
    delhi='दिल्ली में आज श्राद्ध का समय: <b style="color:#211B12;font-weight:600">13:18 – 15:39</b>,&nbsp;अपराह्न।',
    indira='कल <b style="color:#211B12;font-weight:600">इंदिरा एकादशी</b> का व्रत रखा था? आज सुबह सूर्योदय के बाद व्रत खोलें।',
    more='अपने शहर का समय:', link='astroriver.com/hi/journal/pitru-paksha')
HINDI_CSS = f"""
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-400-normal.woff2');font-weight:400;}}
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-600-normal.woff2');font-weight:600;}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700;}}
h1{{font-family:'NSR' !important;line-height:1.3 !important}} em{{font-style:normal !important}}
.b,.note,.m{{font-family:'NSD' !important;line-height:1.6 !important}} .eb{{font-family:'NSD' !important;letter-spacing:0 !important}}
.tr2 .p{{font-family:'NSD' !important;font-weight:600 !important}} .tr2 .d{{font-family:'NSD' !important}} .tr2.hd span{{font-family:'NSD' !important;letter-spacing:0 !important}}
"""

def block(sz, L):
    return f"""
 <div class="eb" style="font-size:{sz['eb']}px">{L['eb']}</div>
 <h1 style="font-size:{sz['h1']}px;margin-top:{sz['g1']}px">{L['head']}</h1>
 <div class="b" style="font-size:{sz['b']}px;margin-top:{sz['g2']}px">{L['body']}</div>
 <div style="margin-top:{sz['g3']}px">{table(L)}</div>
 <div class="note" style="font-size:{sz['n']}px;margin-top:{sz['g4']}px;color:#211B12">{L['delhi']}</div>
 <div class="note" style="font-size:{sz['n2']}px;margin-top:14px">{L['indira']}</div>
 <div class="m" style="font-size:{sz['n']}px;margin-top:{sz['g5']}px">{L['more']}</div>
 <div class="link" style="font-size:{sz['lk']}px;margin-top:4px">{L['link']}</div>"""

ST_SZ = dict(eb=25, h1=96, g1=26, b=36, g2=30, g3=46, n=31, n2=29, g4=36, g5=40, lk=34)
def story(L, css=''):
    return page(1080, 1920, f'<div class="flow" style="top:230px;bottom:250px">{block(ST_SZ, L)}</div>',
             river_path(1742, 1728, 1716, True, True), (470, 1680), 90, 820, 90).replace(
             '</style>', EXTRA + ".tr2{padding:32px 0} .tr2.hot{padding-left:18px;padding-right:18px} .tr2.hd{padding:0 0 16px} .tr2 .p{font-size:36px} .tr2 .d{font-size:32px} .tr2 .d small{font-size:23px} .tr2.hd span{font-size:22px}" + css + "</style>", 1)

XW, XH = 1600, 900
def river_x(a, b):
    mid = (a + b) / 2 - 14
    p = f"M100,{a} C420,{a+12} 560,{mid} 800,{mid} C1060,{mid} 1200,{b} 1495,{b}"
    q = f"M100,{a+14} C420,{a+26} 560,{mid+18} 800,{mid+18} C1060,{mid+18} 1200,{b+14} 1495,{b+14}"
    return (f'<path d="{q}" fill="none" stroke="#E2D7C4" stroke-width="3"/><path d="{p}" fill="none" stroke="#D77B09" stroke-width="4.5" stroke-linecap="round"/>'
            f'<circle cx="100" cy="{a}" r="9" fill="#D77B09"/><circle cx="1495" cy="{b}" r="20" fill="none" stroke="#D77B09" stroke-width="3"/><circle cx="1495" cy="{b}" r="8" fill="#D77B09"/>')
x = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{EXTRA}
html,body{{width:{XW}px;height:{XH}px}} .s{{width:{XW}px;height:{XH}px}}
.tr2{{padding:18px 0}} .tr2.hot{{padding-left:18px;padding-right:18px}} .tr2.hd{{padding:0 0 12px}} .tr2 .p{{font-size:27px}} .tr2 .d{{font-size:25px}} .tr2 .d small{{font-size:18px}} .tr2.hd span{{font-size:17px}}</style></head><body><div class="s">
<div class="wm" style="top:330px;left:260px">astroriver.com</div><div class="tr" style="top:52px">astroriver.com</div>
<div style="position:absolute;left:100px;right:100px;top:100px;bottom:190px;display:flex;align-items:center;gap:64px">
 <div style="flex:1">
  <div class="eb" style="font-size:19px">Pitru Paksha 2026</div>
  <h1 style="font-size:66px;margin-top:18px">{EN['head']}</h1>
  <div class="b" style="font-size:26px;margin-top:20px">The Dwadashi tithi began at 00:35 IST and runs through the whole&nbsp;afternoon.</div>
  <div class="m" style="font-size:24px;margin-top:22px">The hours for your city:</div>
  <div class="link" style="margin-top:2px;font-size:27px">astroriver.com/journal/pitru-paksha</div>
 </div>
 <div style="flex:1.05">{table(EN)}
  <div class="note" style="font-size:23px;margin-top:20px;color:#211B12">{EN['delhi']}</div>
 </div>
</div>
<svg class="r" width="{XW}" height="{XH}">{river_x(794, 782)}</svg>
<div class="tag" style="left:700px;top:746px">astroriver.com</div>
<div class="foot" style="bottom:26px"><span class="n" style="font-size:32px">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

async def main():
    jobs = [('dwadashi-status-1080x1920', story(EN), 1080, 1920), ('dwadashi-status-hi-1080x1920', story(HI, HINDI_CSS), 1080, 1920),
            ('dwadashi-x-1600x900', x, XW, XH)]
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html, w, h in jobs:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            fn = os.path.join(HERE, name + '.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            r = await pg.evaluate("() => { const d=document.querySelector('.flow'); if(!d) return null; const k=[...d.children]; return [Math.round(k[0].getBoundingClientRect().top), Math.round(k[k.length-1].getBoundingClientRect().bottom)] }")
            print(name, 'content spans', r)
            await pg.screenshot(path=os.path.join(HERE, 'out', name + '.png'))
        await b.close()
asyncio.run(main())
