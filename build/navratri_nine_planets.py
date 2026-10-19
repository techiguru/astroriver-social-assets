# Vijayadashami (Tue 20 Oct 2026): "आपका कमज़ोर ग्रह, माँ के किस रूप का पूजन करें?", the nine Navratri pictures joined
# into one Reel that answers a question (founder 19 Oct: the Reels average 3 s of watching, and the plain nine-forms
# film "has nothing interesting"). Each form of Navadurga governs a planet (Drik Panchang, each form's page: Shailputri
# Chandra, Brahmacharini Mangal, Chandraghanta Shukra, Kushmanda Surya, Skandamata Budha, Katyayani Brihaspati,
# Kalaratri Shani, Mahagauri Rahu, Siddhidatri Ketu). The signs on each card are the founder's approved wording
# (19 Oct: "All are good"). The question is on screen from the very first frame, with a promise that keeps people
# watching ("more than one planet weak? the remedy is at the end"); each card asks first (the sign), then names the
# planet, then the form of Maa, while her picture slides in like the view from a train window. After the nine comes
# the remedy for more than one troubled planet: Lord Shiva (the founder, 19 Oct: "the answer to everything is actually
# lord shiva"), from a Canva picture checked for his iconography (tiger skin, Nandi a humped bull). No deity ever
# moves. It ends honestly ("these are only signs; your chart tells") and asks for a comment (the founder answers them;
# no "free" wording), then loops to the start.
# Text keeps out of what Instagram lays over a Reel (measured on the founder's Day 8 screenshot): nothing above y 193,
# nothing right of x 950 below y 773, nothing in y 1248-1480 on the left or below y 1591; all text here sits in
# y 200-1000. The band under Instagram's top bar is a soft marigold wash, not empty cream, and ASTRO RIVER stands
# right below it on every frame (founder 19 Oct: the blank head of each slide made the brand look like it doesn't exist).
# Usage: python3 navratri_nine_planets.py <absolute outdir> [stills]   (silent Reel, cover and pin; or only the stills)
import os, sys, subprocess
import numpy as np, cv2
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import navratri_nine_forms as N
W, H, FPS = N.W, N.H, N.FPS
CARDS = [  # sign, planet, planet symbol (DejaVu Sans), form
    ('नींद नहीं, मन बेचैन?', 'चन्द्र', '☽', 'शैलपुत्री'),
    ('गुस्सा जल्दी, हिम्मत कम?', 'मंगल', '♂', 'ब्रह्मचारिणी'),
    ('रिश्तों में खटास?', 'शुक्र', '♀', 'चन्द्रघण्टा'),
    ('आत्मविश्वास कम, मान-सम्मान नहीं?', 'सूर्य', '☉', 'कूष्माण्डा'),
    ('बोलने-पढ़ने में अटकते हैं?', 'बुध', '☿', 'स्कन्दमाता'),
    ('विवाह या संतान में देरी?', 'बृहस्पति', '♃', 'कात्यायनी'),
    ('मेहनत बहुत, फल कम?', 'शनि', '♄', 'कालरात्रि'),
    ('अचानक उलझनें, भ्रम?', 'राहु', '☊', 'महागौरी'),
    ('मन कहीं नहीं लगता?', 'केतु', '☋', 'सिद्धिदात्री')]
SHIVA = (HERE + '/out/vijayadashami/shiva-canva.png', 655)    # the picture, the top of his jata
MAROON, SAFFRON, INK = (122, 31, 43), (181, 84, 22), (59, 36, 23)
SYM = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
WIN_Y = 630                                     # the picture window: y 630 to the bottom
T_HOOK, T_CARD, T_SLIDE, T_SHIVA, T_END = 2.4, 2.7, 0.45, 3.4, 5.0
LINE_B, LINE_C = 0.35, 0.75                     # when the planet and the form appear on a card


def cream():
    c = np.zeros((H, W, 3), np.float32); c[:] = N.CREAM; return c


def window(im, crown):
    """Her picture from just above her crown down, filling the window below the text."""
    y0 = int(np.clip(crown - 40, 0, im.shape[0] - (H - WIN_Y))); return im[y0:y0 + H - WIN_Y]


