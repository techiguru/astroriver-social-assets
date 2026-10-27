// Round 4 mockup data. The day is Tuesday 27 October 2026, New Delhi, as astroriver.com/panchang
// and /planetary-positions showed it that morning (Lahiri). In the build each field comes from the
// source named in the README's DATA table; nothing here is hard-coded in the build.
// ?tod=morning|afternoon|evening|night  ?me=1 (with birth details)  ?theme=light|dark (else by time of day)
const Q = new URLSearchParams(location.search);
const TOD = Q.get('tod') || 'morning';
const ME = Q.get('me') === '1';
const THEME = Q.get('theme') || (TOD === 'evening' || TOD === 'night' ? 'dark' : 'light');

const DAY = {
  n: 27, wd: 'Tuesday', wdHi: 'मंगलवार', month: 'October 2026', city: 'New Delhi',
  deity: 'Hanuman', capt: "Mangalavara, Mars's day, is kept for Hanuman.",
  fest: { b: 'Karwa Chauth in 2 days', s: 'Thu 29 Oct · Diwali in 12 days', href: '/journal/karwa-chauth' },
};

// Four parts of day, fixed by code: morning 4–11, afternoon 12–16, evening 17–20, night 21–3.
const TIMES = {
  morning: {
    clock: '9:32', greetHi: 'शुभ प्रभात', greet: 'Good morning.',
    tithiOver: "Today's tithi", tithi: 'Dwitiya', tithiHi: 'द्वितीया',
    tithiP: 'Krishna Dwitiya since 7:01 am, until 4:07 am Wednesday.',
    pic: 'img/hanuman.jpg', picPos: '50% 18%', capt: DAY.capt,
    tiles: [
      { k: 'Nakshatra', v: 'Bharani', s: 'till 3:39 pm, then Krittika', href: '/nakshatra/bharani' },
      { k: 'Sun', v: '6:29 · 5:40', s: 'sunrise · sunset', href: '/panchang' },
      { c: 'g', k: 'Good now', v: 'Char', s: 'till 10:41 am', href: '/muhurat' },
      { c: 'b', k: 'Rahu Kaal', v: '2:53 – 4:16', s: 'this afternoon', href: '/panchang' },
    ],
  },
  afternoon: {
    clock: '1:10', greetHi: 'शुभ दोपहर', greet: 'Good afternoon.',
    tithiOver: "Today's tithi", tithi: 'Dwitiya', tithiHi: 'द्वितीया',
    tithiP: 'Krishna Dwitiya, until 4:07 am Wednesday.',
    pic: 'img/hanuman.jpg', picPos: '50% 18%', capt: DAY.capt,
    tiles: [
      { k: 'Nakshatra', v: 'Bharani', s: 'till 3:39 pm, then Krittika', href: '/nakshatra/bharani' },
      { c: 'g', k: 'Next good window', v: '1:57 – 2:41', s: 'Vijaya Muhurat', href: '/muhurat' },
      { c: 'g', k: 'Good now', v: 'Amrit', s: 'till 1:29 pm', href: '/muhurat' },
      { c: 'b', k: 'Rahu Kaal', v: '2:53 – 4:16', s: 'in 1 h 43 min', href: '/panchang' },
    ],
  },
  evening: {
    clock: '6:05', greetHi: 'शुभ संध्या', greet: 'Good evening.',
    tithiOver: "This evening's tithi", tithi: 'Dwitiya', tithiHi: 'द्वितीया',
    tithiP: 'Krishna Dwitiya, until 4:07 am. Krittika since 3:39 pm.',
    pic: 'img/diya-dusk.jpg', picPos: '50% 60%', capt: 'Light the lamp at sunset, for Hanuman.',
    tiles: [
      { k: 'Sunset', v: '5:40 pm', s: 'Godhuli till 6:06 pm', href: '/panchang' },
      { c: 'g', k: 'Sandhya window', v: '5:40 – 6:57', s: 'now', href: '/panchang' },
      { k: 'Moonrise', v: '6:23 pm', s: 'Moon in Mesha', href: '/panchang' },
      { c: 'g', k: 'Next good window', v: '7:17 – 8:53', s: 'Labh choghadiya', href: '/muhurat' },
    ],
  },
  night: {
    clock: '10:40', greetHi: 'शुभ रात्रि', greet: 'Good night.',
    tithiOver: 'Tomorrow, Wed 28', tithi: 'Tritiya', tithiHi: 'तृतीया',
    tithiP: 'Krishna Tritiya from 4:07 am; Krittika until 1:26 pm.',
    pic: 'img/moon-ghat.jpg', picPos: '50% 40%', capt: 'The Moon moved into Vrishabha at 9:06 pm.',
    tiles: [
      { k: 'Sunrise tomorrow', v: '6:30 am', s: 'Wednesday, for Ganesha', href: '/panchang' },
      { k: 'Moon', v: 'Vrishabha', s: 'since 9:06 pm', href: '/planetary-positions' },
    ],
  },
};
const T = TIMES[TOD];

