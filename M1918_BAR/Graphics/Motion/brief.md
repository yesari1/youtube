# Brief — M1918 BAR motion graphics (doc-insert)
- mode: doc-insert, 6 data graphics G01–G06 for the Warfront Archives BAR documentary
- viewer: history/military YouTube audience; must understand each number while it is spoken
- length: real narration slots from word timestamps (G01 15.6 s, G02 19.2, G03 16.2, G04 21.0, G05 18.9, G06 25.7) + 0.5 s handle
- frame rate 60, 1920×1080, H.264 CRF 10 (DaVinci finishing on the PC)
- brand: Warfront Archives dark archival look; palette ink #ece5d3, dim #8f897a, OD #7f8b66, brass #c9a45a, rust #b3362a, bg #0b0a08/#1b1914; fonts Playfair Display (titles), Barlow Condensed (labels/numbers), IBM Plex Mono (axes/footers), all OFL
- facts: section F G-sheets of M1918_BAR_video_package.md (FM 23-15 1943, FM 7-10 1944, T/O F-series 1944, ORO-R-13 1951, production figures) — see facts.json
- toolchain: own HTML + Playwright frame-by-frame kit (kit/), ffmpeg encode
- autonomy: unattended. ChatGPT layers were not available (PC offline), so everything is drawn in code.
