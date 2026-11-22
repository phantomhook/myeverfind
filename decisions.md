# Decision Log - [CLIENT NAME]

Log before implementing, not after. One row per decision. This file is also scope protection: "approved YYYY-MM-DD" ends disputes.

| Date | Decision | Why | Declined alternatives | Approved by |
|---|---|---|---|---|
| YYYY-MM-DD | [What was decided] | [Rationale in one line] | [What was considered and passed on] | [Andrew / client name] |

## 2026-09-05 - Hold. Wait for Tom to reach out.

**Decided by:** Andrew.

**Decision:** Do not chase Tom on the shoot date. No re-opening email, no nudge. The next
move on the video is Tom's, whenever he makes it.

**Why:** Tom is under his own pressure to move fast on the product. Adding a scheduling ask
on top of that costs the relationship more than the shoot is worth right now. Andrew's read
on Tom, not a scheduling judgement.

**What this reverses:** a drafted plan to email Tom re-opening the shoot with Brian.
Not sent, not written.

**Correcting the record at the same time:** every project file said the ball was with Tom
for the musician friend's name. That was FALSE from 2026-08-24. Tom supplied both names on
2026-08-23 at 10:56pm PT - **Brian Bernasconi** (bass player, the on-camera guest) and
**Paul Pastrone** (producer) - and confirmed on 8/24 that "Brian is good for this week."
Andrew acknowledged and the thread went quiet. The shoot stalled on OUR side for 12 days
while the notes blamed Tom. Verified in Gmail 2026-09-05, thread `1a03257b3976bb58`.

**Consequently still undone, and now deliberately parked:**
- Appearance release never filled with Brian's name
- Prospect briefing wording never sent to Tom
- Bass-sting ask never raised. Brian is a bass player, so it costs nothing when it is raised
- Brian's stated availability window (week of 8/24) has lapsed

**No backstop set.** Andrew's read (2026-09-05): Tom is a mover and will update us this week
unprompted. No calendar check, no nudge, no reminder. If a fortnight passes in silence, that
read has not held and it is worth saying so once - but the hold is Andrew's to lift, not a
trigger to fire automatically.

**Standing risk:** "waiting on them" with no trigger is how a project dies quietly. Per memory
`waiting-on-them-is-an-inbox-claim`, this row must be re-verified with from: AND to: searches
before it is ever repeated. Last outbound to Tom on the video: 2026-08-24.

## 2026-10-16 - Hold lifted. Tom reached out; video track restarts.

**Decided by:** Andrew (the lift condition was Tom reaching out, per the 2026-09-05 entry above).

**New evidence:** Tom emailed 10/15 5:43pm PT ("very close to try to get this in front of the public"), then held a 36-minute call 10/16 1:30pm PT. Verbatim: `_transcripts/20261016_tom-call-VERBATIM.md`. To-dos: `_transcripts/20261016_tom-call-TODOS-summary.md`.

**Decision:** Restart the video track. Tom will contact Paul and Brian about Fri 10/23. A dry run comes before any guest is on camera (Tom, 29:40). The demo is cut to two marquee features: all marketplaces in one place, and the Worth Knowing panel (Tom, 30:59). The 9/5 "do not chase" rule is closed, not reversed: it said the next move was Tom's, and he made it.

**Not decided (do not record as decided):**
- Whether Fri 10/23 is the dry run or the shoot with guests.
- Whether to link to Reverb sold listings. Tom is leaning yes after an AI answer about Awin attribution, which is UNVERIFIED until he confirms Reverb's cookie window and terms.
- Promotion channels and the call to action. Andrew owes an options list.

**Risk logged:** eBay refused (10/16) to raise Tom's 5,000-search cap. When it runs out the site returns Reverb-only results, which undercuts marquee feature 1 on camera. Needs eBay live on shoot day or Etsy integrated first.

**Still undone from the 9/5 list:** release not filled with Brian's or Paul's name, prospect briefing wording not sent, bass-sting ask not raised.

## 2026-10-17 - Plan and host guide go to Tom as one encrypted HTML page, not Google Docs.

