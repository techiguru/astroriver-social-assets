# Week-ahead post for Wed 21 Oct 2026: "आने वाले व्रत-त्योहार", the coming vrats and festivals from the site's own
# panchang (astroriver.com/panchang, New Delhi), checked against other panchangs for India:
#   Thu 22 Oct  Papankusha Ekadashi  (Shukla Ekadashi at sunrise, 2:12 pm Wed to 2:48 pm Thu)
#   Fri 23 Oct  Shukra Pradosh vrat  (Trayodashi from 2:36 pm Fri, so in the evening's pradosh kaal)
#   Sun 25 Oct  Sharad Purnima       (Purnima from 11:56 am Sun to 9:41 am Mon; moonrise 5:00 pm)
#   Thu 29 Oct  Karva Chauth         (Krishna Chaturthi 1:07 am to 10:10 pm; moonrise 8:17 pm)
# The picture is a Canva generation (a full moon over a river ghat, for Sharad Purnima), brought to HD with
# Real-ESRGAN (out/week-ahead/moon-hd.png). Canva put the moon high in the sky; on Sharad Purnima it rises at 5:00 pm,
# at dusk, so it is lowered to just above the horizon, straight above its reflection on the water.
# Ivory, purple and gold, ASTRO RIVER on top; no logo.
# Usage: python3 week_ahead_post.py <outdir>   (4:5 feed and 9:16 story)
import os, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import navratri_nine_forms as N
IVORY, PURPLE, MAROON, INK, GOLD = (251, 245, 232), (75, 36, 101), (122, 31, 43), (90, 70, 60), (201, 151, 58)
ROWS = [('गुरुवार', '22 अक्टूबर', 'पापांकुशा एकादशी', ''),
        ('शुक्रवार', '23 अक्टूबर', 'शुक्र प्रदोष व्रत', ''),
        ('रविवार', '25 अक्टूबर', 'शरद पूर्णिमा', 'चंद्रोदय शाम 5:00'),
        ('गुरुवार', '29 अक्टूबर', 'करवा चौथ', 'चंद्रोदय शाम 8:17')]


def text(d, xy, txt, ff, px, rgb, anchor='ls'):
    """Draw one line at xy (anchor 'ls' left or 'rs' right); non-Devanagari characters in Lora, as in N.text_layer."""
    lora = HERE + '/fonts/Lora[wght].ttf'; runs, cur, kind = [], '', None
    for ch in txt:
        k = kind if ch == ' ' and kind else ('latin' if not ('ऀ' <= ch <= 'ॿ') else 'main')
        if k != kind and cur: runs.append((cur, kind)); cur = ''
        cur += ch; kind = k
    if cur: runs.append((cur, kind))
    fs = []
    for r, k in runs:
        f = ImageFont.truetype(lora if k == 'latin' else ff, int(px * 0.92) if k == 'latin' else px, layout_engine=ImageFont.Layout.RAQM)
        if k == 'latin': f.set_variation_by_axes([700])
        fs.append((r, f))
    w = sum(f.getlength(r) for r, f in fs); x = xy[0] - (w if anchor == 'rs' else w / 2 if anchor == 'ms' else 0)
    for r, f in fs: d.text((x, xy[1]), r, font=f, fill=rgb + (255,), anchor='ls'); x += f.getlength(r)


