# Astro River post build kit

The scripts that draw every post image in `posts/`. Each script writes HTML, renders it with
Playwright (Chromium) and saves PNGs to `out/` (or `out4/`). Running a script again produces
the same bytes as the published image.

    pip install playwright
    python3 planet_series_rahu.py        # -> out/rahu-*.png

## The brand system (decided 29 Sep 2026)

One frame, one light ground, one dark ground. A series is told apart by its **structure on the
cover**, never by a colour of its own. Do not add a new colour for a new series.

| Series | Ground | Cover signature | Script to copy |
|---|---|---|---|
| Shradh and calendar days | Ivory `#F3EDE2` | A date table; reads like a calendar page | `chaturthi_panchami.py`, `bharani_hindi.py` |
| River Journal teaching | Ivory `#F3EDE2` | The diagram on the cover, RIVER JOURNAL label | `money_houses.py`, `sade_sati_and_bharani.py` |
| Transits | Sand `#EADFCB` | NAKSHATRA TRANSIT / SIGN TRANSIT pill, plus the wheel or planet art | `transit_mars_pushya.py` |
| Planet series (hooks) | Warm ink `#211B12` | Planet or eclipse art, one big question | `planet_series_rahu.py` |
| Products (from 11 Oct) | Ivory | Product art; no new colour | to be made |

- The dark ground is used only for hook posts, so the grid gets one dark tile every three or
  four posts. Lessons stay light because they are read.
- The one dark is the warm ink `#211B12`, the site's own heading colour, as used on the 29 Sep
  Rahu post. Never blue. If the finished emblem's colour is ever to be carried onto posts, that
  is a single decision taken with a test post shown to the founder, not a drift.
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
