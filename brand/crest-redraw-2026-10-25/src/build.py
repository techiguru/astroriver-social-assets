#!/usr/bin/env python3
"""Astro River crest redraw — three options, generated as pure vector SVG.

Letters come from open-licence fonts (Cinzel, Cormorant Garamond; SIL OFL)
and are converted to outlines here, so the SVGs need no font.

Usage: python3 build.py FONT_DIR OUT_DIR
FONT_DIR must hold static instances named Cinzel-<wght>.ttf and
CormorantGaramond-<wght>.ttf (see README.md for how they were made).
"""
import math
import os
import sys

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONT_DIR, OUT = sys.argv[1], sys.argv[2]
_fonts = {}


def font(name):
    if name not in _fonts:
        _fonts[name] = TTFont(os.path.join(FONT_DIR, name + ".ttf"))
    return _fonts[name]


def glyph_path(fname, ch, x, y, scale):
    """Outline of one glyph, baseline-left at (x, y), as SVG path data."""
    f = font(fname)
    gs = f.getGlyphSet()
    g = f.getBestCmap()[ord(ch)]
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.1f}")
    gs[g].draw(TransformPen(pen, (scale, 0, 0, -scale, x, y)))
    return pen.getCommands(), gs[g].width * scale


def text_path(fname, text, cx, y, size, tracking=0.0):
    """Centred single line of text as outlines. tracking in em."""
    f = font(fname)
    upm = f["head"].unitsPerEm
    s = size / upm
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    adv = []
    for ch in text:
        adv.append(gs[cmap[ord(ch)]].width * s + tracking * size)
    total = sum(adv) - tracking * size
    x = cx - total / 2
    parts = []
    for ch, a in zip(text, adv):
        if ch != " ":
            d, _ = glyph_path(fname, ch, x, y, s)
            parts.append(d)
        x += a
    return " ".join(parts)


# ---------------------------------------------------------------- geometry
def P(a, r, cx, cy):
    """Point at angle a (degrees, 0 = top, clockwise) on circle."""
    t = math.radians(a)
    return cx + r * math.sin(t), cy - r * math.cos(t)


def arc(cx, cy, r, a0, a1):
    x0, y0 = P(a0, r, cx, cy)
    x1, y1 = P(a1, r, cx, cy)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f"M{x0:.2f},{y0:.2f} A{r},{r} 0 {large} 1 {x1:.2f},{y1:.2f}"


def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return (u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
            u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1])


