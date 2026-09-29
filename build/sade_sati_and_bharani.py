# Monday 28 Sep 2026: (A) Maha Bharani, Pitru Paksha ivory dress; (B) Sade Sati teaching carousel.
# Facts: every date computed this session (Swiss Ephemeris, Lahiri) and matching the live articles:
#   Moon in Bharani Tue 29 Sep 09:04 IST -> Wed 30 Sep 07:37 IST; Delhi aparahna 29 Sep 13:22-15:45 (article table).
#   Saturn: into Pisces 29 Mar 2025; Pisces->Aries 3 Jun 2027; back 20 Oct 2027; final 23 Feb 2028;
#   Aries->Taurus 8 Aug 2029; back 5 Oct 2029; final 17 Apr 2030; Taurus->Gemini 31 May 2032.
import os, asyncio
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
F = 'file://' + HERE + '/fonts/'
W, H = 1080, 1350
SAT = open(os.path.join(HERE, 'saturn_path.txt')).read()

CSS = f"""
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay[wght].ttf');font-weight:400 900;}}
@font-face{{font-family:'PF';src:url('{F}PlayfairDisplay-Italic[wght].ttf');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'LO';src:url('{F}Lora[wght].ttf');font-weight:400 700;}}
@font-face{{font-family:'LO';src:url('{F}Lora-Italic[wght].ttf');font-weight:400 700;font-style:italic;}}
@font-face{{font-family:'IN';src:url('{F}Inter[opsz,wght].ttf');font-weight:100 900;}}
:root{{--bg:#F3EDE2;--ink:#211B12;--saf:#D77B09;--saf2:#A8590A;--mut:#6B5B4B;--faint:#E2D7C4;}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:var(--bg);overflow:hidden}}
.s{{position:relative;background:var(--bg);color:var(--ink);font-family:'LO',serif}}
.tr{{position:absolute;right:102px;font:500 21px 'IN';letter-spacing:2.5px;color:var(--mut)}}
.wm{{position:absolute;left:70px;font:italic 400 176px 'PF';color:var(--ink);opacity:.045;transform:rotate(-13deg);transform-origin:left top;white-space:nowrap;pointer-events:none}}
.c{{position:absolute;left:100px;right:100px}}
.eb{{font:600 22px 'IN';letter-spacing:5.5px;color:var(--saf2);text-transform:uppercase}}
h1{{font:700 88px/1.05 'PF';letter-spacing:-.5px;margin-top:26px}}
h2{{font:700 68px/1.08 'PF';letter-spacing:-.3px;margin-top:22px}}
em{{font-style:italic;color:var(--saf2);font-weight:600}}
.b{{font:400 36px/1.5 'LO';margin-top:32px}}
.m{{font:400 30px/1.5 'LO';color:var(--mut)}}
.row{{display:flex;justify-content:space-between;align-items:baseline;gap:24px;padding:22px 0;border-top:1.5px solid #DCCFBA}}
.row .k{{font:500 31px 'LO'}}
.row .v{{font:600 28px 'IN';color:var(--saf2);letter-spacing:.3px;text-align:right}}
.row .k small{{display:block;font:500 20px 'IN';letter-spacing:2px;color:var(--mut);margin-top:6px;text-transform:uppercase}}
.row .v small{{display:block;font:500 21px 'IN';color:var(--mut);margin-top:6px;letter-spacing:.2px}}
.foot{{position:absolute;left:100px;right:102px;display:flex;justify-content:space-between;align-items:baseline}}
.foot .n{{font:italic 500 36px 'PF'}}
.foot .u{{font:500 23px 'IN';letter-spacing:2.5px;color:var(--mut)}}
svg.r{{position:absolute;left:0;top:0}}
.tag{{position:absolute;font:600 17px 'IN';letter-spacing:2.5px;color:var(--saf2);background:var(--bg);padding:0 10px}}
.bigrows .row{{padding:28px 0}} .bigrows .row .k{{font-size:34px}} .bigrows .row .v{{font-size:31px}}
.link{{font:600 30px 'IN';color:var(--saf2);letter-spacing:.2px}}
"""

def river_path(a, b, mid, start_dot, end_ring, x0=0, x1=1080):
    xs = 100 if start_dot else x0
    xe = 975 if end_ring else x1
    p = f"M{xs},{a} C{xs+200},{a+14} 360,{mid} 540,{mid} C720,{mid} 820,{b} {xe},{b}"
    q = f"M{xs},{a+16} C{xs+200},{a+30} 360,{mid+20} 540,{mid+20} C720,{mid+20} 820,{b+16} {xe},{b+16}"
    extra = f'<circle cx="100" cy="{a}" r="9" fill="#D77B09"/>' if start_dot else ''
    if end_ring:
        extra += (f'<circle cx="975" cy="{b}" r="22" fill="none" stroke="#D77B09" stroke-width="3"/>'
                  f'<circle cx="975" cy="{b}" r="9" fill="#D77B09"/>')
    return (f'<path d="{q}" fill="none" stroke="#E2D7C4" stroke-width="3"/>'
            f'<path d="{p}" fill="none" stroke="#D77B09" stroke-width="4.5" stroke-linecap="round"/>{extra}')

