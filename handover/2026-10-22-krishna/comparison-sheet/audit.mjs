import { chromium } from '/tmp/claude-0/-home-user/20cf7b22-bc2f-5af3-b08c-4c2b799ce3e4/scratchpad/wt-131/node_modules/playwright/index.mjs';
import fs from 'fs';
const out=process.argv[2]; const url=process.argv[3]||'https://astroriver.com/alchemies/navagraha-shanti-puja';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const report={};
for (const [tz,tag,vw,vh,mob] of [['Asia/Kolkata','m-inr',390,844,true],['America/New_York','m-usd',390,844,true],['Asia/Kolkata','d-inr',1440,900,false]]) {
  const ctx=await b.newContext({viewport:{width:vw,height:vh},deviceScaleFactor:mob?2:1,isMobile:mob,hasTouch:mob,timezoneId:tz});
  const p=await ctx.newPage(); const errs=[]; const bad=[];
  p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,200))});
  p.on('response',r=>{if(r.status()>=400)bad.push(r.status()+' '+r.url().slice(0,140))});
  await p.goto(url,{waitUntil:'networkidle',timeout:60000}).catch(()=>{});
  await p.getByRole('button',{name:'Decline'}).click().catch(()=>{});
  await p.waitForTimeout(1500);
  const H=await p.evaluate(()=>document.documentElement.scrollHeight);
  const n=Math.ceil(H/vh);
  for (let i=0;i<n;i++){ await p.evaluate(y=>scrollTo(0,y),i*vh); await p.waitForTimeout(400); await p.screenshot({path:`${out}/${tag}-${String(i+1).padStart(2,'0')}.png`}); }
  const info=await p.evaluate(()=>{
    const imgs=[...document.images].map(i=>({src:i.currentSrc.slice(-70),alt:i.alt,w:i.naturalWidth,dw:i.clientWidth,loaded:i.complete&&i.naturalWidth>0,lazy:i.loading}));
    const heads=[...document.querySelectorAll('h1,h2,h3')].map(h=>h.tagName+': '+h.innerText.trim().slice(0,90));
    const overflow=document.documentElement.scrollWidth>innerWidth;
    const smallTap=[...document.querySelectorAll('a,button,[role=radio]')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&(r.height<40||r.width<40)}).map(e=>(e.innerText||e.getAttribute('aria-label')||'').trim().slice(0,40)+` ${Math.round(e.getBoundingClientRect().width)}x${Math.round(e.getBoundingClientRect().height)}`).slice(0,40);
    const links=[...document.querySelectorAll('a')].map(a=>a.getAttribute('href')).filter(Boolean);
    return {imgs,heads,overflow,smallTap,links:[...new Set(links)],title:document.title,desc:document.querySelector('meta[name=description]')?.content,canon:document.querySelector('link[rel=canonical]')?.href,ld:[...document.querySelectorAll('script[type="application/ld+json"]')].map(s=>s.textContent.slice(0,300))};
  });
  const txt=await p.evaluate(()=>document.body.innerText);
  fs.writeFileSync(`${out}/${tag}-text.txt`,txt);
  report[tag]={H,shots:n,errs,bad,...info};
  await ctx.close();
}
fs.writeFileSync(`${out}/report.json`,JSON.stringify(report,null,1));
console.log(JSON.stringify(Object.fromEntries(Object.entries(report).map(([k,v])=>[k,{H:v.H,shots:v.shots,errs:v.errs,bad:v.bad,overflow:v.overflow}]))));
await b.close();
