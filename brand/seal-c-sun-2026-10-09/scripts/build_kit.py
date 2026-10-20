# Builds the Seal C brand kit into ./AstroRiver-SealC-brand-kit
import os, shutil, asyncio, hashlib
import seal as S, textpath as T
from PIL import Image
from playwright.async_api import async_playwright
OUT = os.path.abspath('AstroRiver-SealC-brand-kit')
for d in ['logo', 'icons', 'social', 'card', 'preview']:
    os.makedirs(f'{OUT}/{d}', exist_ok=True)
SP = '/tmp/claude-0/-home-user/5116f683-b12f-5c43-a9c9-1c4e80d8bd09/scratchpad'
INK, IVORY, PURPLE, TEXT_D, GOLD_D, GOLD_L = '#1E1A14', '#FAF7F2', '#6D28D9', '#F4ECDC', '#D4AF5A', '#A97A24'
NIGHT_BG = f'<radialGradient id="bg" cx="50%" cy="42%" r="70%"><stop offset="0" stop-color="{S.NIGHT_GLOW}"/><stop offset="1" stop-color="{S.NIGHT}"/></radialGradient>'
svgs = {}   # name -> svg text

def put(name, text):
    svgs[name] = text
    with open(f'{OUT}/{name}', 'w', newline='\n') as f: f.write(text)

# 1. the seal on its own
for kind in ['full', 'small']:
    fn = getattr(S, kind); box = S.BOX[kind]; tag = '' if kind == 'full' else '-small'
    for label, kw in [('on-dark', dict(scheme=S.DARK)), ('on-light', dict(scheme=S.LIGHT))]:
        put(f'logo/astro-river-seal{tag}-{label}.svg', S.svg_doc(*fn(**kw), box))
for label, col in [('one-colour-ink', INK), ('one-colour-white', '#FFFFFF'), ('one-colour-gold', GOLD_L)]:
    put(f'logo/astro-river-seal-{label}.svg', S.svg_doc(*S.full(one=col), S.BOX['full']))

# 2. the seal with the name: stacked (under) and horizontal (beside)
def stacked(scheme, name_col, tag_col, one=None, bg=None):
    d, body = S.full(scheme=scheme, one=one)
    bx, by, bw, bh = S.BOX['full']
    sc = 1.0  # seal drawn at its own size, 408 tall
    name, wn = T.text('ASTRO RIVER', T.PLAYFAIR(600), 84, tracking=.14, fill=name_col)
    tag, wt = T.text('INSTITUTE · EST. 2008', T.INTER(500), 25, tracking=.34, fill=tag_col)
    W = max(wn, wt, bw) + 80; H = bh + 60 + 84 + 30 + 25 + 60
    cx = W / 2
    g_seal = f'<g transform="translate({cx - 200:.2f},{40 - by:.2f})">{body}</g>'
    yname = 40 + bh + 50 + 62
    name, _ = T.text('ASTRO RIVER', T.PLAYFAIR(600), 84, x=cx + 0.07 * 84, y=yname, tracking=.14, fill=name_col, anchor='middle')
    tag, _ = T.text('INSTITUTE · EST. 2008', T.INTER(500), 25, x=cx + .17 * 25, y=yname + 58, tracking=.34, fill=tag_col, anchor='middle')
    back = f'<rect width="{W:.0f}" height="{H:.0f}" fill="{bg}"/>' if bg else ''
    defs = d + (NIGHT_BG if bg == 'url(#bg)' else '')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}"><defs>{defs}</defs>{back}{g_seal}{name}{tag}</svg>\n'

def horizontal(scheme, name_col, tag_col, one=None):
    d, body = S.small(scheme=scheme, one=one)
    bx, by, bw, bh = S.BOX['small']
    k = 120 / bh  # seal 120 tall
    name, wn = T.text('Astro River Institute', T.PLAYFAIR(700), 56, tracking=-.01, fill=name_col)
    tag, wt = T.text('VEDIC ASTROLOGY · EST. 2008', T.INTER(500), 15, tracking=.3, fill=tag_col)
    gap = 30; x_text = 20 + bw * k + gap
    W = x_text + max(wn, wt) + 20; H = 160
    g_seal = f'<g transform="translate({20 - bx * k:.2f},{20 - by * k:.2f}) scale({k:.4f})">{body}</g>'
    name, _ = T.text('Astro River Institute', T.PLAYFAIR(700), 56, x=x_text, y=88, tracking=-.01, fill=name_col)
    tag, _ = T.text('VEDIC ASTROLOGY · EST. 2008', T.INTER(500), 15, x=x_text + 2, y=122, tracking=.3, fill=tag_col)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H}"><defs>{d}</defs>{g_seal}{name}{tag}</svg>\n'

