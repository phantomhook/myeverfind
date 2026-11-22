#!/usr/bin/env python3
"""Motion-graphics hook for the no-voice cut (v0.2, 2026-11-22): a pile of listing windows -> one clean search.
v0.2 (Andrew's notes): every move lands on the music beat (Arpeggiated Mood: 0.5715 s beat, first beat 0.20 s, ~105 BPM),
windows sit in a spaced grid, and the cards use REAL listing photos, titles and prices cropped from the 11/21 screen recording.
Third-party listing photos: review use only until rights are settled.
Run: ~/.venvs/video/bin/python tools/make_hook.py -> working/shoot2/novoice/hook.mp4 (silent, 1920x1080, 30 fps)
"""
import math, random, subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

V = Path(__file__).resolve().parent.parent
WORK = V / "working/shoot2/novoice"; WORK.mkdir(parents=True, exist_ok=True)
OUT = WORK / "hook.mp4"
SCR = V / "working/shoot2/proxies/scr_full.mp4"
SCR_OFFSET = 9.475
BEAT_P, BEAT_OFF = 0.5715, 0.20
def B(k): return BEAT_OFF + BEAT_P * k            # time of beat k (k may be fractional)
W, H, FPS = 1920, 1080, 30
DUR = B(21)                                        # hook ends on beat 21; the next piece dissolves in during the last 0.45 s
NAVY, PANEL, AMBER, IVORY = (13, 27, 42), (27, 44, 64), (244, 163, 98), (244, 240, 232)
GEO, HELV = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf", "/System/Library/Fonts/Helvetica.ttc"
F = lambda p, s: ImageFont.truetype(p, s)
random.seed(11)

# (front-clock time of the frame, column 0-5, crop y0, crop y1, title, price)  columns are 254 px apart from x=198, 235 px wide
PHOTOS = [
    (100, 0, 350, 535, "1993 Rich & Taylor Roy...", "$75,000"),
    (90, 1, 436, 624, "Taylor Baby 305", "$250"),
    (100, 2, 350, 535, "James Olson SJ", "$40,495"),
    (540, 0, 338, 522, "Gibson Custom Shop", "$5,000"),
    (100, 3, 350, 535, "Taylor Custom Gold Label", "$32,999"),
    (90, 4, 436, 624, "Taylor Baby BT1 Left", "$316.70"),
    (540, 1, 338, 522, "Gibson 1964 Trini Lopez", "$5,000"),
    (100, 5, 350, 535, "Olson James Taylor Sig.", "$31,974"),
    (540, 4, 338, 522, "Gibson Custom Shop '59", "$5,000"),
    (90, 0, 436, 624, "Taylor Baby BT1", "$229.99"),
]
TILES_SRC = [(90, 0, 436, 624, "Taylor Baby BT1", "$229.99"), (90, 1, 436, 624, "Taylor Baby 305", "$250"),
             (90, 4, 436, 624, "Taylor Baby BT1 Left", "$316.70")]


def grab(t, col, y0, y1):
    p = WORK / f"fr_{t}.png"
    if not p.exists():
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t - SCR_OFFSET:.3f}", "-i", str(SCR), "-frames:v", "1", str(p)], check=True)
    x0 = 198 + 254 * col
    return Image.open(p).convert("RGB").crop((x0, y0, x0 + 235, y1))


def ease_out(x): x = min(max(x, 0), 1); return 1 - (1 - x) ** 3
def ease_in(x): x = min(max(x, 0), 1); return x ** 3
def seg(t, a, b): return min(max((t - a) / (b - a), 0), 1)


