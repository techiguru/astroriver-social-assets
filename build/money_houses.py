# Wed 30 Sep 2026 evening: teaching carousel "Where money shows in your chart: the 2nd and 11th houses".
# Ivory teaching look (same dress as the Sade Sati carousel). Every astrology line follows the live article
# /journal/2nd-11th-house-money (content/source/journal-money-houses.md): the 2nd is the tank (dhana bhava),
# the 11th the flow (labha bhava), the 12th expense and loss ("a river, not a lake"); the 9th, 5th, 10th and
# the 1st as hinge; Parashara's rule (lords of 1, 2, 5, 9, 11 connected); the four things that break a yoga.
# The offer slide matches the product in the article (wealth-report). No dates on this post.
import os, asyncio
from playwright.async_api import async_playwright
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_shared.py')).read())
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)

EXTRA = """
.flow{position:absolute;left:100px;right:100px;display:flex;flex-direction:column;justify-content:center}
.hr{display:flex;gap:30px;align-items:baseline;padding:22px 0;border-top:1.5px solid #DCCFBA}
.hr:last-child{border-bottom:1.5px solid #DCCFBA}
.hr .n{font:700 46px 'PF';color:#D77B09;min-width:92px}
.hr .t{font:600 33px 'LO'}
.hr .t small{display:block;font:400 28px/1.45 'LO';color:var(--mut);margin-top:4px}
.pt{display:flex;gap:24px;align-items:baseline;padding:18px 0;border-top:1.5px solid #E2D7C4}
.pt:last-child{border-bottom:1.5px solid #E2D7C4}
.pt .k{font:700 32px 'PF';color:#D77B09;min-width:30px}
.pt .k.w{min-width:88px}
.pt .v{font:400 31px/1.4 'LO'}
.rule{border:2.5px solid #D77B09;background:#FBF1E3;border-radius:18px;padding:26px 30px}
.rule .l{font:600 19px 'IN';letter-spacing:3px;color:#A8590A;text-transform:uppercase}
.rule .x{font:500 34px/1.4 'LO';margin-top:10px}
"""

def three_houses(x0, y0, bw, bh, gap, big=False):
    items = [("11th", "Labha bhava", "The flow", "income, profit", False),
             ("2nd", "Dhana bhava", "The tank", "savings, what you keep", True),
             ("12th", "Vyaya bhava", "The leak", "expense, loss", False)]
    f1, f2, f3, f4 = (60, 19, 25, 22) if not big else (70, 22, 29, 26)
    s = ''
    for k, (num, bhava, role, sub, hot) in enumerate(items):
        x = x0 + k * (bw + gap)
        fill = '#D77B09' if hot else '#FBF7F0'
        ink = '#FFF8EE' if hot else '#211B12'
        subc = '#FCE8CF' if hot else '#6B5B4B'
        s += (f'<rect x="{x}" y="{y0}" width="{bw}" height="{bh}" rx="18" fill="{fill}" stroke="{"#D77B09" if hot else "#DCCFBA"}" stroke-width="2"/>'
              f'<text x="{x+bw/2}" y="{y0+bh*0.52}" text-anchor="middle" font-family="PF" font-weight="700" font-size="{f1}" fill="{ink}">{num}</text>'
              f'<text x="{x+bw/2}" y="{y0+bh*0.52+f2+22}" text-anchor="middle" font-family="IN" font-weight="600" font-size="{f2}" letter-spacing="2" fill="{subc}">{bhava.upper()}</text>'
              f'<text x="{x+bw/2}" y="{y0+bh+f3+26}" text-anchor="middle" font-family="IN" font-weight="700" font-size="{f3}" letter-spacing="1.5" fill="{"#A8590A" if hot else "#6B5B4B"}">{role.upper()}</text>'
              f'<text x="{x+bw/2}" y="{y0+bh+f3+f4+40}" text-anchor="middle" font-family="LO" font-size="{f4+4}" fill="#6B5B4B">{sub}</text>')
        if k < 2:  # arrow into the next box
            ax0, ax1, ay = x + bw + 10, x + bw + gap - 12, y0 + bh / 2
            s += (f'<line x1="{ax0}" y1="{ay}" x2="{ax1-8}" y2="{ay}" stroke="#D77B09" stroke-width="3"/>'
                  f'<path d="M{ax1-12},{ay-10} L{ax1},{ay} L{ax1-12},{ay+10} Z" fill="#D77B09"/>')
    return s

N = 5
Y = [1212, 1176, 1204, 1170, 1206, 1196]
def slide_river(i):
    a, b = Y[i], Y[i + 1]
    mid = (a + b) / 2 + (16 if i % 2 else -16)
    return river_path(a, b, mid, i == 0, i == N - 1)
