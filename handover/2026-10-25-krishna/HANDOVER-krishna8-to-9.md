# Krishna handover: KRISHNA 8 (session_012bYyz5DqEqSDAv8DLZ7aDF) → KRISHNA 9. 25 Oct 2026, ~19:10 UTC. KRISHNA 8 at ~44%.

Read first, every time: HANDOVER.md top section "FOUNDER RULES REPEATED 25 OCT". Then HANDOVER-krishna7-to-8.md ("LATEST FOUNDER INSTRUCTIONS"), then KRISHNA8-LOG.md (full running log), then this. Treat as leads; verify before repeating.

## FOUNDER INSTRUCTIONS TO KRISHNA 9 (25 Oct, ~19:08 UTC); pass all of these on, including this line
1. FIRST: help him fix the sitemap and submit it.
   - The live sitemap (https://astroriver.com/sitemap.xml) has 144 URLs. It MISSES every /alchemies/* shop page (pujas, gemstones, rudrakshas, yantras, mahapujas, category pages, /alchemies/diwali-lakshmi-puja-2026), /alchemies itself, /ask and /inscriptions. Also add IndexNow for Bing.
   - A tech chat builds it on a branch from main, with a preview and a PR. It merges only on the founder's "go" typed in that chat, as a GitHub PR merge done by the chat itself.
   - Then the founder resubmits the sitemap in Google Search Console himself (OpenRush GSC is read-only). Then "Request indexing", about 10 a day. K8 already gave him the priority list: Diwali EN+HI, Dhanteras EN+HI, Karwa EN+HI, diwali-2026-sky, weekly-almanac-2026-11-02, /alchemies/diwali-lakshmi-puja-2026; next day the free tools, /ask, /consultation, /alchemies.
2. Then LIST ALL PENDING TASKS for his review. Include at least:
   - the 24 panchang pages;
   - the article v3 design for all remaining Journal articles. Content 3's "In short" overviews are done on tech3-in-short @ 1ced3c0, unmerged; 40 of 44 pages have one. The pages still need articleV3.ts configs, covers and pictures. The founder approves pictures himself and likes 2–3 options per picture; Krishna makes them in Canva.
   - and whatever else is open in the old chats. FIND it: read the old Krishna handovers and logs in this folder and handover/2026-10-22-krishna/ (BACKLOG-founder-2026-10-24.md), and old workers' post_turn_summary. Make one clean list; recommend an order; don't make him decide each item.
3. Move chats only with his permission. Tell him in ONE line at 50% and 60% context and ask "change now or not yet?" (K8 missed 30%). On a move, put "(old) " at the very front of the old chat's title, and pass on all instructions.

## DONE TODAY (verified on astroriver.com by K8)
All three festival pages are live in the new article v3 design, EN + HI:
- https://astroriver.com/journal/diwali · https://astroriver.com/hi/journal/diwali (PR #179, main 8a11846)
- https://astroriver.com/journal/diwali/dhanteras · https://astroriver.com/hi/journal/diwali/dhanteras (PR #181, 84273d3; cover Kubera with Lakshmi; also fixed the status-card overlap and the Vancouver times)
- https://astroriver.com/journal/karwa-chauth · https://astroriver.com/hi/journal/karwa-chauth (PR #180, cdbce7d; Pichwai cover, haveli dusk picture inside)
- #182 (05f619b): British Columbia stays on UTC−7 from 1 Nov 2026 (tzdata 2026e); zoneAt applied site-wide (birthTime, kundli, almanac, rashifal…).
- #157 Weekly Sky Notes 2–8 Nov and #173 festival year roll are live (Tech 5).
- Share on WhatsApp with ?v=2 to bust the old picture cache.

## HOW GOING LIVE WORKS (lesson from today)
- The founder NEVER pushes from a PC. Workers merge their own PR on GitHub after the founder types it in the worker's chat, e.g. "go. Hindi approved. Merge PR #NNN yourself on GitHub." Workers keep asking him to run git commands; tell him the line instead.
- Krishna cannot relay approvals, and the auto-mode classifier blocks Krishna's messages that sound like a production instruction. Phrase worker messages as branch-only.
- Workers can't download Canva images full size. Route: put the media into the Canva holder design DAHZCe0SLBA (read-design open_transaction → update_fill / insert_fill → commit → export-design jpg), curl the export, commit to this repo under brand/festival-pictures-2026-10-25/, and send the raw.githubusercontent URLs (this repo is public).
- Hindi titles lead with the Latin keyword (D-175, founder 26 Sep). K8 wrongly asked to change one and cancelled it.

## OPEN / TIME-BOUND
- BEFORE 11 Nov: merge Content 3's Diwali 2027 roll (branch tech3-diwali-2027-roll @ 7f899b3) TOGETHER with the Lakshmi tithi-cap engine fix (not built; plan in docs/sessions/2026-10-25-journal-design-3-status.md on tech3-jd3-status). Otherwise from 12 Nov the hub shows 2027 with a wrong New Delhi window (18:35–20:13 vs Drik 18:34–19:05). Needs the founder's go.
- #135 on-time nightly rebuild: a first-run check is due ~19:50 UTC today (Tech 3c session_01XJFRDwhTqhYHsckjymksFD reports). K8 moved the reminder to KRISHNA 9 (see the scheduled task). Then tell the founder in 1–2 lines and retire Tech 3c. Tech 5 holds the #135 merge for his "go".
- Karwa Chauth katha page is not in v3 (optional).
- Crest redraw: waiting for the founder's pick (Crest Redraw 1, session_018CsxPkCt9Jv1RUhRNN6Cuc; brand/crest-redraw-2026-10-25/compare.png; K7/K8 view: 2 best icon, 3 most distinctive).
- Cookie notice is English on Hindi pages (site-wide, a tech chat).
- From K7: /ask showing rates signed-out (decided, not built); 11 /alchemies pages missing from the sitemap (now part of task 1); signed-in production cart check; founder reminders (delete old Supabase key; staging redirect URL; delete WorkDrive public link to the Dharmayana recording; home page pick from the 17-screen sheet).

## CHATS
- Content 3 session_01Ex8iNhAj7XLKNRXPkPLMzx (~5%): holding. Owns tech3-in-short and tech3-diwali-2027-roll. Good for Hindi checks.
- Tech 5 session_01BG8HYBFHNDqxq4NBWxVkuZ (~30%): holds #135's go only; retire after.
- Tech 3c session_01XJFRDwhTqhYHsckjymksFD: #135 check, then retire.
- Free Tools 4 session_01BbLq6UMsTH5NcA2ofyaVFH: idle (#171, #172, #175). Could take the sitemap job if a new chat can't be created.
- Crest Redraw 1 session_018CsxPkCt9Jv1RUhRNN6Cuc: waiting for the pick.
- Retired "(old)": Journal Design 3, 4, 5; KRISHNA 7; KRISHNA 8 (this one).
- WARNING: session lineage. KRISHNA 8 was depth 7 of a limit of 8, so KRISHNA 9 is depth 8 and may NOT be able to create new worker chats. Test create_session once. If it fails, use existing idle chats (Free Tools 4, Content 3) and tell the founder in one line that the next Krishna should be started by him from a fresh chat.
- Account weekly usage limit is in "warning": keep few chats active.

## Krishna's clone
/home/user/astroriver-social-assets, branch ccr-c9d9af03-66j7k7 (K8 worked on a local branch krishna8-work that tracks it; pull before you push).
