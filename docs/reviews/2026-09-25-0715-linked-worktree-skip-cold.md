# Cold pass — the linked-worktree skip across eleven scanners

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/410-rule-4-cold-pass-queued-the-linked-worktree-skip.md`.
**Why it earns a review:** one pruning line was hand-copied into eleven guards'
file walks; it makes a real surface (a linked worktree's files) invisible to
every scanner, and it prunes on a heuristic (a file named `.git`) whose
false-positive cost was accepted by a worker.

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

- `db9a785` / `eeb94e9` (2026-09-20) — the landing commits

Delta paths:

- the `_walk_files` pruning line in `tools/secretscan.py`, `leakscan.py`,
  `conflictscan.py`, `linkscan.py`, `sizescan.py`, `datescan.py`, `wrapscan.py`,
  `spellscan.py`, `pathscan.py`, `licenscan.py`, `stampscan.py`
- the `LinkedWorktreeSkipped` class in each of their eleven `test_*.py` siblings

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the eleven lines are identical (diff them). Whether pruning on file-ness
is the right test and what it costs: construct a directory holding an ordinary
file named `.git` (a submodule checkout is the real-world case — is it one?), a
linked worktree, a nested clone, and a `.git` symlink, and record what each
scanner does with each. Whether anything *should* be scanned inside a linked
worktree: a worktree with a planted secret, committed on its branch — which
plane catches it now, and which does not. Whether the two exemption claims hold
on every one of the eleven, by probe: that a file argument never reaches
`_walk_files`, and that `--staged` routes through the git-diff path.
**Non-goal:** the E9 finding's commission. ⚠️ **Probe in your own scratch clone
only** — this batch's shared worktree is itself a linked worktree of the primary
checkout; never create or remove worktrees in it.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   skip presumes a linked worktree's contents are covered by scanning its own
   branch — test that against how the floor actually runs (the hook runs in the
   worktree where the commit happens; CI runs on the pushed branch). Ask whether
   the cost was a worker's to accept, as counsel.
2. **Correctness & quality.** Read each of the eleven walks. Run each tool's
   `--selftest` and each `LinkedWorktreeSkipped` class. Drive every case in
   *Scope* against at least `secretscan` and `leakscan`, and the two exemption
   claims against all eleven by probe, not by reading.
3. **Completeness / harvest.** Which scanners in the registry did *not* get the
   line, and do they walk files (`harvestscan`, `reviewscan`, `publishscan`,
   `pointerscan`, `board`, `blockscan`, `signscan`)? Is the skip documented in
   `tools/README.md` and `CONTRIBUTING.md`?
4. **Security & privacy** — mandatory. The skip makes files invisible to a
   secret scanner. State the exact condition under which a committed secret in a
   linked worktree reaches `origin` with every plane green, or show there is
   none. The house scanner is discharged by grounds (landed delta; pending =
   other passes' drafts) — say so, and deliver the code-altitude read by hand.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- a `diff` of the eleven pruning lines and their surrounding walks
- every listed tool's `--selftest`; the eleven `LinkedWorktreeSkipped` classes;
  the full Python suite once
- the *Scope* cases in a scratch clone with a scratch linked worktree; the floor
  on both planes at HEAD

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
`docs/roadmap/160-doctrine-review-owed/410-rule-4-cold-pass-queued-the-linked-worktree-skip.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md` (⚠️ head and tail
  read by the brief-writer; the `020/160` section not opened)
- the board items `docs/roadmap/020-*/160-*.md`, `docs/roadmap/115-*/080-*.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/410-rule-4-cold-pass-queued-the-linked-worktree-skip.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `LW`: `LW1`, `LW2`, …) and severities (MAJOR / MODERATE
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

## Verdict — LW cold pass (phase 1, written 2026-09-26 UTC)

### Provenance, repeated

- **Reviewer:** a fresh Fable subagent (`claude-fable-5-1`), spawned by the batch orchestrator
  (`review-batch-0925`) with this brief as its only framing. I was neither started nor
  instructed by the author of `db9a785`/`eeb94e9`, and I have edited none of the delta's paths.
  Tier checked at claim: Fable, the principal-named review tier.
- **Shape:** reviewer-plus-orchestrator, as the brief discloses. The orchestrator holds the
  `.deferred.md` sibling outside the tree; I have not seen it. The orchestrator formed no finding
  and wrote no severity — everything below is mine.
- **Where I worked:** the shared review worktree `/Users/mike/worktrees/atelier-review-batch-0925`
  at `f81a98f`, read-only; every mutation probe ran in my own clone of it
  (`<scratchpad>/LW/probe`, HEAD `f81a98f`) and in a throwaway scenario repo beside it. No git
  command that writes was run in the worktree. No worktree was created, removed or listed for
  mutation anywhere but inside the scratch scenario.
- **What I read:** this brief; `docs/method/REVIEW.md` and `docs/method/00-APEX.md` at HEAD; the
  two landing commits' subjects, bodies and `--stat`; the diffs of `db9a785` for the eleven
  scanners and three of their test files; the eleven scanners' walk wrappers and `--help`;
  `tools/filewalk.py` in full; `tools/floor.py` lines 1–1135 (registry and planes);
  `.githooks/pre-commit`; `.github/workflows/ci.yml`; `.atelier-floor.json`; `.gitignore`
  lines 14–21; `tools/README.md` lines 6–45 and greps of it; `CHANGELOG.md` lines 6–51;
  `tools/reviewscan.py` 270–350, `tools/pointerscan.py` 440–475, `tools/coldsweep.py` 85–125,
  `tools/linkscan.py` 495–600.
- **Rule-2 exposure, disclosed:** none of the barred files was opened. `coldsweep` ran once with
  the default bar plus `--also-exclude` for all three items the brief lists (the queue pointer,
  `020/160`, `115/080`); it excluded 349 files and I never used `--include-barred`. Two
  incidental exposures: (1) `docs/ROADMAP.md` (the generated index, not barred) showed me the
  one-line titles of the `115/080` item (`[~]`, "part 1 of 3 DONE") and of a separate `⏳`
  pointer `160/420` for the single-sourced file walk — titles only, no item text; (2) a
  `pgrep` I ran to see whether my test suite was still alive printed another reviewer's shell
  command line (its scratch prefix and the fact that it was running the full suite in the shared
  worktree) — process metadata, no brief or finding content. I checked that the review worktree
  holds no nested `.claude/worktrees/` before sweeping, so the coldsweep hole in LW2 below did
  not reach me.
- **Process deviation, disclosed:** the full Python suite exceeded the harness's 600 s
  foreground cap on this shared machine (a second reviewer's suite was running concurrently)
  and the harness moved it to the background automatically; I ran it exactly once and read its
  result from the saved output. The two floor-plane runs waited until it had finished.

### The delta at HEAD is not the delta the brief describes

The brief says the pruning line lives in eleven `_walk_files` copies. At `f81a98f` it lives
**once**: commit `c1a2f12` (2026-09-21, "single-source the scanner file walk, 115/080 part 1")
moved the walk into `tools/filewalk.py`, and each scanner's `_walk_files` is now a one-line
wrapper passing its own skip-set. `filewalk.py`'s docstring claims the E9 line was "present,
identically, in all eleven copies already; it is preserved here unchanged" — I verified both
halves (ledger items 1 and 2). So this pass reviews the *skip semantics* as they stand at HEAD,
reached through `filewalk.py`; the single-sourcing decision itself has its own queued pointer
(`160/420`) and is not judged here (LW9).

### Lens 1 — approach and assumptions

Load-bearing assumptions, named by me and tested:

1. **"A linked worktree's contents are covered by scanning its own branch."** Holds, on both
   planes, by live probe. The hook runs where the commit happens: `git rev-parse --show-toplevel`
   inside a nested worktree is the worktree root, `core.hooksPath` and `hooks.atelierTools`
   live in the shared repo config, and a real `git commit` in the scenario worktree with a
   planted secret was **blocked** by the hook (ledger 9). CI runs on the pushed branch: the
   ci-plane floor on a fresh clone of that branch reds and names the worktree's file (ledger 9).
   What the fix removes is only the *primary checkout's* view of a sibling's tree — which is
   the double-count E9 measured, and the intended effect.
2. **"CI never contains a `.git` file."** Holds, and more strongly than the commit argued:
   git will not put a path named `.git` (file or symlink) into the index at all — `git add -f`
   exits 0 and silently drops it; a tree hand-built with `mktree` to carry one fails
   `git fsck --strict` (`hasDotgit`), is rejected by a remote with `receive.fsckObjects`
   (GitHub's setting), and a clone of it aborts checkout with "invalid path" (ledger 12). The
   one CI-reachable `.git` file is an *initialised submodule*, and a plain clone checks out no
   submodule content (ledger 7: 0 files) — `actions/checkout` defaults to `submodules: false`.
3. **"A bare file named `.git` is never anything else."** Nearly: it is also a **submodule
   checkout** (the commit says so in a comment, but names only worktrees in the tested and
   "confirmed unaffected" lists) and, because `Path.is_file()` follows symlinks, a **`.git`
   symlink that points at any file** (ledger 8). Neither reaches CI or the staged hook plane; both
   change what a local whole-tree run sees (LW5).
4. **"Both planes are unaffected."** False as stated, and false in the direction that favours
   the fix: the hook plane runs eight registry scanners whole-tree, and with a nested worktree
   present the *pre-fix* hook from the primary root reds `linkscan` on the sibling worktree's
   broken link while HEAD does not (ledger 10). The hook plane *is* affected — that is the
   `faves` incident being closed — and the record says the opposite (LW7).

**Was the cost a worker's to accept, as counsel?** For the stated cost — an ordinary file
literally named `.git` prunes its parent — yes: it is reversible, tested, near-zero in
incidence, and git itself refuses to track such a path, so no committed tree can ever exhibit
it. For the *unstated* costs — submodule content and `.git`-symlink-to-file directories
becoming invisible to local whole-tree runs — the worker widened the boundary scanners' blind
spot on a real-world shape without naming it as a decision, a test, or a README residual. That
is the class `floor.py` makes children declare with a reason; the parent's tooling should hold
itself to the same bar (LW5, LW6).

### Lens 2 — correctness and quality

- **Are the eleven lines identical?** The code line is byte-identical in all eleven
  (`and not Path(dirpath, d, ".git").is_file()`); the surrounding comments differ only in which
  `faves` figure they cite; `sizescan` names its skip-set `NON_CONTENT_DIR_NAMES` (pre-existing).
  At HEAD all eleven route through the one line in `filewalk.py` (ledger 1, 2).
- **Selftests and test classes:** all eleven `--selftest` exit 0; the eleven
  `LinkedWorktreeSkipped` classes pass (33 tests) at HEAD; run against the pre-fix modules,
  22 fail and 11 pass — the eleven "nested repo's own `.git` dir" tests pin unchanged behaviour
  and were never going to fail, so the commit's "each proved to fail against the pre-fix module"
  is an overclaim for a third of them (ledger 4, 5; LW7).
- **The Scope cases, driven against every one of the eleven** (ledger 8, walk matrix): HEAD
  prunes the linked worktree, the submodule, the ordinary `.git` file and the `.git`
  symlink-to-file; it walks the nested independent clone (its own `.git` dir pruned inside),
  the `.git` symlink-to-directory case and the broken `.git` symlink case. Pre-fix walked all
  eight. `secretscan` and `leakscan` CLI runs agree with the matrix (ledger 7).
- **Exemption claim 1 — a file argument never reaches `_walk_files`:** holds for ten of eleven
  by monkeypatch (the walk patched to raise; a worktree-internal file passed positionally is
  scanned and the walk is never entered) and by CLI (four scanners report the planted finding).
  For `licenscan` the claim is **vacuous**: it takes a root, not files, and its walk is always
  entered with that root (ledger 8).
- **Exemption claim 2 — `--staged` routes through git-diff:** holds for the three scanners that
  have the flag (finding reported from inside the worktree with the walk never entered). The
  other eight have no `--staged` at all (argparse exit 2), so for them the claim is vacuous and
  the hook plane runs them whole-tree — see lens 1, assumption 4.
- **Quality of the line itself:** one extra `stat` per subdirectory; `is_file()` swallows the
  OSErrors that matter; the check is on *children* of the walk base, so a scan rooted at a
  worktree still scans it — which is what makes the in-worktree hook correct.

### Lens 3 — completeness and harvest

Registry and tool walkers that did **not** get the line, checked by reading and by probe:

| tool | walks files? | reaches a nested worktree? | probe result |
|---|---|---|---|
| `reviewscan` | yes — `base.rglob("docs/reviews")`, `base.rglob("docs/decisions")` | **yes** | reds the primary's hook on a sibling worktree's draft brief (LW1) |
| `pointerscan` | yes — `p.rglob("*.md")` with a name-only `SKIP_DIRS` | yes on a root scope | names a worktree item in a `--root . .` run (LW3) |
| `coldsweep` | yes — `root.rglob("*")` with a name-only `NOISE` | **yes** | shows the worktree's copy of a barred `docs/reviews` file (LW2) |
| `linkscan` (basename index / `rglob` fallback) | yes, dot-dirs pruned | only if the worktree is at a non-dot path | suggestion text only (LW4) |
| `board` | `sec.glob("*.md")`, non-recursive under `docs/roadmap` | no | — |
| `harvestscan`, `publishscan`, `signscan` | git-based (diff / tracked set / log) | no | — |
| `blockscan` | reads named map paths | no | — |
| `floor.py` | runs scanners, walks nothing | no | — |

**Documentation:** neither `tools/README.md` § *What these scans cannot see* (the stated home
for what an instrument drops, EVIDENCE §14) nor `CHANGELOG.md`'s 2026-09-20 section mentions
the skip; there is no `CONTRIBUTING.md` in the tree (LW6). `filewalk.py` has no test of its
own — `tools/test_filewalk.py` does not exist — so the single line is pinned only through the
eleven wrappers (LW8).

### Lens 4 — security and privacy

`/security-review` is **discharged by grounds**: it reads the session's pending diff, which in
this shared worktree is other passes' unstaged drafts, and this is a landed-delta review. The
code-altitude read was done by hand against the OWASP catalogue: the surface is a filesystem
walk, so the live classes are improper link resolution / symlink following (CWE-59, CWE-61),
path handling and TOCTOU; injection, XSS and auth do not apply.

**The exact condition under which a committed secret in a linked worktree reaches `origin`
with every plane green: there is none that is worktree-specific.** The chain, each link
re-driven (ledger 9): a commit inside the worktree meets the shared hook and is blocked;
`--no-verify` lands it locally; the push meets CI on that branch, which reds and names the
file. CI is a backstop, so the secret is at `origin` when CI reds — but that is identical to
the primary checkout, not a hole the skip opened. What the skip did change: a whole-tree run
from the primary (hand run, or `floor.py --plane ci --root .` locally) no longer sees a
sibling worktree's files. That is the intended effect, and it covers uncommitted content
only — anything committed meets the hook in its own tree.

**Can the skip be weaponised to hide a directory from CI?** No (ledger 12): git refuses to
index a `.git` path, `fsck` reds a hand-built one (`hasDotgit`), a `receive.fsckObjects`
remote rejects the push, and a clone refuses to check it out. The symlink-following `is_file()`
is therefore a local-only concern (LW5). Privacy at design altitude: the one genuine exposure
this delta leaves is not in the eleven — it is `coldsweep`, whose bar can be bypassed by a
nested worktree's copy of a barred file (LW2).

### Findings

**LW1 — MODERATE.** `reviewscan` still descends into a nested linked worktree, on the hook
plane, whole-tree, and **blocks**. Probe: with a sibling worktree at `.claude/worktrees/wt`
holding an uncommitted draft brief with an inline deferred section, `floor.py --plane hook`
from the primary root exits 1 on that file (ledger 10, 11). The primary session's commit is
blocked by a defect in another session's uncommitted draft — the exact E9 class, on a scanner
the commit subject ("every scanner's file walk") implies was covered. `docs/decisions` has the
same shape. Counsel: give `find_briefs`/`find_records` the same file-ness prune (or route their
tree case through `filewalk.walk_files` and filter), with a test mirroring
`LinkedWorktreeSkipped`.

**LW2 — MODERATE.** `coldsweep` — the tool rule 2 made the *default* because hand exclusions
failed three times — surfaces barred content through a nested worktree's copy. Probe: a file
under `docs/reviews/` is excluded, but its copy at `.claude/worktrees/wt/docs/reviews/…` is
printed as an ordinary hit (ledger 11). The bar is computed on the relative path, so any nested
checkout defeats it. Live shape: the repo's own `.gitignore` says harness worktrees land at
`.claude/worktrees/`. No nested worktree existed under the primary or the review worktree at
the time of this pass, so no reviewer in this batch was exposed. Counsel: prune `.git`-file
directories in `coldsweep.walk` and, belt and braces, apply the bar to the path *after* any
`.claude/worktrees/<x>/` prefix; add a selftest case.

**LW3 — minor.** `pointerscan.roadmaps` walks `rglob("*.md")` with a name-only skip set, so a
root-scoped run names a sibling worktree's roadmap items (ledger 11). Warn-only, and the
registry scopes it to `docs`, so the floor never reaches it; a `--root . .` hand run does.

**LW4 — note.** `linkscan._build_basename_index` and the `rglob` fallback in `_suggest` prune
dot-directories only; a nested worktree at a non-dot path would feed *suggestions* from the
copy. Advisory text only; verdicts and exit codes unaffected.

**LW5 — minor.** The skip also prunes a **submodule checkout** and any directory whose `.git`
is a **symlink to a file** (ledger 8). Neither is tested, neither appears in the commit's
"confirmed unaffected" list, and the README residual is silent. Effect is local-only (lens 4):
CI checks out no submodule content and git cannot commit either marker. Counsel: pin both
shapes as deliberate in the test class, and name them in the README residual; if submodule
content *should* be scanned locally, the check needs `gitdir:` parsing after all.

**LW6 — minor.** The skip is undocumented on the two live surfaces that exist for it:
`tools/README.md` § *What these scans cannot see* and `CHANGELOG.md` (the 2026-09-20 section
covers `020/370`/`020/380` and not `020/160`). A reader trusting a clean local run has no line
telling them nested checkouts are invisible.

**LW7 — minor.** Three overclaims in the landing record (`eeb94e9`, and `db9a785`'s body):
"33 new tests … each proved to fail against the pre-fix module" — 11 of 33 pass against it by
design (ledger 5); "both planes verified unaffected" — the hook plane is affected for the
eight whole-tree scanners, beneficially (ledger 10); "every scanner's file walk" — two registry
walkers and one review tool were not touched (lens 3). None changes the code's correctness;
each is a claim stronger than its evidence, which the apex names as the one unrecoverable
defect class.

**LW8 — note.** `tools/filewalk.py` now carries the line once and has no test file of its own;
the behaviour is pinned only through the eleven wrappers' `LinkedWorktreeSkipped` classes. A
future caller of `walk_files` that is not one of the eleven inherits no test. Belongs with the
`160/420` pass; recorded here so it is not lost between the two.

**LW9 — note (brief framing).** The brief's *Delta paths* describe eleven copies; at HEAD the
line exists once in `filewalk.py`. The review still lands — the semantics are unchanged and
verified — but the next reader should know the surface moved between landing and review, and
that this pass and `160/420` overlap on that one line.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 4 minor · 3 note.** The eleven lines do what
they claim, identically, on every shape probed, and the two planes that gate publication are
unaffected by construction; the findings are two walkers the sweep missed (one of which is a
rule-2 mechanism), an untested widening of the blind spot, and record honesty.

### Re-run ledger

All commands ran on 2026-09-26 (UTC) in the review worktree (read-only) or the LW scratch
clone/scenario. `<W>` = the worktree, `<P>` = scratch clone at `f81a98f`, `<PRE>` = `tools/`
extracted from `db9a785~1` via `git archive`, `<S>` = the scenario repo.

1. `git diff db9a785~1 db9a785 -- tools/{eleven}.py` — one identical code line in each; comments
   differ in cited figures only.
2. `git log db9a785..HEAD -- tools/*scan.py tools/filewalk.py` → `c1a2f12` only; each
   `_walk_files` at HEAD is `return filewalk.walk_files(base, SKIP_DIR_NAMES)`;
   `filewalk.walk_files` carries the same line. `ls tools/test_filewalk.py` → absent.
3. `python3 tools/<s>.py --selftest` × 11 → all exit 0.
4. `cd tools && python3 -m unittest test_<s>.LinkedWorktreeSkipped` × 11 → Ran 33, OK.
5. Same 33 classes copied beside `<PRE>` modules → FAILED (failures=22): the two
   worktree/dotfile tests fail in all eleven, the nested-repo test passes in all eleven.
6. `python3 -m unittest discover -s tools -p 'test_*.py'` in `<P>`, once → Ran 1564 tests in
   1141 s, FAILED (failures=2): `test_pins.BoundedMemory.test_peak_memory_does_not_scale_with_
   sibling_count` and `test_spellscan.BoundedMemory.test_peak_memory_does_not_scale_with_many_
   line_file_size`. Neither touches the delta; both are peak-memory measurements, and the run
   shared the machine with a second reviewer's full suite (wall time ~3× nominal). I did not
   re-run (the once rule), so they stand as **unexplained, not dismissed** — a quiet-machine
   re-run is owed before anyone reads them as green.
7. Scenario (`<S>`, built by `LW/probe.sh`): main repo with a committed secret-shaped string, a
   nested linked worktree at `.claude/worktrees/wt` (secret + structural-leak string + draft
   brief with deferred section + roadmap pointer with a question + broken link + conflict
   marker), a nested independent clone, an ordinary file named `.git`, three `.git` symlinks
   (to file / to dir / broken), and a submodule. `secretscan --root . .` at HEAD names
   `main`, `nested`, `symb`, `symd` files; `<PRE>` names those plus worktree, dotfile, symf and
   submodule files. `leakscan` at HEAD names nothing in the worktree; `<PRE>` names the
   worktree's leak file. Plain clone of main: `sm/` has 0 files.
8. `LW/walk_matrix.py`: per-module `_walk_files` matrix, HEAD vs `<PRE>`, eight cases — HEAD
   prunes dotfile/worktree/symf/submod and walks nested/symd/symb/main in all eleven; `<PRE>`
   walks all eight in all eleven. Monkeypatch: walk patched to raise, `main(["--root",S,
   <worktree file>])` → walk never reached in ten; `licenscan` reached with the root (no file
   argument exists). CLI: four scanners exit 1 on a worktree-internal file argument. `--staged`
   inside the worktree: secretscan/leakscan/conflictscan exit 1; the other eight exit 2.
9. Hook plane inside the worktree with the secret staged: `floor.py --plane hook` exit 1; real
   `git commit` with `core.hooksPath` → blocked (1 BLOCK line); `--no-verify` lands.
   `floor.py --plane ci` on a fresh clone of branch `wt` → exit 1 naming the worktree's secret
   file. `floor.py --plane ci --root <S>/main` (HEAD tools) → worktree file not named; `<PRE>`
   `secretscan --root . .` names it.
10. `floor.py --plane hook --root <S>/main` with the nested worktree present: HEAD tools → exit
    1, only `reviewscan` red (the worktree's draft brief); `<PRE>` tools → exit 1, `linkscan`
    additionally red on the worktree's broken link.
11. `reviewscan --root . .` → exit 1 naming the worktree draft; `pointerscan --root . .` →
    exit 0 with 1 grammar finding in the worktree item; `coldsweep --root . VERDICTMARKER` →
    1 hit, the
    `.claude/worktrees/wt/docs/reviews/…` copy, the primary's copy excluded as barred;
    `conflictscan` and `linkscan --root . .` → worktree not named.
12. `git add -f dotfile/.git` / `symf/.git` → exit 0, nothing indexed; `mktree` with a `.git`
    entry → accepted; `git fsck --strict` → `hasDotgit` errors, exit 1; push to a bare remote
    with `receive.fsckObjects=true` → rejected (`hasDotgit`); `git clone -b evil` → "invalid
    path 'hidden/.git'", checkout aborted. git 2.50.1.
13. Floor at HEAD, both planes, in `<P>` (`floor.py --plane ci --root .` and `--plane hook
    --root .`, 2026-09-26T14:43Z): both exit 0. Blocking checks all green; `secretscan` 22
    advisory findings on the ci plane (0 staged on hook); `sizescan` 2 size-advisory;
    `pointerscan` 1 grammar finding and `pathscan` 1 finding, both warn-only and pre-existing
    (not inspected — their files may be barred). No output line named another pass's brief.
14. `coldsweep --root <W> --also-exclude {pointer} --also-exclude {020/160} --also-exclude
    {115/080} -i "linked.worktree|LinkedWorktreeSkipped|gitdir|020/160"` → 109 hits over 508
    files, 349 excluded; no `--include-barred`.

### Follow-up checklist

- [ ] LW1 — prune `.git`-file directories in `reviewscan.find_briefs`/`find_records` (+ test)
- [ ] LW2 — prune in `coldsweep.walk` and bar paths beneath `.claude/worktrees/<x>/` (+ selftest)
- [ ] LW3 — prune in `pointerscan.roadmaps` (+ test)
- [ ] LW4 — decide whether `linkscan`'s index should prune `.git`-file dirs; note if not
- [ ] LW5 — pin submodule and `.git`-symlink-to-file shapes as deliberate; decide on `gitdir:`
- [ ] LW6 — add the residual line to `tools/README.md` and a `020/160` line to `CHANGELOG.md`
- [ ] LW7 — correct the three overclaims where the record is next touched (never rewrite history)
- [ ] LW8 / LW9 — hand to the `160/420` pass: `test_filewalk.py`, and the shared line's ownership
- [ ] Orchestrator: fold the sibling below the reconcile; update the queue pointer
