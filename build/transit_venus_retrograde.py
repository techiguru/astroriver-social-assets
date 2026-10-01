# Fri 2 Oct 2026 evening: Venus turns retrograde (transit series: sand ground, the chip names the kind of
# transit). Dates computed this session (Swiss Ephemeris, Lahiri) and matching the live article
# /journal/venus-retrograde-2026:
#   Station retrograde Sat 3 Oct 12:43 IST (07:13 UTC) at 14 deg 15' Libra, in Swati.
#   Combust (within 8 deg of the Sun) 19 Oct 08:29 -> 29 Oct 10:29 IST.  Into Virgo 6 Nov 01:29 IST.
#   Station direct Sat 14 Nov 05:59 IST at 28 deg 37' Virgo.  Back into Libra 22 Nov.  Shadow ends 16 Dec.
#   3 Oct station abroad (article): London 08:13, New York/Toronto 03:13, Pacific 00:13, Sydney 17:13.
# Words for "what to delay / what still works" follow the article. Rewritten 1 Oct for plain readers (founder: followers
# are simple people, not astrologers) and for search (OpenRush, India: "venus retrograde 2026" ~880/mo, "shukra asta 2026"
# ~1,300/mo, "venus retrograde meaning" ~210/mo): no degrees, nakshatra or 'combust/debilitation' on the images. Founder approves before posting.
import os, asyncio, math
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
BG, IV, MUT, SAF, SAF2, LINE, RIVER = '#EADFCB', '#211B12', '#6B5B4B', '#A8590A', '#A8590A', '#D3C2A6', '#D77B09'
GROUND = BG
CARD_HOT, CARD = '#F4ECDF', '#EFE5D3'
PREFIX = 'venus-'
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
.wm{{position:absolute;left:70px;font:italic 400 176px 'PF';color:{IV};opacity:.045;transform:rotate(-13deg);transform-origin:left top;white-space:nowrap}}
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


def chip(text, size):
    return (f'<div style="display:inline-block;align-self:flex-start;font:700 {size}px \'IN\';letter-spacing:4px;color:#FFF8EE;'
            f'background:#A8590A;border-radius:999px;padding:11px 24px 10px">{text}</div>')

