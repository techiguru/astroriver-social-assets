# Mon 5 Oct 2026, 19:30 IST: pitra dosh. Founder 5 Oct: not a check-your-chart post; tell people what forms it and
# what it brings, with authority; show both North and South Indian charts; a real Reel. (First draft was a checklist.)
# Topic from search data (India, monthly): "pitra dosh" 6,600; "pitra dosh kya hota hai" 6,600; "pitra dosh ke upay"
# 3,600; "what is pitra dosh" 2,400; "pitra dosh ke lakshan" 2,400 (14,800 in Pitru Paksha 2025).
# Rules (founder, 4-5 Oct: four steps from our article, then "research online and decide"):
#   Our article /journal/pitru-paksha: seen in the 9th house (father, lineage) and the Sun, when Rahu, Ketu or Saturn
#   press on them; "a chart condition is not a curse, and it is not read from one placement"; the Institute arranges
#   tarpan, shradh and pitru dosh puja in the family's name.
#   Common readings online (checked 4-5 Oct): Saturn's aspect on the Sun counts; an afflicted 9th lord counts; eased by
#   Jupiter with the Sun or aspecting the 9th, the Sun in Aries or Leo, a strong 9th lord. Self-check = sitting
#   together; aspect and 9th lord = what an astrologer reads (founder: a little technical points people to a reading).
# Spelling (founder 5 Oct, from search data): "pitru dosha" in English, matching Pitru Paksha and South Indian
# readers; the caption carries "pitra dosh" for the 6,600 Hindi-speaking searches. Hindi goes in the Reel (पितृ दोष).
# Look: ivory, with shades of the Sun's terracotta from the locked palette (the Sun is the father's planet).
import os, asyncio, math
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
BG, IV, MUT, SAF, SAF2, LINE, RIVER = '#F3EDE2', '#211B12', '#6B5B4B', '#A8590A', '#A8590A', '#DCCFBA', '#D77B09'
CARD_HOT, CARD = '#FBF1E3', '#F7F0E5'
RED, RED_FILL, RED_LINE = '#9C5048', '#F3D9CF', '#C98A7C'   # defaults, overridden below by the Sun's terracotta
KFILL, KLINE, KTEXT, KHOT_FILL, KHOT_LINE, KHOT_TEXT, WM_OP = '#FBF8F2', '#8C7254', '#8C7254', RED_FILL, RED, RED, '.045'
GLYPH_RING, GLYPH = RED_FILL, RED

_t = '#9A543C'   # Sun terracotta, deep (locked palette); 5.6:1 on ivory, carries small text
SAF, SAF2, MUT, LINE = _t, _t, '#6E554B', '#E6D2C6'
CARD_HOT, CARD = '#F8E7DD', '#F7F0E5'
RED, RED_FILL = _t, '#EDCDBE'
KFILL, KLINE, KTEXT, KHOT_FILL, KHOT_LINE, KHOT_TEXT, WM_OP = '#FBF8F2', '#A98A7E', '#8C6E62', RED_FILL, _t, '#7A3A26', '.045'
GLYPH_RING, GLYPH = '#F1DCD0', _t
PREFIX = 'pitra-dosh-'
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
.wm{{position:absolute;left:70px;font:italic 400 176px 'PF';color:{IV};opacity:{WM_OP};transform:rotate(-13deg);transform-origin:left top;white-space:nowrap}}
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
    return (f'<circle cx="{cx}" cy="{cy}" r="{r*2.1}" fill="{GLYPH_RING}" opacity=".55"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*1.7}" fill="none" stroke="{SAF}" stroke-opacity=".35" stroke-width="1.5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*0.72}" fill="none" stroke="{GLYPH}" stroke-width="{r*0.13:.1f}"/>'
            f'<line x1="{ex:.1f}" y1="{ey:.1f}" x2="{tip_x:.1f}" y2="{tip_y:.1f}" stroke="{GLYPH}" stroke-width="{r*0.13:.1f}" stroke-linecap="round"/>'
            f'<path d="M{tip_x:.1f},{tip_y:.1f} l{-r*0.42:.1f},0 M{tip_x:.1f},{tip_y:.1f} l0,{r*0.42:.1f}" stroke="{GLYPH}" stroke-width="{r*0.13:.1f}" stroke-linecap="round" fill="none"/>')

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
        out += f'<path d="{d}" fill="{KHOT_FILL if hot else KFILL}" stroke="{KHOT_LINE if hot else KLINE}" stroke-width="{3 if hot else 1.6}" stroke-opacity="{1 if hot else .55}"/>'
    # labels at each house's centre
    for h, pts in polys.items():
        cx = sum(p[0] for p in pts) / len(pts); cy = sum(p[1] for p in pts) / len(pts)
        if len(pts) == 3:   # pull the triangle labels a little toward the corner so they sit in the open part
            kx, ky = pts[0]; cx, cy = cx*0.72 + kx*0.28, cy*0.72 + ky*0.28
        hot = h in shade
        out += (f'<text x="{cx:.1f}" y="{cy + fs*0.36:.1f}" text-anchor="middle" font-family="PF" font-weight="700" font-size="{fs}" fill="{KHOT_TEXT if hot else KTEXT}">{h}</text>')
    # the lagna mark
    out += f'<text x="{S/2:.1f}" y="{S/4 + fs*1.25:.1f}" text-anchor="middle" font-family="IN" font-weight="600" font-size="{fs*0.5:.0f}" letter-spacing="2" fill="{KHOT_TEXT}">LAGNA</text>'
    out += f'<rect x="0" y="0" width="{S}" height="{S}" fill="none" stroke="{KLINE}" stroke-width="2.2"/></g>'
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

