# G01 source

Rebuild: `NODE_PATH=$(npm root -g) node render.js && python3 post.py`

- `g01.html`: the graphic. `render(t)` sets every property from time `t`, so frames are deterministic.
- `render.js`: Playwright/Chromium, 180 frames × 4 sub-frames (180° shutter, motion blur).
- `post.py`: sub-frame averaging, film grain and flicker, H.264 encode (1920×1080, 30 fps, 6.00 s).
- Fonts: Playfair Display, Barlow Condensed, IBM Plex Mono (Google Fonts, SIL Open Font License 1.1; commercial use permitted).
