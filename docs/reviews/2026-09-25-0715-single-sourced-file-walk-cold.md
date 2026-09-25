# Cold pass — the single-sourced file walk — eleven scanner walks become one `filewalk.py`

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/420-rule-4-cold-pass-queued-the-single-sourced-file-walk.md`.
**Why it earns a review:** every file-reading guard in the fleet now walks the
tree through one function; a skip path that the shared walk gets wrong is wrong
in eleven guards at once, and the byte-identical before/after evidence was taken
on one tree.

## Spawn provenance

- **Author of the work under review:** the session(s) that landed the commits
  named under *What the work is*. This brief-writer was not that session, was
  neither started nor instructed by it, and has edited none of the delta's
  paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-09-20 and
  re-pointed on 2026-09-24 with the prompt "Please deliver all fable dependent
  work, and work that would be best delivered using fable", on the Fable tier
  (`claude-fable-5-1`), orchestrating this batch of twenty rule-4 passes. It
  wrote this brief from the queue pointer, the landing commits' subjects and
  file lists, and the delta paths' names; it did not open the intent record or
  any prior verdict on these surfaces.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree, commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the `docs/SESSIONS.md` index entries of 2026-09-11 to 2026-09-19
  (the last three summarise the 2026-09-18 and 2026-09-19 runs in the authors'
  words); the first 30 lines and the last ~3,000 characters of
  `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`, read during an
  interrupted-session sweep on 2026-09-20; every queued `⏳` pointer on the board
  in full, including each pointer's own "lens that matters" paragraph — that
  paragraph is the author's framing and has been moved to this pass's sibling;
  the pass file `docs/reviews/2026-08-17-1000-coldsweep-cold.md` in full (brief
  and verdict) and lines 1–80 of
  `docs/reviews/2026-08-21-0820-pointing-up-cold.md`, both as formatting
  templates; the landing commits' subjects and `--stat` file lists (never the
  diffs); and, as doctrine read at onramp, `docs/method/CONCURRENCY.md` §§ *On a
  split board*, *Claiming at a dirty primary checkout* and *Surviving an
  interrupted session*, `docs/method/REVIEW.md` and `docs/method/00-APEX.md` at
  HEAD. Per-pass additions are marked ⚠️ under *Deferred reading*.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `c1a2f12` / `a59e5d0` (2026-09-21 NZ) — the landing commits; `548b706`
  corrected the item's scope (board only)

Delta paths:

- `tools/filewalk.py` (new)
- the `_walk_files` wrapper and the dropped `import os` in
  `tools/secretscan.py`, `leakscan.py`, `conflictscan.py`, `linkscan.py`,
  `sizescan.py`, `datescan.py`, `wrapscan.py`, `spellscan.py`, `pathscan.py`,
  `licenscan.py`, `stampscan.py`

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the shared walk reproduces each of the eleven former walks **exactly**,
on a tree that exercises every skip path — build one in your scratch clone with
`dist/`, `build/`, `node_modules/`, hidden directories, a broken symlink, a
symlinked directory, a directory holding an ordinary file named `.git`, a nested
clone, a linked worktree, a file with no read permission, and unicode names —
and diff each scanner's yielded file list at `c1a2f12^` against HEAD (check out
the parent in the scratch clone). Whether `skip_dir_names` accepting any
`Iterable` and coercing with `set()` is safe when the caller passes a one-shot
iterator and the walk is itself a generator. Whether each wrapper passes exactly
the parameters its old walk used (`licenscan`'s parameterisation especially).
Whether the four distinct readers left beside the walk make the seam more or
less legible than either endpoint — counsel, not a verdict. **Non-goal:** the
principal's funding of `115/080`; part 2 is not built.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   delta's justification is that one shared walk makes the *next* correction
   cheaper — test that claim against the one correction that has already
   happened (`db9a785`'s pruning line, `160/410`): count what it took across
   eleven files and what it would take now.
2. **Correctness & quality.** Read `filewalk.py` and all eleven wrappers. Run
   every selftest and the full suite. Run the fixture-tree diff in *Scope* for
   all eleven scanners and record the per-scanner result.
3. **Completeness / harvest.** Which scanners still carry their own walk
   (`harvestscan`, `reviewscan`, `publishscan`, `pointerscan`, `board`,
   `blockscan`, `signscan`, the fleet tools)? Is `filewalk.py` documented in
   `tools/README.md` and reachable by a child via `$ATELIER_TOOLS` (a child's
   hook imports the scanner, which imports `filewalk` — from where)?
4. **Security & privacy** — mandatory. The walk decides which files every guard
   reads. Check symlink handling cannot be used to walk out of the root, that
   the skip set cannot be widened by a child's config into hiding a secret, and
   that an unreadable file is reported rather than silently skipped. The house
   scanner is discharged by grounds (landed delta; pending = other passes'
   drafts) — say so, and deliver the code-altitude read by hand.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- every listed scanner's `--selftest`; the full Python suite once
- the eleven-scanner fixture diff in *Scope*, parent vs HEAD, in a scratch clone
- a child-shaped import: run one scanner from a scratch child with
  `ATELIER_TOOLS` pointed at the worktree's `tools/`
- the floor on both planes at HEAD

## House rules for this run

- You work in the shared review worktree
  `/Users/mike/worktrees/atelier-review-batch-0925` (branch
  `review-batch-0925`), read-only except for THIS brief file. Other reviewers
  are working there at the same time on their own briefs; never open another
  `docs/reviews/2026-09-25-0715-*` file — it is another pass's framing.
- Run **no git command that writes** in the worktree (no add, commit, stash,
  checkout, worktree, reset, clean). Read-only git (`log`, `show`, `diff`,
  `blame`, `branch -r`) is fine. Mutation probes, checkouts of older commits,
  scratch children and scratch linked worktrees go in your own clone: `git clone
  <worktree> <scratchpad>/<PREFIX>/probe` under the session scratchpad, named by
  your prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full Python suite
  (`python3 -m unittest discover -s tools`, in the foreground, ~minutes) at most
  once, never scan any tree outside the worktree or your scratch clone, and
  never point a scanner at the machine's other repos.
- `/security-review` is **discharged by grounds** for this batch: it reads the
  session's pending diff, which in the shared worktree is other passes' unstaged
  drafts, and this is a landed-delta review. State that line in your lens-4
  answer and deliver the code-altitude read by hand, checked against the OWASP
  catalogue where the work has a code surface.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" tree-wide,
  and would block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ
  English. Never quote a secret, a placeholder token, an email address or any
  personal detail — this repo is PUBLIC; describe, don't quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/420-rule-4-cold-pass-queued-the-single-sourced-file-walk.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md` (⚠️ head and tail
  read by the brief-writer on 2026-09-20; not this section)
- the board items `docs/roadmap/115-*/080-*.md` and
  `docs/roadmap/115-*/220-*.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/420-rule-4-cold-pass-queued-the-single-sourced-file-walk.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `FW`: `FW1`, `FW2`, …) and severities (MAJOR / MODERATE
/ minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with the commands and their results, and a follow-up checklist.
Then STOP and report to the orchestrator that phase 1 is written. Do not open
the sibling (it is not in the tree); do not edit the queue pointer, the board,
or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
records, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

The author is not the taker, so record every finding and apply nothing; counsel
on fixes is welcome, labelled as counsel.