**Decided by:** Andrew.

**Why:** Andrew did not like Docs formatting and readability. Tom's job is to react and decide, not to edit, so section comments plus a Send button fit better than a shared edit file. The guide doubles as his shoot-day card, where collapsible stages work well on a phone. Same pattern as the Jowers detail plan (StaticCrypt + the `doc_review_submissions` table).

**What shipped:** `Marketing/20261017_tom-review-page_v1.0.html` (source, version-locked), published encrypted and unlisted at `aa-foundry.com/mef-review-0b58588380f7` (personal-site commit 55e9b04). Password is held by Andrew, NOT recorded in this folder; he texts it to Tom separately. Verified: wrong password stays locked, right password opens, Send writes one row, test row deleted, no readable text in the served file, noindex present, not in the sitemap.

**Declined:** Google Docs (kept unshared in the private `_old drafts` Drive folder); a markdown attachment ("don't send .md files").

**Still open:** the email to Tom is a Gmail draft and NOT sent. The $100 draw needs Tom's approval before it stays on the survey. No dry-run or shoot date is being pushed.

**Update 2026-10-17, review page v1.1** (same address, personal-site commit ae8fdfa; v1.0 source moved to `Marketing/_archive/`): "Draft" added to the page and lock-screen titles; "react / not time-sensitive" line removed; round 2 wording rewritten; "Not recommended" paragraph removed; the eBay/Reverb follow-up now appears only when Tom picks "OK, run it" for the $100 draw. Decisions cut from eight inputs to four taps (draw, SCORE contacts, ask the professor, share link). Launch date, his 20, signal numbers, measurement, incentive, dry-run date and the Reverb sold-listing link moved to a "talk through on the next call" list. Comment boxes are collapsed behind "Add a comment". 30 of 30 behaviour tests passed; live file matches the build.

**Update 2026-10-18, review page v1.2 (AA Foundry formatting, per-client identity):** Andrew asked for the AA Foundry look, then raised that identical styling would make every client blend together. Decision: a shared AA Foundry frame (warm ivory ground, Instrument Serif headings, the rows and boxed-italic-is-spoken conventions, "Prepared by AA Foundry" credit) with a per-client identity layer taken from the client's own brand. MyEverFind uses its navy (#0D1B2A) and amber (#F4A261) with its own note mark, in a navy masthead band; navy was chosen over amber alone because amber sits too close to AA gold. Same address, personal-site commit ff4c23b; v1.1 source moved to `Marketing/_archive/`. 30 of 30 behaviour tests passed; arithmetic (29 minutes, 30 people) confirmed in Python. Not yet written into the aafoundry-client-doc skill: asked Andrew first.

