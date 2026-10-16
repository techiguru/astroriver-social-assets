# Sarva Pitru Amavasya Reel in Hindi, for Fri 9 Oct 2026 (founder 8 Oct: approved the fresh Hindi lines, "make all").
# Same design as amavasya_reel.py (the Moon goes dark, stars, the lists, the diya; ASTRO RIVER at the top). Every line is
# taken from our Hindi page /hi/journal/pitru-paksha (the Amavasya paragraph, Ghata Chaturdashi, the home-shradh steps,
# the svadha mantra ॐ पितृभ्यः स्वधा नमः, the Delhi table for 10 Oct). No "today": the date is stated as "2026 में".
# Writes out/amavasya-reel-hi.mp4. REEL_STILLS=5,12 writes only those moments as PNGs.
import os, random, asyncio
import pitra_dosh as P, pitra_dosh_reel as R
SAF, MUT, IV = P.SAF, P.MUT, P.IV
END = 38.0
R.S = [(-0.35, 8.0), (8.0, 15.2), (15.2, 21.4), (21.4, 30.8), (30.8, END + 1)]
a, items, scene = R.a, R.items, R.scene
EB = lambda t, text: a(t, text, 'up', cls='eb')
H2 = lambda t, text, size=70: a(t, text, 'up', f"font:700 {size}px/1.3 'NSR';margin-top:12px")
DARK, LIGHT, GLOW, MOON = '#1E1712', '#F3EDE2', '#E9DFCF', '#D9C6A2'

# scene 1: the hook. The question is on screen from the first frame; the Moon goes dark, the screen with it, stars come
# out, and the answer comes in, light on dark. Then back to ivory.
random.seed(10)
STARS = ''.join(f'<circle cx="{random.randint(60, 1020)}" cy="{random.randint(250, 900)}" r="{random.choice([1.6, 2.2, 3])}" fill="{LIGHT}" opacity="{random.choice([.4, .6, .85])}"/>'
                for _ in range(46))
MOON_ART = f"""<div id="dark" style="position:absolute;inset:0;background:{DARK};opacity:0"></div>
<svg class="art" width="1080" height="1920">
<g id="stars" opacity="0">{STARS}</g>
<g id="halo"><circle cx="540" cy="580" r="300" fill="{P.GLYPH_RING}" opacity=".6"/>
<circle cx="540" cy="580" r="246" fill="none" stroke="{SAF}" stroke-opacity=".25" stroke-width="1.5"/></g>
<g id="rays"></g>
<circle cx="540" cy="580" r="150" fill="{MOON}" stroke="#C4AD84" stroke-width="2"/>
<circle cx="500" cy="540" r="22" fill="#C7B08A" opacity=".75"/><circle cx="585" cy="625" r="30" fill="#C7B08A" opacity=".65"/><circle cx="590" cy="525" r="12" fill="#C7B08A" opacity=".75"/><circle cx="470" cy="630" r="9" fill="#C7B08A" opacity=".6"/>
<defs><filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="8"/></filter></defs>
<g id="corona" opacity="0"><circle cx="540" cy="580" r="158" fill="none" stroke="{GLOW}" stroke-width="10" filter="url(#blur)" opacity=".7"/>
<circle cx="540" cy="580" r="153" fill="none" stroke="{GLOW}" stroke-width="2" opacity=".8"/></g>
<g id="rahu"><circle cx="542" cy="578" r="152" fill="#120D0A"/></g>
</svg>"""
s1 = scene(0, MOON_ART + f"""<div class="box" id="qs" style="top:960px">
{a(-0.7, 'पितृ पक्ष · अंतिम दिन', 'fade', f"font:600 34px 'NSD';color:{SAF}")}
{a(-0.7, 'पूर्वजों की तिथि याद&nbsp;नहीं?', 'up', "font:700 70px/1.35 'NSR';margin-top:14px")}
{a(1.2, 'या उनका नाम भी&nbsp;नहीं?', 'up', "font:700 70px/1.35 'NSR';margin-top:16px")}
</div>
<div class="box" style="top:940px;color:{LIGHT}">
{a(3.4, f'उनके लिए भी एक दिन है: <em style="color:#EBA884">सर्वपितृ&nbsp;अमावस्या</em>।', 'up', "font:700 80px/1.35 'NSR'")}
{a(4.6, 'पितृ पक्ष की अमावस्या, जिस दिन सभी पितरों का श्राद्ध होता&nbsp;है।', 'up', "font:400 44px/1.55 'NSD';margin-top:20px;opacity:.9")}
</div>""")

s2 = scene(1, f"""<div class="box c">
{EB(8.2, 'यह दिन किसके लिए है')}
{H2(8.3, 'सभी पितरों के लिए एक&nbsp;दिन।', 80)}
{items(9.0, 0.8, [('&#8212;', 'जिनकी देहांत-तिथि याद नहीं।'), ('&#8212;', 'वे पूर्वज जिनके नाम अब याद नहीं&nbsp;रहे।'),
                   ('&#8212;', 'जिनका स्वाभाविक देहांत चतुर्दशी को&nbsp;हुआ।')], 46)}
{a(11.8, 'बंगाल में यही महालया&nbsp;है।', 'fade', f"font:400 42px/1.5 'NSD';color:{MUT};margin-top:30px")}
</div>""")

