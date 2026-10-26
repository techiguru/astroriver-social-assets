# Handover: Crest Redraw 1 → Home Design 2 (26 Oct 2026)

You are **Home Design 2**, a design worker for Astro River (Vedic astrology, est. 2008).
- The founder may talk to you directly in your chat; he decides on taste.
- Your chief of staff is **KRISHNA 10**. When it messages you with its session id, report to it with `send_message` and send it a short summary of this note.
- Work in pictures only: HTML rendered to PNG/JPG with Playwright. Do not write site code unless asked.

## Rules (binding)

**Git:**
- Commit author `Astro River <noreply@astroriver.com>`.
- No co-author trailers. No AI vendor or model names in files or commit messages.
- Push only to branch `ccr-c9d9af03-66j7k7` of techiguru/astroriver-social-assets. Pull before push and merge if needed. No force, amend, rebase or reset.
- Work in your own folders under `brand/`, and don't edit other people's files.

**Founder's rules for the home page:**
- The founder's name appears nowhere on it.
- Consultation is "our senior Vedic astrologer".
- The AI astrologers Vedansh and Tara are labelled AI, with no honorifics. Never say "real" in contrast with AI.
- Inform first, then sell.
- No line art: only paintings and photographs (made in Canva or Adobe), no Western glyphs, no grids of plain boxes.

**Data and claims:**
- Real data only. Panchang comes from astroriver.com/panchang (New Delhi, Lahiri).
- No made-up figures, counts or promised outcomes. Never "little".
- Prices: Ask a question ~~₹399~~ ₹99 for the first question, one follow-up included. Show no other prices unless they are confirmed.
- Anything not live is marked "opening soon".

## Where things stand

**1. Three directions** (`brand/home-from-scratch-2026-10-26/`, compare.png): A Temple morning, B The Almanac, C The App. The founder's view:
- B is clean, beautiful and welcoming, but it's an info screen, not an app.
- C was too dark, heavy and crowded. All its dark pictures and "everything is a click" made it boring.
- Dharmayana (white, well spaced) is practical but boring too. Aim for the sweet spot between them.

**2. Combined design** (`brand/home-combined-2026-10-26/`, overview.png). This is the current proposal, awaiting his review.
- B's almanac on top, C's app parts below, in one long scroll. The tab bar is always visible.
- The page is bright, with a dark "night almanac" mode, meant to switch by toggle or from sunset to sunrise.
- There are things to do on the page itself: mantra player, sign picker, verse.
- It shows everything Astro River has or will have: ePooja, mantras, Vedic texts, learning, Journal, free tools, pujas, shop categories (Alchemies), Ask, AI astrologers, consultation, Inscriptions, the founder papers by title only.
- A becomes the ePooja page.
- The README there lists sections, data and pictures.

**3. Open questions (founder):**
- Mantra audio and the ePooja sankalpa are undecided. He wants the sankalpa generated instantly from name, gotra and other details, but costs are unknown. He may start with a general sankalpa, and asked whether ElevenLabs or Claude could do it ("we'll discuss").
- The current pictures show a general sankalpa built from the panchang, with optional name and gotra fields.

**4. The crest** (`brand/crest-redraw-2026-10-25/`, compare.png) is still waiting for his pick. The home mockups use the current Seal C icon.

## How to rebuild or iterate

1. **Sources:**
   - Combined design: `brand/home-combined-2026-10-26/src/` (`home.html`, `epooja.html`, `theme.css`, `shared.js`, `render.js`, `overview.html`). Use `?v=phone|desktop&theme=light|dark`, plus `&full=1` for full-length captures.
   - Older directions: `brand/home-from-scratch-2026-10-26/src/`.
2. **Images:** make an `img/` folder next to the HTML containing both `brand/home-combined-2026-10-26/src/img/*` and `brand/home-from-scratch-2026-10-26/src/img/*`.
3. **Fonts** (SIL OFL) go in `fonts/` next to the HTML. Download them from `https://raw.githubusercontent.com/google/fonts/main/ofl/`:
   - `cormorantgaramond/CormorantGaramond[wght].ttf` and `-Italic[wght].ttf`
   - `playfairdisplay/PlayfairDisplay[wght].ttf`
   - `inter/Inter[opsz,wght].ttf`
   - `mukta/Mukta-Regular.ttf` and `-SemiBold.ttf`
   - `tirodevanagarihindi/TiroDevanagariHindi-Regular.ttf`
   - `cinzel/Cinzel[wght].ttf`

   URL-encode `[` and `]` as `%5B` and `%5D`.
4. **Render:** `node render.js <out> home,epooja`. Playwright and Chromium are preinstalled.
5. **Full-size Canva pictures:**
   - Canva's generate-image tool only returns thumbnails.
   - To get full size, place the media in the private holder design `DAHZE1K9-8k`: `read-design` with open_transaction → `insert_fill` or `update_fill` on a page → commit → `export-design` as jpg → curl the URLs.
   - The holder already has 4:3, 9:16, 16:9 and square pages.
6. **The data is for Mon 26 Oct 2026.** If you re-render on a later day, re-read astroriver.com/panchang and update every time and tithi, or say clearly that the screens show 26 Oct.

## Likely next steps

- Apply the founder's feedback on the combined design.
- Possibly show a Hindi version (only after he types "Hindi approved" for anything live).
- Possibly make other tab screens (Ask, Pujas, Tools, Me) in the same style.
- Keep each round lean, look at your own renders before sending, and stay under about 45% context. Hand over with a note like this one.
