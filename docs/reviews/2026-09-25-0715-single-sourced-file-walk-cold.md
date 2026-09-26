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

---

## Verdict — phase 1 (FW), written 2026-09-26 UTC

### Provenance, repeated

- **How this reviewer was spawned:** a fresh Fable subagent (`claude-fable-5-1`) started
  by the batch orchestrator with this brief as its only framing. It is not the author's
  session and was not instructed by the author; the orchestrator holds the sibling, forms
  no finding and writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked.
- **Tier at claim:** `claude-fable-5-1`, checked before any file was opened.
- **What was read:** this brief; `docs/method/REVIEW.md` and `docs/method/00-APEX.md` at
  HEAD (`f81a98f`); the landing diff of `c1a2f12` via `git show` and the twelve delta
  files at HEAD (`git diff c1a2f12 HEAD -- <delta paths>` is empty, so HEAD is the landed
  text); `.githooks/pre-commit`, `tools/pre-commit.sample`, the docstring of
  `tools/floor.py`, `.github/workflows/ci.yml` in full and `floor.yml` by grep;
  `tools/README.md` by index, lines 368–382 and 1150–1156; the code regions of
  `licenscan`, `linkscan`, `sizescan`, `datescan`, `spellscan`, `stampscan`, `wrapscan`,
  `secretscan` and `reviewscan` cited under the findings; `tools/test_secretscan.py` by
  grep; CPython's `pathlib` source for 3.9 (local), 3.12 and 3.13 (fetched from the
  CPython repository); `.atelier-floor.json`'s `scope` block. Tree searches ran through
  `tools/coldsweep.py` with `--also-exclude` for the queue pointer, `115/080` and
  `115/220`.
- ⚠️ **Exposure, disclosed.** (a) `git status --short` in the shared worktree printed the
  names of four modified files belonging to other passes (three `2026-09-25-0715-*` briefs
  and one `160/` pointer) — names only, none opened. (b) One early `grep -rln filewalk`
  listed filenames only, among them the barred pointer and `115/080` (both named in this
  brief) and `115/220` (named in `548b706`'s file list) — no content read. (c) One early
  hand grep ran before I switched to `coldsweep`; it excluded records by path prefix and
  hit only `tools/`, `CHANGELOG.md` and `commands/`. (d) The `self-contained` sweep
  returned two one-line hits in `docs/roadmap/320-*` items, which are not barred. (e) A
  `pgrep` while waiting for the suite showed another reviewer's shell command line (a
  command, no brief content). No prior verdict, session record, `ROADMAP-DONE.md` or
  barred item was opened. (f) The full suite exceeded the tool's 600 s foreground limit
  and the harness moved it to the background; I did not choose a background run, and a
  sibling reviewer's suite was running beside it at the time.

### Lens 1 — approach & assumptions

The load-bearing assumptions, named by me and tested:

- **A1 — the eleven walks were one walk plus a skip-set parameter.** True at the parent
  commit. With the fixture tree below, `_walk_files` at `c1a2f12^` yields the same list
  for all ten common-set scanners and a list for `licenscan` that differs by exactly the
  six `dist`/`build` paths; at HEAD every scanner's yield is byte-identical to its own
  parent yield, raw order included (ledger rows 3–4).
- **A2 — `sys.path.insert(0, Path(__file__).resolve().parent)` reaches every consumer
  shape.** Verified five ways: the hook's env-pointed script, a symlinked script in a
  child's `bin/`, `floor.py --plane hook` from a scratch child, a by-path
  `importlib` load from a foreign cwd, and the child CI workflow, which checks out the
  whole of `mike548141/atelier` as a sibling directory and runs `atelier/tools/<s>.py`
  (ledger rows 7–8). `filewalk` resolved to the worktree's copy in every case.
- **A3 — one shared walk makes the next correction cheaper.** Tested against the one
  correction that has happened, `db9a785` (the `160/410` pruning line): it touched
  eleven scanner files (+159 lines: the one-line prune became a five-line comprehension
  plus a ten-line comment, eleven times) and eleven test files (+622 lines) — 22 files,
  +781 in all. At HEAD the same code change is one five-line comprehension in one file.
  **The proof half is not cheaper:** no test imports `filewalk`, so a walk correction is
  still proven eleven times through the wrappers, or not at all (FW3). The claim holds
  for code and is half-true overall.