// Planets now (the /planetary-positions engine). Rx marks vakri as the live page does; it does not
// mark Rahu and Ketu, which always move backwards.
const PLANETS = [
  ['Sun', 'Tula'], ['Moon', TOD === 'night' ? 'Vrishabha' : 'Mesha'], ['Mars', 'Karka'],
  ['Mercury', 'Tula', 1], ['Jupiter', 'Karka'], ['Venus', 'Tula', 1],
  ['Saturn', 'Meena', 1], ['Rahu', 'Kumbha'], ['Ketu', 'Simha'],
];

// "With birth details": an EXAMPLE chart for the mockup (the client-side kundli engine fills it).
const MYCHART = {
  lagna: 'Karka', moon: 'Kumbha', moonHi: 'कुम्भ', nak: 'Dhanishta', pada: 3, moonHouse: 8,
  md: 'Jupiter', mdEnd: 'Aug 2033', ad: 'Saturn', adEnd: 'Feb 2027',
  transit: {
    morning: [10, 'The house of work and standing. Days like this tend to put your work where others see it: finish what will be seen.'],
    afternoon: [10, 'The house of work and standing. Days like this tend to put your work where others see it: finish what will be seen.'],
    evening: [10, 'Until 9:06 pm; then your 11th, the house of gains and friends. A good evening to call someone you have not.'],
    night: [11, 'Since 9:06 pm, and all of tomorrow: the house of gains and friends. What you hoped for tends to come closer.'],
  },
  sadeSati: 'Sade Sati is on: its last phase, until June 2027',
};

// Today's remedy: the day's deity, three small acts (one set for the day, one for the evening).
const REMEDY = {
  day: {
    over: "Today's remedy · Tuesday, for Hanuman", h: 'Three small acts for Mangalavara',
    acts: [
      { b: 'Chant ॐ हं हनुमते नमः', s: 'Om Ham Hanumate Namah, 11 or 108 times, with the player', player: true },
      { b: 'Offer red flowers, or jaggery and roasted chana', s: 'At home or at a Hanuman temple' },
      { b: 'Wear red or saffron', s: 'And keep from meat and alcohol today' },
    ], done: 0,
  },
  evening: {
    over: 'This evening · for Hanuman', h: 'The evening act: the lamp and the aarti',
    acts: [
      { b: 'Light a diya at sunset', s: 'Sesame oil or ghee, before Hanuman; sunset was 5:40 pm' },
      { b: 'Sing the aarti, आरती कीजै हनुमान लला की', s: 'Aarti Kije Hanuman Lala Ki, with the player', player: true },
      { b: 'Offer jaggery and chana, then share them', s: 'As prasad, with the family' },
    ], done: 1,
  },
};
const RM = TOD === 'evening' || TOD === 'night' ? REMEDY.evening : REMEDY.day;
if (TOD === 'night') RM.done = 2;

