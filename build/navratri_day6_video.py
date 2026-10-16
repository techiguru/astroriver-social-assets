# Navratri 2026, Day 6 (Fri 16 Oct, Shashthi): Maa Katyayani in the forest ashram of sage Katyayana, on the founder's
# approved picture (16 Oct, the brighter ashram version) and his Grok clip of it. Founder 16 Oct: "Don't let goddess
# move at all. All face expressions are unnecessary even blinking", then "Can you zoom that out a bit".
# So she and the lion are never taken from the clip: they are cut out of the still picture (BiRefNet matte) and laid
# on top of every frame, pixel for pixel the same. Around them, the scene is zoomed out: Adobe's generative expand
# added more forest on every side and below (katyayani-expanded.png; her own pixels are pasted back unchanged).
# What moves: the smoke and the fire at the hut (taken from the Grok clip, which is aligned to the picture frame by
# frame), a soft breeze in the leaves (the background is gently displaced, never near her or the lion), sunbeams that
# breathe from the bright sky behind her, and gold dust drifting in the light, all behind her.
# Usage: python3 navratri_day6_video.py preview <absolute outdir>     (8 s, no text, plus one frame with the text)
#        python3 navratri_day6_video.py reels <absolute outdir>       (13 s and 8 s Reels with the text layer)
import os, sys, asyncio, subprocess, random
import numpy as np, cv2
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import navratri_day5 as P
D6 = HERE + '/out/navratri/d6/'
W, H, FPS = 1080, 1920, 24
OX, OY = 256, 455                      # where the original picture sits inside katyayani-expanded.png
CY = 338                               # crop top inside the expanded picture: crown at about y 265, paws at about 1455
SC = W / 2048                          # expanded picture to output
K = 1536 / 720 * SC                    # Grok clip pixels (720 wide) to output
MARK = (646, 1242, 710, 1268)          # the Grok mark in the clip (outside every area we take from it)
P.TXT = dict(day='दिन 6', name='माँ कात्यायनी', en='Maa Katyayani · Day 6 of Navratri',
             shloka=['या देवी सर्वभूतेषु माँ कात्यायनी रूपेण संस्थिता।', 'नमस्तस्यै नमस्तस्यै नमस्तस्यै नमो नमः॥'],
             mean='To the Goddess who dwells in all beings as Maa Katyayani: salutations to her, again and again.')


def to_out(img, interp=cv2.INTER_AREA, cy=CY):
    ch = int(round(2048 * 16 / 9)); return cv2.resize(img[cy:cy + ch], (W, H), interpolation=interp)


def layers(cy=CY):
    """Still picture (expanded, original pasted back) and the cut-out matte, both in output pixels."""
    ex = cv2.imread(D6 + 'katyayani-expanded.png').astype(np.float32)
    src = cv2.imread(D6 + 'katyayani-source-lifted.png').astype(np.float32)
    h, w = src.shape[:2]; f = np.zeros((h, w), np.float32); f[24:-24, 24:-24] = 1; f = cv2.GaussianBlur(f, (0, 0), 8)[..., None]
    reg = ex[OY:OY + h, OX:OX + w]; ex[OY:OY + h, OX:OX + w] = src * f + reg * (1 - f)
    m = np.zeros(ex.shape[:2], np.float32); m[OY:OY + h, OX:OX + w] = cv2.imread(D6 + 'katyayani-matte.png', 0) / 255.
    return to_out(ex, cy=cy), np.clip(to_out(m, cv2.INTER_LINEAR, cy=cy), 0, 1)


def grok_frames():
    """The Grok clip, each frame with the affine that puts it back on the picture (in 720-wide picture pixels)."""
    clip = D6 + 'katyayani-grok-720p.mp4'; w, h = 720, 1280
    ref = cv2.resize(cv2.imread(D6 + 'katyayani-source-lifted.png'), (720, 1290), interpolation=cv2.INTER_AREA)[:1280]
    orb = cv2.ORB_create(4000); k0, d0 = orb.detectAndCompute(cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY), None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', clip, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
    out = []
    while True:
        b = dec.stdout.read(w * h * 3)
        if len(b) < w * h * 3: break
        f = np.frombuffer(b, np.uint8).reshape(h, w, 3).copy()
        k, d = orb.detectAndCompute(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), None)
        m = sorted(bf.match(d, d0), key=lambda x: x.distance)[:800]
        M, _ = cv2.estimateAffinePartial2D(np.float32([k[x.queryIdx].pt for x in m]), np.float32([k0[x.trainIdx].pt for x in m]),
                                          method=cv2.RANSAC, ransacReprojThreshold=2)
        out.append((f, M))
    return out