- **A4 — "copyable alone" is a retired design.** It is retired in fact (every scanner now
  imports `filewalk`) but not in the text: nine comments across seven files still assert
  it, including `secretscan`'s design statement that a shared base should be factored
  "then, not speculatively now" — this delta is that base (FW4). The commit swept only
  `sizescan`'s copy.
- **A5 — the walk is "the same name/type check the skip set already makes, not a content
  decision".** Holds; the fixture shows no case where the shared walk reads content to
  decide.
- The brief's own framing, "eleven walks become one": two tree walks of the guard class
  remain outside the module — `linkscan`'s suggestion index and `reviewscan`'s record
  discovery — and the second is proven to carry the E9 defect the shared walk fixed
  (FW7). The framing is accurate for the eleven `_walk_files`; it is not the whole walk
  surface.
- **Non-goal check:** the only stated non-goal (funding of `115/080` part 2) fences off
  nothing this delta risks. The reader question is a genuine separate decision; counsel
  under FW10.

### Lens 2 — correctness & quality

`filewalk.py` and all eleven wrappers read in full. Every wrapper is the one-line
`return filewalk.walk_files(base, <own set>)`; `sizescan` passes `NON_CONTENT_DIR_NAMES`,
`licenscan` its twelve-name set, the other nine `SKIP_DIR_NAMES` — verified by grep and by
the cross-scanner diff. `import os` was dropped from nine scanners; a grep for `os.` in
those nine finds only a comment in `secretscan` (line 543), and every selftest and CLI run
below exercised the modules without a `NameError`. `leakscan` and `linkscan` keep the
import and use it.

**Fixture-tree results, per scanner** (Python 3.14.6; ledger row 3): all eleven
`IDENTICAL` parent vs HEAD — twenty files yielded by the ten common-set scanners,
fourteen by `licenscan`. Per skip path, at both commits:

| Fixture case | Walk behaviour |
|---|---|
| skip names at root and at depth (`docs/node_modules`, `src/dist`) | pruned |
| `.idea`, `.vscode` | pruned; `.hidden/`, `.github/` walked |
| files named `dist`, `build`, `node_modules_file.txt` | yielded (skip is dir-only) |
| `dist/`, `build/` | pruned by `licenscan` only |
| broken symlink | excluded |
| symlink to a directory, inside or outside the root | not descended |
| symlink to a file outside the root | **yielded and read** (FW6) |
| directory holding an ordinary file named `.git` | pruned |
| directory whose `.git` is a symlink to a file | pruned |
| nested plain clone (`.git` directory) | `.git` pruned, clone's content walked (FW9) |
| real linked worktree (`.git` file with `gitdir:`) | pruned entirely |
| unreadable file | yielded; reader behaviour differs (FW8) |
| unreadable directory | silently skipped on 3.14; **traceback on ≤ 3.13** (FW1) |
| unicode names (macrons, CJK, Cyrillic) | walked |
| empty directory | nothing |

**End-to-end** (ledger rows 5–6): each scanner run as a CLI at parent and HEAD, stdout,
stderr and exit code compared after normalising the tools path — identical for all eleven
over the fixture and over the whole scratch clone of HEAD. That re-drives the commit's
"byte-identical stdout/stderr/exit-code" claim on a second tree.

**`Iterable` + `set()` coercion** (ledger row 9): the coercion runs at the generator's
first `next()`, not at call time. A one-shot iterator drained between the call and the
first iteration, a second walk built from the same iterator, or a bare `str` each yield
an empty or character-wise skip set, and the walk descends into `.git` and
`node_modules` — measured 21 → 60 files. No live caller passes anything but a
module-level set, so this is a latent API hazard, not a live defect (FW5).

**Selftests** (ledger row 1): all eleven `OK`, plus `floor`, `floorfleet`, `signscan`,
`blockscan` and the CI loop's fifteen. **Full suite** (ledger row 2): `Ran 1564 tests in 1151.713s`, `FAILED (failures=4)` — the count matches the commit's 1,564; all four failures are `BoundedMemory` cases asserting "scan did not finish in time" (a fixed 60 s wall-clock probe) while six suites shared the machine. Re-run alone, the four pass 4/4 in 190 s with two sibling suites still live. Environment-gated, not a delta defect (FW11).

### Lens 3 — completeness / harvest