def ribbon(segs, width, n=90):
    """Filled tapering ribbon along a chain of cubic Beziers.
    segs: list of (p0,p1,p2,p3); width(t) for t in 0..1 over whole chain."""
    pts = []
    k = len(segs)
    for i, s in enumerate(segs):
        for j in range(n + (1 if i == k - 1 else 0)):
            pts.append(bez(*s, j / n))
    m = len(pts)
    left, right = [], []
    for i, (x, y) in enumerate(pts):
        a = pts[max(i - 1, 0)]
        b = pts[min(i + 1, m - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        w = width(i / (m - 1)) / 2
        left.append((x + nx * w, y + ny * w))
        right.append((x - nx * w, y - ny * w))
    poly = left + right[::-1]
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in poly) + " Z"


def smooth_taper(w0, wmax, w1, peak=0.45):
    """Width profile: w0 at start, swelling to wmax, ending at w1."""
    def f(t):
        if t < peak:
            u = t / peak
            return w0 + (wmax - w0) * math.sin(u * math.pi / 2)
        u = (t - peak) / (1 - peak)
        return w1 + (wmax - w1) * max(0.0, math.cos(u * math.pi / 2)) ** 1.3
    return f


def river_width(w_tail, w_max, w_end):
    """Thin through the curl, swelling under the letters, fine at the mouth."""
    def f(t):
        if t < 0.22:
            return w_tail
        if t < 0.58:
            u = (t - 0.22) / 0.36
            return w_tail + (w_max - w_tail) * math.sin(u * math.pi / 2)
        u = (t - 0.58) / 0.42
        return w_end + (w_max - w_end) * max(0.0, math.cos(u * math.pi / 2)) ** 1.2
    return f


def river_path(T, k=1.0, kx=1.0, w=(4, 44, 1.5), reach=520):
    """The R's tail curls down and sweeps back left under the letters,
    leaving the ring through its lower opening."""
    tx, ty = T
    def p(dx, dy):
        return (tx + dx * k * kx, ty + dy * k)
    r = reach / 520
    segs = [(p(0, 0), p(26, 6), p(40, 40), p(16, 64)),
            (p(16, 64), p(-12, 90), p(-140 * r, 104), p(-270 * r, 114)),
            (p(-270 * r, 114), p(-370 * r, 122), p(-430 * r, 150), p(-480 * r, 214))]
    return ribbon(segs, river_width(*w))


def water_line(x0, x1, y, amp, periods, w, w_end=0.8):
    """Engraved water: a sine line tapering at both ends."""
    n = 160
    pts = [(x0 + (x1 - x0) * i / n, y - amp * math.sin(2 * math.pi * periods * i / n)) for i in range(n + 1)]
    segs = []
    for i in range(0, n, 2):  # quadratic-ish chain via cubic with coincident handles
        a, b, c = pts[i], pts[i + 1], pts[i + 2]
        segs.append((a, b, b, c))
    return ribbon(segs, smooth_taper(w_end, w, w_end, 0.5), n=4)


# ---------------------------------------------------------------- palette
INDIGO = ("#231a5c", "#140f38")          # centre, edge (as the site seal)
CREAM = ("#fbf5e7", "#f1e6cc")
GOLD_ON_INDIGO = ("#ecd08a", "#d2a650", "#b9893a")
GOLD_ON_CREAM = ("#b8893a", "#9a6f24", "#7a5617")

# Navaratna: one gem per graha. Ruby (Surya) sits in the sun.
GEMS = {
    "ruby":     ("Surya",   "#d41f3d"),
    "pearl":    ("Chandra", "#f6f1e6"),
    "coral":    ("Mangal",  "#e8553a"),
    "emerald":  ("Budh",    "#14a05a"),
    "ysapph":   ("Guru",    "#f6c623"),
    "diamond":  ("Shukra",  "#e9f6ff"),
    "bsapph":   ("Shani",   "#2f5fe0"),
    "hessonite": ("Rahu",   "#cf7a2a"),
    "catseye":  ("Ketu",    "#b7b46a"),
}
# Order on the ring, top to bottom. Rahu and Ketu, always opposite,
# close the two ends of the ring beside the river.
RIGHT = ["pearl", "emerald", "ysapph", "hessonite"]
LEFT = ["diamond", "coral", "bsapph", "catseye"]


def defs(theme, uid):
    g = GOLD_ON_INDIGO if theme == "indigo" else GOLD_ON_CREAM
    bg = INDIGO if theme == "indigo" else CREAM
    return f"""<defs>
<linearGradient id="{uid}g" gradientUnits="userSpaceOnUse" x1="200" y1="80" x2="800" y2="940">
<stop offset="0" stop-color="{g[0]}"/><stop offset=".5" stop-color="{g[1]}"/><stop offset="1" stop-color="{g[2]}"/></linearGradient>
<radialGradient id="{uid}bg" cx="500" cy="470" r="620" gradientUnits="userSpaceOnUse">
<stop offset="0" stop-color="{bg[0]}"/><stop offset="1" stop-color="{bg[1]}"/></radialGradient>
</defs>"""


def seat_color(theme):
    """Ground behind a set stone: indigo on both themes so pale stones read."""
    return INDIGO[1] if theme == "indigo" else "#2b2262"


def bg_color(theme):
    return INDIGO[1] if theme == "indigo" else CREAM[1]


def gem(x, y, r, key, gold, theme, bezel=0.32, glint=True, outline=False):
    c = GEMS[key][1]
    out = [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r * (1 + bezel):.1f}" fill="{gold}"/>']
    if outline:  # dark seat so pale stones read against the gold
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r * 1.06:.1f}" fill="{bg_color(theme)}" opacity=".55"/>')
    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{c}"/>')
    if glint:
        out.append(f'<circle cx="{x - r * 0.36:.1f}" cy="{y - r * 0.36:.1f}" r="{r * 0.24:.1f}" fill="#fff" opacity=".75"/>')
    return "".join(out)


