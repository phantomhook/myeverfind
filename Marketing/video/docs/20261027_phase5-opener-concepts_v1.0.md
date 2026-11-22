# Phase 5 - Opener concepts, chapter title, music brief

**v1.0 | 2026-10-27 | Remotion project `film/` (reuses the Anniversary install via a node_modules link). Previews in `previews/`. Nothing here is final art.**

## Two concepts for the first 14 seconds (under Tom's hook line)

| | A: pen-and-ink | B: simple graphic |
|---|---|---|
| Idea | A seated musician; ten browser windows appear around him, each listing laid out differently with missing fields as dashed boxes; they fade and one clean amber search card draws in | Twelve listing cards drift in at odd sizes and layouts, then settle into an even grid with the same layout; an amber rule underlines it |
| Fits the plan | Yes: editorial, hand-drawn, the problem shown before the solution | Yes: simplest, fully on-brand (ink, bone, amber, square corners) |
| Timing to the hook | 5 s "five to ten tabs" lands as windows fill; 10 s "what if I could simplify" lands as the clean card draws | Chaos until about 6 s, grid settles by 9 s, rule draws 10 to 12 s |
| Honest weakness | The figure is a stick drawing. It proves structure and motion, but not the New Yorker polish the plan asks for. Finished art needs a real illustration | Reads as a tidy motion graphic, not a story. No musician, so less warmth |
| Files | `previews/20261027_opener-ConceptA_v0.1.mp4`, `..._long-video_rough-cut_v0.2_with-opener-A.mp4` | `..._opener-ConceptB_v0.1.mp4`, `..._with-opener-B.mp4` |

**My recommendation:** A, with a proper illustration replacing the stick figure and the windows' pen wobble kept. B is the fallback if the illustration does not come together, and costs half the time.

## Reusable pieces
| Piece | State |
|---|---|
| Logo intro and outro card | Existing kit, reused as is |
| Chapter title card ("Feature 2 / Worth Knowing"), amber rule, Fraunces-style display | Built as a Remotion Still, sample in `previews/20261027_chapter-title-sample_v0.1.png`. Fonts fall back to Georgia and Helvetica until Fraunces and Inter are loaded |
| Tom lower third | Existing kit |
| Rough-cut builder, word-aligned cuts | `tools/build_rough_cut.py` |

## Music (you generate it; I align it)
- Suno free tier is non-commercial: fine for review with Tom, not for publishing. A track that can be published needs a paid tier, the bass sting, or a licensed library. UNVERIFIED by me: re-read Suno's terms before any public use.
- Prompt, from the master plan, plus timing: ask for 60 to 90 seconds, about 90 to 105 BPM, instrumental, quiet bed for the first 20 s so the hook stays clear, and one clear accent (piano or bass note) where the logo reveal lands, about 22 s into the cut. Generate three candidates; I will pick the cleanest accent and place it by trimming or a short fade.
- Mix: under dialogue about 16 to 18 dB below Tom, rising only under the logo and the end card.

## What it will take (estimates, basis shown)
| Work | Estimate | Basis |
|---|---|---|
| Opener A finished: real illustration, timing to narration | 3 to 4 h | Illustration is the unknown; the motion code exists |
| Opener B finished | 1 to 1.5 h | Code exists, tune timing and fonts |
| Push-ins on the Worth Knowing panel, Compare window, price dots; chapter titles over each beat | 2 h | Source screen is 2922x1912, so crops stay sharp; about 6 beats |
| Music aligned, ducked, checked on phone and laptop | 1 h | After you supply tracks |
| Final render at 1080p, captions proofread, QA | 1.5 h | Phase 7 |
| Shorts from the same builder | 2 to 3 h for five | Same pipeline, vertical crops |
Total to a finished long video: roughly 8 to 10 h from here. Planning estimate, not a commitment.

## Needs your decision
1. A or B (or A with a hand-made illustration)?
2. Who makes the illustration? Options: you or an illustrator; an image generator with me repairing defects in code (needs your OK to use a third-party service, no footage involved); or keep the simple line style as it is.
3. Music: send me one to three Suno tracks when you have them.

## Update: Andrew chose B (2026-10-27)
Rough cut v0.3 (`previews/20261027_long-video_rough-cut_v0.3.mp4`, 4:19): opener B timed to the hook (cards drift in under "five to ten tabs", settle into a grid on "what if I could simplify this", amber rule at the end), Tom's name card moved to the right side (`assets/brand/lower-third-tom-babula-right.png`), five chapter cards top-left (`assets/brand/chapter-cards/`), slow push-ins on the Worth Knowing, Compare and More-like-this beats. Open: logos in the chaos (Andrew asked); Suno track.
