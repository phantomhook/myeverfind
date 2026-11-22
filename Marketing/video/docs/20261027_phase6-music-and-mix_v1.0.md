# Phase 6 - Music and mix (review version)

**v1.0 | 2026-10-27 | Two Suno candidates compared. Cuts: `previews/..._rough-cut_v0.4.mp4` (MEF Babs) and `..._v0.5.mp4` (Arpeggiated Mood). Mixes are measured, not heard by me.**

| | MEF Babs | Arpeggiated Mood |
|---|---|---|
| Length | 2:38 | 3:25 (nearer the 4:19 cut, so less looping) |
| Tempo (autocorrelation, UNVERIFIED) | about 86 BPM | about 70 BPM |
| Loudness | -14.3 LUFS | -13.9 LUFS |
| Energy in the speech band (300 to 3400 Hz), first minute | 58% | 45%, so it should compete less with Tom's voice |
| Shape | Quiet start, then busy and uneven | Quiet start, then a steady plateau from about 20 s |

**Choice:** Arpeggiated Mood, which is also the one Andrew prefers. v0.5 is the cut to review.

**Mix:** music sits about 12 dB under the voice, rises 12 dB in the silent logo intro and on the end card, is ducked by Tom's voice (sidechain), and fades out over the last 2.5 s. When the cut outlasts the track, it re-enters 8 bars in with a crossfade (27.5 s at 70 BPM). The finished mix measures -13.6 LUFS integrated, peak -0.4 dBFS. UNHEARD by me.

**Rights:** both files carry a "made with suno" tag and the free tier is non-commercial. Review use only. For publishing, a paid tier or another source is needed (UNVERIFIED: read Suno's current terms).

**Not done:** no single accent is aligned to the logo reveal (neither track has a clean one I could find by measurement). `MUSIC_OFFSET` in `tools/build_rough_cut.py` slides the track if Andrew hears a better landing.

## v0.6 (2026-10-27, Andrew's notes on v0.5)
`previews/20261027_long-video_rough-cut_v0.6.mp4`, 4:21, Arpeggiated Mood.
- Chapter cards moved to the right and lower third (clear of site headlines and captions).
- Worth Knowing: the moving zoom is gone. Fixed framing on the right-hand 650 px of the screen keeps the panel's whole width in view (the earlier zoom was centred 85% right and clipped it). The first Worth Knowing line stays full-frame until the panel opens.
- Compare and More like this: full frame, no zoom, so the whole Compare window shows.
- Beat 8: Andrew's "how many results did it come back with?" now bridges into "it came back with 183 results". The "what guitar did Hendrix play?" highlight appears 3.3 s in, after the Feature 4 card has gone.
- Close: the final line now runs through "MyEverFind.com" (verified by transcribing the last seconds).