- **Own walks remaining.** `linkscan._build_basename_index` (`os.walk`, prunes only
  dot-directories, no skip set, no worktree prune — feeds broken-link suggestions, not the
  scan); `reviewscan` (`rglob("docs/reviews")` and `rglob("docs/decisions")`, no prune —
  proven to count a nested linked worktree's records, FW7); `pointerscan`
  (`rglob("*.md")` scoped to the board directory); `coldsweep` (`rglob("*")`, a reviewer
  tool with its own bar); `board` and `pins` (shallow `iterdir`); `harvestscan`,
  `publishscan` and `board` enumerate through `git ls-files`/`git diff` and need no
  walk; `blockscan` and `signscan` walk nothing; `floorfleet` uses a shallow glob; the
  `instruments/` fleet tools are Node and out of this module's reach by construction.
- **Documentation.** `tools/README.md` does not mention `filewalk.py`; its "Bounded
  memory" section still describes the walk as `secretscan`'s own, and its "Tests" line
  ("covers every tool here") is false for `filewalk` (FW2, FW3).
- **Child reach.** A child's hook resolves the scanner by path (`ATELIER_TOOLS` →
  `hooks.atelierTools` → in-repo), and the scanner resolves `filewalk` from its own real
  directory — so from atelier's `tools/`, on every plane, verified under lens 1 A2. A
  child that vendored a single scanner file would now fail at import, which ADR 0008
  already forbids; nothing in the tree documents that consequence (FW4 counsel).

### Lens 4 — security & privacy

`/security-review` is **discharged by grounds**: it reads the session's pending diff, which
in this shared worktree is other passes' unstaged drafts, and this is a landed-delta
review. The code-altitude read was delivered by hand against the OWASP Top 10 classes
that reach a file-walk surface — path traversal (A01), security misconfiguration (A05)
and logging/monitoring failures (A09):

- **Walking out of the root.** Directory symlinks: `os.walk` defaults to
  `followlinks=False`; the fixture's in-root and out-of-root directory links were not
  descended. File symlinks: `p.is_file()` follows the link, so a symlink whose target is
  outside the root is yielded and read (FW6, pre-existing, matches the pre-020/380
  `rglob` filter). `leakscan`'s human render prints `path:line ... → excerpt`, so a
  tracked symlink at a private file would echo an excerpt of it into hook output; on CI
  the target does not exist. Bounded, local, and a design choice for part 2.
- **Widening the skip set from a child's config.** Not possible: each skip set is a
  module-level constant; `.atelier-floor.json` and `floor.py` carry no skip key; the
  `.<scanner>ignore` files are a separate, root-relative glob mechanism applied after
  the walk. A child cannot reach `skip_dir_names` without editing atelier's tools.
- **The `.git`-file prune as a hiding primitive.** Any directory containing a plain
  file or a symlink named `.git` is invisible to all eleven walks. Bounded by git
  itself: `git add hide/.git` exits 0 and indexes nothing (verified), so the hiding file
  cannot reach a CI checkout, and the hook plane's boundary scanners read the staged
  diff, not the tree. Residual: local whole-tree runs only. Noted, not a finding.
- **Unreadable inputs are not reported.** An unreadable **file** is yielded by the walk
  and then silently skipped — with a clean verdict — by seven of eleven guards, including
  `secretscan` and `leakscan`; `conflictscan`, `linkscan`, `pathscan` and `stampscan`
  report it and exit 2 (FW8). An unreadable **directory** is silently skipped by
  `os.walk` (`onerror=None`) on 3.14 and crashes the walk on ≤ 3.13 (FW1). Bounded:
  git refuses to add an unreadable file (verified, exit 128), and a checkout is
  readable; a tracked file made unreadable afterwards commits fine (verified), so the
  exposure is the honesty of a local hook run's report.

### Findings

