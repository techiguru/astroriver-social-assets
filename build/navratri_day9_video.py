# Navratri 2026, Day 9 (Mon 19 Oct, Navami): Maa Siddhidatri on a pink lotus with her lion, on the founder's approved
# picture (18 Oct: made in Canva, with the Day 8 picture as its style guide; her right hands hold the chakra and the
# gada, her left hands the conch and a lotus, as Drik Panchang describes her). Founder 18 Oct, after seeing Day 8 on
# Instagram: no Gemini or Grok from now on, and the text must not sit under Instagram's own buttons. So nothing here
# comes from a video model: she, the lion and the lotus never move, and only light moves around them (stars twinkling,
# every diya flame flickering, her halo glowing, golden energy streaming out from behind her, gold dust rising).
# Text keeps the sizes of Days 5-8 (founder 19 Oct: "See font size carefully. Isn't it small"; "Proper spacing between
# text"; "No mantra below?"). Where Instagram covers the video was measured on the founder's own screenshot of the
# Day 8 Reel (the video fills the screen's width, 0.948 of its pixels, and starts 77 px above the screen): the top bar
# ("Reels", +) covers down to y 193, the repost bubbles y 1248-1480 on the left, the buttons x 950 and beyond from
# y 773, and the username and caption y 1591 and below. So the name block starts at y 210, and the shloka sits in the
# band between the bubbles and the username (y 1480-1582), kept left of the buttons. Its English meaning would fall
# under the username and caption, so it stays in the caption only. The picture is enlarged 1.1x so she fills the frame
# as on Days 5-8 (founder 19 Oct: "Why is it so zoomed out", then "Check the previous reels"). Only an 8 s Reel, with the founder's flute track (echoes_of_lumen
# krishna-flute) from 0 s.
# Usage: python3 navratri_day9_video.py check <absolute outdir>     (one frame with the text, and the same frame inside
#                                                                    a mock of Instagram's Reels screen)
#        python3 navratri_day9_video.py reels <absolute outdir>     (8 s Reel with the text layer, no sound yet)
#        python3 navratri_day9_video.py stills <absolute outdir>    (cover, Status picture, X picture, Pinterest picture)
import os, sys, asyncio, subprocess
import numpy as np, cv2
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import navratri_day5 as P
D9 = HERE + '/out/navratri/d9/'
W, H, FPS = 1080, 1920, 24
P.TXT = dict(day='दिन 9', name='माँ सिद्धिदात्री', en='Maa Siddhidatri · Day 9 of Navratri',
             shloka=['या देवी सर्वभूतेषु माँ सिद्धिदात्री रूपेण संस्थिता।', 'नमस्तस्यै नमस्तस्यै नमस्तस्यै नमो नमः॥'],
             mean='To the Goddess who dwells in all beings as Maa Siddhidatri: salutations to her, again and again.')
HALO = (540, 625)                      # centre of her halo, in output pixels
HEART = (540, 860)                     # where the golden energy comes from, in output pixels
# The Reel's text sits inside Instagram's safe area; the shloka, its meaning and the bottom band are not shown.
SAFE_CSS = """
.mk{top:210px!important;padding-left:9px!important}
.en{top:264px!important}
.nm{top:354px!important}
.top{top:160px!important;height:360px!important;background:linear-gradient(rgba(252,246,236,0),rgba(252,246,236,.55) 30%,rgba(252,246,236,.4) 70%,rgba(252,246,236,0))!important}
.sh{top:1480px!important;left:140px!important;right:135px!important;font-size:35px!important;line-height:1.45!important}
.bot{top:1380px!important}
.mn{display:none!important}
"""
OVERLAY_CSS = 'html,body{background:transparent!important} .cam{display:none!important}'


ZOOM = 1.1                             # she fills the frame as on Days 5-8 (founder 19 Oct: "Check the previous reels")
CROWN = (517, 470)                     # her crown's top: y in the Canva picture, y in the Reel (just under her name)


