# Home, round 3 (27 Oct 2026): a pass over everything, with Night A

The founder picked **Night A (lamp-black)**, so Night B is dropped. Light stays the default. This round is a pass over every section of the home and ePooja pages before the build.

The screens still show the panchang for **Monday 26 October 2026, New Delhi** (astroriver.com/panchang, Lahiri). They were not updated for later days.

## What was checked
- **Pages:** home and ePooja, every section.
- **Sizes:** phone 390 and 360, desktop 1440.
- **Themes and text:** light and night, at normal and large text (about 130%). Large text scales body text by 1.3, tapering to 1.0 for display type of 40 px and up. App chrome (top bar, tab bar) keeps its size, as on iOS.
- **Measured automatically** (`src/audit.js`, results in `audit/report.json`): clipped text, the page getting wider than the screen, and tap targets under 44 px. The last run found none.
- **Contrast** is WCAG AA (4.5:1) or better for every text colour on every background it sits on, in both themes.
- **Full matrix:** all 24 renders are in `audit/`.

## Files
- `overview.png`: one sheet with everything.
- `home-phone390-*`, `home-phone360-*`, `home-desktop-*`: the home page. `*-first-screen-*.png` is the first screen; `*-full-*.jpg` is the whole page.
- `home-phone360-first-screen-light-large.png`: the first screen at large text.
- `epooja-*`: the ePooja page.
- `logo-current-*.png` and `logo-warm-*.png`: the logo tile option (see below).
- `tokens.json`: the colour tokens. They are the same as the `:root` block in `src/theme.css`.
- `src/`: the sources. Set up `img/` and `fonts/` as in `../home-combined-2026-10-26/HANDOVER.md`, then add `src/img/seal-warm-maroon.png`. Run `node render.js <out>` and `node audit.js <out>`. Add `?seal=warm` to the URL to preview the warm tile.

## Colour tokens (light / night)
| token | use | light | night |
|---|---|---|---|
| bg | page | #fbf6ec | #15100c |
| surface | cards | #fffdf8 | #241b15 |
| surface-2 | wells, panchang boxes, footer | #f6eddc | #1f1813 |
| line | borders, rules | #ecdfc6 | #3a2d22 |
| text | body text | #2b2326 | #f3e9d7 |
| text-muted | secondary text | #645a6c | #b9a793 |
| heading | headings, wordmark | #2c1a1f | #f2dcae |
| accent | links, date, Devanagari | #7a2233 | #f0a77e |
| primary / on-primary | buttons, selected day and sign, play, AI tag | #7a2233 / #fffdf8 | #e2bd72 / #2a1a10 |
| gold | rules, arch, borders | #b8862f | #e2bd72 |
| gold-text | gold text | #836017 | #e2bd72 |
| label | small uppercase overlines | #a64f17 | #f2a65a |
| flame | decoration only (story rings) | #e8892b | #f2a65a |
| tint-saffron / lotus / leaf / gold | section bands | #fdeedb / #fbe6e8 / #e6f2e9 / #f8efd9 | #2b1c11 / #2c1719 / #1b2219 / #282015 |
| good, good-bg / bad, bad-bg | Good now, Rahu Kaal | #276a42, #dff0e4 / #b43c46, #fbe3e3 | #9bd3a9, #1c2a1e / #f2a39c, #361b1b |
| on-photo, glass, scrim | text and controls over photos (both themes) | see tokens.json | |

