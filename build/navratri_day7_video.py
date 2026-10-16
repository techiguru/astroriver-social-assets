# Navratri 2026, Day 7 (Sat 17 Oct, Saptami): Maa Kalaratri on her donkey under a starry night full of diyas, on the
# founder's approved picture (16 Oct, fourth version: her right hands bless and give boons, her left hands hold the
# sword and the iron hook) and his Grok clip of it. Founder 16 Oct: "This will require zooming out", "Yes to golden
# energy". As on Day 6 she is never taken from the clip: she is cut out of the still picture and laid on top of every
# frame. The picture is cleaned first (kalaratri-source.png: the Gemini mark filled in, and the moon mirrored so its
# lit half is on the right, as a waxing half moon on Saptami looks from India), then zoomed out with Adobe's generative
# expand. What moves: the donkey's head and ears (from the Grok clip, aligned to the picture; its tail swish ran off the
# edge of the clip, so the tail stays still), stars twinkling, every diya flame flickering, her halo softly glowing,
# and golden energy streaming out from behind her.
# Usage: python3 navratri_day7_video.py preview <absolute outdir>     (8 s, no text, plus one frame with the text)
#        python3 navratri_day7_video.py reels <absolute outdir>       (13 s and 8 s Reels with the text layer)
#        python3 navratri_day7_video.py stills <absolute outdir>      (cover, Status picture, X picture)
import os, sys, asyncio, subprocess
import numpy as np, cv2
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import navratri_day5 as P
D7 = HERE + '/out/navratri/d7/'
W, H, FPS = 1080, 1920, 24
OX, OY = 256, 455                      # where the picture sits inside kalaratri-expanded.png
CY = 280                               # crop top inside the expanded picture: crown at about y 268, hooves at about 1425
SC = W / 2048                          # expanded picture to output
K = 1536 / 720 * SC                    # 720-wide picture pixels (what the clip is aligned to) to output
P.TXT = dict(day='दिन 7', name='माँ कालरात्रि', en='Maa Kalaratri · Day 7 of Navratri',
             shloka=['या देवी सर्वभूतेषु माँ कालरात्रि रूपेण संस्थिता।', 'नमस्तस्यै नमस्तस्यै नमस्तस्यै नमो नमः॥'],
             mean='To the Goddess who dwells in all beings as Maa Kalaratri: salutations to her, again and again.')
# the donkey's head and ears, in 720-wide picture pixels; the right edge follows her two left-side arms, which stay
HEAD = [(0, 452), (128, 452), (140, 482), (186, 548), (190, 640), (186, 745), (168, 785), (150, 830), (40, 845), (0, 830)]
HEART = (372, 560)                     # where the golden energy comes from, in 720-wide picture pixels


def to_out(img, interp=cv2.INTER_AREA, cy=CY):
    ch = int(round(2048 * 16 / 9)); return cv2.resize(img[cy:cy + ch], (W, H), interpolation=interp)


def pt(x, y, cy=CY):
    return x * K + OX * SC, y * K + (OY - cy) * SC


def layers(cy=CY):
    """Still picture (expanded, the cleaned picture pasted back) and the cut-out matte, both in output pixels."""
    ex = cv2.imread(D7 + 'kalaratri-expanded.png').astype(np.float32)
    src = cv2.imread(D7 + 'kalaratri-source.png').astype(np.float32)
    h, w = src.shape[:2]; f = np.zeros((h, w), np.float32); f[24:-24, 24:-24] = 1; f = cv2.GaussianBlur(f, (0, 0), 8)[..., None]
    reg = ex[OY:OY + h, OX:OX + w]; ex[OY:OY + h, OX:OX + w] = src * f + reg * (1 - f)
    m = np.zeros(ex.shape[:2], np.float32); m[OY:OY + h, OX:OX + w] = cv2.imread(D7 + 'kalaratri-matte.png', 0) / 255.
    return to_out(ex, cy=cy), np.clip(to_out(m, cv2.INTER_LINEAR, cy=cy), 0, 1)