def drift(win, u):
    h = win.shape[0]; s = 1 + 0.035 * u; M = np.float32([[s, 0, W / 2 * (1 - s)], [0, s, h * 0.3 * (1 - s)]])
    return cv2.warpAffine(win, M, (W, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


def symbol_layer(ch, px, rgb, cx, baseline):
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); f = ImageFont.truetype(SYM, px)
    ImageDraw.Draw(im).text((cx, baseline), ch, font=f, fill=rgb + (255,), anchor='ms')
    return np.array(im).astype(np.float32)


def header():
    """Every frame's head: a marigold wash fading into the cream under Instagram's top bar, ASTRO RIVER in bold
    letter-spaced Playfair right below it, and a thin gold rule with a diamond."""
    from PIL import Image, ImageDraw, ImageFont
    h = np.zeros((H, W, 4), np.float32); y = np.arange(230)
    h[:230, :, :3] = (245, 205, 140); h[:230, :, 3] = (255 * (1 - y / 230) ** 1.6)[:, None]
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    f = ImageFont.truetype(N.HERE + '/fonts/PlayfairDisplay[wght].ttf', 44); f.set_variation_by_axes([700])
    d.text((W / 2, 262), 'A S T R O   R I V E R', font=f, fill=MAROON + (255,), anchor='ms')
    gold = (201, 151, 58, 255)
    d.line([(W / 2 - 190, 292), (W / 2 - 16, 292)], fill=gold, width=2); d.line([(W / 2 + 16, 292), (W / 2 + 190, 292)], fill=gold, width=2)
    d.polygon([(W / 2, 283), (W / 2 + 9, 292), (W / 2, 301), (W / 2 - 9, 292)], fill=gold)
    t = np.array(im).astype(np.float32); a = t[..., 3:] / 255.
    h[..., :3] = h[..., :3] * (1 - a) + t[..., :3] * a; h[..., 3] = np.maximum(h[..., 3], t[..., 3])
    return h


def hook_layer(bold):
    return N.text_layer([('आपका कमज़ोर ग्रह —', bold, 74, MAROON, 378),
                         ('माँ के किस रूप का', bold, 74, MAROON, 473),
                         ('पूजन करें?', bold, 74, MAROON, 568),
                         ('एक से ज़्यादा ग्रह कमज़ोर? उपाय अंत में', bold, 44, SAFFRON, 638)])


def stills(out):
    """The cover (the head, the hook and all nine, everything inside the profile grid's 3:4 crop, y 240-1680) and the
    2:3 picture for Pinterest and Google Business (1080 x 1620, the same layout moved up)."""
    bold, _ = N.fonts(); os.makedirs(out, exist_ok=True)
    pics = [N.load(p) for p, _, _ in N.FORMS]; hook, head = hook_layer(bold), header()
    cov = N.grid(pics, 200, 311, 718)                                         # text moved 40 px down: ASTRO RIVER clears y 240
    for l in (hook, head): cov = N.over(cov, np.roll(l, 40, axis=0))
    cv2.imwrite(os.path.join(out, 'nine-planets-cover.jpg'), cov.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 94])
    pin = N.grid(pics, 220, 343, 522)
    for l in (hook, head): pin = N.over(pin, np.roll(l, -150, axis=0))
    pin = pin[:1620]
    cv2.imwrite(os.path.join(out, 'nine-planets-pin.jpg'), pin.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 94])


