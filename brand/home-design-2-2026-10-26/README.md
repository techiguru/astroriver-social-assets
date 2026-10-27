# Home, round 2 (26 Oct 2026)

One more design pass on the combined home (`../home-combined-2026-10-26/`), plus two warm night modes. The founder asked for this pass, and said the blue night was bad.

The screens show the panchang for **Monday 26 October 2026, New Delhi** (astroriver.com/panchang, Lahiri). They were not updated for later days.

## Night mode: two options, the founder's pick is open
- **Night A, lamp-black** (`*-night-a.*`): a warm brown-black, like a room lit by a diya. Cream and gold text, peach-saffron accent. Calmer and lighter. Recommended.
- **Night B, temple maroon** (`*-night-b.*`): the same, on a deep maroon ground. Richer, a little heavier.

Both switch by the moon toggle or from sunset to sunrise. The light mode is the default.

## What else changed from round 1
- No blue anywhere: the AI labels for Vedansh and Tara are maroon, and the Learn band is soft green.
- The texts row (Gita, Hanuman Chalisa, Shiv Chalisa, Aartis) has small pictures instead of coloured blocks.
- "How we work" is one photograph and three numbered lines under "An institute, since 2008", instead of a grid of four boxes.
- Each Learn card has a one-line description.
- Links like "Journal →" no longer wrap.
- The free-tools cards are even.

Unchanged: the layout, the order of sections, all wording, and the Ask price (₹399 crossed out, ₹99 for the first question).

## Files
- `overview.png`: everything on one sheet.
- `home-phone-first-screen-{light,night-a,night-b}.png`, `home-phone-full-*.jpg`: the phone home, first screen and whole page.
- `home-desktop-first-screen-*.png`, `home-desktop-full-{light,night-a}.jpg`: the desktop home.
- `epooja-*`: the ePooja page in each theme.

## Rebuild
`src/` holds `home.html`, `epooja.html`, `theme.css`, `shared.js`, `render.js` and `overview.html`. Set up `src/img/` and `src/fonts/` as in `../home-combined-2026-10-26/HANDOVER.md`. Then run `node render.js <out>` from `src/`. Night B is `?theme=dark&night=maroon`.