def layers(crown_y=CROWN[1]):
    """The Canva picture, enlarged by ZOOM about the centre line so her crown sits just under her name, and her cut-out
    matte, enlarged the same way. The enlargement starts from a 2x Real-ESRGAN copy (mixed 3:1 with a plain resize, as
    on Day 8) so it stays sharp."""
    big = cv2.imread(D9 + 'siddhidatri-canva-2x.png')
    m = cv2.resize(cv2.imread(D9 + 'siddhidatri-matte.png', 0), (big.shape[1], big.shape[0]), interpolation=cv2.INTER_LINEAR)
    s = ZOOM / 2; w, h = round(big.shape[1] * s), round(big.shape[0] * s)
    big = cv2.resize(big, (w, h), interpolation=cv2.INTER_AREA); m = cv2.resize(m, (w, h), interpolation=cv2.INTER_AREA)
    x0 = (w - W) // 2; y0 = round(CROWN[0] * ZOOM - crown_y)
    return big[y0:y0 + H, x0:x0 + W].astype(np.float32), np.clip(m[y0:y0 + H, x0:x0 + W] / 255., 0, 1).astype(np.float32)


class Scene:
    def __init__(self, crown_y=CROWN[1], seed=9):
        rng = np.random.default_rng(seed); self.still, self.fg = layers(crown_y); dy = crown_y - CROWN[1]
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        # stars: small bright points in the sky, each with its own twinkle
        lum = cv2.cvtColor(self.still.astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)
        top = lum - cv2.morphologyEx(lum, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
        sky = (yy < 700 + dy).astype(np.float32) * (1 - cv2.dilate(self.fg, np.ones((15, 15), np.uint8)))
        n, self.slab = cv2.connectedComponents(((top > 22) & (sky > 0)).astype(np.uint8))
        self.sexc = np.clip(top / 255., 0, 1) * (self.slab > 0)
        self.sph = rng.uniform(0, 6.3, n).astype(np.float32); self.sfr = rng.uniform(0.25, 0.9, n).astype(np.float32)
        # diya flames: small bright warm blobs low in the picture, each flickering on its own
        hsv = cv2.cvtColor(self.still.astype(np.uint8), cv2.COLOR_BGR2HSV)
        fl = ((hsv[..., 2] > 225) & (hsv[..., 0] < 35) & (yy > 1050 + dy)).astype(np.uint8) * (self.fg < 0.3).astype(np.uint8)
        n2, lab, st, _ = cv2.connectedComponentsWithStats(fl)
        small = (st[:, cv2.CC_STAT_AREA] >= 3) & (st[:, cv2.CC_STAT_AREA] <= 260); small[0] = False
        self.flab = np.where(small[lab], lab, 0); self.fmask = (self.flab > 0).astype(np.float32)
        self.fph = rng.uniform(0, 6.3, (n2, 3)).astype(np.float32); self.ffr = rng.uniform(1.2, 3.4, (n2, 3)).astype(np.float32)
        # golden energy: filaments streaming out from behind her, an aura around her, sparks drifting out
        hx, hy = HEART[0], HEART[1] + dy; self.hx, self.hy = hx, hy
        y2, x2 = np.mgrid[0:H // 2, 0:W // 2].astype(np.float32) * 2
        self.ang = np.arctan2(y2 - hy, x2 - hx); self.r = np.hypot(x2 - hx, y2 - hy)
        self.rays = [dict(th=rng.uniform(-np.pi, np.pi), w=rng.uniform(0.008, 0.022), a=rng.uniform(0.45, 1), dr=rng.uniform(-0.03, 0.03),
                          lam=rng.uniform(60, 140), v=rng.uniform(40, 110), ph=rng.uniform(0, 6.3),
                          wa=rng.uniform(0.03, 0.09), wl=rng.uniform(70, 160), wv=rng.uniform(0.4, 1.2)) for _ in range(54)]
        self.rfall = np.clip((self.r - 60) / 140, 0, 1) * np.exp(-self.r / 520)
        up = np.clip((1150 + dy - yy) / 450, 0, 1)
        self.aura = cv2.GaussianBlur(self.fg * up, (0, 0), 38) * 1.6
        self.sparks = [dict(a=rng.uniform(-np.pi, np.pi), r0=rng.uniform(0, 420), v=rng.uniform(25, 70), s=rng.uniform(1.2, 2.8),
                            ph=rng.uniform(0, 6.3)) for _ in range(90)]
        self.halo = np.exp(-((xx - HALO[0]) ** 2 + (yy - HALO[1] - dy) ** 2) / (2 * 80.0 ** 2)) * (1 - self.fg)

    def energy(self, t):
        e = np.zeros(self.ang.shape, np.float32)
        for q in self.rays:
            th = q['th'] + q['dr'] * t
            th = th + q['wa'] * np.sin(self.r / q['wl'] - t * q['wv'] * 2 * np.pi + q['ph'])
            d = (self.ang - th + np.pi) % (2 * np.pi) - np.pi
            flow = 0.55 + 0.45 * np.sin(self.r / q['lam'] - t * q['v'] / q['lam'] * 2 * np.pi / 3 + q['ph'])
            e += q['a'] * np.exp(-(d / q['w']) ** 2) * flow
        e = cv2.resize(e * self.rfall, (W, H), interpolation=cv2.INTER_LINEAR) * (0.85 + 0.15 * np.sin(2 * np.pi * t / 4.2))
        sp = np.zeros((H, W), np.float32)
        for s in self.sparks:
            rr = (s['r0'] + s['v'] * t) % 520; a = s['a']
            x, y = self.hx + rr * np.cos(a), self.hy + rr * np.sin(a)
            b = float(np.clip(1 - rr / 520, 0, 1) * (0.6 + 0.4 * np.sin(5 * t + s['ph'])))
            if 0 <= x < W and 0 <= y < H: cv2.circle(sp, (int(x * 4), int(y * 4)), int(s['s'] * 4), b, -1, cv2.LINE_AA, 2)
        sp = cv2.GaussianBlur(sp, (0, 0), 1.4)
        return np.clip(e * 0.8 + sp + self.aura * (0.7 + 0.12 * np.sin(2 * np.pi * t / 3.1)), 0, 1.4)

    def frame(self, i):
        t = i / FPS; bg = self.still.copy()
        tw = 0.45 * np.sin(2 * np.pi * self.sfr * t + self.sph)
        bg += (self.sexc * tw[self.slab])[..., None] * 255 * 0.9
        p, f = self.fph, self.ffr
        fk = (0.55 * np.sin(2 * np.pi * f[:, 0] * t + p[:, 0]) + 0.3 * np.sin(2 * np.pi * f[:, 1] * 1.7 * t + p[:, 1])
              + 0.15 * np.sin(2 * np.pi * f[:, 2] * 3.1 * t + p[:, 2]))
        fl = self.fmask * fk[self.flab]
        glow = cv2.GaussianBlur(np.clip(fl, 0, 1), (0, 0), 7) * 2.2
        bg = bg * (1 + 0.16 * fl[..., None]) + glow[..., None] * np.array([40, 120, 230], np.float32) * 0.5
        add = self.halo * (0.14 + 0.06 * np.sin(2 * np.pi * t / 3.6)) + self.energy(t) * 0.8
        bg = 255 - (255 - np.clip(bg, 0, 255)) * (1 - np.clip(add, 0, 1)[..., None] * np.array([0.22, 0.68, 1.0], np.float32))
        fg = self.fg[..., None]                                     # she, the lion and the lotus: the still picture, every frame
        return np.clip(self.still * fg + bg * (1 - fg), 0, 255).astype(np.uint8)


def encode(scene, n, out):                  # yuv444p: an intermediate only, phones can't play it
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-crf', '12', '-preset', 'medium', '-pix_fmt', 'yuv444p', out], stdin=subprocess.PIPE)
    for i in range(n): enc.stdin.write(scene.frame(i).tobytes())
    enc.stdin.close(); enc.wait()


async def browser(p):
    return await p.chromium.launch(executable_path=os.environ.get('CHROMIUM'))


async def overlay(bg, out, html):
    D = P.T['short']['dur']
    async with async_playwright() as p:
        b = await browser(p); pg = await b.new_page(viewport={'width': W, 'height': H})
        open(html, 'w').write(P.page('short'))
        await pg.goto('file://' + html); await pg.evaluate('document.fonts.ready'); await pg.evaluate('window.ready')
        await pg.add_style_tag(content=OVERLAY_CSS + SAFE_CSS); await pg.wait_for_timeout(800)
        await pg.evaluate('document.getAnimations().forEach(a=>a.pause())')
        ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-i', bg, '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'png', '-i', '-',
                               '-filter_complex', '[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]', '-map', '[v]',
                               '-c:v', 'libx264', '-crf', '16', '-preset', 'slow', '-movflags', '+faststart', '-t', str(D), out], stdin=subprocess.PIPE)
        for i in range(int(D * FPS)):
            await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.currentTime={i / FPS * 1000}}})')
            ff.stdin.write(await pg.screenshot(type='png', omit_background=True))
        ff.stdin.close(); ff.wait(); await b.close()


