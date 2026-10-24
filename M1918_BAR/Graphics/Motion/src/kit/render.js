// node render.js <dir> <html> <dur_s> [buildEnd]  -> <dir>/sub/s_%05d_k.png ; env DSF, FPS, SUBB (subframes during build), FROM, TO
const { chromium } = require('playwright'); const fs=require('fs'), path=require('path');
const [dir, html, dur, buildEnd='10'] = process.argv.slice(2);
const FPS=+(process.env.FPS||60), DSF=+(process.env.DSF||2), SUBB=+(process.env.SUBB||2);
const N=Math.round(+dur*FPS), FROM=+(process.env.FROM||0), TO=+(process.env.TO||N);
(async()=>{ const out=path.join(dir,'sub'); fs.mkdirSync(out,{recursive:true});
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:DSF});
 await p.goto('file://'+path.resolve(dir,html)); await p.evaluate(()=>document.fonts.ready);
 for(let i=FROM;i<Math.min(TO,N);i++){ const t0=i/FPS; const sub=t0<+buildEnd?SUBB:1;
  for(let k=0;k<sub;k++){ const t=(i+(sub>1?(k/sub-0.25)*0.5:0))/FPS;
   await p.evaluate(tt=>render(Math.max(0,tt)),t);
   await p.screenshot({path:path.join(out,`s_${String(i).padStart(5,'0')}_${k}.jpg`),type:'jpeg',quality:94}); } }
 await b.close(); })();
