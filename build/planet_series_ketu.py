# Planet Series #2 — Ketu: "Why does the one beside you feel so far away?" Pair to the Rahu post of 29 Sep.
# Redrawn 1 Oct 2026 in Ketu's colour from the locked planet palette (planet_palette.py): smoke. The cover is
# the palette's smoke ground; the inner slides, status and X image use its one-step-deeper smoke so the small
# text reads. Layout, words and the mirrored eclipse are unchanged from the approved dark version.
# Astrology lines follow live pages: /journal/5th-7th-house-love-marriage ("Ketu there brings detachment,
# the partner who is spiritually present and materially absent, or the marriage that ends in withdrawal
# rather than conflict"; Venus colours every relationship reading; the navamsa is the chart of marriage);
# /journal/outer-planets-jyotish (Rahu and Ketu are the Moon's nodes, where eclipses happen);
# /journal/what-a-dasha-is (Ketu dasha 7 years); /nakshatra/ashwini, /nakshatra/mula (Ketu the tail, the
# past already lived; keeps a part back; the loss that turns out to be a release). Founder approves first.
import os, asyncio
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
exec(open(os.path.join(HERE, 'planet_palette.py')).read())
_n, _s, _t, _tone, GROUND, DEEP, IV, ACC = PALETTE['ketu']
BG, MUT, SAF, SAF2, LINE, RIVER = DEEP, '#E2DBD0', ACC, ACC, '#86817B', '#D77B09'
CARD_HOT, CARD = '#5C5853', '#64605B'
CSS = f"""
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900;}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700;}}
@font-face{{font-family:'LO';src:url('{F}Lora-Italic[wght].ttf');font-weight:400 700;font-style:italic;}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900;}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:{BG};overflow:hidden}}
.s{{position:relative;background:{BG};color:{IV};font-family:'LO',serif}}
.tr{{position:absolute;right:102px;font:500 21px 'IN';letter-spacing:2.5px;color:{MUT}}}
.wm{{position:absolute;left:70px;font:italic 400 176px 'PF';color:{IV};opacity:.07;transform:rotate(-13deg);transform-origin:left top;white-space:nowrap}}
.flow{{position:absolute;left:100px;right:100px;display:flex;flex-direction:column;justify-content:center}}
.eb{{font:600 22px 'IN';letter-spacing:5px;color:{SAF};text-transform:uppercase}}
h1{{font:700 96px/1.06 'PF';letter-spacing:-.5px;margin-top:24px}}
h2{{font:700 70px/1.08 'PF';letter-spacing:-.3px;margin-top:22px}}
em{{font-style:italic;color:{SAF2};font-weight:600}}
.b{{font:400 34px/1.5 'LO';margin-top:28px;color:{IV}}}
.m{{font:400 30px/1.5 'LO';color:{MUT}}}
.pt{{display:flex;gap:24px;align-items:baseline;padding:22px 0;border-top:1.5px solid {LINE}}}
.pt:last-child{{border-bottom:1.5px solid {LINE}}}
.pt .k{{font:700 30px 'PF';color:{SAF};min-width:30px}}
.pt .v{{font:400 33px/1.4 'LO'}}
.link1{{font:400 28px 'LO';color:{MUT}}}
.link2{{font:600 29px 'IN';color:{SAF2};letter-spacing:.2px;margin-top:4px}}
.foot{{position:absolute;left:100px;right:102px;display:flex;justify-content:space-between;align-items:baseline}}
.foot .n{{font:italic 500 36px 'PF';color:{IV}}} .foot .u{{font:500 23px 'IN';letter-spacing:2.5px;color:{MUT}}}
svg.r{{position:absolute;left:0;top:0}}
.tag{{position:absolute;font:600 17px 'IN';letter-spacing:2.5px;color:{SAF};background:{BG};padding:0 10px}}
"""
def river(a, b, mid, start_dot, end_ring, W=1080):
    xs = 100 if start_dot else 0
    xe = W - 105 if end_ring else W
    m = W / 2
    p = f"M{xs},{a} C{xs+200},{a+14} {m-180},{mid} {m},{mid} C{m+180},{mid} {m+280},{b} {xe},{b}"
    q = f"M{xs},{a+16} C{xs+200},{a+30} {m-180},{mid+20} {m},{mid+20} C{m+180},{mid+20} {m+280},{b+16} {xe},{b+16}"
    extra = f'<circle cx="100" cy="{a}" r="9" fill="{RIVER}"/>' if start_dot else ''
    if end_ring:
        extra += f'<circle cx="{xe}" cy="{b}" r="22" fill="none" stroke="{RIVER}" stroke-width="3"/><circle cx="{xe}" cy="{b}" r="9" fill="{RIVER}"/>'
    return f'<path d="{q}" fill="none" stroke="{LINE}" stroke-width="3"/><path d="{p}" fill="none" stroke="{RIVER}" stroke-width="4.5" stroke-linecap="round"/>{extra}'