// ---- Round 4.2 ----
// One campaign at a time, from one config: title, link, end time (a real close: the product's booking close or a
// coupon's valid-until). The top line and the pop-up read only this. No campaign → neither shows.
// ?camp=0 hides it in the mockup; ?popup=1 shows the pop-up as it looks after ~20 s or 50% scroll.
const CAMPAIGN = Q.get('camp') === '0' ? null : {
  title: 'Diwali Lakshmi Puja', href: '/alchemies/diwali-lakshmi-puja-2026',
  ends: '2026-11-07T18:00:00+05:30', endLabel: 'Sat 7 Nov, 6 pm',          // Alchemies: bookings close
  pic: 'img/diwali-lakshmi.jpg', line: 'Performed for you on Sun 8 Nov, in the Lakshmi Puja window, in your name and gotra.',
  button: 'Book the puja',
};
// The mockup's "now" for each time of day, IST (Tue 27 Oct 2026).
const NOW = { morning: '09:32', afternoon: '13:10', evening: '18:05', night: '22:40' }[TOD];
function leftUntil(iso) {
  const ms = new Date(iso) - new Date(`2026-10-27T${NOW}:00+05:30`); if (ms <= 0) return null;
  const d = Math.floor(ms / 864e5), h = Math.floor(ms % 864e5 / 36e5), m = Math.floor(ms % 36e5 / 6e4);
  return d >= 2 ? `${d} days` : d ? `1 day ${h} h` : h ? `${h} h ${m} min` : `${m} min`;   // coarser when far off; always to the real end
}

// Streak: a day counts when at least one act is ticked. One missed day in any 7 does not break it.
// Our own lamp ladder, traditional counts. ?streak=<days>  ?reached=1 (the day a lamp is reached)
const LADDER = [[1, 'The first lamp'], [7, 'A week kept'], [21, 'Three weeks'], [40, 'A mandala, forty days'], [108, 'A mala, a hundred and eight days']];
const STREAK = Q.has('streak') ? +Q.get('streak') : (ME ? 12 : 0);
const REACHED = Q.get('reached') === '1';
if (REACHED && RM.done === 0) RM.done = 1;   // a lamp is reached only on a day with a tick

