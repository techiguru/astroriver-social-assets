# Pitru dosha Reel in Hindi (founder 5 Oct: the carousel goes in English, the Reel in Hindi; Hindi written fresh for
# Hindi viewers, not translated; every line approved by the founder). Same moving design as pitra_dosh_reel.py: the Sun
# is eclipsed, both charts draw in and light their houses, the lists come in line by line, a diya burns at the end.
# Two headings use the words people search: "पितृ दोष के लक्षण" and "पितृ दोष के उपाय". The rites and their words
# (पिंड दान; कौए, गाय और कुत्ते; सर्वपितृ अमावस्या) follow our Hindi page /hi/journal/pitru-paksha.
# Writes out/pitra-dosh-reel-hi.mp4. REEL_STILLS=5,12 writes only those moments as PNGs.
import os, re, asyncio
import pitra_dosh as P, pitra_dosh_reel as R
SAF, MUT, IV = P.SAF, P.MUT, P.IV
END = 44.5
R.S = [(-0.35, 8.0), (8.0, 14.8), (14.8, 22.2), (22.2, 29.4), (29.4, 36.0), (36.0, END + 1)]
a, items, scene = R.a, R.items, R.scene
EB = lambda t, text: a(t, text, 'up', cls='eb')
H2 = lambda t, text, size=66: a(t, text, 'up', f"font:700 {size}px/1.3 'NSR';margin-top:12px")

# scene 1: the hook. The question is on screen from the first frame; Rahu covers the Sun completely, the corona lights,
# the screen goes dark (bhagya blocked), and the answer comes in, light on dark. Then back to ivory for the charts.
DARK, LIGHT, GLOW = '#1E1712', '#F3EDE2', '#EBA884'
ECL_HI = f"""<div id="dark" style="position:absolute;inset:0;background:{DARK};opacity:0"></div>
<svg class="art" width="1080" height="1920">
<g id="halo"><circle cx="540" cy="580" r="300" fill="{P.GLYPH_RING}" opacity=".7"/>
<circle cx="540" cy="580" r="246" fill="none" stroke="{SAF}" stroke-opacity=".3" stroke-width="1.5"/></g>
<g id="rays">{''.join(f'<line x1="540" y1="{580-176}" x2="540" y2="{580-222}" stroke="{SAF}" stroke-width="11" stroke-linecap="round" opacity=".6" transform="rotate({d} 540 580)"/>' for d in range(0, 360, 30))}</g>
<circle cx="540" cy="580" r="150" fill="{SAF}"/>
<defs><filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="9"/></filter></defs>
<g id="corona" opacity="0"><circle cx="540" cy="580" r="160" fill="none" stroke="{GLOW}" stroke-width="16" filter="url(#blur)"/>
<circle cx="540" cy="580" r="154" fill="none" stroke="#FBE3C4" stroke-width="3"/></g>
<g id="rahu"><circle cx="544" cy="577" r="151" fill="#120D0A"/></g>
</svg>"""
s1 = scene(0, ECL_HI + f"""<div class="box" id="qs" style="top:950px">
{a(-0.7, 'पितृ पक्ष 2026', 'fade', f"font:600 34px 'NSD';color:{SAF}")}
{a(-0.7, 'बनते-बनते काम क्यों बिगड़ जाते&nbsp;हैं?', 'up', "font:700 66px/1.4 'NSR';margin-top:14px")}
{a(1.1, 'मेहनत पूरी, फिर भी भाग्य साथ क्यों नहीं&nbsp;देता?', 'up', "font:700 66px/1.4 'NSR';margin-top:18px")}
</div>
<div class="box" style="top:950px;color:{LIGHT}">
{a(3.4, f'कहीं यह <em style="color:{GLOW}">पितृ दोष</em> तो&nbsp;नहीं?', 'up', "font:700 96px/1.3 'NSR'")}
{a(4.6, 'पितृ दोष पितरों का क्रोध नहीं है। यह उनका ऋण है, जो <span style="white-space:nowrap">पीढ़ी-दर-पीढ़ी</span> चलता&nbsp;है।', 'up', "font:400 42px/1.55 'NSD';margin-top:18px;opacity:.9")}
</div>""")
JS = """
go(document.getElementById('dark'), [{opacity: 0}, {opacity: 1}], 2.5, 0.9, {easing: 'ease-in-out'});
go(document.getElementById('halo'), [{opacity: 1}, {opacity: .12}], 2.5, 0.9, {easing: 'ease-in-out'});
go(document.getElementById('corona'), [{opacity: 0, transform: 'scale(.92)'}, {opacity: 1, transform: 'scale(1)'}], 2.7, 0.9);
document.getElementById('corona').style.transformOrigin = '540px 580px';
go(document.getElementById('qs'), [{opacity: 1, transform: 'none'}, {opacity: 0, transform: 'translateY(-40px)'}], 2.5, 0.7);
"""

