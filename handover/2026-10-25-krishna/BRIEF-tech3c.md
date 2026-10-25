# Tech 3c brief — 25 Oct 2026 (from Krishna)

Repo: astroriver/astro-river. You are Tech 3c. Old Tech 3/3b chats are retired; do not wake them.

## Rules (founder's, all binding)
- Commit author "Astro River <noreply@astroriver.com>"; no co-author trailers; no vendor/model names anywhere.
- Never push main. No force-push, amend, rebase or reset. Bring main in with a merge commit.
- No production writes or deploys. Staging/preview only (D-200 staging rules).
- No made-up figures; no promised outcomes; no "little" in new client copy; titles end "— Astro River", ≤60 chars.
- Hindi pages stay unpublished until the founder types "Hindi approved".
- Token budget: write a handover file and stop at ~25% context. Keep reports short.

## Tasks, in order
0. **#135 on-time nightly rebuild — do this first, only after the founder types "go on-time rebuild" in THIS chat.** He reports (25 Oct) the Vault secret `cf_pages_deploy_hook` is stored and a fresh production key made. Follow the PR body and RB-81 exactly: gate, apply, verify; never print the hook or key. Tonight check the first run (`cron.job_run_details`, `net._http_response`, `computedAt`). Merge #135 only on his word after it's applied.
1. **#155 Diwali cluster** (head c6852ee, base main). Main has moved (#163, #165, #166, #167 merged). Merge main into tech3-diwali, fix conflicts, `npm run build` green, push, confirm the preview (tech3-diwali.astro-river.pages.dev/journal/diwali, /journal/diwali/dhanteras, /journal/diwali-2026-sky) is rebuilt and loads.
2. **SEO check on those three pages with OpenRush** before the founder sees them: target keywords (e.g. "diwali 2026", "lakshmi puja muhurat 2026", "dhanteras 2026"), SERP check, title/description/H1/schema/internal links. Fix plain gaps on the branch; list anything that needs his call.
3. **#157 Weekly Sky Notes 2–8 Nov** (head 4c5236f, stacked on #155). Merge the updated tech3-diwali in, build, confirm preview. Same short SEO pass. Due on the Journal Thu 29 Oct. If #155 is not merged by Tue 27 Oct, prepare a version on main without the three Diwali links.
4. **#147 Karwa Chauth Hindi** (head 8be55c5): merge main in, build, confirm preview. Do not merge.

## Report back (to Krishna, one short message)
Per PR: head SHA, build status, preview URLs, SEO findings fixed / needing his call. Then wait.
