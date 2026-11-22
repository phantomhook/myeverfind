#!/usr/bin/env python3
"""MyEverFind shoot 2: NO-VOICE cut (v0.1, 2026-11-22). Music bed only, screen picture only, text cards carry the story.

Why: Tom does not want to appear on camera (11/22), and the voice track had artifacts. Nothing here uses the camera
picture or any voice audio. Screen recording time = front clock - 9.475 (same master clock as the voice cut).
Run: ~/.venvs/video/bin/python tools/build_shoot2_novoice.py "assets/music/Arpeggiated Mood.m4a" 0.1
Output: previews/20261122_shoot2-novoice-cut_v<VERSION>.mp4 (+ _nomusic dry file in working/shoot2/novoice)
"""
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

V = Path(__file__).resolve().parent.parent
KIT = V.parent / "brand-kit"
MUSIC = Path(sys.argv[1]) if len(sys.argv) > 1 else V / "assets/music/Arpeggiated Mood.m4a"
VERSION = sys.argv[2] if len(sys.argv) > 2 else "0.1"
MUSIC_FROM = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
WORK = V / "working/shoot2/novoice"; WORK.mkdir(parents=True, exist_ok=True)
SCR = V / "working/shoot2/proxies/scr_full.mp4"
OUT = V / f"previews/20261122_shoot2-novoice-cut_v{VERSION}.mp4"
DRY = WORK / "dry.mp4"
SCR_OFFSET = 9.475
W, H = 1920, 1080
VF = f"scale={W}:{H}:flags=lanczos,setsar=1,fps=30"
ENC = ["-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p", "-r", "30", "-an"]
FADE = 0.45
NAVY, AMBER, IVORY, INK = (13, 27, 42), (244, 163, 98), (244, 240, 232), (13, 27, 42)
GEORGIA = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
HELV = "/System/Library/Fonts/Helvetica.ttc"
FRAME_PANEL = (720, 140, 1180, 664)       # right-hand Worth Knowing panel, 1920x1080 padded screen
HILITE_BOX = (190, 626, 722, 664)         # "Showing 24 on this page - from 16,184 results"

# Storyboard. ("hook",) = motion-graphics opener from make_hook.py  |  ("card", seconds, line1, line2)  |  ("intro",) | ("outro", seconds)
# ("clip", front_clock_start, seconds, label, title, {"frame": box, "hilite": (t0, t1)})
# Card words are the site's own headline, on-screen figures, or Tom's phrases. Nothing else is claimed.
BEAT_P, BEAT_OFF = 0.5715, 0.20      # Arpeggiated Mood, measured 11/22: ~105 BPM, first beat 0.20 s
BOARD = [
    ("hook",),                                                         # ends on beat 21 (make_hook.py)
    ("intro", 13),
    ("clip", 24.6, 8, "THE SEARCH", "Type it once", {}),
    ("clip", 41.0, 8, "THE SEARCH", "Reverb and eBay in one list", {}),
    ("clip", 87.5, 8, "THE SORT", "Lowest price first", {}),
    ("clip", 98.5, 7, "THE SORT", "Or highest first: $75,000", {}),
    ("clip", 140.0, 8, "WORTH KNOWING", "Is it a good deal?", {}),
    ("clip", 165.0, 8, "WORTH KNOWING", "What it recently sold for", {"frame": FRAME_PANEL}),
    ("clip", 310.0, 8, "MORE LIKE THIS", "Similar listings, one click", {}),
    ("clip", 360.0, 8, "COMPARE", "Side by side", {}),
    ("clip", 389.5, 8, "COMPARE", "Reverb next to eBay", {}),
    ("clip", 428.0, 7, "THE CLICK-OUT", "Straight to the seller", {}),
    ("clip", 509.0, 8, "OR JUST DESCRIBE IT", "Warm jazz guitar under $5,000", {}),
    ("clip", 524.0, 7, "OR JUST DESCRIBE IT", "Plain English in, jazz guitars out", {}),
    ("clip", 636.0, 5, "NOT JUST GUITARS", "Microphones", {}),
    ("clip", 688.0, 5, "NOT JUST GUITARS", "Casters and dollies", {}),
    ("clip", 721.0, 5, "NOT JUST GUITARS", "Parts", {}),
    ("card", 7, "Free to use.", "No sign-up."),
    ("outro", 7),
]
# every entry after the hook is N beats long; each piece dissolves in during the 0.45 s BEFORE its beat, so the
# cut itself lands on the beat. Card text fades in on the beat.


