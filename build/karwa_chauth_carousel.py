# Karwa Chauth 2026 carousel, six 4:5 slides and a 9:16 story, for Tue 27 Oct (two days before). Hindi headlines with
# an English italic line, as the Ravi Pushya carousel; inform first, then a soft link to the journal.
# Facts from the site's own article, checked 26 Oct (astroriver.com/journal/karwa-chauth and /hi/journal/karwa-chauth):
#   India Thu 29 Oct; USA, Canada and UK Wed 28 Oct (London: Chaturthi holds at neither moonrise, the texts keep the
#   earlier day). New Delhi: Krishna Chaturthi 1:07 am to 10:10 pm Thu; fast 6:31 am to 8:17 pm; sunset 5:39 pm.
#   Moonrise Thu 29: New Delhi 8:17, Mumbai 9:00, Lucknow 8:06, Jaipur 8:28, Kolkata 7:47, Chennai 8:44,
#   Chandigarh 8:12, Amritsar 8:18 pm. Wed 28 (local): New York 7:35, Toronto 7:45, Chicago 7:27, Houston 8:41,
#   San Francisco 8:08, Vancouver 7:18 pm, London 5:34 pm. Rule: Nirnaya Sindhu, Chaturthi running at moonrise.
# The picture is the journal's own cover (art-journal-karwa-moon.webp, the site's 1600 px image). It shows a full moon;
# four days after the full moon the rising Moon is a waning gibbous about 83% lit, its bright limb toward the Sun below
# the horizon, about 146 degrees counter-clockwise from up at Delhi moonrise (as in karva_chauth_graphic.py). The unlit
# part of the disc is replaced by the plain night sky round it, and the painted glow is kept only round the lit part
# (Krishna's review, 26 Oct: no dark disc, no edge); nothing else in the picture changes.
# Usage: python3 karwa_chauth_carousel.py <outdir>
import os, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from week_ahead_post import text
from ravi_pushya_carousel import frame, font, pill, W, H, IVORY, MAROON, GOLD, DGOLD, INK, GREY, BOLD, SEMI, PF, PFI, INTER
LIT, LIMB = 0.83, 145.6                     # fraction lit; bright limb, degrees counter-clockwise from up
RULE = (220, 200, 170)


