#!/usr/bin/env python3
"""Assemble the MyEverFind long-video rough cut from the proxies.   (v0.2, 2026-10-27)

Run with a Python that has numpy + Pillow (the scratch venv does).
Inputs : working/proxies/cam_proxy.mp4 (voice + wide shot), scr_proxy.mp4 (screen),
         working/transcripts/cam_wordlist_dtw.json (word times, camera clock),
         working/audit/cam_16k.wav (energy, used to land cuts in pauses)
Output : previews/<DATED>_long-video_rough-cut_v<VERSION>.mp4 + .captions.srt

Camera clock is the master. Screen picture for camera time t is scr_proxy at t - SCR_OFFSET.
Segments are chosen by WORDS. Each edge is moved into the pause beside the words and keeps up to
0.25 s of room tone, so joints dissolve (picture) and cross-fade (sound) instead of cutting.
Pictures: 'tom' = camera cropped to Tom only (producer out of frame), 'scr' = screen recording.
"""
import json, os, re, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

VERSION = sys.argv[2] if len(sys.argv) > 2 else "0.4"
REFINE = True      # per-segment opt {"refine": True}: window re-transcription trims remnant words at a joint (helps 5 joints, hurt others)
HD = os.environ.get("MEF_HD") == "1"      # 1920x1080 from the 1080p working copies; otherwise 960x540 review proxies
S = 2 if HD else 1
V = Path(__file__).resolve().parent.parent          # Marketing/video
KIT = V.parent / "brand-kit"
OPENER = V / ("previews/20261027_opener-ConceptB_v0.3_1080.mp4" if HD else "previews/20261027_opener-ConceptB_v0.3.mp4")      # Remotion opener B (film/), 14 s
CARDS = V / ("assets/brand/chapter-cards-1080" if HD else "assets/brand/chapter-cards")
MUSIC = Path(sys.argv[1]) if len(sys.argv) > 1 else V / "assets/music/MEF Babs.m4a"      # Suno free tier, 158.4 s, 86 BPM: REVIEW USE ONLY (non-commercial)
MUSIC_OFFSET = 0.0        # seconds the track is delayed in the cut; slide to move its accents
MUSIC_LOOP_FROM = float(sys.argv[3]) if len(sys.argv) > 3 else 22.3    # 8 bars at 86 BPM: where the track re-enters when the cut outlasts it
NAME_CARD = V / "assets/brand/lower-third-tom-babula-right.png"   # moved to the right at Andrew's request
WORK = V / "working" / "rough"
WORK.mkdir(parents=True, exist_ok=True)
CAM, SCR = ((V / "working/proxies/cam_hi.mp4", V / "working/proxies/scr_hi.mp4") if HD else
            (V / "working/proxies/cam_proxy.mp4", V / "working/proxies/scr_proxy.mp4"))
OUT = V / (f"exports/20261027_myeverfind-long-video_v{VERSION}_1080p.mp4" if HD else f"previews/20261027_long-video_rough-cut_v{VERSION}.mp4")
DRY = WORK / (OUT.stem + "_nomusic.mp4")
SCR_OFFSET = 21.28          # measured 21.271 .. 21.290 over the take (Phase 1)
W, H = 960 * S, 540 * S
CRF = "18" if HD else "22"
FONT = "/System/Library/Fonts/Helvetica.ttc"
TOM_CROP = f"crop={560 * S}:{315 * S}:{80 * S}:{110 * S},scale={W}:{H}:flags=lanczos"      # in the 960x540 camera proxy: Tom, laptop, no producer

