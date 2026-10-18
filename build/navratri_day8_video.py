# Navratri 2026, Day 8 (Sun 18 Oct): Maa Mahagauri in white on her white bull, on the founder's approved picture
# (18 Oct, after three edits: the mount made a bull, not a cow, with a hump and dewlap; her right hands hold the trishul
# and show abhaya, her left hands hold the damaru and show varada, as Drik Panchang describes her) and his Grok clip of
# it. Gemini returned the final edit at 768x1376 with a faded copy of its mark stamped on the ground, so the picture is
# cleaned first: that patch of ground is taken from the previous full-size version (same ground, no mark), then the
# picture is enlarged 2x with Real-ESRGAN (x2plus) mixed 3:1 with a plain resize so her face stays natural
# (mahagauri-source.png). As on Days 6 and 7 she is never taken from the clip: she is cut out of the still picture and
# laid on top of every frame, and the scene is zoomed out with Adobe's generative expand. What moves: the bull's head,
# horns, ears, neck and bell, and its tail (from his second Grok clip, made from the zoomed-out picture so the bull
# has room, and aligned back onto it), stars twinkling, every diya flame flickering, her halo softly glowing, and golden
# energy streaming out from behind her. Founder 18 Oct: "6 to 8
# secs length is enough", so only the 8 s Reel is made, with his flute track (echoes_of_lumen krishna-flute) from 0 s.
# Usage: python3 navratri_day8_video.py preview <absolute outdir>     (8 s, no text, plus one frame with the text)
#        python3 navratri_day8_video.py reels <absolute outdir>       (8 s Reel with the text layer, no sound yet)
#        python3 navratri_day8_video.py stills <absolute outdir>      (cover, Status picture, X picture)
import os, sys, asyncio, subprocess
import numpy as np, cv2
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import navratri_day5 as P
D8 = HERE + '/out/navratri/d8/'
W, H, FPS = 1080, 1920, 24
OX, OY = 256, 455                      # where the picture sits inside mahagauri-expanded.png
CY = 188                               # crop top inside the expanded picture: crown at about y 225, hooves at about 1180
                                       # (720-wide picture pixels), so her crown sits where Day 7's did
SC = W / 2048                          # expanded picture to output
K = 1536 / 720 * SC                    # 720-wide picture pixels (what the clip is aligned to) to output
P.TXT = dict(day='दिन 8', name='माँ महागौरी', en='Maa Mahagauri · Day 8 of Navratri',
             shloka=['या देवी सर्वभूतेषु माँ महागौरी रूपेण संस्थिता।', 'नमस्तस्यै नमस्तस्यै नमस्तस्यै नमो नमः॥'],
             mean='To the Goddess who dwells in all beings as Maa Mahagauri: salutations to her, again and again.')
# the bull's head, horns, ears, neck and bell, and its tail, in 720-wide picture pixels (the left ear runs past the
# picture's edge into the zoomed-out part). The head dips under the foot of her trishul between the horns and stops
# short of the hump and her knee, which stay.
HEAD = [(-40, 600), (0, 470), (90, 470), (96, 540), (138, 572), (168, 572), (178, 470), (250, 470), (250, 560),
        (262, 640), (262, 682), (238, 702), (214, 704), (200, 760), (172, 830), (164, 905), (100, 912), (84, 840),
        (24, 795), (-40, 760)]
TAIL = [(640, 700), (700, 700), (760, 820), (760, 1100), (600, 1100), (610, 900)]
HEART = (372, 500)                     # where the golden energy comes from, in 720-wide picture pixels


def to_out(img, interp=cv2.INTER_AREA, cy=CY):
    ch = int(round(2048 * 16 / 9)); return cv2.resize(img[cy:cy + ch], (W, H), interpolation=interp)


def pt(x, y, cy=CY):
    return x * K + OX * SC, y * K + (OY - cy) * SC


def layers(cy=CY):
    """Still picture (expanded, the cleaned picture pasted back) and the cut-out matte, both in output pixels."""
    ex = cv2.imread(D8 + 'mahagauri-expanded.png').astype(np.float32)
    src = cv2.imread(D8 + 'mahagauri-source.png').astype(np.float32)
    h, w = src.shape[:2]; f = np.zeros((h, w), np.float32); f[24:-24, 24:-24] = 1; f = cv2.GaussianBlur(f, (0, 0), 8)[..., None]
    reg = ex[OY:OY + h, OX:OX + w]; ex[OY:OY + h, OX:OX + w] = src * f + reg * (1 - f)
    m = np.zeros(ex.shape[:2], np.float32); m[OY:OY + h, OX:OX + w] = cv2.imread(D8 + 'mahagauri-matte.png', 0) / 255.
    return to_out(ex, cy=cy), np.clip(to_out(m, cv2.INTER_LINEAR, cy=cy), 0, 1)


def grok_frames():
    """The Grok clip, each frame with the affine that puts it on the output frame. The founder made it from the
    zoomed-out picture (mahagauri-zoomed-out-for-grok.png, the output frame without text), so the bull has room; Grok
    still cropped in by about a third and drifts slowly, which the alignment takes out."""
    clip = D8 + 'mahagauri-grok-zoomed.mp4'; w, h = 704, 1280
    ref = cv2.resize(cv2.imread(D8 + 'mahagauri-zoomed-out-for-grok.png'), (W, H), interpolation=cv2.INTER_AREA)
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
                                          method=cv2.RANSAC, ransacReprojThreshold=3)
        out.append((f, M))
    return out


