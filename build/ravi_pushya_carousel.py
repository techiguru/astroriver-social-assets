# Ravi Pushya (Sun 1 Nov 2026) carousel, five 4:5 slides; the founder's "final" on 20 Oct for the Hindi wording.
# Facts from the site's own panchang (astroriver.com/panchang, New Delhi): Pushya 5:39 am Sunday to 4:30 am Monday;
# sunrise 6:33 am; Ravi Pushya Yoga and Sarvartha Siddhi Yoga 6:33 am to 4:30 am Monday ("for buying gold, and for
# starting study"); Rahu Kaal 4:13 to 5:36 pm; Krishna Ashtami from 2:52 pm (Ahoi Ashtami that evening); Dhanteras
# Fri 6 Nov (Trayodashi from 10:30 am); Diwali Sun 8 Nov. Ivory, maroon and gold; ASTRO RIVER on every slide; no page
# numbers (the founder dislikes them). The cover picture is a Canva generation brought to HD with Real-ESRGAN.
# Usage: python3 ravi_pushya_carousel.py <outdir>
import os, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import navratri_nine_forms as N
from week_ahead_post import text
W, H = 1080, 1350
IVORY, MAROON, GOLD, DGOLD, INK, GREY = (251, 245, 232), (122, 31, 43), (201, 151, 58), (166, 112, 28), (60, 45, 40), (120, 105, 95)
BOLD, SEMI = N.fonts()
PF = HERE + '/fonts/PlayfairDisplay[wght].ttf'; PFI = HERE + '/fonts/PlayfairDisplay-Italic[wght].ttf'; INTER = HERE + '/fonts/Inter[opsz,wght].ttf'


def font(path, px, wght):
    f = ImageFont.truetype(path, px); f.set_variation_by_axes([wght] if 'Inter' not in path else [14, wght]); return f


def frame(im=None):
    """Ivory slide with ASTRO RIVER and a gold rule on top, astroriver.com at the foot."""
    if im is None: im = Image.new('RGB', (W, H), IVORY)
    d = ImageDraw.Draw(im)
    d.text((W / 2, 96), 'A S T R O   R I V E R', font=font(PF, 36, 700), fill=MAROON, anchor='ms')
    g = GOLD; r = 124
    d.line([(W / 2 - 170, r), (W / 2 - 14, r)], fill=g, width=2); d.line([(W / 2 + 14, r), (W / 2 + 170, r)], fill=g, width=2)
    d.polygon([(W / 2, r - 7), (W / 2 + 7, r), (W / 2, r + 7), (W / 2 - 7, r)], fill=g)
    d.text((W / 2, H - 52), 'astroriver.com', font=font(INTER, 26, 500), fill=GREY, anchor='ms')
    return im, d


def pill(d, cx, cy, txt, px, filled):
    f = ImageFont.truetype(BOLD, px, layout_engine=ImageFont.Layout.RAQM); w = f.getlength(txt) + 80; h = px + 46
    box = [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]
    if filled: d.rounded_rectangle(box, radius=h / 2, fill=MAROON)
    else: d.rounded_rectangle(box, radius=h / 2, outline=GOLD, width=3)
    text(d, (cx, cy + px * 0.36), txt, BOLD, px, IVORY if filled else MAROON, 'ms')


def s1(out):                                                                      # cover: the question over the coins
    pic = cv2.imread(HERE + '/out/ravi-pushya/coins-hd.png')[..., ::-1].astype(np.float32)
    p = np.zeros((H, W, 3), np.float32); p[:] = IVORY; top = 610                  # plain ivory for the words,
    p[top:] = pic[960:960 + H - top]                                               # the plate, coins and diya below
    a = np.clip((np.arange(H) - top) / 170, 0, 1)[:, None, None]; base = np.zeros_like(p); base[:] = IVORY
    im = Image.fromarray((p * a + base * (1 - a)).astype(np.uint8)); im, d = frame(im)
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((W / 2, H - 52), 'astroriver.com', font=font(INTER, 26, 500), fill=(60, 10, 10, 220), anchor='ms')
    from PIL import ImageFilter; im = Image.alpha_composite(im.convert('RGBA'), sh.filter(ImageFilter.GaussianBlur(4))).convert('RGB'); d = ImageDraw.Draw(im)
    d.text((W / 2, H - 52), 'astroriver.com', font=font(INTER, 26, 500), fill=IVORY, anchor='ms')   # readable on the red cloth
    text(d, (W / 2, 300), 'धनतेरस से पहले,', BOLD, 84, MAROON, 'ms')
    text(d, (W / 2, 404), 'सोना खरीदने का', BOLD, 84, MAROON, 'ms')
    text(d, (W / 2, 528), 'एक और शुभ दिन', BOLD, 104, DGOLD, 'ms')
    d.text((W / 2, 600), 'Dhanteras isn’t the only gold day  →', font=font(PFI, 38, 500), fill=INK, anchor='ms')
    im.save(os.path.join(out, 'ravi-pushya-1.jpg'), quality=95)