# (beat, hint_s, first words, last words, picture[, {"cut": [(cam_a, cam_b)]}])  cut = show Tom over the screen
# Worth Knowing: the panel sits flush right (x 710-960). Right-aligned crop keeps its whole width; the top of it
# (features, price, sales chart) is what Tom talks about. Compare and More like this use the full frame.
FRAME_PANEL = tuple(v * S for v in (310, 40, 650, 365))
SEGS = [
    ("1 hook", 30, "i always look", "multiple marketplaces", "tom"),
    ("1 hook", 37, "what if i could simplify this", "simplify this", "tom"),
    ("1 hook", 40, "so that you could do one search", "existed before", "tom"),
    ("INTRO", 0, None, None, None),
    ("3 search", 49.5, "so i created", "across the entire market", "scr"),
    ("3 search", 65, "for example", "search for that", "scr"),
    ("3 search", 78, "find results that meet that requirement", "that requirement", "scr"),
    ("3 search", 85, "now of course thats one thing", "more valuable as a buyer", "scr"),
    ("4 questions", 95, "i want to see listings", "important in my decision", "tom"),
    ("4 questions", 109, "so having all those things in mind", "buyer might have", "tom", {"refine": True}),
    ("5 worth knowing", 154, "a couple of other things i might want to do", "brings up a panel", "scr"),
    ("5 worth knowing", 185, "features at a glance", "read through all the listing", "scr", {"frame": FRAME_PANEL}),
    ("5 worth knowing", 192, "and then the current price", "listings that have sold", "scr", {"frame": FRAME_PANEL}),
    ("5 worth knowing", 216, "and if i click on one of these dots", "details of that listing", "scr",
     {"cut": [(216.2, 218.7)], "frame": FRAME_PANEL}),                          # unintended right-click menu on screen
    ("5 worth knowing", 233, "and thats all still within your site", "within your site", "scr", {"frame": FRAME_PANEL}),
    ("6 compare", 310, "i have a compare functionality", "click compare on this item", "scr",
     {"refine": True, "cut": [(311.8, 313.6)]}),                          # unintended right-click menu on screen
    ("6 compare", 320, "this one looks interesting", "compare these", "scr"),
    ("6 compare", 329, "and as i click compare", "we dont insert it", "scr", {"refine": True}),
    ("7 click out", 374, "at any time i can click out", "one of the marketplaces", "scr"),
    # "free, no account" moved out of the long video until Tom confirms where saved searches are stored (flag F4)
    ("8 plain english", 421, "we also do a lot of conversational search", "conversational search", "scr", {"refine": True}),
    ("8 plain english", 458.4, "how many results did it come back with", "183 results", "scr"),
    ("9 more like this", 476, "to see more like this", "focused on 1959 strats", "scr", {"refine": True}),
    ("9 more like this", 489, "and this is the item at the top", "just like this", "scr"),
    ("11 close", 1050, "for the buyer", "decision on that purchase", "tom"),
    ("11 close", 1099, "and if people have questions", "myeverfind.com", "tom", {"min_out": 1.25}),
    ("OUTRO", 0, None, None, None),
]
SLATE_END = 14.0
SLATE_TEXT = ("ANIMATION PLACEHOLDER", "Pen-and-ink problem shot (Phase 5)",
              "A musician, ten browser tabs, listings that disagree")
LOWER_THIRD = (14.6, 19.6)
QUERY_CARD = ("Ask in plain English:", "what guitar did Hendrix play?")   # shown over beat 8
FIX = [(r"\bmy ever ?find\b", "MyEverFind"), (r"\bD 18\b", "D-18")]
QUIET = -33.0               # dB (room tone about -42, speech above -25)
MAX_HANDLE, MAX_XFADE = 0.25, 0.20


def run(cmd):
    r = subprocess.run(list(map(str, cmd)), capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"FAILED: {' '.join(map(str, cmd))[:400]}\n{r.stderr[-900:]}")
    return r.stdout


def vdur(p):
    return float(run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=duration",
                      "-of", "csv=p=0", p]).strip().strip(","))


def dur(p):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]))


def load_db():
    import wave
    w = wave.open(str(V / "working/audit/cam_16k.wav"))
    a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    n = 160
    env = np.sqrt(np.convolve(a * a, np.ones(3 * n) / (3 * n), "same")[::n])
    return 20 * np.log10(env + 1e-6)


def norm(w):
    return re.sub(r"[^a-z0-9]", "", w.lower())


def find(words, phrase, hint, after=0):
    toks = [norm(t) for t in phrase.split()]
    best = None
    for i in range(after, len(words) - len(toks)):
        if all(norm(words[i + k][1]) == toks[k] for k in range(len(toks))):
            if best is None or abs(words[i][0] - hint) < abs(words[best][0] - hint):
                best = i
            if words[i][0] > hint + 40:
                break
    if best is None or abs(words[best][0] - hint) > 40:
        sys.exit(f"phrase not found near {hint}: {phrase!r}")
    return best, best + len(toks) - 1


