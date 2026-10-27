# Social 3 status, 27 Oct 2026 (IST times). Reports to K14 (session_013noAoAgUW7e4f41MXVDGpR).
ContentStudio workspace 5c5f067f2df1b10c6f490d94. scheduled_at is read as IST. 3 posts per item: IG / FB+LI×2+Tumblr+Threads / Pinterest+GBP.

## BLOCKER: ContentStudio API credits used 250 of 250 (error API_CREDIT_LIMIT_EXCEEDED). Resets 1 Nov 2026. No create/update/fetch works until then or until credits are added in Billing (not done: needs the owner's decision).

## Scheduled (fetched back and verified: Karwa to Dhanteras 4 Nov)
- Thu 29 Oct 07:00 Karwa Chauth: 6adf85f47b0050d6db0d9225 / 6adf85f9f61d9eafc5021f29 / 6ae01c7edb69681c37067ddd (template v2 image)
- Fri 30 Oct 19:30 Ravi Pushya carousel: 6ad7fdbb40f36a78500530a5 / 6ad7fdd7922e969b3705f772 / 6ad7fdc11dba642c0206d3f2
- Sat 31 Oct 11:00 Jupiter into Simha: 6ae065ec97a23903da0f0e73 / 6ae070174c932803910b36cc / 6ae07037ef1b12e4270761a0
- Sat 31 Oct 19:30 Lakshmi Puja: 6ae01e5f115bdf42c80d4b23 / 6ae01e73cf4f4b6de8083a18 / 6ae01e7e7328603a5d044b24  (TEXT RE-WORD TO PRODUCT PAGE WORDS STILL TO DO)
- Mon 2 Nov 09:00 five days of Diwali: 6ae090baa01ce02f32043065 / 6ae090c4a91c3e440707cbef / 6ae090ce36bf48f01105ab75
- Wed 4 Nov 09:00 Dhanteras carousel: 6ae090da04b8b5760909f976 / 6ae090e54d68099a7d03d2d2 / 6ae090f1d9897250c106c54a

## Scheduled, create_post returned success, NOT yet fetched back (no credits)
- Fri 6 Nov 08:00 Dhanteras day: IG 6ae091c604b8b5760909f978 / FB 6ae091d0768ba2139409f573 / Pin+GBP 6ae091db88d28e2cf20c08cf
- Fri 6 Nov 19:30 Diwali preview + sell #2 (product page's words): IG 6ae091e5ebde36b8b408f614 / FB 6ae091eeb38ce441120c7fd2 / Pin+GBP 6ae091f8b38ce441120c7fd4
- Sat 7 Nov 08:00 Choti Diwali: IG 6ae092028b72263b230b54a7 / FB 6ae09478893bb937d5073593 / Pin+GBP 6ae0970a1936ac1bc00d6255
- Sun 8 Nov 08:00 Diwali: IG 6ae0977cdd0cfdaaa30eb148 / FB 6ae0978649e5f86cb30cfe11 / Pin+GBP 6ae09790e5787eeb370768b9
- Tue 10 Nov 08:00 Govardhan: IG 6ae0979917f5fd69af041e16 / FB 6ae098b3a6a3f3ef090669ff / Pin+GBP 6ae098c77706e434b0015a94
- Wed 11 Nov 08:00 Bhai Dooj: IG 6ae098d1eeae909956078f3e / FB 6ae098db4c77d6b77f0ae882 / Pin+GBP 6ae098e5b6dc12faf0046963
- Thu 12 Nov 11:00 Mars into Simha (8:18 pm IST that day): IG 6ae098eeaa22da594d0fecda / FB 6ae098f70275fb0d56056544 / Pin+GBP 6ae09901ea8950645f019568
Execute times expected (UTC): 6 Nov 02:30 and 14:00; 7, 8, 10, 11 Nov 02:30; 12 Nov 05:30.

## NOT scheduled
- Sat 14 Nov 10:00 Mercury (direct Fri 13 Nov 9:24 pm IST) and Venus (direct Sat 14 Nov 5:59 am IST). Approved. Image uploaded to ContentStudio media id 6ae09904fa9801d1950104da, URL https://storage.googleapis.com/contentstudio-media-library-nearline/media_library/5c5f067f2df1b10c6f490d94/uncategorized/original/fZKHisIZb4bRHpw.jpg ; text in posts/drafts/plan-c-v2/captions.md (last section). Needs 3 create_post calls (execute_time 2026-11-14T04:30:00Z).
- Then: nothing in the plan after 14 Nov. No Chhath until the site covers it.

## Repo
- Everything on main. Latest: fb84623 (post images in folders posts/2026-11-*/), templates in build/templates (post.html, make.js with size/gap/widow checks), art in build/templates/art (11 new full-size pictures + 5 Dhanteras).
- Method for generated pictures: Canva generate-image, then read-design open_transaction on scratch design DAHZM5jVX60, edit-design add_page (1456x1088) + insert_fill, commit, export-design jpg, curl (replace &amp; with &).
- Rules: no founder download; AI label off; no picture twice in one carousel or within 7 days.

## Comment checks (send_later, IST): 29 Oct 10:00 trig_01F23z2KfkBsLgYgn24n5dt8 · 17:00 trig_01JMDjhHnokW3RDCWemkWieo · 18:30 trig_01NBXQugpEBCHH28LHc45YWy · 30 Oct 22:00 trig_0128uPz5rwJhKdTXqLYkmxNE · 31 Oct 10:00 trig_01GsgCNmebupJRp7pFxbYsRP · 21:00 trig_01SdGf1RXEebFLFGygdZshFR · 1 Nov 10:00 trig_0197Noe43RJRm2sjqDeoC1LF · 21:00 trig_018JUSL4aiVN1DUojoFnLC2Q · 2 Nov 10:00 trig_015mbKaibWPWvf8epv47WWRw
(Reading comments also costs ContentStudio API credits: none left until 1 Nov, so the 29-31 Oct checks cannot run unless credits are added.)

## K14 decision (27 Oct): buy no credits, WAIT for the 1 Nov reset. No ContentStudio calls until then. K14 wakes me 1 Nov 06:15 IST for the ~7 calls: create Sat 14 (3), one batched fetch-back of all Plan C (1), check the 2 Nov post, Lakshmi 31 Oct re-word is dropped (K14: "our pandits perform" matches the page). 29-31 Oct comment checks paused.

## November credit budget (250 credits per month; every API call counts 1: create_post, update_post, upload_media, fetch_posts, fetch_comments, add_comment, fetch_social_accounts)
| Use | Rule | Budget |
|---|---|---|
| New items | 3 create_post per item (IG, FB group, Pinterest+GBP); an update_post costs 1 per post, so get the image and text right before creating | 90 (about 30 posts' worth) |
| Media | 1 upload_media per image; a carousel costs 5. Upload each picture once and reuse its URL across the 3 posts | 40 |
| Fetch-back | ONE fetch_posts per day at most, batched: verify every post created that day in that single call (never one fetch per post) | 30 |
| Comment checks | counted in: one fetch_comments per post per check, only on posts published since the last check; max 3 checks a day, and none when nothing published | 60 |
| Reserve (fixes, updates) | do not touch unless K14 agrees | 30 |
Rules: log every call in this file the day it is made; at 150 used stop and tell K14; at 220 only fixes. Check the remaining credits on the first call of the day (the error message names the count). Do not run test calls.
