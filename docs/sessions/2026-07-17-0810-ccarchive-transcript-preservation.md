# 2026-07-17 · 0810 UTC · ccarchive — durable transcript preservation

## What prompted it

Mike: "Keep all my raw transcripts (word for word), including timestamps and any
other metadata like model used, for reference." Chose **both levers** (stop the
deletion *and* archive) with the durable copy as a **compressed archive in iCloud
Drive**.

## The finding first

The raw record already exists and is complete: every session is a `.jsonl` under
`~/.claude/projects/<repo>/`, one JSON object per turn, verbatim — `timestamp`,
`model`, token counts, tool calls, thinking. `cctranscript` only *reads* these.
The catch is they're **ephemeral**: Claude Code deletes logs older than
`cleanupPeriodDays` (default 30). "Keep for reference" = get ahead of that.

## The build — `ccarchive` (new instrument)

A fourth verb for `instruments/`: **preserve**. Sits beside the observers as a
zero-dep Node CLI, unit-tested like `cctranscript`.

- **Incremental per-session gzip mirror**, not one monolithic tarball. Each
  `<rel>/<name>.jsonl` → `<dest>/<rel>/<name>.jsonl.gz` (sessions *and* nested
  subagent logs). Rejected a single daily tarball: it would re-upload the whole
  ~400 MB→GB blob to iCloud every run, and hide each session inside an archive.
  The mirror uploads only changed sessions and keeps each directly readable
  (`gunzip` → `cctranscript`, or `zgrep`). ~2.8× smaller than raw.
- **Append-only by contract:** never deletes from the archive — when Claude
  Code's cleanup removes a source, the archived copy stays. That's the point.
  It copies bytes (doesn't parse the `.jsonl`), so it's immune to schema drift.
- **Dest derived at runtime** from `$HOME` (default the macOS iCloud Drive path;
  `--dest`/`CCARCHIVE_DEST` override) — so no personal path lives in the code,
  and the public-repo boundary holds. `--dry-run`, `--json`, reads source
  read-only. It's the **first *writing* instrument** — recorded as an ADR 0006
  addendum with the two guards (no personal data in code; the write target is a
  personal store outside any repo).

### Bug found + fixed during verification

First live run re-archived everything every pass. Cause: stamping the mirror's
mtime via a `Date` truncates to milliseconds, so the copy read back a hair
*older* than its source and always looked stale. Fix: stamp with numeric seconds
(full fidelity) **and** give the freshness check a 1 ms tolerance so sub-ms
filesystem rounding can't masquerade as a change. 12 tests, incl. a contract test
over a synthetic tree (round-trip byte-identity, subagent capture, non-`.jsonl`
ignored, idempotency, append-only, dry-run).

## Machine-local wiring (outside the repo — no personal data travels here)

- **Second lever, then reverted at Mike's call.** Set `cleanupPeriodDays: 3650`
  in `~/.claude/settings.json`, then removed it — with `ccarchive` running daily,
  every session is archived long inside the 30-day window, so the archive alone
  is the durable copy and there's no reason to hoard raw logs. Let default
  cleanup keep the working dir lean.
- **Schedule:** `~/Library/LaunchAgents/nz.cxi.ccarchive.plist` — `StartInterval`
  daily + `RunAtLoad`, invoking node by absolute path (launchd's minimal PATH).
  Loaded and confirmed: RunAtLoad archived the changed sessions, exit 0. Log at
  `~/.claude/ccarchive.log`.
- **First archive run:** 428 transcripts, 396 MB → 143 MB, 7.5 s; a mirror
  verified byte-identical to its live source; second run idempotent.

## Reconciliation with `ccrepo.design.md` §8 (Mike flagged mid-session)

§8 defers a *retention ledger* — persisting cost/usage rollups so ccrepo's
month/quarter views survive the ~30-day prune. I'd built ccarchive without seeing
it (the parallel session authored that doc, `e1b8e12`, after I'd started).
Reconciled: **ccarchive subsumes the ledger's *survival* purpose.** It keeps the
raw logs losslessly (~1.2 GB/yr) in a tree mirroring `~/.claude/projects/`, so any
historical view — ccrepo's time grouping included — recomputes at full fidelity
from the archive; a rollup ledger drops to a *precompute/speed* layer, not a
data-survival one. Open seam: `ccrepo`/`cctranscript` read `.jsonl` from the live
dir, not `.jsonl.gz` from the archive — a `--source <archive>` + transparent
gunzip (or a `ccarchive` hydrate mode) is what turns preservation into usable
extended history. Captured in `instruments/README.md`. I did **not** edit §8
itself — it's the parallel session's live design doc; the cross-pointer is queued
below rather than risk a collision on work in flight.

## Concurrency

Mid-session Mike flagged a parallel session live in the shared checkout (it had
landed `e1b8e12`, ccrepo v2). Moved this work to a worktree per CONCURRENCY:
`git stash -u` in the primary checkout (leaving it clean at `e1b8e12` for the
other session) → `git worktree add ~/worktrees/atelier-ccarchive -b ccarchive`
→ `git stash pop`. Not a queue item, so no claim needed.

## Verified

- 46 instrument tests green in the worktree (`node --test instruments/*.test.js`).
- Driven live end-to-end: dry-run, real archive, idempotent re-run, byte-identity
  round-trip, launchd RunAtLoad.

## Owed

- ⏳ **Cold review of the ADR 0006 addendum** (self-authored doctrine ⇒ rule 4:
  author must not spawn it). Pointer queued in ROADMAP. The code + machine wiring
  are tested and driven — self-verifying; only the doctrine delta gates.
- **`ccrepo.design.md` §8 cross-pointer** — add a note there that ccarchive
  supersedes the retention ledger's survival rationale (leaving it a precompute
  option). Left for the ccrepo/design session or a coordinated pass, since that
  doc is in flight in the parallel session; not edited from this worktree.