def loop_art(ox, oy, sc=1.0, labels=True):
    """Venus's retrograde loop, drawn to scale in longitude (30 px a degree, 172-200 deg sidereal)."""
    X = lambda lon: 120 + (lon - 172) * 30
    xR, xD, xB, c1, c2, cj = X(194.26), X(178.63), X(180), X(189.5), X(183.5), X(186.52)
    yU, yM, yL = 175, 300, 425
    t = lambda x, y: f'{ox + x*sc:.1f},{oy + y*sc:.1f}'
    s = ''
    # the sign line: Virgo | Libra
    s += f'<line x1="{ox+xB*sc}" y1="{oy+95*sc}" x2="{ox+xB*sc}" y2="{oy+468*sc}" stroke="#8C7254" stroke-opacity=".55" stroke-width="1.6" stroke-dasharray="6 7"/>'
    s += f'<text x="{ox+(xB-14)*sc}" y="{oy+492*sc}" text-anchor="end" font-family="IN" font-weight="700" font-size="{17*sc:.1f}" letter-spacing="3" fill="#8C7254">VIRGO</text>'
    s += f'<text x="{ox+(xB+14)*sc}" y="{oy+492*sc}" font-family="IN" font-weight="700" font-size="{17*sc:.1f}" letter-spacing="3" fill="#8C7254">LIBRA</text>'
    # the path: forward, turn back at R, back past the Sun, turn forward at D, forward again
    fwd1 = f'M{t(110, yU+18)} C{t(400, yU)} {t(640, yU-6)} {t(xR, yU)}'
    hairR = f'C{t(xR+70, yU+4)} {t(xR+70, yM-4)} {t(xR, yM)}'
    back = f'L{t(xD, yM)}'
    hairD = f'C{t(xD-70, yM+4)} {t(xD-70, yL-4)} {t(xD, yL)}'
    fwd2 = f'C{t(560, yL+6)} {t(800, yL)} {t(965, yL-14)}'
    s += f'<path d="{fwd1} {hairR} {back} {hairD} {fwd2}" fill="none" stroke="#D77B09" stroke-width="{4*sc:.1f}" stroke-linecap="round"/>'
    # combust stretch: the path fades into the Sun's light
    s += f'<line x1="{ox+c1*sc}" y1="{oy+yM*sc}" x2="{ox+c2*sc}" y2="{oy+yM*sc}" stroke="#EADFCB" stroke-width="{7*sc:.1f}"/>'
    s += f'<line x1="{ox+c1*sc}" y1="{oy+yM*sc}" x2="{ox+c2*sc}" y2="{oy+yM*sc}" stroke="#D77B09" stroke-opacity=".35" stroke-width="{4*sc:.1f}" stroke-dasharray="{3*sc:.1f} {7*sc:.1f}" stroke-linecap="round"/>'
    sx, sy, sr = ox + cj*sc, oy + (yM-62)*sc, 20*sc
    rays = ''.join(f'<line x1="{sx+math.cos(a)*sr*1.35:.1f}" y1="{sy+math.sin(a)*sr*1.35:.1f}" x2="{sx+math.cos(a)*sr*1.85:.1f}" y2="{sy+math.sin(a)*sr*1.85:.1f}" stroke="#D77B09" stroke-width="{2.4*sc:.1f}" stroke-linecap="round"/>' for a in [k*math.pi/6 for k in range(12)])
    s += f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr:.1f}" fill="#F7C46A" stroke="#D77B09" stroke-width="{2*sc:.1f}"/>{rays}'
    # arrows on each leg
    def arrow(x, y, d):
        x, y = ox + x*sc, oy + y*sc; a = 11*sc
        return f'<path d="M{x-d*a:.1f},{y-a*.75:.1f} L{x+d*a:.1f},{y:.1f} L{x-d*a:.1f},{y+a*.75:.1f} Z" fill="#D77B09"/>'
    s += arrow(470, yU-3, 1) + arrow(370 + 0, yM, -1) + arrow(650, yL+2, 1)
    # Venus at the turning point, and the turn forward
    vx, vy = ox + (xR+52)*sc, oy + ((yU+yM)/2)*sc
    s += f'<circle cx="{vx:.1f}" cy="{vy:.1f}" r="{17*sc:.1f}" fill="#FBF6EE" stroke="#A8590A" stroke-width="{3*sc:.1f}"/>'
    dx, dy = ox + (xD-52)*sc, oy + ((yM+yL)/2)*sc
    s += f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="{8*sc:.1f}" fill="#A8590A"/>'
    if labels:
        f1, f2 = 17*sc, 21*sc
        s += (f'<text x="{ox+(xR+40)*sc:.1f}" y="{oy+(yU-50)*sc:.1f}" text-anchor="end" font-family="IN" font-weight="700" font-size="{f1:.1f}" letter-spacing="2.5" fill="#A8590A">3 OCT · TURNS BACK</text>'
              f'<text x="{ox+(xR+40)*sc:.1f}" y="{oy+(yU-24)*sc:.1f}" text-anchor="end" font-family="LO" font-size="{f2:.1f}" fill="#6B5B4B">in Libra</text>')
        s += (f'<text x="{ox+110*sc:.1f}" y="{oy+(yM+50)*sc:.1f}" font-family="IN" font-weight="700" font-size="{f1:.1f}" letter-spacing="2.5" fill="#A8590A">14 NOV</text>'
              f'<text x="{ox+110*sc:.1f}" y="{oy+(yM+74)*sc:.1f}" font-family="IN" font-weight="700" font-size="{f1:.1f}" letter-spacing="2.5" fill="#A8590A">TURNS</text>'
              f'<text x="{ox+110*sc:.1f}" y="{oy+(yM+98)*sc:.1f}" font-family="IN" font-weight="700" font-size="{f1:.1f}" letter-spacing="2.5" fill="#A8590A">FORWARD</text>'
              f'<text x="{ox+110*sc:.1f}" y="{oy+(yM+124)*sc:.1f}" font-family="LO" font-size="{f2:.1f}" fill="#6B5B4B">in Virgo</text>')
        s += (f'<text x="{sx:.1f}" y="{oy+(yM+40)*sc:.1f}" text-anchor="middle" font-family="IN" font-weight="700" font-size="{f1:.1f}" letter-spacing="2.5" fill="#A8590A">19–29 OCT</text>'
              f'<text x="{sx:.1f}" y="{oy+(yM+64)*sc:.1f}" text-anchor="middle" font-family="LO" font-size="{f2:.1f}" fill="#6B5B4B">Shukra asta</text>')
    return s

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
rows = lambda items: ''.join(f'<div class="pt" style="gap:28px"><span class="k" style="font:700 26px IN;min-width:190px;letter-spacing:.3px">{k}</span><span class="v" style="font-size:31px">{v}</span></div>' for k, v in items)