def cover(im, w, h):
    s = max(w / im.width, h / im.height); im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def window(i):
    ph, title, price = grab(*PHOTOS[i][:4]), PHOTOS[i][4], PHOTOS[i][5]
    w, h = 420, 270
    im = Image.new("RGBA", (w + 60, h + 60), (0, 0, 0, 0))
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([34, 40, 34 + w, 40 + h], radius=16, fill=(0, 0, 0, 170))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
    d = ImageDraw.Draw(im); x0, y0 = 30, 30
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=16, fill=PANEL, outline=(60, 82, 108, 255), width=2)
    d.rounded_rectangle([x0, y0, x0 + w, y0 + 40], radius=16, fill=(20, 35, 52, 255))
    d.rectangle([x0, y0 + 24, x0 + w, y0 + 40], fill=(20, 35, 52, 255))
    for k, c in enumerate(((255, 95, 86), (255, 189, 46), (39, 201, 63))):
        d.ellipse([x0 + 16 + k * 22, y0 + 13, x0 + 28 + k * 22, y0 + 25], fill=c)
    d.text((x0 + 90, y0 + 11), title[:30], font=F(HELV, 17), fill=(170, 186, 204, 255))
    pic = cover(ph, 196, 168)
    mask = Image.new("L", pic.size, 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, pic.width - 1, pic.height - 1], radius=10, fill=255)
    im.paste(pic, (x0 + 18, y0 + 62), mask)
    d.text((x0 + 232, y0 + 76), price, font=F(GEO, 38), fill=AMBER + (255,))
    for k, ln in enumerate((150, 120, 90)):
        d.rounded_rectangle([x0 + 232, y0 + 150 + 28 * k, x0 + 232 + ln, y0 + 164 + 28 * k], radius=7, fill=(50, 70, 96, 255))
    return im


def tile(j):
    ph, title, price = grab(*TILES_SRC[j][:4]), TILES_SRC[j][4], TILES_SRC[j][5]
    t = Image.new("RGBA", (380, 330), (0, 0, 0, 0)); d = ImageDraw.Draw(t)
    d.rounded_rectangle([0, 0, 379, 329], radius=18, fill=PANEL, outline=(60, 82, 108, 255), width=2)
    pic = cover(ph, 344, 214)
    mask = Image.new("L", pic.size, 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, pic.width - 1, pic.height - 1], radius=12, fill=255)
    t.paste(pic, (18, 18), mask)
    d.text((22, 250), title, font=F(HELV, 24), fill=(205, 218, 232, 255))
    d.text((22, 282), price, font=F(GEO, 34), fill=AMBER + (255,))
    return t


# staggered 4 / 3 / 3 layout, real gaps (window ~311 px wide at scale 0.74, centres 420 apart), slight rotation and jitter
SPR, POS = [], []
CENTRES = [(330, 440), (750, 440), (1170, 440), (1590, 440), (540, 685), (960, 685), (1380, 685), (540, 930), (960, 930), (1380, 930)]
for i in range(10):
    SPR.append(window(i).rotate(random.uniform(-3, 3), expand=True, resample=Image.BICUBIC))
    POS.append((CENTRES[i][0] + random.randint(-8, 8), CENTRES[i][1] + random.randint(-6, 6)))
TILES = [tile(j) for j in range(3)]
# arrivals on the beat: five on whole beats, five on half beats (the pile-up speeds up)
T_IN = [B(2 + i) for i in range(5)] + [B(7 + 0.5 * i) for i in range(5)]
T_OUT = B(11)                                       # sweep away on beat 11
T_H2A, T_H2B, T_BAR, T_TYPE0 = B(12), B(13), B(14), B(14.5)
T_TILES = [B(17), B(18), B(19)]
T_H1 = B(0)


def centered(im, text, font, y, fill, alpha):
    d0 = ImageDraw.Draw(im); w = d0.textlength(text, font=font)
    tmp = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(tmp).text(((W - w) / 2, y), text, font=font, fill=fill + (int(255 * alpha),))
    im.alpha_composite(tmp)


