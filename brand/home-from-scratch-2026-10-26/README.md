# Home page from scratch: three directions (26 Oct 2026)

These are pictures only, not site code. The brief is `handover/2026-10-25-krishna/BRIEF-home-from-scratch.md`.

**Start with `compare.png`.** It shows all three directions side by side.

| Folder | Direction |
|---|---|
| `A-temple-morning/` | Picture-led. A full-bleed painting of today's deity carries the greeting. Today sits on a warm card over the painting. Stories row, ePooja and rashifal follow as big pictures. |
| `B-the-almanac/` | Editorial, like a finely printed panchang. A big serif date and tithi in English and Devanagari, gold rules, one painting per section and large type. |
| `C-the-app/` | App-first. Stories row, a swipeable Today card, "What would you like to do today?" chips, picture tiles and a tab bar. The desktop is an app shell. |

Each folder has three screens:
- `phone-1-first-screen.png`: 390 × 844 at 2x.
- `phone-2-scrolled.png`: the same phone, one scroll down.
- `desktop-first-screen.png`: 1440 × 900.

On phone, all three use the bottom tab bar Today · Ask · Pujas · Tools · Me, ready for the apps.

## Data shown (all real, New Delhi, Monday 26 Oct 2026)

All panchang data is from astroriver.com/panchang (Lahiri ayanamsa), read on 26 Oct. The screens show the time as 9:32 am.

| Item | Value |
|---|---|
| Tithi | Purnima till 9:41 am, then Krishna Pratipada |
| Nakshatra | Ashwini till 5:41 pm, then Bharani |
| Moon | In Mesha (Chandrashtama for Kanya) |
| Sunrise / sunset | 6:29 am / 5:41 pm |
| Good now (choghadiya) | Shubh 9:17–10:41 am, then Rog till 12:05 pm |
| Abhijit | 11:43 am – 12:27 pm |
| Rahu Kaal | 7:53–9:17 am |
| Yamaganda | 10:41 am – 12:05 pm |
| Tomorrow (Tue 27 Oct) | Krishna Pratipada · Bharani, Rahu Kaal 2:53–4:16 pm |
| This week's sky | "Jupiter enters Simha on Saturday afternoon; Mercury, Venus and Saturn are retrograde all week." (quoted from the panchang page) |

Festivals use the dates in the brief:
- Karwa Chauth: Thu 29 Oct
- Dhanteras: Fri 6 Nov
- Diwali: Sun 8 Nov, Lakshmi Puja in New Delhi 5:54–7:50 pm

The day counts are from Mon 26 Oct.

## Founder rules applied

- The founder's name appears nowhere on these screens.
- The order is: greeting → Today → ePooja → rashifal → week/festivals, then selling. Inform first, then sell.
- The greeting comes with the date, the city (with "change") and EN / हिंदी.
- ePooja is shown as "Today's ePooja · about 2 minutes" and marked "Opening soon". It describes "an AI pandit voice" reciting the sankalpa.
- The only price shown is ~~₹399~~ ₹99 for the first question, with one follow-up included. No counts, figures or promised outcomes appear.
- Vedansh and Tara are labelled AI, with no honorifics.
- There is no line art: the screens use paintings and photographs only. They are not grids of plain boxes.

## Pictures

**New, made in Canva for this study** (Canva media IDs in brackets). Full-size copies are in `src/img/`.
- `shiva-portrait` (MAHZE7lLAV8) and `shiva-wide` (MAHZE4c0FiY): Pichwai-style Shiva on Kailash. Monday's deity.
- `puja-thali` (MAHZE7yH7Bw): photograph of a morning puja thali.
- `astrologer-desk` (MAHZEy-mg7g): photograph of a birth chart on a desk. The chart's Devanagari is decorative, not readable.
- `moon-ghat` (MAHZE5hA9G0): painting of a full moon over a river ghat.
- `temple-lakshmi` (MAHZE8NymOI): photograph of a lamp before Lakshmi.

**Reused:**
- `brand/festival-pictures-2026-10-25/`: Karwa Chauth, Dhanteras.
- `handover/2026-10-25-krishna/lakshmi-covers/`: Diwali Lakshmi.
- The Seal C app icon as the mark. The crest is still waiting for the founder's pick.

## Rebuilding

`src/` holds the HTML (`A.html`, `B.html`, `C.html` with `?v=phone` or `?v=desktop`), `render.js` (Playwright) and `compare.html`. Fonts are not committed. They are SIL OFL fonts from github.com/google/fonts, placed in `src/fonts/`: Cormorant Garamond, Playfair Display, Inter, Mukta, Tiro Devanagari Hindi, Cinzel.

```sh
cd src && node render.js . .. A,B,C A:860,B:860,C:720
```
