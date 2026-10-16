# Sarva Pitru Amavasya Reel, in English (founder 7 Oct: the topic is approved; a Reel stays on the profile, so no
# "today" or "this Saturday": the message holds every year and the date is stated as a fact, "In 2026: ...").
# Same moving design as the pitru dosha Reels: the Moon goes dark (amavasya) and stars come out, the lists come in line
# by line, a diya burns at the end; ASTRO RIVER at the top throughout. Every fact is from our article
# /journal/pitru-paksha ("Days that carry extra weight", "How to do shradh at home", the Delhi table for 10 Oct):
#   the new-moon day is for everyone; for anyone whose tithi is not known; for ancestors whose names are no longer known;
#   those who died a natural death on a Chaturdashi are remembered on the Amavasya; in Bengal it is Mahalaya;
#   Sat 10 Oct, Fri 9 Oct in North America; Delhi aparahna 13:17-15:36; tarpan facing south with water and black sesame;
#   svadha (the founder-approved plain form "Om Pitribhyah Swadha Namah"); pinda of cooked rice; a meal, with portions for
#   a crow, a cow and a dog; it can be kept at home and without a priest; the Institute arranges it in the family's name.
# Writes out/amavasya-reel.mp4. REEL_STILLS=5,12 writes only those moments as PNGs.
import os, random, asyncio
import pitra_dosh as P, pitra_dosh_reel as R
SAF, MUT, IV = P.SAF, P.MUT, P.IV
END = 38.0
R.S = [(-0.35, 8.0), (8.0, 15.2), (15.2, 21.4), (21.4, 30.8), (30.8, END + 1)]
a, items, scene = R.a, R.items, R.scene
EB = lambda t, text: a(t, text, 'up', cls='eb')
H2 = lambda t, text, size=70: a(t, text, 'up', f"font:700 {size}px/1.1 'PF';margin-top:16px")
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
{a(-0.7, 'Pitru Paksha · The last day', 'fade', '', 'eb')}
{a(-0.7, 'Don&#8217;t know the tithi your ancestor passed&nbsp;on?', 'up', "font:700 70px/1.1 'PF';margin-top:16px")}
{a(1.2, 'Or even their&nbsp;name?', 'up', "font:700 70px/1.1 'PF';margin-top:20px")}
</div>
<div class="box" style="top:950px;color:{LIGHT}">
{a(3.4, f'There is a day for them: <em style="color:{GLOW}">Sarva Pitru&nbsp;Amavasya</em>.', 'up', "font:700 84px/1.1 'PF'")}
{a(4.6, 'The new-moon day that ends Pitru Paksha. The shradh for&nbsp;everyone.', 'up', "font:400 44px/1.45 'LO';margin-top:24px;opacity:.9")}
</div>""")

# scene 2: who it is for
s2 = scene(1, f"""<div class="box c">
{EB(8.2, 'Who it is for')}
{H2(8.3, 'One day, for every&nbsp;ancestor.', 80)}
{items(9.0, 0.8, [('&#8212;', 'Anyone whose tithi you do not know.'), ('&#8212;', 'Ancestors whose names are no longer&nbsp;remembered.'),
                   ('&#8212;', 'Those who died a natural death on a&nbsp;Chaturdashi.')], 44)}
{a(11.8, 'In Bengal, this morning is Mahalaya: the fortnight of the ancestors turns into the fortnight of the&nbsp;Goddess.', 'fade', f"font:italic 400 40px/1.45 'LO';color:{MUT};margin-top:30px")}
</div>""")

# scene 3: when, stated as a dated fact so it never reads "today"
s3 = scene(2, f"""<div class="box c">
{EB(15.4, 'In 2026')}
{H2(15.5, 'Saturday 10&nbsp;October.', 100)}
{items(16.2, 0.8, [('&#8212;', 'India, UK, Dubai, Singapore, Australia: <b>Saturday 10&nbsp;October</b>.'), ('&#8212;', 'USA and Canada: <b>Friday 9&nbsp;October</b>.')], 44)}
{a(17.8, 'It is done in the afternoon, the <i>aparahna</i>. In Delhi: 13:17 to&nbsp;15:36.', 'up', "font:400 42px/1.45 'LO';margin-top:30px")}
{a(18.6, 'Hours for your city: astroriver.com/journal/pitru-paksha', 'fade', f"font:600 32px/1.4 'IN';color:{SAF};margin-top:22px")}
</div>""")

# scene 4: how to keep it at home
s4 = scene(3, f"""<div class="box c">
{EB(21.6, 'How to keep it at home')}
{H2(21.7, 'Simple, and possible without a&nbsp;priest.', 72)}
{items(22.4, 0.9, [('1', 'Face south. Offer water with black sesame, naming each&nbsp;person.'),
                    ('2', 'With each offering, say <i>svadha</i>: Om Pitribhyah Swadha&nbsp;Namah.'),
                    ('3', 'Offer pinda, balls of cooked rice, if you&nbsp;can.'),
                    ('4', 'Feed someone in their name. Set portions aside for a crow, a cow and a&nbsp;dog.')], 42)}
</div>""")

# scene 5: the diya and the close
s5 = scene(4, f'<div class="diya">{R.DIYA}</div>' + f"""<div class="box" style="top:780px">
{a(31.1, 'Remember them by&nbsp;name.', 'up', "font:700 92px/1.08 'PF'")}
{a(31.9, 'No priest near, or the family far apart? The Institute arranges shradh and tarpan in your family&#8217;s&nbsp;name.', 'up', f"font:400 42px/1.45 'LO';margin-top:26px")}
{a(33.2, 'Save this. Send it to your&nbsp;family.', 'up', f"font:600 46px/1.3 'IN';margin-top:40px;color:{IV}")}
{a(33.8, 'astroriver.com', 'fade', f"font:600 38px 'IN';letter-spacing:1px;margin-top:12px;color:{SAF}")}
</div>""")

CSS = """
em{font-style:italic}
.ch{top:546px} .box.c{top:310px}
.diya{position:absolute;inset:0;transform:translateY(-70px) scale(.82);transform-origin:540px 300px}
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
    asyncio.run(R.render(HTML, 'amavasya-reel', END, [float(x) for x in st.split(',')] if st else None))
