# Navratri 2026: "माँ के 9 रूप" art kit (founder 9 Oct: "Wouldn't you even try?" after an AI-video reference). No AI
# pictures here: each form is shown through her own setting and symbols, seen through a window from a dark room with a
# diya. Scenes are SVG so they can move (sky drift, glow, particles) in the Reel. This file draws; the Reel uses it.
import math, random
W, H = 1080, 1920
WX, WY, WW, WH = 110, 330, 860, 1060          # the window
def lin(id_, stops, x2=0, y2=1):
    s = ''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="{x2}" y2="{y2}">{s}</linearGradient>'
def rad(id_, stops, cx=.5, cy=.5, r=.5):
    s = ''.join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{a}"/>' for o, c, a in stops)
    return f'<radialGradient id="{id_}" cx="{cx}" cy="{cy}" r="{r}">{s}</radialGradient>'
def ridge(seed, y, amp, col, x0=WX - 40, x1=WX + WW + 40, n=14, snow=None):
    random.seed(seed); pts = [(x0, WY + WH + 50)]
    xs = [x0 + i * (x1 - x0) / n for i in range(n + 1)]
    peaks = []
    for i, x in enumerate(xs):
        yy = y - (amp * random.uniform(.3, 1) if i % 2 else amp * random.uniform(0, .35))
        pts.append((x, yy)); peaks.append((x, yy))
    pts.append((x1, WY + WH + 50))
    out = f'<path d="M{" L".join(f"{a:.0f},{b:.0f}" for a, b in pts)} Z" fill="{col}"/>'
    if snow:
        for i in range(1, len(peaks) - 1):
            x, yy = peaks[i]
            if yy < peaks[i - 1][1] and yy < peaks[i + 1][1]:
                lx = x - (x - peaks[i - 1][0]) * .28; ly = yy + (peaks[i - 1][1] - yy) * .28
                rx = x + (peaks[i + 1][0] - x) * .28; ry = yy + (peaks[i + 1][1] - yy) * .28
                out += f'<path d="M{x:.0f},{yy:.0f} L{rx:.0f},{ry:.0f} L{(x+rx)/2:.0f},{ry-10:.0f} L{x:.0f},{ry+6:.0f} L{(x+lx)/2:.0f},{ly-6:.0f} L{lx:.0f},{ly:.0f} Z" fill="{snow}"/>'
    return out
def trishul(cx, cy, s, col, glow=True):
    p = (f'M{cx},{cy-150*s} L{cx+16*s},{cy-100*s} L{cx+7*s},{cy-100*s} L{cx+7*s},{cy-40*s} '
         f'C{cx+40*s},{cy-50*s} {cx+62*s},{cy-80*s} {cx+66*s},{cy-130*s} L{cx+84*s},{cy-118*s} '
         f'C{cx+76*s},{cy-50*s} {cx+44*s},{cy-14*s} {cx+7*s},{cy-10*s} L{cx+7*s},{cy+190*s} L{cx-7*s},{cy+190*s} L{cx-7*s},{cy-10*s} '
         f'C{cx-44*s},{cy-14*s} {cx-76*s},{cy-50*s} {cx-84*s},{cy-118*s} L{cx-66*s},{cy-130*s} '
         f'C{cx-62*s},{cy-80*s} {cx-40*s},{cy-50*s} {cx-7*s},{cy-40*s} L{cx-7*s},{cy-100*s} L{cx-16*s},{cy-100*s} Z')
    g = f'<path d="{p}" fill="{col}" filter="url(#soft)" opacity=".7"/>' if glow else ''
    return g + f'<path d="{p}" fill="{col}"/><rect x="{cx-22*s}" y="{cy+10*s}" width="{44*s}" height="{10*s}" rx="{4*s}" fill="{col}"/>'
