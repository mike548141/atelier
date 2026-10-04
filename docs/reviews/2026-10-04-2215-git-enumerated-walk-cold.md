# Cold pass — the file walk enumerates through git

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-04 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/600-rule-4-cold-pass-queued-git-enumerated-walk.md`.
**Why it earns a review:** every file-reading guard in the fleet takes its file
list from this one function; a file the new enumeration drops is a file no
secret, leak or licence guard reads, in this repo and in every child that calls
the floor.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-04 UTC
  with the prompt "Do all cold reviews and any other work dependent on fable",
  on the Fable tier (`claude-fable-5-1`), orchestrating three rule-4 passes
  (code passes from a seventeen-pointer queue; the principal sized this sitting
  to the weekly allowance he had left). It wrote this brief from the queue
  pointer, the landing commits' subjects and file lists, and the delta paths'
  names; it did not open the intent record or any prior verdict on these
  surfaces.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree and outside
  the harness scratchpad, commits the reviewer's phase-1 findings unrevised,
  then releases the sibling's text by message; the reviewer appends a reconcile
  section; the orchestrator folds the sibling in and updates the pointer. The
  orchestrator forms no finding and writes no severity. Both seats are Fable, so
  the off-tier clause is not invoked; the shape is stated anyway so the record
  is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the tail of the `docs/SESSIONS.md` index (entries of 2026-09-25 to
  2026-10-03), which includes the authoring run's own one-paragraph summary of
  its work and the 2026-10-03 review session's summary naming finding MC1 in one
  line; every queued `⏳` pointer in section 160 in full (each is refs-only); the
  brief half of `docs/reviews/2026-10-03-0357-manifest-checkpoints-cold.md`
  (lines 1–140, no verdict text) as a formatting template; the landing commits'
  subjects and `--stat` file lists (never the diffs); its own cross-session
  memory notes, which carry the principal's standing words on exceptions and
  guards; and, as doctrine at onramp, `docs/method/ECONOMICS.md` § the
  self-check and the headings of `docs/method/REVIEW.md`. Everything evaluative
  it knows about this delta is in the sibling, not here.

## What the work is

Landing commits (diff these; review the paths at HEAD, `3d4fd9d` or later):

- `ef43deb` (2026-10-03) — filewalk: enumerate files through git; landed in
  merge `bd9bd49`

Delta paths:

- `tools/filewalk.py`
- `tools/test_filewalk.py`

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the set of files the walk yields at HEAD is exactly the set it should
be, on every tree shape — build them in your scratch clone and compare the
yielded list against the parent commit's walk and against what you judge
correct: untracked-but-not-ignored files, ignored files, files staged but not
committed, files deleted from the worktree but still in the index, files in the
index marked assume-unchanged or skip-worktree, sparse checkouts, submodules and
nested clones, linked worktrees, symlinks (to files, to directories, broken, and
out of the root), names with spaces, newlines, leading dashes and non-UTF-8
bytes, a tree with no `.git`, a bare or corrupt repository, a root that is a
subdirectory of a repository, a root outside any repository, `git` absent from
`PATH`, and `GIT_DIR` / `GIT_WORK_TREE` / `core.quotePath` / a hostile
`.gitattributes` or config set in the environment. For each: what is yielded,
what is silently dropped, and whether a fallback exists and says it was taken.
Whether a guard can now be blinded by a `.gitignore` line — a secret in an
ignored file is not committed, but a file force-added past an ignore rule is.
Whether every caller's parameters still mean what they meant. **Non-goal:** the
decision that guards should read only what git could commit.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   "What git could commit" is a claim about the index, the worktree and the
   ignore rules together: state precisely which git plumbing answers it and
   whether the code asks that question or a nearby one. Test whether the hook
   plane (staged) and the CI plane (checked out) get the same list.
2. **Correctness & quality.** Read `filewalk.py` and its tests whole. Diff
   `ef43deb`. Run the test file and the full Python suite once. Drive every tree
   shape in *Scope* and record the per-shape result in a table. Check subprocess
   handling: argument construction, NUL-separated output, error and timeout
   paths, exit codes.
3. **Completeness / harvest.** Every caller of the walk (`grep -rn filewalk
   tools/`), the scanners that still carry their own walk, `tools/README.md`,
   and any doctrine sentence that says what the guards read
   (`docs/method/GUARDS.md` and its neighbours). Does each agree with the walk
   at HEAD?
4. **Security & privacy** — mandatory. The walk now shells out to git on a tree
   it does not trust. Check for argument injection through file or directory
   names, for config or attribute driven command execution (`core.fsmonitor`,
   filters, hooks, `safe.directory`), for symlink escape, and for any way a
   committed file can make the guards skip a file. The house scanner is
   discharged by grounds (landed delta; the pending diff is other passes' drafts
   and this brief) — say so, and deliver the code-altitude read by hand, against
   the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_filewalk` or the file's own runner; every
  scanner's `--selftest`; the full Python suite once, foreground
