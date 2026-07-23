# 2026-07-23 · 0327 UTC · cctranscript reads the ccarchive archive

**Model:** Fable · **Worktree:** cctranscript-archive-read · **Trigger:** Mike's
direct ask — "Extend cctranscript so it reads from the live files as it does
today by default, but has an option to read from the same archive that
ccarchive produces/manages."

## What landed

`cctranscript --archive` points every view — `--list`, render, `--json`,
UUID/prefix selection, `-n`/`--repo` — at the compressed mirror ccarchive
maintains, instead of the live logs Claude Code prunes after
`cleanupPeriodDays`. A pruned session now renders word for word from the
archive. Live logs stay the default; nothing changes for existing callers.

Design calls, and why:

- **Shared resolution, shared words.** The archive location resolves exactly as
  in ccarchive — `--dest`, then `$CCARCHIVE_DEST`, then the iCloud Drive
  default — so the same flag/env vocabulary drives both tools. `--dest` alone
  implies `--archive` (naming the archive *is* asking for it).
- **One gunzip choke-point.** `readLogText()` transparently gunzips `.gz`;
  every parser above it stays blind to which store the bytes came from. An
  explicit `.jsonl.gz` path therefore needs no flag at all, and the render is
  byte-identical to the live path (pinned by a contract test).
- **Eviction-aware by design, not afterthought.** Listing peeks inside every
  candidate (cwd sniff + first prompt), which on an iCloud-evicted archive
  would bulk-fault the whole history back to disk. ccarchive's SF_DATALESS
  check is ported (same `CCARCHIVE_SIMULATE_DATALESS` test seam): `--list`
  never reads a dataless mirror — the entry shows an `evicted` marker — while
  rendering one chosen session deliberately fetches its bytes back. Evicted
  records also match `--repo` by dash-encoded folder suffix, because their
  labels fall back to the lossy folder tail.
- **Self-contained, per the instruments pattern.** The ~30 ported lines
  (dataless check, dest default) are duplicated with a pointer comment rather
  than cross-required — same call as cwdFromLog across ccrepo/cctranscript;
  the install symlinks make cross-file requires fragile and the tools stay
  single-file.
- **Provenance is visible.** `--json` transcripts carry `source:
  "archive"|"live"` (judged by the file, so a flagless `.gz` path tags
  correctly); the human header and list footer carry `· archive`.

## Evidence

- Suite 150→156 (`node --test instruments/*.test.js`): identical-render
  contract vs the live fixture, implied `--archive` via `--dest`, flagless
  `.gz` path, simulated-eviction listing (never read, still listed, still
  `--repo`-findable), `readLogText` round-trip, `isDatalessFlags` bits.
  tools/ suite 331 OK. `--help` stays a one-screen digest (the 24-line test
  bit once mid-work — footer condensed); man page updated under the
  flag-superset drift guard.
- Smoke against the real archive: `--archive --list --repo atelier` lists the
  mirrored sessions; `--archive --repo atelier --json` renders the latest
  (31 turns, `source: archive`).

## Records

CHANGELOG (Added), instruments/README (table line + the "sourcing seam"
paragraph now half-closed), ROADMAP-DONE (instruments layer), ROADMAP (open
ccrepo half of the seam recorded under § ccrepo, with the shape a pickup
should follow).

## Open

- The **ccrepo half** of the sourcing seam: rollups still stop at the prune
  horizon (ROADMAP § ccrepo).
- Doctrine-authorship check: this is tool code + records, no doctrine text
  authored, so no review pointer is owed; routine cold review of the change
  rides the normal queue if Mike wants one.
