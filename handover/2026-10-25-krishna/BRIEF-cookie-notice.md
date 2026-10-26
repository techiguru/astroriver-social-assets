# Brief: cookie notice redesign, ElevenLabs-style (KRISHNA 9, 26 Oct 2026)

Founder (26 Oct): "Use the design that's there at ElevenLabs. This way people will have to select mandatory cookies. Check it carefully."
Reference screenshots (taken by Krishna, 26 Oct, elevenlabs.io, UK locale): cookie-elevenlabs/1-first-layer-390.png, 2-settings-390.png, 3-settings-1280.png.

## What ElevenLabs does (verified)
- First layer: small floating card, bottom (phone: full width with 12px margins; desktop: bottom right ~500px). Title "We value your privacy", 3-line text, buttons: "Reject all" (outline), a sliders icon button (opens settings), "Accept all cookies" (filled). Not a blocking modal; page stays usable.
- Settings layer (same card, grows, scrolls inside): tabs "Cookie settings | About". Categories with a toggle each: Strictly necessary (locked ON, greyed), Preferences, Statistics, Marketing, Unclassified; one-line purpose + "Show details" (lists the actual cookies). Buttons: "Reject all", collapse chevron, "Accept selection".
- Footer link "Cookie Settings" reopens it any time.

## What we copy, and what we must NOT copy
- COPY: the layout, the two layers, the locked "Strictly necessary" toggle, Reject all on the first layer with one click, footer link to reopen, non-blocking card.
- DO NOT COPY: ElevenLabs shows Preferences/Statistics toggles already ON in settings. Ours start OFF (opt-in only; GDPR/ePrivacy and India's DPDP Act need a clear affirmative act). Necessary is the only thing on by default, and it is labelled as always on.
- No "Unclassified" or "Marketing" category unless the site really sets such cookies. List only categories and cookies the site actually uses (audit first: name, provider, purpose, expiry). No counts in brackets unless they are the real counts.
- Until consent: Google Consent Mode v2 defaults denied (analytics_storage, ad_storage, ad_user_data, ad_personalization); nothing non-essential loads. Choices stored with a version and date; ask again after 12 months or when categories change. Reject = same effort as Accept.

## Our version
- Our own words, plain, no legalese; brand colours and fonts of the site (cream card, deep indigo primary button, gold focus), light and dark.
- Hindi pages show the Hindi text (Content 3 drafts; it goes live only after the founder types "Hindi approved").
- Phone: card must not cover more than ~40% of a 390px screen on the first layer; never covers the sticky bottom bar's buttons in a way that blocks them (sit above it).
- Accessibility: focusable, Esc closes settings back to the first layer, labels on toggles, 44px targets.

## Steps
Branch tech3-cookie-v2 from latest main. Audit → build → preview → screenshots 390 + 1280, first layer and settings, EN + HI (HI text placeholder until approved) → PR → report to KRISHNA 9. Founder's go typed in the worker's chat for merge.
