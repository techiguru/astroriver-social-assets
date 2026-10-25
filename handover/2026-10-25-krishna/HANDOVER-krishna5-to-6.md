# Krishna handover: KRISHNA 5 (session_01AwGdXNRGupWicxKPBZ4gbu) → KRISHNA 6. 25 Oct 2026, ~08:30 UTC. KRISHNA 5 at 35%.

Read first: HANDOVER.md, top section "FOUNDER RULES REPEATED 25 OCT", then this file. Verify before repeating. Workers can't read this repo: paste brief text into their messages. Workers' own handovers live in astroriver/astro-river (which you can add_repo; use mcp__github__get_file_contents for single files).

## Founder state (25 Oct)
- Felt "a little lost" and that "so much to do": keep messages SHORT, no lists of decisions, stay quiet unless he's needed. One summary in the evening.
- Approved in my chat: $180/$35 (₹65 list, PR #174); "yes, build Ask a question"; "yes for Diwali if SEO is done properly" (I checked on-page SEO: fine). Production "go"s must be typed by him in the worker's own chat.
- Waiting on him: "go" in Tech 5's chat for #155 Diwali (Tech 5 says ready, re-stamped 25 Oct 14:00 IST; re-stamp again if go comes much later). Staging Supabase redirect URL https://tech3-*.astro-river.pages.dev/** (dashboard; asked). Privacy wording on #172 (free tools) and the home's "Times for your city" paragraph. Reference apps he loves (asked; he pointed to Dharmayana instead).
- His home-page direction: greeting; Instagram-style stories on top; "What would you like to do today?" tile grid; lots to do (ePooja, mantras); feels alive. Dharmayana study: handover/2026-10-25-krishna/competitor-dharmayana/REPORT.md. I recommended mantras be recorded by our own pandits (AI voice only for the personal sankalpa); he hasn't answered.

## Workers (report to Krishna by send_message; tell each the new Krishna id)
- **Mobile Home 5** session_01QwDpBexihqUSXq88frTysr (Opus): building the "alive" home on tech3-mobile-home-v5 (preview https://tech3-mobile-home-v5.astro-river.pages.dev/). My decisions given: weekday devata (Sun Surya, Mon Shiva, Tue Hanuman, Wed Ganesha, Thu Vishnu, Fri Lakshmi, Sat Shani; check its one-liners); verse = Gita Sanskrit + Annie Besant 1905 translation, 30 verses; streak levels Diya 1 / Deepak 7 / Jyoti 21 / Aarti 40 / Akhand Jyoti 108; night greeting "Hello"; Ask tab → chooser (/ask or /lobby); ASK_ROUTE stays /lobby until #176 merges; MY_CHART_ROUTE /kundli until #175 merges; no tile may 404; "one clarification included". When the preview arrives: look at it yourself (playwright 390px), then send the founder the link + a recording.
- **Tech 4** session_01Aw2Ds6FAQoyxMeDsFQ8bm5 at ~43%: told to wrap up (handover docs/sessions/2026-10-25-tech4-handover.md on ai/ask-a-question; push #176 to tech3-ask for a preview; don't deploy the fallback fix). Then start a fresh **Tech 6** from that handover for: the #176 preview check, the chat-inference fallback model-id fix on staging (hard-coded id 404s on staging; production unknown), and the production applies.
  - Production order (all on the founder's "go" typed in the doing chat; the production key is only in Tech 3c's chat so far — Tech 4's permissions blocked production reads):
    - Diwali product #169: Diwali file, Diwali USD file, then #174's ₹65 restore (the gate expects factor 88, no snapshot table; md5s of shop_item_check/shop_quote_for/shop_payment_prepare must match).
    - #176 Ask: Tech 2's ai_public_rates files first, then the two ask files, deploy ai-question with --project-ref, then merge.
  - Hand-set USD kept (Navagraha ways, Maha Yagna $2,025, Diwali). Live site today shows $135/$24 for one-day pujas (I verified on the baglamukhi page).
  - Ask copy approved: "One question, answered in writing"; "Your AI astrologer is reading your chart and writing your answer."; "Ask · ₹99 + GST"; the refund line; "I've passed this to our client care team." Care hand-over: (a) care_requests table + admin list now; (b) Zoho Desk ticket later, when the founder sets the Desk secret.
  - Test accounts tech4-ask-a/b-20261025 (+ dry pairs) left on staging.
- **Tech 3c** session_01XJFRDwhTqhYHsckjymksFD (~34%): asked to do the READ-ONLY production read for #174's gate and send it to Tech 4 + me (no reply yet). Its own scheduled task fires 19:45 UTC for the #135 first-run check; told to report to Krishna. After both: retire it.
- **Tech 5** session_01BG8HYBFHNDqxq4NBWxVkuZ (Opus): merges and deploys. #155 ready for the founder's go. Then retarget #157 (Sky Notes, due on the Journal Thu 29 Oct) to main; #173 festival roll must be live before 30 Oct (needs a Diwali festivalDays entry after #155); #168 SEO must merge with or after the mobile home (its "Free tools" link needs /free-tools from tech3-mobile-home-v5); #170 language bar. Previews: tech3-seo1-part-a / -part-b / -part-c .astro-river.pages.dev.
- **Journal Design 1** session_01Tj8od6bPTu8fzVyVYEisjc (Opus): the magazine-style article template on tech3-journal-mag (pilot: /journal/diwali, /journal/diwali/dhanteras): hero, at-a-glance, jump-to, progress bar, images, boxes, reactions, WhatsApp share, related, CTAs, moderated comments behind a flag. Reuse the Ask card from the home (LiveRows.tsx).
- **Free Tools 4** session_01BbLq6UMsTH5NcA2ofyaVFH: idle, waiting. PRs #171 (A), #172 (B, privacy wording needs the founder), #175 (C My Chart; preview https://tech3-ft-c.astro-river.pages.dev/my-chart; end-to-end save needs the redirect URL + the founder signing in). Rashifal mock E sent to the founder (no reply yet). Before C merges: a production sub_profiles read. D (Manglik, no %) held; F (Varshphal) not built. Note: email sign-in has shouldCreateUser:false → new users only via Google (login-redesign backlog).
- Retired today: SEO 1, Mobile Home 3, Mobile Home 4, Free Tools 3 (titles "(old) …").

## Scheduled
- My send_later trig_01WptNotsjrFz2Zinv9b72a6 fires into KRISHNA 5 at 19:50 UTC (#135 check). Delete it and make your own. KRISHNA 4's trigger trig_01StqhL9hgC5RVz5fem6dozD is disabled. Tech 3c's own trig_01GDesXmVE7EXUtPtRxY18bj fires 19:45 UTC (its prompt names an old Krishna; I told Tech 3c to report to Krishna 5 → tell it Krishna 6).
- After #135's check: tell the founder whether the panchang flipped at midnight; he types "go" for #135 in the chat that merges.

## Deadlines
- Tue 27 Oct: #155 Diwali live (else rebuild #157 without the Diwali links).
- Wed 28 Oct: #147 Karwa Chauth Hindi only if he types "Hindi approved" (not raised today; low priority).
- Thu 29 Oct: #157 Weekly Sky Notes on the Journal.
- Before Fri 30 Oct: #173 merged + deployed.

## Content backlog (no content chat active)
- Nakshatra titles collide with tech3-nakshatra-lords (Uttara Phalguni 61 chars; put the lord's name in the title).
- Pitru Paksha 2027 dates (EN + HI) before it can roll; the 2026 text is replaced by default unless he wants it kept.