**Update 2026-10-18, review page v1.3 (colour fix):** Andrew: the v1.2 colour combo "feels slightly off." Cause, measured: three colour temperatures at once (AA yellow-cream ground and warm-black ink, MyEverFind cool navy band, AA green teal for ASK, amber tints turning salmon). v1.3 uses one temperature: MyEverFind bone ground, white cards, navy ink and neutral greys, slate blue (#355A78) for ASK, amber as accent only. Same address, personal-site commit 61e2695; v1.2 source in `Marketing/_archive/`. 30 of 30 tests passed; live file matches the build. Per-client themes added to the `aafoundry-client-doc` skill as the "Per-client identity" section (Andrew's yes, 2026-10-18); memory `client-theme-one-temperature` written.

**Update 2026-10-18, review page v1.4 (Andrew's five points):** (1) Both password-protected pages (MyEverFind review page, Jowers detail plan v2.4) catalogued on the AA Foundry portal as internal `activity` deliverable rows 112 and 113 (visible_to_client false, no passwords). The `deliverables` table is empty and unused; `activity` is the working catalog. (2) Floating Send my review button added. (3) Unsent-input protection: the button shows an "N unsent" badge and pulses, a banner says the answers are saved only on this device, and leaving the page with unsent changes triggers the browser warning; a failed send still counts as unsent. Auto-send was NOT added, so nothing leaves the device until Tom presses Send. (4) New "What the numbers mean, and what comes next" section: about 30 invited, roughly 60 visits at best (Andrew's estimate, labelled as such), measures of success that are not visitor counts, and five next-step ideas (double down on the winning segment, events, low-cost street tactics, the first buyer's story, partners). A reward tied to a buyer's purchase is flagged as needing eBay's written approval and Reverb's permission. (5) Host guide: "the guest" named and defined in a Who is who box, every "him/his" replaced; "More Like This" open item corrected after a live test (it works on a Stratocaster listing; it was never removed). Same address, personal-site commit e3c41f0; v1.3 source in `Marketing/_archive/`. 52 of 52 behaviour tests passed; live file matches the build.

**Update 2026-10-18, review page v1.5 (Source column removed, surveillance-vocabulary rule applied):** Andrew asked for the Source column out and recalled the standing rule (CLIENT-REGISTRY rule 8, set 2026-07-07: no recording, transcripts, capture, timestamps or durations in anything a client reads). v1.0 to v1.4 had broken it with a "Where the facts came from" table citing call timestamps and the word "transcript". v1.5 replaces it with plain-language basis notes (your words on our call, my estimates, tested by me, read by me) and no Source column. The sourced ledger moved to `Marketing/20261017_tom-review-page_RECORD-v1.5.md` (internal). Rule added to the aafoundry-client-doc skill as editorial principle 10, and a test now fails the build if a timestamp or the word transcript reappears. Jowers v2.4 readable source checked read-only: no timestamps, no capture wording. Same address, personal-site commit f731547. 58 of 58 tests passed; live file matches the build.

**Update 2026-10-18, review page v2.0 live (slim rebuild) and lessons captured:** Andrew: too long and tldr; wants standard section titles a CEO or marketer can scan; floating open/close/top control. v2.0 is 1,738 words (was 3,236; about 8 minutes, was about 15), seven standard plan sections and six numbered guide stages, with the floating controls beside the floating Send. Independent QC by Fable (a different model) found 20 items; each was verified against the files first (verdict table in `Marketing/20261017_tom-review-page_RECORD-v2.0.md`); the real defects were fixed, including a version-keyed storage key that would have dropped Tom's unsent answers on any republish. Same address, personal-site commit 4de1668. Andrew then asked what the repeated feedback teaches: captured as the `review-page` skill (`skills/REVIEW-PAGE.md`, wrapper in `~/.claude/skills/review-page/`), nine new REVIEW PAGES checks in `doc-qc.py` (rule 8 vocabulary, Source column, tool words, version-keyed storage, image metadata, unbalanced tags, length budget, title style, tap-count match, unsent protection), `scripts/review-page-build.py` (encrypt, noindex, mark, leak check; proven to pass on the encrypted page and fail on plaintext), a jsdom harness template, a QC prompt template, and a metadata-free logo asset. The same check found Canva and author metadata in the delivered Jowers v2.4 page's logo; NOT changed (delivered; Andrew's call).

**Update 2026-10-18, review page v2.1 live; shape approved; loop closed; template built:** Andrew approved the v2.0 shape ("i did review v2 and do like it much more. approved on shape"; recorded in `Marketing/20261017_tom-review-page_SHAPE.md`) and asked for header uniformity: v2.1 has a larger AA Foundry logo (56px) with two aligned lines, "Prepared by AA Foundry" and "Prepared for MyEverFind | Tom", and the client mark moved to the right; labels stack above values at phone width so nothing wraps. A stale "Your decisions" reference was renamed to the section's real title "Decisions needed". Same address, personal-site commit 6034b30; built with the new `review-page-build.py` (first real use; doc-qc clear, noindex after encrypting, 60-phrase leak check, live hash matched, live leak check passed); 57 of 57 tests. No password reset (Andrew). Closing the loop on Tom's reply: Part C added to the `aafoundry-sweep` skill (reads new `doc_review_submissions` rows by watermark, files his words verbatim, logs decisions, flags first); the table is currently empty. Reusable template saved as `skills/templates/review-page-TEMPLATE_v1.0.html` (doc-qc clear, 13 of 13 smoke tests) and the shape gate is now enforced for every review page; Jowers v2.4 is waived for the gate (built before it existed).

**Update 2026-10-18, review page v2.2 (header redesign) and reply notification:** (1) Andrew: the header was "still off" and asked for a Creative Director solution with the "Prepared for" line first and the black removed from his logo. Diagnosis: two equal-weight icon tiles (a black AA tile and an amber client tile) competed with each other and the title; the credit lines read like a form; the black tile looked like a hole on the navy band. Solution (concept A): client first and large (label, "MyEverFind | Tom", mark at right), then title and standfirst, then a quiet signature row with a transparent AA Foundry glyph and the draft version. The glyph was made by color-keying the gold off the 3D-render background (brightness could not separate them), metadata stripped, brightened for dark. Concept B (paired credits) was compared side by side and not used. Same address, personal-site commit 16776e7; 62 of 62 tests, doc-qc clear. The shape file notes the revision. (2) Andrew asked to be notified when Tom replies instead of asking: LaunchAgent `com.aaos.review-inbox-watch` (every 10 minutes) reads `doc_review_submissions` with the existing keychain key and raises a macOS alert and sound (who and which page, never the answers); the first run initialises silently; TEST-named rows are ignored. Proven: a fake submission alerted once and a re-run stayed silent; a TEST row was ignored; both fake rows deleted; table empty. The sweep skill (Part C) files the content. The Mac must be awake and logged in; missed polls catch up on the next run. Optional later: a phone push.

**Update 2026-10-18, review page v2.3 (lighter mark):** Andrew: "the icon still feels too heavy." The solid amber 84px tile was the heaviest object on the page and outweighed the title. Three lighter treatments were compared on a scratch page (ghost tile, bare note, outline tile); the ghost tile won: it keeps the app-icon identity at a fraction of the weight (64px, 46px on phones; accent at 12% fill, 1.5px hairline at 55%, light-accent note). The lock-screen mark matches. Template rebuilt with the same mark (it was accidentally truncated to 0 bytes by a scripting slip and restored from its generator; verified: gate clear, 13 of 13 smoke tests, no client text). Same address, personal-site commit 43257d6; 65 of 65 tests; live file matches the build; live leak check passed.

## 2026-10-18 - Review page SENT to Tom
- Cover email sent (verified in Gmail Sent, to tom@mybeachview.com, subject "MyEverFind: plan and host guide for your review"). Password texted separately (Andrew, per his report; text itself UNVERIFIED by me).
- Page: aa-foundry.com/mef-review-0b58588380f7 (v2.3). One question in the email: the $100 random draw. No date pressed.
- Reply alert armed: com.aaos.review-inbox-watch (10-minute poll, macOS alert on a real submission). Tom may also reply by email, which the watcher does not see.
- Next: wait for Tom. On reply, file his words verbatim first, then summarize and log decisions.

## 2026-10-20 - Tom replied to the review page (v2.3): the $100 draw comes off.
**Source:** `Marketing/20261020_tom-review-v2.3-reply-VERBATIM.md` (submission id 15, sent 8:39 AM PT). The 8:48 AM text to Andrew was the automated review alert, not from Tom. No email reply checked.
**Decided by:** Tom.
- $100 draw: **take it off.** His reasons: it means collecting personal info he is not set up for, and cash prizes may be seen as a lottery. He still wants incentives people will respond to (open).
- Ask the professor: **yes, he will ask.**
- Screenshot view or share link: **yes.**
- SCORE contacts: **not decided yet.**
- His 20 people: not chosen yet, he will think about it.
- Wording steer: do not imply selling or negotiating ("asked vs sold"); lead with how easy it was to find the item, not price.
- Open from Tom: how to open the conversation with invitees ("I built this for myself" breaks down once a survey is attached and forwarded). Wants to talk it through again.
**Impact to sweep (not yet done):** the draw wording on the live survey, the survey/recruitment email drafts, the plan's incentive and eBay/Reverb follow-up lines, and the offer/CTA copy all need the draw removed and price framing replaced.
**Update 2026-10-20 (Andrew: "yes, remove the draw and price framing"):** `Marketing/20261017_launch-plan_DRAFT-v0.2.md` (draw row dropped, CTA leads with findability, "asked vs sold" screenshot replaced) and `Marketing/20261017_survey-recruitment-email_DRAFT-v1.3.md` (draw sentence and winner-contact wiring removed; sold-price and "what to ask a seller" cut from the pitch). v0.1 and v1.2 moved to `Marketing/_archive/`. NOT changed: the review page Tom answered (v2.3, a record), the sent cover email, and the LIVE Google Form, which still shows the draw in the description and email box (checked by fetch 2026-10-20). Andrew must edit the form.
**Update 2026-10-20 (later): live Google Form cleaned by Andrew.** Verified by fetching the published form: description and email box carry the original wording, no $100 or draw text (the one "draw" match is a font setting), Q8 and Q9 still present. The 10/21 reminder was deleted. Reply to Tom is a Gmail draft, NOT sent (reply on the 10/19 review-email thread).
**Update 2026-10-20: reply to Tom SENT** (verified in Gmail Sent, 2026-10-21 00:41 UTC = 5:41 PM PT 10/20, to tom@mybeachview.com, on the review-email thread). One ask: 20 minutes this week for the opening line and his 20. Next: wait for Tom; on a reply, file it verbatim first.

## 2026-10-27 - Video: 10/27 footage becomes an interim cut; scope set
**Decided by:** Andrew (answers in the 10/27 Code session).
**Decision:** The 10/27 2:15pm session was a dry run. Make a usable interim from it anyway, as a way to build a reusable process. Build one long feature video (3:30 to 4:30) plus short single-feature clips (20 to 45 s). All Facebook and Craigslist material is cut from every version. Andrew's voice may stay in. Suno free-tier music is for review only, non-commercial. Files live in `Marketing/video/`; originals are checksummed and read-only.
**Why:** Andrew wants something usable now and a repeatable process; the Facebook segment was Andrew's call (15:31) and shows a personal account.
**Open:** Tom has not seen the footage or the plan. Claims F1-F4 in `Marketing/video/docs/20261027_phase2-content-map-and-clips_v1.0.md` need Tom before anything is public.

## 2026-10-28 - Long video v1.0 sent to Tom (per Andrew)
**Reported by Andrew, not verified by Claude:** the 1080p long video went to Tom by email and was posted unlisted on YouTube. Master and notes: `Marketing/video/exports/` and `docs/` (phases 1 to 7). **Not cleared for public use:** Suno free-tier music, no signed appearance releases, Reverb listing page on screen, claims for Tom (Worth Knowing sources, where saved searches live). **Next:** Tom's reaction, then the five shorts; a second email to Tom for the open claims. Board row 8 not yet updated with this.

## 2026-10-28 - Reply to Tom on the rough cut SENT (verified in Gmail Sent, 9:51 PT)
Andrew sent the reply on the "Dry run draft vid" thread (id 1a1834a0c4371091). Content as in the revised draft: the video does make the value case (time saved, more information, price comps); the benefit line comes only at the end; sharpen why it beats Google, Reverb's own search or an AI chat; look at the lens for the opening and close; one ask, 30 minutes this week to settle three value points before recording again. Correction recorded: an earlier draft said the video "never says why someone should use it" and implied Google lacks these features; both were wrong or unverified and were removed before sending. **Next:** Tom's answer on the 30 minutes; then the second email on open claims; then the five shorts.

## 2026-11-22 - No-voice cut for video 2
**Decided by:** Andrew.
**Decision:** Video 2 ships as a music-only cut (screen recording plus text cards and a motion-graphics hook), with no voice track and no Tom on camera. v0.3 approved.
**Why:** Tom does not want to be featured on camera after seeing threats against another creator; the voice track also had artifacts and a sync mismatch.
**Declined:** Re-recording voice at home (parked, not dropped).
