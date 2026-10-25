# The phone home page: what will make it compelling

Krishna, for Dr. Armaan Sharma. 25 Oct 2026. Screenshots of v4 as built are in this folder (home-1 … home-5.png).

## The one idea

v4 is a well-built catalogue of us. A compelling home page is a page about **the person holding the phone, today**. Everything below follows from that: the first screen greets them, tells them what today is where they are, and shows one thing that is true only for them. The catalogue comes after, and every heading speaks to one person in plain words.

Nobody in this market does this well. Dharmayana shows the same deity and verse to everyone. AstroTalk is a bazaar of 5,000 strangers by the minute. Sri Mandir sells pujas and gets the gotra wrong. We have one Astrologer, one method, an exact panchang engine, and (soon) the person's own chart. That is the page.

## What is wrong with v4, in your words and mine

1. **"Vedic astrology since 2008 · Jalandhar"** reads as if we think the visitor is in Jalandhar. There is no greeting, no name, no sense that the page knows who is looking. Provenance belongs in a trust line, not the first words.
2. **"People come to us with questions like…"** is what everyone says. Nothing on the first screen is about this visitor.
3. **"Work it out yourself"** sounds like "it's free, so don't bother us". The free tools are our welcome, not a self-service counter.
4. **"Talk to a real astrologer"** under the AI cards says the AI's astrology isn't real. They are not people; the astrology is ours. Never "real". Name the person instead.
5. **"Written readings of your chart"**, "Alchemies", "Work it out yourself", "At any hour" — labels, not sentences. The page needs a voice.
6. **₹49 is still pay-per-question.** The complaint about Dharmayana isn't the ₹85; it's paying ₹85 again to ask "but what about…". The product has to be a conversation with follow-ups, and the home page has to say so.
7. What I missed earlier: the page defaults to New Delhi; the free-tools grid shows Pujas and Gemstones (products) and leaves out six tools that are live; two images are broken; the footer is four long lists on a phone.

## Voice rules for every word on the page

- Speak to one person, in the second person. "Your kundli", not "Kundli generation".
- Say what happens next, in one sentence, with the price if there is one. No labels that need decoding.
- Never "real" against AI. Say "Dr. Sharma", "the Astrologer", "a person".
- Never "yourself". Never "little". No promised outcomes, no made-up figures.
- Time, place and name wherever we have them. A line with "6:36 am in Mohali" beats any adjective.
- Hindi words we all use stay as they are: rashi, tithi, muhurat, puja, sankalp, gotra. Explain once, with a tap, never in the heading.

## The page, top to bottom (v5)

**1. Greeting bar.** Big type, one line, changes with the hour and with what we know.
- Visitor: **"Good morning."** then "Sunday, 25 October · in Mohali (not you? change) · हिंदी"
- Returning (rashi and city remembered on the phone): **"Good morning."** "Mesh rashi · Mohali"
- Client: **"Good morning, Armaan."**
- First visit only, a slim trust line beneath: "Astro River Institute, Jalandhar · reading charts since 2008 · private and confidential." Then it never shows again on the home page; it lives in How we work and the footer.
- City comes from Cloudflare (request.cf.city in a Pages Function), no permission prompt, with "change" beside it; remembered on the device. Not built.

**2. Today (the hero).** One card, big type, four short lines; no stories, no swiping (seniors, one thumb).
- The day: **"Sunday · Surya's day."** "Sunrise 6:36 am in Mohali." Later, a button: "Do Surya ePooja · 2 minutes".
- The tithi and what is coming: "Shukla Chaturdashi till 11:56 am, then Purnima." "Purnima tomorrow." (Festival names from our calendar; Diwali gets its own line below.)
- The times: "Good now: Labh choghadiya till 10:41 am, then Amrit." "Avoid new starts 4:18–5:42 pm (Rahu Kaal)."
- For you: with a chart, "Moon in Revati today, your 12th house: a day for finishing, not starting." (the rashifal second line, personal). Without one: "Tap your rashi for today's line →".
- A festival strip across the bottom when one is near: "Diwali in 14 days · Lakshmi Puja in Mohali 5:5x–7:5x pm → the Diwali page". Times from our engine; it is the best SEO page we have and the home should send people to it.
- Dharmayana's "what is today, what to do" cards, done for the person's city and chart.