def eclipse(cx, cy, r):
    # Ketu: the same eclipse seen from its other end; the bright edge on the upper left, as the shadow moves off
    return (f'<defs><radialGradient id="g" cx="50%" cy="50%" r="50%"><stop offset="55%" stop-color="{SAF}" stop-opacity=".55"/>'
            f'<stop offset="100%" stop-color="{SAF}" stop-opacity="0"/></radialGradient></defs>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*1.75}" fill="url(#g)" opacity=".55"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SAF}"/>'
            f'<circle cx="{cx + r*0.16}" cy="{cy + r*0.10}" r="{r*0.985}" fill="{BG}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*1.28}" fill="none" stroke="{SAF}" stroke-opacity=".35" stroke-width="1.5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*1.55}" fill="none" stroke="{SAF}" stroke-opacity=".18" stroke-width="1.5"/>'
            + ring_text(cx, cy, r*1.415, max(13, r*0.115)))

def ring_text(cx, cy, R, fs):
    import math
    L = 2 * math.pi * R
    pid = f'ring{int(cx)}{int(cy)}'
    unit = 'ASTRORIVER.COM\u2003\u00b7\u2003'
    return (f'<defs><path id="{pid}" d="M{cx-R},{cy} a{R},{R} 0 1,1 {2*R},0 a{R},{R} 0 1,1 {-2*R},0"/></defs>'
            f'<text font-family="IN" font-weight="600" font-size="{fs:.1f}" fill="{SAF}" fill-opacity=".55">'
            f'<textPath href="#{pid}" textLength="{L-2:.1f}" lengthAdjust="spacing">{unit*4}</textPath></text>')

def page(w, h, body, river_svg, tag_xy, tr_top, wm_top, foot_b, art=''):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
html,body{{width:{w}px;height:{h}px}} .s{{width:{w}px;height:{h}px}}</style></head><body><div class="s">
<div class="wm" style="top:{wm_top}px">astroriver.com</div><div class="tr" style="top:{tr_top}px">astroriver.com</div>
<svg class="r" width="{w}" height="{h}">{art}</svg>
{body}
<svg class="r" width="{w}" height="{h}">{river_svg}</svg>
<div class="tag" style="left:{tag_xy[0]}px;top:{tag_xy[1]}px">astroriver.com</div>
<div class="foot" style="bottom:{foot_b}px"><span class="n">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

W, H, N = 1080, 1350, 5
Y = [1212, 1178, 1204, 1172, 1206, 1196]
def sr(i):
    a, b = Y[i], Y[i+1]
    return river(a, b, (a+b)/2 + (16 if i % 2 else -16), i == 0, i == N-1)
TAGS = [(640, 1150), (560, 1148), (700, 1150), (600, 1150), (620, 1162)]
FL = 'top:110px;bottom:210px'
pts = lambda items: ''.join(f'<div class="pt"><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in items)

HEAD = 'Why does the one beside you feel so <em>far&nbsp;away</em>?'
SUB = 'Sometimes it is distance. Sometimes it&nbsp;is&nbsp;Ketu.'
LINK1, LINK2 = 'Love, marriage and Ketu in the 7th house:', 'astroriver.com/journal/5th-7th-house-love-marriage'
slides = []
slides.append(page(W, H, f"""
<div class="flow" style="top:510px;bottom:220px;justify-content:flex-start">
 <div class="eb">The planet series · Ketu</div>
 <h1 style="font-size:98px">{HEAD}</h1>
 <div class="b" style="font-size:38px;margin-top:34px">{SUB}</div>
 <div class="m" style="margin-top:22px;font-size:29px;color:{SAF}">Swipe &#8594;</div>
</div>""", sr(0), TAGS[0], 58, 560, 56, eclipse(800, 290, 124)))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">1 · What Ketu is</div>
 <h2>Ketu is letting go.</h2>
 <div class="b">Ketu cannot be seen. Like Rahu, it is a point where the Moon&#8217;s path crosses the Sun&#8217;s, where eclipses happen: the tail of the eclipse. In Jyotish it is the past already&nbsp;lived.</div>
 <div style="margin-top:40px">{pts([('1', 'Rahu reaches for more. Ketu lets&nbsp;go.'), ('2', 'It keeps a part of the self held back, quietly.'), ('3', 'What it takes away often turns out to be a&nbsp;release.')])}</div>
</div>""", sr(1), TAGS[1], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">2 · How it feels</div>
 <h2>When Ketu sits<br>in the marriage.</h2>
 <div style="margin-top:36px">{pts([('&#8212;', 'A partner who is spiritually present and materially&nbsp;absent.'), ('&#8212;', 'Kind, loyal, and somehow always a little&nbsp;elsewhere.'), ('&#8212;', 'No big fight. The distance grows&nbsp;quietly.'), ('&#8212;', 'Where the bond strains, it thins through withdrawal, not&nbsp;quarrels.')])}</div>
 <div class="m" style="margin-top:30px;font-size:27px">In the chart: Ketu in the 7th house, or a Ketu dasha running. Venus, the karaka of marriage, is always read beside&nbsp;it.</div>
</div>""", sr(2), TAGS[2], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">3 · What helps</div>
 <h2>Distance is not<br>the end of love.</h2>
 <div style="margin-top:36px">{pts([('1', 'Don&#8217;t read quiet as rejection. Ketu withdraws; it does not&nbsp;attack.'), ('2', 'Ask for presence in plain ways: time, words, attention.'), ('3', 'Check your timing. A Ketu dasha runs seven years, and then it&nbsp;ends.')])}</div>
 <div class="m" style="margin-top:28px;font-size:27px">One planet never decides a marriage. The 7th lord, Venus and the navamsa are read&nbsp;together.</div>
 <div class="link1" style="margin-top:30px">{LINK1}</div>
 <div class="link2">{LINK2}</div>
</div>""", sr(3), TAGS[3], 58, 560, 56))

opt = lambda t, sub, hot: (f'<div style="border:{"2.5px solid "+SAF if hot else "1.5px solid "+LINE};background:{CARD_HOT if hot else CARD};border-radius:18px;padding:24px 30px;margin-top:16px">'
                           f'<div style="font:700 {38 if hot else 33}px PF;color:{IV}">{t}</div><div style="font:400 27px/1.45 LO;color:{MUT};margin-top:6px">{sub}</div></div>')
slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">4 · Your own chart</div>
 <h2 style="font-size:66px">Is it Ketu,<br>or is it <em>us</em>?</h2>
 <div class="m" style="margin-top:18px;font-size:29px">Only your chart can say. Three ways to get your answer:</div>
 <div style="margin-top:10px">
  {opt("A written report", "Your 5th and 7th houses, Venus, the navamsa and the dasha, read against your own&nbsp;chart.", True)}
  {opt("A private consultation", "Live, by audio call or chat.", False)}
  {opt("Ask an AI astrologer", "Online at astroriver.com, any time.", False)}
 </div>
 <div style="margin-top:32px;font:500 25px 'IN';letter-spacing:3px;color:{MUT}">REPORT OR CONSULTATION, ON WHATSAPP</div>
 <div style="margin-top:6px;font:700 44px 'IN';color:{SAF2};letter-spacing:.5px">+91 70091 27641</div>
</div>""", sr(4), TAGS[4], 58, 560, 56))