def lotus(cx, cy, s, c1, c2):
    out = ''
    for ang, l, w, c in [(-62, 92, 30, c2), (62, 92, 30, c2), (-34, 110, 34, c1), (34, 110, 34, c1), (0, 124, 38, c1)]:
        out += f'<ellipse cx="{cx}" cy="{cy-l*s/2}" rx="{w*s}" ry="{l*s/2}" fill="{c}" transform="rotate({ang} {cx} {cy})" opacity=".95"/>'
    return out + f'<ellipse cx="{cx}" cy="{cy+6*s}" rx="{70*s}" ry="{12*s}" fill="{c2}" opacity=".8"/>'
def crescent(cx, cy, r, col, bg):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/><circle cx="{cx+r*.42}" cy="{cy-r*.18}" r="{r*.9}" fill="{bg}"/>'
def stars(seed, n, col='#FFF6EA', y1=None):
    random.seed(seed); y1 = y1 or WY + WH * .55
    return ''.join(f'<circle cx="{random.uniform(WX, WX+WW):.0f}" cy="{random.uniform(WY, y1):.0f}" r="{random.choice([1.2,1.8,2.4])}" fill="{col}" opacity="{random.choice([.4,.7,1])}"/>' for _ in range(n))
def window_frame(inner, defs=''):
    """the room: dark walls, the window with its frame and glass sheen, a sill, a diya, and someone seen from behind"""
    clip = f'<clipPath id="win"><rect x="{WX}" y="{WY}" width="{WW}" height="{WH}" rx="28"/></clipPath>'
    return (f'<defs>{clip}<filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>'
            f'<filter id="soft2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>'
            + rad('room', [(0, '#3A2A20', 1), (.55, '#1A1310', 1), (1, '#0B0807', 1)], .5, .45, .8) + lin('sheen', [(0, '#FFFFFF'), (1, '#FFFFFF')], 1, 1) + defs + '</defs>'
            f'<rect width="{W}" height="{H}" fill="url(#room)"/>'
            f'<g clip-path="url(#win)">{inner}</g>'
            f'<rect x="{WX}" y="{WY}" width="{WW}" height="{WH}" rx="28" fill="none" stroke="#5A4535" stroke-width="22"/>'
            f'<rect x="{WX}" y="{WY}" width="{WW}" height="{WH}" rx="28" fill="none" stroke="#8A6C52" stroke-width="3"/>'
            f'<path d="M{WX+40},{WY+30} L{WX+250},{WY+30} L{WX+90},{WY+WH-40} L{WX+40},{WY+WH-40} Z" fill="#FFFFFF" opacity=".035"/>'
            f'<rect x="{WX-40}" y="{WY+WH+8}" width="{WW+80}" height="30" rx="8" fill="#4A382B"/>')
def person():
    """someone seen from behind, head and shoulders, lit from the window (no face)"""
    return ('<g transform="translate(-140 250)"><path d="M170,1920 C180,1700 250,1610 360,1585 C330,1560 315,1520 315,1470 C315,1395 370,1345 440,1345 '
            'C512,1345 565,1398 565,1470 C565,1522 548,1560 518,1585 C630,1612 700,1700 712,1920 Z" fill="#0A0706"/>'
            '<path d="M440,1345 C512,1345 565,1398 565,1470" fill="none" stroke="#C9874E" stroke-opacity=".35" stroke-width="5"/>'
            '<path d="M518,1585 C630,1612 700,1700 712,1920" fill="none" stroke="#C9874E" stroke-opacity=".25" stroke-width="5"/></g>')

# ---- the nine scenes: (key, Hindi, English, sky stops, art) ----
def shailaputri():
    d = lin('sk1', [(0, '#2B3B6B'), (.45, '#C77E8E'), (.75, '#F2B07A'), (1, '#FCE2B8')])
    a = (f'<rect x="{WX}" y="{WY}" width="{WW}" height="{WH}" fill="url(#sk1)"/>'
         f'<circle cx="540" cy="{WY+700}" r="120" fill="#FFE7B8" opacity=".9" filter="url(#soft)"/><circle cx="540" cy="{WY+700}" r="78" fill="#FFF3D6"/>'
         + crescent(760, WY+170, 34, '#FFF6EA', '#3A4673')
         + ridge(3, WY+760, 300, '#8E7C9C', snow='#F4ECF4') + ridge(5, WY+860, 220, '#5F4E6E', snow='#E4D8E8') + ridge(9, WY+960, 120, '#3B2E45')
         + trishul(540, WY+420, 1.15, '#FFE9C4'))
    return d, a
