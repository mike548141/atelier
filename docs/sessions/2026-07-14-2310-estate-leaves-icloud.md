# 2026-07-14 · 23:10 · Fable — the estate leaves iCloud; STORAGE.md rewritten

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 96+1 -->
- [2026-07-14 · 23:10 · Fable, the estate leaves iCloud — STORAGE.md rewritten](2026-07-14-2310-estate-leaves-icloud.md) — the owner-decided estate move (shed roadmap, 2026-07-14) executed: every repo copied iCloud → `~/.pets/` (byte-diff verified, fsck clean, all pushed), sibling-relative wiring survived intact, tiki venv now in-repo. This repo's edit: **STORAGE.md rewritten to the new topology** — three locations carry the four roles; the continuous-backup role iCloud filled splits across *push discipline* (offsite leg, new rule bullet: push early, push often) and *Time Machine → NAS*; the trade-off named (between push and TM snapshot, new work exists in one place); the churny-state gotcha generalised to *never let a sync engine hold the working copy*, estate-specific workarounds marked moot. `is_icloud()` tool checks + fixtures untouched — they detect a hazard that still exists for adopters.


**What happened outside this repo (context):** the owner executed the
2026-07-14 decision (recorded in shed's roadmap) to move every estate repo
out of iCloud Drive to `~/.pets/` — a plain local path no sync engine
touches. Copy → byte-diff verify → git fsck, all 14 repos clean and fully
pushed before the move; iCloud originals quarantined pending owner delete.
Sibling-relative wiring (`../atelier/tools` hooks, `../atelier` doctrine
paths) survived unchanged — the one absolute path in the fleet (shed's
`hooks.atelierTools`) was re-pointed. The tiki venv moved in-repo
(`ros/tiki/.venv`, suite green), retiring the venv-outside-tree workaround.

**This repo's change — STORAGE.md:** the doctrine's worked example no longer
matches reality, so the doc was rewritten to the new topology:

- Four roles, now **three locations**: working copy (`~/.pets/`), GitHub
  (master + device portability), Time Machine → NAS (whole-machine).
- The continuous-backup role iCloud filled splits across **push discipline**
  (the offsite leg) and **Time Machine** (everything else). Trade-off named,
  not hidden: between a push and the next TM snapshot, new work exists in
  exactly one place — hence a new rule bullet, *push early, push often*.
- The "keep churny state out of iCloud" gotcha generalised to *never let a
  sync engine hold the working copy* — kept for peers whose working copies
  do sit in synced folders; the estate's own venv/worktree workarounds are
  marked moot.

**Not done here:** tools' `is_icloud()` checks and their test fixtures keep
their iCloud paths — they test detection of a hazard that still exists for
adopters; the fixtures are correct as-is.