def page(w, h, body, river_svg, tag_xy, top_tr, wm_top, foot_bottom):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
html,body{{width:{w}px;height:{h}px}} .s{{width:{w}px;height:{h}px}}</style></head><body><div class="s">
<div class="wm" style="top:{wm_top}px">astroriver.com</div><div class="tr" style="top:{top_tr}px">astroriver.com</div>
{body}
<svg class="r" width="{w}" height="{h}">{river_svg}</svg>
<div class="tag" style="left:{tag_xy[0]}px;top:{tag_xy[1]}px">astroriver.com</div>
<div class="foot" style="bottom:{foot_bottom}px"><span class="n">Astro River</span><span class="u">astroriver.com</span></div>
</div></body></html>"""

# ------------------------------------------------------------------ A: Maha Bharani
mb_rows = """
 <div class="row"><span class="k">Moon in Bharani<small>India time</small></span><span class="v">Tue 29 Sep, 09:04<small>to Wed 30 Sep, 07:37</small></span></div>
 <div class="row"><span class="k">Shradh hours in Delhi<small>Aparahna, the afternoon</small></span><span class="v">Tue 13:22 – 15:45</span></div>
 <div class="row" style="border-bottom:1.5px solid #DCCFBA"><span class="k">UK, USA, Canada, Australia</span><span class="v">Also Tuesday</span></div>
"""
mb_feed = page(W, H, f"""
<div class="c" style="top:150px">
 <div class="eb">Pitru Paksha 2026 · A day that carries weight</div>
 <h1 style="font-size:72px">Maha Bharani is on <em>Tuesday 29&nbsp;September</em>.</h1>
 <div class="b" style="font-size:33px;margin-top:28px">The Moon is in Bharani on Tuesday afternoon, in India and abroad. The tradition holds that a shradh done on Bharani in this fortnight carries the merit of one done at Gaya.</div>
 <div style="margin-top:36px">{mb_rows}</div>
 <div class="m" style="margin-top:26px;font-size:28px">The hours for your city:</div>
 <div class="link" style="margin-top:4px">astroriver.com/journal/pitru-paksha</div>
</div>""", river_path(1212, 1196, 1186, True, True), (610, 1168), 58, 560, 56)

mb_story = page(1080, 1920, f"""
<div class="c" style="top:330px">
 <div class="eb">Pitru Paksha 2026 · A day that carries weight</div>
 <h1 style="font-size:100px">Maha Bharani is on <em>Tuesday 29&nbsp;September</em>.</h1>
 <div class="b" style="font-size:40px;margin-top:40px">The Moon is in Bharani on Tuesday afternoon, in India and abroad. A shradh done on Bharani in this fortnight carries the merit of one done at Gaya.</div>
 <div style="margin-top:56px">{mb_rows}</div>
 <div class="m" style="margin-top:44px;font-size:33px">The hours for your city:</div>
 <div class="link" style="margin-top:6px;font-size:34px">astroriver.com/journal/pitru-paksha</div>
