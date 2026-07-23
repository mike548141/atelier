# 2026-07-23 · 0441 UTC · Orchestrated queue run — four items, one Opus session (Opus orchestrator)

Mike opened this session and pointed it at the queue with a standing brief:
*maximise plan use — pick unclaimed work, dispatch it, chain until the economics
say stop; use worktrees (parallel sessions live); Opus orchestrates, my choice of
agent tiers; if the orchestrator was opened on the wrong model, stop.* Opus is
the correct orchestration tier, so the run proceeded. This is the
`CONCURRENCY.md` § Orchestrated queue runs pattern executed live for the fourth
time.

## What landed — four items, each with a full per-item close

The tree opened clean with the last chain closed (apex + security-canon cycles
CLOSED). Claimed three items on `main` first (`95cd222`, `[~]` so parallel
sessions take other work), then ran a three-worker wave in isolated worktrees,
adding a fourth (ccrepo) once its file-set was free. **Workers ran no records:**
the orchestrator owned every `ROADMAP`/`SESSIONS`/`CHANGELOG` edit and every
merge to `main`, so worker branches never touched shared record files and merged
without conflict.

| Item | Tier | Landed | Close |
| --- | --- | --- | --- |
| cc-tools flag vocabulary audit | Sonnet | `6796f81` | table in `instruments/README.md`, zero drift; 🎯 rule-direction ratify queued for Mike |
| Apex three-element floor — in-repo sweep | Opus | `9040b02` | 6 surfaces aligned, floor blocks byte-identical (`test_templates` 32/32); fleet sweep split into the pin-bump lane |
| S3 datescan scanner | Sonnet | `04103a9` | `tools/datescan.py`, advisory-only (`--warn`, exit 0), 372 tools tests; ⏳ first-of-kind review queued |
| ccrepo rollup precompute ledger | Opus | `8a31b95` | 3.1× warm speedup, `rollup==recompute` proven live; 🎯 transparent-vs-opt-in queued for Mike |

Floor at head after the last close: tools 372, instruments 167, reviewscan +
linkscan exit 0, tree clean, 0/0 vs `origin/main`.

## The tier split behaved exactly as ECONOMICS predicts

- **Doctrine text → Opus.** The apex sweep is doctrine-text (QR5 — no scanner
  catches a wrong rule), so it stayed capable-tier. The worker's judgement was
  the payoff: it left dated records / review files / EVIDENCE.md's *accurate*
  single-element honesty citation untouched (rewriting them would falsify the
  record or break a faithful citation), and swept only live stale restatements.
- **Correctness-sensitive instrument → Opus.** The ccrepo ledger is a cost tool;
  a stale/miskeyed rollup is a silent-failure class. The worker earned the tier
  with a **design deviation**: it keyed **per-file, not per-period**, because a
  month can't be fingerprinted without first reading files for message timestamps
  (chicken-and-egg; file mtime ≠ message timestamp), so period-keying would
  misfile boundary-straddling sessions and break the `rollup==recompute` floor.
  Per-file `(mtime,size)` + a recipe-signature is provably exact; grouping runs
  downstream from true timestamps. Endorsed at review — more correct, same speed.
- **Third-seat executor trial (Mike, `dadde1d`) — run 1, both PASSED.** The two
  routine, well-floored items (cc-tools audit, S3 scanner build) went to Sonnet
  and cleared the orchestrator review with no hand-up and no rework: clean
  deliveries, floors green, and — notably — the cc-tools recommendation was
  *held as a recommendation* not baked as settled. First positive data point that
  Sonnet does these classes under the floor. **One run ≠ a standing tier claim**;
  the trial stays open for a second run's corroboration before promoting Sonnet
  to the standing executor seat (ROADMAP trial item carries the outcome).

## Orchestration mechanics that worked (extract, don't re-derive)

- **`isolation: worktree` workers + records-reserved-to-orchestrator** is the
  clean shape: each worker gets its own worktree (so its own cwd, tests, and
  commit Just Work), commits its *work files only*, and hands back a structured
  report; the orchestrator reads the diff, runs the floor, and merges per item.
  No worker touched `ROADMAP`/`CHANGELOG`/`SESSIONS`, so no record-file merge
  conflicts arose across four merges — the thing that would otherwise bite a
  parallel wave. Refines the standing "parallel agents, one worktree" +
  "queue-run orchestration mode" memories.
- **`git diff main..branch` is misleading once `main` advances** mid-run. After
  merging worker N, `main` moves; worker N+1's branch (cut earlier) then *appears*
  to revert N's files in a `main..branch` diff. The true worker delta is
  `git diff $(git merge-base main branch)..branch` — always diff against the
  merge-base to see what a worker actually changed, and trust the three-way merge
  to preserve the disjoint advances. Verified this way before each merge.

## Why the run stopped here (economics-judgement, not a cap)

Four substantial items landed with clean closes and two positive tier-trial data
points — a coherent batch. The stop is deliberate (`CONCURRENCY.md` stop
conditions — "or you do for other reasons"): the remaining unclaimed items are
either heavier and better as a **focused session** (fleet apex/floor propagation
is cross-repo; the V1–V7 checklist + two-layer acceptance criteria are one
doctrine cluster), or they'd **stack first-of-kind review debt** (each further
scanner S1/S2/S4/S5 earns its own ⏳). Chaining a fresh session is Mike's to do
(a run never starts its own successor). Budget was also consciously preserved for
a thorough wrap (the questions + learnings capture Mike asked for).

## Open for Mike (surfaced, not stepped over — the run report's job)

Newly surfaced by this run:
- 🎯 **cc-tools vocab rule direction** — ratify *flags-follow-operation* (the
  audit's recommendation, already in `instruments/README.md` marked "recommended")
  or steer to uniform-always.
- 🎯 **ccrepo transparent-vs-opt-in** — the ledger shipped transparent-by-default
  (`--no-rollup` bypass); confirm, or flip to opt-in (one predicate). Also flagged:
  the ~46 MB machine-local ledger the first warm run writes under `~/.claude/`.

Standing Mike-only items (unblocked, his to flesh out — not this run's to touch):
🎯 glossary ratify pass; honesty-vs-truth-vs-transparency (his raw apex note);
the Teams AI-chat grab.

⏳ queued this run: **datescan (S3) first-of-kind review** (delta `6077972`) — for
a later independent session; this chain authored it via dispatch, so it may not
take it (REVIEW rule 4 / QR2).