def pauses(db, t0, t1, thr=-31.0, min_frames=5):
    """(start, end) in seconds of runs below thr, at least min_frames * 10 ms long, inside [t0, t1]."""
    out, run = [], None
    for k in range(int(t0 * 100), int(t1 * 100)):
        if db[k] < thr:
            run = run or k
        elif run is not None:
            if k - run >= min_frames:
                out.append((run / 100, k / 100))
            run = None
    return out


def edge_in(db, s):
    """Pause before the first word. Aligner times drift by up to about 0.7 s, so take the pause whose end
    lies nearest the word's start; keep up to MAX_HANDLE of its room tone. Returns (cin, quiet_kept)."""
    ps = pauses(db, s - 1.0, s + 0.1)
    if not ps:
        k = int((s - 0.3) * 100) + int(np.argmin(db[int((s - 0.3) * 100):int((s + 0.05) * 100)]))
        return k / 100, 0.0
    a, b = min(ps, key=lambda p: abs(p[1] - s))
    cin = max(a, b - MAX_HANDLE)
    return cin, b - cin


def edge_out(db, ws, word, min_off=0.2):
    """Pause after the last word. The aligner's word END includes the pause (and sometimes more words), so
    estimate the end from the word's start and length, then take the nearest pause."""
    est = ws + 0.06 * len(re.sub(r"[^a-z0-9]", "", word.lower())) + 0.12
    ps = pauses(db, ws + min_off, ws + max(1.8, min_off + 1.0))
    if not ps:
        lo, hi = int((ws + 0.3) * 100), int((ws + 0.7) * 100)
        return (lo + int(np.argmin(db[lo:hi]))) / 100, 0.0
    a, b = min(ps, key=lambda p: abs(p[0] - est))
    cout = min(b, a + MAX_HANDLE)
    return cout, cout - a


WHISPER_MODEL = Path.home() / ".cache/whisper-cpp/ggml-medium.en.bin"
REFINE_CACHE = WORK / "refine_cache.json"


def window_words(lo, hi):
    """Re-transcribe a short window with word timestamps. Times inside a short window are far more
    reliable than in the 20-minute pass (which drifts by up to about a second)."""
    import wave
    cache = json.load(open(REFINE_CACHE)) if REFINE_CACHE.exists() else {}
    key = f"{lo:.2f}-{hi:.2f}"
    if key not in cache:
        w = wave.open(str(V / "working/audit/cam_16k.wav"))
        w.setpos(int(lo * 16000)); frames = w.readframes(int((hi - lo) * 16000))
        tmp = WORK / "win.wav"
        o = wave.open(str(tmp), "wb"); o.setnchannels(1); o.setsampwidth(2); o.setframerate(16000); o.writeframes(frames); o.close()
        run(["whisper-cli", "-m", WHISPER_MODEL, "-f", tmp, "-ml", "1", "-sow", "-oj", "-of", WORK / "win"])
        d = json.load(open(WORK / "win.json"))["transcription"]
        cache[key] = [[x["offsets"]["from"] / 1000 + lo, x["text"].strip()] for x in d
                      if x["text"].strip() and not x["text"].strip().startswith("[")]
        json.dump(cache, open(REFINE_CACHE, "w"))
    return cache[key]


