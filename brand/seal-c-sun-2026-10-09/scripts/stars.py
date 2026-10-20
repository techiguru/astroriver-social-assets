# Other heads for the seal, to replace the four-point curved sparkle (the shape AI products use).
import math, seal as S

def eight(x, y, R, fill):
    """the pole star (Dhruva): eight straight rays, long and short, and a small centre"""
    pts = []
    for i in range(16):
        a = math.radians(i * 22.5 - 90)
        r = R if i % 4 == 0 else (R * .62 if i % 2 == 0 else R * .2)
        pts.append((x + r * math.cos(a), y + r * math.sin(a)))
    return '<path d="M' + ' L'.join(f'{a:.2f},{b:.2f}' for a, b in pts) + f'Z" fill="{fill}"/>'

def sun(x, y, R, fill):
    """Surya: a disc with twelve short rays"""
    s = f'<circle cx="{x}" cy="{y}" r="{R*.42:.2f}" fill="{fill}"/>'
    for i in range(12):
        a = math.radians(i * 30)
        x1, y1 = x + R * .58 * math.cos(a), y + R * .58 * math.sin(a)
        x2, y2 = x + R * .95 * math.cos(a), y + R * .95 * math.sin(a)
        s += f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{fill}" stroke-width="{R*.11:.2f}" stroke-linecap="round"/>'
    return s

def bindu(x, y, R, fill):
    """the bindu: a point, with one fine circle round it"""
    return (f'<circle cx="{x}" cy="{y}" r="{R*.36:.2f}" fill="{fill}"/>'
            f'<circle cx="{x}" cy="{y}" r="{R*.72:.2f}" fill="none" stroke="{fill}" stroke-width="{R*.08:.2f}"/>')

_SPARK = S.spark
HEADS = {'eight': eight, 'sun': sun, 'bindu': bindu, 'spark': lambda x, y, R, f: _SPARK(x, y, R, f)}

def with_head(fn, head, **kw):
    """swap the star in one of seal.py's drawings"""
    orig = S.spark
    S.spark = lambda x, y, R, fill, thin=.2: HEADS[head](x, y, R, fill)
    try:
        return fn(**kw)
    finally:
        S.spark = orig