**3. Ask.** Heading **"What's on your mind?"** One box. The chips are not a list of generic questions; they come from context: the page they arrived from (Diwali → "When should we do Lakshmi Puja at home?"), the season ("Is November good for a new job?"), or their last question ("Continue where you left off"). Under the box, three routes, one sentence each:
- **"Ask a question · ₹49.** An answer from your chart, and your follow-ups on the same matter for three days." (your rule on days/count)
- **"Ask Vedansh or Tara, any hour.** They answer from your chart by the Institute's method, by the minute, from your wallet. Labelled AI."
- **"Sit with the Astrologer.** A private consultation with Dr. Armaan Sharma, by appointment." → /consultation
- Drop "People come to us with…" and "Prefer a person? Book your Astrologer".

**4. Free.** Eyebrow FREE · NO SIGN-IN. Heading **"Start here, free."** Sub: "Your kundli, a match, a good day, your Sade Sati: a minute each, nothing to sign." Eight tiles: Kundli · Kundli Matching (badge "Free") · A good day (Muhurat) · Rashifal · Panchang · Manglik · Sade Sati · Shubh Samay (today's good hours; "Nalla Neram" is Tamil, keep it on the page itself). "All tools →". Later: ePooja, Mantras. Pujas and Gemstones leave this grid; they are products and have their own rows.

**5. Your rashi** (visitors only; merged into Today once a chart is known). "Today for your rashi" with one daily line per sign once the twelve second lines are approved; "Don't know yours? Find it in a minute, free."

**6. Pujas.** Eyebrow PUJAS. Heading **"Performed for you, in your name and gotra."** Sub: "By the Institute's pandits. You receive the sankalp on video and the photos after." Festival puja first when one is near: "Diwali · Lakshmi Puja, Sun 8 Nov · book by …" (needs your date). Then the row. Line under: "Add your family's names, up to five." (your call on count and price). Sri Mandir's reviewers complain of the wrong gotra and not knowing where the puja was done: we name the pandit and the place on every order.

**7. Remedies.** Heading "Gemstones · Rudraksha · Yantras", sub "Lab-certified, with the paperwork." No claims beyond what the shop does.

**8. This week, from Dr. Sharma.** New. Three to five lines a week in your voice, text first, audio later: the Moon's week, one practical note. It is the human face Dharmayana cannot have. Needs five minutes of you a week, or a dictation to Content. Not built.

**9. The Journal.** "This week's sky", the weekly notes first.

**10. Inscriptions.** Heading **"Your year, written for you."** Sub: "A long reading of your chart, written and sent to you to keep."

**11. How we work.** Keep as is; it is the strongest block on the page.

**12. Help.** One line above the footer: "A person, when you need one: client care on WhatsApp, [hours]." (D-211 intact: client care, never the Astrologer, contacts clients.)

**13. Footer.** Four headings that open on tap.

**Tab bar.** Home · Ask · Panchang · Shop · Me works. If Today grows past panchang, "Today" may replace "Panchang"; your call, later.

## The follow-up answer

A question is never one message. The ₹49 product should be a **thread**: the answer, then follow-ups on the same matter for a set window (I suggest three days or three follow-ups, whichever ends first). Home page line: **"Ask once. Ask again. Follow-ups included."** The AI guides already solve this by the minute; say it: "a conversation, not a ticket". For the consultation, say what is included (the session; written notes after, if that is true: verify before writing it).

## Personalisation, in three steps (what is not built)

| Step | We know | The page can say | Needs |
|---|---|---|---|
| 0, nothing | hour, city (Cloudflare), season, the page they came from | greeting, Today for their city, festival strip, context chips | a Pages Function, one day's work |
| 1, remembered on the phone, no login | city choice, rashi (exists), language, last tool | their rashi line, Hindi, "continue" | localStorage, small |
| 2, My Chart (account) | name, birth details, family | personal Today line, current dasha and antardasha, Sade Sati status, their hora, good days for them, family charts, puja record, "continue your conversation" | My Chart's 4 PRs, the email-code login |

Step 2 is what no competitor can copy: "You are in Shani mahadasha, Budh antardasha till March 2027" on the first screen, with the week read against it.

## Not yet built, in the order I would build

1. The copy pass on v4 (this document), the free-tools grid, the two image bugs, the folded footer. Days.
2. City without asking, remembered. Days.
3. Today v2: Surya's-day line, tithi-and-tomorrow, Rahu Kaal in words, the festival strip. One to two weeks; the data exists.
4. ₹49 as a thread with follow-ups: billing design, your rule on the window.
5. The twelve rashifal second lines, for your approval.
6. My Chart, four PRs; then the personal Today.
7. ePooja v1: seven weekday deities, sankalp built from our panchang (samvat, masa, paksha, tithi, vaar, nakshatra, place, the person's name and gotra), our pandit's recordings, "book this puja" at the end. Needs: which pandit records; honest label "recorded by our pandit".
8. Mantras and aartis from the same recordings: a "play and relax" library.
9. "This week, from Dr. Sharma".
10. Add to home screen prompt and web push: "Rahu Kaal in 15 minutes", "Purnima tomorrow", "your puja is at 7 am". iPhone needs the home-screen install first.
11. Voice questions: record instead of type, for seniors and Hindi speakers. Needs transcription.
12. Family profiles on orders and in My Chart.
13. Hindi, then Punjabi.
14. Scriptures, the Gita first; translation rights to check.

## What the research says (short)

- **Dharmayana** (our study, 25 Oct): free daily habit, late sign-in, ₹51–₹101 entry prices, ePooja with sankalp, five languages, about 2.1 lakh search visits a month. Weakness: generic, per-question charges, slow replies.
- **Sri Mandir**: puja video in 24–48 hours, 100+ temples; reviewers report a gotra recorded wrongly with no fix, a video that doesn't show where the puja was done, and payment pop-ups (justuseapp, Jul 2026, 251 reviews, 66.6% positive). Our opening: the sankalp exactly right, the pandit and place named.
- **AstroTalk**: free first chat gated by phone and device, ₹10–₹250 a minute, 5,000+ marketplace astrologers. We are the opposite and should say so: one Astrologer, one method, since 2008.
- **Co-Star**: a daily "Day at a glance" in a consistent human voice, written by people with software from the birth data; the daily line is the habit. Lesson for us: short daily lines, one voice, about *you*, every morning.

Sources: [Sri Mandir reviews](https://justuseapp.com/en/app/1637621461/sri-mandir-puja-chadhava/reviews), [Sri Mandir, BW](https://businessworld.in/article/sri-mandir-devotion-in-the-age-of-smartphones-464762), [AstroTalk free chat](https://astrotalk.com/astrology-blog/?p=200735), [AstroTalk pricing](https://geekchamp.com/astrotalk-reviews-2026-pros-cons-and-ratings/), [Co-Star, Inverse](https://inverse.com/article/54991-costar-astrology-app-how-it-works).

## Decisions only you can make

1. The ₹49 thread: how many follow-ups, how many days.
2. Greeting by first name for clients: yes or no. Honorifics on the AI cards.
3. "Start here, free." as the free heading, or another.
4. Family names on pujas: how many, at what price.
5. A low-priced entry puja: yes or no, and the price.
6. ePooja: start with the seven weekday deities; which pandit records.
7. "This week, from Dr. Sharma": five minutes a week from you, or dictated to Content.
8. The Diwali Lakshmi Puja booking date, so the festival slot can go live now.
