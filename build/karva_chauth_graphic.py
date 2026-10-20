# Karva Chauth 2026 (Thu 29 Oct): a quick feed graphic in Astro River branding (the founder via the site chat, 20 Oct).
# Date and moonrise from the site's own panchang (astroriver.com/hi/panchang/2026-10-29, New Delhi): Krishna Chaturthi
# 1:07 am to 10:10 pm, moonrise 8:17 pm, so Chaturthi stands at moonrise on the 29th. The picture is a Canva still life
# (no people). Its moon was lit on the wrong side: four days after the full moon a rising waning gibbous is about 83% lit
# with the bright limb toward the sun below the western horizon, which from Delhi at moonrise is about 146 degrees
# counter-clockwise from straight up (lower left). The moon is rotated to that angle; nothing else in the picture changes.
# Usage: python3 karva_chauth_graphic.py <outdir>
import os, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import navratri_nine_forms as N
W, H, TOP = 1080, 1350, 330                       # 4:5 feed crop of the 1080 x 1920 picture, from y 330
IVORY, GOLD, GOLD_RULE = (246, 239, 226), (233, 196, 106), (201, 151, 58, 255)
LIMB = 145.6                                       # bright limb, degrees counter-clockwise from up (Delhi, 8:17 pm)


def fix_moon(im):
    g = cv2.cvtColor(im[:1000], cv2.COLOR_BGR2GRAY); _, m = cv2.threshold(g, 200, 255, cv2.THRESH_BINARY)
    n, lab, st, cen = cv2.connectedComponentsWithStats(m); i = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
    pts = np.column_stack(np.where(lab == i))[:, ::-1].astype(np.float32)
    (cx, cy), r = cv2.minEnclosingCircle(pts)                                  # the whole disc, lit and dark
    lit = pts.mean(0) - (cx, cy); now = np.degrees(np.arctan2(-lit[0], -lit[1]))  # counter-clockwise from up
    yy, xx = np.mgrid[:im.shape[0], :im.shape[1]]; d = np.hypot(xx - cx, yy - cy)
    hole = (d < r + 16).astype(np.uint8)
    sky = cv2.inpaint(im, hole, 20, cv2.INPAINT_TELEA).astype(np.float32)       # the sky as if there were no moon
    light = im.astype(np.float32) - sky                                         # the moon and its glow alone
    M = cv2.getRotationMatrix2D((cx, cy), LIMB - now, 1.0)                      # OpenCV angles turn counter-clockwise
    light = cv2.warpAffine(light, M, (im.shape[1], im.shape[0]), flags=cv2.INTER_CUBIC)
    a = np.clip((r + 16 - d) / 6, 0, 1)[..., None]
    print(f'moon at ({cx:.0f}, {cy:.0f}) r {r:.0f}: limb {now:.0f} -> {LIMB} degrees')
    return np.clip(im * (1 - a) + (sky + light) * a, 0, 255).astype(np.uint8)


def build(out):
    bold, semi = N.fonts(); os.makedirs(out, exist_ok=True)
    im = fix_moon(cv2.imread(HERE + '/out/karva-chauth/kc-canva.png'))[TOP:TOP + H].astype(np.float32)
    y = np.arange(H)[:, None, None]                                             # a light veil behind the text, a shade at the foot
    im *= 1 - 0.28 * np.clip(1 - y / 470, 0, 1); im *= 1 - 0.55 * np.clip((y - 1150) / 200, 0, 1)
    sz = (W, H)
    im = N.over(im, N.text_layer([('करवा चौथ', bold, 128, GOLD, 272),
                                  ('गुरुवार, 29 अक्टूबर 2026', semi, 48, IVORY, 356),
                                  ('चंद्रोदय शाम 8:17 · नई दिल्ली', bold, 46, IVORY, 428),
                                  ('अपने शहर का चंद्रोदय: astroriver.com/panchang', semi, 30, IVORY, 1312)], sz))
    br = Image.new('RGBA', sz, (0, 0, 0, 0)); d = ImageDraw.Draw(br)
    f = ImageFont.truetype(HERE + '/fonts/PlayfairDisplay[wght].ttf', 38); f.set_variation_by_axes([700])
    d.text((W / 2, 92), 'A S T R O   R I V E R', font=f, fill=IVORY + (255,), anchor='ms')
    d.line([(W / 2 - 170, 118), (W / 2 - 14, 118)], fill=GOLD_RULE, width=2); d.line([(W / 2 + 14, 118), (W / 2 + 170, 118)], fill=GOLD_RULE, width=2)
    d.polygon([(W / 2, 110), (W / 2 + 8, 118), (W / 2, 126), (W / 2 - 8, 118)], fill=GOLD_RULE)
    im = N.over(im, np.array(br).astype(np.float32))
    cv2.imwrite(os.path.join(out, 'karva-chauth-2026.jpg'), np.clip(im, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 94])


if __name__ == '__main__':
    build(sys.argv[1])