def katyayani():
    d = lin('sk6', [(0, '#3A0B0B'), (.4, '#A12A1C'), (.75, '#E0582A'), (1, '#F59A3E')])
    sword = (f'<path d="M540,{WY+120} C560,{WY+260} 566,{WY+420} 556,{WY+600} L524,{WY+600} C514,{WY+420} 520,{WY+260} 540,{WY+120} Z" fill="#FFE7C2"/>'
             f'<rect x="470" y="{WY+600}" width="140" height="22" rx="8" fill="#F2B544"/><rect x="528" y="{WY+622}" width="24" height="90" rx="6" fill="#F2B544"/>'
             f'<circle cx="540" cy="{WY+722}" r="16" fill="#F2B544"/>')
    a = (f'<rect x="{WX}" y="{WY}" width="{WW}" height="{WH}" fill="url(#sk6)"/>'
         f'<circle cx="760" cy="{WY+300}" r="70" fill="#FFD27A" filter="url(#soft)"/><circle cx="760" cy="{WY+300}" r="46" fill="#FFE6A8"/>'
         f'<g filter="url(#soft)" opacity=".8">{sword}</g>{sword}'
         + ridge(21, WY+880, 160, '#5A1A12') + ridge(23, WY+960, 90, '#2A0B08')
         + ''.join(f'<circle cx="{random.uniform(WX,WX+WW):.0f}" cy="{random.uniform(WY+600,WY+WH):.0f}" r="{random.choice([2,3,4])}" fill="#FFB347" opacity=".8"/>' for _ in range(40)))
    return d, a
def kalaratri():
    d = lin('sk7', [(0, '#05060C'), (.6, '#141B2E'), (1, '#2A2238')])
    bolt = lambda x, s: f'<path d="M{x},{WY} L{x-30*s},{WY+260*s} L{x+10*s},{WY+250*s} L{x-40*s},{WY+560*s} L{x+50*s},{WY+220*s} L{x+5*s},{WY+230*s} L{x+40*s},{WY} Z" fill="#E8EEFF"/>'
    a = (f'<rect x="{WX}" y="{WY}" width="{WW}" height="{WH}" fill="url(#sk7)"/>'
         + ''.join(f'<ellipse cx="{x}" cy="{WY+y}" rx="{rx}" ry="{ry}" fill="#242C44" opacity=".9"/>' for x, y, rx, ry in [(260,110,260,90),(700,90,300,100),(500,190,340,80)])
         + f'<g filter="url(#soft)" opacity=".9">{bolt(760,1)}</g>{bolt(760,1)}<g opacity=".7">{bolt(300,.7)}</g>'
         + ridge(31, WY+930, 140, '#0B0D16')
         + ''.join(f'<line x1="{x}" y1="{WY+y}" x2="{x-14}" y2="{WY+y+46}" stroke="#9FB0D8" stroke-width="2" opacity=".35"/>' for x, y in [(random.uniform(WX,WX+WW), random.uniform(0,WH)) for _ in range(90)])
         + f'<path d="M540,{WY+560} C556,{WY+640} 560,{WY+740} 552,{WY+840} L528,{WY+840} C520,{WY+740} 524,{WY+640} 540,{WY+560} Z" fill="#C9D3F0" opacity=".9"/>')
    return d, a
SCENES = {'shailaputri': ('माँ शैलपुत्री', 'Maa Shailaputri', 'Daughter of the mountain', shailaputri),
          'katyayani': ('माँ कात्यायनी', 'Maa Katyayani', 'The warrior', katyayani),
          'kalaratri': ('माँ कालरात्रि', 'Maa Kalaratri', 'The dark night', kalaratri)}
