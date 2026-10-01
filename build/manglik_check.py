# Fri 2 Oct 2026, 13:00 IST: "Are you a Manglik?" The first checklist post (founder, 1 Oct: engaging, evergreen,
# something people save and check against their own chart). Topic chosen from OpenRush (India): "manglik dosha
# meaning" ~22,200/mo, "manglik dosha check" ~8,100, "how to check manglik dosha" ~1,300.
# Rules as the founder set them (1 Oct): Mars in the 1st, 4th, 7th, 8th or 12th house from the lagna (the 2nd house
# left out); the same count from the Moon is Chandra Manglik; Venus is not used. Exceptions named on the image: Mars
# in Aries or Scorpio (own sign), in Capricorn (exalted), both partners Manglik; "and more". Our article
# /journal/5th-7th-house-love-marriage carries the mangal dosha paragraph ("a chart is never judged by Mars alone").
# The AI astrologer lives at astroriver.com/lobby (the site's own "Ask an AI astrologer" link).
# The kundli is the North Indian diamond chart; the lagna is the top diamond, houses run anticlockwise.
import os, asyncio, math
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
BG, IV, MUT, SAF, SAF2, LINE, RIVER = '#F3EDE2', '#211B12', '#6B5B4B', '#A8590A', '#A8590A', '#DCCFBA', '#D77B09'
CARD_HOT, CARD = '#FBF1E3', '#F7F0E5'
RED, RED_FILL, RED_LINE = '#9C5048', '#F3D9CF', '#C98A7C'   # Mars red earth from the planet palette, softened for a tint
PREFIX = 'manglik-'
CSS = f"""
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900;}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700;}}
@font-face{{font-family:'LO';src:url('{F}Lora-Italic[wght].ttf');font-weight:400 700;font-style:italic;}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900;}}
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-600-normal.woff2');font-weight:600;}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:{BG};overflow:hidden}}
.s{{position:relative;z-index:0;background:{BG};color:{IV};font-family:'LO',serif}}
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



def mars_glyph(cx, cy, r):
    # the Mars symbol: a circle and an arrow to the upper right, inside a warm ring
    a = math.radians(-45); ex, ey = cx + r*0.70*math.cos(a), cy + r*0.70*math.sin(a)
    tip_x, tip_y = cx + r*1.30*math.cos(a), cy + r*1.30*math.sin(a)
    return (f'<circle cx="{cx}" cy="{cy}" r="{r*2.1}" fill="{RED_FILL}" opacity=".55"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*1.7}" fill="none" stroke="{SAF}" stroke-opacity=".35" stroke-width="1.5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*0.72}" fill="none" stroke="{RED}" stroke-width="{r*0.13:.1f}"/>'
            f'<line x1="{ex:.1f}" y1="{ey:.1f}" x2="{tip_x:.1f}" y2="{tip_y:.1f}" stroke="{RED}" stroke-width="{r*0.13:.1f}" stroke-linecap="round"/>'
            f'<path d="M{tip_x:.1f},{tip_y:.1f} l{-r*0.42:.1f},0 M{tip_x:.1f},{tip_y:.1f} l0,{r*0.42:.1f}" stroke="{RED}" stroke-width="{r*0.13:.1f}" stroke-linecap="round" fill="none"/>')

def kundli(x0, y0, S, shade=(1, 4, 7, 8, 12), fs=30):
    """North Indian chart. House 1 is the top diamond; houses run anticlockwise."""
    T, L, B, R, C = (S/2, 0), (0, S/2), (S/2, S), (S, S/2), (S/2, S/2)
    q1, q2, q3, q4 = (S/4, S/4), (S/4, 3*S/4), (3*S/4, 3*S/4), (3*S/4, S/4)
    polys = {1: [T, q1, C, q4], 2: [(0, 0), T, q1], 3: [(0, 0), L, q1], 4: [L, q1, C, q2], 5: [(0, S), L, q2], 6: [(0, S), B, q2],
             7: [B, q2, C, q3], 8: [(S, S), B, q3], 9: [(S, S), R, q3], 10: [R, q4, C, q3], 11: [(S, 0), R, q4], 12: [(S, 0), T, q4]}
    out = f'<g transform="translate({x0} {y0})">'
    for h, pts in polys.items():
        d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + ' Z'
        hot = h in shade
        out += f'<path d="{d}" fill="{RED_FILL if hot else "#FBF8F2"}" stroke="{RED if hot else "#8C7254"}" stroke-width="{3 if hot else 1.6}" stroke-opacity="{1 if hot else .55}"/>'
    # labels at each house's centre
    for h, pts in polys.items():
        cx = sum(p[0] for p in pts) / len(pts); cy = sum(p[1] for p in pts) / len(pts)
        if len(pts) == 3:   # pull the triangle labels a little toward the corner so they sit in the open part
            kx, ky = pts[0]; cx, cy = cx*0.72 + kx*0.28, cy*0.72 + ky*0.28
        hot = h in shade
        out += (f'<text x="{cx:.1f}" y="{cy + fs*0.36:.1f}" text-anchor="middle" font-family="PF" font-weight="700" font-size="{fs}" fill="{RED if hot else "#8C7254"}">{h}</text>')
    # the lagna mark
    out += f'<text x="{S/2:.1f}" y="{S/4 + fs*1.25:.1f}" text-anchor="middle" font-family="IN" font-weight="600" font-size="{fs*0.5:.0f}" letter-spacing="2" fill="{RED}">LAGNA</text>'
    out += f'<rect x="0" y="0" width="{S}" height="{S}" fill="none" stroke="#8C7254" stroke-width="2.2"/></g>'
    return out

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
def houses(items, big=False):
    s = ''
    for n, name, what in items:
        s += (f'<div class="pt" style="gap:26px;padding:{22 if big else 19}px 0;align-items:flex-start">'
              f'<span style="font:700 {46 if big else 40}px PF;color:{RED};min-width:{74 if big else 64}px;line-height:1">{n}</span>'
              f'<span><div style="font:700 {34 if big else 31}px PF;color:{IV}">{name}</div><div style="font:400 {28 if big else 26}px/1.4 LO;color:{MUT};margin-top:3px">{what}</div></span></div>')
    return s
FIVE = [('1', 'The 1st house', 'Your body, your temper.'), ('4', 'The 4th house', 'Home, peace of mind.'), ('7', 'The 7th house', 'Marriage, the partner.'),
        ('8', 'The 8th house', 'The length of the marriage.'), ('12', 'The 12th house', 'The bed, private life.')]

HEAD = 'Are you a <em>Manglik</em>?'
SUB = 'Does your Mars build, or burn? Check your own&nbsp;chart.'
LINK2 = 'astroriver.com/journal/5th-7th-house-love-marriage'
slides = []
slides.append(page(W, H, f"""
<div class="flow" style="top:560px;bottom:220px;justify-content:flex-start">
 <div class="eb">Check your own chart</div>
 <h1 style="font-size:112px;margin-top:18px">{HEAD}</h1>
 <div class="b" style="font-size:36px;margin-top:26px">{SUB}</div>
 <div class="m" style="margin-top:20px;font-size:29px;color:{SAF}">Swipe &#8594;</div>
