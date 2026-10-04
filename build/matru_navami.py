# Sun 4 Oct 2026 morning: Matru Navami (English). Calendar series: ivory, the site's own Pitru Paksha drawing on the
# cover, no table on the cover (founder 1 Oct). The drawing is the Journal picture for /journal/pitru-paksha (site repo
# commit d0e9777, public/art/journal/pitru-paksha.svg), copied as art-journal-pitru-tarpan.svg, viewBox cropped to
# 0 0 800 388 above its own river line. Built from pushya_save_the_date.py.
# Facts computed this session (Swiss Ephemeris, Lahiri) and matching the live article /journal/pitru-paksha-2026:
#   Krishna Navami tithi: Sun 4 Oct 05:52 IST -> Mon 5 Oct 03:54 IST. Navami shradh Sun 4 Oct in every column
#   (Pacific column starred: it shares Sunday with Dashami). Delhi aparahna 4 Oct 13:20-15:41 (article table).
#   Article: "Matru Navami (Avidhava Navami) - Sunday 4 October. The Navami shradh is kept for mothers, and for women
#   who died while their husbands lived." On the image "passed away" (no "died" on graphics).
#   Australian clocks go forward on 4 Oct (article). At-home steps follow the article's "How to do shradh at home".
import os, asyncio, math
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); F = 'file://' + HERE + '/fonts/'
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
BG, IV, MUT, SAF, SAF2, LINE, RIVER = '#F3EDE2', '#211B12', '#6B5B4B', '#A8590A', '#A8590A', '#DCCFBA', '#D77B09'
CARD_HOT, CARD = '#FBF1E3', '#F7F0E5'
PREFIX = 'matru-navami-'
ART = 'file://' + os.path.join(HERE, 'art-journal-pitru-tarpan.svg')
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

HEAD = 'Sunday 4 October is for our&nbsp;<em>mothers</em>.'
SUB = 'Matru Navami. The Navami shradh is kept for mothers, and for women who passed away while their husbands&nbsp;lived.'
LINK1, LINK2 = 'The hours for your city:', 'astroriver.com/journal/pitru-paksha'
N = 3
Y = [1212, 1178, 1204, 1196]
def sr(i):
    a, b = Y[i], Y[i+1]
    return river(a, b, (a+b)/2 + (16 if i % 2 else -16), i == 0, i == N-1)
TAGS = [(640, 1150), (560, 1148), (620, 1162)]
slides = []
slides.append(page(W, H, f"""{art(20)}
<div class="flow" style="top:600px;bottom:220px;justify-content:flex-start">
 <div class="eb">Pitru Paksha 2026 · Matru Navami</div>
 <h1 style="font-size:84px;margin-top:20px">{HEAD}</h1>
 <div class="b" style="font-size:33px;margin-top:24px">{SUB}</div>
 <div class="m" style="margin-top:20px;font-size:29px;color:{SAF}">Swipe &#8594;</div>
</div>""", sr(0), TAGS[0], 40, 700, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">1 · The day and the hours</div>
 <h2>Navami runs through<br>Sunday afternoon.</h2>
 <div class="b" style="font-size:31px;margin-top:22px">The Navami tithi begins at 05:52 IST on Sunday and runs through the whole&nbsp;afternoon.</div>
 <div style="margin-top:30px">{rows([('Sun 4 Oct', 'India, Dubai and&nbsp;Singapore.', True), ('Sun 4 Oct', 'UK, USA and Canada. On the Pacific coast it shares the day with&nbsp;Dashami.', False), ('Sun 4 Oct', 'Australia. Clocks go forward that day; use the new&nbsp;time.', False)], 150)}</div>
 <div class="b" style="font-size:30px;margin-top:26px">Shradh hours in Delhi: <b style="font-weight:600">13:20 – 15:41</b>, the&nbsp;aparahna.</div>
 <div class="link1" style="margin-top:22px">{LINK1}</div>
 <div class="link2">{LINK2}</div>
</div>""", sr(1), TAGS[1], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="flow" style="{FL}">
 <div class="eb">2 · At home</div>
 <h2>Simple, and enough.</h2>
 <div style="margin-top:34px">{pts([('1', 'Face south. Pour water with black sesame, through kusha grass if you have it, and say her&nbsp;name.'), ('2', 'With each offering, say <i>Swadha</i>: Om Pitribhyah Swadha&nbsp;Namah.'), ('3', 'Feed someone in her memory. Set portions aside for a crow, a cow and a&nbsp;dog.')])}</div>
 <div class="m" style="margin-top:30px;font-size:28px">No priest nearby, or the family far apart? The Institute arranges tarpan and shradh in your family&#8217;s&nbsp;name.</div>
 <div style="margin-top:24px;font:500 25px 'IN';letter-spacing:3px;color:{MUT}">ON WHATSAPP</div>
 <div style="margin-top:6px;font:700 44px 'IN';color:{SAF2};letter-spacing:.5px">+91 70091 27641</div>
</div>""", sr(2), TAGS[2], 58, 560, 56))

story = page(1080, 1920, f"""{art(150)}
<div class="flow" style="top:760px;bottom:250px;justify-content:flex-start">
 <div class="eb" style="font-size:25px">Pitru Paksha 2026 · Matru Navami</div>
 <h1 style="font-size:100px;margin-top:22px">{HEAD}</h1>
 <div class="b" style="font-size:39px;margin-top:30px">{SUB}</div>
 <div class="b" style="font-size:37px;margin-top:34px">Shradh hours in Delhi: <b style="font-weight:600">13:20 – 15:41</b>.</div>
 <div class="link1" style="margin-top:36px;font-size:31px">{LINK1}</div>
 <div class="link2" style="font-size:31px">{LINK2}</div>
</div>""", river(1742, 1728, 1716, True, True), (470, 1680), 90, 980, 90)

x = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
html,body{{width:1600px;height:900px}} .s{{width:1600px;height:900px}}</style></head><body><div class="s">
<div class="wm" style="top:330px;left:260px">astroriver.com</div><div class="tr" style="top:52px">astroriver.com</div>
{art(150, 760, 800)}
<div class="flow" style="top:100px;bottom:190px;right:840px">
 <div class="eb" style="font-size:19px">Pitru Paksha 2026 · Matru Navami</div>
 <h1 style="font-size:70px;margin-top:18px">{HEAD}</h1>
 <div class="b" style="font-size:27px;margin-top:20px">{SUB}</div>
 <div class="link1" style="margin-top:24px;font-size:24px">Shradh hours in Delhi 13:20 – 15:41. For your city:</div>
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