HEAD = 'Venus turns back on <em>3&nbsp;October</em>.'
SUB = 'Saturday, 12:43 IST. For six weeks Venus seems to move backwards in the sky: a time to review, not&nbsp;to&nbsp;begin.'
LINK1, LINK2 = 'What it means for you, sign by sign:', 'astroriver.com/journal/venus-retrograde-2026'
slides = []
slides.append(page(W, H, f"""
<div class="flow" style="top:600px;bottom:220px;justify-content:flex-start">
 {chip('VENUS RETROGRADE 2026', 22)}
 <h1 style="font-size:84px;margin-top:22px">{HEAD}</h1>
 <div class="b" style="font-size:34px;margin-top:24px">{SUB}</div>
 <div class="m" style="margin-top:20px;font-size:29px;color:{SAF}">Swipe &#8594;</div>
</div>""", sr(0), TAGS[0], 40, 700, 56, loop_art(0, 40)))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">1 · The path</div>
 <h2>Six weeks,<br>step by step.</h2>
 <div style="margin-top:36px">{rows([('3 Oct, 12:43', 'Turns back, in&nbsp;Libra.'), ('19–29 Oct', '<b style="font-weight:600">Shukra asta</b>: hidden in the Sun’s light. No&nbsp;weddings.'), ('6 Nov', 'Into Virgo, where Venus is at its&nbsp;weakest.'), ('14 Nov, 05:59', 'Starts moving forward&nbsp;again.'), ('22 Nov', 'Back in Libra. All&nbsp;clear.')])}</div>
 <div class="m" style="margin-top:26px;font-size:25px">Times in IST. Western astrology says Scorpio; it is the same event. On 3&nbsp;October it is 08:13 in London, 03:13 in New York and 17:13 in&nbsp;Sydney.</div>
</div>""", sr(1), TAGS[1], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">2 · What to hold off on</div>
 <h2>Wait while the<br>light is wrong.</h2>
 <div style="margin-top:36px">{pts([('&#8212;', 'A marriage date fixed only because it “feels&nbsp;right”.'), ('&#8212;', 'Luxury bought for status rather than&nbsp;use.'), ('&#8212;', 'Launching something that depends on people liking&nbsp;it.'), ('&#8212;', 'Signing a deal on trust, without reading the&nbsp;terms.')])}</div>
 <div class="m" style="margin-top:28px;font-size:27px">For anything that matters, wait until Venus is out of Virgo on 22&nbsp;November.</div>
</div>""", sr(2), TAGS[2], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">3 · What still works</div>
 <h2>Retrogrades give<br>things back.</h2>
 <div style="margin-top:36px">{pts([('1', 'Keeping promises already&nbsp;made.'), ('2', 'Repairing a relationship without announcing&nbsp;it.'), ('3', 'Saving money&nbsp;quietly.'), ('4', 'Going back to a person, a project or a purchase you left too&nbsp;fast.')])}</div>
 <div class="link1" style="margin-top:34px">{LINK1}</div>
 <div class="link2">{LINK2}</div>
