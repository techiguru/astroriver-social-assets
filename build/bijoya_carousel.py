# Bijoya Dashami (Wed 21 Oct 2026) carousel, five 4:5 slides, English first (the founder's audience, checked 21 Oct in
# ContentStudio: Instagram ~45% India and the rest worldwide; Facebook ~68% India with Bangladesh and Vietnam next,
# Dhaka the third city), a Hindi line, and the greeting in Bengali too. Facts from the site's panchang (New Delhi; tithi
# times are the same instant everywhere in IST): Shukla Dashami 12:50 pm Tue 20 to 2:12 pm Wed 21; sunrise Wed 6:26 am;
# Purnima 11:56 am Sun 25 to 9:41 am Mon 26, moonrise Sun 5:00 pm; Kojagari Lakshmi Puja on the night of Sun 25 (other
# panchangs agree; some print Mon 26, the day the tithi ends). The cover is the approved Day 6 picture, Maa Katyayani.
# Usage: python3 bijoya_carousel.py <outdir>
import os, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from week_ahead_post import text
from ravi_pushya_carousel import frame, font, W, H, IVORY, MAROON, GOLD, DGOLD, INK, GREY, BOLD, SEMI, PF, PFI, INTER
BENGALI = HERE + '/out/fonts-extra/NotoSerifBengali-Bold.ttf'      # fontsource's Noto Serif Bengali 700
PEACH = (242, 212, 160)


def para(d, x, y, s, f, fill, maxw, lh, anchor='ls'):
    """Wrap English text to maxw; returns the baseline after the last line."""
    words, line = s.split(), ''
    for w in words:
        t = (line + ' ' + w).strip()
        if f.getlength(t) > maxw and line: d.text((x, y), line, font=f, fill=fill, anchor=anchor); y += lh; line = w
        else: line = t
    if line: d.text((x, y), line, font=f, fill=fill, anchor=anchor); y += lh
    return y


def label(d, y, s):
    d.line([(90, y - 9), (130, y - 9)], fill=(200, 100, 30), width=2)
    d.text((146, y), s, font=font(INTER, 26, 600), fill=(200, 100, 30), anchor='ls')


def s1(out):                                                                      # cover: the question over Maa Katyayani
    pic = cv2.imread(os.path.dirname(HERE) + '/posts/navratri-2026-sources/day6-katyayani.png')
    pic = cv2.resize(pic, (W, round(pic.shape[0] * W / pic.shape[1])), interpolation=cv2.INTER_AREA)[..., ::-1].astype(np.float32)
    top = 600; p = np.zeros((H, W, 3), np.float32); p[:] = IVORY; p[top:] = pic[235:235 + H - top]
    a = np.clip((np.arange(H) - top) / 140, 0, 1)[:, None, None]; base = np.zeros_like(p); base[:] = IVORY
    im = Image.fromarray((p * a + base * (1 - a)).astype(np.uint8)); im, d = frame(im)
    d.text((W / 2, H - 52), 'astroriver.com', font=font(INTER, 26, 500), fill=IVORY, anchor='ms')
    d.text((W / 2, 205), 'BIJOYA DASHAMI  ·  WED 21 OCT', font=font(INTER, 26, 600), fill=(200, 100, 30), anchor='ms')
    d.text((W / 2, 292), 'Dussehra was yesterday.', font=font(PF, 64, 600), fill=MAROON, anchor='ms')
    d.text((W / 2, 368), 'So why is Bengal’s Bijoya', font=font(PF, 64, 600), fill=MAROON, anchor='ms')
    d.text((W / 2, 488), 'today?', font=font(PFI, 124, 700), fill=MAROON, anchor='ms')
    text(d, (W / 2, 560), 'दशहरा कल था, बंगाल में विजया दशमी आज क्यों?', SEMI, 34, DGOLD, 'ms')
    im.save(os.path.join(out, 'bijoya-1.jpg'), quality=95)


