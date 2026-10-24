// Stylised side profile of the M1918A2 BAR (muzzle right), 1000 x 200 units. opts: bipod (bool)
function barSVG(opts={}){const bp=opts.bipod!==false;const c=opts.color||'var(--ink)';const w=opts.wood||'#6b5236';
return `<svg viewBox="0 0 1000 200" xmlns="http://www.w3.org/2000/svg" style="overflow:visible">
<g fill="${w}"><path d="M8 66 L60 62 L250 70 L250 108 L214 112 L150 126 L60 140 L8 142 Z"/><path d="M472 74 L650 76 L656 104 L472 108 Z"/></g>
<g fill="${c}">
<rect x="6" y="62" width="10" height="82" rx="3"/>
<path d="M248 60 L478 64 L478 112 L248 112 Z"/>
<path d="M382 112 L438 112 L444 178 L392 180 Z"/>
<path d="M286 112 C286 140 336 142 340 112 L330 112 C328 132 298 132 296 112 Z"/>
<rect x="476" y="96" width="392" height="10" rx="3"/>
<rect x="476" y="76" width="480" height="9" rx="2"/>
<path d="M952 70 L1000 72 L1000 88 L952 90 Z"/>
<rect x="446" y="48" width="14" height="14"/><rect x="986" y="60" width="6" height="12"/>
<path d="M540 64 C548 36 600 36 606 64 L598 64 C594 46 554 46 548 64 Z"/>
${bp?'<path d="M880 86 L892 86 L852 192 L840 192 Z"/><path d="M890 86 L902 86 L942 192 L930 192 Z"/><rect x="826" y="188" width="36" height="7" rx="3"/><rect x="920" y="188" width="36" height="7" rx="3"/>':''}
</g></svg>`;}