def ar_monogram(fname, cx, base, cap_px, overlap, cap_units):
    """'AR' outlines, centred on cx. Returns (path, info) with R tail position."""
    f = font(fname)
    s = cap_px / cap_units
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    wa = gs[cmap[ord("A")]].width
    from fontTools.pens.boundsPen import BoundsPen
    bA = BoundsPen(gs); gs[cmap[ord("A")]].draw(bA)
    bR = BoundsPen(gs); gs[cmap[ord("R")]].draw(bR)
    rx = wa - overlap
    left, right = bA.bounds[0], rx + bR.bounds[2]
    x0 = cx - (left + right) / 2 * s
    dA, _ = glyph_path(fname, "A", x0, base, s)
    dR, _ = glyph_path(fname, "R", x0 + rx * s, base, s)
    return dA + " " + dR, {"s": s, "x0": x0, "rx": x0 + rx * s, "base": base}


def sun_rays(cx, cy, r_in, r_out, n, w, gold, round_caps=True, alt=None):
    out = []
    for i in range(n):
        a = 360 / n * i
        ro = r_out if (alt is None or i % 2 == 0) else alt
        x0, y0 = P(a, r_in, cx, cy)
        x1, y1 = P(a, ro, cx, cy)
        out.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{gold}" stroke-width="{w}" stroke-linecap="{"round" if round_caps else "butt"}"/>')
    return "".join(out)


def pointed_rays(cx, cy, r_in, r_long, r_short, n, half_w, gold):
    """Flame-like pointed rays alternating long and short, as one path."""
    parts = []
    for i in range(n):
        a = 360 / n * i
        ro = r_long if i % 2 == 0 else r_short
        hw = half_w if i % 2 == 0 else half_w * 0.8
        x0, y0 = P(a - hw, r_in, cx, cy)
        x1, y1 = P(a + hw, r_in, cx, cy)
        xt, yt = P(a, ro, cx, cy)
        parts.append(f"M{x0:.1f},{y0:.1f} L{xt:.1f},{yt:.1f} L{x1:.1f},{y1:.1f} Z")
    return f'<path d="{" ".join(parts)}" fill="{gold}"/>'


# ================================================================ OPTION 1
def option1(theme, uid="o1"):
    """Faithful flat: band ring with inner rule and dividers, flame sun,
    chiselled Cinzel AR, ribbon river spreading at the base."""
    G = f"url(#{uid}g)"
    cx, cy = 500, 515
    R_in = 306                      # inner rule
    gap_top, gap_bot = 22, 46       # half-angles of the openings (deg)
    o = [defs(theme, uid)]
    # outer heavy ring
    o.append(f'<path d="{arc(cx, cy, 372, gap_top, 180 - gap_bot)}" fill="none" stroke="{G}" stroke-width="30" stroke-linecap="round"/>')
    o.append(f'<path d="{arc(cx, cy, 372, 180 + gap_bot, 360 - gap_top)}" fill="none" stroke="{G}" stroke-width="30" stroke-linecap="round"/>')
    # inner fine rule
    o.append(f'<path d="{arc(cx, cy, R_in, gap_top + 8, 180 - gap_bot - 6)}" fill="none" stroke="{G}" stroke-width="7" stroke-linecap="round"/>')
    o.append(f'<path d="{arc(cx, cy, R_in, 180 + gap_bot + 6, 360 - gap_top - 8)}" fill="none" stroke="{G}" stroke-width="7" stroke-linecap="round"/>')
    # gems in the channel, dividers between them
    angs = [43, 68, 93, 118]
    rg = (372 - 15 + R_in + 3.5) / 2
    for side, keys in ((1, RIGHT), (-1, LEFT)):
        for a, k in zip(angs, keys):
            x, y = P(side * a, rg, cx, cy)
            o.append(gem(x, y, 15, k, G, theme, bezel=0.4))
        for a in [55.5, 80.5, 105.5]:
            x0, y0 = P(side * a, R_in + 3, cx, cy)
            x1, y1 = P(side * a, 357, cx, cy)
            o.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{G}" stroke-width="6" stroke-linecap="round"/>')
    # sun: flame rays, disc, ruby heart
    sx, sy = cx, cy - 372
    o.append(pointed_rays(sx, sy, 48, 104, 80, 16, 9.5, G))
    o.append(f'<circle cx="{sx}" cy="{sy}" r="56" fill="{G}"/>')
    o.append(f'<circle cx="{sx}" cy="{sy}" r="40" fill="none" stroke="{bg_color(theme)}" stroke-width="4"/>')
    o.append(gem(sx, sy, 19, "ruby", G, theme, bezel=0.0))
    # AR
    d, inf = ar_monogram("Cinzel-700", cx - 14, 604, 246, 70, 700)
    o.append(f'<path d="{d}" fill="{G}"/>')
    # river: the R's tail becomes the river and leaves through the opening
    s = inf["s"]
    T = (inf["rx"] + 786 * s, inf["base"] - 5 * s)
    o.append(f'<path d="{river_path(T, 0.92, w=(10 * s, 40, 1.5), reach=520)}" fill="{G}"/>')
    low = [((cx + 215, cy + 268), (cx + 120, cy + 306), (cx - 10, cy + 304), (cx - 135, cy + 350))]
    o.append(f'<path d="{ribbon(low, smooth_taper(1.5, 17, 1.2, 0.45))}" fill="{G}"/>')
    return "".join(o)


