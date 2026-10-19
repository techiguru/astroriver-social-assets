# Navratri 2026, Vijayadashami (Tue 20 Oct): "माँ के 9 रूप", the nine daily Navratri pictures joined into one Reel, as
# agreed with the founder on 11 Oct ("At the end, the nine become one ... pin that on the profile and use it again next
# year"; his reference was a Reel where the nine forms pass by in a train window). Built from the approved clean
# pictures (posts/navratri-2026-sources/ for Days 1-7, out/navratri/d8 and d9 for Days 8 and 9); no video model, and
# no goddess ever moves: each picture only drifts very slowly, and the forms slide past one after another like the
# view from a train window. Opens on all nine in a 3x3 grid with the title, ends on the grid again with the Vijayadashami
# greeting, then the Astro River end card. Text keeps out of what Instagram lays over a Reel (measured on the founder's
# Day 8 screenshot): the top bar down to y 193, the repost bubbles y 1248-1480 on the left, the buttons right of x 950,
# the username and caption from y 1591. Each form's name sits in a small cream label at y 1488-1584.
# Usage: python3 navratri_nine_forms.py <absolute outdir>   (silent 1080x1920 Reel, cover, and check frames)
import os, sys, subprocess
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
W, H, FPS = 1080, 1920, 24
SRC = ROOT + '/posts/navratri-2026-sources/'
FORMS = [  # picture, name, crown top in the picture once it is 1080 wide (for the grid crop)
    (SRC + 'day1-shailputri.png', 'शैलपुत्री', 425), (SRC + 'day2-brahmacharini.png', 'ब्रह्मचारिणी', 225),
    (SRC + 'day3-chandraghanta.png', 'चन्द्रघण्टा', 125), (SRC + 'day4-kushmanda.png', 'कूष्माण्डा', 350),
    (SRC + 'day5-skandamata.png', 'स्कन्दमाता', 250), (SRC + 'day6-katyayani.png', 'कात्यायनी', 275),
    (SRC + 'day7-kalaratri.png', 'कालरात्रि', 250), (HERE + '/out/navratri/d8/mahagauri-source.png', 'महागौरी', 325),
    (HERE + '/out/navratri/d9/siddhidatri-canva.png', 'सिद्धिदात्री', 475)]
CREAM = (232, 245, 251)                # BGR of #FBF5E8
MAROON = (122, 31, 43)                 # RGB, the name colour used all Navratri
T_GRID, T_IN, T_FORM, T_SLIDE = 3.0, 0.8, 5.0, 0.7
T_OUT, T_GREET, T_END = 0.8, 3.2, 3.5


def fonts():
    """The Noto Serif Devanagari web fonts of the text layer, as TTF files PIL can draw with (shaped with raqm)."""
    d = HERE + '/out/fonts-ttf/'; os.makedirs(d, exist_ok=True)
    for n in ('noto-serif-devanagari-devanagari-700-normal', 'noto-serif-devanagari-devanagari-600-normal'):
        if not os.path.exists(d + n + '.ttf'):
            from fontTools.ttLib import TTFont
            f = TTFont(HERE + '/fonts/' + n + '.woff2'); f.flavor = None; f.save(d + n + '.ttf')
    return d + 'noto-serif-devanagari-devanagari-700-normal.ttf', d + 'noto-serif-devanagari-devanagari-600-normal.ttf'