W, H, N = 1080, 1350, 7
Y = [1212, 1178, 1204, 1172, 1206, 1180, 1200, 1188]
def sr(i):
    a, b = Y[i], Y[i+1]
    return river(a, b, (a+b)/2 + (16 if i % 2 else -16), i == 0, i == N-1)
TAGS = [(640, 1150), (560, 1148), (700, 1150), (600, 1150), (620, 1162), (660, 1150), (600, 1156)]
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

def sun_glyph(cx, cy, r):
    # the Sun's symbol: a circle with a point at its centre, inside the same soft ring as the Mars post
    return (f'<circle cx="{cx}" cy="{cy}" r="{r*2.1}" fill="{GLYPH_RING}" opacity=".7"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*1.7}" fill="none" stroke="{SAF}" stroke-opacity=".35" stroke-width="1.5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*0.78}" fill="none" stroke="{GLYPH}" stroke-width="{r*0.13:.1f}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*0.15:.1f}" fill="{GLYPH}"/>')


def eclipse(cx, cy, r):
    # the Sun eclipsed: the tradition's picture of the Sun with Rahu (grahan)
    return (f'<circle cx="{cx}" cy="{cy}" r="{r*2.05}" fill="{GLYPH_RING}" opacity=".7"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*1.68}" fill="none" stroke="{SAF}" stroke-opacity=".3" stroke-width="1.5"/>'
            + ''.join(f'<line x1="{cx + r*1.12*math.cos(math.radians(a)):.1f}" y1="{cy + r*1.12*math.sin(math.radians(a)):.1f}" '
                      f'x2="{cx + r*1.42*math.cos(math.radians(a)):.1f}" y2="{cy + r*1.42*math.sin(math.radians(a)):.1f}" '
                      f'stroke="{SAF}" stroke-width="{r*0.07:.1f}" stroke-linecap="round" opacity=".55"/>' for a in range(0, 360, 30))
            + f'<circle cx="{cx}" cy="{cy}" r="{r*0.92}" fill="{SAF}"/>'
            f'<circle cx="{cx + r*0.55:.1f}" cy="{cy - r*0.18:.1f}" r="{r*0.86:.1f}" fill="#2A221C"/>')

SIGNS_CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1)]  # Pisces .. Aquarius, clockwise
def south_kundli(x0, y0, S, lagna=1, shade=(5, 9), fs=26):
    """South Indian chart: the signs keep their boxes; houses are counted clockwise from the lagna's box
    (here the example lagna is Aries, the second box of the top row)."""
    c = S / 4
    out = f'<g transform="translate({x0} {y0})">'
    for h in range(1, 13):
        cx, cy = SIGNS_CELLS[(lagna + h - 1) % 12]
        hot = h in shade
        out += f'<rect x="{cx*c:.1f}" y="{cy*c:.1f}" width="{c:.1f}" height="{c:.1f}" fill="{KHOT_FILL if hot else KFILL}" stroke="{KHOT_LINE if hot else KLINE}" stroke-width="{3 if hot else 1.6}" stroke-opacity="{1 if hot else .55}"/>'
    for h in range(1, 13):
        cx, cy = SIGNS_CELLS[(lagna + h - 1) % 12]
        hot = h in shade
        out += f'<text x="{cx*c + c/2:.1f}" y="{cy*c + c/2 + fs*0.36:.1f}" text-anchor="middle" font-family="PF" font-weight="700" font-size="{fs}" fill="{KHOT_TEXT if hot else KTEXT}">{h}</text>'
    lx, ly = SIGNS_CELLS[lagna]
    out += f'<line x1="{lx*c+4:.1f}" y1="{ly*c+4:.1f}" x2="{lx*c+c*0.34:.1f}" y2="{ly*c+c*0.34:.1f}" stroke="{KHOT_TEXT}" stroke-width="2"/>'
    out += f'<text x="{lx*c + c/2:.1f}" y="{ly*c + c*0.86:.1f}" text-anchor="middle" font-family="IN" font-weight="600" font-size="{fs*0.46:.0f}" letter-spacing="1.5" fill="{KHOT_TEXT}">LAGNA</text>'
    out += f'<rect x="0" y="0" width="{S}" height="{S}" fill="none" stroke="{KLINE}" stroke-width="2.2"/>'
    out += f'<rect x="{c:.1f}" y="{c:.1f}" width="{2*c:.1f}" height="{2*c:.1f}" fill="{BG}" stroke="{KLINE}" stroke-width="1.6" stroke-opacity=".55"/></g>'
    return out