# ================================================================ OPTION 2
def option2(theme, uid="o2"):
    """Minimal monogram: one ring (as the seal), round-ray sun,
    bold AR, a single river swash, nine gem dots."""
    G = f"url(#{uid}g)"
    cx, cy = 500, 515
    Rr = 372
    o = [defs(theme, uid)]
    o.append(f'<path d="{arc(cx, cy, Rr, 24, 138)}" fill="none" stroke="{G}" stroke-width="40" stroke-linecap="round"/>')
    o.append(f'<path d="{arc(cx, cy, Rr, 222, 336)}" fill="none" stroke="{G}" stroke-width="40" stroke-linecap="round"/>')
    # sun, as Seal C: disc and round rays
    sx, sy = cx, cy - Rr
    o.append(sun_rays(sx, sy, 72, 106, 12, 20, G))
    o.append(f'<circle cx="{sx}" cy="{sy}" r="52" fill="{G}"/>')
    o.append(f'<circle cx="{sx}" cy="{sy}" r="22" fill="{GEMS["ruby"][1]}"/>')
    # gem dots on the inside of the ring
    angs = [49, 73, 97, 121]
    for side, keys in ((1, RIGHT), (-1, LEFT)):
        for a, k in zip(angs, keys):
            x, y = P(side * a, Rr, cx, cy)
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="17" fill="{seat_color(theme)}"/>')
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13.5" fill="{GEMS[k][1]}"/>')
    d, inf = ar_monogram("Cinzel-900", cx - 16, 600, 268, 96, 700)
    o.append(f'<path d="{d}" fill="{G}"/>')
    s = inf["s"]
    T = (inf["rx"] + 850 * s, inf["base"] - 5 * s)
    o.append(f'<path d="{river_path(T, 0.95, w=(10 * s, 58, 2.5), reach=500)}" fill="{G}"/>')
    return "".join(o)


