const cl=x=>Math.max(0,Math.min(1,x));
const seg=(t,a,b)=>cl((t-a)/(b-a));
const outQuint=x=>1-Math.pow(1-x,5), outCubic=x=>1-Math.pow(1-x,3), outExpo=x=>x>=1?1:1-Math.pow(2,-10*x);
const inOutCubic=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2, inOutSine=x=>-(Math.cos(Math.PI*x)-1)/2;
const outBack=(x,s=1.4)=>1+(s+1)*Math.pow(x-1,3)+s*Math.pow(x-1,2);
const lerp=(a,b,p)=>a+(b-a)*p;
const $=id=>document.getElementById(id);
const fmt=n=>Math.round(n).toLocaleString('en-US');
function reveal(el,p,dy=30,dx=0){el.style.opacity=p;el.style.transform=`translate(${(1-p)*dx}px,${(1-p)*dy}px)`;}
function maskIn(el,p){el.style.transform=`translateY(${(1-p)*110}%)`;}
// hash noise for deterministic jitter
function hn(i){const s=Math.sin(i*127.1+311.7)*43758.5453;return s-Math.floor(s);}
// ambient: slow drift + breathing, never frozen
function ambient(t){return {x:Math.sin(t*0.31)*3+Math.sin(t*0.83)*1.2, y:Math.cos(t*0.27)*2+Math.sin(t*0.61)*0.8};}