async def still(img, html, t, out, h=H, css=''):
    async with async_playwright() as p:
        b = await browser(p); pg = await b.new_page(viewport={'width': W, 'height': h})
        fn = out + '.html'; open(fn, 'w').write(html)
        await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.evaluate('window.ready')
        await pg.add_style_tag(content=OVERLAY_CSS + css); await pg.wait_for_timeout(800)
        await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.pause(); a.currentTime={t * 1000}}})')
        png = await pg.screenshot(type='png', omit_background=True); await b.close()
    ov = cv2.imdecode(np.frombuffer(png, np.uint8), cv2.IMREAD_UNCHANGED).astype(np.float32)
    a = ov[..., 3:] / 255; cv2.imwrite(out, (img.astype(np.float32) * (1 - a) + ov[..., :3] * a).astype(np.uint8))


def instagram_mock(img):
    """The frame with what Instagram's Reels screen lays over it shaded, as measured on the founder's Day 8 screenshot:
    the top bar, the repost bubbles on the left, the buttons on the right, and the username and caption."""
    m = img.astype(np.float32).copy()
    boxes = [(0, 0, W, 193), (0, 1248, 700, 1480), (950, 773, W, 1723), (0, 1591, W, H)]
    for x0, y0, x1, y1 in boxes: m[y0:y1, x0:x1] *= 0.45
    for x0, y0, x1, y1 in boxes: cv2.rectangle(m, (x0, y0), (x1 - 1, y1 - 1), (40, 40, 220), 3)
    return m.astype(np.uint8)