def refine(res, seg, db):
    """Trim words that are not in the intended phrase (the end of the previous sentence, the start of the next)
    using word starts from a window transcription, then snap to the pause beside them."""
    first, last = seg[2], seg[3]
    ww = window_words(res["cin"] - 1.0, res["cout"] + 1.0)
    res["ww"] = ww
    toks = [norm(w[1]) for w in ww]
    ft, lt = [norm(t) for t in first.split()], [norm(t) for t in last.split()]
    exp0 = res["cin"]
    i0 = None
    for i in range(len(toks) - len(ft) + 1):
        if toks[i:i + len(ft)] == ft and (i0 is None or abs(ww[i][0] - exp0) < abs(ww[i0][0] - exp0)):
            i0 = i
    if i0 is None:
        return res
    j1 = None
    for j in range(i0, len(toks) - len(lt) + 1):
        if toks[j:j + len(lt)] == lt:
            j1 = j + len(lt) - 1
    if j1 is None:
        return res
    f_start = ww[i0][0]
    # in-edge: pause before the first word's start
    ps = pauses(db, f_start - 0.6, f_start + 0.05, thr=-30.0, min_frames=3)
    if ps:
        a, b = max(ps, key=lambda p: p[1])
        res["cin"] = max(a, b - MAX_HANDLE); res["qin"] = max(0.0, b - res["cin"])
    else:                                   # words run together: cut in the dip between the two words
        k0, k1 = int((f_start - 0.22) * 100), int((f_start + 0.02) * 100)
        res["cin"], res["qin"] = (k0 + int(np.argmin(db[k0:k1]))) / 100, 0.0
    # out-edge: pause between the last word and the next one (if there is one in the window)
    l_start = ww[j1][0]
    n_start = ww[j1 + 1][0] if j1 + 1 < len(ww) else None
    if n_start is not None:
        lower = l_start + max(0.2, 0.05 * len(lt[-1]) + 0.1)
        ps = [p for p in pauses(db, lower, n_start + 0.05, thr=-30.0, min_frames=5)]
        if ps:
            a, b = ps[-1] if n_start - l_start > 1.4 else ps[0]
            res["cout"] = min(b, a + MAX_HANDLE); res["qout"] = res["cout"] - a
        else:
            k0, k1 = int(max(lower, n_start - 0.25) * 100), int(max(lower + 0.05, n_start) * 100)
            res["cout"] = (k0 + int(np.argmin(db[k0:k1]))) / 100; res["qout"] = 0.0
    return res


def resolve(words, seg, db):
    beat, hint, first, last = seg[:4]
    i0, _ = find(words, first, hint)
    _, j1 = find(words, last, hint, after=i0)
    cin, qin = edge_in(db, words[i0][0])
    cout, qout = edge_out(db, words[j1][0], words[j1][1], (seg[5].get("min_out", 0.2) if len(seg) > 5 else 0.2))
    return dict(cin=cin, cout=cout, qin=qin, qout=qout, text=" ".join(w[1] for w in words[i0:j1 + 1]))


ENC = ["-c:v", "libx264", "-crf", CRF, "-preset", "fast", "-pix_fmt", "yuv420p", "-r", "30",
       "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2"]
VF = f"scale={W}:{H}:flags=lanczos,setsar=1,fps=30"


def make_seg(i, cin, cout, pic, cuts, pin=0.0, pout=0.0, frame=None):
    out = WORK / f"seg_{i:02d}.mp4"
    d = cout - cin
    af = "volume=-2dB,alimiter=limit=0.9"
    if pin or pout:   # a breath of held picture and room around thoughts that were cut tight
        af += f",adelay={int(pin * 1000)}|{int(pin * 1000)},apad=pad_dur={pout:.3f}"
    base = (f"[0:v]{TOM_CROP},setsar=1,fps=30[v]" if pic == "tom"
            else f"[1:v]{VF}[v]")
    fc = base
    vf_s = VF
    if frame and pic == "scr":    # fixed close framing, proxy pixels (x, y, w, h); no moving zoom
        fx, fy, fw, fh = frame
        vf = f"crop={fw}:{fh}:{fx}:{fy},scale={W}:{H}:flags=lanczos,setsar=1,fps=30"
        fc = f"[1:v]{vf}[v]"
        vf_s = vf
    if cuts:
        fc = f"[1:v]{vf_s}[s];[0:v]{TOM_CROP},setsar=1,fps=30[t];[s][t]overlay=0:0:enable='{'+'.join(f'between(t,{a - cin:.2f},{b - cin:.2f})' for a, b in cuts)}'[v]"
        # '+' of between() gives 1/2: enable is true when the sum is non-zero
    if pin or pout:
        fc += f";[v]tpad=start_mode=clone:start_duration={pin:.3f}:stop_mode=clone:stop_duration={pout:.3f}[vv]"
        vmap = "[vv]"
    else:
        vmap = "[v]"
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{cin:.3f}", "-t", f"{d:.3f}", "-i", CAM,
         "-ss", f"{cin - SCR_OFFSET:.3f}", "-t", f"{d:.3f}", "-i", SCR,
         "-filter_complex", fc, "-map", vmap, "-map", "0:a:0", "-af", af, *ENC, out])
    return out


def make_intro(i):
    out = WORK / f"seg_{i:02d}.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-i", KIT / "MyEverFind-Intro_v1.0.m4v",
         "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-map", "0:v:0", "-map", "1:a:0",
         "-shortest", "-vf", VF, *ENC, out])
    return out