def frame(t):
    im = Image.new("RGBA", (W, H), NAVY + (255,))
    a1 = ease_out(seg(t, T_H1, T_H1 + 0.35)) * (1 - seg(t, T_OUT - 0.1, T_OUT + 0.3))
    if a1 > 0:
        centered(im, "Listen up, gear aficionados.", F(GEO, 100), 80 + (1 - ease_out(seg(t, T_H1, T_H1 + 0.35))) * 26, IVORY, a1)
    for i in range(10):
        a = ease_out(seg(t, T_IN[i], T_IN[i] + 0.22))
        if a <= 0: continue
        x, y = POS[i]; dx = 0
        if t >= T_OUT:
            k = ease_in(seg(t, T_OUT, T_OUT + 0.7 + 0.025 * i))
            dx = (-1 if x < W / 2 else 1) * k * 2300; y += k * (-90 if i % 2 else 90)
        spr = SPR[i]
        sc = 0.74 * (1 + 0.12 * (1 - a))                              # lands with a small pop
        spr = spr.resize((int(spr.width * sc), int(spr.height * sc)), Image.BICUBIC)
        if a < 1: spr.putalpha(spr.getchannel("A").point(lambda v: int(v * a)))
        im.alpha_composite(spr, (int(x + dx - spr.width / 2), int(y - spr.height / 2)))
    n = sum(1 for x in T_IN if t >= x)                                # tab counter ticks with every window
    if n and t < T_OUT + 0.4:
        ca = min(1, seg(t, T_IN[0], T_IN[0] + 0.2)) * (1 - seg(t, T_OUT - 0.1, T_OUT + 0.35))
        pill = Image.new("RGBA", (W, H), (0, 0, 0, 0)); pd = ImageDraw.Draw(pill)
        last = max([x for x in T_IN if t >= x] or [0]); bump = 1 - seg(t, last, last + 0.18)
        pd.rounded_rectangle([1500 - 8 * bump, 212 - 4 * bump, 1830 + 8 * bump, 280 + 4 * bump], radius=34, fill=(190, 52, 40, int(240 * ca)))
        pd.text((1534, 226), f"{n} tab open" if n == 1 else f"{n} tabs open", font=F(HELV, 36), fill=(255, 255, 255, int(255 * ca)))
        im.alpha_composite(pill)
    if t >= T_H2A:
        centered(im, "Shopping for music gear just got better,", F(GEO, 76), 120, IVORY, ease_out(seg(t, T_H2A, T_H2A + 0.35)))
        centered(im, "and a lot easier.", F(GEO, 76), 215, AMBER, ease_out(seg(t, T_H2B, T_H2B + 0.35)))
    if t >= T_BAR:
        sb = ease_out(seg(t, T_BAR, T_BAR + 0.35))
        bar = Image.new("RGBA", (W, H), (0, 0, 0, 0)); bd = ImageDraw.Draw(bar)
        y0 = 390 + (1 - sb) * 26
        bd.rounded_rectangle([420, y0, 1500, y0 + 92], radius=14, fill=(22, 38, 56, int(255 * sb)), outline=AMBER + (int(255 * sb),), width=3)
        txt = "Taylor guitars"; k = int(len(txt) * seg(t, T_TYPE0, T_TYPE0 + 6 * BEAT_P / 2))
        bd.text((460, y0 + 26), txt[:k], font=F(HELV, 38), fill=IVORY + (int(255 * sb),))
        bd.rounded_rectangle([1330, y0 + 14, 1480, y0 + 78], radius=10, fill=AMBER + (int(255 * sb),))
        bd.text((1360, y0 + 26), "Search", font=F(HELV, 34), fill=NAVY + (int(255 * sb),))
        im.alpha_composite(bar)
    for j in range(3):
        tj = ease_out(seg(t, T_TILES[j], T_TILES[j] + 0.3))
        if tj > 0:
            s = TILES[j].copy(); s.putalpha(s.getchannel("A").point(lambda v: int(v * tj)))
            im.alpha_composite(s, (int(960 + (j - 1) * 430 - 190), int(540 + (1 - tj) * 36)))
    out = Image.new("RGB", (W, H), NAVY); out.paste(im.convert("RGB"), (0, 0))
    return out


def main():
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p", "-an", str(OUT)],
                         stdin=subprocess.PIPE)
    for k in range(int(round(DUR * FPS))):
        p.stdin.write(frame(k / FPS).tobytes())
    p.stdin.close(); p.wait()
    print("OK", OUT, f"{DUR:.3f}s")


main()
