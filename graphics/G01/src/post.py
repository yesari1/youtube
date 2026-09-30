"""Average sub-frames (180-degree shutter motion blur), add animated film grain + light flicker, encode."""
import os, subprocess, numpy as np
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); N, SUB = 180, 4
os.makedirs(f'{D}/out', exist_ok=True)
rng = np.random.default_rng(39)
for i in range(N):
    acc = sum(np.asarray(Image.open(f'{D}/sub/s_{i:03d}_{k}.png').convert('RGB'), np.float32) for k in range(SUB)) / SUB
    g = rng.normal(0, 1, (540, 960)).astype(np.float32)
    g = np.asarray(Image.fromarray(((g * 40) + 128).clip(0, 255).astype(np.uint8)).resize((1920, 1080), Image.BICUBIC), np.float32) - 128
    lum = acc.mean(2, keepdims=True) / 255
    acc = acc + g[..., None] * (0.07 + 0.08 * (1 - lum))          # grain stronger in shadows
    acc *= 1 + 0.012 * np.sin(i * 2.1) + 0.008 * rng.standard_normal()  # gentle flicker
    Image.fromarray(acc.clip(0, 255).astype(np.uint8)).save(f'{D}/out/f_{i:03d}.png')
enc = ['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', f'{D}/out/f_%03d.png']
subprocess.run(enc + ['-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '17', '-preset', 'slow', '-tune', 'grain', '-movflags', '+faststart', f'{D}/G01_Nearly_Half.mp4'], check=True)
Image.open(f'{D}/out/f_{N-1:03d}.png').convert('RGB').save(f'{D}/G01.jpg', quality=95)