def text_layer(lines, size=(W, H)):
    """Transparent RGBA layer of centred lines: (text, font file, px, rgb, baseline y). The Devanagari web font has only
    Devanagari, so every other character (digits, Latin letters, punctuation, dashes) is drawn in Lora at the same size
    and baseline."""
    im = Image.new('RGBA', size, (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    lora = HERE + '/fonts/Lora[wght].ttf'
    for txt, ff, px, rgb, y in lines:
        dev = 'devanagari' in ff
        runs, cur, kind = [], '', None
        for ch in txt:
            if ch == ' ' and kind: k = kind                                      # a space stays with its run
            else: k = 'latin' if dev and not ('\u0900' <= ch <= '\u097f' or ch in '\u200c\u200d') else 'main'
            if k != kind and cur: runs.append((cur, kind)); cur = ''
            cur += ch; kind = k
        if cur: runs.append((cur, kind))
        fs = []
        for r, k in runs:
            f = ImageFont.truetype(lora if k == 'latin' else ff, int(px * 0.92) if k == 'latin' else px, layout_engine=ImageFont.Layout.RAQM)
            if k == 'latin': f.set_variation_by_axes([700])                       # as bold as the Devanagari
            fs.append((r, f))
        x = (size[0] - sum(f.getlength(r) for r, f in fs)) / 2
        for r, f in fs: d.text((x, y), r, font=f, fill=rgb + (255,), anchor='ls'); x += f.getlength(r)
    return np.array(im).astype(np.float32)


def over(bg, layer, a=1.0):
    al = layer[..., 3:] / 255. * a
    return bg * (1 - al) + layer[..., [2, 1, 0]] * al


def load(p):
    im = cv2.imread(p); h, w = im.shape[:2]; im = cv2.resize(im, (W, round(h * W / w)), interpolation=cv2.INTER_AREA)
    if im.shape[0] < H: im = cv2.copyMakeBorder(im, 0, H - im.shape[0], 0, 0, cv2.BORDER_REPLICATE)
    y = (im.shape[0] - H) // 2; return im[y:y + H].astype(np.float32)


def drift(im, u):
    """A very slow push-in (the whole picture, never the goddess alone): 1.00 to 1.04 over the form."""
    s = 1 + 0.04 * u; M = np.float32([[s, 0, W / 2 * (1 - s)], [0, s, H * 0.42 * (1 - s)]])
    return cv2.warpAffine(im, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


def ease(u): return 0.5 - 0.5 * np.cos(np.pi * np.clip(u, 0, 1))


def grid(pics, cw=300, ch=467, y0=404):
    """All nine on cream, 3 x 3, each cell a crop from just above her crown, with a thin gold edge."""
    g = np.zeros((H, W, 3), np.float32); g[:] = CREAM
    gap = 14; x0 = (W - 3 * cw - 2 * gap) // 2
    for i, (im, (_, _, crown)) in enumerate(zip(pics, FORMS)):
        s = cw / W; small = cv2.resize(im, (cw, round(H * s)), interpolation=cv2.INTER_AREA)
        oy = int(np.clip(crown * s - 26, 0, small.shape[0] - ch)); cell = small[oy:oy + ch]
        x, y = x0 + (i % 3) * (cw + gap), y0 + (i // 3) * (ch + gap)
        g[y - 3:y + ch + 3, x - 3:x + cw + 3] = (58, 151, 201)            # gold #C9973A
        g[y:y + ch, x:x + cw] = cell
    return g


def build(out):
    bold, semi = fonts(); os.makedirs(out, exist_ok=True)
    pics = [load(p) for p, _, _ in FORMS]; G = grid(pics)
    title = text_layer([('A S T R O   R I V E R', HERE + '/fonts/PlayfairDisplay[wght].ttf', 24, MAROON, 236),
                        ('माँ के 9 रूप', bold, 92, MAROON, 352)])
    greet = text_layer([('A S T R O   R I V E R', HERE + '/fonts/PlayfairDisplay[wght].ttf', 24, MAROON, 236),
                        ('विजयादशमी की हार्दिक शुभकामनाएँ', bold, 62, MAROON, 338)])
    labels = []
    for i, (_, name, _) in enumerate(FORMS):
        lab = np.zeros((H, W, 4), np.float32); pill = np.zeros((H, W), np.uint8)
        cv2.rectangle(pill, (190, 1490), (890, 1582), 255, -1); pill = cv2.GaussianBlur(pill.astype(np.float32), (0, 0), 3)
        lab[..., :3] = (251, 245, 232); lab[..., 3] = pill * 0.9                     # cream label, RGB order like text_layer
        t = text_layer([(f'दिन {i + 1}  ·  माँ {name}', bold, 54, MAROON, 1553)])
        a = t[..., 3:] / 255.; lab[..., :3] = lab[..., :3] * (1 - a) + t[..., :3] * a; lab[..., 3] = np.maximum(lab[..., 3], t[..., 3])
        labels.append(lab)
    end = np.zeros((H, W, 3), np.float32); end[:] = CREAM
    end = over(end, text_layer([('A S T R O   R I V E R', HERE + '/fonts/PlayfairDisplay[wght].ttf', 64, MAROON, 940),
                                ('INSTITUTE · EST. 2008 · JALANDHAR, INDIA', HERE + '/fonts/Inter[opsz,wght].ttf', 24, (107, 74, 46), 1010),
                                ('astroriver.com', HERE + '/fonts/Inter[opsz,wght].ttf', 32, (181, 101, 29), 1080)]))
    t_forms = T_GRID; t_after = t_forms + 9 * T_FORM; t_end = t_after + T_OUT + T_GREET; total = t_end + T_END
    n = int(round(total * FPS)); fn = os.path.join(out, 'nine-forms-silent.mp4')
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-crf', '16', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', fn], stdin=subprocess.PIPE)
    def form_frame(i, t):                      # form i at time t since it came in
        f = over(drift(pics[i], t / T_FORM), labels[i], ease(min(t / 0.6, (T_FORM - t) / 0.4 if i < 8 else 1)))
        return f
    for k in range(n):
        t = k / FPS
        if t < t_forms:                                                             # the grid and the title
            s = 1 + 0.02 * t / T_GRID; M = np.float32([[s, 0, W / 2 * (1 - s)], [0, s, H / 2 * (1 - s)]])
            f = over(cv2.warpAffine(G, M, (W, H), borderMode=cv2.BORDER_REPLICATE), title, ease(t / 0.8))
            if t > t_forms - T_IN:                                                  # into Day 1
                u = ease((t - (t_forms - T_IN)) / T_IN); f = f * (1 - u) + form_frame(0, 0) * u
        elif t < t_after:                                                           # the nine forms, sliding past
            i = min(int((t - t_forms) // T_FORM), 8); lt = t - t_forms - i * T_FORM
            f = form_frame(i, lt)
            if i < 8 and lt > T_FORM - T_SLIDE:                                     # next one slides in from the right
                u = ease((lt - (T_FORM - T_SLIDE)) / T_SLIDE); dx = int(round(W * u))
                nxt = form_frame(i + 1, 0); g = np.empty_like(f)
                g[:, :W - dx] = f[:, dx:]; g[:, W - dx:] = nxt[:, :dx] if dx else g[:, W - dx:]
                f = g
        elif t < t_end:                                                             # back to all nine, the greeting
            lt = t - t_after; f = G.copy(); f = over(f, greet, ease((lt - 0.3) / 0.8))
            if lt < T_OUT: u = ease(lt / T_OUT); f = form_frame(8, T_FORM) * (1 - u) + f * u
        else:                                                                       # the end card
            u = ease((t - t_end) / 0.7); last = over(G.copy(), greet); f = last * (1 - u) + end * u
        enc.stdin.write(np.clip(f, 0, 255).astype(np.uint8).tobytes())
    enc.stdin.close(); enc.wait()
    # the cover: a smaller grid, so that the title and all nine fit inside the profile grid's 3:4 crop (y 240-1680)
    cover = over(grid(pics, 268, 417, 384), text_layer([('माँ के 9 रूप', bold, 88, MAROON, 352)]))
    cv2.imwrite(os.path.join(out, 'nine-forms-cover.png'), cover.astype(np.uint8))
    print('seconds', total)


if __name__ == '__main__':
    build(sys.argv[1])
