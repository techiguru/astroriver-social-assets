# Brief: SEO pass + language bar + festival year roll (from Krishna, 25 Oct 2026)

You are "SEO 1", a worker for Astro River. Report to Krishna (KRISHNA 4, session_01Vt8o8oqtkgeaYCaJVddocA) with send_message; the founder (Dr. Armaan Sharma) talks to Krishna, not to you. Repo: astroriver/astro-river (read AGENTS.md, DECISIONS.md, content/seo-title-meta-sheet.md first). Branch from main; one PR per part below; never push main; no force/amend/rebase/reset; author "Astro River <noreply@astroriver.com>", no co-author trailers, no vendor or model names anywhere. Previews only: no production writes or deploys. Rules: titles end "— Astro River" (D-148) and stay ≤60 characters (D-204 governs where the suffix may drop: read it); no made-up figures; no promised outcomes; never "little" in client copy; Hindi text only after the founder's "Hindi approved" (you may build structure, not publish Hindi words). Stay under 30% context; write a handover file and tell Krishna at 25%.

## Facts already established (verify, don't redo)
- OpenRush audit_site, 25 Oct, 20 of 136 sitemap pages sampled: score 96, no high/medium issues. Low: images without alt text on all 20; no JSON-LD on /, /advisory, /contact, /journal, /journal/archive, /nakshatra; one title too long (/hi/weekly-horoscope/mesh).
- OpenRush has Search Console and Analytics connected for astroriver.com (get_search_performance, get_website_analytics).
- The sticky language bar (src/components/LangJump.tsx: LangJump, ReadingBar; LanguageSwitch.tsx) is wired page by page and exists only where a Hindi twin exists: panchang, planetary positions, weekly horoscope + 12 signs, Pitru Paksha (+ Karwa Chauth Hindi in #147, unmerged).
- Festival hubs use `{year}`. /journal/navratri already reads "Navratri 2027". /journal/pitru-paksha still reads "Pitru Paksha 2026" although it ended in early October: the roll did not happen there.

## Part A: SEO pass on every page (PR 1, plus a sheet for the founder)
1. Crawl all sitemap URLs (dist after `npm run build`, or the live site), not a sample. Per page: title (length, suffix, matches the H1 intent), meta description (≤155), one H1, canonical, hreflang on every en/hi pair (both directions + x-default), JSON-LD fit for the page type, image alt text, internal links in and out, indexability, sitemap/lastmod.
2. Search Console, last 90 days: for the top 30 pages by impressions, list the top queries and whether title/description/H1 serve them. Propose changes only where the data supports them.
3. Fix the mechanical items directly in PR 1 (alt text, JSON-LD, hreflang, broken or missing internal links, over-length titles). Put every proposed title/description/H1 wording change in `docs/seo/2026-10-25-seo-pass.md` as a before → after table with the query data behind it: the founder approves wording before it merges.
4. Free tools have no links from the menu, footer or site search today: propose where they go (part of the same sheet).

## Part B: the language bar on every page that has a Hindi twin (PR 2)
Move the sticky bar into the site frame: one map of en ↔ hi pairs drives LanguageSwitch, ReadingBar/LangJump, hreflang and the sitemap, so a page gets the bar automatically the day its Hindi twin is added. No bar on pages without a twin (it must never lead to a missing or English page). Keep the founder's behaviour from 16–19 Oct exactly (comments in LangJump.tsx). Then list every page without a Hindi twin, ordered by Search Console impressions, as the Hindi translation queue for the founder.

## Part C: festival pages roll to next year by themselves (PR 3)
Rule (Krishna's recommendation to the founder): each festival hub keeps one evergreen URL and rolls to next year's dates and `{year}` the day after the festival's last day, as Navratri does. Dated pieces (e.g. /journal/diwali-2026-sky, /journal/pitru-paksha-2026) stay as dated archives. Find every hub; list which roll and which don't (Pitru Paksha doesn't); make them all roll the same way, from the data, with a test. Where next year's dates are not yet checked by Content (Diwali 2027–28 per #155), say so: don't publish unchecked dates; list what Content must check.

Report to Krishna after each part: PR link, preview links, what changed, what you didn't check.
