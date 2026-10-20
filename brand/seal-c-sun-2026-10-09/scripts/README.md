# Seal C, sun version: the scripts that built the kit (9 Oct 2026)

These scripts drew the Seal C sun logo and built `AstroRiver-SealC-SUN-kit.zip` (one folder up).
Checked on 20 Oct 2026: run again, they give back all 14 drawings (SVG) in the kit exactly, byte for byte.

## The files

| File | What it does |
|---|---|
| `seal.py` | Draws the seal: the ring, the Sun (Surya) at the top, the river of lights running down. Three drawings: `full` (the seal), `small` (bolder, for anything under about 64 px) and `icon` (the tab icon). Colours for dark and light backgrounds. |
| `textpath.py` | Turns the words (ASTRO RIVER, INSTITUTE · EST. 2008, ...) into outlines, so the logo files need no fonts. Uses Playfair Display and Inter. |
| `build_kit.py` | Makes the kit folder: every logo as SVG and PNG, the icons, the social pictures and the post-style previews. |
| `sheet.py` | Makes the three-page brand sheet PDF from the kit folder. |
| `seal_sparkle_backup.py` | The first version, with a four-point sparkle at the top. **Retired on 9 Oct** because that sparkle is the shape AI products use. Kept only as a record. Do not build from it. |
| `stars.py`, `compare.py` | The four heads compared on 9 Oct: sparkle, pole star, sun, bindu. `compare.py` makes `star-options.png`. The sun was picked. |

## How to run

Needs Python 3 with Pillow, fontTools and Playwright (Chromium). Run from the folder holding these scripts.

1. `python3 build_kit.py` makes `./AstroRiver-SealC-brand-kit`.
2. `python3 sheet.py` adds `AstroRiver-brand-sheet-SealC.pdf` to it.
3. Make `site/` (plain copies, already named as the website wants them):
   ```
   cd AstroRiver-SealC-brand-kit && mkdir -p site
   cp icons/favicon.ico icons/favicon.svg icons/apple-touch-icon.png icons/pwa-192x192.png icons/pwa-512x512.png icons/pwa-maskable-512x512.png site/
   cp icons/favicon-32.png site/favicon.png
   cp logo/astro-river-seal-small-on-light.svg site/astro-river-seal.svg
   cp logo/astro-river-seal-on-dark.svg site/astro-river-seal-footer.svg
   ```
4. `README.txt` and `TECH-NOTE.md` were written by hand. Take them from the zip.
5. Zip it (the sun kit leaves out `card/`):
   ```
   zip -q -X -r ../AstroRiver-SealC-SUN-kit.zip logo icons site social preview AstroRiver-brand-sheet-SealC.pdf README.txt TECH-NOTE.md
   ```

## Change these paths first

- `build_kit.py` line 9, `SP = ...`, points to the working folder of the 9 Oct session, which no longer exists. It is used only
  at the end, to copy in pictures made earlier: the X banner (`social/x-banner-1500x500.jpg`), the four website mockups in
  `preview/`, and the visiting card (`card/`). The banner and mockups are in the zip; take them from there. Remove the
  `card/` copy, or point it at the visiting card files.
- `build_kit.py` (line 81), `sheet.py` (line 4) and `textpath.py` (line 6) read the fonts from
  `/home/user/astroriver-social-assets/build/fonts/`. That is `build/fonts/` in this repo; change it to where you cloned it.

The scripts are kept exactly as they ran on 9 Oct, which is why the paths are not fixed.

## Good to know

- The SVGs rebuild exactly. PNGs, the PDF and the zip can differ by a few bytes on another machine (browser rendering,
  file times inside the zip). The committed zip is the master copy; rebuild only to make a change.
- Page 3 of the brand sheet still says the crest is retired. On 20 Oct the founder decided the crest stays for large
  places. Change that text in `sheet.py` when the brand sheet is next updated.
- The sun version has not yet been explicitly confirmed as final, and the logo is still on hold for posts.
