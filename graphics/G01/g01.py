"""G01 'Nearly half' motion data graphic, 1920x1080, 30 fps, 6.0 s (180 frames).
Timing per edit map: 0-2 s Built bar grows; 2-5 s USSR bar grows, bracket after it stops; 5-6 s hold."""
import os, random, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS, N = 1920, 1080, 30, 180
OUT = os.path.dirname(os.path.abspath(__file__))
F = "/usr/share/fonts/truetype/dejavu/"
f_title = ImageFont.truetype(F + "DejaVuSerif-Bold.ttf", 96)
f_sub = ImageFont.truetype(F + "DejaVuSans.ttf", 34)
f_lab = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 44)
f_val = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 52)
f_foot = ImageFont.truetype(F + "DejaVuSans.ttf", 24)

BG, INK, DIM = (22, 23, 20), (232, 226, 210), (150, 146, 134)
BUILT, USSR, AXIS = (122, 132, 104), (176, 58, 46), (80, 80, 72)

X0, X1 = 360, 1720                      # zero and 10,000 on the shared scale
sx = lambda v: X0 + (X1 - X0) * v / 10000
Y_B, Y_U, BH = 430, 650, 110            # bar tops, bar height

def ease(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3

def fade(t, a, d=0.35):
    return max(0.0, min(1.0, (t - a) / d))

# static background with vignette and fixed film grain
bg = Image.new("RGB", (W, H), BG)
vig = Image.new("L", (W, H), 0)
ImageDraw.Draw(vig).ellipse((-300, -250, W + 300, H + 250), fill=255)
vig = vig.filter(ImageFilter.GaussianBlur(220))
bg = Image.composite(bg, Image.new("RGB", (W, H), (8, 8, 7)), vig)
random.seed(1)
grains = []
for k in range(6):
    g = Image.effect_noise((W // 2, H // 2), 18).resize((W, H)).convert("RGB")
    grains.append(g)

def text(d, xy, s, font, col, a, anchor="la"):
    c = tuple(int(BG[i] + (col[i] - BG[i]) * a) for i in range(3))
    d.text(xy, s, font=font, fill=c, anchor=anchor)

for i in range(N):
    t = i / FPS
    im = bg.copy()
    d = ImageDraw.Draw(im)
    a0 = fade(t, 0.0, 0.4)
    text(d, (X0, 170), "Nearly half", f_title, INK, a0)
    text(d, (X0, 290), "P-39 Airacobra, 1940–45", f_sub, DIM, a0)
    # zero axis
    d.line((X0, Y_B - 40, X0, Y_U + BH + 40), fill=AXIS, width=3)

    # Built bar: 0-2 s
    pb = ease(t / 1.8)
    if pb > 0:
        d.rectangle((X0, Y_B, sx(9588 * pb), Y_B + BH), fill=BUILT)
    ab = fade(t, 0.15)
    text(d, (X0 - 24, Y_B + BH / 2), "Built", f_lab, INK, ab, "rm")
    text(d, (X0 + 28, Y_B + BH / 2), "9,558–9,588", f_val, (20, 20, 18) if pb > 0.35 else BG, fade(t, 0.7), "lm")

    # USSR bar: 2-4.2 s grow, bracket 4.2-5 s
    pu = ease((t - 2.0) / 2.2)
    if pu > 0:
        d.rectangle((X0, Y_U, sx(4700 * pu), Y_U + BH), fill=USSR)
    au = fade(t, 2.0)
    text(d, (X0 - 24, Y_U + BH / 2 - 6), "To the", f_lab, INK, au, "rs")
    text(d, (X0 - 24, Y_U + BH / 2 + 6), "USSR", f_lab, INK, au, "ra")
    ak = fade(t, 4.2, 0.5)
    if ak > 0:
        c = tuple(int(BG[j] + (INK[j] - BG[j]) * ak) for j in range(3))
        xa, xb, yb = sx(4400), sx(4950), Y_U + BH + 22
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        od.rectangle((xa, Y_U, xb, Y_U + BH), fill=INK + (int(70 * ak),))
        for yy in (Y_U, Y_U + BH):
            for xx in range(int(xa), int(xb), 18):
                od.line((xx, yy, min(xx + 9, xb), yy), fill=INK + (int(255 * ak),), width=3)
        od.line((xa, Y_U, xa, Y_U + BH), fill=INK + (int(255 * ak),), width=3)
        od.line((xb, Y_U, xb, Y_U + BH), fill=INK + (int(255 * ak),), width=3)
        im.paste(ov, (0, 0), ov)
        d = ImageDraw.Draw(im)
        d.line((xa, yb, xb, yb), fill=c, width=4)
        d.line((xa, yb - 16, xa, yb + 4), fill=c, width=4)
        d.line((xb, yb - 16, xb, yb + 4), fill=c, width=4)
        text(d, (xb + 30, Y_U + BH / 2), "c. 4,400–4,950", f_val, INK, ak, "lm")

    text(d, (X0, 960), "Sources: AAF Statistical Digest; AAF official history; Soviet/Western estimates",
         f_foot, DIM, fade(t, 0.3, 0.6))

    im = Image.blend(im, grains[i % 6], 0.035)
    im.save(f"{OUT}/f_{i:03d}.png")

subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{OUT}/f_%03d.png",
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "14", "-preset", "slow",
                f"{OUT}/G01_Nearly_Half.mp4"], check=True)
if os.environ.get("PRORES"):
  subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{OUT}/f_%03d.png",
                "-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le",
                f"{OUT}/G01_Nearly_Half.mov"], check=True)
Image.open(f"{OUT}/f_{N-1:03d}.png").convert("RGB").save(f"{OUT}/G01.jpg", quality=95)