def s2(out):                                                                      # one Dashami, two rules
    im, d = frame(); label(d, 210, 'WHY TWO DATES')
    f = font(PF, 70, 600); d.text((90, 300), 'One Dashami, ', font=f, fill=MAROON, anchor='ls')
    d.text((90 + f.getlength('One Dashami, '), 300), 'two rules', font=font(PFI, 74, 700), fill=MAROON, anchor='ls')
    x0, x1 = 90, 990; t0, t1 = 6.0, 6.0 + 36                                     # Tue 6 am to Wed 6 pm, in hours from Tue 0:00
    X = lambda h: x0 + (x1 - x0) * (h - t0) / (t1 - t0)
    y = 420; d.line([(x0, y), (x1, y)], fill=(210, 195, 175), width=2)
    for h, s in ((12, 'Tue noon'), (24, 'midnight'), (36, 'Wed noon')):
        d.line([(X(h), y - 8), (X(h), y + 8)], fill=GREY, width=2); d.text((X(h), y - 18), s, font=font(INTER, 24, 500), fill=GREY, anchor='ms')
    a, b = X(12 + 50 / 60), X(24 + 14 + 12 / 60)                                 # Dashami 12:50 pm Tue to 2:12 pm Wed
    d.rounded_rectangle([a, y + 24, b, y + 64], radius=20, fill=PEACH)
    d.text(((a + b) / 2, y + 53), 'DASHAMI', font=font(INTER, 24, 700), fill=MAROON, anchor='ms')
    d.text((a, y + 96), '12:50 PM Tue', font=font(INTER, 24, 500), fill=INK, anchor='ls')
    d.text((b, y + 96), '2:12 PM Wed', font=font(INTER, 24, 500), fill=INK, anchor='rs')
    ry = 600; d.line([(90, ry - 50), (990, ry - 50)], fill=(225, 210, 190), width=1)
    d.text((90, ry), 'NORTH INDIA', font=font(INTER, 26, 700), fill=(200, 100, 30), anchor='ls')
    d.rounded_rectangle([X(13.2), ry + 24, X(15.5), ry + 56], radius=6, fill=MAROON)
    para(d, 90, ry + 104, 'The day whose afternoon falls in Dashami: Tuesday 20, Dussehra.', font(INTER, 32, 500), INK, 900, 42)
    ry = 820; d.line([(90, ry - 50), (990, ry - 50)], fill=(225, 210, 190), width=1)
    d.text((90, ry), 'BENGAL', font=font(INTER, 26, 700), fill=(200, 100, 30), anchor='ls')
    sx = X(24 + 6 + 26 / 60); d.ellipse([sx - 14, ry + 26, sx + 14, ry + 54], fill=MAROON)
    para(d, 90, ry + 104, 'The tithi at sunrise: Dashami at 6:26 AM Wednesday, so Bijoya Dashami is today.', font(INTER, 32, 500), INK, 900, 42)
    d.rounded_rectangle([90, 1040, 990, 1150], radius=24, fill=MAROON)
    d.text((W / 2, 1090), 'Both are right.', font=font(PF, 44, 700), fill=IVORY, anchor='ms')
    text(d, (W / 2, 1134), 'तिथि एक, नियम दो। दोनों सही।', SEMI, 30, (240, 200, 120), 'ms')
    im.save(os.path.join(out, 'bijoya-2.jpg'), quality=95)


def s3(out):                                                                      # today in Bengal
    im, d = frame(); label(d, 210, 'TODAY IN BENGAL')
    f = font(PF, 70, 600); d.text((90, 300), 'A farewell ', font=f, fill=MAROON, anchor='ls')
    d.text((90 + f.getlength('A farewell '), 300), 'in red', font=font(PFI, 74, 700), fill=MAROON, anchor='ls')
    y = 420
    for title, body in (('Sindoor khela', 'Married women offer sindoor to the goddess, then smear it on each other, wishing a long married life.'),
                        ('Visarjan', 'To the beat of the dhak, the idol is immersed. She returns to Kailash, to Shiva.'),
                        ('Shubho Bijoya', 'Elders are greeted, sweets go round, friends embrace.')):
        d.line([(90, y), (110, y)], fill=GOLD, width=3)
        d.text((128, y + 14), title, font=font(PF, 54, 700), fill=MAROON, anchor='ls')
        y = para(d, 128, y + 74, body, font(INTER, 35, 400), INK, 860, 48) + 52
    d.line([(W / 2 - 60, y + 10), (W / 2 + 60, y + 10)], fill=GOLD, width=3)
    f = ImageFont.truetype(BENGALI, 96, layout_engine=ImageFont.Layout.RAQM)
    d.text((W / 2, max(y + 140, 1150)), 'শুভ বিজয়া', font=f, fill=MAROON, anchor='ms')
    im.save(os.path.join(out, 'bijoya-3.jpg'), quality=95)