</div>""", sr(0), TAGS[0], 40, 700, 56, mars_glyph(540, 290, 110)))

slides.append(page(W, H, f"""
<div class="flow" style="top:96px;bottom:200px;justify-content:flex-start">
 <div class="eb">1 · Find your Mars</div>
 <h2 style="font-size:60px">Is Mars in a red&nbsp;box?</h2>
 <div class="b" style="font-size:29px;margin-top:14px">Open your kundli. Mars is written <b style="font-weight:700">Ma</b>, or <b style="font-family:NSD;font-weight:600">मं</b> in Hindi. If it sits in one of the five red houses, that is mangal&nbsp;dosha.</div>
 <div style="height:490px"></div>
 <div class="m" style="font-size:25px">Then do the same from your Moon: the house your Moon is in counts as 1. Mars in a red box from there is <b style="font-weight:600;color:{IV}">Chandra Manglik</b>, read with the same&nbsp;weight.</div>
 <div class="m" style="font-size:22px;margin-top:12px">North Indian chart. In a South Indian chart the lagna is marked As, and the houses run&nbsp;clockwise.</div>
</div>
<svg class="r" width="{W}" height="{H}">{kundli(310, 318, 460)}</svg>""", sr(1), TAGS[1], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">2 · Why these five</div>
 <h2>Here, Mars doesn&#8217;t build.<br>It&nbsp;burns.</h2>
 <div class="b" style="font-size:29px;margin-top:18px">Mars is action and energy. In these five houses that energy lands on the marriage&nbsp;itself.</div>
 <div style="margin-top:22px">{houses(FIVE)}</div>
</div>""", sr(2), TAGS[2], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">3 · Found it? Breathe.</div>
 <h2>Exceptions apply,<br>and there are&nbsp;many.</h2>
 <div style="margin-top:34px">{pts([('&#8212;', 'Mars at home, in Aries or&nbsp;Scorpio.'), ('&#8212;', 'Mars at its strongest, in&nbsp;Capricorn.'), ('&#8212;', 'Both partners Manglik: the fire meets its&nbsp;match.'), ('&#8212;', 'And more, read from the whole&nbsp;chart.')])}</div>
 <div class="b" style="font-size:31px;margin-top:32px">A chart is never judged by Mars alone. Most people who were told they are Manglik were never told about the&nbsp;exceptions.</div>
 <div class="link1" style="margin-top:28px">Love, marriage and the houses that decide them:</div>
 <div class="link2" style="font-size:26px">{LINK2}</div>