**FW1 — MODERATE (pre-existing; single-sourced by this delta).** `Path(dirpath, d,
".git").is_file()` raises `PermissionError` when `d` is a directory the process cannot
search, on every Python before 3.14: verified live on 3.9.6 (all eleven scanners exit 1
with a traceback over the fixture); confirmed by source for 3.12 and 3.13, whose
`Path.is_file` re-raises any `OSError` not in `(ENOENT, ENOTDIR, EBADF, ELOOP)`; 3.14's
`is_file` delegates to `os.path.isfile`, which swallows it. The house CI pins 3.12. A CI
checkout cannot contain an unreadable directory, so the live exposure is the hook plane
on a machine running ≤ 3.13 with such a directory in the tree (a root-owned build output,
a mounted volume): every commit is blocked with a traceback rather than a report. The
direction is fail-closed, which is the right side; the shape is a crash, which is not.
Introduced by `db9a785` in eleven copies; now one line. *Counsel:* guard the `.git`
check with `try/except OSError` and pass an `onerror` callback to `os.walk` that counts
or names the directory it could not enter, so the skip is reported rather than silent
(the same class as FW8). *Recurrence prevention:* a `chmod 000` directory case in a
`filewalk` test, run on the CI interpreter.

**FW2 — minor.** `filewalk.py` is undocumented in `tools/README.md`: no entry in the
tool index, the "Bounded memory" section (lines 368–382) still attributes the streamed
walk to `secretscan` alone, and the "Tests" section's "covers every tool here" is untrue
for it. The module's own docstring is thorough; the README is where a child's operator
looks.

**FW3 — MODERATE.** The shared module has no test of its own contract: no `test_filewalk`
exists and no test imports `filewalk`. The eleven E9 tests from `db9a785` prove only the
`.git`-file prune, each through its own wrapper; `test_secretscan` adds one "a content
directory named `build` is walked" case. Broken symlinks, directory and file symlinks,
unreadable files and directories, skip names at depth, files named like skip
directories, unicode names — none has a proof anywhere in the suite. This pass's fixture
found FW1 and FW8 on first contact. The module's stated purpose is that the next
correction lands once; without a single-sourced proof it is still proven eleven times
or not at all (lens 1, A3). *Counsel:* a `test_filewalk` built from the fixture in this
verdict's ledger (row 3 names every case); keep the per-scanner E9 tests as
wrapper-passthrough proofs.

