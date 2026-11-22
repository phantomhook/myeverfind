# Phase 4 - Rough cut v0.1 notes

**v1.0 | 2026-10-27 | Output: `previews/20261027_long-video_rough-cut_v0.1.mp4` (4:28, 960x540, 30 fps) and `.captions.srt`. Rebuild with `tools/build_rough_cut.py` (cut list is by words, so a re-run after editing a phrase is a 30 s job).**

## How it was made
1. Proxies: camera 960x540 30 fps with HDR converted to SDR (colorspace filter, checked on one frame), screen cropped to the browser (menu bar, Dock and tab bar removed), 30 fps fixed.
2. Camera audio is the voice track for the whole video. Screen picture for camera time t is the screen proxy at t minus 21.28 s (Phase 1 offset).
3. Cut points are word-aligned (whisper with word-level alignment), then snapped to the nearest pause so cuts land between words. Audio: 25 ms fades at each joint, light gain trim and limiter. Loudness -14 LUFS integrated, peak about -1 dBFS.
4. Placeholders: animation slate for the first 14 s (Phase 5), the existing logo intro (6.7 s, longer than the 3 s noted earlier), the existing outro card with the commission disclosure, Tom's existing lower third. No music yet.

## Known roughness (all expected at v0.1)
| Issue | Plan |
|---|---|
| Captions come straight from whisper and are not proofread. They overlap the lower third at 0:14 to 0:20 | Proofread against audio; move captions up while the lower third shows |
| The Hendrix query is cut word by word (about 11 s); the typing and the spoken words may drift by a fraction of a second | Listen and adjust, or replace with a title card of the query |
| Beat 10 is only about 9 s and ends on Andrew's "smarter buyer" without the lead-in | Add the missing sentence or drop the beat |
| Tom's stammer remains in "even, even works on these" | Tighten in the final edit |
| Screen text is small at 960x540 | Push-ins on the Worth Knowing panel and Compare window in Phase 5/7 (screen file has 3x the pixels) |
| The site's own "Also search: Facebook, Craigslist, Sweetwater" links appear in the filter row during the Hendrix and More-like-this beats | Zoom past that row or crop it (we agreed to cut Facebook/Craigslist content) |
| 4:28 is at the top of the 3:30 to 4:30 range, with a 6.7 s intro | Trim the intro and beats 9 and 10 if review says too long |

## Checked
- 31 cuts verified on a 24-frame contact sheet: pictures match the narration at each beat; no Facebook page, personal tab or Dock appears.
- I re-transcribed the output as a check. It read well except at a few joints, where whisper dropped or garbled a word; those need a listen, not a transcript.
- Not checked: any of it by ear, or on a phone speaker.

---

## v0.2 (2026-10-27, after Andrew's notes on v0.1)

`previews/20261027_long-video_rough-cut_v0.2.mp4`, 4:19. v0.1 stays for comparison.

| Andrew's note (v0.1 time) | Change in v0.2 |
|---|---|
| 0:28 "I" cut off | Edges now snap to the nearest real pause (aligner times drift up to 0.7 s), and every start keeps room tone before the first word |
| 0:33 Andrew looks tired, crop out | Camera shots now use a Tom-only crop. The origin story (beat 3) is covered by the site's home page instead of the wide shot |
| 0:53 / 0:55 / 1:10 abrupt | Added two bridging lines Tom said ("one thing that's basic ... more valuable as a buyer"; "having all those things in mind ... answers to the questions a buyer might have"), plus a breath of room tone and a 0.2 s dissolve and cross-fade at each joint |
| 1:46 and 1:55 unintended right-click menu | Cut away to Tom over those 2.5 s and 1.8 s; picture only, his voice continues |
| 2:02 / 2:46 / 4:14 / 4:21 abrupt | Compare is now one continuous take with a bridge line ("this one looks interesting, let's compare these"); the closing "drilling down" lines and beat 10 are gone, so the close is the main benefit, then "where do they go? MyEverFind.com" |
| 2:33 sentence cut off | End-of-segment now waits for the pause after the last word ("we don't insert it") |
| 3:12 awkward | Hendrix typing removed; it goes "we also do a lot of conversational search ... it came back with 183 results" with an on-screen card "what guitar did Hendrix play?" |
| 3:29 cuts off | The More like this beat now ends on "just like this" |

Also: "free, no account" (beat 7) moved out of the long video until Tom confirms where saved and recent searches are stored (flag F4). The lower third is raised so captions no longer overlap it.

**Not verified by ear.** Re-transcribing the output shows most joints clean. Remaining small risks: a trailing syllable of the previous sentence at the start of beats 6 ("version.") and 8 ("for"), and a clipped "Strats" at the end of beat 9. Beat 3's last line cuts straight to "now of course, that's one thing that's basic", which should be checked for flow.