</div>""", sr(3), TAGS[3], 58, 560, 56))

opt = lambda t, sub, hot: (f'<div style="border:{"2.5px solid "+SAF if hot else "1.5px solid "+LINE};background:{CARD_HOT if hot else CARD};border-radius:18px;padding:24px 30px;margin-top:16px">'
                           f'<div style="font:700 {38 if hot else 33}px PF;color:{IV}">{t}</div><div style="font:400 27px/1.45 LO;color:{MUT};margin-top:6px">{sub}</div></div>')
slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">4 · Not sure where your Mars is?</div>
 <h2 style="font-size:64px">Ask. It takes<br>a&nbsp;minute.</h2>
 <div style="margin-top:14px">
  {opt("Ask our AI astrologer", "Give it your birth date, time and place and ask: am I Manglik? It reads your real chart, shows you where your Mars sits, and which exceptions apply. Any time, day or&nbsp;night.", True)}
 </div>
 <div class="link2" style="font-size:30px;margin-top:14px">astroriver.com/lobby</div>
 <div style="margin-top:30px">
  {opt("A private consultation", "The whole chart, read live by audio call or&nbsp;chat.", False)}
 </div>
 <div style="margin-top:26px;font:500 25px 'IN';letter-spacing:3px;color:{MUT}">ON WHATSAPP</div>
 <div style="margin-top:6px;font:700 44px 'IN';color:{SAF2};letter-spacing:.5px">+91 70091 27641</div>
</div>""", sr(4), TAGS[4], 58, 560, 56))

story = page(1080, 1920, f"""
<div class="flow" style="top:600px;bottom:250px;justify-content:flex-start">
 <div class="eb" style="font-size:25px">Check your own chart</div>
 <h1 style="font-size:124px;margin-top:22px">{HEAD}</h1>
 <div class="b" style="font-size:40px;margin-top:30px">{SUB}</div>
 <div class="b" style="font-size:32px;margin-top:36px;color:{MUT}">Mars in the 1st, 4th, 7th, 8th or 12th house from the lagna is mangal dosha. Exceptions apply, and there are&nbsp;many.</div>
 <div style="height:400px"></div>
 <div class="link1" style="font-size:30px">Not sure where your Mars is? Ask our AI astrologer:</div>
 <div class="link2" style="font-size:31px">astroriver.com/lobby</div>
</div>
<svg class="r" width="1080" height="1920">{mars_glyph(540, 330, 115)}{kundli(370, 1232, 340, fs=24)}</svg>""", river(1742, 1728, 1716, True, True), (470, 1680), 90, 980, 90)

x = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
html,body{{width:1600px;height:900px}} .s{{width:1600px;height:900px}}</style></head><body><div class="s">
<div class="wm" style="top:330px;left:260px">astroriver.com</div><div class="tr" style="top:52px">astroriver.com</div>
<svg class="r" width="1600" height="900">{kundli(1010, 130, 470, fs=28)}</svg>
<div class="flow" style="top:100px;bottom:190px;right:720px">
 <div class="eb" style="font-size:19px">Check your own chart</div>
 <h1 style="font-size:92px;margin-top:18px">{HEAD}</h1>
 <div class="b" style="font-size:30px;margin-top:22px">{SUB}</div>
 <div class="b" style="font-size:25px;margin-top:22px;color:{MUT}">Mars in a red house is mangal dosha. Exceptions apply, and there are&nbsp;many.</div>
 <div class="link2" style="font-size:24px;margin-top:22px">astroriver.com/lobby</div>
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
