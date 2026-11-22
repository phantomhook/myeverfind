# NEXT: shoot 2 voice audio, then the full 5-minute cut (handoff, 2026-11-21, evening)

**Read first:** this note, then `20261121_shoot2-content-map_v0.1.md`, then skill `video-cut` (`Personal/personal-OS/skills/VIDEO-CUT.md`), memory `video-overlays-need-contrast`.
**Supersedes:** `20261121_NEXT-shoot2-edit.md` (its "still open" list is answered below).
**State:** a 49.7 s review sample exists (v0.3). The full cut is NOT started. One blocking decision: which voice track to use.

## Step 1 of 4: decide the voice (blocks everything else)

Andrew said the iPhone 1 lav sound is "horrid" and suspected a sync fault. Measured (11/21, `working/shoot2/`):

| Finding | Evidence |
|---|---|
| Not a sync fault | iPhone 1 left and right identical in time (0.06 ms); Mac mic and side phone match iPhone 1 at constant offsets 9.469 s and 0.047 s; speech lines up across all three in `ab/spec3.png` |
| Lav is the duller, noisier source | 6 to 8 kHz about 8 to 10 dB below the Mac mic; noise floor -63 dBFS vs -76 dBFS Mac; no clipping or dropouts anywhere |
| Hiss appears only while he talks | Spectrogram (top row of `ab/spec3.png`). Looks like the lav's noise cancellation. UNVERIFIED: ask Andrew whether noise cancellation was on |
| Mac mic has keyboard and mouse clicks | Thin vertical lines in silence, same image (middle row) |
| Side iPhone is a room mic | Bottom row |

**Listening reel sent to Andrew:** `working/shoot2/ab/ab_reel.m4a`, same 9 s five ways (beeps): 1 lav as shot, 2 Mac mic, 3 side iPhone, 4 lav cleaned, 5 Mac mic cleaned. **Waiting on his pick.** Cleanup chains are in the Bash history of the session; rebuild with `ffmpeg -af "highpass=f=90,afftdn=nr=10:nf=-60,equalizer=f=3500:t=q:w=1:g=2"` (Mac) and `"highpass=f=90,equalizer=f=250:t=q:w=1:g=-3,equalizer=f=4500:t=q:w=1:g=5,afftdn=nr=8:nf=-55"` (lav).

If he picks the Mac mic (reel 2 or 5): builder must take its audio from the screen recording (offset: front t = scr t + 9.475), not from `front_hi.mp4`. Small change in `make_seg`: take `-map` audio from input 1. Remember the screen proxy was made with `-an`; make a voice proxy from the original `.mov` with the cleanup chain.

## Step 2 of 4: build the full cut (target 5:00 max, Andrew's rule)

Beat plan (source times in the front take; details in the content map): hook 17.5-24; search and sort short; Worth Knowing as the lead (136-243); More Like This 299-353; Compare 353-446; share 446-462; close 785-822 ("no sign-up, always free, myeverfind.com"). Cut beats 9 to 11 (natural-language, studio mics, other categories) unless Andrew asks for the "warm jazz guitar" search back.
- Builder: `tools/build_shoot2_sample.py` (config block at top `SEGS`). Pictures: `tom` (front, full frame), `scr`, `side` via `{"side": [(a,b)]}`, `{"broll": [(a,b)]}`. Run: `~/.venvs/video/bin/python tools/build_shoot2_sample.py "assets/music/Arpeggiated Mood.m4a" <version> 27.5`. Proxies cover only 0-300 s of the take: remake `working/shoot2/proxies/{front,side,scr}_hi.mp4` for the full length with `working/shoot2/make_proxies.sh` (drop `-t 300`; screen proxy needs the letterbox `scale=1920:-2,pad=1920:1080:0:(oh-ih)/2:color=0x0d1b2a`). About 6 min of machine time per 300 s of footage, run in the background.
- Tom reading on camera is not wanted: cover with b-roll, the screen, or the side camera only when he is working. Andrew's voice is on the track (66 s "What order are they, Tom?", 462-483, about 668 s, about 690 s): cut around it.
- Intro/outro: video 1 format, hook then logo (`brand-kit/MyEverFind-Intro_v1.0.m4v`, 6.7 s) then content, then `outro_16x9.png`. Andrew did not object to the 6.6 s logo, the verifier suggested about 3 s. His call.
- **End card must NOT say "Founding 100 Advisors" or point to a feedback button** until Tom confirms the button is live (decided 11/21). Andrew's 5:47 PM email to Tom proposes it; Tom has not answered.
- Overlay rules already fixed in the builder: opaque navy caption plate with amber outline, ivory cards with navy outline, card 1 in the empty top-right (`CARD_Y1`), amber highlight box on a spoken number (`HILITE_BOX`; the page scrolls, check the frame).

