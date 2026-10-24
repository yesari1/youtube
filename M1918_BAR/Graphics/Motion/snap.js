const { chromium } = require('playwright'); const path=require('path');
const [html,out,...ts]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
await p.goto('file://'+path.resolve(html));await p.evaluate(()=>document.fonts.ready);
for(const t of ts){await p.evaluate(tt=>render(tt),+t);await p.screenshot({path:`${out}_${t}.png`});}
await b.close();})();