def make_outro(i, secs=4):
    out = WORK / f"seg_{i:02d}.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "30", "-t", secs,
         "-i", KIT / "outro_16x9.png", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
         "-map", "0:v:0", "-map", "1:a:0", "-t", secs, "-vf", VF, *ENC, out])
    return out


def pill(draw, text, font, y, fill=(13, 27, 42, 215)):
    w = draw.textlength(text, font=font)
    x = (W - w) / 2
    draw.rounded_rectangle([x - 14 * S, y - 6 * S, x + w + 14 * S, y + font.size + 10 * S], radius=8 * S, fill=fill)
    draw.text((x, y), text, font=font, fill=(244, 240, 232, 255))


def caption_png(text, path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    f = ImageFont.truetype(FONT, 25 * S)
    d = ImageDraw.Draw(im)
    lines = [text]
    if d.textlength(text, font=f) > W - 80 * S:
        words = text.split(); half = len(words) // 2
        lines = [" ".join(words[:half]), " ".join(words[half:])]
    for k, ln in enumerate(lines):
        pill(d, ln, f, H - 62 * S - (len(lines) - 1 - k) * 36 * S)
    im.save(path)


def card_png(path, lines):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    small, big = ImageFont.truetype(FONT, 20 * S), ImageFont.truetype(FONT, 30 * S)
    pill(d, lines[1], big, 150 * S, fill=(244, 163, 98, 235))
    w = d.textlength(lines[1], font=big)                  # amber pill needs ink text
    d.text(((W - w) / 2, 150 * S), lines[1], font=big, fill=(42, 26, 7, 255))
    im.save(path)


def slate_png(path):
    im = Image.new("RGBA", (W, H), (13, 27, 42, 255))
    d = ImageDraw.Draw(im)
    big, mid = ImageFont.truetype(FONT, 34), ImageFont.truetype(FONT, 22)
    for k, (t, f, c) in enumerate(zip(SLATE_TEXT, (big, mid, mid), ((244, 163, 98), (244, 240, 232), (140, 158, 178)))):
        w = d.textlength(t, font=f); d.text(((W - w) / 2, 200 + k * 48), t, font=f, fill=c)
    im.save(path)


def cues(seg_words):
    """Caption chunks at sentence ends, or after a comma once there are four words, never over nine."""
    out, cur = [], []
    for w in seg_words:
        cur.append(w)
        t = w[1]
        if re.search(r"[.?!]$", t) or (t.endswith(",") and len(cur) >= 4) or len(cur) >= 9:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    if len(out) > 1 and len(out[-1]) <= 2 and len(out[-2]) + len(out[-1]) <= 11:   # no one- or two-word orphans
        out[-2] += out.pop()
    return out


def mix_music(src, out, intro_t, outro_t):
    """Bed under the voice, up in the silent logo intro and the end card, ducked by the voice, faded out."""
    total = dur(src)
    first = f"[1:a]aresample=48000,aformat=channel_layouts=stereo,asetpts=PTS-STARTPTS[m1]"
    second = f"[2:a]aresample=48000,aformat=channel_layouts=stereo,atrim=start={MUSIC_LOOP_FROM},asetpts=PTS-STARTPTS[m2]"
    win = (f"max(clip(min((t-{intro_t:.2f})/0.8,({intro_t + 7.0:.2f}-t)/0.8),0,1),clip((t-{outro_t:.2f})/0.8,0,1))")
    delay = f",adelay={int(MUSIC_OFFSET * 1000)}|{int(MUSIC_OFFSET * 1000)}" if MUSIC_OFFSET else ""
    fc = (f"{first};{second};[m1][m2]acrossfade=d=2.788:c1=tri:c2=tri{delay},atrim=0:{total:.2f},"
          f"volume='pow(10,(-12+12*{win})/20)':eval=frame,afade=t=out:st={total - 2.5:.2f}:d=2.5[mx];"
          f"[0:a]asplit=2[v][key];[mx][key]sidechaincompress=threshold=0.04:ratio=4:attack=20:release=500[duck];"
          f"[v][duck]amix=inputs=2:duration=first:normalize=0,"
          + ("loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000" if HD else "alimiter=limit=0.95") + "[a]")
    run(["ffmpeg", "-v", "error", "-y", "-i", src, "-i", MUSIC, "-i", MUSIC, "-filter_complex", fc,
         "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out])


def main():
    words = json.load(open(V / "working/transcripts/cam_wordlist_dtw.json"))
    db = load_db()
    SEG = []
    for sg in SEGS:
        if sg[2] is None:
            SEG.append(dict(beat=sg[0], cin=None, qin=0.2, qout=0.2, text="", pic="", cuts=[]))
        else:
            opt = sg[5] if len(sg) > 5 else {}
            r = resolve(words, sg, db)
            if REFINE and opt.get("refine"):
                r = refine(r, sg, db)
            r.update(beat=sg[0], pic=sg[4], cuts=opt.get("cut", []), frame=opt.get("frame"), min_out=opt.get("min_out", 0.2))
            r["pin"], r["pout"] = max(0.0, 0.16 - r["qin"]), max(0.0, 0.24 - r["qout"])
            r["qin"] += r["pin"]; r["qout"] += r["pout"]
            SEG.append(r)
    files = []
    for i, s in enumerate(SEG):
        files.append(make_intro(i) if s["beat"] == "INTRO" else make_outro(i) if s["beat"] == "OUTRO"
                     else make_seg(i, s["cin"], s["cout"], s["pic"], s["cuts"], s.get("pin", 0), s.get("pout", 0), s.get("frame")))
    durs = [vdur(f) for f in files]      # video length rules; audio is forced to match below (avoids drift)
    # joint lengths: dissolve/cross-fade as long as both sides kept room tone there
    joints = [0.0]
    for a, b in zip(SEG, SEG[1:]):
        joints.append(max(0.05, min(MAX_XFADE, a["qout"], b["qin"])))
    starts, t = [], 0.0
    for k, d in enumerate(durs):
        t -= joints[k]
        starts.append(t); t += d
    total = t
    inputs = []
    for f in files:
        inputs += ["-i", f]
    vch, ach = [], []
    # every audio stream is padded or trimmed to its video's exact length, so cross-fades cannot accumulate drift
    for k, d in enumerate(durs):
        ach.append(f"[{k}:a]apad,atrim=end={d:.4f},asetpts=PTS-STARTPTS[a{k}]")
    vlast, alast, acc = "[0:v]", "[a0]", durs[0]
    for k in range(1, len(files)):
        off = acc - joints[k]
        vch.append(f"{vlast}[{k}:v]xfade=transition=fade:duration={joints[k]:.3f}:offset={off:.3f}[xv{k}]")
        ach.append(f"{alast}[a{k}]acrossfade=d={joints[k]:.3f}:c1=tri:c2=tri[xa{k}]")
        vlast, alast = f"[xv{k}]", f"[xa{k}]"
        acc = off + durs[k]
    base = WORK / "base.mp4"
    (WORK / "xfade.txt").write_text(";\n".join(vch + ach))
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-/filter_complex", WORK / "xfade.txt",
         "-map", vlast, "-map", alast, "-c:v", "libx264", "-crf", CRF, "-preset", "fast", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", str(base)])

    # overlays: (path, start, end, dy, kind) ; kind: "still" (single frame, held), "video" (opener),
    # "card" (still turned into a short stream so it can fade in and out)
    ov = []
    if OPENER.exists():
        ov.append((OPENER, 0.0, SLATE_END, 0, "video"))
    else:
        sp = WORK / "slate.png"; slate_png(sp); ov.append((sp, 0.0, SLATE_END, 0, "still"))
    ov.append((NAME_CARD, *LOWER_THIRD, -70 * S, "name"))
    qc = WORK / "querycard.png"; card_png(qc, QUERY_CARD)
    card_for = {"3 search": 1, "5 worth knowing": 2, "6 compare": 3, "8 plain english": 4, "9 more like this": 5}
    seen = set()
    srt, n, caps = [], 0, []
    for s, t0, d in zip(SEG, starts, durs):
        if s["cin"] is None:
            continue
        if s["beat"] in card_for and s["beat"] not in seen:
            seen.add(s["beat"])
            ov.append((CARDS / f"card_{card_for[s['beat']]}.png", t0 + s["pin"] + 0.2, t0 + s["pin"] + 3.0, 0, "card"))
        if s["beat"].startswith("8") and s["text"].lower().startswith("we also"):
            ov.append((qc, t0 + 3.3, t0 + d + 2.6, 0, "still"))
        # caption text is the intended phrase from the full-length transcript (cleaner than the short windows);
        # words are spread over the speech part of the segment in proportion to their length
        wt = re.sub(r"\bD 18\b", "D-18", s["text"]).split()
        sp0, sp1 = t0 + s["qin"], t0 + d - s["qout"]
        tot = sum(len(w) + 1 for w in wt)
        pos, seg_words = 0, []
        for w in wt:
            seg_words.append([sp0 + (sp1 - sp0) * pos / tot, w, 0.0]); pos += len(w) + 1
            seg_words[-1][2] = sp0 + (sp1 - sp0) * pos / tot
        sentence_start = True
        for cue in cues(seg_words):
            a, b = cue[0][0], cue[-1][2] + 0.1
            text = " ".join(w[1] for w in cue)
            for pat, rep in FIX:
                text = re.sub(pat, rep, text, flags=re.I)
            text = text.strip(" ,")
            if text and sentence_start:
                text = text[0].upper() + text[1:]
            sentence_start = bool(re.search(r"[.?!]$", text))
            caps.append((a, b, text))
    caps.sort()
    for k, (a, b, text) in enumerate(caps):          # joints overlap by up to 0.2 s: never show two captions at once
        if k + 1 < len(caps):
            b = min(b, caps[k + 1][0] - 0.03)
        if b - a < 0.3:
            continue
        p = WORK / f"cap_{n:03d}.png"; caption_png(text, p); ov.append((p, a, b, 0, "still")); n += 1
        srt.append((a, b, text))
    inp2, chain, last = [], [], "[0:v]"
    for k, (p, a, b, dy, kind) in enumerate(ov):
        if kind == "card":
            inp2 += ["-loop", "1", "-framerate", "30", "-t", f"{b - a:.2f}", "-i", p]
        else:
            inp2 += ["-i", p]
        pre = ""
        if kind == "video":
            pre = (f"[{k + 1}:v]scale={W}:{H},setsar=1,fps=30,format=yuva420p,"
                   f"fade=t=out:st={b - a - 0.5:.2f}:d=0.5:alpha=1[o{k}];")
        elif kind in ("name", "card"):
            fade = (f",fade=t=in:st=0:d=0.25:alpha=1,fade=t=out:st={b - a - 0.25:.2f}:d=0.25:alpha=1,setpts=PTS+{a:.2f}/TB"
                    if kind == "card" else "")
            pre = f"[{k + 1}:v]scale={W}:{H},format=rgba{fade}[o{k}];"
        src = f"[o{k}]" if pre else f"[{k + 1}:v]"
        eof = ":eof_action=pass" if kind in ("card",) else ""
        chain.append(f"{pre}{last}{src}overlay=0:{dy}{eof}:enable='between(t,{a:.2f},{b:.2f})'[v{k}]")
        last = f"[v{k}]"
    (WORK / "filter.txt").write_text(";\n".join(chain))
    OUT.parent.mkdir(exist_ok=True)
    run(["ffmpeg", "-v", "error", "-y", "-i", base, *inp2, "-/filter_complex", WORK / "filter.txt",
         "-map", last, "-map", "0:a", "-c:v", "libx264", "-crf", CRF, "-preset", "fast", "-pix_fmt", "yuv420p",
         "-c:a", "copy", "-movflags", "+faststart", DRY])
    mix_music(DRY, OUT, starts[[x["beat"] for x in SEG].index("INTRO")], starts[[x["beat"] for x in SEG].index("OUTRO")])
    with open(OUT.with_suffix(".captions.srt"), "w") as fh:
        ts = lambda s: f"{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{int(s % 60):02d},{int(s % 1 * 1000):03d}"
        for k, (a, b, tx) in enumerate(srt, 1):
            fh.write(f"{k}\n{ts(a)} --> {ts(b)}\n{tx}\n\n")
    json.dump([dict(beat=s["beat"], cam_in=s["cin"] and round(s["cin"], 2), cam_out=s.get("cout") and round(s["cout"], 2),
                    pic=s["pic"], out_start=round(st, 2), joint=round(j, 2), q_in=round(s["qin"], 2),
                    q_out=round(s["qout"], 2), text=s["text"]) for s, st, j in zip(SEG, starts, joints)],
              open(WORK / "cutlist.json", "w"), indent=1)
    print(f"OK {OUT.name}  {dur(OUT):.1f}s  cues={n}")


main()
