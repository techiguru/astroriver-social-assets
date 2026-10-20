import os, asyncio
from playwright.async_api import async_playwright
K = os.path.abspath('AstroRiver-SealC-brand-kit'); F = 'file://' + K + '/'
PF = 'file:///home/user/astroriver-social-assets/build/fonts/'
def img(p, style=''): return f'<img src="{F}{p}" style="{style}">'
def sw(name, hexv, use, bg=None):
    bg = bg or hexv
    return f'<div class="sw"><div class="chip" style="background:{bg}"></div><b>{name}</b><span>{hexv}</span><i>{use}</i></div>'
NIGHT = 'radial-gradient(ellipse at 50% 40%,#23185C,#0F092A 78%)'
html = f"""<html><head><style>
@font-face{{font-family:'PF';src:url('{PF}PlayfairDisplay[wght].ttf');font-weight:400 900}}
@font-face{{font-family:'IN';src:url('{PF}Inter[opsz,wght].ttf');font-weight:100 900}}
@page{{size:A4;margin:0}}
body{{margin:0;font:400 10.5pt/1.5 IN;color:#3B3328;background:#FAF7F2}}
.pg{{width:210mm;height:297mm;box-sizing:border-box;padding:16mm 17mm 14mm;position:relative;page-break-after:always;overflow:hidden}}
.eb{{font:600 8pt IN;letter-spacing:.22em;color:#A97A24}}
h1{{font:700 34pt/1.05 PF;color:#1E1A14;margin:8px 0 10px}}
h2{{font:700 15.5pt PF;color:#1E1A14;margin:13px 0 8px;padding-top:10px;border-top:2px solid #D4AF5A;width:fit-content;border-top-width:0}}
h2:before{{content:'';display:block;width:34px;height:1.5px;background:#D4AF5A;margin-bottom:9px}}
p{{margin:0 0 6px}}
.row{{display:flex;gap:10px}}
.card{{flex:1;border:1px solid #E6DCCB;border-radius:10px;padding:9px;background:#fff}}
.card .art{{height:118px;border-radius:7px;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.card .art img{{max-height:100%;max-width:92%}}
.card p{{font-size:8.6pt;line-height:1.4;margin-top:7px}}
.card b{{color:#1E1A14}}
.sw{{flex:1;font-size:8pt;line-height:1.35}} .sw .chip{{height:24px;border-radius:6px;margin-bottom:5px;border:1px solid rgba(0,0,0,.08)}}
.sw b{{display:block;color:#1E1A14}} .sw span{{display:block;color:#6B5B4B}} .sw i{{display:block;font-style:normal;color:#7A6A58}}
.foot{{position:absolute;left:17mm;right:17mm;bottom:9mm;display:flex;justify-content:space-between;font-size:7.5pt;color:#8A7A66}}
ul{{margin:0;padding-left:16px}} li{{margin-bottom:4px;font-size:9pt;line-height:1.42}}
.ic{{display:flex;align-items:flex-end;gap:22px;margin-top:6px}} .ic div{{text-align:center;font-size:8pt;color:#6B5B4B}}
</style></head><body>

<div class="pg">
<div class="eb">BRAND KIT · 9 OCTOBER 2026 · SUN VERSION</div>
<h1>Astro River · Seal C</h1>
<p>The seal: the Sun, Surya, sits in the opening at the top of the ring, and a river of lights runs down from it and out through the bottom. The river comes from the sky and reaches the earth. Akash Ganga, the river of the sky, is the idea behind the name. One drawing, from a 16 px tab icon to a sign.</p>
<p>It replaces the gold AR crest as the logo. The crest is kept, with its own files, in the Crest kit folder.</p>
<h2>The logo</h2>
<div class="row">
<div class="card"><div class="art" style="background:{NIGHT}">{img('logo/astro-river-logo-stacked-on-dark-1024.png','height:108px')}</div><p><b>Main logo, on dark</b><br>astro-river-logo-stacked-on-dark. Posts, the About page, banners, the share picture.</p></div>
<div class="card"><div class="art" style="background:#FAF7F2;border:1px solid #EEE6D8">{img('logo/astro-river-logo-stacked-on-light-1024.png','height:108px')}</div><p><b>Main logo, on light</b><br>astro-river-logo-stacked-on-light. Ivory pages, letters, certificates.</p></div>
<div class="card"><div class="art" style="background:{NIGHT}">{img('logo/astro-river-seal-on-dark-1024.png','height:104px')}</div><p><b>The seal alone</b><br>astro-river-seal-on-dark / on-light. Where the name is already written beside it.</p></div>
</div>
<div class="row" style="margin-top:10px">
<div class="card" style="flex:2"><div class="art" style="background:#FAF7F2;border:1px solid #EEE6D8;height:80px">{img('logo/astro-river-logo-horizontal-on-light-1024.png','height:60px')}</div><p><b>Side by side</b> (astro-river-logo-horizontal-on-light / on-dark). The website header, letterhead, email signature. It uses the small seal.</p></div>
<div class="card"><div class="art" style="background:#FAF7F2;border:1px solid #EEE6D8;height:80px">{img('logo/astro-river-seal-small-on-light-1024.png','height:66px')}</div><p><b>Small seal</b> (seal-small). One bold ring, fewer lights: for anything under about 64 px.</p></div>
</div>
<h2>One colour</h2>
<div class="row">
<div class="card"><div class="art" style="background:#fff;border:1px solid #EEE;height:96px">{img('logo/astro-river-logo-stacked-one-colour-ink-1024.png','height:88px')}</div><p><b>Ink</b> (one-colour-ink). Rubber stamp, forms, the office printer, embossing.</p></div>
<div class="card"><div class="art" style="background:#0F092A;height:96px">{img('logo/astro-river-logo-stacked-one-colour-white-1024.png','height:88px')}</div><p><b>White</b> (one-colour-white). On photos and dark colours; embroidery on dark cloth.</p></div>
<div class="card"><div class="art" style="background:#FAF7F2;border:1px solid #EEE;height:96px">{img('logo/astro-river-seal-one-colour-gold-1024.png','height:86px')}</div><p><b>Gold</b> (seal-one-colour-gold). Gold foil on cards and certificates: give the printer the SVG.</p></div>
</div>
<div class="foot"><span>Astro River · Vedic Astrology · Est. 2008</span><span>1 of 3</span></div></div>

<div class="pg">
<h2 style="margin-top:0">Tab icon and app icons</h2>
<div class="ic">
<div>{img('icons/favicon-16.png','width:16px;height:16px')}<br>16 px</div><div>{img('icons/favicon-32.png','width:32px')}<br>32 px</div><div>{img('icons/favicon-48.png','width:48px')}<br>48 px</div>
<div>{img('icons/favicon-48.png','width:80px;image-rendering:pixelated')}<br>48 px, enlarged</div>
<div>{img('icons/apple-touch-icon.png','width:80px;border-radius:18px')}<br>iPhone home screen</div>
<div>{img('icons/pwa-maskable-512x512.png','width:80px;border-radius:50%')}<br>Android, round crop</div></div>
<p style="margin-top:10px">The tab icon is its own drawing: a heavier ring, a bolder sun, six lights, built round the ring's centre so it sits dead centre. favicon.svg is the same drawing as lines, sharp at every size. The home-screen icons sit on a night tile.</p>
<h2>Colours of the seal</h2>
<div class="row">
{sw('Seal gold', '#D4AF5A', 'ring and sun, on dark', 'linear-gradient(135deg,#F2D99A,#D4AF5A 55%,#B88A3A)')}
{sw('Deep seal gold', '#A97A24', 'ring and sun, on light', 'linear-gradient(135deg,#C79A3A,#A97A24 55%,#86601A)')}
{sw('River, on dark', '#F2D99A → #9A7BE0', 'gold turning violet', 'linear-gradient(90deg,#F2D99A,#9A7BE0)')}
{sw('River, on light', '#B5832A → #6D28D9', 'gold turning to the site purple', 'linear-gradient(90deg,#B5832A,#6D28D9)')}
{sw('Night', '#0F092A', 'behind the seal, the card', 'radial-gradient(circle,#23185C,#0F092A)')}
{sw('Night glow', '#23185C', 'the soft centre of the night', '#23185C')}
</div>
<h2>Colours of the website (as set in the site)</h2>
<div class="row">
{sw('Ivory', '#FAF7F2', 'public pages')}{sw('Ink', '#1E1A14', 'headings, text')}{sw('Deep purple', '#6D28D9', 'buttons, links, header name')}
{sw('Warm gold', '#D97706', 'small labels, lines')}{sw('Cosmic navy', '#0A1428', 'the client app')}{sw('Footer purple', '#1A0A2E', 'the site footer')}
</div>
<h2>Letters</h2>
<p><span style="font:700 13pt PF;color:#1E1A14">Playfair Display</span> for the name and headings, <b style="color:#1E1A14">Inter</b> for everything else, as on the website. In the logo files the name is already drawn as outlines, so no font is needed to open them. The name is two words: Astro River. Never AstroRiver.</p>
<h2>Using the logo</h2>
<ul>
<li><b>Sizes.</b> The full seal from about 64 px on screen or 15 mm in print. Smaller than that, the small seal. For tab and app icons, the icons folder. The stacked logo with its name needs at least 180 px or 40 mm so INSTITUTE · EST. 2008 stays readable.</li>
<li><b>Space around it.</b> At least a quarter of the seal's width empty on every side.</li>
<li><b>Keep it whole.</b> Do not stretch, tilt, crop the ring, add a glow or a shadow, or recolour it beyond the versions here. The sun stays at the top.</li>
<li><b>Backgrounds.</b> "On dark" for night, purple and black; "on light" for ivory and white; one colour on photos. Never on busy photos.</li>
<li><b>WhatsApp and phone galleries</b> show see-through pictures badly. There, use the profile picture or the share picture (both have their own night background).</li>
<li><b>Printers</b> get the SVG files: they print sharp at any size, including foil, embossing and signboards.</li>
</ul>
<div class="foot"><span>Astro River · Vedic Astrology · Est. 2008</span><span>2 of 3</span></div></div>

<div class="pg">
<h2 style="margin-top:0">Profile picture, share picture, X banner</h2>
<div class="row">
<div class="card"><div class="art" style="background:#fff;height:108px">{img('social/profile-picture-1080.png','height:104px;border-radius:50%')}</div><p><b>Profile picture</b> (1080 × 1080). Instagram, Facebook, WhatsApp, YouTube, LinkedIn, X. Safe for the round crop.</p></div>
<div class="card" style="flex:1.6"><div class="art" style="height:108px">{img('social/share-picture-1200x630.png','height:108px')}</div><p><b>Share picture</b> (1200 × 630). For posts and outside link previews. Pages on astroriver.com keep their own share pictures.</p></div>
</div>
<div class="card" style="margin-top:10px"><div class="art" style="height:78px">{img('social/x-banner-1500x500.jpg','height:78px')}</div><p><b>X banner</b> (1500 × 500), cut from the visiting card's river of stars.</p></div>
<h2>In posts</h2>
<div class="row">
<div class="card"><div class="art" style="height:140px">{img('preview/post-style-ivory.png','height:140px')}</div><p>On ivory: the seal in deep gold as the crest.</p></div>
<div class="card"><div class="art" style="height:140px">{img('preview/post-style-night.png','height:140px')}</div><p>On night: the seal as on the card.</p></div>
<div class="card" style="flex:1.3"><p style="margin-top:0">The seal sits at the top as the crest, at full strength. The sign-off at the bottom: a short gold line, ASTRO RIVER INSTITUTE, then EST. 2008 · ASTRORIVER.COM. A suggestion, not yet decided: festival posts could use the warm colours of the 2019 logo (marigold, maroon, orange, leaf green) with the seal.</p></div>
</div>
<h2>Visiting card</h2>
<div class="card"><div class="art" style="height:80px">{img('card/both-sides.png','height:78px')}</div><p><b>The river-of-stars card</b>, front and back, as made on 25 Sep. It fits the seal. Card files and printing notes are in the card folder. The back could carry the small seal beside the name: not done yet.</p></div>
<h2>Retired, kept on record</h2>
<p><b>The gold AR crest</b> (29 Sep): in AR Assets › Crest kit - gold AR emblem (Oct 2026, not the logo). Not to be used as the logo. <b>The 2019 astroriver.com logo</b>: in this kit's folder old-astroriver-com-logo, with its original vector files.</p>
<div class="foot"><span>Astro River · Vedic Astrology · Est. 2008</span><span>3 of 3</span></div></div>
</body></html>"""
open('sheet.html', 'w').write(html)
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.goto('file://' + os.path.abspath('sheet.html')); await pg.wait_for_timeout(1200)
        await pg.pdf(path=K + '/AstroRiver-brand-sheet-SealC.pdf', format='A4', print_background=True, prefer_css_page_size=True)
        await b.close()
asyncio.run(main())