def s2(out):                                                                      # the day and the yoga
    im, d = frame()
    text(d, (W / 2, 250), 'रवि पुष्य', SEMI, 44, DGOLD, 'ms')
    text(d, (W / 2, 362), 'रविवार, 1 नवंबर', BOLD, 100, MAROON, 'ms')
    d.line([(W / 2 - 60, 412), (W / 2 + 60, 412)], fill=GOLD, width=3)
    pill(d, W / 2, 520, 'रविवार', 52, False)
    text(d, (W / 2, 618), '+', BOLD, 60, GOLD, 'ms')
    pill(d, W / 2, 700, 'चंद्रमा पुष्य नक्षत्र में', 52, False)
    text(d, (W / 2, 798), '=', BOLD, 60, GOLD, 'ms')
    pill(d, W / 2, 880, 'रवि पुष्य योग', 58, True)
    text(d, (W / 2, 1040), 'साथ में सर्वार्थ सिद्धि योग', BOLD, 54, MAROON, 'ms')
    d.text((W / 2, 1100), 'Sunday + Moon in Pushya = Ravi Pushya, with Sarvartha Siddhi Yoga', font=font(PFI, 28, 500), fill=GREY, anchor='ms')
    im.save(os.path.join(out, 'ravi-pushya-2.jpg'), quality=95)


def s3(out):                                                                      # the timing, on a line
    im, d = frame()
    text(d, (W / 2, 250), 'समय · नई दिल्ली', SEMI, 44, DGOLD, 'ms')
    text(d, (W / 2, 370), 'सूर्योदय 6:33 से', BOLD, 88, MAROON, 'ms')
    text(d, (W / 2, 476), 'सोमवार सुबह 4:30 तक', BOLD, 88, MAROON, 'ms')
    x0, x1, y = 120, 960, 700; span = 21 + 57 / 60                               # 6:33 am Sunday to 4:30 am Monday
    X = lambda h: x0 + (x1 - x0) * h / span                                       # hours after 6:33 am
    d.rounded_rectangle([x0, y - 22, x1, y + 22], radius=22, fill=(242, 212, 160))
    r0, r1 = X(9 + 40 / 60), X(11 + 3 / 60)                                      # Rahu Kaal 4:13 to 5:36 pm
    d.rounded_rectangle([r0, y - 26, r1, y + 26], radius=6, fill=MAROON)                # Rahu Kaal, a solid block on the line
    for xx, c in ((x0, (200, 100, 30)), (x1, MAROON)):
        d.line([(xx, y - 60), (xx, y + 30)], fill=c, width=3); d.ellipse([xx - 9, y - 69, xx + 9, y - 51], fill=c)
    text(d, (x0 - 6, y - 118), 'सुबह 6:33', BOLD, 38, (200, 100, 30)); text(d, (x0 - 6, y - 80), 'सूर्योदय', SEMI, 30, INK)
    text(d, (x1 + 6, y - 118), 'सोमवार 4:30', BOLD, 38, MAROON, 'rs'); text(d, (x1 + 6, y - 80), 'पुष्य समाप्त', SEMI, 30, INK, 'rs')
    for h, lab in ((5 + 27 / 60, 'दोपहर 12'), (14 + 27 / 60, 'रात 9'), (17 + 27 / 60, 'रात 12')):
        d.line([(X(h), y + 22), (X(h), y + 40)], fill=GREY, width=2); text(d, (X(h), y + 78), lab, SEMI, 28, GREY, 'ms')
    cx = (r0 + r1) / 2; d.line([(cx, y + 26), (cx, y + 120)], fill=MAROON, width=2)
    text(d, (cx, y + 160), 'राहुकाल', BOLD, 36, MAROON, 'ms'); text(d, (cx, y + 198), 'शाम 4:13–5:36', SEMI, 30, INK, 'ms')
    d.rounded_rectangle([140, 1000, 940, 1110], radius=20, fill=MAROON)
    text(d, (W / 2, 1072), 'राहुकाल शाम 4:13–5:36 छोड़ें', BOLD, 52, IVORY, 'ms')
    text(d, (W / 2, 1190), 'अपने शहर का समय: astroriver.com/panchang', SEMI, 32, INK, 'ms')
    im.save(os.path.join(out, 'ravi-pushya-3.jpg'), quality=95)


