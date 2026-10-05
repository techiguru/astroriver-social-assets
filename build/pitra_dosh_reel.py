# Mon 5 Oct 2026: pitra dosh as a Reel (founder 4 Oct: Reels reach people who don't follow us; posted by hand from the
# app with a trending sound, so the video is silent). Founder 5 Oct: "make the reel properly", so this is moving
# design, not still cards: the Sun is eclipsed, both charts draw in and light their 5th and 9th houses, the lists come
# in line by line, and a diya burns at the end. Same words and facts as pitra_dosh.py.
# 1080x1920, 30 fps, about 37 s. Text stays inside Instagram's safe area: clear of the top bar (above y 250), the
# caption and name at the bottom (below y 1500) and the buttons on the right (x past 950).
# How it is made: one page; every move is a Web Animation, paused; each frame sets the clock and takes a screenshot;
# ffmpeg joins the frames. Writes out/pitra-dosh-reel.mp4. REEL_STILLS=7.5,14 writes only those moments as PNGs.
import os, sys, asyncio, subprocess
from playwright.async_api import async_playwright
import pitra_dosh as P
HERE = P.HERE; OUT = os.path.join(HERE, 'out')
IV, SAF, MUT, BG, LINE, RIVER = P.IV, P.SAF, P.MUT, P.BG, P.LINE, P.RIVER
FPS, END = 30, 37.6

# the scenes: (start, end) in seconds; each fades in and out as a whole, and its lines come in on their own times
S = [(-0.35, 6.6), (6.6, 12.8), (12.8, 19.4), (19.4, 25.6), (25.6, 30.8), (30.8, END + 1)]

def a(t, html, kind='up', style='', cls=''):
    return f'<div class="a {cls}" data-t="{t}" data-k="{kind}" style="{style}">{html}</div>'

def items(t0, step, rows, size=46):
    return '<div class="list">' + ''.join(
        a(t0 + i*step, f'<span class="k">{k}</span><span class="v" style="font-size:{size}px">{v}</span>', 'left', cls='row')
        for i, (k, v) in enumerate(rows)) + '</div>'

def scene(i, html):
    s, e = S[i]
    return f'<div class="scene" data-s="{s}" data-e="{e}">{html}</div>'

EB = lambda t, text: a(t, text, 'up', cls='eb')
H2 = lambda t, text, size=70: a(t, text, 'up', f"font:700 {size}px/1.08 'PF';margin-top:16px")

# scene 1: the Sun is eclipsed while the question comes in
ECL = f"""<svg class="art" width="1080" height="1920">
<circle cx="540" cy="580" r="290" fill="{P.GLYPH_RING}" opacity=".7"/>
<circle cx="540" cy="580" r="238" fill="none" stroke="{SAF}" stroke-opacity=".3" stroke-width="1.5"/>
<g id="rays">{''.join(f'<line x1="540" y1="{580-157}" x2="540" y2="{580-199}" stroke="{SAF}" stroke-width="10" stroke-linecap="round" opacity=".6" transform="rotate({d} 540 580)"/>' for d in range(0, 360, 30))}</g>
<circle cx="540" cy="580" r="129" fill="{SAF}"/>
<g id="rahu"><circle cx="611" cy="557" r="121" fill="#2A221C"/></g>
</svg>"""
s1 = scene(0, ECL + f"""<div class="box" style="top:960px">
{a(-0.7, 'Effort, but no&nbsp;fortune?', 'up', f"font:600 62px/1.15 'PF';color:{MUT}")}
{a(1.8, 'Is it the anger of the&nbsp;ancestors?', 'up', f"font:600 62px/1.15 'PF';color:{MUT};margin-top:20px")}
{a(3.1, 'Or <em>pitru&nbsp;dosha</em>:', 'up', "font:700 108px/1.05 'PF';margin-top:46px")}
{a(3.7, 'a debt your family line still&nbsp;carries.', 'up', "font:400 52px/1.35 'LO';margin-top:12px")}
</div>""")

# scene 2: both charts draw in, then the 9th and the 5th houses light up
def chart(x, fn):
    return (f'<svg class="ch" data-t="7.3" data-k="wipe" style="left:{x}px" width="404" height="404">{fn(())}</svg>'
            f'<svg class="ch" data-t="8.7" data-k="glow" style="left:{x}px" width="404" height="404">{fn((9,))}</svg>'
            f'<svg class="ch" data-t="10.0" data-k="glow" style="left:{x}px" width="404" height="404">{fn((5, 9))}</svg>')