## Step 3 of 4: audio defects still open

| Item | State |
|---|---|
| Music "crackle/breaks near 0:46" (Andrew, v0.2) | Cause not proven. v0.2 chained a dynamic loudnorm and two limiters; v0.3 uses two-pass linear loudnorm, +7 dB (was +12) rise on the logo and end card, no limiter. A click detector found nothing at 40-50 s in either version. The raw Suno track has small clicks at 4.7, 6.8, 9.05, 15.5 s (under the logo). **Ask Andrew to listen at 0:46 on v0.3** |
| Music choice | Arpeggiated Mood again (3:25, loops at 27.5 s for a 5-min cut). Offered a longer Suno extension or a new prompt ("warm acoustic guitar, steady 70 BPM, light and optimistic, no vocals, builds gently"); Andrew has not chosen |
| Whisper QA on the cut | Unreliable on abutting segments (skips lines), so judge by ear and by per-second level, not by re-transcription |

## Step 4 of 4: gates and housekeeping

- **Verifier:** the `verifier` agent is not registered until Claude Code restarts. Until then run a general-purpose agent with `.claude/agents/verifier.md` as its brief, read-only (done once on the sample, report: caption capital, end the sales line at "similar to this", rights blockers). Producer likewise.
- **Rights (blocks any public upload):** no signed releases (Tom, Andrew); Suno free tier is review-only; Reverb and eBay marks uncleared; "Founder" on the name card unconfirmed; the "recent sales" window shows three different windows on one panel (Sep 2025 to Oct 2026, "2023-2026", "12 most recent close-match"). Run `rights-gate.py` before anything public.
- Carried from shoot 1, Tom owns: Worth Knowing lineage source, where saved searches live, "recent sales" window, "Founder" title, eBay 5,000-search cap.
- Not done: board row 8 update, effort-log row for this session (Claude time roughly 3 h elapsed, estimate; tokens not captured), back-port the overlay and loudnorm fixes into `build_rough_cut_REFERENCE.py`, generalize `ingest.sh` to N sources.
- Not heard by Claude: any audio. Every audio finding here is from measurement.

## Where things are

| What | Path (under `Marketing/video/`) |
|---|---|
| Sample v0.3 (review only) | `previews/20261121_shoot2-sample_v0.3.mp4` (v0.1 and v0.2 are earlier iterations) |
| Builder | `tools/build_shoot2_sample.py` |
| Transcript, word list | `working/shoot2/transcripts/front_2409_words.json`, `working/shoot2/words.json` |
| Sync audio, A/B reel, spectrograms | `working/shoot2/front_16k.wav`, `scr_16k.wav`, `side_16k.wav`, `working/shoot2/ab/` |
| Originals (read only, not copied) | `/Volumes/Samsung_T3/MyEverFind Screen Capture 112126/` (iphone 1: IMG_2405-2409; iphone 2: IMG_5495; mac recording x3; b-roll: IMG_5496.HEIC, IMG_5497.mov). Move to `source/shoot2/` with SHA-256 before the final export |
| Content map | `docs/20261121_shoot2-content-map_v0.1.md` |

Not yet seen: iPhone 1 clips 2405-2408 (rehearsals, 66 s to 6:55), the two short Mac captures at 3:35 and 3:36 PM (24 s, 18 s, likely pickups), a possible second file from iPhone 2.
