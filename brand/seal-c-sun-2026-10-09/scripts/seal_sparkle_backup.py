# Seal C, as clean standalone SVG. Everything is drawn round the ring's centre (200,200).
import math

DARK = dict(foil=('#F2D99A', '#D4AF5A', '#B88A3A'), river=('#F2D99A', '#9A7BE0'))   # for night backgrounds
LIGHT = dict(foil=('#C79A3A', '#A97A24', '#86601A'), river=('#B5832A', '#6D28D9'))  # for ivory and white
NIGHT, NIGHT_GLOW = '#0F092A', '#23185C'

def mix(a, b, t):
    a = [int(a[i:i+2], 16) for i in (1, 3, 5)]; b = [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return '#' + ''.join(f'{round(x + (y - x) * t):02X}' for x, y in zip(a, b))

def bez(P, u):
    (a, b), (c, d), (e, f), (g, h) = P
    m = lambda p0, p1, p2, p3: (1-u)**3*p0 + 3*(1-u)**2*u*p1 + 3*(1-u)*u**2*p2 + u**3*p3
    return m(a, c, e, g), m(b, d, f, h)

def along(P, n, start=0.05):
    """n points spaced evenly along the curve's length"""
    pts = [bez(P, i / 800) for i in range(801)]; acc = [0]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]): acc.append(acc[-1] + math.hypot(x2 - x1, y2 - y1))
    out = []
    for i in range(n):
        t = i / (n - 1); L = acc[-1] * (start + (1 - start) * t)
        j = min(range(801), key=lambda k: abs(acc[k] - L)); out.append((pts[j], t))
    return out

def spark(x, y, R, fill, thin=.2):
    r = R * thin
    return (f'<path d="M{x:g},{y-R:g} C{x+r*.2:.2f},{y-r:.2f} {x+r:.2f},{y-r*.2:.2f} {x+R:g},{y:g} C{x+r:.2f},{y+r*.2:.2f} {x+r*.2:.2f},{y+r:.2f} {x:g},{y+R:g} '
            f'C{x-r*.2:.2f},{y+r:.2f} {x-r:.2f},{y+r*.2:.2f} {x-R:g},{y:g} C{x-r:.2f},{y-r*.2:.2f} {x-r*.2:.2f},{y-r:.2f} {x:g},{y-R:g}Z" fill="{fill}"/>')

def ring(r, w, gap_top, gap_bot, col, op=1):
    p = lambda a: (200 + r * math.cos(math.radians(a)), 200 + r * math.sin(math.radians(a)))
    out = ''; opa = '' if op == 1 else f' opacity="{op}"'
    for a0, a1 in [(-90 + gap_top, 90 - gap_bot), (90 + gap_bot, 270 - gap_top)]:
        (x0, y0), (x1, y1) = p(a0), p(a1)
        out += (f'<path d="M{x0:.2f},{y0:.2f} A{r},{r} 0 0 1 {x1:.2f},{y1:.2f}" fill="none" stroke="{col}" stroke-width="{w}" '
                f'stroke-linecap="round"{opa}/>')
    return out

def paint(scheme, one, uid):
    """returns (defs, ring/star fill, river colour function)"""
    if one:
        return '', one, (lambda t: one)
    f = scheme['foil']; r = scheme['river']
    defs = (f'<linearGradient id="g{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{f[0]}"/>'
            f'<stop offset=".55" stop-color="{f[1]}"/><stop offset="1" stop-color="{f[2]}"/></linearGradient>')
    return defs, f'url(#g{uid})', (lambda t: mix(r[0], r[1], t))

# the three drawings: full (large uses), small (under about 64 px), icon (16-48 px, tab and app icons)
def full(scheme=DARK, one=None, uid='f'):
    defs, g, rc = paint(scheme, one, uid)
    s = ring(170, 5, 15, 9, g) + ring(160, 1.6, 17, 10, g, .75)
    for (x, y), t in along([(200, 92), (322, 150), (78, 262), (200, 372)], 11):
        s += f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{4 + 7.5 * t:.2f}" fill="{rc(t)}"/>'
    return defs, s + spark(200, 30, 40, g)

def small(scheme=DARK, one=None, uid='s'):
    defs, g, rc = paint(scheme, one, uid)
    s = ring(164, 16, 19, 13, g)
    for (x, y), t in along([(200, 100), (330, 160), (70, 260), (200, 368)], 7, .06):
        s += f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{9 + 9 * t:.2f}" fill="{rc(t)}"/>'
    return defs, s + spark(200, 32, 50, g, .26)

def icon(scheme=DARK, one=None, uid='i'):
    defs, g, rc = paint(scheme, one, uid)
    s = ring(150, 18, 20, 14, g)
    for (x, y), t in along([(200, 110), (322, 165), (78, 255), (200, 350)], 6, .06):
        s += f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{11 + 9 * t:.2f}" fill="{rc(t)}"/>'
    return defs, s + spark(200, 50, 44, g, .28)

# boxes that hold each drawing with a little room, centred on the ring where that matters
BOX = {'full': (20, -16, 360, 408), 'small': (20, -26, 360, 420), 'icon': (-10, -10, 420, 420)}

def svg_doc(defs, body, box, w=None, h=None, extra=''):
    x, y, bw, bh = box
    size = f' width="{w}" height="{h}"' if w else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:g} {y:g} {bw:g} {bh:g}"{size}>'
            + (f'<defs>{defs}</defs>' if defs else '') + extra + body + '</svg>\n')
