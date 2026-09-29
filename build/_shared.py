# Monday 28 Sep 2026: (A) Maha Bharani, Pitru Paksha ivory dress; (B) Sade Sati teaching carousel.
# Facts: every date computed this session (Swiss Ephemeris, Lahiri) and matching the live articles:
#   Moon in Bharani Tue 29 Sep 09:04 IST -> Wed 30 Sep 07:37 IST; Delhi aparahna 29 Sep 13:22-15:45 (article table).
#   Saturn: into Pisces 29 Mar 2025; Pisces->Aries 3 Jun 2027; back 20 Oct 2027; final 23 Feb 2028;
#   Aries->Taurus 8 Aug 2029; back 5 Oct 2029; final 17 Apr 2030; Taurus->Gemini 31 May 2032.
import os, asyncio

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