def picture():
    """The journal painting, RGB float, with the moon shaded to its Karwa Chauth phase."""
    im = cv2.imread(HERE + '/art-journal-karwa-moon.webp')
    X0, Y0 = 820, 70                                                              # the sky inside the painted frame
    g = cv2.cvtColor(im[Y0:430, X0:1260], cv2.COLOR_BGR2GRAY); _, m = cv2.threshold(g, 150, 255, cv2.THRESH_BINARY)
    n, lab, st, cen = cv2.connectedComponentsWithStats(m); i = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
    (cx, cy), r = cv2.minEnclosingCircle(np.column_stack(np.where(lab == i))[:, ::-1].astype(np.float32)); cx += X0; cy += Y0
    t = np.radians(LIMB); u = np.array([-np.sin(t), -np.cos(t)])                  # toward the lit limb, image axes
    yy, xx = np.mgrid[:im.shape[0], :im.shape[1]].astype(np.float32)
    px, py = (xx - cx) / r, (yy - cy) / r
    a = px * u[0] + py * u[1]; b = -px * u[1] + py * u[0]                         # along and across the limb axis
    edge = -(2 * LIT - 1) * np.sqrt(np.clip(1 - b * b, 0, 1))                     # the terminator, an ellipse
    d = np.hypot(px, py)
    disc = np.clip((1.0 - d) / 0.015 + 0.5, 0, 1)
    lit = np.clip((a - edge) / 0.10 + 0.5, 0, 1) * disc                          # the lit part of the disc, soft terminator
    f = im.astype(np.float32); col = np.zeros((im.shape[0], 3), np.float32)       # plain sky, row by row: the blue pixels
    xs = np.arange(650, 1400)                                                     # of the row outside the glow
    for y in range(im.shape[0]):
        row = f[y, 650:1400]; ok = (np.abs(xs - cx) > 2.3 * r) & (row[:, 0] > row[:, 2] + 25)
        col[y] = np.median(row[ok], 0) if ok.sum() > 8 else (col[y - 1] if y else row.mean(0))
    col = cv2.GaussianBlur(col[:, None, :], (1, 31), 0)[:, 0]
    skyish = cv2.erode(((f[..., 0] > f[..., 2] + 15) & (yy > 80)).astype(np.uint8), np.ones((7, 7), np.uint8)) > 0   # night sky only
    res = f - col[:, None, :]; G = np.zeros((241, 3), np.float32)                 # the glow's radial profile, 1.0 to 3.4 r
    for k in range(241):
        ring = skyish & (np.abs(d - (1.0 + k * 0.01)) < 0.006)
        if ring.sum() > 20: G[k] = np.median(res[ring], 0)
    G = np.maximum(cv2.GaussianBlur(G[:, None, :], (1, 21), 0)[:, 0] - G[-20:].mean(0), 0); G[-30:] *= np.linspace(1, 0, 30)[:, None]
    t = np.clip((d - 1.0) / 0.01, 0, 240); i0 = np.floor(t).astype(int); i1 = np.minimum(i0 + 1, 240); fr = (t - i0)[..., None]
    glow = G[i0] * (1 - fr) + G[i1] * fr                                           # glow at each pixel, for a full disc
    sg = 0.35 * r
    near = cv2.GaussianBlur(lit, (0, 0), sg) / np.maximum(cv2.GaussianBlur(disc, (0, 0), sg), 1e-3)
    sky = f - glow                                                                # outside the disc: the sky without the glow
    rng = np.random.default_rng(29); far = skyish & (d > 2.5) & (d < 3.5)
    tex = rng.normal(0, (f[far] - col[np.where(far)[0]]).std(0) * 0.6, f.shape).astype(np.float32)
    inner = col[:, None, :] + cv2.GaussianBlur(tex, (0, 0), 1.2)                  # inside the disc: plain sky, a little grain
    q = ((1 - np.clip(near, 0, 1)) * np.clip((2.6 - d) / 0.8, 0, 1))[..., None]   # on the dark side the painted halo rings
    sky = sky * (1 - q) + inner * q                                               # give way to plain sky
    base = np.where((d < 1.0)[..., None], inner, sky)
    base = cv2.GaussianBlur(base, (0, 0), 2.0) * (np.abs(d - 1) < 0.03)[..., None] + base * (np.abs(d - 1) >= 0.03)[..., None]
    moonless = base + glow * np.clip(near, 0, 1)[..., None]                      # the glow kept round the lit part only
    out = f * lit[..., None] + moonless * (1 - lit[..., None])
    zone = (d < 3.3) & (skyish | (d < 1.05))
    w = cv2.GaussianBlur(zone.astype(np.float32), (0, 0), 1.5)[..., None]
    out = np.clip(f * (1 - w) + out * w, 0, 255)
    print(f'moon ({cx:.0f}, {cy:.0f}) r {r:.0f}: {LIT:.0%} lit, limb {LIMB} degrees')
    return out[..., ::-1]


def over_picture(pic, top, h, x0, x1, y0, y1, fade=170):
    """Ivory slide with the crop [y0:y1, x0:x1] of the picture filling rows top..h, faded in from ivory at its top."""
    crop = pic[y0:y1, x0:x1]; s = W / crop.shape[1]
    crop = cv2.resize(crop, (W, round(crop.shape[0] * s)), interpolation=cv2.INTER_AREA)
    p = np.zeros((h, W, 3), np.float32); p[:] = IVORY; n = min(h - top, crop.shape[0]); p[top:top + n] = crop[:n]
    a = np.clip((np.arange(h) - top) / fade, 0, 1)[:, None, None]; base = np.zeros_like(p); base[:] = IVORY
    return Image.fromarray((p * a + base * (1 - a)).astype(np.uint8))


