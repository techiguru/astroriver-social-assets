import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import { dirname } from 'path'; import { fileURLToPath } from 'url';
const d=dirname(fileURLToPath(import.meta.url));
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await (await b.newContext()).newPage();
await p.goto('file://'+d+'/sheet.html',{waitUntil:'networkidle'}); await p.waitForTimeout(800);
await p.pdf({path:d+'/Navagraha-Shanti-Pujan-vs-Sampoorna-Mahapujan.pdf',format:'A4',printBackground:true,margin:{top:'0',bottom:'0',left:'0',right:'0'}});
await b.close();