s3 = scene(2, f"""<div class="box c">
{EB(15.4, '2026 में')}
{H2(15.5, 'शनिवार 10&nbsp;अक्टूबर।', 100)}
{items(16.2, 0.8, [('&#8212;', 'भारत, ब्रिटेन, दुबई, सिंगापुर, ऑस्ट्रेलिया: <b>शनिवार 10&nbsp;अक्टूबर</b>'), ('&#8212;', 'अमेरिका और कनाडा: <b>शुक्रवार 9&nbsp;अक्टूबर</b>')], 44)}
{a(17.8, 'श्राद्ध अपराह्न में किया जाता है। दिल्ली में: <span style="white-space:nowrap">13:17 से 15:36</span>।', 'up', "font:400 42px/1.55 'NSD';margin-top:30px")}
{a(18.6, 'अपने शहर का समय: <span style="font-family:IN">astroriver.com/hi/journal/pitru-paksha</span>', 'fade', f"font:600 30px/1.5 'NSD';color:{SAF};margin-top:20px")}
</div>""")

s4 = scene(3, f"""<div class="box c">
{EB(21.6, 'घर पर श्राद्ध कैसे करें')}
{H2(21.7, 'सरल है, पुरोहित के बिना भी हो सकता&nbsp;है।', 66)}
{items(22.4, 0.9, [('1', 'दक्षिण की ओर मुख करें। काले तिल मिला जल अर्पित करें, हर व्यक्ति का नाम&nbsp;लेकर।'),
                    ('2', 'हर अर्पण के साथ बोलें: ॐ पितृभ्यः स्वधा&nbsp;नमः।'),
                    ('3', 'हो सके तो पिंड दान करें, पके चावल के&nbsp;पिंड।'),
                    ('4', 'उनके नाम किसी को भोजन कराएं। कौए, गाय और कुत्ते के लिए भी हिस्सा&nbsp;निकालें।')], 40)}
</div>""")

s5 = scene(4, f'<div class="diya">{R.DIYA}</div>' + f"""<div class="box" style="top:760px">
{a(31.1, 'उन्हें नाम लेकर याद&nbsp;करें।', 'up', "font:700 84px/1.3 'NSR'")}
{a(31.9, 'पास में पुरोहित नहीं, या परिवार दूर-दूर है? संस्थान आपके परिवार के नाम से श्राद्ध और तर्पण की व्यवस्था करता&nbsp;है।', 'up', "font:400 40px/1.55 'NSD';margin-top:22px")}
{a(33.2, 'सेव करें, और परिवार के साथ शेयर&nbsp;करें।', 'up', f"font:600 44px/1.4 'NSD';margin-top:36px;color:{IV}")}
{a(33.8, 'astroriver.com', 'fade', f"font:600 38px 'IN';letter-spacing:1px;margin-top:10px;color:{SAF}")}
</div>""")

F = P.F
CSS = f"""
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-400-normal.woff2');font-weight:400;}}
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-600-normal.woff2');font-weight:600;}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-600-normal.woff2');font-weight:600;}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700;}}
em{{font-style:normal}}
.eb{{font:600 32px 'NSD';letter-spacing:0;text-transform:none}}
.row{{padding:18px 0}} .row .v{{font-family:'NSD';line-height:1.5}}
.ch{{top:546px}} .box.c{{top:310px}}
.diya{{position:absolute;inset:0;transform:translateY(-70px) scale(.82);transform-origin:540px 300px}}
"""
BRAND = f"""<div id="brand" style="position:absolute;left:0;right:0;top:176px;text-align:center;color:{IV}">
<div style="font:600 34px 'PF';letter-spacing:15px;padding-left:15px">ASTRO RIVER</div>
<svg width="220" height="26" style="display:block;margin:10px auto 0"><path d="M14,15 C60,4 90,24 110,13 C130,3 160,22 206,11" fill="none" stroke="{P.RIVER}" stroke-width="3" stroke-linecap="round"/>
<circle cx="14" cy="15" r="4.5" fill="{P.RIVER}"/><circle cx="206" cy="11" r="7" fill="none" stroke="{P.RIVER}" stroke-width="2"/></svg></div>"""
JS = """
go(document.getElementById('dark'), [{opacity: 0}, {opacity: 1}], 2.5, 0.9, {easing: 'ease-in-out'});
go(document.getElementById('halo'), [{opacity: 1}, {opacity: .1}], 2.5, 0.9, {easing: 'ease-in-out'});
go(document.getElementById('stars'), [{opacity: 0}, {opacity: 1}], 3.0, 1.4, {easing: 'ease-in-out'});
go(document.getElementById('corona'), [{opacity: 0}, {opacity: 1}], 2.8, 1.0);
go(document.getElementById('qs'), [{opacity: 1, transform: 'none'}, {opacity: 0, transform: 'translateY(-40px)'}], 2.5, 0.7);
go(document.getElementById('brand'), [{color: '%s', offset: 0}, {color: '%s', offset: .16}, {color: '%s', offset: .93}, {color: '%s', offset: 1}], 2.5, 5.5, {easing: 'linear'});
""" % (IV, LIGHT, LIGHT, IV)
HTML = R.page(s1 + s2 + s3 + s4 + s5 + BRAND, END, R.S[0][1], CSS, JS)

if __name__ == '__main__':
    st = os.environ.get('REEL_STILLS')
    asyncio.run(R.render(HTML, 'amavasya-reel-hi', END, [float(x) for x in st.split(',')] if st else None))