# ================================================================ OPTION 3
def option3(theme, uid="o3"):
    """Classical fine-line: temple arch in double engraved lines,
    fine-ray sun, Cormorant AR with an inline, river as three
    parallel engraved currents."""
    G = f"url(#{uid}g)"
    cx = 500
    o = [defs(theme, uid)]
    # arch: straight jambs, round head (a torana)
    top_cy, r1 = 452, 326
    yb = 812
    lw = 12
    for r, w in ((r1, lw), (r1 - 32, 5.5)):
        d = (f"M{cx - r},{yb} L{cx - r},{top_cy} "
             f"A{r},{r} 0 0 1 {cx + r},{top_cy} L{cx + r},{yb}")
        o.append(f'<path d="{d}" fill="none" stroke="{G}" stroke-width="{w}" stroke-linecap="round"/>')
    # plinths at the foot of each jamb
    for sgn in (-1, 1):
        x = cx + sgn * (r1 - 16)
        o.append(f'<rect x="{x - 36:.1f}" y="{yb - 4}" width="72" height="12" rx="3" fill="{G}"/>')
        o.append(f'<rect x="{x - 26:.1f}" y="{yb + 14}" width="52" height="7" rx="3" fill="{G}"/>')
    # gems set between the two lines of the arch
    rm = r1 - 16
    pos = []
    for a in (40, 80):
        pos.append(P(a, rm, cx, top_cy))
    for yy in (548, 644, 740):
        pos.append((cx + rm, yy))
    for side, keys in ((1, RIGHT), (-1, LEFT)):
        for (x, y), k in zip([pos[0], pos[1], pos[3], pos[4]], keys):
            xx = cx + side * (x - cx)
            o.append(f'<circle cx="{xx:.1f}" cy="{y:.1f}" r="21" fill="{seat_color(theme)}"/>')
            o.append(f'<circle cx="{xx:.1f}" cy="{y:.1f}" r="17" fill="none" stroke="{G}" stroke-width="4"/>')
            o.append(f'<circle cx="{xx:.1f}" cy="{y:.1f}" r="11" fill="{GEMS[k][1]}"/>')
    # sun at the apex
    sx, sy = cx, top_cy - r1
    o.append(f'<circle cx="{sx}" cy="{sy}" r="60" fill="{bg_color(theme)}"/>')
    o.append(sun_rays(sx, sy, 50, 104, 24, 6, G, alt=84))
    o.append(f'<circle cx="{sx}" cy="{sy}" r="40" fill="none" stroke="{G}" stroke-width="5"/>')
    o.append(f'<circle cx="{sx}" cy="{sy}" r="18" fill="{GEMS["ruby"][1]}"/>')
    o.append(f'<circle cx="{sx}" cy="{sy}" r="25" fill="none" stroke="{G}" stroke-width="4"/>')
    # AR, engraved: solid letters with an inline cut
    d, inf = ar_monogram("CormorantGaramond-700", cx - 12, 622, 236, 46, 628)
    o.append(f'<path d="{d}" fill="{G}"/>')
    # river: the R's tail runs into engraved water between the jambs
    s = inf["s"]
    T = (inf["rx"] + 702 * s, inf["base"] - 6 * s)
    seg = [(T, (T[0] + 22, T[1] + 4), (T[0] + 30, T[1] + 30), (T[0] - 10, T[1] + 48)),
           ((T[0] - 10, T[1] + 48), (T[0] - 90, T[1] + 80), (cx - 160, yb - 120), (cx - 250, yb - 104))]
    o.append(f'<path d="{ribbon(seg, river_width(4.5, 15, 1))}" fill="{G}"/>')
    o.append(f'<path d="{water_line(cx - 230, cx + 210, yb - 66, 10, 3, 10)}" fill="{G}"/>')
    o.append(f'<path d="{water_line(cx - 165, cx + 145, yb - 26, 9, 2, 8.5)}" fill="{G}"/>')
    return "".join(o)


OPTIONS = {1: option1, 2: option2, 3: option3}
WORD_FONT = {1: ("Cinzel-700", "Cinzel-700"), 2: ("Cinzel-700", "Cinzel-700"),
             3: ("CormorantGaramond-600", "CormorantGaramond-600")}


def svg(body, w, h, extra="", vb=None):
    vb = vb or f"0 0 {w} {h}"
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}">{extra}{body}</svg>\n'


def icon_svg(n, theme):
    body = OPTIONS[n](theme, f"o{n}{theme[0]}")
    bg = f'<rect width="1000" height="1000" fill="url(#o{n}{theme[0]}bg)"/>'
    # background rect must follow defs; defs are the first element of body
    i = body.index("</defs>") + len("</defs>")
    return svg(body[:i] + bg + body[i:], 1000, 1000)


def lockup_svg(n, theme):
    uid = f"o{n}{theme[0]}"
    body = OPTIONS[n](theme, uid)
    i = body.index("</defs>") + len("</defs>")
    G = f"url(#{uid}g)"
    W, H = 1000, 1250
    f1, f2 = WORD_FONT[n]
    big = 100 if n != 3 else 112
    words = text_path(f1, "ASTRO RIVER", 500, 1090, big, tracking=0.06)
    sub = text_path(f2, "VEDIC ASTROLOGY · EST. 2008", 500, 1168, 38 if n != 3 else 43, tracking=0.16)
    bg = f'<rect width="{W}" height="{H}" fill="{bg_color(theme)}"/><rect width="{W}" height="{H}" fill="url(#{uid}bg)"/>'
    text = f'<path d="{words}" fill="{G}"/><path d="{sub}" fill="{G}"/>'
    return svg(body[:i] + bg + '<g transform="translate(0,-10)">' + body[i:] + "</g>" + text, W, H)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for n in OPTIONS:
        d = os.path.join(OUT, f"option-{n}")
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "icon.svg"), "w").write(icon_svg(n, "indigo"))
        open(os.path.join(d, "icon-cream.svg"), "w").write(icon_svg(n, "cream"))
        open(os.path.join(d, "lockup.svg"), "w").write(lockup_svg(n, "indigo"))
        print("wrote option", n)
