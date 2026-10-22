# Papankusha Ekadashi story (Thu 22 Oct 2026), the founder's approval relayed by the chief-of-staff chat: a 9:16 frame
# for the Instagram Story and WhatsApp Status, and a 4:5 version for X and Facebook. English only. Facts from the site's
# panchang (New Delhi): Shukla Ekadashi 2:12 pm Wed to 2:48 pm Thu, so Ekadashi stands at sunrise today. The name:
# papa (wrongdoing) + ankusha (the goad that holds it back); tradition worships Vishnu as Padmanabha today; Thursday is
# kept as Vishnu's day. The picture (tulsi, diya, conch, yellow flowers) is a Canva generation brought to HD with
# Real-ESRGAN; the founder adds the "Times for your city" link sticker in the Instagram app, in the space kept for it.
# Usage: python3 ekadashi_story.py <outdir>
import os, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ravi_pushya_carousel import font, IVORY, MAROON, GOLD, DGOLD, INK, GREY, PF, PFI, INTER
from bijoya_carousel import para


def compose(W, H, top, src_y, text_top, scale=1.0):
    pic = cv2.imread(HERE + '/out/ekadashi/tulsi-hd.png')[..., ::-1].astype(np.float32)
    p = np.zeros((H, W, 3), np.float32); p[:] = IVORY
    if scale < 1:                                                                 # the whole still life, on the same ivory
        sp = cv2.resize(pic, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA); x0 = (W - sp.shape[1]) // 2
        band = sp[round(src_y * scale):round(src_y * scale) + H - top]; e = np.ones(band.shape[1], np.float32)
        e[:80] = np.linspace(0, 1, 80); e[-80:] = np.linspace(1, 0, 80); e = e[None, :, None]
        p[top:top + band.shape[0], x0:x0 + band.shape[1]] = band * e + p[top:top + band.shape[0], x0:x0 + band.shape[1]] * (1 - e)
    else: p[top:] = pic[src_y:src_y + H - top]
    a = np.clip((np.arange(H) - top) / 200, 0, 1)[:, None, None]; base = np.zeros_like(p); base[:] = IVORY
    im = Image.fromarray((p * a + base * (1 - a)).astype(np.uint8)); d = ImageDraw.Draw(im); y = text_top
    d.text((W / 2, y), 'A S T R O   R I V E R', font=font(PF, 38, 700), fill=MAROON, anchor='ms'); r = y + 28
    d.line([(W / 2 - 170, r), (W / 2 - 14, r)], fill=GOLD, width=2); d.line([(W / 2 + 14, r), (W / 2 + 170, r)], fill=GOLD, width=2)
    d.polygon([(W / 2, r - 7), (W / 2 + 7, r), (W / 2, r + 7), (W / 2 - 7, r)], fill=GOLD)
    y += 110; d.text((W / 2, y), 'THURSDAY 22 OCT', font=font(INTER, 28, 600), fill=(200, 100, 30), anchor='ms')
    y += 96; d.text((W / 2, y), 'Papankusha Ekadashi', font=font(PF, 74, 700), fill=MAROON, anchor='ms')
    y += 84; d.text((W / 2, y), 'today, on Vishnu’s own day', font=font(PFI, 56, 600), fill=MAROON, anchor='ms')
    y += 70; para(d, W / 2, y, 'Papa + ankusha: the goad that holds back wrongdoing. The tradition worships Vishnu as Padmanabha today.',
                  font(INTER, 32, 400), INK, W - 200, 44, anchor='ms')
    y += 150; d.rounded_rectangle([W / 2 - 330, y - 54, W / 2 + 330, y + 40], radius=47, fill=MAROON)
    d.text((W / 2, y + 2), 'Ekadashi ends 2:48 PM · New Delhi', font=font(INTER, 34, 600), fill=IVORY, anchor='ms')
    y += 100; d.text((W / 2, y), 'Fast today. When to break it: in tonight’s story.', font=font(INTER, 30, 500), fill=INK, anchor='ms')
    # the space below is left clear for the founder's link sticker in the Instagram app
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((W / 2, H - 60), 'astroriver.com/panchang', font=font(INTER, 28, 600), fill=(60, 30, 10, 220), anchor='ms')
    im = Image.alpha_composite(im.convert('RGBA'), sh.filter(ImageFilter.GaussianBlur(6))).convert('RGB'); d = ImageDraw.Draw(im)
    d.text((W / 2, H - 60), 'astroriver.com/panchang', font=font(INTER, 28, 600), fill=IVORY, anchor='ms')
    return im


def build(out):
    os.makedirs(out, exist_ok=True)
    compose(1080, 1920, 1000, 860, 230).save(os.path.join(out, 'ekadashi-story.jpg'), quality=95)   # Story and WhatsApp Status
    compose(1080, 1350, 680, 860, 90, 0.8).save(os.path.join(out, 'ekadashi-feed.jpg'), quality=95)     # X and Facebook


if __name__ == '__main__':
    build(sys.argv[1])
