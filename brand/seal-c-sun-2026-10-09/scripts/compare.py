import asyncio, os, seal as S, stars as T
from playwright.async_api import async_playwright
NIGHT = 'radial-gradient(ellipse at 50% 40%,#23185C,#0F092A 78%)'
def box(fn, kind, head, scheme, uid, h):
    d, b = T.with_head(getattr(S, fn), head, scheme=scheme, uid=uid)
    bx = S.BOX[kind]
    return f'<svg viewBox="{bx[0]} {bx[1]} {bx[2]} {bx[3]}" height="{h}" width="{h*bx[2]/bx[3]:.0f}"><defs>{d}</defs>{b}</svg>'
def fav(head, s, uid):
    d, b = T.with_head(S.icon, head, scheme=S.DARK, uid=uid)
    return (f'<svg viewBox="-10 -10 420 420" width="{s}" height="{s}"><defs>{d}</defs>'
            f'<circle cx="200" cy="200" r="210" fill="#0F092A"/>{b}</svg>')
cols = [('spark', 'Now: the curved sparkle'), ('eight', 'A · Pole star (Dhruva), 8 straight rays'), ('sun', 'B · Sun (Surya)'), ('bindu', 'C · Bindu, the point')]
cells = ''
for i, (h, label) in enumerate(cols):
    cells += f"""<div style="width:330px;text-align:center;font:600 17px system-ui;color:#333">
<div style="height:46px">{label}</div>
<div style="background:{NIGHT};border-radius:14px;padding:24px 0">{box('full','full',h,S.DARK,f'd{i}',240)}</div>
<div style="background:#FAF7F2;border:1px solid #eee;border-radius:14px;padding:24px 0;margin-top:12px">{box('full','full',h,S.LIGHT,f'l{i}',240)}</div>
<div style="display:flex;gap:18px;justify-content:center;align-items:center;margin-top:16px">{fav(h,64,f'a{i}')}{fav(h,32,f'b{i}')}{fav(h,16,f'c{i}')}</div></div>"""
html = f'<html><body style="margin:0;padding:24px;background:#fff;display:flex;gap:26px">{cells}</body></html>'
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1440, 'height': 760})
        await pg.set_content(html); await pg.wait_for_timeout(300)
        await pg.screenshot(path='star-options.png', full_page=True); await b.close()
asyncio.run(main())
