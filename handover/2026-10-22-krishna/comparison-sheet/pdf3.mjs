import { chromium } from '/tmp/claude-0/-home-user/20cf7b22-bc2f-5af3-b08c-4c2b799ce3e4/scratchpad/wt-131/node_modules/playwright/index.mjs';
const d='/tmp/claude-0/-home-user/20cf7b22-bc2f-5af3-b08c-4c2b799ce3e4/scratchpad/compare3';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await (await b.newContext()).newPage();
await p.goto('file://'+d+'/sheet.html',{waitUntil:'networkidle'}); await p.waitForTimeout(800);
await p.pdf({path:d+'/Navagraha-Shanti-Pujan-vs-Sampoorna-Mahapujan.pdf',format:'A4',printBackground:true,margin:{top:'0',bottom:'0',left:'0',right:'0'}});
await b.close();