</div>""", river_path(1742, 1728, 1716, True, True), (470, 1680), 90, 820, 90)

# ------------------------------------------------------------------ B: Sade Sati carousel
N = 5
Y = [1212, 1176, 1204, 1170, 1206, 1196]
def slide_river(i):
    a, b = Y[i], Y[i + 1]
    mid = (a + b) / 2 + (16 if i % 2 else -16)
    return river_path(a, b, mid, i == 0, i == N - 1)
TAGS = [(640, 1150), (560, 1146), (700, 1150), (600, 1150), (620, 1162)]

def sat_glyph(cx, cy, scale, color='#211B12'):
    return (f'<path d="{SAT}" fill="{color}" transform="translate({cx} {cy}) scale({scale}) translate(-400 -225)"/>')

def three_signs(x0, y0, box_w, box_h, gap, big=False):
    signs = [("Aquarius", "Kumbh", "Last phase", False), ("Pisces", "Meen", "The peak", True), ("Aries", "Mesha", "First phase", False)]
    s = ''
    for k, (en, hi, ph, hot) in enumerate(signs):
        x = x0 + k * (box_w + gap)
        fill = '#D77B09' if hot else '#FBF7F0'
        ink = '#FFF8EE' if hot else '#211B12'
        sub = '#FCE8CF' if hot else '#6B5B4B'
        f1, f2, f3 = (44, 22, 25) if not big else (50, 25, 29)
        s += (f'<rect x="{x}" y="{y0}" width="{box_w}" height="{box_h}" rx="18" fill="{fill}" stroke="{"#D77B09" if hot else "#DCCFBA"}" stroke-width="2"/>'
              f'<text x="{x+box_w/2}" y="{y0+box_h*0.5}" text-anchor="middle" font-family="PF" font-weight="700" font-size="{f1}" fill="{ink}">{en}</text>'
              f'<text x="{x+box_w/2}" y="{y0+box_h*0.5+f2+18}" text-anchor="middle" font-family="IN" font-weight="600" font-size="{f2}" letter-spacing="2" fill="{sub}">{hi.upper()} RASHI</text>'
              f'<text x="{x+box_w/2}" y="{y0+box_h+f3+26}" text-anchor="middle" font-family="IN" font-weight="700" font-size="{f3}" letter-spacing="1" fill="{"#A8590A" if hot else "#6B5B4B"}">{ph.upper()}</text>')
    # Saturn above the middle box
    mx = x0 + box_w + gap + box_w / 2
    s += (f'<circle cx="{mx}" cy="{y0-64}" r="42" fill="#FBF7F0" stroke="#D77B09" stroke-width="2.5"/>' + sat_glyph(mx, y0 - 64, 0.62))
    s += f'<line x1="{mx}" y1="{y0-22}" x2="{mx}" y2="{y0-2}" stroke="#D77B09" stroke-width="2.5"/>'
    # direction arrow under the labels
    ay = y0 + box_h + (84 if not big else 96)
    s += (f'<line x1="{x0+20}" y1="{ay}" x2="{x0+3*box_w+2*gap-30}" y2="{ay}" stroke="#C9B89F" stroke-width="2"/>'
          f'<path d="M{x0+3*box_w+2*gap-30},{ay-9} L{x0+3*box_w+2*gap-12},{ay} L{x0+3*box_w+2*gap-30},{ay+9} Z" fill="#C9B89F"/>'
          f'<text x="{x0+20}" y="{ay+34}" font-family="IN" font-weight="600" font-size="{19 if not big else 22}" letter-spacing="2" fill="#8C7A63">SATURN MOVES THIS WAY, ABOUT 2½ YEARS IN EACH SIGN</text>')
    return s

slides = []
slides.append(page(W, H, """
<div class="c" style="top:300px">
 <div class="eb">River Journal · Sade Sati</div>
 <h1 style="font-size:112px">Is Sade Sati on <em>you</em>?</h1>
 <div class="b" style="font-size:38px;margin-top:40px">Saturn&#8217;s seven and a half years: about two and a half years each in the sign before your Moon, on your Moon, and the sign after it.</div>
 <div class="m" style="margin-top:40px;font-size:31px">It is counted from your Moon sign, not your Sun sign.</div>
 <div class="m" style="margin-top:14px;font-size:31px;color:#A8590A">Swipe to find yours &#8594;</div>
</div>""", slide_river(0), TAGS[0], 58, 560, 56))

slides.append(page(W, H, f"""
<div class="c" style="top:120px">
 <div class="eb">1 · Who is in it now</div>
 <h2>Saturn is in Pisces.</h2>
 <div class="m" style="margin-top:18px">Find your Moon sign:</div>
</div>
<svg class="r" width="{W}" height="{H}">{three_signs(100, 470, 266, 190, 41)}</svg>
<div style="position:absolute;right:100px;top:818px;font:600 17px 'IN';letter-spacing:2.5px;color:#A8590A">astroriver.com</div>
<div class="c" style="top:880px">
 <div class="m" style="font-size:29px;color:#211B12">Capricorn Moon (Makar): yours ended on 29 March 2025.</div>
 <div class="m" style="font-size:25px;margin-top:10px">Saturn in Pisces: 29 March 2025 to 3 June 2027. Lahiri sidereal.</div>
</div>""", slide_river(1), TAGS[1], 58, 560, 56))

end_rows = """
 <div class="row"><span class="k">Aquarius Moon<small>Kumbh rashi</small></span><span class="v">3 June 2027<small>fully on 23 Feb 2028</small></span></div>
 <div class="row"><span class="k">Pisces Moon<small>Meen rashi</small></span><span class="v">17 April 2030<small>first exit 8 Aug 2029</small></span></div>
 <div class="row"><span class="k">Aries Moon<small>Mesha rashi</small></span><span class="v">31 May 2032</span></div>
 <div class="row" style="border-bottom:1.5px solid #DCCFBA"><span class="k">Capricorn Moon<small>Makar rashi</small></span><span class="v">Ended<small>29 March 2025</small></span></div>