FIVE_NINE = (5, 9)
HEAD = 'Is <em>pitru dosha</em><br>blocking your&nbsp;bhagya?'
SUB = 'Not the anger of the ancestors, as many fear. A debt the family line still carries, and one that can be&nbsp;eased.'
tile = lambda k, t, d: (f'<div style="flex:1;border:1.5px solid {LINE};background:{CARD};border-radius:16px;padding:22px 20px">'
                        f'<div style="font:700 34px PF;color:{SAF}">{k}</div><div style="font:700 26px PF;color:{IV};margin-top:8px">{t}</div>'
                        f'<div style="font:400 23px/1.4 LO;color:{MUT};margin-top:6px">{d}</div></div>')
slides = []
slides.append(page(W, H, f"""
<div class="flow" style="top:600px;bottom:220px;justify-content:flex-start">
 <div class="eb">Pitru Paksha 2026 · Pitru dosha</div>
 <h1 style="font-size:80px;margin-top:18px">{HEAD}</h1>
 <div class="b" style="font-size:31px;margin-top:22px">{SUB}</div>
 <div class="m" style="margin-top:18px;font-size:29px;color:{SAF}">Swipe &#8594;</div>
</div>""", sr(0), TAGS[0], 40, 700, 56, eclipse(540, 290, 110)))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">1 · What it is</div>
 <h2>A debt to the ancestors, still&nbsp;unpaid.</h2>
 <div class="b" style="font-size:31px;margin-top:20px">The tradition calls it <i>pitru rin</i>. When rites are left undone, or a family line carries an old wrong, the next generation feels it as fortune that will not&nbsp;open.</div>
 <div class="b" style="font-size:29px;margin-top:26px;color:{MUT}">In the birth chart, it shows in three&nbsp;places:</div>
 <div style="display:flex;gap:16px;margin-top:20px">{tile('☉', 'The Sun', 'Your father, your soul.')}{tile('9', 'The 9th house', 'Bhagya, your father, your lineage.')}{tile('5', 'The 5th house', 'Past merit, your children.')}</div>
</div>""", sr(1), TAGS[1], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="top:96px;bottom:226px;justify-content:center">
 <div class="eb">2 · Where to look</div>
 <h2 style="font-size:60px">The 5th and 9th houses, in either&nbsp;chart.</h2>
 <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-top:30px">
  <div style="width:400px"><svg width="400" height="400">{kundli(2, 2, 396, shade=FIVE_NINE, fs=28)}</svg>
   <div style="font:700 26px PF;margin-top:16px">North Indian</div><div class="m" style="font-size:23px;line-height:1.4;margin-top:4px">The boxes are houses. The top diamond is always house&nbsp;1.</div></div>
  <div style="width:400px"><svg width="400" height="400">{south_kundli(2, 2, 396, fs=28)}</svg>
   <div style="font:700 26px PF;margin-top:16px">South Indian</div><div class="m" style="font-size:23px;line-height:1.4;margin-top:4px">The boxes are signs. Count clockwise from your lagna (here,&nbsp;Aries).</div></div>
 </div>
 <div class="b" style="font-size:28px;margin-top:30px">Check your own chart, or ask our AI astrologer at astroriver.com, any&nbsp;time.</div>
</div>""", sr(2), TAGS[2], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">3 · What forms it</div>
 <h2>The combinations the tradition looks&nbsp;for.</h2>
 <div style="margin-top:26px">{pts([('1', 'The Sun with Rahu, Ketu or Saturn: the Sun eclipsed, <i>grahan</i>.'), ('2', 'Rahu, Ketu or Saturn in the 9th&nbsp;house.'), ('3', 'The 9th lord weak, or pressed by Rahu, Ketu or&nbsp;Saturn.'), ('4', 'Rahu or Ketu in the 5th house, or a troubled 5th&nbsp;lord.'), ('5', 'Saturn&#8217;s glance on the Sun. And&nbsp;more.')])}</div>
