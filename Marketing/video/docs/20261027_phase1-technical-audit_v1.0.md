# Phase 1 - Technical audit of the 2026-10-27 footage

**v1.0 | 2026-10-27 | Measured with ffprobe/ffmpeg 8 (Homebrew) on the untouched originals. Stills and audio extracts are in `../working/audit/`.**

## Files

| | Camera (`IMG_2367.MOV`) | Screen (`Screen Recording ... 14.42.21.mov`) |
|---|---|---|
| Duration | 19:37.19 | 18:15.77 |
| Video | HEVC 1920x1080, 10-bit, **HDR (HLG, BT.2020)**, nominal 60 fps (measured 59.97) | H.264 2922x1912, SDR (BT.709), **variable frame rate** (37,191 frames over 1,096 s, about 34 fps average) |
| Orientation | Stored upside down (180 flag); players and ffmpeg rotate it correctly | Normal |
| Audio | AAC 48 kHz stereo | AAC 48 kHz stereo |
| Loudness | -16.6 LUFS integrated, hot. Hits 0 dBFS, 457 samples at or near full scale (light clipping, to be located) | -35.0 LUFS, very quiet. Peak -8.9 dBFS. Laptop mic, backup only |

## Sync: feasible, and good

Cross-correlated the speech band of both audio tracks at eight points across the recording.

| Screen time | 0:05 | 2:30 | 5:00 | 7:30 | 10:00 | 12:30 | 15:00 | 17:10 |
|---|---|---|---|---|---|---|---|---|
| Camera offset (s) | 21.271 | 21.273 | 21.276 | 21.279 | 21.282 | 21.284 | 21.287 | 21.290 |

- **Offset:** screen time 0 = camera time 21.27 s. This matches the filenames (screen started 14:42:21, camera about 14:42:00).
- **Drift:** 19 ms across 17 minutes, steady and linear. That is about one frame at 60 fps. One correction value is enough, no stretching needed.
- **Correlation:** 0.46 to 0.70 at every point, so the match is real, not a guess.
- **Coverage:** the screen file spans camera 0:21 to 18:37. The camera has about 60 seconds of extra footage at the end.
- **No clap used:** the card's sync clap was not needed. Audio correlation works without it.

## Content seen (stills at screen 0:40, 6:40, 15:00; camera 1:00, 6:40, 15:00)

- **Camera:** locked-off wide shot on a couch, Tom left, producer right, a ukulele and an acoustic guitar on the wall behind. Both men wear lav mics. Bright, clean, framed well for a two-shot. The 10/26 camera plan called for two iPhones; only this one angle was supplied.
- **Screen:** myeverfind.com in Safari, full screen: search, Recently Viewed list, Saved (2) plus a Compare 2 button. Later a Facebook Marketplace search for "beginner guitar under $500".

## Findings that affect the edit

| # | Finding | Effect |
|---|---|---|
| 1 | Camera is HDR (HLG). The screen is SDR | Must be converted to SDR before mixing, or the picture looks washed out. This ffmpeg build has `tonemap` and `colorspace` but not `zscale`; the conversion is doable, needs a test pass |
| 2 | Screen recording is variable frame rate | Convert to a constant 30 or 60 fps working copy before editing |
| 3 | Screen file shows the whole desktop: menu bar, Dock with notification badges, personal browser tabs, a Facebook account, "Los Gatos, California" | Crop to the browser content for anything shown outside the family. Check every segment used for private items before publishing |
| 4 | Camera audio is hot and lightly clipped | Use the camera lav as the primary voice, lower the gain, check the clipped spots by ear |
| 5 | Screen resolution is 2922x1912 | Plenty of room for crops and push-ins at 1080p |

## Open

- No lav-versus-camera-mic confirmation yet. The loudness and the visible clip-ons suggest the lavs went into the iPhone, but a listen in Phase 2 confirms it.
- Frame rate, color and clip spots were measured, not watched end to end.
