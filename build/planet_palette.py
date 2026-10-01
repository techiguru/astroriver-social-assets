# THE PLANET SERIES PALETTE, LOCKED 1 Oct 2026 (founder: "Pallette approved. Lock it").
# Each planet is posted in its own colour from the tradition, softened so the grid stays elegant
# (founder: Rahu is blue, Ketu is smoke, Saturn is black; red need not be blood red, black need not be
# deep black). Do not change a value here without the founder's say.
#
#   ground  the cover colour (the swatch on the approved sheet)
#   deep    the inner slides, status and X images: one step deeper where small text needs it
#           (ivory text at 4.5:1 or better); the same as ground where it already reads well
#   text    the type colour on that ground
#   accent  eyebrow, italic word, ring text, crescent
# The saffron river line (#D77B09), the fonts, the tags and the footer are the same on every planet.
# Only the planet series is coloured; shradh/calendar posts stay ivory, transits stay sand.
# 1 Oct 2026, same day: Ketu changed from mid smoke (#8A847E, ivory type) to pale smoke with ink type
# (founder: "too smokey, not readable" -> "Pale smoke dark text").

IVORY, INK = '#F3EDE2', '#211B12'

PALETTE = {
    #  key        name       Sanskrit   tradition   tone              ground     deep       text   accent
    'sun':     ('Sun',     'Surya',   'copper red', 'terracotta',      '#B4674C', '#9A543C', IVORY, '#FBE3C4'),
    'moon':    ('Moon',    'Chandra', 'white',      'moonstone',       '#DEDDD8', '#DEDDD8', INK,   '#A8590A'),
    'mars':    ('Mars',    'Mangal',  'red',        'red earth',       '#9C5048', '#9C5048', IVORY, '#F7CFA0'),
    'mercury': ('Mercury', 'Budh',    'green',      'durva sage',      '#8E9C7C', '#8E9C7C', INK,   '#3E4A2E'),
    'jupiter': ('Jupiter', 'Guru',    'yellow',     'pitambar yellow', '#EBC458', '#EBC458', INK,   '#6A4508'),
    'venus':   ('Venus',   'Shukra',  'white',      'rose cream',      '#EBD9CF', '#EBD9CF', INK,   '#A8590A'),
    'saturn':  ('Saturn',  'Shani',   'black',      'slate',           '#4E4D52', '#4E4D52', IVORY, '#E9A85A'),
    'rahu':    ('Rahu',    'Rahu',    'blue',       'dusk indigo',     '#4B5675', '#4B5675', IVORY, '#F0B061'),
    'ketu':    ('Ketu',    'Ketu',    'smoke',      'pale smoke',      '#D3CCC4', '#D3CCC4', INK,   '#9A520B'),
}
