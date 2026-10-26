# Home, combined: the almanac on top, the app below (26 Oct 2026)

These are pictures only, not site code. They follow the founder's direction of 26 Oct:
- Direction B (The Almanac) opens the page.
- C's app parts follow as you scroll.
- The page is bright, with a dark mode.
- It is long and engaging, with things to do right on the page and every part of Astro River shown.
- Direction A (Temple morning) becomes the ePooja page.

**Start with `overview.png`.**

## Files

**Home page:**

| File | What it is |
|---|---|
| `home-phone-first-screen-light.png` / `-dark.png` | The first phone screen, 390 × 844 at 2x |
| `home-phone-full-light.jpg` / `-dark.jpg` | The whole phone page, top to bottom |
| `home-desktop-first-screen-light.png` / `-dark.png` | The first desktop screen, 1440 × 900 |
| `home-desktop-full-light.jpg` | The whole desktop page |

**ePooja page (A's style):**

| File | What it is |
|---|---|
| `epooja-phone-first-screen-light.png` / `-dark.png` | The first phone screen |
| `epooja-phone-full-light.jpg` / `-dark.jpg` | The whole phone page |
| `epooja-desktop-first-screen-light.png` / `-dark.png` | The desktop screen |

## The home page, top to bottom (phone)

1. **The almanac:** greeting, the big date in English and Hindi, city, tithi, the painting of today's deity, four time tiles (nakshatra, sun, Good now, Rahu Kaal) and the festival strip.
2. **Stories row.**
3. **"What would you like to do today?"** with picture chips.
4. **Today's ePooja**, marked "Opening soon". It opens the ePooja page.
5. **Mantra of the day**, with a player on the page and an × 108 counter.
6. **Your rashifal:** pick your sign once.
7. **This week:** a seven-day strip with tithis and events, then festival cards with countdowns.
8. **Today's verse:** Gita 2.47 in Sanskrit and English, then the texts library.
9. **Free tools:** "Start here, free".
10. **Learn and Journal.**
11. **Pujas performed for you:** the Diwali Lakshmi Puja.
12. **The shop (Alchemies):** gemstones, rudraksha, yantras, puja items.
13. **Ask:**
    - Ask a question, ~~₹399~~ ₹99 for the first question
    - Vedansh and Tara, labelled AI, by the minute
    - a private consultation with our senior Vedic astrologer
14. **Inscriptions** and **the founder papers.** The papers are shown by title only, with no name on the home page.
15. **How we work** and the footer.

The tab bar (Today · Ask · Pujas · Tools · Me) is always visible.

## Look

- **Light:** ivory paper, with soft saffron, lotus, sky and gold bands between sections. Only daytime, bright pictures, with text under the pictures rather than on dark fades. More space than the first round.
- **Dark ("night almanac"):** deep indigo, cream and gold text. It is meant to switch by toggle, or automatically from the city's sunset to sunrise.

## Data and content (real)

- **Panchang:** New Delhi, Mon 26 Oct 2026, from astroriver.com/panchang (Lahiri ayanamsa).
  - Tithi: Purnima till 9:41 am, then Krishna Pratipada.
  - Nakshatra: Ashwini till 5:41 pm, then Bharani.
  - Sunrise 6:29, sunset 5:41.
  - Good now: Shubh till 10:41 am.
  - Rahu Kaal: 7:53–9:17 am.
- **Week strip:** the tithis for 27 Oct – 1 Nov and "Jupiter into Simha" on Sat 31 Oct, from the same page.
- **Sankalpa on the ePooja page:** Vikram Samvat 2083, Ashvina, Shukla Purnima, Ashwini, New Delhi. All from the panchang page. It is general; name and gotra are optional fields.
- **Festivals:**
  - Karwa Chauth: Thu 29 Oct
  - Dhanteras: Fri 6 Nov
  - Diwali: Sun 8 Nov, Lakshmi Puja 5:54–7:50 pm
- **Diwali puja card:** the wording follows the earlier home brief.
- **Founder paper titles:** the titles shown on astroriver.com today.
- **Journal article:** the live "Saturn retrograde 2026" title.

## Not decided yet (shown as placeholders)

- **Mantra audio and the ePooja recitation:** the source is still open (own recordings or a generated voice; cost unknown). The ePooja shows a general sankalpa and says "Read along, or listen when the recitation opens".
- **"The nakshatras, one by one" course, the texts library, and shop categories beyond what exists:** drawn as if built, per the founder. Anything not live must be marked "opening soon".

## Pictures

**New, made in Canva on 26 Oct** (media IDs in brackets). Copies are in `src/img/`.

| File | Picture | Canva media ID |
|---|---|---|
| `mantra` | Rudraksha and Shivling | MAHZFexJhTU |
| `texts` | Gita manuscript | MAHZFZLIQW0 |
| `learn` | Notebook with a जन्म कुंडली chart | MAHZFb0pAFE |
| `book` | Inscriptions | MAHZFR9U98M |
| `gems` | Gemstones | MAHZFQZ7VTk |
| `rudraksha` | Rudraksha | MAHZFYl9bNk |
| `yantra` | Yantra | MAHZFXUFC-U |
| `puja-set` | Puja items | MAHZFQw1PJg |

The other pictures are in `brand/home-from-scratch-2026-10-26/src/img/`: Shiva, the puja thali and the festival paintings. To rebuild, copy both sets into one `img/` folder next to the HTML. Fonts are as in that folder's README.

```sh
node src/render.js out home,epooja
```