def ellipse(cx, cy, ax, ay, feather):
    """A soft ellipse given in 720-wide picture pixels, drawn in output pixels."""
    m = np.zeros((H, W), np.float32)
    cv2.ellipse(m, (int(cx * K + OX * SC), int(cy * K + (OY - CY) * SC)), (int(ax * K), int(ay * K)), 0, 0, 360, 1, -1)
    return cv2.GaussianBlur(m, (0, 0), feather)


class Scene:
    def __init__(self, cy=CY, seed=6):
        self.cy = cy
        self.still, self.fg = layers(cy)
        near = (self.fg > 0.04).astype(np.uint8)
        dist = cv2.distanceTransform(1 - near, cv2.DIST_L2, 5)
        keep_off = np.clip((dist - 6) / 22, 0, 1)                                   # nothing borrowed or bent within ~6-28 px of her
        # where the Grok clip is used: only the smoke and the fire at the hut (its sun glint left of the sword brought
        # a stray wisp of smoke with it, so the sunlight there is ours)
        self.ms = ellipse(650, 600, 56, 160, 14) * keep_off
        x0 = int(706 * K + OX * SC); self.ms[:, x0:] *= 0                              # stay off the clip's own right edge
        self.ms = cv2.GaussianBlur(self.ms, (0, 0), 4)
        self.ring = self.ms * (1 - self.ms) * 4
        # breeze: strongest in the trees overhead and the flowers at the sides, none on the ground, the hut or near her
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        top = np.clip((1080 - yy) / 380, 0, 1)
        sides = np.clip((np.abs(xx - 540) - 330) / 90, 0, 1) * np.clip((1560 - yy) / 120, 0, 1) * 0.8
        hut = 1 - ellipse(650, 560, 140, 140, 30)
        self.amp = 2.6 * np.maximum(top, sides) * keep_off * np.clip(hut, 0, 1) * (1 - self.ms)
        rng = np.random.default_rng(seed)
        def field(sig, scale):
            n = cv2.GaussianBlur(rng.standard_normal((H // 8, W // 8)).astype(np.float32), (0, 0), sig)
            n = (n - n.mean()) / (n.std() + 1e-6); return cv2.resize(n, (W, H), interpolation=cv2.INTER_CUBIC) * scale
        self.p1, self.p2, self.p3 = field(9, 3.2), field(6, 2.6), field(8, 3.0)
        self.xx, self.yy = xx, yy
        # sunbeams: a fan of soft rays from the bright sky behind her crown
        sx, sy = 540, 150
        self.ang = np.arctan2(yy - sy, xx - sx); r = np.hypot(xx - sx, yy - sy)
        self.rfall = (np.exp(-r / 820) * np.clip((r - 40) / 160, 0, 1)).astype(np.float32)
        self.rays = [(rng.uniform(5, 11), rng.uniform(0.15, 0.4) * rng.choice([-1, 1]), rng.uniform(0, 6.3), rng.uniform(0.6, 1)) for _ in range(5)]
        # gold dust, drifting up slowly in the light
        self.dust = [dict(x=rng.uniform(90, 990), y=rng.uniform(120, 1300), vy=rng.uniform(-14, -5), sw=rng.uniform(6, 18),
                          ph=rng.uniform(0, 6.3), r=rng.uniform(1.6, 3.6), tw=rng.uniform(1.2, 2.8)) for _ in range(70)]
        self.g = grok_frames(); n = len(self.g); self.O = FPS; self.step = n - self.O
        T = np.array([[K, 0, OX * SC], [0, K, (OY - self.cy) * SC], [0, 0, 1]], np.float64)
        self.A = [(T @ np.vstack([M, [0, 0, 1]]))[:2] for _, M in self.g]

    def grok(self, i):
        return cv2.warpAffine(self.g[i][0], self.A[i], (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE).astype(np.float32)

    def smoke(self, i):
        """The clip played on a loop: each pass fades into the next over one second."""
        k, j = divmod(i, self.step)
        if k > 0 and j < self.O:
            w = j / self.O; return self.grok(j + self.step) * (1 - w) + self.grok(j) * w
        return self.grok(j)

    def frame(self, i):
        t = i / FPS
        a = self.amp
        dx = a * (0.62 * np.sin(2 * np.pi * t / 4.3 + self.p1) + 0.38 * np.sin(2 * np.pi * t / 2.6 + self.p2))
        dy = a * 0.35 * np.sin(2 * np.pi * t / 3.4 + self.p3)
        bg = cv2.remap(self.still, self.xx + dx, self.yy + dy, cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
        g = self.smoke(i)
        wsum = self.ring.sum() + 1e-6
        off = ((self.still - g) * self.ring[..., None]).sum((0, 1)) / wsum
        m = self.ms[..., None]; bg = bg * (1 - m) + np.clip(g + off, 0, 255) * m
        # sunbeams (screen blend, warm cream), gently breathing
        ray = np.zeros((H, W), np.float32)
        for n, wv, ph, wt in self.rays:
            ray += wt * (0.5 + 0.5 * np.sin(n * self.ang + ph + wv * np.sin(2 * np.pi * t / 7.5 + ph))) ** 3
        ray = ray / len(self.rays) * self.rfall * (0.75 + 0.25 * np.sin(2 * np.pi * t / 5.2))
        light = np.zeros((H, W), np.float32)
        for d in self.dust:
            y = (d['y'] + d['vy'] * t - 120) % 1180 + 120; x = d['x'] + d['sw'] * np.sin(t * 0.7 + d['ph'])
            b = 0.55 + 0.45 * np.sin(2 * np.pi * t / d['tw'] + d['ph'])
            cv2.circle(light, (int(x * 4), int(y * 4)), int(d['r'] * 4), float(b), -1, cv2.LINE_AA, 2)
        light = cv2.GaussianBlur(light, (0, 0), 1.6)
        add = np.clip(ray * 0.22 + light * 0.75, 0, 1)[..., None] * np.array([196, 238, 255], np.float32)[None, None] / 255
        bg = 255 - (255 - bg) * (1 - add)
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


async def text_frame(img, t, out, mode='full'):
    """One frame of the picture with the text layer at time t (for checking the layout)."""
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': W, 'height': H})
        html = out + '.html'; open(html, 'w').write(P.page(mode))
        await pg.goto('file://' + html); await pg.evaluate('document.fonts.ready'); await pg.evaluate('window.ready')
        await pg.add_style_tag(content=OVERLAY_CSS); await pg.wait_for_timeout(800)
        await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.pause(); a.currentTime={t * 1000}}})')
        png = await pg.screenshot(type='png', omit_background=True); await b.close()
    ov = cv2.imdecode(np.frombuffer(png, np.uint8), cv2.IMREAD_UNCHANGED).astype(np.float32)
    a = ov[..., 3:] / 255; cv2.imwrite(out, (img * (1 - a) + ov[..., :3] * a).astype(np.uint8))


async def still(img, html, t, out, h=H, css=''):
    """A picture with a text page laid over it at time t (cover, Status picture, X picture)."""
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
    # cover: the picture placed lower (crop from the top of the expanded picture) so day and name sit above her crown,
    # inside the 3:4 crop of the Instagram grid, as on Days 1-5
    low, _ = layers(cy=0)
    asyncio.run(still(low, P.page('full', cover=True), 13, os.path.join(out, 'navratri-day6-katyayani-cover.png')))
    asyncio.run(still(low, P.page('full', cover=True), 13, os.path.join(out, 'navratri-day6-katyayani-status.png'),
                      css='.dy{display:none!important}'))
    # X: 1080 x 1350, from just above her crown to the lion's paws, her name small at the top
    pic, _ = layers()
    asyncio.run(still(pic[120:1470], P.page('full', x=True), 13, os.path.join(out, 'navratri-day6-katyayani-x.png'), h=1350))


if __name__ == '__main__':
    cmd, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
    if cmd == 'stills': stills(out); sys.exit()
    sc = Scene()
    if cmd == 'preview':
        encode(sc, 8 * FPS, os.path.join(out, 'day6-katyayani-zoomed-out-preview.mp4'), crf=16, pix='yuv420p')
        f = sc.frame(int(6 * FPS)); cv2.imwrite(os.path.join(out, 'day6-frame.png'), f)
        asyncio.run(text_frame(f.astype(np.float32), 6.0, os.path.join(out, 'day6-frame-with-text.png')))
    elif cmd == 'reels':
        bg = os.path.join(out, '_bg.mp4'); encode(sc, int(P.T['full']['dur'] * FPS), bg)     # the 8 s Reel uses its first 8 s
        for mode, tag in (('full', 'reel'), ('short', 'short-8s')):
            asyncio.run(overlay(bg, mode, os.path.join(out, f'navratri-day6-katyayani-{tag}.mp4'),
                                os.path.join(out, f'navratri-day6-katyayani-{tag}.html')))