TAGS = [(640, 1150), (560, 1146), (700, 1150), (600, 1150), (620, 1162)]
FL = 'top:110px;bottom:210px'
def sl(i, inner, fl=FL):
    return page(W, H, f'<div class="flow" style="{fl}">{inner}</div>', slide_river(i), TAGS[i], 58, 560, 56).replace('</style>', EXTRA + '</style>', 1)

HEAD = 'Where money shows in <em>your</em>&nbsp;chart.'
pts = lambda items: ''.join(f'<div class="pt"><span class="k w">{k}</span><span class="v">{v}</span></div>' for k, v in items)
DIAG = lambda w, h, big=False, gap=65, bw=250, bh=190: f'<svg width="{w}" height="{h}" viewBox="100 0 {w} {h}" style="display:block">{three_houses(100, 10, bw, bh, gap, big)}</svg>'

slides = []
slides.append(sl(0, f"""
 <div class="eb">River Journal · Money in the chart</div>
 <h1 style="font-size:92px">Where money shows in <em>your</em>&nbsp;chart.</h1>
 <div class="b" style="font-size:33px;margin-top:26px">Not in your Sun sign. Two houses carry most of it: the 2nd and the&nbsp;11th.</div>
 <div style="margin-top:46px">{DIAG(880, 330)}</div>
 <div class="m" style="margin-top:26px;font-size:29px;color:#A8590A">Swipe &#8594;</div>""", 'top:110px;bottom:210px'))

slides.append(sl(1, f"""
 <div class="eb">1 · The tank and the flow</div>
 <h2>The 11th brings it in.<br>The 2nd holds it.</h2>
 <div style="margin-top:36px">{pts([('11th', 'Labha bhava, the house of gains. Income, profit, what&nbsp;arrives.'), ('2nd', 'Dhana bhava, the house of wealth. Savings, family wealth, what you&nbsp;hold.'), ('12th', 'Vyaya bhava, expense and loss. When it pulls on the 2nd, the chart earns and cannot&nbsp;hold.')])}</div>
 <div class="b" style="font-size:31px;margin-top:34px">The eleventh is the flow. The second is the tank. Money in a chart with a strong twelfth is a river, not a&nbsp;lake.</div>
 <div class="m" style="font-size:25px;margin-top:22px">Houses are counted from your lagna, the rising sign. Lahiri sidereal.</div>"""))

rows = [("9th", "Fortune, <i>bhagya</i>", "Luck with money: the inheritance, the windfall, the&nbsp;patron."),
        ("5th", "The mind", "Speculation, and the mind&#8217;s earning&nbsp;power."),
        ("10th", "Career", "The work the money comes&nbsp;from."),
        ("1st", "You", "Wealth that does not connect to your lagna is someone else&#8217;s&nbsp;wealth.")]
hr = ''.join(f'<div class="hr"><span class="n">{n}</span><span class="t">{t}<small>{s}</small></span></div>' for n, t, s in rows)
slides.append(sl(2, f"""
 <div class="eb">2 · The houses behind them</div>
 <h2>Four more have a say.</h2>
 <div style="margin-top:40px">{hr}</div>"""))