- the tree-shape matrix in *Scope*, parent (`ef43deb^`) against HEAD, in a
  scratch clone
- the floor on both planes at HEAD

## House rules for this run

- You work in the shared review worktree
  `/Users/mike/worktrees/atelier-review-1004` (branch `review-1004`), read-only
  except for THIS brief file. Other sessions are live on this machine and in the
  primary checkout — touch nothing there. Other reviewers are working there at
  the same time on their own briefs; never open another
  `docs/reviews/2026-10-04-2215-*` file — it is another pass's framing.
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
`docs/roadmap/160-doctrine-review-owed/600-rule-4-cold-pass-queued-git-enumerated-walk.md`
(it carries the author's own lens hints), and:

- `docs/reviews/2026-09-25-0715-single-sourced-file-walk-cold.md` and
  `docs/reviews/2026-09-25-0715-linked-worktree-skip-cold.md`
- every item under `docs/roadmap/110-estate-duplication-exception-audit-mike/`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-1004 --also-exclude
docs/roadmap/160-doctrine-review-owed/600-rule-4-cold-pass-queued-git-enumerated-walk.md
--also-exclude docs/roadmap/110-estate-duplication-exception-audit-mike
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `GW`: `GW1`, `GW2`, …) and severities (MAJOR / MODERATE
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

## Verdict — phase 1 (written 2026-10-04 UTC, before any deferred reading)

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE · 6 minor · 3 notes.**

The enumeration is sound on the question the brief put first: no tree shape I
could build makes the walk at HEAD drop a file that git could commit and that
the parent walk read, and a `.gitignore` line cannot blind a guard to a
force-added file. What it carries forward, and now pins with a test, is the
skip-name set applied to tracked files (GW1).

### Provenance

- **How I was spawned:** a subagent started by the batch orchestrator with this
  brief as its only framing, told to do phase 1 and stop. I am not the author's
  session and was not instructed by it.
- **Tier:** `claude-fable-5-1` (Fable).
- **What I read:** this brief; `tools/filewalk.py` and `tools/test_filewalk.py`
  whole; the full message and diff of `ef43deb` (the message carries the
  author's own reasons, which is part of the delta); the walk call sites in the
  eleven scanners; the registry and scope rendering in `tools/floor.py`;
  `.githooks/pre-commit`; both workflow files; `tools/README.md` and
  `CHANGELOG.md` by grep; the docstrings of `conflictscan`, `pathscan` and
  `linkscan` near their walk text.
- **Not opened:** the queue pointer, anything under the barred `110` roadmap
  section, `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any
  prior verdict, any other brief of this batch, the deferred sibling.
- ⚠️ **Exposure, disclosed.** `coldsweep` runs (default bar plus the two
  `--also-exclude` paths plus `docs/reviews`) printed single matching lines
  from non-barred board files: the index title of the `110` item in
  `docs/ROADMAP.md`; lines of the `020/160` and `020/370` items, one of which
  records that "skip all gitignored paths" was once left open; and one line of
  the `160/420` pointer that names a finding `FW3` (MODERATE, "no test imports
  filewalk") from an earlier pass on this module. I read those lines as grep
  output and opened none of the files. The harness also loaded the repo onramp
  and a cross-session memory index into my context; the index carries one-line
  notes on guard design (streamed guards, narrowest exceptions). None of it
  named this delta's findings.
- **Where I worked:** read-only in the review worktree; every probe in
  `<scratchpad>/GW/` — a clone at `f1a667b` (`GW/probe`), throwaway trees under
  `GW/shapes/`, and the parent module extracted with
  `git show ef43deb^:tools/filewalk.py`. No scanner was pointed outside those.
  The delta paths are unchanged between `ef43deb` and HEAD (`git log
  ef43deb..HEAD -- <paths>` is empty).

### Lens 1 — approach and assumptions

Load-bearing assumptions, named before testing:

1. `git ls-files --cached --others --exclude-standard` is the set "what git
   could commit". **Holds, with one precision:** it is the index plus the
   untracked-unignored worktree. That is a superset of what the next commit
   holds, and the walk then reads the *worktree* copy, so it answers "which
   paths", never "which content" (GW10).
2. A tracked file is listed whatever the ignore rules say. **Holds** — shape 01:
   a file force-added under an ignored directory and one matching an ignored
   glob are both yielded.
3. The answer depends on the directory walked, not the caller's environment.
   **Holds for the four scrubbed variables** (shapes 14, 14b), untested (GW3).
4. Where git cannot answer, the fallback is wider, never narrower. **Holds** in
   every shape driven; but only one of the three fallbacks says it ran (GW2).
5. The per-guard skip names still mean what they meant. **They do — and that is
   the problem** (GW1): the names were a way to avoid walking litter; applied to
   git's list they can now only ever remove committable files.
6. The tree being walked is trusted to configure git. **Unstated, and new** —
   the parent walk executed nothing from the tree (GW5).

**Hook plane against CI plane.** Same module, different trees. Probe: a tree
with a staged file, a staged-then-deleted file, an unstaged untracked file and a
force-added ignored file, walked before the commit and again in a fresh clone of
that commit. The lists differ by exactly two entries, both as expected: the
untracked unstaged file is read at the hook only; the staged-then-deleted file
is committed but unread at the hook (GW10). `secretscan`, `leakscan` and
`conflictscan` do not use the walk at the hook at all (`--staged`), so the walk
is their CI plane only; eight other guards use it on both planes.

### Lens 2 — correctness and quality

`test_filewalk`: 15 tests, OK. Full suite: 1669 tests, OK. Every selftest: exit
0. Floor: exit 0 on both planes.

**Tree-shape matrix** — parent (`ef43deb^`) against HEAD, same skip set.
"same" means the two lists were identical.

| # | Shape | Mode at HEAD | HEAD against parent |
|---|-------|--------------|---------------------|
| 01 | untracked-unignored | git | same: yielded |
| 01 | ignored file, ignored dir | git | **dropped** (design) |
| 01 | force-added past an ignore rule | git | same: yielded |
| 02 | staged, intent-to-add | git | same: yielded |
| 02 | deleted from tree, still indexed | git | same: not yielded |
| 03 | assume-unchanged, skip-worktree | git | same |
| 04 | sparse checkout, sparse index | git | same |
| 05 | submodule with `.git` FILE | git | same: content unread |
| 05b | uninitialised submodule | git | same |
| 05c | gitlink with `.git` DIRECTORY | git | same: content read |
| 06 | untracked nested clone | git | same, ignored content too (GW9) |
| 06b | nested `git init`, no commits | git | same |
| 06c | nested clone, parent tracks files | git | same, no duplicate |
| 06d | nested clone the parent ignores | git | **dropped** (design) |
| 06e | nested clone under a skip name / deep | git | same |
| 07 | linked worktree inside the tree | git | same: pruned |
| 07b | root IS a linked worktree | git | parent also yielded `.git` |
| 07c | tracked dir gains a stray `.git` file | git | same: pruned |
| 08 | symlink to file, dir, broken, out-file | git | same |
| 08b | tracked dir replaced by out-of-root link | git | **HEAD reads through it** (GW4) |
| 09 | space, newline, dash, tab, quote, glob | git | same |
| 09c | `core.quotePath=true` via env | git | same |
| 09d | non-UTF-8 name, index only | git | same, no crash |
| 10 | no `.git`, outside any repository | os.walk | same |
| 11 | root is a bare repository | os.walk | same |
| 11b | corrupt `HEAD` | os.walk | same, silent (GW2) |
| 11c | corrupt index | git | **raises**, scanner exits 1 |
| 11d | root `.git` file points nowhere | os.walk | same |
| 11e | index file missing | git | same |
| 12 | root = tracked subdirectory | git | same |
| 12b/c | root ignored, or under an ignored dir | os.walk | same |
| 12e/f | untracked subdir root; symlinked root | git | same / ignored dropped |
| 13 | `git` absent from `PATH` | os.walk | same, warns on stderr |
| 14 | `GIT_DIR` + `GIT_WORK_TREE` elsewhere | git | scrubbed; ignored dropped |
| 14b | `GIT_INDEX_FILE` elsewhere | git | scrubbed |
| 14c | `GIT_CEILING_DIRECTORIES` | git / os.walk | wider fallback |
| 14d | env-config `core.excludesFile` | git | hides untracked only |
| 14f | dubious ownership (simulated) | os.walk | same, silent (GW2) |
| 15 | hostile `.gitattributes` + filter | git | same; filter not run |
| 15b | `core.fsmonitor` in the tree's config | git | same; **command ran** (GW5) |
| 16 | committed dir shaped like a git dir | os.walk | same; nothing ran |
| 17 | unmerged path, three stages | git | same, one yield |
| 18 | unreadable untracked directory | git | same |
| 19 | TRACKED files under skip names | git | same: **not yielded** (GW1) |

Not drivable here: a non-UTF-8 name **on disk** (this filesystem refuses the
bytes); 09d covers the decode path only. Dubious ownership was simulated with
git's own test variable, not a real second owner.

**Subprocess handling.** Arguments are a fixed list with no shell; no file or
directory name is ever passed to git, only `base` as the value of `-C`. Output
is NUL-separated and read in 64 KiB chunks; stderr goes to a temporary file, so
no pipe can fill. A non-zero exit after a complete read raises, and a real
scanner turns that into exit 1 with the git message, `--warn` wiring included
(11c). An early stop by the consumer kills the child and does not raise. There
is no timeout on any of the three git calls (GW8).

### Lens 3 — completeness and harvest

- **Callers:** eleven scanners, each a one-line wrapper passing its own skip
  set; ten pass through `[base] if base.is_file() else _walk_files(base)`, so a
  named file is never filtered by ignore rules. Parameters mean what they meant.
- **Scope roots:** `floor.py` renders a child's declared scope paths as
  absolute subdirectories, so the walk does run with a subdirectory root in the
  fleet; shapes 12–12f cover it.
- **Own walks that remain:** `linkscan`'s suggestion index (GW7); `reviewscan`
  and `pointerscan` `rglob` their bases; `coldsweep` `rglob`s by design.
- **Docs:** stale in three places, silent in one (GW6). `docs/method/GUARDS.md`
  makes no claim about which files guards read, so nothing there disagrees.

### Lens 4 — security and privacy

`/security-review` is **discharged by grounds**: this is a landed delta, and the
session's pending diff in the shared worktree is other passes' drafts and this
brief. Code-altitude read by hand, against the OWASP catalogue:

- **Injection (A03):** clean. No shell, fixed argv, names never reach git;
  leading-dash, newline, quote and glob names all round-trip (09). A root path
  with a leading dash is the value of `-C`, by reading — not probed.
- **Security misconfiguration / untrusted config (A05):** GW5. Filters and
  textconv did not run (15). A committed directory shaped like a git directory
  did not get its config honoured, as a root or as the parent of a root (16,
  and two further variants).
- **Broken access control / path traversal (A01):** GW4.
- **Logging and monitoring failures (A09):** GW2.
- **Insecure design (A04):** GW1 — the one way a *committed* file makes the
  secret and leak guards skip it on the walk plane. A committed `.gitignore`
  cannot (01); a committed `.gitattributes` cannot (15); a `.git` file cannot be
  committed at all, so 07c is a worktree-only state.
- **Privacy:** the walk reads less than it did. Nothing new is written, logged
  or sent.

### Findings

**GW1 — MODERATE. Tracked files under a skip-named directory are invisible to
the walk, so the CI plane of the secret, leak and conflict guards never reads
them.** Probe (`GW/skipprobe.py`): a synthetic credential committed at
`.vscode/settings.json`, `venv/…`, `a/.idea/…` and `node_modules/…`. In each,
`secretscan --staged` exits 1 and the whole-tree `secretscan --root` exits 0; a
control at a plain path exits 1 on both. The parent walk behaves the same, so
the delta did not open this. What the delta did: it removed the reason the skip
set existed (not paying to walk litter — git no longer lists litter), stated
the new contract as "everything that could be committed", kept the skip set on
git's list, and pinned it with `test_skip_dir_names_hold_in_git_mode`, whose
fixture is force-added files. After this change the skip names can remove
nothing *except* committable files. CI is the backstop for commits that never
met the hook; for those, a secret in a committed editor-settings file passes.
Only `secretscan` was probed; `leakscan` and `conflictscan` share the path.
*Counsel:* in git mode apply the skip names to untracked entries and nested
walks only, or drop them for the three boundary guards; decide per guard.

**GW2 — minor. Two of the three fallbacks are silent, and one is mislabelled.**
`LAST_MODE` is read by no caller (`grep` across `tools/`, `instruments/`, the
hook and the workflows: only the module and its test). A corrupt `HEAD` (11b)
and a tree git refuses on ownership grounds (14f) both report
`not-in-git-tree` and walk the whole disk with no output. Probe: the same tree
scanned by `secretscan` exits 0 under its owner and 1 under simulated dubious
ownership, because the ignored file is read again — and nothing in the output
says why. The fallback is the wide one, so no protection is lost; the cost is
the original slow walk returning unannounced on container runners, and a result
that changes with the machine. *Counsel:* distinguish "git says no repository"
from "git failed", and print the mode once for any fallback.

**GW3 — minor. Three behaviours the module relies on have no test.** Mutation
probes in the scratch clone (`GW/mutate.py`, twelve mutants, nine killed).
Survivors: the environment scrub replaced by a plain copy; the unmerged-stage
dedupe removed; the `.git`-FILE check removed from the per-directory test. The
scrub is the code's own stated reason for existing on the hook plane. Also
unpinned: no test asserts that a file force-added past an ignore rule is
yielded — the property the whole design rests on; a mutant cannot express it,
shape 01 shows it holds.

**GW4 — minor. In git mode the walk follows a symlinked directory out of the
root.** Shape 08b: the index holds `d/f.txt`, the worktree has `d` replaced by a
link to a directory outside the root. The parent yields nothing; HEAD yields
`d/f.txt` and a guard would read the outside file and may print its matching
lines. Reachable only from a dirty worktree (git cannot commit both), so hook
plane and hand runs only. The commit message's "symlink behaviour is unchanged"
is true for the leaf and false for a parent component. *Counsel:* check that no
component of a yielded path is a symlink, or compare resolved paths to the root.

**GW5 — minor. Scanning a tree now executes a command its `.git/config` names.**
Shape 15b: with `core.fsmonitor` set to a script in the walked tree's own
config, one `walk_files` call ran the script. The parent executed nothing from
the tree. For a repository the operator owns this equals the trust already
given to its hooks, and a child's floor config may already name a local check,
so the fleet's boundary does not move. It does move for anyone pointing a guard
at a tree they did not create, which a public tool invites. Verified
counter-measure: `git -c core.fsmonitor=false ls-files …` did not run it.

**GW6 — minor. Three statements about the walk are now false, and the change is
recorded nowhere a reader would look.** `tools/README.md` (the bounded-memory
section) still says the directory walk is `os.walk` pruned in place and never
mentions `filewalk` or git. `tools/conflictscan.py`'s scope docstring says no
scanner consults `git ls-files` and that reading an untracked file is "a strict
superset … never a hole" — both untrue at HEAD. `CHANGELOG.md` has no entry
for a change that alters what every guard in every child reads; its newest
entry is dated 2026-09-20. The per-scanner ignore files still carry globs for
nested worktrees that git mode already drops — harmless, worth a line.

**GW7 — minor. `linkscan` still walks ignored trees, so the commit's headline
is not true of every guard.** Probe: a repository with an ignored directory and
one broken link; `os.walk` instrumented. `linkscan`'s index builder
(`linkscan.py`, the `os.walk(root)` that prunes dot-directories only) visited
the ignored tree. `reviewscan` and `pointerscan` use `rglob` over their bases
(by reading, not probed). The cost the delta set out to remove survives here
whenever a link is broken.

**GW8 — note. No git call has a timeout.** Probe: a stand-in `git` that sleeps
blocked `walk_files` for the full sleep of each call. `floor.py` sets no
timeout either (`grep timeout`: none). A hung git hangs the guard.

**GW9 — note. An untracked nested clone is walked whole, its own ignored files
included** (shape 06). Documented and deliberate; it means a large ignored tree
one level down inside a nested clone is still read, and that content cannot be
committed to the parent as files in any case.

**GW10 — note. The walk answers "which paths", not "which content".** At the
hook a staged-then-deleted file is committed unread, and a file whose worktree
copy differs from its staged copy is read in the wrong version. Inherited; the
three boundary guards avoid it with `--staged`; eight guards do not.

### Re-run ledger

All in the scratch clone at `f1a667b` unless stated; all foreground.

| Command | Result |
|---------|--------|
| `python3 -m unittest test_filewalk` (in `tools/`) | 15 tests, OK |
| `python3 -m unittest discover -s tools -p 'test_*.py'` | 1669 tests, OK, 418 s |
| `floor.py`, `floorfleet.py`, `signscan.py` `--selftest` | exit 0 each |
| `--selftest` for the 15 names from `floor.py --list --plane ci` | exit 0 each |
| `floor.py --plane ci --root .` | exit 0; secretscan 22 advisory |
| `floor.py --plane hook --root <clone> --tools <clone>/tools` | exit 0 |
| `GW/matrix.py` — 51 walks, parent against HEAD, plus plane parity | table above |
| `GW/skipprobe.py` — skip names, corrupt index, ownership | GW1, GW2 |
| `GW/mutate.py` — 12 mutants against `test_filewalk` | 9 killed, 3 survive |
| embedded git-directory variants ×3 | no config honoured |
| `linkscan` with `os.walk` instrumented | ignored tree visited |
| stand-in slow `git` on `PATH` | walk blocked 12.7 s |

Both floor runs print two advisory `pathscan` findings in files outside this
delta; they are warn-only and not mine to judge here. The hook-plane run had
nothing staged, so its three `--staged` guards passed on an empty diff.

### Follow-up checklist

- [ ] GW1 — decide, per guard, whether skip names apply to tracked files.
- [ ] GW2 — voice every fallback; separate "no repository" from "git failed".
- [ ] GW3 — tests for the env scrub, the stage dedupe, the `.git`-file check,
      and force-added-past-ignore.
- [ ] GW4 — refuse a yielded path with a symlinked parent component.
- [ ] GW5 — neutralise tree-configured commands on the git calls, or state the
      trust assumption.
- [ ] GW6 — correct the README section and the `conflictscan` docstring; add
      the changelog entry.
- [ ] GW7 — sweep the remaining own-walks (`linkscan`, `reviewscan`,
      `pointerscan`).
- [ ] GW8, GW9, GW10 — record or rule; no action assumed.
