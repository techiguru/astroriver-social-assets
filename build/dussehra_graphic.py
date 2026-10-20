# Dussehra 2026 (Tue 20 Oct): a greeting in Astro River branding (the founder, 20 Oct: "Use canva. Create an excellent
# graphic, not too dark ... for Dussehra", "where's ravan", then "doesn't look premium/hd, looks blurred and
# cartoonish"). The picture is one Canva generation in a realistic style (Shri Ram with his bow in abhaya at golden
# hour, the Ravan effigy burning across the river), exported at its own size (926 x 1646) and brought to 1080 x 1920
# with Real-ESRGAN x2 (out/dussehra/ram-ravan-hd.png). Here: the generator's corner star is removed; Canva drew Ravan
# with eleven heads, so the outermost head on the left is replaced with the sky beside it (five on one side of the
# main head, four on the other: ten); the shadows are lifted a little. Greeting: the founder's approved line.
# Usage: python3 dussehra_graphic.py <outdir>   (4:5 feed picture and 9:16 story picture)
import os, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import navratri_nine_forms as N
IVORY, PURPLE, GOLD = (251, 245, 232), (75, 36, 101), (201, 151, 58, 255)
STAR = (1018, 1870, 1066, 1920)                    # x0, y0, x1, y1: the generator's star, bottom right
EXTRA = (612, 645, 657, 760)                       # the eleventh head, outermost on the left, up to the next head's edge


def clean(im):
    x0, y0, x1, y1 = STAR; m = np.zeros(im.shape[:2], np.uint8); m[y0:y1, x0:x1] = 255
    im = cv2.inpaint(im, m, 9, cv2.INPAINT_TELEA)
    x0, y0, x1, y1 = EXTRA; w = x1 - x0; sky = im[y0:y1, x0 - w:x0].astype(np.float32)
    d = im[y0:y1, x0 - 1].astype(np.float32) - sky[:, 0]                           # the copied sky is a shade off: match it,
    sky += cv2.GaussianBlur(d[:, None, :], (1, 0), 0, sigmaY=6)                  # row by row, to the sky beside the head
    a = np.ones((y1 - y0, w), np.float32); r = np.linspace(0, 1, 6)
    a[:, :6] *= r; a[:6] *= r[:, None]; a[-6:] *= r[::-1, None]                   # soft on the sky sides
    a[:, -2:] *= np.array([0.6, 0.3])                                            # and a 2 px blend into the next head
    im[y0:y1, x0:x1] = (im[y0:y1, x0:x1] * (1 - a[..., None]) + sky * a[..., None]).astype(np.uint8)
    f = im.astype(np.float32) / 255; L = f.mean(2, keepdims=True)                 # lift the shadows, keep the sky
    return (np.clip(f + (f ** 0.8 - f) * (1 - L), 0, 1) * 255).astype(np.float32)


def head_text(size, brand_y, lines):
    im = Image.new('RGBA', size, (0, 0, 0, 0)); d = ImageDraw.Draw(im); cx = size[0] / 2
    f = ImageFont.truetype(HERE + '/fonts/PlayfairDisplay[wght].ttf', 40); f.set_variation_by_axes([700])
    d.text((cx, brand_y), 'A S T R O   R I V E R', font=f, fill=PURPLE + (255,), anchor='ms')
    r = brand_y + 26
    d.line([(cx - 180, r), (cx - 15, r)], fill=GOLD, width=2); d.line([(cx + 15, r), (cx + 180, r)], fill=GOLD, width=2)
    d.polygon([(cx, r - 8), (cx + 8, r), (cx, r + 8), (cx - 8, r)], fill=GOLD)
    t = N.text_layer(lines, size); b = np.array(im).astype(np.float32); a = t[..., 3:] / 255.
    b[..., :3] = b[..., :3] * (1 - a) + t[..., :3] * a; b[..., 3] = np.maximum(b[..., 3], t[..., 3]); return b


def band(size, solid, fade):
    """Ivory over the top of the picture: solid to y `solid`, fading out by y `fade`."""
    y = np.arange(size[1]); a = np.clip((fade - y) / (fade - solid), 0, 1)
    l = np.zeros((size[1], size[0], 4), np.float32); l[..., :3] = IVORY; l[..., 3] = 255 * a[:, None]; return l


def build(out):
    bold, _ = N.fonts(); os.makedirs(out, exist_ok=True)
    pic = clean(cv2.imread(HERE + '/out/dussehra/ram-ravan-hd.png'))
    cv2.imwrite(os.path.join(out, 'ram-ravan-clean.png'), pic.astype(np.uint8))
    greet = 'विजयादशमी की हार्दिक शुभकामनाएँ'
    W, H = 1080, 1350; f = pic[20:20 + H].copy()                                  # 4:5 feed: his crown just under the head
    f = N.over(f, band((W, H), 205, 280)); f = N.over(f, head_text((W, H), 82, [(greet, bold, 62, PURPLE, 192)]))
    cv2.imwrite(os.path.join(out, 'dussehra-2026-feed.jpg'), np.clip(f, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 95])
    W, H = 1080, 1920; s = N.over(pic.copy(), band((W, H), 285, 330))            # 9:16 story: below the story's own bar
    s = N.over(s, head_text((W, H), 170, [(greet, bold, 62, PURPLE, 265)]))
    cv2.imwrite(os.path.join(out, 'dussehra-2026-story.jpg'), np.clip(s, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 95])


if __name__ == '__main__':
    build(sys.argv[1])