**FW4 — minor.** Stale "self-contained / copyable alone" claims survive the delta in
nine places across seven files: `secretscan.py` 67–70 (the design statement — "each
self-contained so a peer can copy either one alone … if a third scanner ever lands,
factor a shared base then, not speculatively now"; the eleventh landed and this commit is
that base) and 643–644; `datescan.py` 501, `linkscan.py` 277, `spellscan.py` 504,
`stampscan.py` 450, `wrapscan.py` 392 (each: readers "duplicated rather than imported so
this scanner stays copyable alone" — true of the reader, false of the scanner, which now
imports `filewalk`); `floor.py` 680 and `test_floor.py` 1275 ("self-contained by
design"). The commit's message says one stale `sizescan` comment was corrected; the
class was not swept (`PRINCIPLES.md` §6). ADR 0008 already forbids vendoring, so the
retired design was already retired; the text should say so where it says the opposite.

**FW5 — minor.** `walk_files` is a generator, so `set(skip_dir_names)` runs at the first
`next()`, and the `Iterable[str]` annotation admits a bare `str`. Proven: a drained
one-shot iterator, a second walk built from the same iterator, and `"node_modules"`
passed as a string each silently yield no pruning (21 → 60 files, `.git` and
`node_modules` entered). No live caller is affected — all eleven pass a module-level
`set` — but the failure mode is silent and fail-open, the pair the house treats as
worst. *Counsel:* make `walk_files` a plain function that coerces eagerly with
`frozenset()`, rejects `str` explicitly, and returns an inner generator; one test each.

**FW6 — note (pre-existing; security lens).** A symlink to a file outside the root is
yielded and read; directory symlinks are not followed. Same behaviour as the
pre-020/380 `rglob` filter and as the parent commit. Threat: a tracked symlink at a
private file makes a hook-plane guard read and excerpt it locally; nothing reaches CI.
A per-guard design choice (`not p.is_symlink()`, or resolve-and-check-under-root) that
belongs with `115/080` part 2, not a fix in passing.

**FW7 — minor (outside the delta; the class the delta exists to end).** `reviewscan`
discovers `docs/reviews` and `docs/decisions` with `rglob`, no skip set and no worktree
prune. Proven: over the fixture, whose only `docs/reviews` and `docs/decisions` live
under the nested linked worktree, it reported 136 review briefs and 5 decision records
as this tree's — the E9 double-count. In atelier itself, where harness worktrees nest in
the repo, a sibling session's in-flight brief can red `reviewscan` on the primary
checkout. `linkscan._build_basename_index` has the same shape but only feeds
suggestions. *Counsel:* route both through `filewalk` (a directory-yielding variant, or
match `docs/reviews` on the walked path) so the prune is single-sourced for every guard
that walks.

**FW8 — MODERATE (pre-existing; security lens; reader-side).** An unreadable file is
skipped in silence and the run reports clean by seven of eleven guards — `secretscan`,
`leakscan`, `sizescan`, `datescan`, `wrapscan`, `spellscan`, `licenscan` — while
`conflictscan`, `linkscan`, `pathscan` and `stampscan` name it on stderr and exit 2.
Every tally line counts allow-markers, ignore hits and truncation, and none counts a
file it could not open: identical output for materially different cover, the EP3 class
this house already names. Bounded: git will not add an unreadable file, and CI
checkouts are readable, so the exposure is a tracked file made unreadable afterwards on
a local hook run. The defect sits in the readers, which is `115/080` part 2's surface;
it is recorded here because lens 4 asked the question and the answer is no. *Counsel:*
count `files_unreadable` in every tally beside `files_truncated`, and rule per guard
whether it is exit 2 as four already do.

**FW9 — note (pre-existing).** A nested plain clone has its `.git` directory pruned but
its content walked and scanned; a nested linked worktree is pruned whole. Two answers to
"a second repository inside this one". Defensible either way; worth one line of design
intent in the module docstring, which describes the worktree case and not the clone.

**FW10 — note (counsel, as the brief asked).** The seam is more legible than either
endpoint: the walk is one thing with one docstring, and the readers beside it are
visibly three shapes plus `linkscan`'s fenced-block state, named honestly in that
docstring and in `115/220`. What makes it less legible is FW4 — seven comments still
say the readers are duplicated "so this scanner stays copyable alone", which now reads
as a contradiction beside `import filewalk`. Counsel: part 2 should decide the reader
question on its own evidence; this delta did not pre-empt it, and should not be read as
having settled it.

**FW11 — note (outside the delta; environment).** The four `BoundedMemory` tests in
`test_leakscan`, `test_secretscan`, `test_spellscan` and `test_pins` bound their probe
with a fixed 60 s wall-clock timeout and fail — as a memory assertion would — when the
machine is contended: four false failures in a 1,152 s run with six suites live, 4/4
green alone. A timeout that fails the *memory* test under CPU contention is the
"identical output for materially different causes" shape one surface over. *Counsel:*
report `timed_out` as a skip-with-reason, not a failure, or scale the bound to the
small run's measured wall time.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE (FW1, FW3, FW8) · 4 minor (FW2, FW4, FW5,
FW7) · 4 note (FW6, FW9, FW10, FW11).** The delta does what it claims: eleven walks reproduce
their parent behaviour exactly on a tree that exercises every skip path, the wrappers
pass exactly their old parameters, and the module reaches every child shape. The three
MODERATE findings are two pre-existing defects the single source now makes cheap to fix
and one missing proof that the single source needs to earn its stated purpose. No
finding challenges the approach. The cycle may close on this pass under REVIEW.md's
no-MAJOR rule once the rulings are recorded.

### Re-run ledger

All commands ran from the shared worktree at `f81a98f` or from the scratch area
`…/scratchpad/FW/` (the scratch clone `probe/` is a clone of the worktree; `parent_tools/`
is `git archive c1a2f12^ tools`; `fixture/` is the tree described under lens 2).
Interpreter: Python 3.14.6 unless stated.

