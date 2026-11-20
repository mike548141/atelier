# 2026-07-17 · 2234 UTC · ccarchive — `--audit`, the live-store drift check

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 115+1 -->
- [2026-07-17 · 2234 UTC · ccarchive — `--audit`, the live-store drift check (Opus)](2026-07-17-2234-ccarchive-audit.md) — instruments backlog (Mike's theme); first of ccarchive's four open features. `--verify` checks the archive against its own manifest; **`--audit` checks the *live* store against the archive** — hashes every live `.jsonl` and buckets it: **synced** · **grown** (archived bytes a strict prefix — a plain append the next run captures; the classification that keeps the audit *honest not noisy*, so an active session between daily runs isn't a false "mutated") · **mutated** (rewritten/truncated) · **renamed** (content matched an archived path now gone from live; a still-present match is a copy, not a move) · **new** · **pruned**. Only mutated+renamed are drift (listed, non-zero exit); the rest counted. Read-only over both trees ⇒ no dest git-guard. Pure core (`auditCategorize` sha-bucketing + `classifyDivergence` prefix test) unit-tested; the runner bounds the gunzip IO to the sha-failed `changed` bucket. +11 tests (ccarchive 35→46, instrument 86; tool suite 247 green; mandoc + sizescan + linkscan clean). **Driven live**: 435 archived · 432 synced · 3 grown · 19 new · 0 drift → exit 0 (active sessions read as grown/new, the design goal observed). man AUDIT section + README + `--help`. No review owed (instrument diagnosis, writes nothing). Worked in `instruments-audit` worktree alongside a live main session (rebased onto its `dd51a14`→`7202b85`, disjoint files); landed `0b783ec`, worktree away. Next ccarchive item = **restore** (the writing cure to this read-only diagnosis; its own session + Mike's clobber-UX steer).


Instruments backlog session (Mike's themed steer). First of ccarchive's four
open features. Worked in an isolated worktree (`instruments-audit`) — a parallel
session was live on `main` the whole time (it claimed, released, and re-claimed
the ros/faves ROADMAP harvests: `dd51a14` → `7202b85`), so the claim went on
`main` first, the build stayed in the worktree, and the land rebased onto the
other session's commits (no conflict — disjoint files).

## The feature

`--verify` already answers *is the archive intact against its own manifest?*
`--audit` answers the other axis: *has the live store drifted from what was
preserved?* It hashes every live `.jsonl` and buckets it against the manifest:

- **synced** — live bytes match the recorded sha256 (the healthy majority).
- **grown** — the archived bytes are a *strict prefix* of the live file: a plain
  append since the last archive run. This is the classification that keeps the
  audit **honest instead of noisy** — an active session between daily archive
  runs would otherwise read as "changed/mutated" and cry wolf. Growth is normal;
  the next `ccarchive` captures it.
- **mutated** — live diverges from the archived copy by something *other* than
  growth: rewritten, or shrunk/truncated (a prefix *loss*). Real drift.
- **renamed** — a live file with no manifest entry whose content matches an
  archived transcript recorded under a different path that is *itself gone* from
  the live store (a match whose old path is still present is a copy, not a move).
- **new** — unarchived live file matching nothing archived (next run archives it).
- **pruned** — archived entry with no live counterpart (the expected steady state
  after Claude Code's cleanup).

Only **mutated** and **renamed** are drift: listed by name, non-zero exit.
grown/new/pruned are normal and only counted. Read-only over both trees — no
write path, so (unlike an archive run) no git-worktree dest guard is needed.

## Shape

Two pure, side-effect-free helpers do the thinking and are unit-tested straight:
`auditCategorize(manifest, liveList)` sha-buckets into synced/changed/renamed/
added/pruned (rename detection via a sha256→archived-rels index, only matching
paths absent from live); `classifyDivergence(archivedBuf, liveBuf)` is the
prefix test → `grown` | `shrunk` | `rewritten`. The runner (`auditLiveStore`)
does the byte reads: it hashes live files, and only for the `changed` bucket
does it gunzip the archived `.gz` to split grown from mutated — the expensive
IO is bounded to files that already failed the cheap sha check.

## Verified

- +11 tests (ccarchive 35→46; instrument suite 86 total), covering both pure
  helpers and eleven behaviour contracts (clean/rewritten/grown/shrunk/renamed/
  pruned/new + human output). Full tool suite 247 green; sizescan + linkscan
  clean; mandoc lint clean on the updated man page.
- **Driven live** against the real archive (435 archived): `432 synced · 3 grown
  · 19 new · 0 pruned · 0 mutated · 0 renamed → exit 0`, with the "run ccarchive
  to catch up" nudge. The active sessions (this one included) correctly read as
  grown/new, not false-alarm mutated — the design goal, observed.

Docs: man page gains an **AUDIT** section plus SYNOPSIS/OPTIONS/EXAMPLES/EXIT
STATUS entries; `instruments/README.md` and `--help` document it (`--help` held
at 22 lines, still one screen).

No review owed — instrument display/diagnosis change, self-verifying (ceremony
∝ risk; it writes nothing). Landed to `main` at the merge; worktree put away.

## Left for a later session

The natural next ccarchive item is **restore from archive** — audit is diagnosis,
restore is the cure, and `--audit`'s mutated/renamed/pruned buckets are exactly
the delta source a `--restore` delta mode needs (noted in the ROADMAP item). It's
a *writing-into-live-data* feature with clobber-safety (never overwrite a live
file newer than the archived copy) — deserves its own focused session and
possibly Mike's steer on the confirm/refuse UX, which is why this session stopped
after the read-only half.
