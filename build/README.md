# Astro River post build kit

The scripts that draw every post image in `posts/`. Each script writes HTML, renders it with
Playwright (Chromium) and saves PNGs to `out/` (or `out4/`). Running a script again produces
the same bytes as the published image.

    pip install playwright
    python3 planet_series_rahu.py        # -> out/rahu-*.png

## The three looks

| Look | Ground | Used for | Script to copy |
|---|---|---|---|
| Ivory "dress" | `#F3EDE2` | Pitru Paksha and calendar days, teaching posts | `sade_sati_and_bharani.py`, `bharani_hindi.py`, `pitru_paksha_hindi.py` |
| Sand "uniform" | `#EADFCB` | Transits, with a NAKSHATRA TRANSIT / SIGN TRANSIT pill above the headline | `transit_mars_pushya.py` |
| Dark planet series | `#211B12` (warm ink, never blue) | The planet series (Rahu first), eclipse art with a ring of astroriver.com | `planet_series_rahu.py` |

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