def foot_on_picture(im, h):
    """astroriver.com in ivory with a soft shadow, readable on the painting's border and cloth."""
    sh = Image.new('RGBA', im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((W / 2, h - 52), 'astroriver.com', font=font(INTER, 26, 500), fill=(60, 10, 10, 230), anchor='ms')
    im = Image.alpha_composite(im.convert('RGBA'), sh.filter(ImageFilter.GaussianBlur(4))).convert('RGB')
    d = ImageDraw.Draw(im); d.text((W / 2, h - 52), 'astroriver.com', font=font(INTER, 26, 500), fill=IVORY, anchor='ms')
    return im, d


def brand(im):
    """ASTRO RIVER and the gold rule on top, as frame() draws them, without frame()'s 4:5 footer."""
    d = ImageDraw.Draw(im); d.text((W / 2, 96), 'A S T R O   R I V E R', font=font(PF, 36, 700), fill=MAROON, anchor='ms')
    d.line([(W / 2 - 170, 124), (W / 2 - 14, 124)], fill=GOLD, width=2); d.line([(W / 2 + 14, 124), (W / 2 + 170, 124)], fill=GOLD, width=2)
    d.polygon([(W / 2, 117), (W / 2 + 7, 124), (W / 2, 131), (W / 2 - 7, 124)], fill=GOLD)
    return im, d


def rule(d, y): d.line([(W / 2 - 60, y), (W / 2 + 60, y)], fill=GOLD, width=3)


def s1(out, pic):                                                                 # cover: the date over the karva
    im = over_picture(pic, 640, H, 185, 1415, 0, 900); im, d = frame(im); im, d = foot_on_picture(im, H)
    text(d, (W / 2, 262), 'करवा चौथ', BOLD, 132, MAROON, 'ms')
    text(d, (W / 2, 372), 'गुरुवार, 29 अक्टूबर', BOLD, 72, DGOLD, 'ms')
    rule(d, 420)
    d.text((W / 2, 492), 'India: Thursday 29 October', font=font(PFI, 40, 500), fill=INK, anchor='ms')
    d.text((W / 2, 546), 'USA, Canada and UK: Wednesday 28 October', font=font(PFI, 40, 500), fill=INK, anchor='ms')
    d.text((W / 2, 604), 'Swipe for your city’s moonrise  →', font=font(INTER, 26, 600), fill=(200, 100, 30), anchor='ms')
    im.save(os.path.join(out, 'karwa-chauth-1.jpg'), quality=95)


def s2(out):                                                                      # why the date differs by country
    im, d = frame()
    text(d, (W / 2, 250), 'कौन-सा दिन?', SEMI, 44, DGOLD, 'ms')
    text(d, (W / 2, 356), 'चंद्रोदय पर चतुर्थी', BOLD, 92, MAROON, 'ms')
    d.text((W / 2, 422), 'The day on which Chaturthi is running at your moonrise', font=font(PFI, 32, 500), fill=GREY, anchor='ms')
    rule(d, 466)
    text(d, (W / 2, 560), 'कृष्ण चतुर्थी: गुरुवार रात 1:07 – रात 10:10 (IST)', SEMI, 38, INK, 'ms')
    rows = [('भारत', 'India', 'गुरुवार, 29 अक्टूबर', 'Thursday 29 Oct'),
            ('अमेरिका, कनाडा', 'USA, Canada', 'बुधवार, 28 अक्टूबर', 'Wednesday 28 Oct'),
            ('ब्रिटेन', 'UK', 'बुधवार, 28 अक्टूबर *', 'Wednesday 28 Oct')]
    y = 640
    for hi, en, dhi, den in rows:
        d.line([(110, y), (970, y)], fill=RULE, width=2)
        text(d, (120, y + 70), hi, BOLD, 48, MAROON); d.text((120, y + 112), en, font=font(INTER, 24, 500), fill=GREY, anchor='ls')
        text(d, (960, y + 70), dhi, BOLD, 44, DGOLD, 'rs'); d.text((960, y + 112), den, font=font(INTER, 24, 500), fill=GREY, anchor='rs')
        y += 140
    d.line([(110, y), (970, y)], fill=RULE, width=2)
    text(d, (W / 2, y + 66), 'तिथि पूरी दुनिया में एक ही पल बदलती है, चांद हर शहर में अलग समय पर निकलता है।', SEMI, 29, INK, 'ms')
    d.text((W / 2, y + 112), '* London: Chaturthi holds at neither moonrise; the texts keep the earlier day.', font=font(INTER, 22, 500), fill=GREY, anchor='ms')
    im.save(os.path.join(out, 'karwa-chauth-2.jpg'), quality=95)


def times(out, name, label, head, en, rows, note):
    im, d = frame()
    text(d, (W / 2, 250), label, SEMI, 44, DGOLD, 'ms')
    text(d, (W / 2, 352), head, BOLD, 84, MAROON, 'ms')
    d.text((W / 2, 416), en, font=font(PFI, 34, 500), fill=GREY, anchor='ms')
    rule(d, 458)
    y, step = 520, 78 if len(rows) > 7 else 88
    for k, (city, t) in enumerate(rows):
        if k % 2 == 0: d.rounded_rectangle([110, y, 970, y + step - 6], radius=14, fill=(246, 236, 216))
        d.text((150, y + step / 2 + 9), city, font=font(PF, 38, 600), fill=INK, anchor='ls')
        d.text((930, y + step / 2 + 9), t, font=font(INTER, 36, 600), fill=MAROON, anchor='rs')
        y += step
    text(d, (W / 2, y + 74), note, SEMI, 32, INK, 'ms')
    im.save(os.path.join(out, name), quality=95)


INDIA = [('New Delhi', '8:17 pm'), ('Chandigarh', '8:12 pm'), ('Amritsar', '8:18 pm'), ('Lucknow', '8:06 pm'),
         ('Jaipur', '8:28 pm'), ('Mumbai', '9:00 pm'), ('Kolkata', '7:47 pm'), ('Chennai', '8:44 pm')]
ABROAD = [('New York', '7:35 pm'), ('Toronto', '7:45 pm'), ('Chicago', '7:27 pm'), ('Houston', '8:41 pm'),
          ('San Francisco', '8:08 pm'), ('Vancouver', '7:18 pm'), ('London *', '5:34 pm')]


def s3(out): times(out, 'karwa-chauth-3.jpg', 'चंद्रोदय · भारत', 'गुरुवार, 29 अक्टूबर', 'Moonrise in India, Thursday 29 October',
                   INDIA, 'हर शहर का अपना समय, साफ़ क्षितिज पर')


def s4(out): times(out, 'karwa-chauth-4.jpg', 'चंद्रोदय · विदेश में', 'बुधवार, 28 अक्टूबर', 'Moonrise abroad, Wednesday 28 October, local time',
                   ABROAD, 'हर शहर की अपनी घड़ी का समय')


def s5(out):                                                                      # the day, sargi to arghya
    im, d = frame()
    text(d, (W / 2, 250), 'व्रत का दिन · नई दिल्ली', SEMI, 44, DGOLD, 'ms')
    text(d, (W / 2, 356), 'सरगी से अर्घ्य तक', BOLD, 92, MAROON, 'ms')
    d.text((W / 2, 422), 'From the meal before dawn to the Moon', font=font(PFI, 34, 500), fill=GREY, anchor='ms')
    steps = [('भोर से पहले', 'सरगी', 'Sargi, before sunrise'),
             ('सुबह 6:31', 'व्रत आरंभ', 'The fast begins at sunrise'),
             ('शाम 5:39 के बाद', 'पूजा और कथा', 'Gauri puja and the katha, after sunset'),
             ('रात 8:17', 'चंद्रोदय, अर्घ्य', 'Water to the Moon, seen through the sieve')]
    x, y0, step = 200, 500, 140
    d.line([(x, y0 + 10), (x, y0 + 3 * step + 10)], fill=GOLD, width=3)
    for k, (t, what, en) in enumerate(steps):
        y = y0 + k * step; last = k == len(steps) - 1
        d.ellipse([x - 14, y - 4, x + 14, y + 24], fill=MAROON if last else IVORY, outline=MAROON, width=3)
        text(d, (x + 50, y + 20), t, SEMI, 32, DGOLD)
        text(d, (x + 50, y + 78), what, BOLD, 50, MAROON)
        d.text((x + 50, y + 116), en, font=font(INTER, 24, 500), fill=GREY, anchor='ls')
    d.rounded_rectangle([140, 1100, 940, 1190], radius=45, fill=MAROON)
    text(d, (W / 2, 1160), 'परिवार का अपना पंचांग हो, तो उसी को मानें', SEMI, 36, IVORY, 'ms')
    im.save(os.path.join(out, 'karwa-chauth-5.jpg'), quality=95)


def s6(out):                                                                      # the soft link
    im, d = frame()
    text(d, (W / 2, 300), 'अपने शहर का चंद्रोदय', BOLD, 84, MAROON, 'ms')
    d.text((W / 2, 368), 'Your city’s moonrise, and the whole fast', font=font(PFI, 36, 500), fill=GREY, anchor='ms')
    rule(d, 412)
    items = [('चंद्रोदय', 'शहर-शहर का समय', 'Moonrise, city by city'), ('सरगी', 'भोर से पहले का भोजन', 'The meal before dawn'),
             ('कथा', 'वीरावती और करवा की कहानी', 'The katha of Veeravati and Karva'), ('विधि', 'करवा, छलनी और थाली', 'The karva, the sieve and the thali')]
    y = 500
    for k, (head, hi, en) in enumerate(items):
        d.polygon([(150, y - 14), (162, y - 2), (150, y + 10), (138, y - 2)], fill=GOLD)
        text(d, (190, y + 12), head, BOLD, 48, MAROON)
        text(d, (400, y + 6), hi, SEMI, 34, INK); d.text((400, y + 46), en, font=font(INTER, 23, 500), fill=GREY, anchor='ls')
        y += 120
    d.rounded_rectangle([90, 985, 990, 1185], radius=28, fill=MAROON)
    text(d, (W / 2, 1060), 'पूरी जानकारी हिंदी और English में', SEMI, 40, IVORY, 'ms')
    d.text((W / 2, 1140), 'astroriver.com/journal/karwa-chauth', font=font(INTER, 40, 600), fill=(240, 200, 120), anchor='ms')
    im.save(os.path.join(out, 'karwa-chauth-6.jpg'), quality=95)


def story(out, pic):                                                              # 9:16: the date, Delhi and New York, the link
    SH = 1920
    im = over_picture(pic, 1130, SH, 185, 1415, 0, 900, fade=200); im, d = brand(im); im, d = foot_on_picture(im, SH)
    text(d, (W / 2, 330), 'करवा चौथ', BOLD, 150, MAROON, 'ms')
    d.text((W / 2, 410), 'Karwa Chauth 2026', font=font(PFI, 44, 500), fill=GREY, anchor='ms')
    rule(d, 460)
    for k, (hi, en, t) in enumerate([('भारत · गुरुवार, 29 अक्टूबर', 'India · Thursday 29 Oct', 'नई दिल्ली चंद्रोदय रात 8:17'),
                                     ('अमेरिका, कनाडा, ब्रिटेन · बुधवार, 28 अक्टूबर', 'USA, Canada, UK · Wednesday 28 Oct', 'New York moonrise 7:35 pm')]):
        y = 560 + k * 230
        text(d, (W / 2, y), hi, BOLD, 50, MAROON, 'ms')
        d.text((W / 2, y + 52), en, font=font(INTER, 28, 500), fill=GREY, anchor='ms')
        text(d, (W / 2, y + 118), t, SEMI, 40, DGOLD, 'ms')
    d.rounded_rectangle([120, 990, 960, 1090], radius=50, fill=MAROON)
    text(d, (W / 2, 1056), 'अपने शहर का समय: लिंक पर', SEMI, 40, IVORY, 'ms')
    im.save(os.path.join(out, 'karwa-chauth-story.jpg'), quality=95)


if __name__ == '__main__':
    o = sys.argv[1]; os.makedirs(o, exist_ok=True); pic = picture()
    s1(o, pic); s2(o); s3(o); s4(o); s5(o); s6(o); story(o, pic)
