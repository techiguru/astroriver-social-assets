# Home, round 4.2 (27 Oct 2026): your sky, the planets, the remedy, four times of day

Round 4 starts from round 3.1 (`../home-design-3-2026-10-27/`). It adds the astrology and the institute to the almanac without redesigning what was there. All the round 3 tokens and fixes are kept. Light is the default, and Night A (lamp-black) is the night mode. A build chat should start at "Build handover", at the end.

**Round 4.2** (the founder's notes on 4.1):
1. **Logo:** the warm maroon tile is decided. It is used in the header, the footer and on desktop, and the navy option is gone from the overview.
2. **Streak** in Today's remedy. A day counts when at least one act is ticked, and one missed day in any seven does not break it.
   - The ladder is our own, a lamp theme with traditional counts: 1 "The first lamp", 7 "A week kept", 21 "Three weeks", 40 "A mandala, forty days", 108 "A mala, a hundred and eight days".
   - Copy:
     - "12 days kept · next: 21 days".
     - New visitor: "Light the first lamp today. Tick any one act and the day counts."
     - After a break: "Start again today."
     - A lamp reached: one quiet card with the level's name, and no confetti.
   - No guilt copy, ever.
3. **Top line:** a slim line above the header for one campaign, e.g. "**Diwali Lakshmi Puja** · closes in 11 days · Book →".
   - It is dismissible (×), and stays hidden for the rest of the day once dismissed.
   - The countdown runs only to the campaign's real end time: days when it is 2 days or more away, then hours, then minutes.
   - It hides when no campaign is live.
   - At 390 the panchang tiles stay on the first screen with it. To make room, the header and the date numeral are a little tighter.
4. **Pop-up:** the same campaign. On the phone it is a bottom sheet; on desktop a small card at the bottom right.
   - It shows a picture, one line, the real deadline and one button.
   - It appears after about 20 s or 50% scroll, never on arrival and never over the first screen's panchang, and at most once a day.
   - It closes with one tap: the × or a tap outside.
5. **The no-fake-urgency rule**, below.

### Rule: no fake urgency
Indian dark-pattern rules name false urgency and nagging. On this page:
- **Countdowns** run only to a real end time (a product's booking close, or a coupon's valid-until). They never restart, never reset per visit and never run past the end. With no end time there is no countdown.
- **No invented scarcity or social proof:** no "only N left", no "N people viewing", no "N booked today" unless the number is real, live and audited.
- **No pre-ticked boxes**, no add-ons in the basket by default, and no "No, I don't want…" decline copy.
- **No nagging:** one campaign at a time; the top line hides for the day once dismissed; the pop-up shows at most once a day, never on arrival, and closes in one tap.
- **No guilt:** the streak never says a streak was broken or lost. It just offers "Start again today".

**Round 4.1** (after KRISHNA 13's review):
1. "What would you like to do today?" is now a tight 2 × 3 grid of six live actions: Ask a question · Make my kundli / My kundli · Book a puja · A good day · Chant · Shop. It has no Soon items; ePooja and the texts keep their own sections.
2. The photographs are the Institute's own (the founder's photographs of 20 Oct 2026). The "PHOTOGRAPH" badge is replaced by a quiet caption, "From the Institute's ceremonies".
3. The evening tile reads "Sandhya window", not "Pradosh".
4. The Ask overline reads "AI astrologers · by the minute, any hour". That the names come from live data is a build note, kept here only.
5. The consultation card keeps "in English, Hindi or Punjabi", which is quoted from the live /consultation page: "a private, live session with one of our senior astrologers, who reads your birth chart with you — on an audio call or by chat, in English, Hindi or Punjabi".

**Render day: Tuesday 27 October 2026, New Delhi.** Data comes from astroriver.com/panchang and /planetary-positions (Lahiri), as read that morning. The "with details" screens use an **example chart** (lagna Karka, Moon in Kumbha, Dhanishta pada 3, Jupiter–Saturn dasha). In the build, the site's own kundli engine fills it in.

## Files
- `overview.png`: one sheet with everything, including the warm maroon logo (decided in 4.2).
- 4.2 pieces: `topline-*`, `popup-*` and `streak-*` (new visitor, day 12 light and night, a lamp reached, start again).
- `view/`: the phone 390 morning page with details at 3× (1170 px wide), in 11 screen-sized parts.
- `phone390-first-<time>-<no|with>-details.png`: the first screen for morning, afternoon, evening and night, each without and with birth details (8 files).
- `phone390-full-*.jpg`: the whole phone page in three states: morning light without details, morning light with details, and evening Night A with details.
- `desktop1440-full-*.jpg`: desktop in morning light and evening Night A. Desktop carries the same sections as the phone. `desktop1440-first-morning-light.png` is the desktop first screen.
- `phone360-first-morning-large-text.png` and `phone360-full-morning-large-text.jpg`: phone 360 at large text (130%).
- `audit/report.json`: the audit, 54 runs and 0 issues. Two sample full pages at 360 large text sit beside it.
- `src/`:
  - `home.html`: the sections, written once and used for both phone and desktop.
  - `data.js`: the day's data, the four times of day, the example chart and the remedies.
  - `home-base.css`: the round 3.1 styles.
  - `theme.css`, `shared.js`: from round 3.1.
  - `render.js`, `audit.js`, `audit-lib.js`, `tokencheck.js`, `overview.html` / `overview.js`, `shot.js`.
- URL options: `?v=phone|desktop&tod=morning|afternoon|evening|night&me=0|1`, `&camp=0` (no campaign), `&popup=1`, `&streak=<days>`, `&reached=1`, `&again=1`, plus `&theme=light|dark` to override the theme and `&full=1` for full-page captures. Without `theme`, the page is light in the morning and afternoon, and Night A in the evening and at night.

## Change list vs 3.1
Sections not listed here are as in 3.1.

| # | Section | Change |
|---|---|---|
| 0 | Header | The search icon takes the bell's place. EN/हिं and the moon toggle stay. The search icon, the brand and हिं all have 44 px hit areas. |
| 1 | Almanac | **New** identity line under the greeting block: "The Astro River Institute's almanac, consultations and pujas · Jalandhar · since 2008". On the phone, the deity painting now sits beside the tithi (112 × 138 arch) instead of under it, so that the tiles and the start of "Your sky" fit on the first screen. Desktop keeps the large arch. Tuesday's deity is Hanuman: a new painting, `img/hanuman.jpg`. |
| 2 | **Your sky today** (new) | **No details:** "Tell us your birth date, time and place once. Every morning this page reads your chart.", the button "Add my birth details" → /kundli, and a ghosted example of the filled card, marked EXAMPLE. **With details:** the heading "Moon in your 10th house". Below it: your Moon (sign, nakshatra, pada) and lagna; Mahadasha–Antardasha with end dates; "The Moon crosses your Nth house" with one plain line on what it tends to bring; a Sade Sati flag → /sade-sati; "Your full kundli →"; Edit → /profile. |
| 3 | **Planets now** (new) | One strip with the nine grahas, each with its sign, and ℞ on Mercury, Venus and Saturn. The strip → /planetary-positions. |
| 4 | What would you like to do today? (4.1) | A 2 × 3 grid of equal tiles (picture and label), six live actions only: Ask a question → /ask · Make my kundli / My kundli → /kundli · Book a puja → /alchemies/category/pujas (it may read "Diwali puja" during Diwali) · A good day → /muhurat · Chant → the remedy on this page · Shop → /alchemies. On desktop the six tiles sit in one row. |
| 5 | **Today's remedy** (changed; absorbs Mantra of the day) | The day's deity, and three tickable acts: the chant with the player (11 or 108), an offering, and what to wear or avoid. It shows "n of 3 done", and the ticks are kept until the next sunrise. Bridge with details: "The Moon in your chart: in Kumbha, in your 8th house. The Chandra remedy →" (/remedies). Without details: "Remedies for each graha →" (/remedies). In the evening it becomes the evening act: the diya at sunset, the aarti with the player, and the prasad. At night it keeps the evening ticks and adds a line on tomorrow's deity. |
| 6 | Today's ePooja | Monday's Shiv puja becomes "Mangalvar Hanuman puja". Still opening soon, with no button. |
| 7 | Rashifal | With details, Kumbha is pre-picked and labelled "your Moon sign", and the Moon's current sign is marked "Moon now". |
| 8 | This week | Updated to 27 Oct: Karwa Chauth in 2 days, Dhanteras in 10, Diwali in 12. |
| 9 | **Tomorrow at 6 am** (new) | One warm card: "Get tomorrow's panchang on WhatsApp", with "Follow the channel" → the channel, and a small Instagram link. |
| 10–13 | Verse, texts, free tools, learn | Unchanged. The course card now reads "Today's is Bharani". |
| 14 | **Pujas** (changed) | Three cards: Diwali Lakshmi Puja; Navagraha Shanti Puja with the Institute's own photograph (`img/havan-kund.jpg`, from the live puja page), captioned "From the Institute's ceremonies"; "All pujas →". Under them: "Photos of your puja are sent to you after the ceremony." |
| 16 | **Ask** (changed) | The private consultation is now a full card, the same size as "Ask a question": what it is (live, audio or chat, English, Hindi or Punjabi, by the minute, fifteen minutes at least) and "Book →". It shows no price, because /consultation shows none. There is no face and no name. Vedansh and Tara keep a name and one line each ("Opens the lobby"), under "AI astrologers · by the minute, any hour". Build note: the names come from live data, the /lobby source; do not hard-code them. |
| 19 | **How we work** (changed) | "30+ years of practice · 35,000+ charts read · Jalandhar" under the heading. The three numbered lines stay. The painting is replaced by the Institute's own photograph (`img/navagraha-temple.jpg`, from the live puja page), with the same caption. |
| 20 | **Help** (new) | "A question about an order or a booking?" with "Chat with us" → /contact. |
| 21 | Site footer | The live site's footer, as a plain block: four columns, the © line, the jurisdiction line and the guidance line. |
| — | Stories row | **Removed.** The round 4 order does not list it. Its links still live in the chips and the festival cards. Say if it should come back. |
| — | Desktop | Desktop now carries every phone section, in phone order: two to a row where they pair, and Free tools and Help full width. The menu has Kundli and Journal in place of the three Soon items, Mantras and Learn. ePooja stays, marked SOON. |

**Four times of day** (fixed by code: morning 4–11, afternoon 12–16, evening 17–20, night 21–3). The mockups are shown at 9:32 am, 1:10 pm, 6:05 pm and 10:40 pm.

| | Greeting | Tiles | Picture | Theme |
|---|---|---|---|---|
| Morning | शुभ प्रभात Good morning | Nakshatra · Sun (sunrise, sunset) · Good now (Char till 10:41) · Rahu Kaal 2:53–4:16 | Hanuman | light |
| Afternoon | शुभ दोपहर Good afternoon | Nakshatra · **Next good window** (Vijaya Muhurat 1:57–2:41) · Good now (Amrit till 1:29) · Rahu Kaal (in 1 h 43 min) | Hanuman | light |
| Evening | शुभ संध्या Good evening | Sunset 5:40 pm (Godhuli till 6:06) · **Sandhya window** 5:40–6:57 · **Moonrise** 6:23 pm · Next good window (Labh 7:17–8:53) | the lamp (`img/diya-dusk.jpg`) | Night A from sunset |
| Night | शुभ रात्रि Good night | Quiet: "Tomorrow, Wed 28: Tritiya", Krittika until 1:26 pm; two tiles only (sunrise tomorrow 6:30, Moon in Vrishabha since 9:06 pm); no festival strip | the Moon over the ghat | Night A |

## Checks
Every check below is in `src/audit.js` and `src/tokencheck.js`. The audit has 54 runs (48, plus four pop-up runs and two streak runs): phone 390 and 360 and desktop 1440, × 4 times of day, × with and without details, × normal and large text. **0 issues.**
- **AA contrast:** each text run is measured against the colour behind it (4.5:1, or 3:1 for large text). Text on photographs uses the on-photo tokens over a scrim. A self-test with low-contrast text was caught.
- **Taps:** 44 px or more, including the remedy ticks (28 px circle in a 44 px hit area).
- **One token set:** every computed colour on every state is in `tokens.json`. There is no blue. The evening painting's sky is a painting, not a UI colour.
- **No sideways scroll** at 360 or at large text.
- **Every link is a live route**; Soon items are not links and have no buttons.
- **Copy:**
  - There is no count of AI astrologers and no "AI-powered" wording.
  - The written products are called "Inscriptions".
  - The only prices are ₹399 / ₹99 + GST for Ask. The consultation shows none.
  - The founder's name appears nowhere.
  - The page title is "Today's panchang and your sky — Astro River".

## Tap list (4.2 additions)
| On the page | Opens |
|---|---|
| Top line: Book → | the campaign's link (now /alchemies/diwali-lakshmi-puja-2026) |
| Top line: × | hides the line until tomorrow (on the device) |
| Pop-up: button | the campaign's link |
| Pop-up: ×, or a tap outside (phone scrim; desktop: anywhere off the card) | closes it; not shown again that day |
| Streak ladder | not a link |

## Tap list
Unchanged rows from 3.1 are repeated, so this is the whole list. "Sign-in" means the page is live behind sign-in.

| On the page | Opens |
|---|---|
| Logo | / |
| Search icon | /search (the live site's "Find anything") |
| EN / हिं | हिं → /hi/panchang |
| Moon icon | switches light / Night A on the page |
| Identity line | not a link |
| City · change | city picker on the page |
| Tithi block | /panchang |
| Tiles | Nakshatra → /nakshatra/bharani · Sun, Rahu Kaal, Sunset, Sandhya, Moonrise, Sunrise tomorrow → /panchang · Good now, Next good window → /muhurat · Moon (night) → /planetary-positions |
| Festival strip | /journal/karwa-chauth |
| Your sky, no details: Add my birth details | /kundli (the ghosted example is not a link) |
| Your sky, with details: Moon row, dasha row · transit row · Sade Sati flag · Your full kundli · Edit | /kundli · /planetary-positions · /sade-sati · /kundli · /profile |
| Planets now: strip, All → | /planetary-positions |
| What would you like to do today: Ask a question · Make my kundli / My kundli · Book a puja · A good day · Chant · Shop | /ask · /kundli · /alchemies/category/pujas · /muhurat · the remedy on this page · /alchemies |
| Remedy: ticks, player, × 108 | on the page (ticks kept on the device until sunrise; audio still undecided) |
| Remedy bridge | /remedies (with or without details) |
| Today's ePooja | SOON, with no button |
| Rashifal signs | /rashifal/mesh … /rashifal/meen |
| This week: heading, day cells, festival cards | /journal/jupiter-in-leo-2026 · /panchang (Thu → /journal/karwa-chauth, Sat → /journal/jupiter-in-leo-2026) · /journal/karwa-chauth, /journal/diwali/dhanteras, /journal/diwali |
| Tomorrow at 6 am: Follow the channel · Instagram | https://whatsapp.com/channel/0029Vb92NvV2v1J203DyVy39 · https://instagram.com/astroriverofficial |
| Verse: Share | native share sheet |
| The texts | SOON |
| Free tools · All tools | /kundli, /kundli-matching, /muhurat, /manglik-dosha · /tools (sign-in) |
| Learn: course · Saturn piece · kundli guide · Journal → | SOON · /journal/saturn-retrograde-2026 · SOON · /journal |
| Pujas: Book the puja · See the puja · All pujas card · All pujas → | /alchemies/diwali-lakshmi-puja-2026 · /alchemies/navagraha-shanti-puja · /alchemies/category/pujas · /alchemies/category/pujas |
| Shop: Visit · four circles | /alchemies · /alchemies/category/gemstones, /rudrakshas, /yantras, /pujas |
| Ask a question (card and "Ask →") | /ask (sign-in) |
| Vedansh, Tara | /lobby (sign-in) |
| A private consultation (card and "Book →") | /consultation |
| Inscriptions | /inscriptions |
| Founder papers A–D · Library | /archives/first-principles, /dasha-systems, /nature-of-nakshatras, /jaimini-sutras · /archives |
| Help: Chat with us | /contact (it has the chat widget) |
| Site footer | the live footer's own links, unchanged |
| Tab bar: Today · Ask · Pujas · Tools · Me | / · /ask · /alchemies/category/pujas · /tools · /profile |
| Desktop menu | Today / · Panchang /panchang · Kundli /kundli · ePooja SOON · Pujas /alchemies/category/pujas · Ask /ask · Free tools /tools · Journal /journal · Shop /alchemies · Sign in /login |

## DATA: where each shown field comes from
| Field | Source |
|---|---|
| Date, weekday (English and Hindi), city | device date; city picker (same list as /panchang) |
| Greeting and part of day | the code's four parts of day (4–11, 12–16, 17–20, 21–3) for the city's local time |
| Theme | light by day; Night A from sunset (panchang sunset for the city) until sunrise, or by the moon toggle |
| Tithi, end time, next tithi; nakshatra and end time | panchang engine behind /panchang |
| Sunrise, sunset, moonrise, Godhuli, Sayahna Sandhya (the "Sandhya window") | panchang engine (/panchang "Sun", "Moonrise", the GOOD bar). If a Pradosh window is wanted later, the Diwali code already has a Pradosh rule the build can reuse. |
| Good now, next good window (choghadiya, Abhijit, Vijaya) | panchang engine (choghadiya and "Later today", the same data as /muhurat) |
| Rahu Kaal and "in 1 h 43 min" | panchang engine; the countdown is computed on the page |
| Tomorrow's tithi and nakshatra (night) | panchang engine, the "Tomorrow" view of /panchang |
| Deity, painting, caption | static, one per weekday (plus the evening lamp and the night Moon pictures) |
| Festival countdown, this week, festival cards | panchang for 7 days and the journal's festival dates |
| Identity line, stats line ("30+ years · 35,000+ charts · Jalandhar") | static copy, as given by the founder's office |
| Your Moon sign, nakshatra, pada, lagna | client-side kundli engine (/kundli), from the saved birth details |
| Mahadasha, Antardasha and their end dates | kundli engine, Vimshottari |
| "The Moon crosses your Nth house" | today's Moon sign (planetary positions) counted from the natal lagna; the one plain line is static copy, one per house (12 lines) |
| Sade Sati flag | transit Saturn against the natal Moon (the same logic as /sade-sati) |
| Planets now: sign and ℞ | the engine behind /planetary-positions |
| Remedy: deity and three acts (day and evening sets) | static, one set per weekday |
| Remedy ticks | on the device, cleared at the next sunrise |
| Bridge "The Moon in your chart …" | kundli engine (natal Moon sign and house) |
| Rashifal: Moon now, your Moon sign | panchang (Moon sign); kundli engine (natal Moon), or the visitor's pick |
| WhatsApp channel, Instagram | static links |
| Pujas: Diwali booking close; Navagraha text and photograph | Alchemies (the live product pages) |
| Ask price | `src/lib/askQuestion.ts` (₹399 + GST; first question ₹99 + GST) |
| Vedansh, Tara | live data, the /lobby source; not hard-coded |
| Consultation text | the live /consultation page (no price shown, so none here) |
| Founder papers | the archives list, titles only |
| Footer | the live site footer |
| Birth details themselves | saved by /kundli for the visitor; the home reads them (signed in: /profile) |

### DATA (4.2 additions)
| Field | Source |
|---|---|
| Campaign: title, link, end time, picture, line, button | one config (`CAMPAIGN` in `data.js`); the end time is the product's booking close in Alchemies, or a coupon's valid-until |
| Countdown in the top line | computed on the page from the end time; it hides itself when the end time passes |
| Top line dismissed, pop-up seen today | on the device, cleared at the next day |
| Streak count, days kept, lamps reached | **signed out: on the device; signed in: on the account** (merged on sign-in, the larger count wins). A day = at least one remedy act ticked; one missed day in any seven does not break it |
| Ladder names and counts | static (`LADDER` in `data.js`) |

## Open questions
1. **The house lines.** "What the Moon in your Nth house tends to bring" needs 12 short lines in the institute's voice. The two shown (10th, 11th) are drafts.
2. **Remedy content.** The weekday acts need the institute's sign-off: for Hanuman, the chant; red flowers, or jaggery and chana; red or saffron clothes, and no meat or alcohol. In the evening, the diya, the aarti and the prasad. Mantra and aarti audio is still undecided.
3. **The top line and "Your sky" at 390:** with the top line on, the tiles stay on the first screen, but the "Your sky" heading moves just below it. Without a campaign, it shows as in 4.1.

Settled in 4.1:
- The photographs are the Institute's own.
- The evening tile reads "Sandhya window".
- The consultation shows no price, because the live page shows none.
- The stories row stays out until there is a story viewer.
- Logo: warm maroon (4.2).

## Build handover
Start from this folder. `src/home.html` with `src/data.js` is the reference. Each section is one function, and the phone and desktop render the same functions.
- **Colour:** `tokens.json` (unchanged from 3.1) is the only source of colour. `tokencheck.js` proves the mockup uses nothing else.
- **Fonts:** as in 3.1 (Cormorant Garamond, Playfair Display, Inter, Tiro Devanagari Hindi, Mukta, Cinzel; all SIL OFL). To rebuild, put them in `src/fonts/` (see `../home-combined-2026-10-26/HANDOVER.md`).
- **Images:** copy `src/img/` from 3.1's sources: `../home-combined-2026-10-26/src/img/*` and `../home-from-scratch-2026-10-26/src/img/*`. The new pictures in `src/img/` are:
  - `hanuman.jpg` and `diya-dusk.jpg`, two new paintings;
  - `havan-kund.jpg` and `navagraha-temple.jpg`, the photographs from astroriver.com/alchemies/navagraha-shanti-puja.
- **Run:** `node render.js ..`, `node audit.js ../audit`, `node tokencheck.js`, and `node overview.js ../overview.png`.
- **Part of day and theme:** use the code's four parts exactly. Night A switches on at the city's sunset, and the visitor's toggle wins.
- **Your sky:** shown only when birth details are saved. Otherwise show the invitation with the ghosted example. There is no Ashtakavarga score.
- **Ticks:** stored on the device and cleared at the next sunrise for the city.
- **Soon:** a feature that is not live has an "Opening soon" line or tag, and never a button.
- **The build starts only on the founder's explicit approval.**
