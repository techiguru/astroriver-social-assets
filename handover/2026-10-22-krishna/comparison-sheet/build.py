import os
D=os.path.dirname(os.path.abspath(__file__))
def tick(c='#7a581b'):
    return f'<svg width="20" height="20" viewBox="0 0 20 20"><circle cx="10" cy="10" r="10" fill="{c}"/><path d="M5.5 10.5l3 3 6-7" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
T1=tick('#b38738'); T2=tick('#4a191c'); DASH='<span class="dash">—</span>'
def row(label, sub, a, b, an='', bn=''):
    s=f'<div class="sl">{sub}</div>' if sub else ''
    a_=a+(f'<div class="note">{an}</div>' if an else ''); b_=b+(f'<div class="note b">{bn}</div>' if bn else '')
    return f'<tr><td class="lab"><b>{label}</b>{s}</td><td class="c">{a_}</td><td class="c b">{b_}</td></tr>'
def grp(t): return f'<tr class="g"><td colspan="3">{t}</td></tr>'
def txt(t): return f'<span class="txt">{t}</span>'
rows=[
 grp('The ceremony and the havan'),
 row('Time at the pujan', '', txt('Up to 3 days'), txt('4–5 days'), '', 'and longer hours each day'),
 row('Ganesh puja and Kalash puja', '', T1, T2),
 row('Navagraha mandal sthapana, each graha invoked one by one', '', T1, T2),
 row('Navagraha stotra and havan for all nine', 'In the Mahapujan each graha receives its own samidha, the wood the tradition gives it', T1, T2, 'One havan for all nine', 'With each graha’s own samidha'),
 row('Each graha’s own beej-mantra jaap', 'Each graha’s own beej mantra is chanted for it', DASH, T2),
 row('Additional Vedic processes', 'For these the tradition turns to Shiva', DASH, T2),
 grp('Your focus'),
 row('Extra attention to the challenge you name', 'The grahas behind it receive extra attention in the jaap', DASH, T2),
 grp('If needed'),
 row('A call with your Astrologer', 'We arrange it, before the puja', DASH, T2),
 grp('In both'),
 row('Sankalp in your name and gotra', 'Each further name ₹2,100', txt('Up to 4 names'), txt('Up to 4 names')),
 row('Food and vastra for the brahmins', '', T1, T2),
 row('Photos and a recording of your sankalp', '', T1, T2),
]
woods=[('Surya','Aak (Arka)'),('Chandra','Palash'),('Mangal','Khair (Khadira)'),('Budh','Apamarg'),('Brihaspati','Peepal (Ashvattha)'),('Shukra','Gular (Udumbara)'),('Shani','Shami'),('Rahu','Durva'),('Ketu','Kusha')]
wood_html=''.join(f'<div class="w"><div class="wg">{g}</div><div class="ww">{w}</div></div>' for g,w in woods)
html=f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
<style>
@page{{size:A4;margin:0}} html,body{{background:#faf6f0;margin:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:Inter,sans-serif;color:#2b2118}}
.page{{padding:9mm 13mm 8mm;box-sizing:border-box}} .pb{{break-before:page}}
.top{{display:flex;align-items:center;gap:12px;margin-bottom:8px}} .top img{{width:44px;height:44px}}
.brand{{font-family:'Playfair Display',serif;font-size:21px;color:#4a191c;font-weight:700}} .since{{font-size:12px;color:#8a7763}}
.kicker{{letter-spacing:.18em;font-size:11.5px;color:#b38738;font-weight:600;text-transform:uppercase}}
h1{{font-family:'Playfair Display',serif;font-size:29px;line-height:1.12;margin:3px 0 6px}}
.sub{{font-size:14px;color:#4a3b2e;line-height:1.45;margin:0 0 10px}}
table{{break-inside:avoid;width:100%;border-collapse:separate;border-spacing:0;background:#fff;border:1.5px solid #ead9bf;border-radius:16px;overflow:hidden}}
th{{font-family:'Playfair Display',serif;text-align:center;padding:10px 8px 9px;font-size:18px;vertical-align:bottom;line-height:1.15}}
th.a{{background:#fbf5ec}} th.b{{background:#4a191c;color:#fff}}
th .p{{font-family:Inter,sans-serif;font-size:22px;font-weight:700;color:#7a581b;margin-top:5px}} th.b .p{{color:#fff}}
th .gst{{font-family:Inter;font-size:11px;color:#8a7763;font-weight:400}} th.b .gst{{color:#e8cfcf}}
th .tag{{display:inline-block;margin-top:7px;font-family:Inter;font-size:10.5px;white-space:nowrap;font-weight:600;border-radius:999px;padding:3px 10px;background:#f3e6d2;color:#7c4a12}}
th.b .tag{{background:#d9a74a;color:#3b1d06}}
td{{padding:5px 12px;border-top:1px solid #f1e6d4;font-size:13.5px;line-height:1.35;vertical-align:middle}}
td.lab{{width:52%}} td.lab b{{font-weight:600}} td.c{{text-align:center;width:24%}} td.b{{background:#f9f2f2}}
.sl{{font-size:12px;color:#7a6654;margin-top:2px;line-height:1.35}}
tr.g td{{background:#f6ecdc;font-weight:700;font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:#7c4a12;padding:6px 12px}}
.note{{font-size:11.5px;color:#8a7763;margin-top:3px;line-height:1.3}} .note.b{{color:#4a191c;font-weight:600}}
.dash{{color:#c9b79f;font-size:16px}} .txt{{font-size:13.5px;font-weight:700}} td.b .txt{{color:#4a191c}}
.diff{{margin:0 0 14px;background:#fff;border:1.5px solid #ead9bf;border-left:5px solid #4a191c;border-radius:12px;padding:12px 16px;font-size:14px;line-height:1.5}}
.diff b{{color:#4a191c}}
h2{{font-family:'Playfair Display',serif;font-size:24px;margin:0 0 10px}}
.woods{{display:grid;grid-template-columns:190px 1fr;gap:16px;background:#fff;border:1.5px solid #ead9bf;border-radius:16px;padding:14px;margin-bottom:14px}}
.woods img{{width:190px;height:190px;object-fit:cover;border-radius:12px;display:block}}
.cap{{font-size:10.5px;color:#8a7763;margin-top:4px}}
.woods p{{font-size:14px;line-height:1.5;margin:0 0 10px}}
.wgrid{{display:grid;grid-template-columns:repeat(3,1fr);gap:7px}}
.w{{background:#fbf5ec;border:1px solid #efe1c9;border-radius:10px;padding:6px 8px}} .wg{{font-size:11px;color:#8a7763}} .ww{{font-size:14px;font-weight:700;color:#7c4a12}}
.choose{{display:grid;grid-template-columns:1fr 1.25fr;gap:14px;margin-bottom:14px}}
.ch{{border-radius:16px;padding:15px 16px;background:#fff;border:1.5px solid #ead9bf}} .ch.b{{border:2px solid #4a191c;background:#f9f2f2}}
.ch .lbl{{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;border-radius:999px;padding:3px 10px;margin-bottom:8px;background:#f3e6d2;color:#7c4a12}}
.ch.b .lbl{{background:#4a191c;color:#fff}}
.ch h3{{font-size:17px;margin:0 0 6px;color:#2b2118}} .ch p{{font-size:14px;line-height:1.5;margin:0}}
.steps{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:14px}}
.st{{background:#fff;border:1.5px solid #ead9bf;border-radius:14px;padding:10px 11px;font-size:13px;line-height:1.4}}
.st .n{{width:26px;height:26px;border-radius:50%;background:#b38738;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;margin-bottom:7px;font-size:13px}}
.ask{{background:#4a191c;color:#fff;border-radius:18px;padding:16px 20px;display:flex;justify-content:space-between;align-items:center;gap:16px}}
.ask .t{{font-family:'Playfair Display',serif;font-size:21px}} .ask .s{{font-size:14px;opacity:.92;margin-top:4px}}
.ask .num{{font-size:18px;font-weight:700;background:#fff;color:#4a191c;border-radius:12px;padding:10px 14px;white-space:nowrap}}
.foot{{font-size:11.5px;color:#8a7763;margin-top:12px;line-height:1.5}}
</style></head><body>
<div class="page">
<div class="top"><img src="https://astroriver.com/astro-river-seal.svg"><div><div class="brand">Astro River Institute</div><div class="since">Jalandhar · since 2008</div></div></div>
<div class="kicker">Navagraha Shanti Puja</div>
<h1>Shanti Pujan or Sampoorna Mahapujan?</h1>
<p class="sub">Both are your own ceremony for all nine grahas, performed in full, in your name and gotra. The Sampoorna Mahapujan takes four to five days and adds the additional Vedic processes, each graha’s own beej-mantra jaap and its own samidha in the havan, and extra attention to the challenge you name.</p>
<table><tr><th style="text-align:left;font-family:Inter;font-size:12px;color:#8a7763;font-weight:600;background:#fff">What you get</th>
<th class="a">Shanti Pujan<div class="p">₹24,800</div><div class="gst">including GST</div><div class="tag">All nine, together</div></th>
<th class="b">Sampoorna Mahapujan<div class="p">₹53,100</div><div class="gst">including GST</div><div class="tag">For a pressing challenge</div></th></tr>
{''.join(rows)}
</table>
</div>
<div class="page pb">
<h2>The wood the tradition gives each graha</h2>
<div class="woods"><div><img src="homam-mandal.jpg"><div class="cap">Representative picture</div></div>
<div><p>In Shanti Pujan, one havan is offered for all nine. In the Mahapujan each graha receives its own samidha in the fire, the wood the tradition gives it:</p>
<div class="wgrid">{wood_html}</div></div></div>
<h2>Which suits you?</h2>
<div class="choose">
<div class="ch"><div class="lbl">Shanti Pujan · ₹24,800</div><h3>When several parts of life feel unsettled at once</h3><p>Or before a new chapter: a move, a venture, a big decision. All nine grahas are honoured together, by the full procedure, for balance and a strong start.</p></div>
<div class="ch b"><div class="lbl">Sampoorna Mahapujan · ₹53,100</div><h3>When one challenge stands out and presses hard</h3><p>Rarely is one graha alone the cause; the tradition holds that results come from how the grahas act on one another. This pujan touches all nine, and the grahas behind the challenge you name receive extra attention in the jaap.</p></div>
</div>
<h2>After you book</h2>
<div class="steps">
<div class="st"><div class="n">1</div><b>Your sankalp</b><br>Choose your pujan and share the names for the sankalp.</div>
<div class="st"><div class="n">2</div><b>Your call</b><br>With the Mahapujan, we arrange your call with your Astrologer: name the one challenge pressing you most, and the muhurat is chosen.</div>
<div class="st"><div class="n">3</div><b>The pujan</b><br>The pandits perform the pujan in your name and gotra. You do not need to be present.</div>
<div class="st"><div class="n">4</div><b>See it done</b><br>Photos and a recording of your sankalp are sent to you after the ceremony.</div>
</div>
<div class="ask"><div><div class="t">Ready to book, or a question first?</div><div class="s">Message our client care on WhatsApp.</div></div><a class="num" href="https://wa.me/917009127641" style="text-decoration:none">+91 70091 27641</a></div>
<div class="foot">astroriver.com/alchemies/navagraha-shanti-puja · We can only pray; the rest is in nature's hands. No result can be promised.</div>
</div></body></html>'''
open(os.path.join(D,'sheet.html'),'w').write(html)