def build(out):
    bold, semi = N.fonts(); os.makedirs(out, exist_ok=True)
    pics = [N.load(p) for p, _, _ in N.FORMS]
    wins = [window(pics[i], crown) for i, (_, _, crown) in enumerate(N.FORMS)] + [window(N.load(SHIVA[0]), SHIVA[1])]
    G = N.grid(pics, 252, 392, 672); HEAD = header(); hook = hook_layer(bold)
    A, B, C = [], [], []
    for i, (sign, planet, sym, form) in enumerate(CARDS):
        A.append(N.text_layer([(sign, bold, 60 if len(sign) < 26 else 52, INK, 375)]))
        B.append(N.text_layer([(f'{planet} कमज़ोर', bold, 66, SAFFRON, 478)]))
        C.append(N.text_layer([(f'माँ {form} का पूजन करें', bold, 58, MAROON, 580)]))
    # planet symbols sit to the left of "<planet> कमज़ोर": find where that text starts, put the symbol 60 px before it
    for i, (_, _, sym, _) in enumerate(CARDS):
        cols = np.where(B[i][448:488, :, 3].max(0) > 0)[0]; x = cols.min() - 52
        B[i] = np.maximum(B[i], symbol_layer(sym, 64, SAFFRON, x, 480))
    A.append(N.text_layer([('एक से ज़्यादा ग्रह परेशान करें?', bold, 52, INK, 375)]))     # the remedy promised on frame 1
    B.append(N.text_layer([('भगवान शिव की आराधना करें', bold, 62, SAFFRON, 478)]))
    C.append(N.text_layer([('ॐ नमः शिवाय', bold, 64, MAROON, 580)]))
    endtxt = N.text_layer([('विजयादशमी की हार्दिक शुभकामनाएँ', bold, 54, MAROON, 368),
                           ('ये केवल संकेत हैं —', semi, 44, INK, 442),
                           ('कौन-सा ग्रह सच में कमज़ोर है,', semi, 44, INK, 500),
                           ('यह आपकी कुंडली बताती है।', semi, 44, INK, 558),
                           ('अपना कमज़ोर ग्रह जानना है?', bold, 50, SAFFRON, 650),
                           ('Comment में लिखें: ग्रह', bold, 60, MAROON, 728),
                           ('astroriver.com', N.HERE + '/fonts/Inter[opsz,wght].ttf', 34, (181, 101, 29), 795)])
    Gend = N.grid(pics, 220, 342, 860)
    t_cards = T_HOOK; t_shiva = t_cards + 9 * T_CARD; t_end = t_shiva + T_SHIVA; total = t_end + T_END
    n = int(round(total * FPS)); fn = os.path.join(out, 'nine-planets-silent.mp4')
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-crf', '16', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', fn], stdin=subprocess.PIPE)
    fade = lambda x, d=0.18: float(np.clip(x / d, 0, 1))
    def card(i, lt, with_window=True):
        f = cream()
        if with_window: f[WIN_Y:] = drift(wins[i], lt / (T_SHIVA if i == 9 else T_CARD))
        f = N.over(f, A[i], fade(lt))
        f = N.over(f, B[i], fade(lt - LINE_B)); f = N.over(f, C[i], fade(lt - LINE_C))
        return f
    for k in range(n):
        t = k / FPS
        if t < t_cards:                                                      # the question, on screen from frame 1
            s = 1 + 0.03 * t / T_HOOK; M = np.float32([[s, 0, W / 2 * (1 - s)], [0, s, 1100 * (1 - s)]])
            f = N.over(cv2.warpAffine(G, M, (W, H), borderMode=cv2.BORDER_REPLICATE), hook)
            if t > t_cards - 0.3:                                            # quick cut to the first card
                u = N.ease((t - (t_cards - 0.3)) / 0.3); f = f * (1 - u) + card(0, 0) * u
        elif t < t_end:
            if t < t_shiva: i = min(int((t - t_cards) // T_CARD), 8); lt = t - t_cards - i * T_CARD
            else: i, lt = 9, t - t_shiva                                     # Lord Shiva, the remedy
            f = card(i, lt)
            if i < 9 and lt > T_CARD - T_SLIDE:                               # the next one slides in, the text changes
                u = N.ease((lt - (T_CARD - T_SLIDE)) / T_SLIDE); dx = int(round(W * u))
                cur = f[WIN_Y:].copy(); nxt = drift(wins[i + 1], 0)
                f[WIN_Y:, :W - dx] = cur[:, dx:]
                if dx: f[WIN_Y:, W - dx:] = nxt[:, :dx]
                top = cream()
                f[:WIN_Y] = f[:WIN_Y] * (1 - u) + top[:WIN_Y] * u
        else:                                                                # honest ending, then back to the start
            lt = t - t_end; f = Gend.copy(); f = N.over(f, endtxt, N.ease(lt / 0.4))
            if lt < 0.4: u = N.ease(lt / 0.4); f = card(9, T_SHIVA) * (1 - u) + f * u
            if lt > T_END - 0.35:
                u = N.ease((lt - (T_END - 0.35)) / 0.35); h0 = N.over(G, hook); f = f * (1 - u) + h0 * u
        f = N.over(f, HEAD)                                                  # the marigold head and ASTRO RIVER, always
        enc.stdin.write(np.clip(f, 0, 255).astype(np.uint8).tobytes())
    enc.stdin.close(); enc.wait()
    stills(out); print('seconds', total)


if __name__ == '__main__':
    stills(sys.argv[1]) if sys.argv[2:] == ['stills'] else build(sys.argv[1])