def grok_frames():
    """The Grok clip, each frame with the affine that puts it back on the picture (720-wide picture pixels)."""
    clip = D7 + 'kalaratri-grok-704p.mp4'; w, h = 704, 1280
    ref = cv2.resize(cv2.imread(D7 + 'kalaratri-source-original.png'), (720, 1290), interpolation=cv2.INTER_AREA)
    orb = cv2.ORB_create(5000); k0, d0 = orb.detectAndCompute(cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY), None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', clip, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
    out = []
    while True:
        b = dec.stdout.read(w * h * 3)
        if len(b) < w * h * 3: break
        f = np.frombuffer(b, np.uint8).reshape(h, w, 3).copy()
        k, d = orb.detectAndCompute(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), None)
        m = sorted(bf.match(d, d0), key=lambda x: x.distance)[:1000]
        M, _ = cv2.estimateAffinePartial2D(np.float32([k[x.queryIdx].pt for x in m]), np.float32([k0[x.trainIdx].pt for x in m]),
                                          method=cv2.RANSAC, ransacReprojThreshold=2)
        out.append((f, M))
    return out


class Scene:
    def __init__(self, cy=CY, seed=7, grok=True):
        self.cy = cy; rng = np.random.default_rng(seed)
        self.still, self.fg = layers(cy)
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32); self.xx, self.yy = xx, yy
        # the donkey's head from the clip
        poly = np.array([pt(x, y, cy) for x, y in HEAD], np.int32)
        hard = np.zeros((H, W), np.float32); cv2.fillPoly(hard, [poly], 1)
        self.mh = cv2.GaussianBlur(cv2.erode(hard, np.ones((5, 5), np.uint8)), (0, 0), 3)
        self.ring = self.mh * (1 - self.mh) * 4
        self.fgx = self.fg * (1 - self.mh)                                          # she stays on top; the head below her comes from the clip
        # stars: small bright points in the sky, each with its own twinkle
        lum = cv2.cvtColor(self.still.astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)
        top = lum - cv2.morphologyEx(lum, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
        sky = (yy < 1050).astype(np.float32) * (1 - cv2.dilate(self.fg, np.ones((15, 15), np.uint8)))
        sm = ((top > 28) & (sky > 0)).astype(np.uint8)
        n, self.slab = cv2.connectedComponents(sm)
        self.sexc = np.clip(top / 255., 0, 1) * (self.slab > 0)
        self.sph = rng.uniform(0, 6.3, n).astype(np.float32); self.sfr = rng.uniform(0.25, 0.9, n).astype(np.float32)
        # diya flames: small bright warm blobs low in the picture, each flickering on its own
        hsv = cv2.cvtColor(self.still.astype(np.uint8), cv2.COLOR_BGR2HSV)
        fl = ((hsv[..., 2] > 225) & (hsv[..., 0] < 35) & (yy > 1000)).astype(np.uint8) * (self.fg < 0.3).astype(np.uint8)
        n2, lab, st, _ = cv2.connectedComponentsWithStats(fl)
        small = (st[:, cv2.CC_STAT_AREA] >= 3) & (st[:, cv2.CC_STAT_AREA] <= 260); small[0] = False   # flames only, not the glow
        self.flab = np.where(small[lab], lab, 0)
        self.fmask = (self.flab > 0).astype(np.float32)
        self.fph = rng.uniform(0, 6.3, (n2, 3)).astype(np.float32); self.ffr = rng.uniform(1.2, 3.4, (n2, 3)).astype(np.float32)
        # golden energy: filaments streaming out from behind her, an aura around her, sparks drifting out
        hx, hy = pt(*HEART, cy); self.hx, self.hy = hx, hy
        y2, x2 = np.mgrid[0:H // 2, 0:W // 2].astype(np.float32) * 2                 # the filaments are worked out at half size
        self.ang = np.arctan2(y2 - hy, x2 - hx); self.r = np.hypot(x2 - hx, y2 - hy)
        self.rays = [dict(th=rng.uniform(-np.pi, np.pi), w=rng.uniform(0.008, 0.022), a=rng.uniform(0.45, 1), dr=rng.uniform(-0.03, 0.03),
                          lam=rng.uniform(60, 140), v=rng.uniform(40, 110), ph=rng.uniform(0, 6.3),
                          wa=rng.uniform(0.03, 0.09), wl=rng.uniform(70, 160), wv=rng.uniform(0.4, 1.2)) for _ in range(54)]
        self.rfall = np.clip((self.r - 60) / 140, 0, 1) * np.exp(-self.r / 520)
        up = np.clip((1250 - yy) / 500, 0, 1)                                        # strongest around her, fading down the donkey
        self.aura = cv2.GaussianBlur(self.fg * up, (0, 0), 38) * 1.6
        self.rr_full = np.hypot(xx - hx, yy - hy)
        self.away = 1 - cv2.GaussianBlur(cv2.dilate(hard, np.ones((25, 25), np.uint8)), (0, 0), 25)
        self.sparks = [dict(a=rng.uniform(-np.pi, np.pi), r0=rng.uniform(0, 420), v=rng.uniform(25, 70), s=rng.uniform(1.2, 2.8),
                            ph=rng.uniform(0, 6.3)) for _ in range(90)]
        # halo behind her head
        cx, cyh = pt(372, 268, cy); self.halo = np.exp(-((xx - cx) ** 2 + (yy - cyh) ** 2) / (2 * 95.0 ** 2)) * (1 - self.fg)
        if grok:
            self.g = grok_frames(); n = len(self.g); self.O = FPS; self.step = n - self.O
            T = np.array([[K, 0, OX * SC], [0, K, (OY - cy) * SC], [0, 0, 1]], np.float64)
            self.A = [(T @ np.vstack([M, [0, 0, 1]]))[:2] for _, M in self.g]

    def grok(self, i):
        return cv2.warpAffine(self.g[i][0], self.A[i], (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE).astype(np.float32)

    def clip(self, i):
        """The clip played on a loop: each pass fades into the next over one second."""
        k, j = divmod(i, self.step)
        if k > 0 and j < self.O:
            w = j / self.O; return self.grok(j + self.step) * (1 - w) + self.grok(j) * w
        return self.grok(j)

    def energy(self, t):
        e = np.zeros(self.ang.shape, np.float32)
        for q in self.rays:
            th = q['th'] + q['dr'] * t
            th = th + q['wa'] * np.sin(self.r / q['wl'] - t * q['wv'] * 2 * np.pi + q['ph'])   # wavy, like flowing energy
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
        return np.clip(e * 0.8 + sp * 1.0 + self.aura * (0.7 + 0.12 * np.sin(2 * np.pi * t / 3.1)), 0, 1.4) * self.away

    def frame(self, i, grok=True):
        t = i / FPS; bg = self.still.copy()
        # stars twinkle
        tw = 0.45 * np.sin(2 * np.pi * self.sfr * t + self.sph)
        bg += (self.sexc * tw[self.slab])[..., None] * 255 * 0.9
        # diya flames flicker and glow
        p = self.fph; f = self.ffr
        fk = (0.55 * np.sin(2 * np.pi * f[:, 0] * t + p[:, 0]) + 0.3 * np.sin(2 * np.pi * f[:, 1] * 1.7 * t + p[:, 1])
              + 0.15 * np.sin(2 * np.pi * f[:, 2] * 3.1 * t + p[:, 2]))
        fl = self.fmask * fk[self.flab]
        glow = cv2.GaussianBlur(np.clip(fl, 0, 1), (0, 0), 7) * 2.2                  # only ever adds warm light
        bg = bg * (1 + 0.16 * fl[..., None]) + glow[..., None] * np.array([40, 120, 230], np.float32) * 0.5
        # halo breathes, golden energy streams out (screen blend, behind her)
        add = self.halo * (0.14 + 0.06 * np.sin(2 * np.pi * t / 3.6)) + self.energy(t) * 0.8
        bg = 255 - (255 - np.clip(bg, 0, 255)) * (1 - np.clip(add, 0, 1)[..., None] * np.array([0.22, 0.68, 1.0], np.float32))  # gold
        if grok:
            g = self.clip(i); off = ((self.still - g) * self.ring[..., None]).sum((0, 1)) / (self.ring.sum() + 1e-6)
            m = self.mh[..., None]; bg = bg * (1 - m) + np.clip(g + off, 0, 255) * m
            fg = self.fgx[..., None]
        else:
            fg = self.fg[..., None]
        return np.clip(self.still * fg + bg * (1 - fg), 0, 255).astype(np.uint8)


def encode(scene, n, out, crf=12, pix='yuv444p'):          # yuv444p only for intermediates: phones can't play it
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-crf', str(crf), '-preset', 'medium', '-pix_fmt', pix, '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    for i in range(n): enc.stdin.write(scene.frame(i).tobytes())
    enc.stdin.close(); enc.wait()


OVERLAY_CSS = 'html,body{background:transparent!important} .cam{display:none!important}'


async def overlay(bg, mode, out, html):
    D = P.T[mode]['dur']
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': W, 'height': H})
        open(html, 'w').write(P.page(mode))
        await pg.goto('file://' + html); await pg.evaluate('document.fonts.ready'); await pg.evaluate('window.ready')
        await pg.add_style_tag(content=OVERLAY_CSS); await pg.wait_for_timeout(800)
        await pg.evaluate('document.getAnimations().forEach(a=>a.pause())')
        ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-i', bg, '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'png', '-i', '-',
                               '-filter_complex', '[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]', '-map', '[v]',
                               '-c:v', 'libx264', '-crf', '16', '-preset', 'slow', '-movflags', '+faststart', '-t', str(D), out], stdin=subprocess.PIPE)
        for i in range(int(D * FPS)):
            await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.currentTime={i / FPS * 1000}}})')
            ff.stdin.write(await pg.screenshot(type='png', omit_background=True))
        ff.stdin.close(); ff.wait(); await b.close()


