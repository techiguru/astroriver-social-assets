# Navratri 2026: split the founder's approved picture into layers so it can move without being redrawn
# (founder 13 Oct, Day 4: "You do it. Make it impeccable."). Produces, at 1080 px wide:
#   fg.png   the goddess and her mount, cut out (BiRefNet matte, made by rembg beforehand)
#   bg.jpg   the sky and clouds with the figure removed (the hole filled softly; only slivers ever show)
#   mist-a.png, mist-b.png   soft cloud wisps generated here, to drift across the cloud sea
# Usage: python3 navratri_layers.py <picture> <matte> <outdir>
import os, sys
import numpy as np, cv2
from PIL import Image, ImageFilter

W = 1080

def main(pic, matte, out):
    os.makedirs(out, exist_ok=True)
    im = Image.open(pic).convert('RGB'); m = Image.open(matte).convert('L')
    h = round(im.height * W / im.width)
    im = im.resize((W, h), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
    m = m.resize((W, h), Image.LANCZOS)
    rgb = np.asarray(im).astype(np.float32); a = np.asarray(m).astype(np.float32) / 255

    # foreground: the picture's own pixels with the matte as alpha
    Image.fromarray(np.dstack([rgb, a * 255]).astype(np.uint8), 'RGBA').save(os.path.join(out, 'fg.png'))

    # background: original outside the figure; inside it, a soft fill grown from the surrounding sky
    core = cv2.dilate((a > 0.06).astype(np.uint8), np.ones((7, 7), np.uint8))          # figure plus its fringe
    hole = cv2.dilate((a > 0.02).astype(np.uint8), np.ones((25, 25), np.uint8))       # keep figure colours out of the fill
    # each hidden pixel takes the colour of the nearest visible sky or cloud, then a light blur; so whatever
    # sliver shows when the layers move matches the sky right beside it
    _, lab = cv2.distanceTransformWithLabels(hole, cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)
    ys, xs = np.nonzero(hole == 0); idx = np.zeros(lab.max() + 1, np.int64)
    zl = lab[hole == 0]; idx[zl] = ys * W + xs
    fill = rgb.reshape(-1, 3)[idx[lab]].reshape(h, W, 3)
    fill = cv2.GaussianBlur(fill, (0, 0), 9)
    k = cv2.GaussianBlur(core.astype(np.float32), (0, 0), 2)[..., None]
    bg = rgb * (1 - k) + fill * k
    Image.fromarray(np.clip(bg, 0, 255).astype(np.uint8)).save(os.path.join(out, 'bg.jpg'), quality=95)

    # cloud wisps: layered noise, soft and warm, densest at the bottom edge
    rng = np.random.default_rng(7)
    for name, (mw, mh, seed, dens) in {'mist-a.png': (1700, 760, 7, 0.55), 'mist-b.png': (1700, 600, 11, 0.42)}.items():
        rng = np.random.default_rng(seed); n = np.zeros((mh, mw), np.float32)
        for octv, amp in [(6, 1.0), (12, .5), (24, .25), (48, .12)]:
            g = rng.random((max(2, mh * octv // mw), octv)).astype(np.float32)
            n += amp * cv2.resize(g, (mw, mh), interpolation=cv2.INTER_CUBIC)
        n = (n - n.min()) / (n.max() - n.min())
        n = np.clip((n - 0.42) / 0.4, 0, 1); n = n * n * (3 - 2 * n)
        n = cv2.GaussianBlur(n, (0, 0), 14)
        ramp = (np.clip(np.linspace(-0.25, 1.15, mh), 0, 1) * np.clip(np.linspace(8, 0, mh), 0, 1))[:, None]  # fade out at top and bottom edges
        edge = np.clip(np.minimum(np.linspace(0, 6, mw), np.linspace(6, 0, mw)), 0, 1)[None, :]
        al = np.clip(n * ramp * edge * dens, 0, 1)
        col = np.zeros((mh, mw, 3), np.float32); col[...] = (255, 243, 226)
        Image.fromarray(np.dstack([col, al * 255]).astype(np.uint8), 'RGBA').save(os.path.join(out, name))
    print('layers', W, h)

if __name__ == '__main__':
    main(*sys.argv[1:4])