def hindi_lagna(svg):
    return re.sub(r'font-family="IN" font-weight="600" font-size="\d+" letter-spacing="[\d.]+"([^>]*)>LAGNA<',
                  r'font-family="NSD" font-weight="600" font-size="19"\1>लग्न<', svg)
def chart(x, fn, t):
    return (f'<svg class="ch" data-t="{t[0]}" data-k="wipe" style="left:{x}px" width="404" height="404">{hindi_lagna(fn(()))}</svg>'
            f'<svg class="ch" data-t="{t[1]}" data-k="glow" style="left:{x}px" width="404" height="404">{hindi_lagna(fn((9,)))}</svg>'
            f'<svg class="ch" data-t="{t[2]}" data-k="glow" style="left:{x}px" width="404" height="404">{hindi_lagna(fn((5, 9)))}</svg>')
HROW = lambda t, n, title, what: a(t, f'<span class="hn">{n}</span><span><b>{title}</b><br>{what}</span>', 'left', cls='hrow')
SUN = f'<svg width="56" height="56"><circle cx="28" cy="28" r="22" fill="none" stroke="{SAF}" stroke-width="5"/><circle cx="28" cy="28" r="5" fill="{SAF}"/></svg>'
CT = (8.8, 11.2, 12.4)
s2 = scene(1, f"""<div class="box" style="top:300px">
{EB(8.3, 'कुंडली में कहाँ देखें')}
{H2(8.4, 'सूर्य, नवम भाव और पंचम&nbsp;भाव')}
</div>
{chart(88, lambda sh: P.kundli(2, 2, 400, shade=sh, fs=30), CT)}{chart(548, lambda sh: P.south_kundli(2, 2, 400, shade=sh, fs=30), CT)}
<div class="cap" style="left:90px">{a(9.3, 'उत्तर भारतीय कुंडली', 'fade')}</div><div class="cap" style="left:550px">{a(9.3, 'दक्षिण भारतीय कुंडली', 'fade')}</div>
<div class="box" style="top:1046px">
{HROW(10.0, SUN, 'सूर्य', 'पिता का कारक&nbsp;ग्रह।')}
{HROW(11.2, '9', 'नवम भाव', 'भाग्य, पिता और पूर्वजों का&nbsp;घर।')}
{HROW(12.4, '5', 'पंचम भाव', 'पूर्व जन्म का पुण्य, और&nbsp;संतान।')}
</div>""")

s3 = scene(2, f"""<div class="box c">
{EB(15.0, 'पितृ दोष कैसे बनता है')}
{H2(15.1, 'ज्योतिष में ये योग देखे जाते&nbsp;हैं')}
{items(15.8, 0.8, [('1', 'सूर्य के साथ राहु या केतु। इसे ग्रहण योग कहते&nbsp;हैं।'), ('2', 'सूर्य के साथ शनि, या सूर्य पर शनि की&nbsp;दृष्टि।'),
                    ('3', 'नवम भाव में राहु, केतु या&nbsp;शनि।'), ('4', 'नवम भाव का स्वामी कमज़ोर या&nbsp;पीड़ित।'),
                    ('5', 'पंचम भाव में राहु या केतु, या पंचम भाव का स्वामी&nbsp;पीड़ित।')], 40)}
{a(19.8, 'ये प्रमुख योग हैं। और भी&nbsp;हैं।', 'fade', f"font:400 38px/1.5 'NSD';color:{MUT};margin-top:24px")}
</div>""")

s4 = scene(3, f"""<div class="box c">
{EB(22.4, 'जीवन में कैसे दिखता है')}
{H2(22.5, 'पितृ दोष के लक्षण', 76)}
{items(23.2, 0.75, [('&#8212;', 'बनते काम आख़िरी समय पर अटक जाते&nbsp;हैं।'), ('&#8212;', 'शादी में बार-बार रुकावट आती&nbsp;है।'),
                     ('&#8212;', 'संतान सुख में देरी या चिंता रहती&nbsp;है।'), ('&#8212;', 'पैसा आता है, पर घर में बरकत नहीं&nbsp;रहती।'),
                     ('&#8212;', 'घर में बिना वजह कलह और अशांति रहती&nbsp;है।')], 40)}
{a(26.9, 'पर ये लक्षण दूसरे कारणों से भी हो सकते हैं। इसलिए फ़ैसला पूरी कुंडली देखकर होता है, किसी एक योग से&nbsp;नहीं।', 'fade', f"font:400 35px/1.55 'NSD';color:{MUT};margin-top:26px")}
</div>""")