slides[0] = slides[0].replace(BG, GROUND)

# WhatsApp status / Pinterest, 1080x1920
story = page(1080, 1920, f"""
<div class="flow" style="top:560px;bottom:250px">
 <div class="eb" style="font-size:25px">The planet series · Ketu</div>
 <h1 style="font-size:108px">{HEAD}</h1>
 <div class="b" style="font-size:42px;margin-top:34px">{SUB}</div>
 <div style="margin-top:44px">{pts([('&#8212;', 'A partner who is spiritually present and materially&nbsp;absent.'), ('&#8212;', 'No big fight. The distance grows&nbsp;quietly.'), ('&#8212;', 'A Ketu dasha runs seven years, and then it&nbsp;ends.')])}</div>
 <div class="link1" style="margin-top:44px;font-size:32px">{LINK1}</div>
 <div class="link2" style="font-size:31px">{LINK2}</div>
</div>""", river(1742, 1728, 1716, True, True), (470, 1680), 90, 820, 90, eclipse(790, 330, 120))

# X, 1600x900
x = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
html,body{{width:1600px;height:900px}} .s{{width:1600px;height:900px}}</style></head><body><div class="s">
<div class="wm" style="top:330px;left:260px">astroriver.com</div><div class="tr" style="top:52px">astroriver.com</div>
<svg class="r" width="1600" height="900">{eclipse(1250, 380, 150)}</svg>
<div class="flow" style="top:100px;bottom:190px;right:620px">
 <div class="eb" style="font-size:21px">The planet series · Ketu</div>
 <h1 style="font-size:80px">{HEAD}</h1>
 <div class="b" style="font-size:34px;margin-top:26px">{SUB}</div>
 <div class="link1" style="margin-top:30px;font-size:26px">{LINK1}</div>
 <div class="link2" style="font-size:27px">{LINK2}</div>
</div>
<svg class="r" width="1600" height="900">{river(794, 782, 774, True, True, 1600)}</svg>
<div class="tag" style="left:700px;top:746px">astroriver.com</div>
<div class="foot" style="bottom:26px"><span class="n" style="font-size:32px">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

async def main():
    jobs = [(f'ketu-slide-{i+1}-of-{N}', s, W, H) for i, s in enumerate(slides)]
    jobs += [('ketu-status-1080x1920', story, 1080, 1920), ('ketu-x-1600x900', x, 1600, 900)]
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html, w, h in jobs:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            fn = os.path.join(HERE, name + '.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            r = await pg.evaluate("() => { const d=document.querySelector('.flow'); const k=[...d.children]; return [Math.round(k[0].getBoundingClientRect().top), Math.round(k[k.length-1].getBoundingClientRect().bottom)] }")
            print(name, r)
            await pg.screenshot(path=os.path.join(HERE, 'out', name + '.png'))
        await b.close()
asyncio.run(main())