</div>""", sr(3), TAGS[3], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">4 · What it can bring</div>
 <h2>Effort that does not turn into&nbsp;fortune.</h2>
 <div style="margin-top:26px">{pts([('&#8212;', 'Work that stalls just before it&nbsp;succeeds.'), ('&#8212;', 'A marriage delayed, despite every&nbsp;effort.'), ('&#8212;', 'Delay, or worry, around&nbsp;children.'), ('&#8212;', 'Money that comes, and does not&nbsp;stay.'), ('&#8212;', 'Unrest at home that never quite&nbsp;ends.')])}</div>
 <div class="b" style="font-size:29px;margin-top:28px;color:{MUT}">Many things can cause these. That is why the whole chart is read, never one&nbsp;placement.</div>
</div>""", sr(4), TAGS[4], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">5 · Found it? Breathe.</div>
 <h2>Exceptions apply,<br>and there are&nbsp;many.</h2>
 <div style="margin-top:34px">{pts([('&#8212;', 'Jupiter with your Sun, or looking at your 9th&nbsp;house.'), ('&#8212;', 'Your Sun strong, in Aries or&nbsp;Leo.'), ('&#8212;', 'A strong 9th&nbsp;lord.'), ('&#8212;', 'And more, read from the whole&nbsp;chart.')])}</div>
 <div class="b" style="font-size:31px;margin-top:32px">Pitru dosha is not a curse. It is a debt, and a debt can be&nbsp;paid.</div>
</div>""", sr(5), TAGS[5], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">6 · What the tradition does</div>
 <h2 style="font-size:58px">Tarpan, shradh, pinda daan, pitru dosha&nbsp;puja.</h2>
 <div class="b" style="font-size:30px;margin-top:20px">And a meal given in their name, with portions set aside for a crow, a cow and a&nbsp;dog.</div>
 <div class="b" style="font-size:30px;margin-top:18px">The time is now. Pitru Paksha ends on Saturday 10 October, Sarva Pitru&nbsp;Amavasya.</div>
 <div class="b" style="font-size:30px;margin-top:18px;color:{MUT}">No priest nearby, or the family far apart? The Institute arranges tarpan, shradh and pitru dosha puja in your family&#8217;s&nbsp;name.</div>
 <div style="margin-top:30px;font:500 25px 'IN';letter-spacing:3px;color:{MUT}">CONNECT ON WHATSAPP</div>
 <div style="margin-top:8px;font:700 50px 'IN';color:{SAF2};letter-spacing:.5px">+91 70091 27641</div>
</div>""", sr(6), TAGS[6] if len(TAGS) > 6 else TAGS[5], 58, 560, 56))

story = page(1080, 1920, f"""
<div class="flow" style="top:620px;bottom:250px;justify-content:flex-start">
 <div class="eb" style="font-size:25px">Pitru Paksha 2026 · Pitru dosha</div>
 <h1 style="font-size:100px;margin-top:22px">{HEAD}</h1>
 <div class="b" style="font-size:38px;margin-top:30px">{SUB}</div>
 <div class="b" style="font-size:32px;margin-top:34px;color:{MUT}">What forms it, what it can bring, and what the tradition does, before Pitru Paksha ends on Saturday 10&nbsp;October.</div>
 <div style="flex:1"></div>
 <div class="link1" style="font-size:30px">Read it here:</div>
 <div class="link2" style="font-size:31px">astroriver.com/journal/pitru-paksha</div>
</div>
<svg class="r" width="1080" height="1920">{eclipse(540, 330, 115)}</svg>""", river(1742, 1728, 1716, True, True), (470, 1680), 90, 980, 90)

x = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
html,body{{width:1600px;height:900px}} .s{{width:1600px;height:900px}}</style></head><body><div class="s">
<div class="wm" style="top:330px;left:260px">astroriver.com</div><div class="tr" style="top:52px">astroriver.com</div>
<svg class="r" width="1600" height="900">{eclipse(1240, 360, 120)}</svg>
<div class="flow" style="top:100px;bottom:190px;right:640px">
 <div class="eb" style="font-size:19px">Pitru Paksha 2026 · Pitru dosha</div>
 <h1 style="font-size:78px;margin-top:18px">{HEAD}</h1>
 <div class="b" style="font-size:28px;margin-top:22px">{SUB}</div>
 <div class="link2" style="font-size:24px;margin-top:22px">astroriver.com/journal/pitru-paksha</div>
</div>
<svg class="r" width="1600" height="900">{river(794, 782, 774, True, True, 1600)}</svg>
<div class="tag" style="left:700px;top:746px">astroriver.com</div>
<div class="foot" style="bottom:26px"><span class="n" style="font-size:32px">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

N = len(slides)
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
if __name__ == '__main__':
    asyncio.run(main())
