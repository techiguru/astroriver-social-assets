# Sat 3 Oct 2026 evening: Guru and Ravi Pushya, "save the date" (calendar series: ivory, with the site's own
# Pushya drawing on the cover; no table on the cover, founder 1 Oct). The drawing is the Journal picture for
# /journal/guru-pushya-ravi-pushya-2026 (site repo commit d0e9777, public/art/journal/guru-pushya-ravi-pushya-2026.svg),
# copied here with its viewBox cropped above its own river line (viewBox 0 0 800 388): art-journal-pushya-lotus.svg.
# Times computed this session (Swiss Ephemeris, Lahiri) and matching the live article:
#   Moon in Pushya: Mon 5 Oct 00:14 -> 23:09 IST; Sun 1 Nov 05:39 -> Mon 2 Nov 04:30 IST; Sat 28 Nov 12:50 -> Sun 29 Nov 10:59 IST.
#   Delhi sunrise: 5 Oct 06:17, 1 Nov 06:34. Diwali Sun 8 Nov, Dhanteras Fri 6 Nov (article).
#   Abroad (article table): 1 Nov Dubai whole day until Mon 03:00; Singapore from 08:09; Sydney from 11:09; London whole
#   day until 23:00; New York/Toronto sunrise until 18:00; Vancouver/San Francisco sunrise until 15:00.
#   29 Nov: no Ravi Pushya in the UK, USA or Canada. Next Guru Pushya Thu 18 Feb 2027 from 21:06 IST; Thu 18 Mar 2027 whole day.
#   Not for the wedding itself (article). Founder approves before posting.
import os, asyncio, math
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
BG, IV, MUT, SAF, SAF2, LINE, RIVER = '#F3EDE2', '#211B12', '#6B5B4B', '#A8590A', '#A8590A', '#DCCFBA', '#D77B09'
CARD_HOT, CARD = '#FBF1E3', '#F7F0E5'
PREFIX = 'pushya-'
ART = 'file://' + os.path.join(HERE, 'art-journal-pushya-lotus.svg')
def art(top, w=1080, left=0):
    return f'<img src="{ART}" style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{w*388/800:.0f}px;z-index:-1">'
CSS = f"""
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900;}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700;}}
@font-face{{font-family:'LO';src:url('{F}Lora-Italic[wght].ttf');font-weight:400 700;font-style:italic;}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900;}}
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
def rows(items, kw=230):
    s = ''
    for k, v, hot in items:
        bg = f'background:{CARD_HOT};margin:0 -18px;padding-left:18px;padding-right:18px;' if hot else ''
        s += (f'<div class="pt" style="gap:28px;{bg}"><span class="k" style="font:700 26px IN;min-width:{kw}px;max-width:{kw}px;letter-spacing:.3px;line-height:1.35">{k}</span>'
              f'<span class="v" style="font-size:30px">{v}</span></div>')
    return s

HEAD = 'There is no Guru Pushya left in&nbsp;<em>2026</em>.'
SUB = 'The day to plan around is Ravi Pushya: Sunday 1&nbsp;November, five days before&nbsp;Dhanteras.'
LINK1, LINK2 = 'Times for your city:', 'astroriver.com/journal/guru-pushya-ravi-pushya-2026'
slides = []
slides.append(page(W, H, f"""{art(20)}
<div class="flow" style="top:600px;bottom:220px;justify-content:flex-start">
 <div class="eb">Muhurat · Pushya nakshatra</div>
 <h1 style="font-size:82px;margin-top:20px">{HEAD}</h1>
 <div class="b" style="font-size:34px;margin-top:24px">{SUB}</div>
 <div class="m" style="margin-top:20px;font-size:29px;color:{SAF}">Swipe &#8594;</div>
</div>""", sr(0), TAGS[0], 40, 700, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">1 · The dates</div>
 <h2>Three Ravi Pushya<br>windows in 2026.</h2>
 <div style="margin-top:36px">{rows([('Night of Sun 4&nbsp;Oct', '00:14 IST until sunrise on Monday. It falls inside Pitru Paksha, so many families&nbsp;wait.', False), ('Sun 1 Nov', 'From sunrise (06:34 in Delhi) until 04:30 on Monday: effectively the whole&nbsp;day.', True), ('Sun 29 Nov', 'Until 10:59 IST. Morning&nbsp;only.', False)])}</div>
 <div class="m" style="margin-top:26px;font-size:26px">The next Guru Pushya: Thursday 18 February 2027. The strongest of 2027: Thursday 18 March, the whole&nbsp;day.</div>
</div>""", sr(1), TAGS[1], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">2 · What it is for</div>
 <h2>A day for beginnings<br>that last.</h2>
 <div style="margin-top:36px">{pts([('&#8212;', 'Gold and silver, bought to&nbsp;keep.'), ('&#8212;', 'Opening an account or a&nbsp;business.'), ('&#8212;', 'Signing for a house or a&nbsp;vehicle.'), ('&#8212;', 'Starting a course of study or a&nbsp;treatment.')])}</div>
 <div class="m" style="margin-top:28px;font-size:27px">One exception, old and consistent in the texts: not the wedding&nbsp;itself.</div>