</div>""", sr(3), TAGS[3], 58, 560, 56))

opt = lambda t, sub, hot: (f'<div style="border:{"2.5px solid "+SAF if hot else "1.5px solid "+LINE};background:{CARD_HOT if hot else CARD};border-radius:18px;padding:24px 30px;margin-top:16px">'
                           f'<div style="font:700 {38 if hot else 33}px PF;color:{IV}">{t}</div><div style="font:400 27px/1.45 LO;color:{MUT};margin-top:6px">{sub}</div></div>')
slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">4 · Your own chart</div>
 <h2 style="font-size:66px">Where does it fall<br><em>for you</em>?</h2>
 <div class="m" style="margin-top:18px;font-size:29px">It depends on your own birth chart. Three ways to get your&nbsp;answer:</div>
 <div style="margin-top:10px">
  {opt("A written report", "Venus’s six weeks, read against your own&nbsp;chart.", True)}
  {opt("A private consultation", "Live, by audio call or chat.", False)}
  {opt("Ask an AI astrologer", "Online at astroriver.com, any time.", False)}
 </div>
 <div style="margin-top:32px;font:500 25px 'IN';letter-spacing:3px;color:{MUT}">REPORT OR CONSULTATION, ON WHATSAPP</div>
 <div style="margin-top:6px;font:700 44px 'IN';color:{SAF2};letter-spacing:.5px">+91 70091 27641</div>
</div>""", sr(4), TAGS[4], 58, 560, 56))

# WhatsApp status / Pinterest, 1080x1920
story = page(1080, 1920, f"""
<div class="flow" style="top:800px;bottom:250px;justify-content:flex-start">
 {chip('VENUS RETROGRADE 2026', 26)}
 <h1 style="font-size:100px;margin-top:26px">{HEAD}</h1>
 <div class="b" style="font-size:40px;margin-top:30px">{SUB}</div>
 <div style="margin-top:40px">{rows([('19–29 Oct', 'Shukra asta. No&nbsp;weddings.'), ('14 Nov', 'Starts moving forward&nbsp;again.')])}</div>
 <div class="link1" style="margin-top:40px;font-size:32px">{LINK1}</div>
 <div class="link2" style="font-size:31px">{LINK2}</div>
</div>""", river(1742, 1728, 1716, True, True), (470, 1680), 90, 980, 90, loop_art(0, 170, 1.0))

# X, 1600x900
x = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
html,body{{width:1600px;height:900px}} .s{{width:1600px;height:900px}}</style></head><body><div class="s">
<div class="wm" style="top:330px;left:260px">astroriver.com</div><div class="tr" style="top:52px">astroriver.com</div>
<svg class="r" width="1600" height="900">{loop_art(740, 100, 0.78)}</svg>
<div class="flow" style="top:100px;bottom:190px;right:900px">
 {chip('VENUS RETROGRADE 2026', 19)}
 <h1 style="font-size:72px;margin-top:20px">{HEAD}</h1>
 <div class="b" style="font-size:29px;margin-top:22px">{SUB}</div>
 <div class="link1" style="margin-top:26px;font-size:25px">{LINK1}</div>
 <div class="link2" style="font-size:25px">{LINK2}</div>
</div>
<svg class="r" width="1600" height="900">{river(794, 782, 774, True, True, 1600)}</svg>
<div class="tag" style="left:700px;top:746px">astroriver.com</div>
<div class="foot" style="bottom:26px"><span class="n" style="font-size:32px">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

async def main():
    jobs = [(f'{PREFIX}slide-{i+1}-of-{N}', s, W, H) for i, s in enumerate(slides)]
    jobs += [(f'{PREFIX}status-1080x1920', story, 1080, 1920), (f'{PREFIX}x-1600x900', x, 1600, 900)]
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
