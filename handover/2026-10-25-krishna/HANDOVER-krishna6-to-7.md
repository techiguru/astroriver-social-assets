# Krishna handover: KRISHNA 6 (session_01U5YzkVqyrEsC9FaW2C7NzQ) → KRISHNA 7. 25 Oct 2026, ~12:25 UTC.

Read first: HANDOVER.md top section "FOUNDER RULES REPEATED 25 OCT", then this file. Verify before repeating. Workers can't read this repo: paste brief text into messages.

## Founder state
- Frustrated today (home "just blocks", Journal "still line art... you don't listen... you rush... you could have just asked me"). Keep messages very short; ask him on TASTE before building anything visual; decide everything else yourself.
- He sometimes writes "go" in Krishna's chat: tell him kindly it must be typed in the worker's own chat (safety check ignores relays). He did this once (12:0x UTC).
- He still wrote to KRISHNA 5 after the move; KRISHNA 5 has stopped. If he writes elsewhere, ask him once to use the current Krishna chat.

## DONE 25 Oct ~12:35 UTC (founder typed "go" + "Merge" in Tech 6's chat)
- Production: Diwali product #169 (₹11,700 / $180), dollars at 65 #174, Navagraha Sampoorna further name ₹5,100/$80 #178, Ask #176 (ai-question v1, rates), chat-inference v88 fallback fix #177. All merged in order; main = e27af19; live pages checked by Tech 6.
- Open: signed-in production cart/quote check needs a real cart (production write) → Tech 6 will ask the founder how. ASK_ROUTE → /ask lives only on frozen tech3-mobile-home-v5: switch it there when the home work resumes (nothing on main to change).
- Tech 4 wrongly thinks it should be stopped/consulted; it is stopped. Ignore its reports.

## Waiting on him (production "go" typed in the worker's chat)
1. **Tech 5** session_01BG8HYBFHNDqxq4NBWxVkuZ: #155 Diwali cluster, head a7c6b49 (copy fixes "some silver", "some coriander"; re-stamped 25 Oct 14:30 IST). After merge: retarget #157 Sky Notes to main (due Thu 29 Oct), #173 festival roll live before 30 Oct, #168 with/after the mobile home, #170.
2. (DONE, see above) **Tech 6** session_019uBmXiU2p5AKL24STsCZqD: one go ran the sheet docs/sessions/2026-10-25-tech6-production-run.md (branch fix/chat-fallback-model): Diwali product #169 → its USD file → usd_at_65 → #174 ₹65 restore → step 2c #178 Navagraha Sampoorna further name ₹5,100/$80 (page now shows running total, cart "Further names ×N", checkout "6 names (2 further)") → Tech 2's ai_public_rates → ask files → deploy ai-question → #176 Ask → #177 fallback model fix (deploy chat-inference, merge). If its key can't write, it stops before changing anything and tells him which key to paste. After #176 merges: tell the next Mobile Home chat to switch ASK_ROUTE to /ask (src/lib/home/routes.ts on tech3-mobile-home-v5).
3. **Image style**: sent him two Canva samples (handover/2026-10-25-krishna/image-style-samples/A-painted.png, B-photo.png). I recommended "both" (painted for deities/festival heroes, photos for puja steps/items). No answer yet.
4. **Reference screenshots**: asked for 2–3 screens he loves (Dharmayana or any app) for a home mock-up.

## FROZEN (no code until he approves a full-colour mock-up made in Canva/Adobe)
- Home: Mobile Home 5 stopped at ~25% (handover docs/design/mobile-home/HANDOVER_2026-10-25_mobile-home-5.md; preview tech3-mobile-home-v5 @ 396fbe6 has: route constants, no 404s, AI astrologer row + consultation card after the Journal, "All free tools" button). Next: Krishna makes a picture-led, flowing (not grid-of-boxes) mock-up from his screenshots, shows him, builds only on his yes.
- Journal: Journal Design 1 session_01Tj8od6bPTu8fzVyVYEisjc HOLDING at tech3-journal-mag @ 682e39f. It sent an image-slot list (hero 16:9 1600×900 per piece; figures 4:3 1600×1200; puja card 16:9; share cards 1200×630; Dhanteras Figure B should be the Yama lamp). Rules: licence on file, no AI label (D-191), no text in images, respectful deities, no faces without release. Decisions given: keep JSON-LD "Astro River Institute" + byline "Astro River Journal"; reactions/comments/Listen flagged off; Ask card → ASK_ROUTE.

## Workers
- Tech 3c session_01XJFRDwhTqhYHsckjymksFD: its 19:45 UTC #135 check reports to Krishna. KRISHNA 6's send_later trig_019HLvpmMmNfTuYvuFyM8z15 is DISABLED. **KRISHNA 7: create your own send_later for 19:50 UTC (#135 check via Tech 3c).** Then tell the founder if the panchang flipped at midnight; he types "go" for #135 in Tech 5's chat. Then retire Tech 3c.
- Free Tools 4 session_01BbLq6UMsTH5NcA2ofyaVFH: idle (PRs #171, #172 privacy wording needs him, #175 My Chart needs staging redirect URL).
- Stopped: Tech 4, Mobile Home 5, KRISHNA 5.

## Scheduled tasks
- trig_01Wmt2cfC4td3nwWHpxD1KoD (KRISHNA 5, 19:50): DISABLED by me.
- trig_01GDesXmVE7EXUtPtRxY18bj Tech 3c 19:45: prompt names an old Krishna; Tech 3c told to report to Krishna 6 → tell it Krishna 7.
- trig_019TeN79kjh7ytCRjvNPH76W (1 Dec $4.99 switch) WRONG: once #176 is live, rewrite as a check that prices read ₹399/₹99 and $6.99/$2.99.
- trig_015Pyj7oyhmK24UEYFkqd6LH (9 Nov after Diwali) fires into an old session: rewrite as a check that Diwali rolled to 2027.

## Still open (remind once, low priority)
- Delete old production Supabase key. Staging Supabase redirect URL https://tech3-*.astro-river.pages.dev/** (needed for /ask and /my-chart previews when signed in). #147 Karwa Chauth Hindi only on "Hindi approved" before Wed 28 Oct.
- Login/dashboard (his words 24 Oct): "login screen looks dead. Black and dead... dash, we need a light mode too. Toggleable... discuss login methods in detail... magic link... should be email code instead may be." Plan with him later, mock-up first.