</div>""", sr(2), TAGS[2], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">3 · Outside India</div>
 <h2>1 November holds<br>everywhere.</h2>
 <div style="margin-top:34px">{rows([('Dubai', 'The whole day, until Monday&nbsp;03:00.', False), ('London', 'The whole day, until&nbsp;23:00.', False), ('New York, Toronto', 'From sunrise until&nbsp;18:00.', False), ('Pacific coast', 'From sunrise until&nbsp;15:00.', False), ('Singapore, Sydney', 'From 08:09 and from 11:09.', False)], 260)}</div>
 <div class="m" style="margin-top:24px;font-size:26px">29 November is not a Ravi Pushya in the UK, the USA or&nbsp;Canada.</div>
 <div class="link1" style="margin-top:22px">{LINK1}</div>
 <div class="link2" style="font-size:27px">{LINK2}</div>
</div>""", sr(3), TAGS[3], 58, 560, 56))

opt = lambda t, sub, hot: (f'<div style="border:{"2.5px solid "+SAF if hot else "1.5px solid "+LINE};background:{CARD_HOT if hot else CARD};border-radius:18px;padding:24px 30px;margin-top:16px">'
                           f'<div style="font:700 {38 if hot else 33}px PF;color:{IV}">{t}</div><div style="font:400 27px/1.45 LO;color:{MUT};margin-top:6px">{sub}</div></div>')
slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">4 · For something that matters</div>
 <h2 style="font-size:64px">A good day is for everyone.<br><em>Your</em> hour is&nbsp;yours.</h2>
 <div class="m" style="margin-top:18px;font-size:29px">For an ordinary purchase, the day is enough. For something that matters, choose the moment against your own&nbsp;chart.</div>
 <div style="margin-top:10px">
  {opt("A private consultation", "A moment chosen against your lagna, your dasha and the transits. Live, by audio call or&nbsp;chat.", True)}
  {opt("Ask an AI astrologer", "Online at astroriver.com, any time.", False)}
 </div>
 <div style="margin-top:32px;font:500 25px 'IN';letter-spacing:3px;color:{MUT}">CONSULTATION, ON WHATSAPP</div>
 <div style="margin-top:6px;font:700 44px 'IN';color:{SAF2};letter-spacing:.5px">+91 70091 27641</div>
</div>""", sr(4), TAGS[4], 58, 560, 56))

# WhatsApp status / Pinterest, 1080x1920
story = page(1080, 1920, f"""{art(150)}
<div class="flow" style="top:760px;bottom:250px;justify-content:flex-start">
 <div class="eb" style="font-size:25px">Muhurat · Pushya nakshatra</div>
 <h1 style="font-size:98px;margin-top:22px">{HEAD}</h1>
 <div class="b" style="font-size:40px;margin-top:30px">{SUB}</div>
 <div style="margin-top:36px">{rows([('Sun 1 Nov', 'Sunrise to 04:30 IST on&nbsp;Monday.', True), ('Sun 29 Nov', 'Until 10:59 IST.', False)], 200)}</div>
 <div class="link1" style="margin-top:36px;font-size:30px">{LINK1}</div>
 <div class="link2" style="font-size:28px">{LINK2}</div>
</div>""", river(1742, 1728, 1716, True, True), (470, 1680), 90, 980, 90)

# X, 1600x900
x = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
html,body{{width:1600px;height:900px}} .s{{width:1600px;height:900px}}</style></head><body><div class="s">
<div class="wm" style="top:330px;left:260px">astroriver.com</div><div class="tr" style="top:52px">astroriver.com</div>
{art(150, 760, 800)}
<div class="flow" style="top:100px;bottom:190px;right:840px">
 <div class="eb" style="font-size:19px">Muhurat · Pushya nakshatra</div>
 <h1 style="font-size:70px;margin-top:18px">{HEAD}</h1>
 <div class="b" style="font-size:29px;margin-top:22px">{SUB}</div>
 <div class="link1" style="margin-top:26px;font-size:24px">{LINK1}</div>
 <div class="link2" style="font-size:22px">{LINK2}</div>
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
