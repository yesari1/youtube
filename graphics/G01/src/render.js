// Deterministic frame render: render(t) per sub-frame, 180-degree shutter for motion blur.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const FPS = 30, N = +(process.env.N || 180), SUB = +(process.env.SUB || 4);
const ONLY = process.env.ONLY ? process.env.ONLY.split(',').map(Number) : null;
(async () => {
  const dir = __dirname, out = path.join(dir, 'sub'); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' in {} ? undefined : undefined });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(dir, 'g01.html'));
  await p.evaluate(() => document.fonts.ready);
  for (let i = 0; i < N; i++) {
    if (ONLY && !ONLY.includes(i)) continue;
    for (let k = 0; k < SUB; k++) {
      const t = (i + (SUB > 1 ? (k / SUB - 0.25) * 0.5 : 0)) / FPS;
      await p.evaluate(tt => render(Math.max(0, tt)), t);
      await p.screenshot({ path: path.join(out, `s_${String(i).padStart(3, '0')}_${k}.png`) });
    }
  }
  await b.close();
})();
