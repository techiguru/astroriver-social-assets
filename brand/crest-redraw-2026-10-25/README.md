# Crest redraw — three options (25 Oct 2026)

These are options to choose from. Nothing has been replaced anywhere.

Each redraw keeps the ring, the sun at the top, the "AR" monogram and the river flowing from the R.
They all use flat gold on deep indigo, the same family as the site's Seal C.
The Western planet glyphs are gone. In their place are the nine Navaratna gems, one for each graha.

**Start with `compare.png`.** It shows today's crest and the three options, large and at 48 / 64 / 128 px.

## Files per option (`option-1/`, `option-2/`, `option-3/`)

| File | What it is |
|---|---|
| `icon.svg`, `icon-1024.png` | Emblem only, no words, on deep indigo. For WhatsApp, app and profile icons. Built for a circle crop. |
| `icon-cream.svg`, `icon-cream-1024.png` | The same emblem on cream, with darker gold. |
| `lockup.svg`, `lockup.png` | Emblem with "ASTRO RIVER" and "VEDIC ASTROLOGY · EST. 2008". |
| `small-test.png` | The icon in circles at 48, 64 and 128 px at true pixel size, on light and dark chat lists, plus 48 px enlarged ×4. |

The SVGs are pure vector: the letters are outlines, so no font is needed.

## The three directions

**1 · Faithful flat.** This is closest to today's crest.
- It keeps the broad ring with an inner rule and dividers, a flame-ray sun, the chiselled Cinzel "AR" and a river with two currents spreading out at the base. The gems sit in gold bezels inside the ring channel.
- At 48 px it reads as ring + sun + AR; the gems and dividers turn into texture. It feels the most like today's crest.

**2 · Minimal monogram.** This is the app-icon version.
- It has one heavy ring, the round-ray sun of Seal C, a heavy Cinzel "AR" and one bold river swash leaving through the opening. The gems are set straight into the ring.
- It is the clearest of the three at 48 px and the closest sibling to Seal C.

**3 · Classical fine-line.** This is the engraved temple arch.
- A torana-style arch in double engraved lines stands on plinths. It has a fine-ray sun at the apex, a Cormorant "AR", and the R's tail runs into engraved water between the pillars. The gems are set into the arch.
- It is the most ornamental and premium-feeling of the three, and the most delicate at 48 px. The AR still reads there, but the fine lines soften. It is best in print and at larger sizes.

## The nine gems (Navaratna)

The ruby (Surya) sits at the heart of the sun. The other eight sit on the ring, listed top to bottom.

| Right side | Left side |
|---|---|
| Pearl — Chandra | Diamond — Shukra |
| Emerald — Budh | Red coral — Mangal |
| Yellow sapphire — Guru | Blue sapphire — Shani |
| Hessonite — Rahu | Cat's eye — Ketu |

Rahu and Ketu are always opposite each other, so they close the two ends of the ring on either side of the river.

## Colours

- Indigo ground: radial `#231a5c` to `#140f38`.
- Gold on indigo: `#ecd08a` → `#d2a650` → `#b9893a`.
- Cream ground: `#fbf5e7` to `#f1e6cc`.
- Gold on cream: `#b8893a` → `#9a6f24` → `#7a5617`.

## Rebuilding

`src/build.py` writes every SVG from code. `src/render.js` renders the PNGs and `compare.png` with Playwright/Chromium.

```sh
# fonts (SIL Open Font Licence): Cinzel, Cormorant Garamond from github.com/google/fonts (ofl/)
# make static instances Cinzel-700/-900.ttf and CormorantGaramond-600/-700.ttf
#   with fontTools.varLib.instancer, put them in FONT_DIR, then:
python3 src/build.py FONT_DIR .
node src/render.js .
```