def icon(d, kind, x, y):
    c = DGOLD; w = 4
    if kind == 'coins':
        for i, (dx, dy) in enumerate([(0, 30), (0, 14), (0, -2), (44, 40)]):
            d.ellipse([x + dx, y + dy, x + dx + 60, y + dy + 22], outline=c, width=w, fill=IVORY)
    elif kind == 'bank':
        d.polygon([(x, y + 22), (x + 45, y - 4), (x + 90, y + 22)], outline=c, width=w)
        for i in range(4): d.line([(x + 12 + i * 22, y + 30), (x + 12 + i * 22, y + 66)], fill=c, width=w)
        d.line([(x, y + 26), (x + 90, y + 26)], fill=c, width=w); d.line([(x - 4, y + 72), (x + 94, y + 72)], fill=c, width=w)
    elif kind == 'house':
        d.line([(x, y + 34), (x + 42, y - 4), (x + 84, y + 34)], fill=c, width=w, joint='curve')
        d.rectangle([x + 10, y + 30, x + 74, y + 74], outline=c, width=w); d.rectangle([x + 34, y + 48, x + 50, y + 74], outline=c, width=w)
    else:
        d.polygon([(x, y + 4), (x + 42, y + 12), (x + 42, y + 72), (x, y + 64)], outline=c, width=w)
        d.polygon([(x + 84, y + 4), (x + 42, y + 12), (x + 42, y + 72), (x + 84, y + 64)], outline=c, width=w)


def s4(out):                                                                      # what the day is for
    im, d = frame()
    text(d, (W / 2, 300), 'किस काम के लिए शुभ', BOLD, 84, MAROON, 'ms')
    d.line([(W / 2 - 60, 350), (W / 2 + 60, 350)], fill=GOLD, width=3)
    items = [('coins', 'सोना-चाँदी'), ('bank', 'नया खाता या व्यापार'), ('house', 'घर या वाहन'), ('book', 'पढ़ाई या नई आदत')]
    for i, (k, lab) in enumerate(items):
        cx = 90 + (i % 2) * 460; cy = 420 + (i // 2) * 270
        icon(d, k, cx + 30, cy + 30); text(d, (cx + 30, cy + 180), lab, BOLD, 46, INK)
    d.line([(540, 420), (540, 960)], fill=(220, 200, 170), width=2); d.line([(90, 690), (990, 690)], fill=(220, 200, 170), width=2)
    d.rounded_rectangle([270, 1030, 810, 1130], radius=50, fill=MAROON)
    text(d, (W / 2, 1098), 'विवाह के लिए नहीं', BOLD, 52, IVORY, 'ms')
    im.save(os.path.join(out, 'ravi-pushya-4.jpg'), quality=95)


def s5(out):                                                                      # the Diwali week and the comment
    im, d = frame()
    text(d, (W / 2, 280), 'दिवाली सप्ताह', BOLD, 88, MAROON, 'ms')
    rows = [('रविवार, 1 नवंबर', 'रवि पुष्य', 'अहोई अष्टमी भी'), ('शुक्रवार, 6 नवंबर', 'धनतेरस', ''), ('रविवार, 8 नवंबर', 'दीपावली', '')]
    y = 390; d.line([(160, y + 20), (160, y + 2 * 175 + 20)], fill=GOLD, width=3)
    for i, (date, name, sub) in enumerate(rows):
        yy = y + i * 175; d.ellipse([148, yy + 8, 172, yy + 32], fill=MAROON if i == 0 else IVORY, outline=MAROON, width=3)
        text(d, (210, yy + 36), date, SEMI, 38, DGOLD); text(d, (210, yy + 104), name, BOLD, 62, MAROON)
        if sub: text(d, (210 + ImageFont.truetype(BOLD, 62, layout_engine=ImageFont.Layout.RAQM).getlength(name) + 24, yy + 100), f'({sub})', SEMI, 36, GREY)
    d.rounded_rectangle([90, 935, 990, 1175], radius=28, fill=MAROON)
    text(d, (W / 2, 1022), 'अपने शहर का समय जानना है?', SEMI, 46, IVORY, 'ms')
    text(d, (W / 2, 1120), 'Comment में लिखें: पुष्य', BOLD, 66, (240, 200, 120), 'ms')
    im.save(os.path.join(out, 'ravi-pushya-5.jpg'), quality=95)


if __name__ == '__main__':
    o = sys.argv[1]; os.makedirs(o, exist_ok=True)
    for f in (s2, s3, s4, s5): f(o)
    if os.path.exists(HERE + '/out/ravi-pushya/coins-hd.png'): s1(o)
