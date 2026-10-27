# Social templates (round-4 identity)

Every Astro River post is made from one template, `post.html`, so the feed looks like the home page:
- the same colour tokens: maroon, gold and warm cream, with Night A for evening and festival-night posts;
- Cormorant for headlines and Inter for text;
- the warm-maroon crest as the signature.

## Make posts
```
./fonts.sh                         # once: fetches the fonts into fonts/
node make.js                       # every post in posts/
node make.js posts/03-puja-diwali-lakshmi.json
```
- **Output:** `out/<post>-<format>.png`, and `out/contact.png` with everything on one sheet.
- **Checks:** `make.js` reports text that runs into the signature, a picture squeezed under 400 px, and, in a story, anything but the picture in the top 250 or bottom 250 px.
- **New post:** copy the nearest file in `posts/`, change the words and the picture, and run it. No design work is needed.

## The post file
```json
{ "template": "festival", "formats": ["feed", "story"],
  "content": { "theme": "night", "art": "karwa.jpg", "pos": "62% 30%",
    "over": "Festival · Thursday 29 October", "h": "Karwa Chauth", "body": "…" } }
```
| field | use |
|---|---|
| `formats` | `feed` 1080×1350, `story` 1080×1920 (safe zones: nothing in the top 250 or bottom 250 px), `square` 1080×1080 |
| `theme` | `light`, or `night` (Night A) for evening and festival-night posts |
| `art`, `pos` | one picture from `art/` and its focus (CSS object-position) |
| `over` | the overline, in small caps: "Kind · day and date". It replaces pill tags |
| `h`, `hHi` | the headline, and an optional Devanagari line beside it |
| `body` | one or two sentences |
| `deadline` | puja or sell posts only: the **real** booking close. No price goes on the image |
| `rows` | carousel inner pages: `[["Fri 6 Nov", "Dhanteras"], …]` |
| `transit` | transit posts: `{ "graha", "from", "to" }`, which draws fine gold line-work (the ecliptic, the two signs, the graha) over the night sky |
| `artHeight` | optional fixed picture height per format, when a page carries rows |

## The five templates
1. **Transit:** a planet enters a sign or turns direct. Night A, the neutral night-sky painting with gold line-work. Never a glyph, and never one graha's image for another.
2. **Festival:** the date, why it matters and what to do, with the festival's painting.
3. **Puja or sell:** the puja's painting or the Institute's ceremony photo, one line, and the real deadline. No price.
4. **Carousel:** the cover (as a festival post), then inner pages with `rows`.
5. **WhatsApp channel:** a square for the feed and a story. Copy: "On WhatsApp" / "Festival dates, before they arrive". Never promise a daily or timed post; the founder posts by hand, before festivals.

## Rules (from the home page)
- One strong picture per post: the deity paintings, the festival art, the Institute's own ceremony photos.
- Generous space, and at most three type sizes: the overline (22), the headline (84, or 72 on the square) and the body (30).
- The signature row (crest, "Astro River Institute", astroriver.com) sits in the same place on every post of a format.
- No pill tags, no decorative lines or wave rules, no watermarks, no orange, no cartoon glyphs.
- No fake urgency: a countdown or deadline is only ever the real close. No invented stock or "N people".
- Dates and times come from the panchang and planetary-positions engines (astroriver.com/panchang, /planetary-positions).

## Art in `art/`
night-sky (transits), karwa, diwali-lakshmi, lakshmi-lotus, dhanteras, brass, hanuman, havan-kund (the Institute's own photograph), seal-warm-maroon (the signature).