async def still(img, html, t, out, h=H, css=''):
    """A picture with a text page laid over it at time t (cover, Status picture, X picture, layout check)."""
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': W, 'height': h})
        fn = out + '.html'; open(fn, 'w').write(html)
        await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.evaluate('window.ready')
        await pg.add_style_tag(content=OVERLAY_CSS + css); await pg.wait_for_timeout(800)
        await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.pause(); a.currentTime={t * 1000}}})')
        png = await pg.screenshot(type='png', omit_background=True); await b.close()
    ov = cv2.imdecode(np.frombuffer(png, np.uint8), cv2.IMREAD_UNCHANGED).astype(np.float32)
    a = ov[..., 3:] / 255; cv2.imwrite(out, (img.astype(np.float32) * (1 - a) + ov[..., :3] * a).astype(np.uint8))


def stills(out):
    # cover: the picture placed lower so day and name sit above her crown, inside the Instagram grid's 3:4 crop
    low = Scene(cy=40, grok=False).frame(int(2.5 * FPS), grok=False)
    asyncio.run(still(low, P.page('full', cover=True), 13, os.path.join(out, 'navratri-day7-kalaratri-cover.png')))
    asyncio.run(still(low, P.page('full', cover=True), 13, os.path.join(out, 'navratri-day7-kalaratri-status.png'),
                      css='.dy{display:none!important}'))
    pic = Scene(grok=False).frame(int(2.5 * FPS), grok=False)
    asyncio.run(still(pic[110:1460], P.page('full', x=True), 13, os.path.join(out, 'navratri-day7-kalaratri-x.png'), h=1350))


if __name__ == '__main__':
    cmd, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
    if cmd == 'stills': stills(out); sys.exit()
    sc = Scene()
    if cmd == 'preview':
        encode(sc, 8 * FPS, os.path.join(out, 'day7-kalaratri-preview.mp4'), crf=18, pix='yuv420p')
        f = sc.frame(int(6 * FPS)); cv2.imwrite(os.path.join(out, 'day7-frame.png'), f)
        asyncio.run(still(f, P.page('full'), 6.0, os.path.join(out, 'day7-frame-with-text.png')))
    elif cmd == 'reels':
        bg = os.path.join(out, '_bg7.mp4'); encode(sc, int(P.T['full']['dur'] * FPS), bg)     # the 8 s Reel uses its first 8 s
        for mode, tag in (('full', 'reel'), ('short', 'short-8s')):
            asyncio.run(overlay(bg, mode, os.path.join(out, f'navratri-day7-kalaratri-{tag}.mp4'),
                                os.path.join(out, f'navratri-day7-kalaratri-{tag}.html')))