brk = [("1", "A weak planet in the yoga."), ("2", "A malefic aspect on the 2nd or&nbsp;11th."), ("3", "The 12th house, the leak."), ("4", "The dasha that never&nbsp;arrives.")]
pt = ''.join(f'<div class="pt"><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in brk)
slides.append(sl(3, f"""
 <div class="eb">3 · Dhana yoga</div>
 <h2>Wealth is a timing question.</h2>
 <div class="rule" style="margin-top:34px"><div class="l">Parashara&#8217;s rule</div><div class="x">The lords of the 1st, 2nd, 5th, 9th and 11th, connected to one another, give&nbsp;wealth.</div></div>
 <div class="m" style="margin-top:30px;font-size:29px;color:#211B12">What breaks a wealth yoga:</div>
 <div style="margin-top:12px">{pt}</div>
 <div class="m" style="margin-top:26px;font-size:28px">A yoga pays in the periods of the planets that form it. The 2nd and 11th house, in&nbsp;full:</div>
 <div class="link" style="margin-top:4px;font-size:29px">astroriver.com/journal/2nd-11th-house-money</div>"""))

opt = lambda title, sub, hot: (
    f'<div style="border:{"2.5px solid #D77B09" if hot else "1.5px solid #DCCFBA"};background:{"#FBF1E3" if hot else "#FBF7F0"};border-radius:18px;padding:24px 30px;margin-top:16px">'
    f'<div style="font:700 {38 if hot else 33}px PF">{title}</div>'
    f'<div style="font:400 27px/1.45 LO;color:#6B5B4B;margin-top:6px">{sub}</div></div>')
slides.append(sl(4, f"""
 <div class="eb">4 · Your own chart</div>
 <h2 style="font-size:66px">Will it come,<br>and <em>when</em>?</h2>
 <div class="m" style="margin-top:18px;font-size:29px">Only your chart can say. Three ways to get your answer:</div>
 <div style="margin-top:10px">
  {opt("A written wealth report", "Your 2nd, 11th and 9th houses, every dhana yoga graded, timed against your&nbsp;dasha.", True)}
  {opt("A private consultation", "Live, with a senior astrologer.", False)}
  {opt("Ask an AI astrologer", "Online at astroriver.com, any time.", False)}
 </div>
 <div style="margin-top:32px;font:500 25px 'IN';letter-spacing:3px;color:#6B5B4B">REPORT OR CONSULTATION, ON WHATSAPP</div>
 <div style="margin-top:6px;font:700 44px 'IN';color:#A8590A;letter-spacing:.5px">+91 70091 27641</div>"""))

story = page(1080, 1920, f"""
<div class="flow" style="top:170px;bottom:250px">
 <div class="eb" style="font-size:24px">River Journal · Money in the chart</div>
 <h1 style="font-size:112px;margin-top:26px">{HEAD}</h1>
 <div class="b" style="font-size:38px;margin-top:34px">Not in your Sun sign. Two houses carry most of it: the 2nd and the&nbsp;11th.</div>
 <div style="margin-top:64px">{DIAG(880, 360, True, 55, 257, 210)}</div>
 <div class="b" style="font-size:34px;margin-top:34px">When the 12th pulls on the 2nd, the chart earns and cannot hold: a river, not a&nbsp;lake.</div>
 <div class="m" style="font-size:28px;margin-top:20px">Houses counted from your lagna. Lahiri sidereal.</div>
 <div style="margin-top:44px;padding-top:34px;border-top:1.5px solid #DCCFBA">
  <div class="m" style="font-size:32px">The 2nd and 11th house, in full:</div>
  <div class="link" style="margin-top:4px;font-size:34px">astroriver.com/journal/2nd-11th-house-money</div>
 </div>
</div>""", river_path(1742, 1728, 1716, True, True), (470, 1680), 90, 820, 90).replace('</style>', EXTRA + '</style>', 1)

XW, XH = 1600, 900
def river_x(a, b):
    mid = (a + b) / 2 - 14
    p = f"M100,{a} C420,{a+12} 560,{mid} 800,{mid} C1060,{mid} 1200,{b} 1495,{b}"
    q = f"M100,{a+14} C420,{a+26} 560,{mid+18} 800,{mid+18} C1060,{mid+18} 1200,{b+14} 1495,{b+14}"
    return (f'<path d="{q}" fill="none" stroke="#E2D7C4" stroke-width="3"/><path d="{p}" fill="none" stroke="#D77B09" stroke-width="4.5" stroke-linecap="round"/>'
            f'<circle cx="100" cy="{a}" r="9" fill="#D77B09"/><circle cx="1495" cy="{b}" r="20" fill="none" stroke="#D77B09" stroke-width="3"/><circle cx="1495" cy="{b}" r="8" fill="#D77B09"/>')
XD = 3 * 200 + 2 * 50
x = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{EXTRA}
html,body{{width:{XW}px;height:{XH}px}} .s{{width:{XW}px;height:{XH}px}}</style></head><body><div class="s">
<div class="wm" style="top:330px;left:260px">astroriver.com</div><div class="tr" style="top:52px">astroriver.com</div>
<div style="position:absolute;left:100px;right:100px;top:100px;bottom:190px;display:flex;align-items:center;justify-content:space-between;gap:56px">
 <div style="flex:1">
  <div class="eb" style="font-size:20px">River Journal · Money in the chart</div>
  <h1 style="font-size:80px;margin-top:18px">{HEAD}</h1>
  <div class="b" style="font-size:29px;margin-top:22px">The 11th brings it in. The 2nd holds it. The 12th lets it&nbsp;go.</div>
  <div class="m" style="font-size:25px;margin-top:24px">The 2nd and 11th house, in full:</div>
  <div class="link" style="margin-top:2px;font-size:27px">astroriver.com/journal/2nd-11th-house-money</div>
 </div>
 <div>{DIAG(XD, 300, False, 50, 200, 170)}
  <div class="m" style="font-size:21px;margin-top:6px">Houses counted from your lagna. Lahiri sidereal.</div></div>
</div>
<svg class="r" width="{XW}" height="{XH}">{river_x(794, 782)}</svg>
<div class="tag" style="left:700px;top:746px">astroriver.com</div>
<div class="foot" style="bottom:26px"><span class="n" style="font-size:32px">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

async def main():
    jobs = [(f'money-slide-{i+1}-of-{N}', s, W, H) for i, s in enumerate(slides)]
    jobs += [('money-status-1080x1920', story, 1080, 1920), ('money-x-1600x900', x, XW, XH)]
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