class Scene:
    def __init__(self, cy=CY, seed=7, grok=True):
        self.cy = cy; rng = np.random.default_rng(seed)
        self.still, self.fg = layers(cy)
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32); self.xx, self.yy = xx, yy
        # the bull's head from the clip
        hard = np.zeros((H, W), np.float32)
        for part in (HEAD, TAIL): cv2.fillPoly(hard, [np.array([pt(x, y, cy) for x, y in part], np.int32)], 1)
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
        up = np.clip((1250 - yy) / 500, 0, 1)                                        # strongest around her, fading down the bull
        self.aura = cv2.GaussianBlur(self.fg * up, (0, 0), 38) * 1.6
        self.rr_full = np.hypot(xx - hx, yy - hy)
        self.away = 1 - cv2.GaussianBlur(cv2.dilate(hard, np.ones((25, 25), np.uint8)), (0, 0), 25)
        self.sparks = [dict(a=rng.uniform(-np.pi, np.pi), r0=rng.uniform(0, 420), v=rng.uniform(25, 70), s=rng.uniform(1.2, 2.8),
                            ph=rng.uniform(0, 6.3)) for _ in range(90)]
        # halo behind her head
        cx, cyh = pt(372, 290, cy); self.halo = np.exp(-((xx - cx) ** 2 + (yy - cyh) ** 2) / (2 * 95.0 ** 2)) * (1 - self.fg)
        if grok:
            self.g = grok_frames()
            self.A = [M for _, M in self.g]
            # where each frame of the clip actually has picture: it fades out over 14 px inside its edge
            one = np.ones((1280 - 28, 704 - 28), np.float32)
            self.cov = [cv2.GaussianBlur(cv2.warpAffine(cv2.copyMakeBorder(one, 14, 14, 14, 14, cv2.BORDER_CONSTANT, value=0), M, (W, H)),
                                         (0, 0), 6) for M in self.A]

    def grok(self, i):
        return cv2.warpAffine(self.g[i][0], self.A[i], (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE).astype(np.float32)

    def clip(self, i):
        """The clip played forwards, then backwards for the rest of the Reel (a loop would fade two poses of the head
        into each other), and where that frame has picture."""
        n = len(self.g); j = i % (2 * n - 2); j = j if j < n else 2 * n - 2 - j
        return self.grok(j), self.cov[j]

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
            g, cov = self.clip(i); ring = self.ring * cov
            off = ((self.still - g) * ring[..., None]).sum((0, 1)) / (ring.sum() + 1e-6)
            mh = self.mh * cov; m = mh[..., None]; bg = bg * (1 - m) + np.clip(g + off, 0, 255) * m
            fg = (self.fg * (1 - mh))[..., None]
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
        b = await p.chromium.launch(executable_path=os.environ.get('CHROMIUM')); pg = await b.new_page(viewport={'width': W, 'height': H})
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
        b = await p.chromium.launch(executable_path=os.environ.get('CHROMIUM')); pg = await b.new_page(viewport={'width': W, 'height': h})
        fn = out + '.html'; open(fn, 'w').write(html)
        await pg.goto('file://' + fn); await pg.evaluate('document.fonts.ready'); await pg.evaluate('window.ready')
        await pg.add_style_tag(content=OVERLAY_CSS + css); await pg.wait_for_timeout(800)
        await pg.evaluate(f'document.getAnimations().forEach(a=>{{a.pause(); a.currentTime={t * 1000}}})')
        png = await pg.screenshot(type='png', omit_background=True); await b.close()
    ov = cv2.imdecode(np.frombuffer(png, np.uint8), cv2.IMREAD_UNCHANGED).astype(np.float32)
    a = ov[..., 3:] / 255; cv2.imwrite(out, (img.astype(np.float32) * (1 - a) + ov[..., :3] * a).astype(np.uint8))


def stills(out):
    # cover: the picture placed lower so day and name sit above her crown, inside the Instagram grid's 3:4 crop
    low = Scene(cy=0, grok=False).frame(int(2.5 * FPS), grok=False)
    asyncio.run(still(low, P.page('full', cover=True), 13, os.path.join(out, 'navratri-day8-mahagauri-cover.png')))
    asyncio.run(still(low, P.page('full', cover=True), 13, os.path.join(out, 'navratri-day8-mahagauri-status.png'),
                      css='.dy{display:none!important}'))
    pic = Scene(grok=False).frame(int(2.5 * FPS), grok=False)
    asyncio.run(still(pic[230:1580], P.page('full', x=True), 13, os.path.join(out, 'navratri-day8-mahagauri-x.png'), h=1350))


if __name__ == '__main__':
    cmd, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
    if cmd == 'stills': stills(out); sys.exit()
    sc = Scene()
    if cmd == 'preview':
        encode(sc, 8 * FPS, os.path.join(out, 'day8-mahagauri-preview.mp4'), crf=18, pix='yuv420p')
        f = sc.frame(int(6 * FPS)); cv2.imwrite(os.path.join(out, 'day8-frame.png'), f)
        asyncio.run(still(f, P.page('full'), 6.0, os.path.join(out, 'day8-frame-with-text.png')))
    elif cmd == 'reels':
        bg = os.path.join(out, '_bg8.mp4'); encode(sc, int(P.T['short']['dur'] * FPS), bg)    # only the 8 s Reel today
        asyncio.run(overlay(bg, 'short', os.path.join(out, 'navratri-day8-mahagauri-reel-8s-silent.mp4'),
                            os.path.join(out, 'navratri-day8-mahagauri-reel-8s.html')))