put('logo/astro-river-logo-stacked-on-dark.svg', stacked(S.DARK, TEXT_D, GOLD_D))
put('logo/astro-river-logo-stacked-on-light.svg', stacked(S.LIGHT, INK, GOLD_L))
put('logo/astro-river-logo-stacked-one-colour-ink.svg', stacked(None, INK, INK, one=INK))
put('logo/astro-river-logo-stacked-one-colour-white.svg', stacked(None, '#FFFFFF', '#FFFFFF', one='#FFFFFF'))
put('logo/astro-river-logo-horizontal-on-light.svg', horizontal(S.LIGHT, PURPLE, GOLD_L))
put('logo/astro-river-logo-horizontal-on-dark.svg', horizontal(S.DARK, TEXT_D, GOLD_D))

# 3. icons: the icon drawing on a night disc (favicon) or a night tile (home screen)
fd, fb = S.icon(S.DARK, uid='fi')
put('icons/favicon.svg', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 -10 420 420">'
    f'<defs>{fd}<radialGradient id="bgf" cx="50%" cy="45%" r="60%"><stop offset="0" stop-color="{S.NIGHT_GLOW}"/><stop offset="1" stop-color="{S.NIGHT}"/></radialGradient></defs>'
    f'<circle cx="200" cy="200" r="210" fill="url(#bgf)"/>{fb}</svg>\n')

def tile(scale, uid, kind='small'):
    """square night tile, the seal centred on its ring at `scale` of the tile"""
    d, b = getattr(S, kind)(S.DARK, uid=uid)
    k = 512 * scale / 400
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">'
            f'<defs>{d}<radialGradient id="bg{uid}" cx="50%" cy="45%" r="72%"><stop offset="0" stop-color="{S.NIGHT_GLOW}"/><stop offset="1" stop-color="{S.NIGHT}"/></radialGradient></defs>'
            f'<rect width="512" height="512" fill="url(#bg{uid})"/><g transform="translate({256 - 200 * k:.2f},{256 - 200 * k:.2f}) scale({k:.4f})">{b}</g></svg>\n')
TILE = tile(.74, 't')            # apple-touch and pwa "any"
MASK = tile(.56, 'm')            # maskable: the whole seal inside the central safe circle

# 4. social and preview pages (HTML rendered to pictures)
def svg_inline(t): return t.replace('<svg xmlns="http://www.w3.org/2000/svg"', '<svg')
PF = 'file:///home/user/astroriver-social-assets/build/fonts/'
FONTS = (f"@font-face{{font-family:'PF';src:url('{PF}PlayfairDisplay[wght].ttf');font-weight:400 900}}"
         f"@font-face{{font-family:'PF';src:url('{PF}PlayfairDisplay-Italic[wght].ttf');font-weight:400 900;font-style:italic}}"
         f"@font-face{{font-family:'IN';src:url('{PF}Inter[opsz,wght].ttf');font-weight:100 900}}")
NIGHT_CSS = f'radial-gradient(ellipse at 50% 40%,{S.NIGHT_GLOW},{S.NIGHT} 75%)'

def seal_box(kind, scheme, uid, h, ring_centre=False):
    d, b = getattr(S, kind)(scheme, uid=uid)
    box = S.BOX[kind] if not ring_centre else (-30, -30, 460, 460)
    w = h * box[2] / box[3]
    return f'<svg viewBox="{box[0]} {box[1]} {box[2]} {box[3]}" width="{w:.0f}" height="{h}"><defs>{d}</defs>{b}</svg>'

PROFILE = f'<div style="width:1080px;height:1080px;background:{NIGHT_CSS};display:flex;align-items:center;justify-content:center">{seal_box("full", S.DARK, "p", 1000, True)}</div>'
OG = f"""<div style="width:1200px;height:630px;background:{NIGHT_CSS};display:flex;align-items:center;justify-content:center;gap:64px;font-family:IN">
{seal_box('full', S.DARK, 'o', 420)}<div><div style="font:600 64px 'PF';letter-spacing:.12em;color:{TEXT_D}">ASTRO RIVER</div>
<div style="font:500 20px IN;letter-spacing:.34em;color:{GOLD_D};margin-top:20px">INSTITUTE &nbsp;·&nbsp; EST. 2008</div>
<div style="font:400 26px IN;color:#C3BADF;margin-top:40px">Vedic astrology · Jalandhar · astroriver.com</div></div></div>"""

