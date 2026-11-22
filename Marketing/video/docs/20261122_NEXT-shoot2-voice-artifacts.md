# NEXT: shoot 2 full cut, voice still has artifacts (handoff, 2026-11-22)

**Read first:** this note, then `20261121_NEXT-shoot2-audio-and-full-cut.md` (earlier handoff), skill `video-cut`.
**State:** Full cut v0.3 exists (4:38). Andrew: visuals and music are great; the voice still sounds like more than one voice, with artifacts, from the first second. Not fixed. Nothing committed.

## What was learned this session (11/21)

| Finding | Evidence |
|---|---|
| The iPhone "lav" track is the iPhone's built-in mic. The DJI audio was never recorded | Andrew found the input set to iPhone in iPhone settings. Mimo showed "connected" and meters moved, which only proves the receiver heard the mic. L/R correlation 0.75 to 0.87, not one voice per channel. Receiver dial was at +12. Receiver LED was green (Mono; cyan = Stereo) |
| Mac mic is the best remaining track | Cleaner than iPhone built-in. Laptop mic across the room, so room echo and keyboard clicks |
| Andrew picked reel clip 2 (Mac mic, light cleanup, no compression) over the cleaned and compressed ones | `working/shoot2/ab2/hook_reel.m4a` (4 variants of the 7 s hook) |
| The compressor chain in v0.1 and v0.2 was over-processed | Andrew heard a distorted second layer. v0.3 removed it. Complaint persists |

## Lead for the next session (UNVERIFIED, check first)

Whisper on the v0.3 mix (`/private/tmp/claude-503/x/cut16.srt`, may be gone) heard phrases that are not in any cut segment: "sorted by what my Everfind thinks are the best match" (source about 67.7 s) and "let's go back to best match" (about 110.7 s). Whisper on the cut at 26.3 s heard: "So we get a sort of a snapshot of what my Everfind thinks are the best match for Taylor guitars." Intended text there: "...snapshot of all types of Taylor guitars that are being listed" (source 59.4 to 65.9).

That could mean the voice audio inside segments is not the audio at the cut times (a timeline mismatch in the voice track), which would sound like extra voices, not just artifacts. It could also be whisper hallucinating on poor audio. **Do this before any rebuild:**
1. Transcribe `working/shoot2/voice_v3.wav` at 59.4 for 7 s and compare with the iPhone transcript for the same times (`working/shoot2/words.json`). Use `bash -c`, because zsh does not word-split the loop variables (a first attempt failed on that).
2. If they differ, suspect `make_proxies_ext.sh` and the mux: `voice_v3.wav` is the Mac audio delayed by 9.475 s (`adelay=9475`, `apad=whole_dur=824`); `front_full.mp4` is `front_hi_300.mp4` + `front_ext.mp4` video with that wav muxed in. Check that the Mac `.mov` audio stream starts at the same time as its video (ffprobe `start_time` for each stream); offset 9.475 was measured by audio correlation against the iPhone.
3. Check each segment boundary in `working/shoot2/rough_full/cutlist.json`: seg 3 ends at 65.86 s, and Andrew's "What order are they, Tom?" starts at 65.7 s.

## Files

| What | Path (under `Marketing/video/`) |
|---|---|
| Full cut builder | `tools/build_shoot2_full.py` (copy of the sample builder; SEGS holds the 20-segment plan) |
| Full cut v0.3 (current), v0.1 and v0.2 earlier | `previews/20261121_shoot2-full-cut_v0.3.mp4` plus `.captions.srt`; `_nomusic` variants in `working/shoot2/rough_full/` |
| Voice (current: Mac mic, light cleanup, no compressor, +gain) | `working/shoot2/voice_v3.wav` (front clock, 824 s); raw cleaned `voice_mac_clean_raw.wav`; gain in `gain.txt` |
| Full-length proxies | `working/shoot2/proxies/{front,scr,side}_full.mp4`; `make_proxies_ext.sh` made them |
| Run | `~/.venvs/video/bin/python tools/build_shoot2_full.py "assets/music/Arpeggiated Mood.m4a" <version> 27.5` (about 4 min) |

## Decisions and open asks

| Item | State |
|---|---|
| Final voice plan | Tom re-records at home from a script Andrew will request after the cut is locked; sync to existing footage where he is on camera, otherwise screen and b-roll |
| No-voice sampler (about 60 s, music bed, captions and feature cards) | Proposed, Andrew said "we may want to try". Not started. Needs a builder flag to mute voice and raise the music |
| Tell Tom about the audio miss | Andrew wants to own it when he sends the final clip. Offered a short draft; not written. Stage as a Gmail draft, Andrew sends |
| Isolation test for Andrew | Send a voice-only clip (the `_nomusic` file) so he can say whether the second voice is in the voice or the music mix |
| DJI | Check Mimo for transmitter onboard recordings (Mic Mini may keep a backup; unknown). Before reuse: firmware update, set receiver dial to 0, test in Camera with headphones |
| Music crackle near 0:46 | Not confirmed fixed |
| Rights (blocks public use) | No releases, Suno free tier, Reverb and eBay marks, "Founder" title, mixed "recent sales" windows. Review copy only |
