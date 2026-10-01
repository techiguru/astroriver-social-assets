# Astro River post build kit

The scripts that draw every post image in `posts/`. Each script writes HTML, renders it with
Playwright (Chromium) and saves PNGs to `out/` (or `out4/`). Running a script again produces
the same bytes as the published image.

    pip install playwright
    python3 planet_series_rahu.py        # -> out/rahu-*.png

## The brand system (decided 29 Sep 2026; planet colours locked 1 Oct 2026)

One frame. Shradh, calendar, teaching and transit posts stay light; a series is told apart by its
**structure on the cover**. The one exception is the planet series: **each planet is posted in its
own colour from the tradition**, softened so the grid stays elegant (founder, 1 Oct 2026).

| Series | Ground | Cover signature | Script to copy |
|---|---|---|---|
| Shradh and calendar days | Ivory `#F3EDE2` | A date table; reads like a calendar page | `chaturthi_panchami.py`, `shashthi.py`, `bharani_hindi.py` |
| River Journal teaching | Ivory `#F3EDE2` | The diagram on the cover, RIVER JOURNAL label | `money_houses.py`, `sade_sati_and_bharani.py` |
| Transits | Sand `#EADFCB` | NAKSHATRA TRANSIT / SIGN TRANSIT pill, plus the wheel or planet art | `transit_mars_pushya.py` |
| Planet series (hooks) | **The planet's own colour** (below) | Planet or eclipse art, one big question | `planet_series_ketu.py` |
| Products (from 11 Oct) | Ivory | Product art; no new colour | to be made |

### The planet palette (locked 1 Oct 2026; values in `planet_palette.py`)

| Planet | Tradition | Tone | Cover ground | Inner slides | Text |
|---|---|---|---|---|---|
| Sun · Surya | copper red | terracotta | `#B4674C` | `#9A543C` | ivory |
| Moon · Chandra | white | moonstone | `#DEDDD8` | same | ink |
| Mars · Mangal | red | red earth | `#9C5048` | same | ivory |
| Mercury · Budh | green | durva sage | `#8E9C7C` | same | ink |
| Jupiter · Guru | yellow | pitambar yellow | `#EBC458` | same | ink |
| Venus · Shukra | white | rose cream | `#EBD9CF` | same | ink |
| Saturn · Shani | black | slate | `#4E4D52` | same | ivory |
| Rahu | blue | dusk indigo | `#4B5675` | same | ivory |
| Ketu | smoke | pale smoke | `#D3CCC4` | same | ink |

- Ketu was first locked as a mid smoke with ivory type; the same day it proved too faint to read and
  the founder chose pale smoke with dark text.
- Founder's rulings: Rahu is blue, Ketu is smoke, Saturn is black. Red need not be blood red and
  black need not be deep black. The earlier "never blue" rule is withdrawn; it was about the old
  dark-blue site look, not about Rahu.
- The cover uses the ground; inner slides, status and X images use the inner tone, one step
  deeper where small text needs it (ivory at 4.5:1 or better).
- The saffron river line `#D77B09`, fonts, tags and footer are the same on every planet. Only the
  planet series is coloured, about one tile in three or four.
- The 29 Sep Rahu post (warm ink `#211B12`) stays as published.
- Do not change a palette value without the founder's say. `planet_colours_v3.py` drew the
  approved sheet and sample covers.
- Hindi posts keep their series' look with the हिंदी label.
- Sand is the light ground's warm shade, not a third colour.

Ink `#211B12`, saffron `#D77B09` / `#A8590A`, muted `#6B5B4B`. Headings Playfair Display,
body Lora, labels Inter; Hindi in Noto Serif / Sans Devanagari (all in `fonts/`, OFL).

## Rules that came from review

- Lay content out as one flowing block with even gaps (flex column), centred in the frame.
  Pinning pieces at fixed heights leaves big gaps and reads as "stretched".
- No single word alone on the last line of a heading or line: use `<br>` or `&nbsp;`.
- Every image carries: the faint slanted astroriver.com across the middle, a small top-right
  tag, a tag on the saffron river line, and the footer. On the dark look the slanted mark is
  at .07 opacity; on ivory .045.
- Carousels: one river line runs unbroken across all slides (the `Y` list).
- Teaching posts name the ayanamsa on the image: Lahiri sidereal. Dates are computed with
  Swiss Ephemeris (Lahiri), never recalled.
- Hindi is a separate image with the हिंदी label, never mixed with English on one image.
- Gentle copy: no "death" or "died" on graphics.
- Sizes: feed 1080x1350, status/Pinterest 1080x1920, X 1600x900.