def stills(out):
    low = Scene(crown_y=520).frame(int(2.5 * FPS))                 # day and name sit above her crown, inside the 3:4 grid crop
    # सिद्धिदात्री's tall vowel signs reach up into the day line at the usual size, so both move apart a little
    cc = '.cover .dy{top:252px!important} .cover .nm{top:326px!important;font-size:108px!important}'
    asyncio.run(still(low, P.page('full', cover=True), 13, os.path.join(out, 'navratri-day9-siddhidatri-cover.png'), css=cc))
    asyncio.run(still(low, P.page('full', cover=True), 13, os.path.join(out, 'navratri-day9-siddhidatri-status.png'),
                      css=cc + ' .dy{display:none!important}'))
    pic = Scene().frame(int(2.5 * FPS))
    asyncio.run(still(pic[270:1620], P.page('full', x=True), 13, os.path.join(out, 'navratri-day9-siddhidatri-x.png'), h=1350,
                      css='.x .mk{top:18px!important} .x .nm{top:74px!important}'))


if __name__ == '__main__':
    cmd, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
    if cmd == 'stills': stills(out); sys.exit()
    sc = Scene()
    if cmd == 'check':
        f = sc.frame(int(6 * FPS)); fn = os.path.join(out, 'day9-frame-with-text.png')
        asyncio.run(still(f, P.page('short'), 5.0, fn, css=SAFE_CSS))
        cv2.imwrite(os.path.join(out, 'day9-instagram-check.png'), instagram_mock(cv2.imread(fn)))
    elif cmd == 'reels':
        bg = os.path.join(out, '_bg9.mp4'); encode(sc, int(P.T['short']['dur'] * FPS), bg)
        asyncio.run(overlay(bg, os.path.join(out, 'navratri-day9-siddhidatri-reel-8s-silent.mp4'),
                            os.path.join(out, 'navratri-day9-siddhidatri-reel-8s.html')))
