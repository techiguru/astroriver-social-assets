# Type set as outlines, so the logo files need no fonts installed. Playfair Display for the name, Inter for the line.
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FD = '/home/user/astroriver-social-assets/build/fonts/'
_cache = {}
def font(name, axes):
    key = (name, tuple(sorted(axes.items())))
    if key not in _cache:
        _cache[key] = instancer.instantiateVariableFont(TTFont(FD + name), axes)
    return _cache[key]
PLAYFAIR = lambda w=600: font('PlayfairDisplay[wght].ttf', {'wght': w})
INTER = lambda w=500: font('Inter[opsz,wght].ttf', {'wght': w, 'opsz': 14})

def kern_table(f):
    """pair kerning from the GPOS PairPos format 1 subtables (enough for capitals)"""
    pairs = {}
    if 'GPOS' not in f: return pairs
    for lookup in f['GPOS'].table.LookupList.Lookup:
        if lookup.LookupType not in (2, 9): continue
        for st in lookup.SubTable:
            if lookup.LookupType == 9: st = st.ExtSubTable
            if st.Format == 1:
                for i, g1 in enumerate(st.Coverage.glyphs):
                    for pvr in st.PairSet[i].PairValueRecord:
                        v = pvr.Value1.XAdvance if pvr.Value1 and hasattr(pvr.Value1, 'XAdvance') else 0
                        if v: pairs[(g1, pvr.SecondGlyph)] = v
            elif st.Format == 2:
                c1 = st.ClassDef1.classDefs; c2 = st.ClassDef2.classDefs
                for g1 in st.Coverage.glyphs:
                    k1 = c1.get(g1, 0)
                    rec = st.Class1Record[k1]
                    for g2, k2 in list(c2.items()):
                        v = rec.Class2Record[k2].Value1
                        v = getattr(v, 'XAdvance', 0) if v else 0
                        if v: pairs.setdefault((g1, g2), v)
    return pairs
_kern = {}

def text(s, f, size, x=0, y=0, tracking=0.0, fill='#000', anchor='start'):
    """returns (svg path element, width). y is the baseline. tracking in em."""
    gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm; sc = size / upm
    kid = id(f)
    if kid not in _kern: _kern[kid] = kern_table(f)
    kern = _kern[kid]
    names = [cmap[ord(c)] for c in s]
    adv = []
    for i, n in enumerate(names):
        a = gs[n].width
        if i + 1 < len(names): a += kern.get((n, names[i + 1]), 0)
        adv.append(a)
    width = (sum(adv) + tracking * upm * (len(names) - 1)) * sc
    x0 = x - width / 2 if anchor == 'middle' else x - width if anchor == 'end' else x
    d = ''; pen_x = 0
    for n, a in zip(names, adv):
        pen = SVGPathPen(gs, ntos=lambda v: ('%.2f' % v).rstrip('0').rstrip('.'))
        gs[n].draw(TransformPen(pen, (sc, 0, 0, -sc, x0 + pen_x * sc, y)))
        d += pen.getCommands()
        pen_x += a + tracking * upm
    return f'<path fill="{fill}" d="{d}"/>', width
