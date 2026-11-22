# NEXT: MyEverFind shoot 2 edit (handoff, 2026-11-21)

**Read first:** `20261121_shoot2-prep_v1.0.md` (the plan), skill `video-cut`, agents `producer` then `verifier`.
**State:** Shoot is Sat 11/21. No footage on disk yet. Nothing built except the plan.

## What was settled this session

| Item | Answer |
|---|---|
| Sources | Tom's screen, front iPhone (Andrew's, carries the lav audio), side iPhone |
| Mic | DJI Mic Mini, 2 transmitters + 1 receiver into the front iPhone |
| Receiver mode | Stereo: double-press the receiver linking button (side, under the 3.5 mm jack); LED solid cyan = Stereo, green = Mono. Confirm in the DJI Mimo app |
| Why Stereo | Each voice on its own channel; in post, split, center each, mix. Raw stereo is hard-panned (lopsided), which is why mono sounded better in shoot 1 |
| Exception | If only Tom speaks on tape, Mono is fine |

## Still open (ask Andrew)

| # | Open item |
|---|---|
| 1 | Is the second mic heard on tape, or only a backup |
| 2 | Is Tom's script a file yet (it is the paper-edit spine) |
| 3 | Which transmitter is Tom's; adapter type (Lightning or USB-C) |
| 4 | UNVERIFIED: does the iPhone Camera app keep both channels. Proof = 10 s test clip, mic A only then mic B only; check with ffprobe/ffmpeg channel split |

## When footage lands (in order)

1. Copy originals to `source/shoot2/` read-only with SHA-256. Run ingest in the background.
2. `ingest.sh` takes exactly two sources: generalize to N first.
3. Check the front-phone file's audio channels; two `av-offset.py` runs (front vs screen, front vs side). Constant lag = one offset each.
4. Split stereo into two centered voice tracks and mix.
5. Paper edit from Tom's script; offer `/storytelling` as a read, not a rewrite.
6. Builder: copy `build_rough_cut_REFERENCE.py`, edit config only, add `front`/`side`/`scr` pictures and in-segment switches. Switches land in pauses; scr shown whenever a product claim is spoken.
7. 20-30 s sample via `producer`, then `verifier`. Then full cut, `rights-gate.py`, unlisted review copy only.

## Carried over (Tom owns)

Worth Knowing lineage source; where saved searches live; "recent sales" window; "Founder" title; eBay 5,000-search cap risk. Music is Suno free tier (review only); no signed releases, so nothing is cleared for public use.

## Housekeeping not done

Board row 8 update; effort-log row for this session.
