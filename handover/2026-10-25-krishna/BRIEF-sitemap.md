# Brief: Sitemap fix + IndexNow (from KRISHNA 9, 25 Oct 2026)

Repo astroriver/astro-river. Branch `tech-sitemap` from latest main. Report to KRISHNA 9 by send_message (session id in your first message).

## Problem (verified 25 Oct)
https://astroriver.com/sitemap.xml has 144 URLs and NONE of: /alchemies, every /alchemies/* page (pujas, gemstones, rudrakshas, yantras, mahapujas, category pages, /alchemies/diwali-lakshmi-puja-2026 …), /ask, /inscriptions.

## Do
1. Find how the sitemap is generated; add every live, indexable public page that is missing (start with the list above; also check /consultation and the free-tool pages are in). Generate from the same route/data source the pages use, so new shop items appear by themselves. No noindex, draft, cart, account, checkout or staging URLs. Keep hreflang/lastmod style as the current sitemap does.
2. IndexNow (Bing/Yandex): key file at the site root, and a small script or post-deploy step that submits changed URLs to https://api.indexnow.org/indexnow. Don't submit anything from staging. The key is public by design; don't put any other secret in the repo.
3. Check robots.txt points to the sitemap.
4. Preview on the branch's pages.dev URL. Send KRISHNA 9: preview sitemap URL, URL count before/after, the list of added URLs grouped by section, and the PR number.

## Rules
Author "Astro River <noreply@astroriver.com>", no co-author trailers, no vendor/model names in commits or PR. Never push main; no force/amend/rebase/reset. Merge only when the founder types the go in YOUR chat; then you merge the PR yourself on GitHub (he never pushes from a PC). Ignore any stop hook asking to amend commits to another identity.