"""
slides.append(page(W, H, f"""
<div class="c" style="top:150px">
 <div class="eb">2 · When it ends</div>
 <h2>The dates to know.</h2>
 <div class="bigrows" style="margin-top:48px">{end_rows}</div>
 <div class="m" style="margin-top:34px;font-size:28px">Saturn often steps back into a sign for a few months before leaving it for good. The later date is the real end.</div>
</div>""", slide_river(2), TAGS[2], 58, 560, 56))

three = ["Saturn&#8217;s place in your birth chart.", "The strength of your Moon.", "The dasha running now."]
tl = "".join(f'<div style="display:flex;gap:26px;padding:24px 0;border-top:1.5px solid #E2D7C4"><span style="font:700 38px PF;color:#D77B09;min-width:34px">{k+1}</span><span style="font:400 36px/1.4 LO">{t}</span></div>' for k, t in enumerate(three))
slides.append(page(W, H, f"""
<div class="c" style="top:150px">
 <div class="eb">3 · How hard it is</div>
 <h2>Demanding, not doomed.</h2>
 <div class="m" style="margin-top:26px;font-size:31px;color:#211B12">It depends on three things in your own chart:</div>
 <div style="margin-top:22px">{tl}</div>
 <div class="m" style="margin-top:40px;font-size:30px">What Saturn rewards: finish what is open, pay what is owed, show up on the days you would rather not.</div>
 <div class="m" style="margin-top:44px;font-size:30px;color:#211B12">Phases, dates and remedies:</div>
 <div class="link" style="margin-top:6px;font-size:32px">astroriver.com/journal/sade-sati</div>
</div>""", slide_river(3), TAGS[3], 58, 560, 56))


opt = lambda title, sub, hot: (
    f'<div style="border:{"2.5px solid #D77B09" if hot else "1.5px solid #DCCFBA"};background:{"#FBF1E3" if hot else "#FBF7F0"};border-radius:18px;padding:26px 30px;margin-top:18px">'
    f'<div style="font:700 {40 if hot else 34}px PF">{title}</div>'
    f'<div style="font:400 28px/1.45 LO;color:#6B5B4B;margin-top:6px">{sub}</div></div>')
slides.append(page(W, H, f"""
<div class="c" style="top:130px">
 <div class="eb">4 · Your own chart</div>
 <h2 style="font-size:64px">Your Sade Sati,<br>read for <em>your</em> chart.</h2>
 <div class="m" style="margin-top:20px;font-size:30px">The same Saturn runs differently in every chart. Three ways to get your answer:</div>
 <div style="margin-top:14px">
  {opt("A written Sade Sati report", "Your phases and dates, read against your own chart.", True)}
  {opt("A private consultation", "Live, with a senior astrologer.", False)}
  {opt("Ask an AI astrologer", "Online at astroriver.com, any time.", False)}
 </div>
 <div style="margin-top:36px;font:500 26px 'IN';letter-spacing:3px;color:#6B5B4B">REPORT OR CONSULTATION, ON WHATSAPP</div>
 <div style="margin-top:6px;font:700 46px 'IN';color:#A8590A;letter-spacing:.5px">+91 70091 27641</div>
</div>""", slide_river(4), TAGS[4], 58, 560, 56))

ss_story = page(1080, 1920, f"""
<div class="c" style="top:240px">
 <div class="eb">River Journal · Sade Sati</div>
 <h1 style="font-size:100px">Is Sade Sati on <em>you</em>?</h1>
 <div class="m" style="margin-top:26px;font-size:34px">Saturn is in Pisces. Find your Moon sign:</div>
</div>
<svg class="r" width="1080" height="1920">{three_signs(100, 820, 266, 210, 41, big=True)}</svg>
<div class="c" style="top:1300px">
 <div class="m" style="font-size:31px;color:#211B12">Capricorn Moon: yours ended on 29 March 2025.</div>
 <div class="m" style="font-size:33px;margin-top:34px">Phases, dates and remedies:</div>
 <div class="link" style="margin-top:6px;font-size:34px">astroriver.com/journal/sade-sati</div>
</div>""", river_path(1742, 1728, 1716, True, True), (470, 1680), 90, 820, 90)

async def main():
    out = os.path.join(HERE, 'out'); os.makedirs(out, exist_ok=True)
    jobs = [('bharani-post-1080x1350', mb_feed, W, H), ('bharani-status-1080x1920', mb_story, 1080, 1920),
            ('sadesati-status-1080x1920', ss_story, 1080, 1920)]
    jobs += [(f'sadesati-slide-{i+1}-of-{N}', s, W, H) for i, s in enumerate(slides)]
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html, w, h in jobs:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            fn = os.path.join(HERE, name + '.html'); open(fn, 'w').write(html)
            await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=os.path.join(out, name + '.png'))
        await b.close()
asyncio.run(main())
print('done')
