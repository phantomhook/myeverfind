# Phase 7 - QA, rights checklist, and notes for the next recording

**v1.0 | 2026-10-27 | Export: `exports/20261027_myeverfind-long-video_v1.0_1080p.mp4` (+ `.captions.srt`, web version `..._720p.mp4`). This is a REVIEW candidate. It is not cleared for public use: see "Not cleared".**

## Export
| Item | Result |
|---|---|
| Format | H.264 1920x1080, 30 fps, AAC 48 kHz stereo, about 261 s |
| Loudness | about -14 LUFS integrated, true peak below -1 dBFS (measured, not heard) |
| Picture | Camera converted from HDR to SDR (colour-space filter, checked on one frame); screen cropped to the browser, no menu bar, Dock or tabs |
| Sync | Voice from the camera lav throughout. Audio length forced to match picture per segment; offsets checked against the original, no drift |
| Captions | From the intended text of the full transcript, not the cut audio. `.srt` provided; also burned in |
| Rebuild | `MEF_HD=1 python tools/build_rough_cut.py "assets/music/Arpeggiated Mood.m4a" 1.0 27.5` |

## QA checklist
| Check | Status | How |
|---|---|---|
| Spelling: MyEverFind, Worth Knowing, Martin D-18, Strats | Done | Read all caption text |
| Captions match the spoken words | Mostly | Re-transcribed the final audio; wording agrees except where whisper mishears over a joint (e.g. "Nothing is sold on MyEverFind" read as "Everything", around 3:14). **Listen to 3:14 to confirm** |
| Stray words at joints | Improved, not zero | Five joints trimmed by window re-transcription. Possible leftovers: an "Andrew" reaction ("Wow") just after "183 results" at about 3:29 |
| Product claims | Checked against on-screen content | Cut keeps only what the screen shows: Compare lists only what the seller lists; sales chart reads "Aug 2026 to Oct 2026"; nothing says "live data", "no account" or a result count other than the 183 and 242 shown on screen |
| Privacy on screen | Cropped; full sweep see below | Menu bar, Dock, personal tabs and Facebook window are outside the crop |
| Facebook and Craigslist | Content cut | The site's own "Also search" link row can still be visible small in some result screens |
| Colour consistency | Checked on stills | Brand ink, bone and amber throughout; camera shots converted to SDR |
| Abrupt transitions | Improved | 0.2 s dissolve and room-tone breath at joints; Andrew's v0.5 notes applied |

## Not cleared (do not publish)
| Item | Status | What clears it |
|---|---|---|
| Music | Suno free tier: non-commercial, "made with suno" tag on both files | Paid tier, the musician's bass sting (owned outright), or a licensed library. Re-read Suno's current terms (UNVERIFIED) |
| Appearance release | Andrew approved in chat on 10/27; Tom's consent was not captured on this take and no signed release is on file (UNVERIFIED) | Signed releases for Tom and Andrew (template: `20260827_appearance-release-template_v1.2.html`) |
| Third-party marks and images | Reverb and eBay appear as plain-text labels on the opener cards and as the site's own badges; listing photos from sellers and a Reverb listing page appear on screen | Check Reverb and eBay affiliate brand rules (UNVERIFIED); consider a shorter or blurred Reverb page shot |
| Claims for Tom to confirm | Where Worth Knowing's lineage facts come from; where saved and recent searches are stored; what "recent sales" window is intended | One short second email after Tom reacts |
| Tom's title | "Founder" on the name card comes from the existing brand kit | Ask Tom |

## Five things to work on for the next recording
| # | Do this | Why, from this session |
|---|---|---|
| 1 | **Camera:** shoot 4K in standard (SDR) colour, not HDR; second camera on Tom's face; frame Tom alone, with any guest clearly to one side | HDR needed conversion; the 1080p wide shot gets soft when cropped to Tom; the second person is in nearly every wide frame |
| 2 | **Screen:** a clean browser window sized to 1920x1080, notifications off, bookmarks and tabs cleared, page zoom up about 125%, searches pre-loaded so nobody waits on a spinner, no right-clicks, cursor still while talking | Two stray right-click menus, 20 to 30 s loading waits, personal tabs and Dock visible, small text |
| 3 | **Delivery:** one idea per take, short sentences, a one-second pause between thoughts, restart a stumbled sentence from the top, do not talk while typing. Record each feature again as its own 30 to 45 s take | Cuts land cleanly in pauses; Tom's best lines were the short, complete ones; the Hendrix typing ran 20 s; shorts need self-contained takes |
| 4 | **Producer:** short questions, wait for the answer, no talking over Tom, a lav on each person on separate tracks, 30 s of room tone at the start | Overlapping voices made some lines unusable; room tone makes joins smooth |
| 5 | **Before rolling:** confirm Tom's facts (sales window, Worth Knowing sources, where saved searches live), screen brightness at maximum, appearance releases signed, consent line spoken on tape, ask Tom about the musician's bass sting for owned music | These were the open claims, a dim screen until 9:28, and a missing release |