s5 = scene(4, f"""<div class="box c">
{EB(29.6, 'घबराइए नहीं')}
{H2(29.7, 'हर योग दोष नहीं&nbsp;बनता।', 84)}
{a(30.3, 'इन स्थितियों में दोष का असर कम हो जाता&nbsp;है:', 'up', f"font:400 38px/1.5 'NSD';color:{MUT};margin-top:16px")}
{items(30.9, 0.7, [('&#8212;', 'सूर्य के साथ गुरु हो, या नवम भाव पर गुरु की दृष्टि हो।'), ('&#8212;', 'सूर्य मेष या सिंह राशि में बलवान&nbsp;हो।'),
                    ('&#8212;', 'नवम भाव का स्वामी बलवान&nbsp;हो।')], 40)}
{a(33.0, 'पितृ दोष शाप नहीं, ऋण है।<br>और ऋण उतारा जा सकता&nbsp;है।', 'up', f"font:600 48px/1.45 'NSR';margin-top:34px;color:{SAF}")}
</div>""")

s6 = scene(5, f'<div class="diya">{R.DIYA}</div>' + f"""<div class="box" style="top:760px">
{a(36.3, 'पितृ दोष के उपाय', 'up', "font:700 84px/1.3 'NSR'")}
{a(37.0, 'तर्पण, श्राद्ध, पिंड दान<br>और पितृ दोष&nbsp;पूजा।', 'up', f"font:600 44px/1.45 'NSR';color:{SAF};margin-top:14px")}
{a(37.8, 'पितरों के नाम भोजन कराएँ। कौए, गाय और कुत्ते के लिए भी हिस्सा&nbsp;निकालें।', 'up', "font:400 37px/1.55 'NSD';margin-top:18px")}
{a(38.8, 'इसका समय अभी है: पितृ पक्ष शनिवार 10 अक्टूबर, <span style="white-space:nowrap">सर्वपितृ अमावस्या</span> को समाप्त&nbsp;होगा।', 'up', "font:400 37px/1.55 'NSD';margin-top:14px")}
{a(40.0, 'सेव करें, और परिवार के साथ शेयर&nbsp;करें।', 'up', f"font:600 44px/1.4 'NSD';margin-top:30px;color:{IV}")}
{a(40.5, 'astroriver.com', 'fade', f"font:600 38px 'IN';letter-spacing:1px;margin-top:10px;color:{SAF}")}
</div>""")

F = P.F
CSS = f"""
@font-face{{font-family:'NSD';src:url('{F}noto-sans-devanagari-devanagari-400-normal.woff2');font-weight:400;}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-600-normal.woff2');font-weight:600;}}
@font-face{{font-family:'NSR';src:url('{F}noto-serif-devanagari-devanagari-700-normal.woff2');font-weight:700;}}
em{{font-style:normal}}
.eb{{font:600 32px 'NSD';letter-spacing:0;text-transform:none}}
.row{{padding:18px 0}} .row .v{{font-family:'NSD';line-height:1.5}}
.cap{{font:600 32px 'NSD'}}
.hrow{{font:400 34px/1.45 'NSD'}} .hrow b{{font:600 38px 'NSD'}}
.ch{{top:546px}} .cap{{top:968px}} .box.c{{top:310px}}
.diya{{position:absolute;inset:0;transform:translateY(-70px) scale(.82);transform-origin:540px 300px}}
"""
# the wordmark at the top (founder 5 Oct: the top of the Reel looked empty): ASTRO RIVER in spaced capitals with a
# short river line under it, centred so it sits between Instagram's "Reels" label and camera icon. It stays for the
# whole Reel and turns light while the screen is dark.
BRAND = f"""<div id="brand" style="position:absolute;left:0;right:0;top:176px;text-align:center;color:{IV}">
<div style="font:600 34px 'PF';letter-spacing:15px;padding-left:15px">ASTRO RIVER</div>
<svg width="220" height="26" style="display:block;margin:10px auto 0"><path d="M14,15 C60,4 90,24 110,13 C130,3 160,22 206,11" fill="none" stroke="{P.RIVER}" stroke-width="3" stroke-linecap="round"/>
<circle cx="14" cy="15" r="4.5" fill="{P.RIVER}"/><circle cx="206" cy="11" r="7" fill="none" stroke="{P.RIVER}" stroke-width="2"/></svg></div>"""
JS += """
go(document.getElementById('brand'), [{color: '%s', offset: 0}, {color: '%s', offset: .16}, {color: '%s', offset: .93}, {color: '%s', offset: 1}], 2.5, 5.5, {easing: 'linear'});
""" % (IV, LIGHT, LIGHT, IV)
HTML = R.page(s1 + s2 + s3 + s4 + s5 + s6 + BRAND, END, R.S[0][1], CSS, JS)

if __name__ == '__main__':
    st = os.environ.get('REEL_STILLS')
    asyncio.run(R.render(HTML, 'pitra-dosh-reel-hi', END, [float(x) for x in st.split(',')] if st else None))