| # | What | Command (abridged) | Result |
|---|---|---|---|
| 1 | eleven `--selftest` + CI selftest step | `python3 tools/<s>.py --selftest` ×11; `floor.py --selftest`; `floorfleet.py --selftest`; `signscan.py --selftest`; `blockscan.py --selftest`; the `ci.yml` loop over `floor.py --list --plane ci` (15) | all exit 0, `selftest OK` |
| 2 | full Python suite, once | `python3 -m unittest discover -s tools -p 'test_*.py'` | `Ran 1564 tests in 1151.713s`, `FAILED (failures=4)` — the count matches the commit's 1,564; all four failures are `BoundedMemory` cases asserting "scan did not finish in time" (a fixed 60 s wall-clock probe) while six suites shared the machine. Re-run alone, the four pass 4/4 in 190 s with two sibling suites still live. Environment-gated, not a delta defect (FW11). |
| 3 | walk-yield diff, parent vs HEAD, per scanner | `walkdump.py <tools> <s> fixture` ×22, `cmp` per scanner | 11/11 IDENTICAL (20 files; `licenscan` 14) |
| 3a | same under Python 3.9.6 | `PY=/usr/bin/python3` | 22/22 `PermissionError` at `unreadable_dir/.git` (FW1) |
| 4 | cross-scanner at HEAD | `cmp head.secretscan head.<s>` | 9 identical; `licenscan` differs by the 6 `dist`/`build` paths only |
| 5 | CLI end-to-end over fixture | `<s>.py --root . .` (licenscan: `.`) at parent and HEAD; stdout+stderr+exit compared | 11/11 IDENTICAL |
| 6 | CLI end-to-end over the scratch clone (HEAD content) | as row 5 | 11/11 IDENTICAL |
| 7 | child-shaped runs | `ATELIER_TOOLS=<wt>/tools python3 "$ATELIER_TOOLS/secretscan.py" --root . .`; symlinked `bin/secretscan`; `floor.py --plane hook --root <child> --tools <wt>/tools`; by-path `importlib` load from a foreign cwd | all resolved `filewalk` to the worktree's copy; floor exit 0 |
| 8 | child CI shape | `.github/workflows/floor.yml` by grep | whole-repo checkout of atelier as a sibling; runs `atelier/tools/<s>.py` |
| 9 | coercion hazards | `probe_iterable.py fixture` | drained iterator 60 vs 21; str 60; coercion at first `next()` |
| 10 | unreadable-file reporting | `probe_unreadable.sh` (unreadable `docs/unreadable.md`, 11 HEAD CLIs) | 4 report + exit 2; 7 silent + clean (FW8) |
| 11 | git bounds | `git add hide/.git` (file, symlink); `git add` unreadable; add-then-chmod-000 commit | 0 but not indexed; 128; commits (FW1/FW8 bounds) |
| 12 | `pathlib` sources | local 3.9 `_IGNORED_ERROS`; fetched 3.12 `Lib/pathlib.py`, 3.13 `Lib/pathlib/_abc.py` + `_local.py` | ≤ 3.13 re-raise EACCES; 3.14 `os.path.isfile` |
| 13 | floor, hook plane | `floor.py --plane hook --root <wt> --tools <wt>/tools` | exit 0; 11 ✅ enforced, 3 👁️ warn-only, licenscan ✅ |
| 14 | floor, CI plane | `floor.py --plane ci --root .` + `stampscan.py --warn --root . .` + `blockscan.py --check --warn --root .` | exit 0 / 0 / 0; secretscan 🟡 22 advisory, leakscan 🟡 structural-only (expected) |
| 15 | reviewscan's own walk | `reviewscan.py --root .` over fixture | exit 0, "136 review brief(s) … 5 decision record(s)" — all under `linked_wt` (FW7) |
| 16 | sweeps | `coldsweep.py --root . --also-exclude ×3 '<pattern>'` for `copyable alone|self-contained`, `filewalk`, `_walk_files`, `skip_dir|SKIP_DIR|NON_CONTENT_DIR` | 18 / 34 / 70 / 48 hits; 349 files barred |
| 17 | prior correction's cost | `git show --numstat db9a785` | 11 scanners +159; 11 tests +622; 22 files +781 |

Not re-run: the walk under Python 3.12 (the CI interpreter) — not installed on this
machine; FW1's 3.12 claim rests on source, and is marked so.

### Follow-up checklist

- [ ] FW1 — guard the `.git` check against `OSError` and report un-enterable
      directories; test on the CI interpreter.