## Every change from round 2
**Colour**
1. All colours come from the token set above. The night-only overrides and every one-off colour are gone: the story rings, the ePooja photo text and its overlays are now tokens.
2. The last blue is gone. Headings were indigo (#1f1a4f) and are now a warm near-black (#2c1a1f). Body text moved from #2a2233 to #2b2326.
3. Contrast fixes, light mode:
   - Overline labels: #e8892b → #a64f17. They were 2.3 to 2.6:1 and are now at least 4.7:1.
   - Gold text: #9a6f24 → #836017. It was 3.9 to 4.4:1.
   - Muted text: #6f6577 → #645a6c. It was 4.6 to 4.8:1 on the bands.
   - "Good now" green: #2f7d4f → #276a42. It was 4.25:1.
4. The ePooja picture's dark fade had never shown, a bug since round 1, so the title sat on the bare painting. It is fixed, and the painting is still visible above the text.
5. The logo tile is shown in a warm maroon version beside the current navy one, as an option only. It is not applied, and the crest is unchanged.

**Size and fit**

6. The phone layout is fluid. There is no sideways scroll at 360, or at large text.
7. Tap targets:
   - Top bar icons are 36 px circles on a 44 px pitch, each with a 44 px hit area. The EN/हिं switch is one 44 px control.
   - Chips, buttons and desktop "Sign in" are at least 44 px tall.
   - ePooja back and share are 44 px. The name and gotra fields are 52 px.
   - Text links (→) have a 44 px hit area.
8. Small text was raised:
   - "This week" labels: 8.5–9.5 px → 11 px.
   - AI tag: 9 → 10 px.
   - Panchang box labels, field labels and Learn labels: 10 → 11 px.
   - Story names: 11 → 12 px.
   - Tags: 10 → 11 px.
9. "This week" is now a scrolling day strip instead of seven squeezed columns, so tithi and festival names stay readable.
10. Fit fixes:
    - Shop circles scale with the screen; the last one was cut off at 360 with large text.
    - The A/B/C letters of the founder papers line up.
    - The Gita verse's danda (।) no longer drops onto a line of its own.
    - Buttons and tags never break in two ("Remind me daily" did at large text); a row of buttons wraps instead.
    - The desktop mantra player keeps its wave and "× 108" at large text.
11. The ePooja title block grows with large text, so it stays below Shiva's face. Its tags never split.

**Copy** (forced by the live site or the rules)

12. Ask card: "One question, answered from your chart. One follow-up to clarify, included." → "One question, answered in writing by an AI astrologer, from your chart. One clarification included." This matches the live /ask page and labels the AI.
13. Diwali Lakshmi Puja: "with up to four family names in the sankalpa" → "in your name and gotra, with your family's names if you add them." The live page sets no four-name limit.
14. Shop: the category "Puja items" → "Pujas", on phone and desktop. The live shop has Pujas and no puja-items category.
15. Free tools, desktop: "Muhurat for what you plan" → "Muhurat for your plans", the same as on phone.
16. "Soon" marks for pages that are not live:
    - Chips (phone and desktop): Today's ePooja, Read the Gita.
    - Desktop menu: ePooja, Mantras, Learn.
    - "Opening soon" tags: All mantras and aartis, the texts row, the nakshatra course card, the "Reading your own kundli" card.

Nothing was removed. The layout, the order of sections and all other wording are unchanged.

## Where every tap goes (live astroriver.com routes, checked 27 Oct 2026)
"Sign-in" means the page is live but asks the visitor to sign in first. "SOON" means there is no page yet, and the design marks it.

| On the page | Opens |
|---|---|
| Logo | / |
| EN / हिं | Hindi home: **no page, flagged**. Hindi exists for /hi/panchang, /hi/journal/…, /hi/weekly-horoscope, /hi/planetary-positions |
| Moon icon | switches light and night on the page |
| Bell | notifications: **no page, flagged** |
| New Delhi · change | city picker on the page (same cities as /panchang) |
| Tithi, Sun, Rahu Kaal boxes | /panchang |
| Nakshatra Ashwini | /nakshatra/ashwini |
| Good now · Shubh | /muhurat (Choghadiya) |
| Karwa Chauth strip | /journal/karwa-chauth |
| Stories: Shiva's day · Mantra · Karwa Chauth · Dhanteras · Diwali | ePooja (SOON) · mantra player on the page · /journal/karwa-chauth · /journal/diwali/dhanteras · /journal/diwali. The story viewer itself is new to build |
| Chips: Today's ePooja · Chant a mantra · Make my kundli · Diwali puja · Read the Gita · Shop | ePooja (SOON) · mantra player on the page · /kundli · /alchemies/diwali-lakshmi-puja-2026 · Gita (SOON) · /alchemies |
| ePooja card: Begin · Remind me daily | ePooja page, this design (SOON) · reminders (SOON, inside the opening-soon card) |
| Mantra: play, × 108 | on the page (audio still undecided) |
| All mantras and aartis | SOON |
| Rashifal signs | /rashifal/mesh, /vrishabh, /mithun, /kark, /singh, /kanya, /tula, /vrishchik, /dhanu, /makar, /kumbh, /meen |
| This week: day cells | /panchang/&lt;date&gt; |
| "Jupiter enters Simha" | /journal/jupiter-in-leo-2026 |
| Festival cards | /journal/karwa-chauth · /journal/diwali/dhanteras · /journal/diwali |
| Verse: Share | the phone's share sheet |
| Texts row: Bhagavad Gita, Hanuman Chalisa, Shiv Chalisa, Aartis | SOON |
| Free tools: kundli · matching · a good day · Manglik · Sade Sati | /kundli · /kundli-matching · /muhurat · /manglik-dosha (the "Sade Sati" half opens /sade-sati) |
| All tools | /tools (sign-in) |
| Learn: nakshatra course · Saturn retrograde · reading your kundli | SOON (live now: /nakshatra has all 27) · /journal/saturn-retrograde-2026 · SOON |
| Journal → | /journal |
| Pujas card, Book the puja | /alchemies/diwali-lakshmi-puja-2026 |
| All pujas | /alchemies/category/pujas |
| Shop: Visit · four circles | /alchemies · /alchemies/category/gemstones, /rudrakshas, /yantras, /pujas |
| Ask a question | /ask (sign-in) |
| Vedansh AI, Tara AI | /lobby (sign-in) |
| A private consultation | /consultation |
| Inscriptions card | /inscriptions |
| Founder papers A, B, C · Library | /archives/first-principles, /archives/dasha-systems, /archives/nature-of-nakshatras · /archives |
| Footer links | /panchang · /alchemies/category/pujas · /ask · /tools · /journal · /alchemies |
| Tab bar: Today · Ask · Pujas · Tools · Me | / · /ask · /alchemies/category/pujas · /tools · /profile (Ask, Tools and Me need sign-in) |
| Desktop menu | Today / · Panchang /panchang · ePooja SOON · Mantras SOON · Pujas /alchemies/category/pujas · Ask /ask · Free tools /tools · Learn SOON · Shop /alchemies · Sign in /login |
| ePooja page: back · share · name and gotra · Begin the puja | the home page · share sheet · on the page (kept on the phone) · the steps on the page |

## Open points
- **₹399 / ₹99:** these come from the price rule in `../home-combined-2026-10-26/HANDOVER.md`, carried over from the founder. Live /ask is behind sign-in and its price comes from the database, so I could not see it on a public page. Someone signed in should confirm it before launch.
- **Vedansh and Tara:** the AI astrologer list (/lobby) is behind sign-in and comes from the database. Confirm both names are live.
- **Founder's name:** the founder's rule for this page is that his name appears nowhere on it. The papers are listed by title only, so "Dr. Armaan Sharma" is not used. The live archive also has paper D, "Jaimini Sutras and Modern Practice". It can be added if wanted; I did not add it.
- **Desktop:** the desktop page shows fewer sections than the phone (no mantra band, rashifal, Learn, Inscriptions, papers or "How we work"). The build should reuse the phone sections.
- **Not live yet, and marked SOON:** ePooja, the mantra and aarti library, the texts library, the course, the kundli guide, reminders, notifications, the Hindi home and the app.
