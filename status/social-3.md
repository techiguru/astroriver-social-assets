# Social 3 status (IST times). Reports to K25 (session_013noAoBT49Axo8y6ARMsbry) from 9 Nov 2026; before that K24, K23, K22, K15, K14.
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

## Founder rule from 30 Oct (via K14): every new picture is PICHWAI style, and the founder sees it before it is used in a post. Order for every new post: picture first, shown to the founder via K14, then render on template v2, then schedule. (The pictures already made in "painted devotional style" for 6-14 Nov are already scheduled; ask K14 whether they stay.)

## 1 Nov 06:15 IST round (credits reset; 250 for November) — LOG
- 3 x create_post: Sat 14 Nov 10:00 IST Mercury/Venus: IG 6ae68bfc334a8048b5046d08 / FB 6ae68c0a458e0731b6028219 / Pin+GBP 6ae68c147cf483052206f598 (media 6ae09904fa9801d1950104da)
- 1 x fetch_posts (all posts from 1 Nov): all 30 posts for 2 Nov, 4 Nov, 6-12 Nov, 14 Nov are status scheduled with the right execute_time (2 Nov 03:30Z, 4 Nov 03:30Z, 6 Nov 02:30Z and 14:00Z, 7/8/10/11 Nov 02:30Z, 12 Nov 05:30Z, 14 Nov 04:30Z), media counts as planned (carousels 2 and 5 images, cover-only on Pinterest/GBP), no "&amp;", UTM sources correct, the Fri 6 19:30 sell line in the product page's words with "Saturday 7 November, 6:00 pm IST".
- Credits used this round: 4 (3 + 1). Credits left for November: at most 246 (other sessions' calls not counted here).
- Lakshmi 31 Oct re-word: moot (published). Nothing else open.

## Comment-check rule (K14, 1 Nov)
Run the 10:00 IST check each day, skip the 21:00 ones. At most 2 credits per check. Stop the checks as soon as the month's remaining budget is under 60 (15-30 Nov posts still to create). Reply only to a real question from a real person; never to spam; never with a sell line. Log every check here in one line.
Check log:
- 1 Nov 10:00 IST: Lakshmi (31 Oct) and Jupiter (31 Oct) Instagram posts, 0 comments each, 2 credits, nothing to reply.

## 1 Nov evening: Diwali Lakshmi Puja promotion (K15's order, Armaan saw the graphics)
- Mon 2 Nov 11:00 IST feed (IG + FB) 6ae78222b6b4358a2909b739; 11:05 IST IG story 6ae7822bf31ddc77020b65bb. Media 6ae7820a12388b60420092a8 (feed), 6ae7820f56dbf8e1e4017e15 (story). Caption exactly as given (no UTM, 4 hashtags, English only). Fetched back: scheduled, execute_time 05:30Z / 05:35Z. Credits used: 5 (2 uploads, 2 creates, 1 fetch).
- Note: this is a second sell post this week besides Fri 6 Nov 19:30 (lead's call).
- 1 Nov 19:13 UTC: K15 swapped in Armaan's approved version (Vedic Mahalakshmi Puja caption, English + Hindi, new feed/story images). update_post on both posts; fetched back: feed 6ae78222b6b4358a2909b739 (IG+FB, 05:30Z, media 6ae78f40b88732e0d70dc816), story 6ae7822bf31ddc77020b65bb (IG, 05:35Z, media 6ae78f45b79c8237b20aea3c). Old family images no longer used. Credits: 5 (2 uploads, 2 updates, 1 fetch), about 10 for the whole promotion. Tone rule (Armaan): elegant, never bragging, no comparison with puja at home. Fri 6 Nov 19:30 post not changed; sent to K15 for checking.
- 1 Nov 19:47 UTC: Fri 6 Nov 19:30 IST Diwali post fixed (Armaan approved): image replaced with the no-moon version (media 6ae7973c22e7c17f57075455) on IG 6ae091e5ebde36b8b408f614, FB/LinkedIn x2/Tumblr/Threads 6ae091eeb38ce441120c7fd2, Pinterest+GBP 6ae091f8b38ce441120c7fd4; "Can't be home?" paragraph replaced with the Mahalakshmi wording on IG, FB, LinkedIn, Tumblr (Threads and Pinterest/GBP never had it). Fetched back, all scheduled at 14:00Z. Repo copy posts/2026-11-06-diwali-preview/diwali-preview-feed.jpg replaced with the no-moon image (the story file there is not used by a scheduled post). Credits: 5 (1 upload, 3 updates, 1 fetch).
- 2 Nov 10:00 IST: five-days IG carousel (today 09:00) and Lakshmi (31 Oct) IG post, 0 comments each, 2 credits, nothing to reply. Credits used in Nov so far about 24 (estimate, other sessions not counted). Next check 3 Nov 10:00 IST.
- 3 Nov 10:00 IST: Lakshmi puja promotion feed (2 Nov 11:00 IG+FB, 6ae78222b6b4358a2909b739) and five-days IG carousel, 0 comments each, 2 credits, nothing to reply. Nov credits used about 26 (estimate). Next check 4 Nov 10:00 IST.
- 4 Nov 10:00 IST: Dhanteras IG post (4 Nov 09:00, 6ae090da04b8b5760909f976) and Lakshmi puja promotion feed (6ae78222b6b4358a2909b739), 0 comments each, 2 credits, nothing to reply. Nov credits used about 28 (estimate). Next check 5 Nov 10:00 IST.
- 5 Nov 10:00 IST: Dhanteras IG post (6ae090da04b8b5760909f976) and Lakshmi puja promotion feed (6ae78222b6b4358a2909b739), 0 comments each, 2 credits, nothing to reply. Nov credits used about 30 (estimate). Next check 6 Nov 10:00 IST.
- 6 Nov 10:00 IST: Dhanteras day IG post (6 Nov 08:00, 6ae091c604b8b5760909f978) and Lakshmi puja promotion feed (6ae78222b6b4358a2909b739), 0 comments each, 2 credits, nothing to reply. Nov credits used about 32 (estimate). Next check 7 Nov 10:00 IST.
- 7 Nov 10:00 IST: Choti Diwali IG post (7 Nov 08:00, 6ae092028b72263b230b54a7) and Diwali preview IG post (6 Nov 19:30, 6ae091e5ebde36b8b408f614), 0 comments each, 2 credits, nothing to reply. Nov credits used about 34 (estimate). Next check 8 Nov 10:00 IST.
- 8 Nov 10:00 IST: Diwali greeting IG post (8 Nov 08:00, 6ae0977cdd0cfdaaa30eb148) and Diwali preview IG post (6ae091e5ebde36b8b408f614), 0 comments each, 2 credits, nothing to reply. Nov credits used about 36 (estimate). Next check 9 Nov 10:00 IST.

## 8 Nov: K22 leads (session_013noAo94xYcMLRJqNrbmxJX, took over from K21; K22 session exists and works in astroriver/astro-river)
- Task from K22 (founder: "yes schedule goverdhan"): Govardhan post IG+FB Tue 10 Nov 07:30 IST with 2026-11-10_social_govardhan-post_v2.png (sha ba240d3f matches, in posts/drafts/2026-11-10-govardhan-v2/, commit 07e4f34). NOT scheduled yet: caption is in CAPTIONS.md in another repo (astroriver/astro-river, branch krishna-notes); add_repo was refused, so I asked K22 to commit the file here or confirm access. Status/story: HOLD until K22 says. Old Govardhan post (6ae0979917f5fd69af041e16 / 6ae098b3a6a3f3ef090669ff / 6ae098c77706e434b0015a94, 10 Nov 08:00) untouched, asked K22 what to do with it. No ContentStudio calls for this task yet.
- 8 Nov: K22 sent the Govardhan caption as base64; decoded, sha256 804bdfc8...c26d matches. Saved posts/drafts/2026-11-10-govardhan-v2/caption.txt. HOLD: nothing created. K22 is asking the founder: (A) update the old 10 Nov 08:00 post in place (v2 picture, this caption, 07:30, Pinterest/GBP kept) or (B) leave it and add a new one.
- 8 Nov 05:30 UTC: K22 relayed founder's "A haan" + "Status haan". DONE and fetched back (all scheduled, execute_time 02:00Z = Tue 10 Nov 07:30 IST): IG feed 6ae0979917f5fd69af041e16 (updated in place, v2 picture media 6af003c7640ceb38c60b0de2, full EN+HI caption); FB/LinkedIn x2/Tumblr/Threads 6ae098b3a6a3f3ef090669ff (updated in place; FB, LinkedIn, Tumblr full EN+HI; Threads English block only); Pinterest+GBP 6ae098c77706e434b0015a94 (updated in place, English block only, Pin title/link and GBP Learn more link kept). IG story 6af009369797f0e2bb0b3202 and FB story 6af0094688b3ca66e6035cbb (status picture, media 6af0009d803b8d613c088d3a, no caption); both fetched back as post_type story. Status picture sha 4abcfa58 matches K22's. No follow-us line added (caption byte-exact). WhatsApp channel by hand: send raw link on 9 Nov evening. Risk: the feed picture is 1080x1440 (3:4); Instagram feed accepts down to 4:5, so IG may crop or refuse at publish. Credits for this task about 10 (2 uploads, 3 updates, 2 creates, 3 fetches); Nov estimate about 46 used.
- 8 Nov: K23 (session_013noAo7zrU8UcTCkTa6beeX, child of K22) now leads in place of K22; checked the session record. Govardhan report sent to K23. Header lead is now K23.
- 8 Nov: K22 says keep the 1080x1440 Govardhan feed picture (founder approved the art as is; Instagram accepts 3:4). K23 leads; reports and the 9 Nov WhatsApp link go to K23. Reminder set for 9 Nov 18:00 IST to send the WhatsApp raw link (status picture, commit 36fdb5a).
- 8 Nov: K23 asked for a 1080x1350 version of the Govardhan feed picture for the Instagram FEED post 6ae0979917f5fd69af041e16 only, to send link + sha BEFORE swapping. Made it (crop y 70 to 1420; bangle and logo intact), sha 73674023..., committed. NOT swapped yet. All other posts and both stories unchanged.
- 8 Nov: K23 said go. IG feed 6ae0979917f5fd69af041e16 now uses the 1080x1350 Govardhan picture (media 6af00a04e53c7decfc030b12), same caption, 10 Nov 07:30 IST, fetched back. Nothing else changed. Credits 3 (Nov estimate about 49).
- 8 Nov: K23 (founder: social takes too much time and credits): Govardhan CLOSED, no more checks or changes there. Only the 9 Nov evening WhatsApp link, one line. From now: post simply, report in one line, no extra rounds. Asked K23 if the daily 10:00 comment check should stop; skipping the 9 Nov check until answered.
- 8 Nov: K23 changed the comment check from daily to WEEKLY, Mondays 10:00 IST (next: Mon 9 Nov, reminder trig_01FtrH22AQTCfBbK8C4V5kYy stays; each check sets the next Monday). Report to K23 only if a comment is found. Same rules: at most 2 credits, reply only to a real question from a real person, never spam or a sell line, log one line.
- 8 Nov 12:16 UTC: K24 (session_013noAoAyZer6Jkm7tmxuphZ, child of K23) leads; K23 done. Report to K24: the Govardhan WhatsApp link (9 Nov evening, reminder trig_012btF7PbmeVK418shE4ySfe updated to K24) and the Monday comment check (report only if a comment is found).
- 9 Nov 03:53 UTC: K25 (session_013noAoBT49Axo8y6ARMsbry, child of K24) leads. Report to K25: the Govardhan WhatsApp link this evening (reminder trig_012btF7PbmeVK418shE4ySfe updated to K25) and the weekly Monday comment check (only if a comment is found).
- Mon 9 Nov 10:00 IST (weekly): Diwali greeting IG (8 Nov, 6ae0977cdd0cfdaaa30eb148) and Choti Diwali IG (7 Nov, 6ae092028b72263b230b54a7), 0 comments each, 2 credits, nothing to reply, no report to K25 (only if a comment is found). Nov credits used about 51 (estimate). Next check Mon 16 Nov 10:00 IST.