- [ ] FW3 — a `filewalk` test built from the ledger's fixture cases.
- [ ] FW8 — count unreadable files in every tally; rule per guard on exit 2.
- [ ] FW4 — sweep the nine stale "copyable alone / self-contained" claims.
- [ ] FW2 — `tools/README.md` entry for `filewalk.py`; correct the "Tests" line.
- [ ] FW5 — eager `frozenset` coercion, `str` rejected, tested.
- [ ] FW7 — route `reviewscan` (and `linkscan`'s index) through the shared walk.
- [ ] FW11 — make the memory probes' timeout a skip, or ground the bound.
- [ ] FW6, FW9 — record the design intent (symlinked files; nested clones) with
      `115/080` part 2, where the reader decision is taken.
- [ ] Orchestrator: record the rulings against this verdict and tick the pointer; no
      queued pointer is owed if the cycle closes here (no MAJOR).

### Reconcile

Written 2026-09-26 UTC after phase 1 was committed at `4a6a11a`. Opened at this
step, in this order: the sibling's text (the pointer's four lens hints, verbatim;
the brief-writer seeded nothing beyond them), the queue pointer `160/420`, the funded
item `115/080`, the three-mechanisms item `115/220`, and the named intent record
`docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md` in full. Nothing in the
phase-1 text above has been revised.

**A note on the intent record before the per-finding notes.** The pointer names the
2026-09-20 1053 session record as the delta's intent record. That record carries no
account of `115/080` part 1, of `020/160`'s E9 fix, or of the harness at all — its
only mention of `115/080` is as a loose end selected at open — and it has no closing
block. The account this reconcile could test against lives in `115/080`'s own
"PART 1 LANDED" block and the landing commit's message; both were used below.

**Against the pointer's four lens hints** (the author's framing; anticipated means the
author named the risk, not that the author found what the finding found):

1. *Is the byte-identical evidence as strong as it reads, taken on one tree with no
   `dist/`, `build/` or broken symlink?* Anticipated. Answered by the fixture (lens 2):
   with all three present, plus every other skip path, the eleven walks are still
   identical by correctness, not accident — `licenscan`'s parameterisation and the
   `is_file()` filter both do what the wrapper text says. The hint's instinct was
   right in a way it did not name: the one-tree evidence could not show FW1, which no
   real checkout can exercise and the fixture showed on the first run under 3.9.
2. *Can `skip_dir_names` be passed something whose iteration is not repeatable?*
   Anticipated exactly; FW5 is the measured answer (yes; silent; latent, because every
   live caller passes a set). The hint under-states the second half of the hazard —
   a bare `str` — which the `Iterable[str]` annotation invites.
3. *Is the next correction cheaper in fact or in principle?* Anticipated as
   "testable rather than asserted", and tested (lens 1 A3): cheaper in fact for the
   code, not for the proof. FW3 is where the hint lands.
4. *Do four readers left beside one walk confuse more than either endpoint?*
   Anticipated, and delegated to `115/220`. FW10 is the counsel; FW4 is the concrete
   confusion (comments that now contradict the import beside them).

**Against `115/080`'s funded scope** — "the walk and its parameters", share the
mechanism never one constant, every scanner's output proved unchanged, suite green,
part 1 the lowest-risk slice:

- The scope was honoured: the cross-scanner diff proves the per-guard set survived
  (ledger row 4), and the worker's refusal to fold the readers in — recorded there
  as "Part 1's scope as written was WRONG" — is the decision this verdict's FW10
  endorses.
- Its evidence claims re-drive: "byte-identical stdout, stderr and exit code" holds
  on a second tree and on the fixture (rows 5–6); "suite 1,564 tests OK" — the count
  matches, and the four failures in my run are environment-gated (FW11), not the
  delta's; "twenty-two files for one line" is my own count for `db9a785` (row 17).
- Its claim that "the standing suite already carries a per-scanner regression test
  for it — the floor, not a scratch probe" is true of the E9 prune only, and is the
  point FW3 contests: eleven wrapper tests are not a proof of the shared module.
  **FW3: not anticipated; the item accepted per-scanner tests as sufficient.**
- Its own corrected count ("eleven, not ten") was made by `_walk_files` name. FW7
  shows a twelfth tree walk of the guard class outside that name, with the E9 defect
  intact. **FW7: not anticipated** — the same count-by-memory shape `115/220` warns
  about, one step over.
- FW1, FW6, FW8, FW9 (unreadable inputs, symlinked files, nested clones) are
  **unaddressed** there: neither anticipated nor rejected; the item's frame is
  consolidation of plumbing, and none of these is a consolidation question. They
  are the cases a single source now makes cheap to decide, which is the item's own
  argument for existing.
- FW2 and FW4 (README, stale claims): **not anticipated**; the landing block records
  one `sizescan` comment corrected and no sweep of the class.