def run(cmd):
    r = subprocess.run(list(map(str, cmd)), capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"FAILED: {' '.join(map(str, cmd))[:400]}\n{r.stderr[-900:]}")
    return r.stdout


def dur(p):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]))


def lower_card(path, label, title):
    """Same ivory plate, amber bar, navy ink as the voice cut's feature cards; lower right."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    big, small = ImageFont.truetype(GEORGIA, 64), ImageFont.truetype(HELV, 24)
    d = ImageDraw.Draw(im)
    w = int(max(d.textlength(title, font=big) + 110, 380)); h = 140
    x1, y1 = 1824, 952; x0, y0 = x1 - w, y1 - h
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle([x0 + 4, y0 + 8, x1 + 4, y1 + 8], fill=(0, 0, 0, 150))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)))
    d = ImageDraw.Draw(im)
    d.rectangle([x0, y0, x1, y1], fill=IVORY + (255,), outline=INK + (255,), width=3)
    d.rectangle([x0, y0, x0 + 10, y1], fill=(240, 160, 95, 255))
    d.text((x0 + 44, y0 + 20), label, font=small, fill=(150, 88, 30, 255))
    d.text((x0 + 44, y0 + 52), title, font=big, fill=INK + (255,))
    im.save(path)


def full_card(path, l1, l2):
    im = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(im)
    f1, f2 = ImageFont.truetype(GEORGIA, 104), ImageFont.truetype(GEORGIA, 104)
    for y, t, f, c in ((380, l1, f1, IVORY), (520, l2, f2, AMBER)):
        w = d.textlength(t, font=f); d.text(((W - w) / 2, y), t, font=f, fill=c)
    d.rectangle([W / 2 - 60, 690, W / 2 + 60, 696], fill=AMBER)
    im.save(path)


def hilite_png(path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    x0, y0, x1, y1 = HILITE_BOX
    glow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(glow).rounded_rectangle([x0, y0, x1, y1], radius=10, outline=AMBER + (255,), width=10)
    im.alpha_composite(glow.filter(ImageFilter.GaussianBlur(8)))
    ImageDraw.Draw(im).rounded_rectangle([x0, y0, x1, y1], radius=10, outline=AMBER + (255,), width=5)
    im.save(path)


def seg_clip(i, t0, nb, label, title, opt):
    secs = nb * BEAT_P + FADE
    out = WORK / f"seg_{i:02d}.mp4"
    cp = WORK / f"card_{i:02d}.png"; lower_card(cp, label, title)
    if opt.get("frame"):
        fx, fy, fw, fh = opt["frame"]
        base = f"[0:v]crop={fw}:{fh}:{fx}:{fy},scale={W}:{H}:flags=lanczos,setsar=1,fps=30[b]"
    else:
        base = f"[0:v]{VF}[b]"
    c0, c1 = FADE, FADE + min(nb * BEAT_P - 0.5, 3.4)      # card in on the beat, out before the next dissolve
    fc = (base + f";[1:v]format=rgba,fade=t=in:st={c0:.2f}:d=0.25:alpha=1,fade=t=out:st={c1 - 0.25:.2f}:d=0.25:alpha=1[c];"
          f"[b][c]overlay=0:0:eof_action=pass:enable='between(t,{c0:.2f},{c1:.2f})'[v]")
    last, extra = "[v]", []
    if opt.get("hilite"):
        hp = WORK / "hilite.png"; hilite_png(hp); extra = ["-loop", "1", "-framerate", "30", "-t", f"{secs:.2f}", "-i", hp]
        a, b = opt["hilite"]
        fc += f";[v][2:v]overlay=0:0:eof_action=pass:enable='between(t,{a},{b})'[vh]"; last = "[vh]"
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t0 - SCR_OFFSET:.3f}", "-t", f"{secs:.3f}", "-i", SCR,
         "-loop", "1", "-framerate", "30", "-t", f"{secs:.2f}", "-i", cp, *extra,
         "-filter_complex", fc, "-map", last, *ENC, out])
    return out


def seg_card(i, nb, l1, l2):
    secs = nb * BEAT_P + FADE
    out = WORK / f"seg_{i:02d}.mp4"; p = WORK / f"fullcard_{i:02d}.png"; full_card(p, l1, l2)
    run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "30", "-t", secs, "-i", p, "-vf", VF, *ENC, out])
    return out


def seg_hook(i):
    return V / "working/shoot2/novoice/hook.mp4"      # made by tools/make_hook.py (motion graphics, silent)


def seg_intro(i, nb):
    out = WORK / f"seg_{i:02d}.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-i", KIT / "MyEverFind-Intro_v1.0.m4v", "-vf", VF + ",tpad=stop_mode=clone:stop_duration=6",
         "-t", f"{nb * BEAT_P + FADE:.3f}", *ENC, out]); return out


def seg_outro(i, nb):
    secs = nb * BEAT_P + FADE
    out = WORK / f"seg_{i:02d}.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "30", "-t", secs, "-i", KIT / "outro_16x9.png",
         "-vf", VF, *ENC, out]); return out


def main():
    files, plan = [], []
    for i, b in enumerate(BOARD):
        k = b[0]
        files.append(seg_hook(i) if k == "hook" else seg_intro(i, b[1]) if k == "intro" else seg_outro(i, b[1]) if k == "outro"
                     else seg_card(i, *b[1:]) if k == "card" else seg_clip(i, *b[1:]))
        print("seg", i, k, flush=True)
    durs = [dur(f) for f in files]
    hook_len = durs[0]                                   # ends on beat 21
    starts = [0.0, hook_len - FADE]                      # piece 1 finishes dissolving in exactly on that beat
    for k in range(1, len(files) - 1):
        starts.append(starts[k] + BOARD[k][1 if BOARD[k][0] in ("intro", "card", "outro") else 2] * BEAT_P)
    ins = [x for f in files for x in ("-i", f)]
    ch, last = [], "[0:v]"
    for k in range(1, len(files)):
        ch.append(f"{last}[{k}:v]xfade=transition=fade:duration={FADE}:offset={starts[k]:.3f}[x{k}]")
        last = f"[x{k}]"
    total = starts[-1] + durs[-1]
    (WORK / "xfade.txt").write_text(";\n".join(ch))
    run(["ffmpeg", "-v", "error", "-y", *ins, "-/filter_complex", WORK / "xfade.txt", "-map", last, *ENC, DRY])
    # music only: fade in, fade out, one fixed gain (two-pass linear loudnorm, as in the voice cut)
    pre = WORK / "music_pre.wav"
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{MUSIC_FROM}", "-t", f"{total:.2f}", "-i", MUSIC, "-af",
         f"aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=1.5,afade=t=out:st={total - 3.0:.2f}:d=3.0",
         "-c:a", "pcm_f32le", pre])
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(pre), "-af",
                        "loudnorm=I=-14:TP=-2:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True)
    m = json.loads(r.stderr[r.stderr.rindex("{"):r.stderr.rindex("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-2:LRA=11:measured_I={m['input_i']}:measured_LRA={m['input_lra']}:measured_TP={m['input_tp']}"
          f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000")
    OUT.parent.mkdir(exist_ok=True)
    run(["ffmpeg", "-v", "error", "-y", "-i", DRY, "-i", pre, "-map", "0:v", "-map", "1:a", "-af", ln, "-c:v", "copy",
         "-c:a", "aac", "-b:a", "256k", "-shortest", "-movflags", "+faststart", OUT])
    json.dump([dict(i=i, kind=b[0], start=round(s, 2), secs=round(d, 2), src=b[1:] and str(b[1:])[:90])
               for i, (b, s, d) in enumerate(zip(BOARD, starts, durs))], open(WORK / "board.json", "w"), indent=1)
    print(f"OK {OUT.name} {dur(OUT):.1f}s")


main()
