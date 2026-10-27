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
      { c: 'g', k: 'Pradosh window', v: '5:40 – 6:57', s: 'sandhya, now', href: '/panchang' },
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