HROW = lambda t, n, title, what: a(t, f'<span class="hn">{n}</span><span><b>{title}</b><br>{what}</span>', 'left', cls='hrow')
s2 = scene(1, f"""<div class="box" style="top:270px">
{EB(6.9, 'Where it shows')}
{H2(7.0, 'In the 9th house, the 5th, and the&nbsp;Sun.', 66)}
</div>
{chart(88, lambda sh: P.kundli(2, 2, 400, shade=sh, fs=30))}{chart(548, lambda sh: P.south_kundli(2, 2, 400, shade=sh, fs=30))}
<div class="cap" style="left:90px">{a(7.8, 'North Indian', 'fade')}</div><div class="cap" style="left:550px">{a(7.8, 'South Indian', 'fade')}</div>
<div class="box" style="top:1012px">
{HROW(8.7, '9', 'The 9th house', 'Bhagya, your father, your&nbsp;lineage.')}
{HROW(10.0, '5', 'The 5th house', 'Past merit, your&nbsp;children.')}
{HROW(11.2, '<svg width="56" height="56"><circle cx="28" cy="28" r="22" fill="none" stroke="' + SAF + '" stroke-width="5"/><circle cx="28" cy="28" r="5" fill="' + SAF + '"/></svg>', 'The Sun', 'Your father, your&nbsp;soul.')}
</div>""")

# scene 3: what forms it
s3 = scene(2, f"""<div class="box c">
{EB(13.0, 'What forms it')}
{H2(13.1, 'The combinations the tradition looks&nbsp;for.')}
{items(13.8, 0.75, [('1', 'The Sun with Rahu, Ketu or Saturn: the Sun eclipsed, <i>grahan</i>.'), ('2', 'Rahu, Ketu or Saturn in the 9th&nbsp;house.'),
                     ('3', 'The 9th lord weak, or pressed by Rahu, Ketu or&nbsp;Saturn.'), ('4', 'Rahu or Ketu in the 5th house, or a troubled 5th&nbsp;lord.'),
                     ('5', 'Saturn&#8217;s glance on the&nbsp;Sun.')], 42)}
{a(17.3, 'And more.', 'fade', f"font:italic 400 42px 'LO';color:{MUT};margin-top:26px")}
</div>""")

# scene 4: what it can bring
s4 = scene(3, f"""<div class="box c">
{EB(19.6, 'What it can bring')}
{H2(19.7, 'Effort that does not turn into&nbsp;fortune.')}
{items(20.4, 0.7, [('&#8212;', 'Work that stalls just before it&nbsp;succeeds.'), ('&#8212;', 'A marriage delayed, despite every&nbsp;effort.'),
                    ('&#8212;', 'Delay, or worry, around&nbsp;children.'), ('&#8212;', 'Money that comes, and does not&nbsp;stay.'),
                    ('&#8212;', 'Unrest at home that never quite&nbsp;ends.')], 44)}
{a(23.8, 'Many things can cause these. That is why the whole chart is read, never one&nbsp;placement.', 'fade', f"font:400 38px/1.45 'LO';color:{MUT};margin-top:30px")}
</div>""")

# scene 5: exceptions
s5 = scene(4, f"""<div class="box c">
{EB(25.8, 'Found it? Breathe.')}
{H2(25.9, 'Exceptions apply, and there are&nbsp;many.', 84)}
{items(26.7, 0.7, [('&#8212;', 'Jupiter with your Sun, or looking at your 9th&nbsp;house.'), ('&#8212;', 'Your Sun strong, in Aries or&nbsp;Leo.'),
                    ('&#8212;', 'A strong 9th&nbsp;lord.')], 46)}
{a(28.6, 'Pitru dosha is not a curse. It is a debt, and a debt can be&nbsp;paid.', 'up', f"font:600 52px/1.3 'PF';margin-top:40px;color:{SAF}")}
</div>""")

# scene 6: a diya (the Manglik post's clay diya, in the Sun's terracotta), and what the tradition does
def _flame(cx, y0, h, fill):
    y1 = y0 + h
    return (f'<path d="M{cx},{y0} C{cx+0.10*h:.1f},{y0+0.25*h:.1f} {cx+0.38*h:.1f},{y0+0.42*h:.1f} {cx+0.36*h:.1f},{y0+0.68*h:.1f} '
            f'C{cx+0.34*h:.1f},{y1-0.06*h:.1f} {cx+0.18*h:.1f},{y1} {cx},{y1} C{cx-0.18*h:.1f},{y1} {cx-0.34*h:.1f},{y1-0.06*h:.1f} {cx-0.36*h:.1f},{y0+0.68*h:.1f} '
            f'C{cx-0.38*h:.1f},{y0+0.42*h:.1f} {cx-0.10*h:.1f},{y0+0.25*h:.1f} {cx},{y0} Z" fill="{fill}"/>')
