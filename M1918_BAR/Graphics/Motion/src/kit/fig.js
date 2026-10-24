// simple standing-figure symbol, ~64 px tall, centred on (0,0). bar=true adds a BAR outline across the body
function figSVG(fill,bar){return `<svg width="70" height="80" viewBox="-35 -42 70 80" style="overflow:visible">
<circle cx="0" cy="-26" r="12" fill="${fill}"/><path d="M-17 -8 Q0 -16 17 -8 L19 30 Q0 36 -19 30 Z" fill="${fill}"/>
${bar?'<path d="M-30 18 L32 -14" stroke="#e8c983" stroke-width="5" stroke-linecap="round"/><path d="M14 -4 L18 8" stroke="#e8c983" stroke-width="3"/>':''}</svg>`;}