- FW5: **anticipated** by the pointer, not by the item.

**Against `115/220`** — the readers are four shapes, shape 3 (five truncation-only
readers) "already literally identical across all five" and the safest candidate:

- FW10 is **anticipated in full**; my counsel matches its ranking (shape 3 cheap,
  shapes 1 and 4 plausible, shape 2 wait for `linkscan`'s fence state).
- FW8's per-guard split does **not** follow the shapes: inside shape 1,
  `conflictscan` reports an unreadable file and exits 2 while `secretscan` and
  `leakscan` go silent; inside shape 3, `stampscan` reports and the other four go
  silent. So the five shape-3 readers are identical in their constants and not in
  their error path — see FW13 below.

**Findings formed at reconcile** (numbered on from FW11; marked as such):

**FW12 — minor (formed at reconcile; records, outside the delta).** The intent record
the pointer names carries no account of the work and no closing block. The run that
landed part 1 (claimed at 2026-09-20 2239 UTC per `115/080`, landed 2026-09-21 NZ)
left its account only in the board item and the commit message; the session index
has no entry dated 2026-09-20 or later. A pointer that is refs-only by rule is only
as good as the record it references. *Counsel:* the orchestrator, when folding,
should either add the closing block to the 1053 record or note in the pointer that
the intent lives in `115/080`'s landing block, so the next reader is not sent to a
record that does not answer.

**FW13 — note (formed at reconcile; feeds `115/220`).** The reader shapes diverge on
the error path where they agree on constants: one shape-1 reader and one shape-3
reader treat an unreadable file as a configuration error (stderr line, exit 2); the
rest skip it and report clean (ledger row 10). `115/220`'s "safest candidate" claim
for shape 3 therefore has one behavioural decision inside it that consolidation
would force — which of the two error policies the shared reader takes — and that
decision belongs in the ruling `115/220` asks for, alongside FW8's counsel to count
the skip either way.

### Overall, restated

**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE (FW1, FW3, FW8) · 5 minor (FW2, FW4, FW5,
FW7, FW12) · 5 note (FW6, FW9, FW10, FW11, FW13).** Reconcile changed no phase-1
severity. Of the eleven phase-1 findings, four were anticipated by the author's
framing (FW3, FW5, FW10, and FW1's one-tree gap in spirit), none was rejected there,
and six were unaddressed by any record opened. The cycle may close on this pass
under the no-MAJOR rule once the rulings are recorded.

## Deferred material — folded in at reconcile

# Deferred material — single-sourced-file-walk (open only after your findings are durably written)

Sibling of `docs/reviews/2026-09-25-0715-single-sourced-file-walk-cold.md` under
REVIEW.md rule 1's split; held by the orchestrator outside the worktree. Folded
into the brief below the verdict when the verdict lands.

## Intent records

- `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md` — the run's
  account. **Partially read** (not this section).
- `docs/roadmap/115-*/080-*.md` — the funded item (GA1) with the principal's
  scope. **Not opened.**
- `docs/roadmap/115-*/220-*.md` — the *three mechanisms, not one with
  parameters* item filed at landing. **Not opened.**

## Prior verdicts and barred items on the same surfaces

- `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md` (⚠️ head and tail
  read by the brief-writer on 2026-09-20; not this section)
- the board items `docs/roadmap/115-*/080-*.md` and
  `docs/roadmap/115-*/220-*.md`

## The queue pointer's own lens hints — the author's seeded questions, verbatim

**The lenses that matter most here:** whether the byte-identical
before/after evidence is as strong as it reads, given it was taken on
one tree whose content may not exercise every skip path — a tree with no
`dist/`, no `build/` and no broken symlinks would show `licenscan`'s
parameterisation and the `is_file()` filter as identical by accident
rather than by correctness; whether `skip_dir_names` being accepted as
any `Iterable` and coerced with `set()` can be passed something whose
iteration is not repeatable, since the walk consumes it once per call
but is itself a generator; whether one shared walk makes the **next**
correction cheaper in fact or merely in principle, which is this item's
whole justification and is now testable rather than asserted; and
whether consolidating the walk while leaving four distinct readers
copied alongside it leaves the codebase more confusing than either
endpoint, which is `115/220`'s open question reaching back into this
delta.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these; a question you did not think of is a
prompt to re-read the surface, not an agenda.

None beyond the pointer's own.