cx, cy = 540, 560
L, T, by = cx - 180, cx + 100, cy + 60
fh = 170; fx, fy = T - 14, by - 24 - fh
DIYA = f"""<svg class="art" width="1080" height="1920">
<circle cx="{cx}" cy="{cy}" r="231" fill="{P.GLYPH_RING}" opacity=".7"/>
<circle cx="{cx}" cy="{cy}" r="187" fill="none" stroke="{SAF}" stroke-opacity=".35" stroke-width="1.5"/>
<g id="glow"><circle cx="{fx}" cy="{fy + 110}" r="120" fill="#F6C98E" opacity=".35"/></g>
<g id="flame" style="transform-origin:{fx}px {by - 24}px">{_flame(fx, fy, fh, SAF)}{_flame(fx, fy + 56, fh - 62, '#D77B09')}{_flame(fx, fy + 102, fh - 114, '#FBE3C4')}</g>
<path d="M{L},{by} C{L+15},{by+95} {T-120},{by+105} {T},{by-22} Q{cx},{by+20} {L},{by} Z" fill="{SAF}"/>
<path d="M{L},{by} Q{cx-40},{by-26} {T},{by-22} Q{cx},{by+20} {L},{by} Z" fill="#BE7B63"/>
<path d="M{L+40},{by+44} C{cx-60},{by+68} {cx+10},{by+60} {T-95},{by+30}" fill="none" stroke="#F1DCD0" stroke-width="3" stroke-opacity=".7"/>
</svg>"""
s6 = scene(5, DIYA + f"""<div class="box" style="top:880px">
{a(31.2, 'A debt can be&nbsp;paid.', 'up', "font:700 96px/1.06 'PF'")}
{a(32.0, 'Tarpan · Shradh · Pinda daan<br>Pitru dosha&nbsp;puja', 'up', f"font:600 44px/1.35 'PF';color:{SAF};margin-top:24px")}
{a(32.9, 'The time is now. Pitru Paksha ends on Saturday 10&nbsp;October.', 'up', "font:400 42px/1.4 'LO';margin-top:24px")}
{a(34.0, 'Save this. Send it to your&nbsp;family.', 'up', f"font:600 46px/1.3 'IN';margin-top:42px;color:{IV}")}
{a(34.6, 'astroriver.com', 'fade', f"font:600 38px 'IN';letter-spacing:1px;margin-top:14px;color:{SAF}")}
</div>""")

def page(body, end, hook_end, css='', js=''):
    """The whole Reel as one page: the scenes, the river along the bottom, and the timeline script."""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{P.CSS}
html,body{{width:1080px;height:1920px}} .s{{width:1080px;height:1920px;overflow:hidden}}
.scene{{position:absolute;inset:0;opacity:0}}
.art{{position:absolute;left:0;top:0}}
.box{{position:absolute;left:90px;right:130px}}
.box.c{{top:270px;bottom:450px;display:flex;flex-direction:column;justify-content:center}}
.a{{will-change:transform,opacity}}
.eb{{font:600 26px 'IN';letter-spacing:5px;color:{SAF};text-transform:uppercase}}
.list{{margin-top:34px}}
.row{{display:flex;gap:26px;align-items:baseline;padding:22px 0;border-top:1.5px solid {LINE}}}
.row:last-child{{border-bottom:1.5px solid {LINE}}}
.row .k{{font:700 40px 'PF';color:{SAF};min-width:40px}} .row .v{{font-family:'LO';line-height:1.38}}
.ch{{position:absolute;top:510px}}
.cap{{position:absolute;top:932px;font:700 36px 'PF';color:{IV}}}
.hrow{{display:flex;gap:28px;align-items:center;padding:14px 0;border-top:1.5px solid {LINE};font:400 33px/1.32 'LO';color:{MUT}}}
.hrow:last-child{{border-bottom:1.5px solid {LINE}}}
.hrow b{{font:700 37px 'PF';color:{IV}}}
.hn{{font:700 64px 'PF';color:{SAF};min-width:70px;text-align:center;line-height:1}}
{css}
</style></head><body><div class="s">
<div class="wm" style="top:1180px">astroriver.com</div>
{body}
<svg class="art" width="1080" height="1920">
 <path d="M90,1478 L950,1478" stroke="{LINE}" stroke-width="4" stroke-linecap="round"/>
 <path id="prog" d="M90,1478 L950,1478" stroke="{RIVER}" stroke-width="5" stroke-linecap="round" pathLength="1000" stroke-dasharray="1000" stroke-dashoffset="1000"/>