// ---- Round 4.4: stories. Six circles, built each day from data the site already has; no manual work
// except circle 6 (a short list the office edits; hidden when empty). Rings reset at sunrise for the city.
// ?seen=1 marks some circles seen (they move to the end of the row); ?story=<id>&slide=<n> opens the viewer.
const SEEN = Q.get('seen') === '1' ? ['today', 'planets'] : [];
const STORIES = [
  { id: 'today', label: 'Today', icon: 'img/brass.jpg', slides: [
    { art: 'img/moon-ghat.jpg', over: 'Today · Tue 27 Oct · New Delhi', h: 'Krishna Dwitiya', hHi: 'कृष्ण द्वितीया',
      p: 'Until 4:07 am on Wednesday. The nakshatra is Bharani until 3:39 pm, then Krittika.' },
    { art: 'img/brass.jpg', over: 'The times', h: 'Sun 6:29 am · 5:40 pm',
      rows: [['Rahu Kaal', '2:53 – 4:16 pm', 'bad'], ['Good now', 'Char, till 10:41 am', 'good']] },
    { art: 'img/hanuman.jpg', pos: '50% 20%', over: 'The day', h: 'Mangalavara, kept for Hanuman',
      p: "Mars's day. Tradition keeps it for courage and steady work, and for Hanuman's name.", cta: ['Full panchang →', '/panchang'] },
  ]},
  { id: 'you', label: 'Your day', icon: 'img/learn.jpg', slides: ME ? [
    { art: 'img/moon-ghat.jpg', over: 'Your day · from your chart', h: 'The Moon crosses your 10th house',
      p: 'The house of work and standing. Days like this tend to put your work where others see it: finish what will be seen.' },
    { art: 'img/learn.jpg', over: 'Your dasha now', h: 'Jupiter – Saturn',
      p: 'Jupiter Mahadasha until Aug 2033. Saturn Antardasha until Feb 2027.' },
    { art: 'img/mantra.jpg', over: 'A remedy for your chart', h: 'The Chandra remedy',
      p: 'The Moon in your chart is in Kumbha, in your 8th house. Its remedy is on the remedies page.', cta: ['Your kundli →', '/kundli'] },
  ] : [
    { art: 'img/learn.jpg', over: 'Your day', h: 'Add your birth details',
      p: 'Tell us your birth date, time and place once. Every morning this circle reads your chart.', cta: ['Add my birth details', '/kundli', 'solid'] },
  ]},
  { id: 'fest', label: 'Karwa Chauth', icon: 'img/karwa.jpg', slides: [
    { art: 'img/karwa.jpg', pos: '62% 30%', over: 'In 2 days', h: 'Karwa Chauth', p: 'Thursday 29 October, on Krishna Chaturthi.' },
    { art: 'img/karwa-courtyard.jpg', over: 'Why it matters', h: 'A fast for a long marriage',
      p: 'Married women keep a fast from sunrise to moonrise for their husband\'s long life, and hear the Karwa Chauth katha together.' },
    { art: 'img/karwa-courtyard.jpg', pos: '30% 50%', over: 'What to do', h: 'Sargi, the katha, the Moon',
      p: 'Eat the sargi before sunrise. Hear the katha in the evening. Break the fast after seeing the Moon; the moonrise for your city is on the panchang that day.',
      cta: ['Read the katha →', '/journal/karwa-chauth'] },
  ]},
  { id: 'planets', label: 'Planets', icon: 'img/navagraha-temple.jpg', slides: [
    { art: 'img/navagraha-temple.jpg', over: 'This week in the sky', h: 'Jupiter enters Simha on Saturday',
      p: 'At 12:02 pm on 31 October. It leaves Karka and stays in Simha until 25 January.' },
    { art: 'img/shiva-wide.jpg', pos: '30% 50%', over: 'Moving backwards', h: 'Mercury, Venus and Saturn are retrograde',
      p: 'Seen from here they seem to move backwards. Mercury turns direct on 13 Nov, Venus on 14 Nov, Saturn on 11 Dec.', cta: ['All planets →', '/planetary-positions'] },
  ]},
  { id: 'deity', label: 'Hanuman', icon: 'img/hanuman.jpg', slides: [
    { art: 'img/hanuman.jpg', pos: '50% 20%', over: "Today's deity", h: 'Hanuman', hHi: 'हनुमान', p: 'Tuesday is kept for Hanuman: strength, courage and devotion.' },
    { art: 'img/hanuman.jpg', pos: '50% 45%', over: 'The mantra', h: 'ॐ हं हनुमते नमः', dev: true, p: 'Om Ham Hanumate Namah. Chant it 11 or 108 times.', player: true },
    { art: 'img/diya-dusk.jpg', over: 'The verse · Hanuman Chalisa, opening doha', h: 'बुद्धिहीन तनु जानिके सुमिरौं पवन-कुमार&nbsp;।<br>बल बुधि बिद्या देहु मोहिं हरहु कलेस&nbsp;बिकार&nbsp;॥', dev: true, small: true,
      p: 'Knowing this body is without wisdom, I remember the Son of the Wind. Give me strength, wisdom and learning; take away my troubles and faults.', cta: ['Chant now', '#remedy', 'solid'] },
  ]},
  // Circle 6: only when the office's list has an item. Example item for the mockup.
  { id: 'inst', label: 'Institute', icon: 'img/havan-kund.jpg', slides: [
    { art: 'img/havan-kund.jpg', over: 'From the Institute · 20 Oct 2026', h: 'A Navagraha Shanti Puja',
      p: 'Performed at the Institute. The photos and the sankalp recording go to each family after the ceremony.', cta: ['See the puja →', '/alchemies/navagraha-shanti-puja'] },
  ]},
];
// The festival circle sells only on its last slide, and only when the festival has a puja with a real deadline.
// Karwa Chauth has none in Alchemies, so it ends at the katha. Diwali (?fest=diwali) shows the selling slide:
if (Q.get('fest') === 'diwali') Object.assign(STORIES[2], { label: 'Diwali', icon: 'img/lakshmi-lotus.jpg', slides: [
  { art: 'img/lakshmi-lotus.jpg', over: 'In 12 days', h: 'Diwali', p: 'Sunday 8 November. Lakshmi Puja in New Delhi, 5:54 – 7:50 pm.' },
  { art: 'img/diwali-lakshmi.jpg', over: 'Performed for you', h: 'Diwali Lakshmi Puja',
    p: 'On Sun 8 Nov, in the Lakshmi Puja window, in your name and gotra.', deadline: 'Bookings close Sat 7 Nov, 6 pm', cta: ['Book the puja →', '/alchemies/diwali-lakshmi-puja-2026', 'solid'] },
]});