def post(dark):
    bg = NIGHT_CSS if dark else '#F3EDE2'
    ink, mut, acc = (TEXT_D, '#C3BADF', GOLD_D) if dark else (INK, '#5E4F40', '#A8590A')
    return f"""<div style="width:1080px;height:1350px;background:{bg};position:relative;overflow:hidden;font-family:IN">
<div style="position:absolute;left:0;right:0;top:110px;display:flex;justify-content:center">{seal_box('full', S.DARK if dark else S.LIGHT, 'c' + str(int(dark)), 270)}</div>
<div style="position:absolute;left:90px;right:90px;top:510px;text-align:center">
<div style="font:600 30px IN;letter-spacing:8px;color:{acc}">TODAY'S SKY &nbsp;·&nbsp; FRIDAY 9 OCTOBER</div>
<div style="font:700 104px/1.08 'PF';color:{ink};margin-top:34px">The Moon is in<br><em style="font-weight:600">Uttara Phalguni</em></div>
<div style="font:400 46px/1.4 IN;color:{mut};margin-top:30px">until 21:19 IST</div></div>
<div style="position:absolute;left:0;right:0;bottom:110px;text-align:center">
<div style="width:90px;height:2px;background:{acc};margin:0 auto 34px;opacity:.8"></div>
<div style="font:600 36px 'PF';letter-spacing:.2em;padding-left:.2em;color:{ink}">ASTRO RIVER INSTITUTE</div>
<div style="font:500 20px IN;letter-spacing:.4em;padding-left:.4em;color:{acc};margin-top:16px">EST. 2008 &nbsp;·&nbsp; ASTRORIVER.COM</div></div></div>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        async def shot(html, w, h, path, transparent=False, bg='#fff'):
            await pg.set_viewport_size({'width': w, 'height': h})
            fn = path + '.tmp.html'
            open(fn, 'w').write(f"<html><head><style>{FONTS} html,body{{margin:0;background:{'transparent' if transparent else bg}}}</style></head><body>{html}</body></html>")
            await pg.goto('file://' + fn); await pg.wait_for_timeout(400)
            await pg.screenshot(path=path, omit_background=transparent); os.remove(fn)
        async def svg_png(svgtext, path, w, transparent=True, bg='#fff'):
            import re
            vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', svgtext).group(1).split()]
            h = round(w * vb[3] / vb[2])
            await shot(svg_inline(svgtext).replace('<svg ', f'<svg width="{w}" height="{h}" style="display:block" ', 1), w, h, path, transparent, bg)
        # logo PNGs: 4096 for print and big uses, 1024 for everyday
        for name, t in list(svgs.items()):
            if not name.startswith('logo/'): continue
            base = f'{OUT}/' + name[:-4]
            big = 4096 if 'horizontal' not in name else 3000
            await svg_png(t, f'{base}-{big}.png', big)
            await svg_png(t, f'{base}-1024.png', 1024)
        # black-and-white for the office printer: ink stacked logo on white
        await svg_png(svgs['logo/astro-river-logo-stacked-one-colour-ink.svg'], f'{OUT}/logo/astro-river-logo-black-white.png', 2048, transparent=False)
        # icons
        for s in (16, 32, 48, 256):
            await svg_png(svgs['icons/favicon.svg'], f'{OUT}/icons/favicon-{s}.png', s)
        await svg_png(TILE, f'{OUT}/icons/apple-touch-icon.png', 180, transparent=False)
        await svg_png(TILE, f'{OUT}/icons/pwa-192x192.png', 192, transparent=False)
        await svg_png(TILE, f'{OUT}/icons/pwa-512x512.png', 512, transparent=False)
        await svg_png(MASK, f'{OUT}/icons/pwa-maskable-512x512.png', 512, transparent=False)
        # social
        await shot(PROFILE, 1080, 1080, f'{OUT}/social/profile-picture-1080.png')
        await shot(OG, 1200, 630, f'{OUT}/social/share-picture-1200x630.png')
        await shot(post(False), 1080, 1350, f'{OUT}/preview/post-style-ivory.png')
        await shot(post(True), 1080, 1350, f'{OUT}/preview/post-style-night.png')
        await b.close()
asyncio.run(main())

# favicon.ico with the hand-drawn 16/32/48 inside (not one picture shrunk)
ims = [Image.open(f'{OUT}/icons/favicon-{s}.png').convert('RGBA') for s in (16, 32, 48)]
ims[2].save(f'{OUT}/icons/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)], append_images=ims[:2])
os.remove(f'{OUT}/icons/favicon-256.png') if os.path.exists(f'{OUT}/icons/favicon-256.png') else None
# PNGs that must have no see-through: flatten
for n in ['apple-touch-icon.png', 'pwa-192x192.png', 'pwa-512x512.png', 'pwa-maskable-512x512.png']:
    Image.open(f'{OUT}/icons/{n}').convert('RGB').save(f'{OUT}/icons/{n}', optimize=True)
for n in ['profile-picture-1080.png', 'share-picture-1200x630.png']:
    Image.open(f'{OUT}/social/{n}').convert('RGB').save(f'{OUT}/social/{n}', optimize=True)
# X banner: from the visiting card's own art (made earlier today)
shutil.copy(f'{SP}/x/astro-river-x-banner-indigo.jpg', f'{OUT}/social/x-banner-1500x500.jpg')
# previews made earlier: the seal on the live website
for a, n in [('seal-site-header.jpg', 'website-header-desktop.jpg'), ('seal-site-phone.jpg', 'website-header-phone.jpg'),
             ('seal-site-footer.jpg', 'website-footer.jpg'), ('tab-icon-check.jpg', 'tab-icon-check.jpg')]:
    shutil.copy(f'{SP}/x/{a}', f'{OUT}/preview/{n}')
# the visiting card: the river-of-stars card, both sides, as sent
for f in os.listdir(f'{SP}/card/zip'):
    shutil.copy(f'{SP}/card/zip/{f}', f'{OUT}/card/{f}')
print('ok')
