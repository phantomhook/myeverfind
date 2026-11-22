# MyEverfind — Video Production Master Plan
**Version 1.0 | October 27, 2026 | For Claude Code Desktop**

## Mission
Create a polished, prospect-facing introductory video for MyEverfind from approximately 20 minutes of recorded footage. Working target: 90–150 seconds, adjustable after footage review. This is an editorial product story, not a feature-complete training video. Prioritize credibility, musical sophistication, clarity, and the founder's authentic voice. Build reusable production capabilities without overengineering the first experiment.

## Operating instructions for Claude Code
Read this entire brief first. Execute **one phase at a time**; present concise findings, a recommended next action, and an explicit approval request before proceeding. Do not launch the full pipeline at once. Be economical with tokens, renders, and paid services. Never modify source media. Never assume that a feature, brand claim, visual, or quotation is accurate without verification. Clearly label creative proposals versus observed facts. Do not purchase credits, subscribe, upload proprietary footage to third-party services, or install major dependencies without approval. Prefer local, deterministic tools (e.g. FFmpeg/ffprobe and available transcription tooling). Explain blockers in plain language.

## Inputs and constraints
- One camera/tripod angle showing Tom, with the producer seated alongside as a placeholder; usable lavalier audio was recorded.
- Separate screen recording of Tom's desktop, including its own audio.
- Roughly 20 minutes recorded; exact file durations, quality, formats, and synchronization unknown until inspected.
- Tom opens by describing why he built the product; later demonstrates actual features.
- Brand website believed to be myeverfind.com; verify current logo, spelling, colors, and rights before incorporating assets. Seek original SVG or transparent PNG if available.
- Music will be generated or selected separately, potentially via Suno; do not presume usage or commercial licensing rights.

## Audience and editorial promise
Prospective users interested in music gear, including musically knowledgeable and potentially older viewers. Communicate an intelligent, tasteful, trustworthy product rather than a loud tech advertisement. Main pain point: listings from different marketplaces use inconsistent layouts and have varying completeness. MyEverfind provides a consistent view that makes comparison easier; it does **not** invent missing listing data. Additional product-level specifications/background and price history may be retrieved based on identifying information, as demonstrated. Verify exact behaviors against footage and Tom before making claims.

## Provisional story arc (subject to transcript and footage)
1. **Human hook (approximately 8–15 sec):** Best authentic excerpt from Tom explaining the frustration or motivation. Choose the strongest sentence, not necessarily the earliest. Preserve his actual wording.
2. **Problem visualization (approximately 8–15 sec, may overlap hook):** Restrained editorial pen-and-ink illustration of a musician confronted with inconsistent gear listings, incomplete fields, scattered prices and clutter. Sophisticated New Yorker-like editorial sensibility without imitating any particular artist. Gentle visual wit is optional, not a requirement.
3. **Branded reveal (approximately 4–6 sec):** Elegant MyEverfind logo motion, timed to a musical accent. Use verified brand artwork. A subtle scan/reveal line is one candidate, not a locked design. Avoid flashy effects.
4. **Product proof (majority of runtime):** Actual screen recording of finding gear, consistent side-by-side comparison, supplemental product specifications/background, and price history—only where visually clear and actually demonstrated. Use Tom's recorded narration where possible. Show Tom briefly for personality or emphasis; prioritize readable screen content.
5. **Close (approximately 5–10 sec):** Clear, accurate benefit and simple invitation to explore MyEverfind. Confirm final URL and call to action with owner. Optional musical callback.

The animation should illustrate the *problem*, while actual captured product footage should prove the *solution*. Avoid fabricating UI screens. If narration does not support a needed statement, suggest an on-screen caption or a short pickup line for Tom, subject to approval.

## Visual and sound direction
- Style: contemporary documentary/editorial, sophisticated minimalism, restrained hand-drawn pen-and-ink imagery; black/white plus possibly one verified brand accent color.
- Motion: subtle parallax, line reveals, purposeful timing, not cartoon slapstick. Optional understated humor if naturally supported by the story.
- Music: original-feeling, contemporary instrumental; nuanced jazz-influenced harmony, warm piano, subtle synth texture, melodic bass, precise understated percussion, memorable motif, elegant spacious production. No vocals, bombastic builds, or generic corporate-tech sound.
- Musical reference: sophistication and restraint of a premium interview/podcast opening, **not** imitation of an existing copyrighted theme.
- Start with music primarily under brand reveal and transitions; keep Tom's speech intelligible. Mix conservatively and check on phone and laptop speakers.
- Verify licensing/usage terms of any generated or sourced music before publishing.

### Initial Suno creative prompt
Contemporary instrumental theme with sophisticated jazz-influenced harmonies, minimalist electronic production, warm piano, subtle synth textures, melodic bass, precise understated percussion, and a distinctive memorable motif that develops naturally. Intellectually engaging, elegant, confident, modern, excellent musicianship, polished but restrained production, spacious arrangement. No vocals, no dramatic cinematic builds, no generic corporate music. Suitable for a thoughtfully produced documentary about music and a premium music-gear discovery brand. Create an opening-friendly musical phrase with a clear but subtle accent for logo reveal.

