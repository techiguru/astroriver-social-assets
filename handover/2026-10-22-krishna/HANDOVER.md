# Krishna handover — 22 Oct 2026

The founder (Dr. Armaan Sharma) ended the previous Krishna chat with: "You are hallucinating. Move to a new chat. Your quality has dropped." Treat everything below as a lead to check, not as truth. Verify each fact against the repo, the live site or the chat that owns it before you repeat it to him.

## Who you are

You are Krishna, chief of staff for Astro River. You delegate to the other chats, verify their work yourself, and bring the founder checked links with short steps he can't get wrong. He gets overwhelmed, so keep replies short, decisive and in plain words.

## Standing rules (in force)

**Keys and production**
- Never paste keys or tokens into chat.
- Production database writes, deploys and secrets happen only after the founder types his go in the chat that does the write.
- Staging is allowed under D-200: write the reverse file first, report after, no secrets, no production data.

**Git**
- Author is `Astro River <noreply@astroriver.com>`.
- No co-author trailers, and no vendor or model names anywhere.
- Never push main.
- Use explicit `git add` paths. No force push, amend, rebase or reset.

**Content**
- No made-up figures, reviews or testimonials.
- No promised outcomes: "we can only pray; the rest is in nature's hands."
- Hindi only after he says "Hindi approved".
- Never state how many pandits take part.
- Remove nothing without his say, and don't reduce a page's beauty.
- **The Astrologer never contacts clients directly.** Client care sends nearly all messages and arranges any call (D-211).
- **Never use the word "little"** in client copy (founder, 22 Oct). Use "extra attention".
- **Never use "over five to seven days"** in Maha Yagna copy. He called it bad copy.
- Navagraha Shanti Puja is not for Sade Sati. Talk about how the grahas act on one another, not one planet (D-211).
- AI images are approved only for the Maha Yagna yantra illustration.

## Open work, in order

### 1. Client comparison sheet: Shanti Pujan ₹24,800 vs Sampoorna Mahapujan ₹53,100

**The client**
- A woman born around 1989, unmarried, unhappy in her romantic life.
- Never mention romance or marriage to her.
- She is unsure which to choose. He wants her to choose the Sampoorna Mahapujan without being pushed.
- The sheet goes to her as a PDF from client care, not from the Astrologer.

**His instructions so far**
- Emphasis order: the elaborate process and havan first, then the extra focus on the one challenge she names, then the call with her Astrologer, "if needed".
- Take the rows from the product page's compare table.
- Send a PDF that's comfortable to read, not a long image.
- Don't undersell the ₹24,800 pujan.
- No "little".

**Version 3** is in `comparison-sheet/` (`build.py` writes `sheet.html`; `pdf3.mjs` renders the PDF; `pages.png` is the preview he saw). His only reaction was the "hallucinating" message.

Before showing anything new, check every line against the product page text in `astroriver/astro-river` (`src/data/alchemyPages2026.ts`, `NAVAGRAHA_SHANTI_PAGE`, on PR #165's branch `shop/maha-yagna-page-2026-10-22`). Lines I wrote that are not taken directly from the page:
- "Nine jaaps, one for each graha"
- "Each of the nine called by its own seed mantra, chanted for it on its own"
- "Offered to Shiva, as the tradition does…" (the page says "for these the tradition turns to Shiva")
- "Nine sacred woods in the fire"
- "When life asks for balance"
- the "Our suggestion" label on the Sampoorna box
- "You and up to three family members: four names"

The photo is Adobe Stock (standard licence) and is captioned "Representative picture".

**Client care's number:** +91 70091 27641 (WhatsApp).

### 2. Navagraha Maha Yagna page (₹1,78,200), PR #165

- Branch `shop/maha-yagna-page-2026-10-22`, last head I saw: **5006b35**.
- Preview: https://shop-maha-yagna-page-2026-10.astro-river.pages.dev/alchemies/navagraha-maha-yagna
- Shanti page on the same preview: `/alchemies/navagraha-shanti-puja?way=sampoorna`
- **Shop 2** (`session_01T6iJYRYoGVn98aXneSyNmm`) has my last fix list and owes one push:
  - "little" → "extra attention" (six lines on the Shanti page, including the FAQ "How much" answer);
  - every "over five to seven days" removed (seven lines);
  - two Astrologer lines changed to "we arrange".
  - It should report the head and zero counts for "little" and "over five" in the built HTML.
- After that push:
  1. Audit both pages yourself at 390 and 1440, in ₹ and $ (`comparison-sheet/audit.mjs`: `node audit.mjs <outdir> <url>`; it needs Playwright with `/opt/pw-browsers/chromium`).
  2. Show the founder the preview. He approves with "Approved Maha Yagna".
  3. He types "Go maha yagna production" in **Tech 2b** (`session_01SZLwMdTbwEtv134bZV372T`). Tech 2b applies four production files in this order: six names → extra-name price → sends_items → content clean. Files 1–2 also exist on #164; Tech 2b checked all four gates against production.
  4. Merge #165 at the confirmed head and check both pages live.

**Maha Yagna facts from the founder**
- One havan kund, 5–7 days.
- Each graha's full jaap: 1,30,000 in all, from Surya's 7,000 to Shani's 23,000.
- Dashansh havan, mentioned simply.
- Navagraha daan.
- Up to 6 names; each further name ₹11,000 / $150.
- Everything in the Sampoorna Mahapujan.
- A copper Navagraha yantra, about 3×3 in, made siddha in the yagna, with a raksha sutra. Shipped free in India and abroad, within 7 days of the yagna.
- No food prasad.
- Copy must say the yantra received may differ from the picture.

### 3. Founder's own actions still open (remind him once, not every message)

- Delete the old production key (Tech 2b says it still works).
- Reply "OK" in the social chat to schedule the Facebook Parana post.
- Approve Karwa Chauth EN #145 (about 24 Oct) and Pushya #141.
- Decide 20x Max vs a second account (Settings → Usage).

### 4. Later

- Free tools PR #163 and mobile home #162: his approval, then merge.
- #148, #152, #155, #157, #147: Hindi waits.
- A ₹2.5 lakh seva tier: bhojan through Pingalwara, medicine daan. Needs costs and a CA's view on GST.
- A real yantra photo when one exists.
- After his approval, carry the Shanti page's design and text trims to the other product pages.
- #135 nightly rebuild: production go.
- `ai_public_rates` to production before the V4 flags go on.

## Chats (from list_sessions, 22 Oct)

| Chat | Session |
|---|---|
| Shop 2 (Maha Yagna page) | `session_01T6iJYRYoGVn98aXneSyNmm` |
| Tech 2b (production apply and merges) | `session_01SZLwMdTbwEtv134bZV372T` |
| Shop photos | `session_011MycwjQvAxuxZfeUMZ9ygP` |
| Free Tools 2 | `session_01VgsWuJu98s5YXqBxmk28ZZ` |
| Content 2 | `session_01GeK5g2w5BRStXRrTQMVwWd` |
| Tech 3b | `session_0139zb4exnpjz9AiDQwYnqrh` |
| Mobile Home 2 | `session_01UsCcgx6rS5P66K62QrwHmb` |
| Social chat ongoing | `session_01HusY9Bs36EHSBzhBxNZQvZ` |
| ongoing helper tech 2 | `session_01VkkCyqSfhPjKt3D6ET5qQj` |

The previous Krishna chat was `session_01B52dLVK8GYnx7sYvxS7mVS`. Its transcript holds the full history if a detail is disputed.