def lower_moon(im, y_new=880):
    g = cv2.cvtColor(im[:1000].astype(np.uint8), cv2.COLOR_BGR2GRAY); _, m = cv2.threshold(g, 215, 255, cv2.THRESH_BINARY)
    n, lab, st, cen = cv2.connectedComponentsWithStats(m); i = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
    (cx, cy), r = cv2.minEnclosingCircle(np.column_stack(np.where(lab == i))[:, ::-1].astype(np.float32))
    yy, xx = np.mgrid[:im.shape[0], :im.shape[1]]; R = r * 2.2                     # the disc and its halo
    hole = (np.hypot(xx - cx, yy - cy) < R).astype(np.uint8)
    sky = cv2.inpaint(im.astype(np.uint8), hole, 25, cv2.INPAINT_TELEA).astype(np.float32)
    light = np.where(hole[..., None] > 0, im - sky, 0)                           # the moon's light over the sky
    M = np.float32([[1, 0, 0], [0, 1, y_new - cy]]); light = cv2.warpAffine(light, M, (im.shape[1], im.shape[0]))
    print(f'moon ({cx:.0f}, {cy:.0f}) r {r:.0f} -> y {y_new}')
    return np.clip(sky + np.maximum(light, 0), 0, 255)


def card(pic, W, H, img_h):
    bold, semi = N.fonts()
    out = np.zeros((H, W, 3), np.float32); out[:] = IVORY[::-1]
    s = W / pic.shape[1]; p = cv2.resize(pic, (W, round(pic.shape[0] * s)), interpolation=cv2.INTER_AREA)
    y0 = 1225 - img_h                                                             # down to just below the horizon
    band = p[y0:y0 + img_h]; a = np.clip((img_h - np.arange(img_h)) / 130, 0, 1)[:, None, None]
    out[:img_h] = band * a + out[:img_h] * (1 - a)                                # the picture fades into ivory
    im = Image.fromarray(np.clip(out[..., ::-1], 0, 255).astype(np.uint8)).convert('RGBA'); d = ImageDraw.Draw(im)
    f = ImageFont.truetype(HERE + '/fonts/PlayfairDisplay[wght].ttf', 40); f.set_variation_by_axes([700])
    top = 84 if H < 1500 else 200                                                # a story keeps clear of its own bar
    d.text((W / 2, top), 'A S T R O   R I V E R', font=f, fill=IVORY + (255,), anchor='ms')
    g = GOLD + (255,); r = top + 26
    d.line([(W / 2 - 180, r), (W / 2 - 15, r)], fill=g, width=2); d.line([(W / 2 + 15, r), (W / 2 + 180, r)], fill=g, width=2)
    d.polygon([(W / 2, r - 8), (W / 2 + 8, r), (W / 2, r + 8), (W / 2 - 8, r)], fill=g)
    y = img_h + 40
    text(d, (W / 2, y), 'आने वाले व्रत-त्योहार', bold, 66, PURPLE, 'ms')
    y += 34; d.line([(W / 2 - 60, y), (W / 2 + 60, y)], fill=g, width=3)
    y += 92; step = (H - 110 - y) / len(ROWS)
    for day, date, name, note in ROWS:
        text(d, (300, y), date, bold, 40, MAROON, 'rs'); text(d, (300, y + 40), day, semi, 30, INK, 'rs')
        d.line([(340, y - 38), (340, y + 48)], fill=g, width=2)
        text(d, (380, y + (0 if note else 18)), name, bold, 50, PURPLE)
        if note: text(d, (380, y + 44), note + ' · नई दिल्ली', semi, 30, INK)
        y += step
    text(d, (W / 2, H - 52), 'अपने शहर का समय: astroriver.com/panchang', semi, 30, MAROON, 'ms')
    return cv2.cvtColor(np.array(im.convert('RGB')), cv2.COLOR_RGB2BGR)


def build(out):
    os.makedirs(out, exist_ok=True); pic = lower_moon(cv2.imread(HERE + '/out/week-ahead/moon-hd.png').astype(np.float32))
    cv2.imwrite(os.path.join(out, 'week-ahead-feed.jpg'), card(pic, 1080, 1350, 620), [cv2.IMWRITE_JPEG_QUALITY, 95])
    cv2.imwrite(os.path.join(out, 'week-ahead-story.jpg'), card(pic, 1080, 1920, 980), [cv2.IMWRITE_JPEG_QUALITY, 95])


if __name__ == '__main__':
    build(sys.argv[1])