</svg>
</div>
<script>
const E = 'cubic-bezier(.2,.7,.2,1)', ms = s => s * 1000;
const go = (el, kf, t, d, o = {{}}) => el.animate(kf, Object.assign({{delay: ms(t), duration: ms(d), fill: 'both', easing: E}}, o));
document.querySelectorAll('.scene').forEach(sc => {{
  const s = +sc.dataset.s, e = +sc.dataset.e, d = e - s, f = Math.min(.35 / d, .2);
  go(sc, [{{opacity: 0, offset: 0}}, {{opacity: 1, offset: f}}, {{opacity: 1, offset: 1 - f}}, {{opacity: 0, offset: 1}}], s, d, {{easing: 'linear'}});
}});
const K = {{
  up:   [{{opacity: 0, transform: 'translateY(38px)'}}, {{opacity: 1, transform: 'none'}}],
  left: [{{opacity: 0, transform: 'translateX(-46px)'}}, {{opacity: 1, transform: 'none'}}],
  fade: [{{opacity: 0}}, {{opacity: 1}}],
  wipe: [{{opacity: 0, clipPath: 'inset(0 0 100% 0)'}}, {{opacity: 1, clipPath: 'inset(0 0 0% 0)'}}],
  glow: [{{opacity: 0}}, {{opacity: 1}}],
}};
const D = {{up: .7, left: .6, fade: .8, wipe: 1.2, glow: .6}};
document.querySelectorAll('[data-k]').forEach(el => go(el, K[el.dataset.k], +el.dataset.t, D[el.dataset.k]));
// the Sun: rays turn slowly; Rahu slides in and covers it; the rays dim once it is covered
const rays = document.getElementById('rays'); rays.style.transformOrigin = '540px 580px';
go(rays, [{{transform: 'rotate(0deg)'}}, {{transform: 'rotate(24deg)'}}], 0, {hook_end}, {{easing: 'linear'}});
go(document.getElementById('rahu'), [{{transform: 'translate(330px,-60px)', opacity: 0}}, {{opacity: 1, offset: .25}}, {{transform: 'translate(0,0)', opacity: 1}}], 0.4, 2.4, {{easing: 'cubic-bezier(.4,0,.2,1)'}});
document.querySelector('#rays').animate([{{opacity: 1}}, {{opacity: .35}}], {{delay: ms(2.4), duration: ms(.8), fill: 'both', composite: 'replace'}});
// the diya: the flame breathes and the glow with it
const fl = document.getElementById('flame');
fl.animate([{{transform: 'scale(1,1) skewX(0deg)'}}, {{transform: 'scale(.94,1.07) skewX(2deg)'}}, {{transform: 'scale(1.03,.95) skewX(-2deg)'}}, {{transform: 'scale(.97,1.04) skewX(1deg)'}}, {{transform: 'scale(1,1) skewX(0deg)'}}],
  {{duration: 1300, iterations: Infinity, easing: 'ease-in-out'}});
document.getElementById('glow').animate([{{opacity: .8}}, {{opacity: 1}}, {{opacity: .7}}, {{opacity: .8}}], {{duration: 1700, iterations: Infinity, easing: 'ease-in-out'}});
// the river along the bottom fills as the Reel runs
go(document.getElementById('prog'), [{{strokeDashoffset: 1000}}, {{strokeDashoffset: 0}}], 0, {end}, {{easing: 'linear'}});
{js}
const all = document.getAnimations(); all.forEach(x => x.pause());
window.seek = t => all.forEach(x => x.currentTime = ms(t));
</script></body></html>"""

HTML = page(s1 + s2 + s3 + s4 + s5 + s6, END, S[0][1])

async def render(html=HTML, name='pitra-dosh-reel', end=END, times=None):
    fn = os.path.join(OUT, name + '.html'); open(fn, 'w').write(html)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(500)
        if times:
            for t in times:
                await pg.evaluate(f'seek({t})')
                await pg.screenshot(path=os.path.join(OUT, f'{name}-at-{t}s.png'))
        else:
            out = os.path.join(OUT, name + '.mp4')
            ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'png', '-i', '-',
                                   '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
            for i in range(int(end * FPS)):
                await pg.evaluate(f'seek({i / FPS})')
                ff.stdin.write(await pg.screenshot(type='png'))
            ff.stdin.close(); ff.wait()
            print(out, end, 's')
        await b.close()

if __name__ == '__main__':
    st = os.environ.get('REEL_STILLS')
    asyncio.run(render(times=[float(x) for x in st.split(',')] if st else None))
