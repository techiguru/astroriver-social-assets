# Brief: Mobile home v5 (from Krishna, 25 Oct 2026). Supersedes HOME-PROPOSAL.md where they differ.

You are "Mobile Home 3", a worker for Astro River. Report to Krishna (KRISHNA 4, session_01Vt8o8oqtkgeaYCaJVddocA) by send_message after each step and whenever blocked; the founder talks to Krishna. Repo astroriver/astro-river; the v4 home is PR #162 (read it and its screenshots first). Branch from #162's head or main as #162 requires; previews only, no production; never push main; no force/amend/rebase/reset; author "Astro River <noreply@astroriver.com>", no co-author trailers, no vendor or model names. Stay under 30% context; hand over at 25%.

## Hard rules (founder, repeated)
- **Dr. Armaan Sharma's name appears only as founder and on archive papers (Inscriptions).** No "from Dr. Sharma", no consultation "with Dr. Armaan Sharma", no quotes in his name. Consultation = "our senior Vedic astrologer".
- Never "real" against AI; AI astrologers are labelled AI. No honorifics on AI cards (plain names: Vedansh, Tara).
- No made-up figures, no promised outcomes, never "little", Hindi words only after "Hindi approved", D-211 (the Astrologer never contacts clients).

## The idea
The home page is who we are: **inform first, then sell.** Someone should open it every day because it tells them something true about their day, in their city. Selling comes after, quietly. Build every section as a self-contained card that will become a screen of the Capacitor apps (coming soon).

## Order, top to bottom (phone first)
1. **Greeting.** "Good morning." + date + city ("in Mohali · change") + language switch. Signed-in client: "Good morning, <first name>." City from Cloudflare's request country/city without asking; change remembered on the device. No sign-up needed for any of the informing sections.
2. **Today** (the big card). Weekday and its deity; sunrise/sunset for the city; tithi and nakshatra with end times; "Good now: <choghadiya> till <time>, then <next>"; Rahu Kaal; a festival strip when one is within 15 days ("Diwali in 14 days · Lakshmi Puja in <city> <window>"). Signed in with a chart: one line on the Moon's house for them. All from our panchang (D-201 rounding).
3. **Today's ePooja** (free, about two minutes, the daily habit). The weekday deity's puja. The client fills in name, gotra and family names once (remembered); an AI pandit voice recites the full sankalpa instantly with today's tithi, nakshatra, place and their names, then the puja. **No pandit records anything.** Labelled plainly as a recited, generated voice. v1 = the seven weekday deities. For this PR: the card and its entry point only; the ePooja itself is a separate plan (Krishna will brief it).
4. **Your rashifal today.** Pick a sign once (remembered); one or two lines, link to the full page.
5. **This week and what's coming.** The latest weekly sky piece from the Journal (title + two lines), and the next three festivals with their dates for the city.
6. **Free tools grid.** Heading "Start here, free." Kundli, Kundli Matching, A good day (Muhurat), Rashifal, Panchang, Manglik, Sade Sati, Shubh Samay. Pujas and gemstones leave this grid.
7. **Then sell, one section, calm:** Ask a question (price below) · the AI astrologers by the minute (labelled AI) · Pujas performed for you (Diwali Lakshmi Puja first while it is open) · a private consultation with our senior Vedic astrologer · Inscriptions ("Your year, written for you").
8. **How we work** (as is) and the footer.

## Prices and offers (Krishna's decisions)
- **Ask a question: regular ₹399, first question ₹99**, shown "~~₹399~~ ₹99 · your first question". The struck price must be real (consumer law on false reference prices): every later question is ₹399. USD follows the existing USD struck-price pattern; propose the USD figures from the site's current USD table, don't invent a parity. Includes **one follow-up to clarify the answer**; copy: "One question, answered from your chart. One follow-up to clarify, included."
- Pujas: up to four family names in the sankalp at no extra charge. No separate low-priced entry puja: the free ePooja is the entry.
- Diwali Lakshmi Puja: performed on Sun 8 Nov in the Lakshmi Puja window; bookings close Sat 7 Nov, 6 pm IST. Show it only if the puja product exists with that date; if not, report and leave the slot out.

## Habit, not gimmicks
- City, sign and puja details remembered on the device; no sign-up wall in front of information.
- At night (after sunset), Today shows a small "Tomorrow" peek.
- Opt-in reminders (ePooja daily, festival muhurat, Rahu Kaal): design the opt-in now; on the web, offer add-to-home-screen on the third visit; push wiring comes with the app.
- No streak counters or badges.

## App-ready (Capacitor)
- Phone layout has a bottom tab bar ready: Today · Ask · Pujas · Tools · Me (behind a flag on the web if it clashes with the current menu; propose).
- Each section is its own component taking data from one API/data layer (no data baked only into the page), so the app reuses it.
- Safe-area insets, no hover-only UI, 44 px touch targets, today's panchang cached for offline, every card deep-linkable (astroriver.com/<path> = the app screen).

## Also in this PR
The two image bugs (blank puja images, broken Journal image), the folded footer, and the free-tools grid fix from the v4 review.

## Steps and reports
1. Plan (files, components, data sources, what needs new data) → report to Krishna, wait for "go" from Krishna.
2. Build on a preview branch; screenshots at 390 px and 1280 px, light and dark → report with preview link.