## Phased execution and approval gates
### Phase 0 — Workspace and tooling assessment
Locate project directory or ask user to identify it. Inventory existing tools and current Claude Code conventions. Propose directory tree before creating anything substantial. Place source media in read-only `source/` or equivalent, with untouched originals. Distinguish reusable global skills from brand/project-specific instructions. **Deliverable:** folder proposal, tooling inventory, missing inputs, estimated effort. **STOP for approval.**

### Phase 1 — Media ingest and technical audit
Locate/import user-designated recordings, record checksums, metadata (duration, resolution, frame rate, audio channels/sample rate), check lav and screen audio, identify obvious defects and potential clock drift. Create proxies if necessary; preserve originals. **Deliverable:** concise technical report and synchronization feasibility. **STOP for approval.**

### Phase 2 — Transcript and content map
Transcribe speech with timestamps and speaker labels where feasible. Identify Tom's best founder statements and actual demo moments for: searching, comparing listings, product specifications/background, price history. Produce a timestamped feature map, exact quote options, claim verification flags, and any unclear/inaudible sections. **Deliverable:** transcript plus shortlist of clips with source/timecode. **STOP for approval.**

### Phase 3 — Editorial outline and paper edit
Propose 1–2 tight story structures in 90–150 second range (or recommend another length if footage warrants). Give sequence, estimated durations, actual spoken excerpts/timecodes, corresponding screen visuals, proposed captions, animation placeholders, and proposed CTA. Mark missing proof explicitly. **Deliverable:** selected paper edit / edit decision list. **STOP for approval.**

### Phase 4 — Sync and rough cut
Align camera/lav and screen recording by common audio; check drift near start/middle/end. Use lav as primary audio where it is best; mute or selectively use desktop track as needed. Assemble screen-first rough cut with temporary slates for animation/logo/music. Keep captions legible and UI readable on mobile. **Deliverable:** watchable low-resolution rough cut plus notes on issues. **STOP for approval.**

### Phase 5 — Opening animation and brand package
Use approved narrative timing and verified brand assets. Produce no more than 2 lightweight storyboard/motion concepts first: (A) editorial pen-and-ink comparison problem; (B) simpler graphic alternative. Humor optional. Avoid expensive full renders until one is selected. Create reusable logo reveal, simple chapter transition, and closing treatment. **Deliverable:** short previews and estimated additional work. **STOP for approval.**

### Phase 6 — Music and audio finishing
Review 2–3 candidate music cues, including Suno outputs supplied by user. Check rights. Time logo motion to musical accents; duck/trim music beneath dialogue. Clean lav audio without unnatural processing; normalize speech and avoid clipping. **Deliverable:** near-final mix preview. **STOP for approval.**

### Phase 7 — Final edit, QA, export
Polish pacing, transitions, legibility, spelling, factual claims, color consistency, audio sync, and caption accuracy. Confirm permissions for footage, logos, and music. Export primary 16:9 master, web-friendly version, and optional caption file. Record tool commands and source/asset provenance. **Deliverable:** final files and QA checklist. **STOP for final acceptance.**

### Phase 8 — Reusable skills and handoff
Only after workflow is validated, package reusable skills: (1) media ingest/transcription and feature mapping, (2) synchronized screen-first editing and QA, (3) project-specific MyEverfind brand/story templates. Keep generic tools/skills outside the MyEverfind project; store branding, assets, and creative rules inside it. Follow current Claude Code skill conventions discovered locally. Document invocation, dependencies, inputs/outputs, limitations, and simple instructions for the next video. Do not automatically generalize experimental scripts. **Deliverable:** tested skills, clean project structure, one-page repeatable checklist. **STOP for approval.**

## Suggested directory responsibilities (Claude may refine)
- `source/` untouched originals; `working/` proxies, synced audio, transcripts, edit decisions
- `assets/brand/`, `assets/illustration/`, `assets/music/`
- `previews/` review renders; `exports/` approved deliverables
- `docs/` brief, decisions, permissions, QA, version notes
- Shared skill/script directory outside this project, using documented Claude Code conventions

Use descriptive versioned filenames, no overwriting approved exports, and separate temporary artifacts from finals. Confirm paths with user before moving files from Downloads.

## Budget and schedule assumptions
Initial directional estimate: **8–15 hours** for first video, plus **3–5 hours** to formalize reusable skills (roughly **11–20 hours** total), highly dependent on local tooling, animation complexity, quality of footage, review cycles, and render time. A first rough cut might take 3–5 hours if sync and transcription work smoothly. These are planning estimates, not commitments. Prefer no new paid tools until a clear limitation justifies them. Flag any costs or license requirements before action.

## Critical safeguards
- No alteration/deletion of originals; checksums and backups where practical.
- No invented quotes, product functionality, standardized missing data, or fabricated screenshots.
- Do not assume music, fonts, artwork, or third-party marketplace screenshots are cleared for publication.
- Do not assume Claude Code natively performs transcription/editing/animation: inspect available local tools and state what needs installation or manual review.
- User approves every phase; no autonomous spending or publishing.
- Keep user-facing summaries short, clear, and nontechnical.

## First instruction to Claude Code
**Read the attached MyEverfind Video Production Master Plan. Do not begin editing. Start with Phase 0 only: inspect my available project location and tools, propose the folder/skills structure, identify the recordings and brand assets you need, and give me a concise checklist. Do not move or change any files until I approve your plan.**