def s4(out):                                                                      # the same question this Sunday
    im, d = frame(); label(d, 210, 'NEXT: THIS SUNDAY')
    d.text((90, 300), 'Sharad Purnima:', font=font(PF, 70, 600), fill=MAROON, anchor='ls')
    d.text((90, 390), '25th or 26th?', font=font(PFI, 80, 700), fill=MAROON, anchor='ls')
    x0, x1 = 90, 990; t0, t1 = 6.0, 6.0 + 30                                     # Sun 6 am to Mon noon
    X = lambda h: x0 + (x1 - x0) * (h - t0) / (t1 - t0)
    y = 520; d.line([(x0, y), (x1, y)], fill=(210, 195, 175), width=2)
    for h, s in ((12, 'Sun noon'), (24, 'midnight'), (36, 'Mon noon')):
        d.line([(X(h), y - 8), (X(h), y + 8)], fill=GREY, width=2); d.text((X(h), y - 18), s, font=font(INTER, 24, 500), fill=GREY, anchor='m' + 's' if h < 36 else 'rs')
    a, b = X(11 + 56 / 60), X(24 + 9 + 41 / 60)                                  # Purnima 11:56 am Sun to 9:41 am Mon
    d.rounded_rectangle([a, y + 24, b, y + 64], radius=20, fill=PEACH)
    d.text(((a + b) / 2, y + 53), 'PURNIMA', font=font(INTER, 24, 700), fill=MAROON, anchor='ms')
    d.text((a, y + 96), '11:56 AM Sun', font=font(INTER, 24, 500), fill=INK, anchor='ls')
    d.text((b, y + 96), '9:41 AM Mon', font=font(INTER, 24, 500), fill=INK, anchor='rs')
    m = X(17); d.ellipse([m - 22, y + 22, m + 22, y + 66], fill=(255, 250, 235), outline=GOLD, width=3)   # moonrise 5:00 pm Sun
    d.text((m, y + 130), 'Moonrise 5:00 PM', font=font(INTER, 24, 600), fill=INK, anchor='ms')
    yy = para(d, 90, 760, 'The festival belongs to the night of Sunday 25: kheer under the moonlight, and Bengal’s Kojagari Lakshmi Puja.', font(INTER, 34, 500), INK, 900, 46)
    para(d, 90, yy + 20, 'Some calendars print Monday 26, the day the tithi ends.', font(INTER, 30, 400), GREY, 900, 42)
    text(d, (90, 1130), 'शरद पूर्णिमा: रविवार 25 अक्टूबर की रात', BOLD, 44, MAROON)
    d.text((90, 1190), 'Moonrise for New Delhi; your city at astroriver.com/panchang', font=font(INTER, 24, 500), fill=GREY, anchor='ls')
    im.save(os.path.join(out, 'bijoya-4.jpg'), quality=95)


def s5(out):                                                                      # the ask
    im, d = frame()
    d.text((W / 2, 340), 'Confused about', font=font(PF, 80, 600), fill=MAROON, anchor='ms')
    d.text((W / 2, 440), 'a festival date?', font=font(PFI, 88, 700), fill=MAROON, anchor='ms')
    text(d, (W / 2, 520), 'किसी त्योहार की तारीख़ पर उलझन?', SEMI, 40, DGOLD, 'ms')
    d.rounded_rectangle([90, 600, 990, 840], radius=28, fill=MAROON)
    d.text((W / 2, 700), 'Ask us in the comments.', font=font(PF, 56, 700), fill=IVORY, anchor='ms')
    d.text((W / 2, 780), 'We’ll tell you the right day.', font=font(INTER, 38, 500), fill=(240, 200, 120), anchor='ms')
    d.text((W / 2, 1000), 'Shubho Bijoya', font=font(PFI, 56, 700), fill=MAROON, anchor='ms')
    text(d, (W / 2 - 150, 1090), 'शुभ विजया', BOLD, 48, DGOLD, 'ms')
    d.text((W / 2 + 150, 1090), 'শুভ বিজয়া', font=ImageFont.truetype(BENGALI, 48, layout_engine=ImageFont.Layout.RAQM), fill=DGOLD, anchor='ms')
    im.save(os.path.join(out, 'bijoya-5.jpg'), quality=95)


if __name__ == '__main__':
    o = sys.argv[1]; os.makedirs(o, exist_ok=True)
    for f in (s1, s2, s3, s4, s5): f(o)
