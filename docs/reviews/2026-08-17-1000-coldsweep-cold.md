# Cold pass — `coldsweep.py`, the cold-sweep exclusion guard

**Pass type:** code cold pass (REVIEW.md rule 4 — a first-of-kind reviewer's
instrument whose default *is* rule 2's bar, and a rule-2 edit that directs
every future cold reviewer to use it; the tool encodes review policy as code,
which rule 3 says does not keep the ordinary-code escape).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04). Checked
at selection: a session that cannot honour the bar stops rather than takes.
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that built the guard on
  2026-08-17 (wt: `rulings-0817`, landing commit `613132e`, merged to `main`
  in PR #27; Opus tier per the commit trailer). The same session applied the
  ruling round in the previous commit and orchestrated the two cold passes in
  which the third instance of the defect this guard answers was recorded.
- **Who wrote this brief:** an atelier session Mike opened 2026-08-17 at 0955
  UTC on the **Fable** tier under his standing cold-session instruction (*do
  any review work, any Fable-dependent work, write briefs for reviews that
  need them; a brief-writer never runs its own brief*). It authored no part of
  this delta, was neither started nor instructed by the authoring session, and
  has edited no file this delta touches. It wrote this brief from the diff of
  the five delta paths at `613132e` and from the queue pointer; it did **not**
  open the board item `290-…/040` that carries the ruling, or the intent
  record.
- ⚠️ **Three disclosures, all about the brief-writer.**
  1. **It read the `docs/SESSIONS.md` tail** at session onramp, before this
     brief was commissioned; the index entries there mention the guard's
     build and the defect count in the author's words. Rule-2 barred material,
     read. It is why the board item was left unopened.
  2. **It read the landing commit's message in full**, and the queue pointer
     carries the author's own lens-1 hint (that the guard eases the safe path
     without failing the unsafe one). Both are the author's framing; generate
     your own reading of the code before you weigh either.
  3. **It is running `coldsweep.py` itself, in another pass, at the time of
     writing** — as the sweep instrument for a concurrent unrelated review it
     is orchestrating. That is use, not authorship, and it made no change to
     the tool; but a brief-writer that has just used the thing under review
     is not neutral about whether it works. Weight accordingly.
- **Who takes the review:** the next cold session meeting rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in the
  verdict: how it was spawned, and its non-involvement with both the authoring
  session and this brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling
  `2026-08-17-1000-coldsweep-cold.deferred.md` (rule 1's split). Recommended:
  run under an orchestrator that holds the sibling's bytes and releases them
  only after the reviewer's findings are durably written. A taker working by
  hand opens the sibling as a deliberate second act after its findings are
  committed, and says so. Fold in and delete when the verdict lands.
- **A circularity to name.** Rule 2 now tells the reviewer to sweep with the
  tool under review. Doing so is fine and expected — but say in the verdict
  that you did, and treat any surprise the tool gives you *during* the pass as
  a finding about the tool, not as a reviewer error to work around.

## What the work is

One commit, `613132e`, five delta paths. Reviewed at HEAD.

**`tools/coldsweep.py` (new, 282 lines).** A tree search for cold reviewers.
It walks the tree with `pathlib.rglob`, skips a noise set (`.git`,
`node_modules`, `__pycache__`, `.venv`) and symlinks, and partitions files
into *searchable* and *barred* by comparing **relative path parts** against a
`BARRED` tuple of four entries — `docs/SESSIONS.md`, `docs/sessions`,
`docs/ROADMAP-DONE.md`, `docs/reviews`. `is_barred()` accepts any spelling of
an entry (`./x`, `x/`, `x//y`) because it splits into parts rather than
comparing text. Search is a Python regex per line over UTF-8-decoded bytes,
binary files (NUL in the first 8 KiB) skipped. Flags: `-i`, `--root`,
`--also-exclude PATH` (repeatable), `--include-barred` (the exception; prints
a disclosure banner), `--list-barred`, `--selftest`. Every run prints a
provenance line naming the exclusion set used. Exit codes follow `grep`: 0
matched, 1 no match, 2 the search failed. Not registered in the floor.

**`tools/test_coldsweep.py` (new, 147 lines).** Twenty tests over three
classes: path barring (every spelling bars, sibling-prefixed dirs and files do
not, nested files under a barred dir do, an empty entry bars nothing), the
sweep itself (default reaches only unbarred files, `--include-barred` reaches
all, `--also-exclude` bars extra, `-i`, binary skip, `.git` never searched)
and exit codes. Plus the in-tool `--selftest`, whose corpus the docstring says
is "the three real instances reduced to shapes".

**`tools/README.md` § `coldsweep.py`** — a catalogue entry (38 lines).
**`docs/method/REVIEW.md` rule 2** — nine added lines directing reviewers to
sweep with the tool and making `--include-barred` the disclosed exception.
**`CHANGELOG.md`** — an *Added* entry.

## Scope

Widest the work admits. The delta's subject is **a bar encoded as a default**,
so the reviewable question is not only whether the code is correct but whether
the bar it encodes is rule 2's bar — the same set, no wider, no narrower — and
whether the tool can mislead a reviewer into believing a sweep was clean when
it was not, or barred when it was not. In scope: whether `BARRED` matches
rule 2's stated set at HEAD and whether the two can drift (one is prose, one
is a tuple, nothing ties them); the geometries `is_barred()` meets that its
tests do not — a `--root` that is a subdirectory of the repo (relative parts
then differ from repo-relative parts), a repo whose records live at a
different path per `.atelier-floor.json` (children *declare* where records
live — does the tool read that, or assume atelier's layout?), symlinked
records directories (silently skipped as symlinks: is that a bar or a hole?),
case-different spellings on a case-insensitive filesystem; whether the noise
set hides material a reviewer would want (a `.claude/` worktree nested in the
tree, `.deferred.md` siblings that a reviewer must not see but the tool does
not know about); whether the exit-code contract survives the provenance line
being printed to stdout on every run (a pipeline consumer sees the banner as
a hit); and whether "not a floor check, deliberately not in the registry" is
the right altitude for a tool whose absence from a reviewer's habit is the
whole failure mode.

**Non-goals, and neither fences the risk:** the ruling to build a guard is
the principal's and is not under review — only the guard built; and no
finding is decided by the reviewer (rule 3 — the tool encodes review policy),
so counsel on altitude is welcome and must be labelled as counsel.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself
   first. The stated principle is *the exclusion becomes the default, not the
   discipline*. Test the premise: was the defect it answers a matching defect
   (prefix text against tool output) or a habit defect (reviewers reaching
   for `grep`)? A tool that fixes the first does nothing about the second
   unless it displaces `grep` in practice — consider what would, and whether
   the rule-2 edit is enough. Consider the opposite altitude too: should the
   bar be *enforced* (a reviewer-session hook, a wrapper the harness prefers)
   or is a soft instrument the right stopping point given the guard doctrine's
   own warnings about a guard layer consuming the programme? Say which, as
   counsel.
2. **Correctness & quality.** Read the whole tool, not the diff. Trace
   `_parts()`, `is_barred()`, `walk()` and `search()` for the geometries above.
   Check that `walk()`'s `sorted(root.rglob("*"))` and the symlink skip do what
   the docstring says on this platform. Check `--also-exclude` with an
   absolute path, a path with `..`, and a path outside the root. Check that
   the selftest's temp corpus actually exercises the "three real instances" —
   or only the shapes the author says they had. Check the tests assert the
   property their names claim. Run the tool with a pattern that matches
   nothing, a bad regex, an unreadable file, and a NUL in the ninth KiB. Say
   whether the provenance line on stdout breaks `coldsweep … | wc -l`.
3. **Completeness / harvest.** Every surface that told a reviewer how to
   sweep before this: `REVIEW.md` (rule 2 and *The lifecycle*), the review
   brief template or skill if one exists under `docs/build/` or `.claude/`,
   `tools/README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, and any brief in
   flight that still instructs a hand-written exclusion. Does anything still
   say `grep --exclude-dir`? Is the tool reachable from a child (children
   call the floor's tools via `hooks.atelierTools` — does the README say how
   a child's reviewer invokes it, and does `--root` make that work)? Is there
   a memory or session-onramp surface that would tell a cold reviewer the
   tool exists before it reaches for `grep`?
4. **Security & privacy** — mandatory. atelier is PUBLIC. The tool prints
   file paths and matched lines; check it can never print an absolute machine
   path in its provenance line or banner (it resolves `--root` — does the
   resolved path reach stdout?). The tool reads every non-barred file in the
   tree: consider `.env`-class files, secrets under `.git/` (skipped) and under
   anything *not* in the noise set. Check whether the barred default could be
   used the other way — `--include-barred` as a one-flag path to the exact
   material rule 2 protects, with only a banner between. The house security
   scanner reads the session's pending diff whatever path it is aimed at; this
   is a landed-delta review, so state the reach case that applied rather than
   assuming one. If the lens has no surface beyond these, discharge it in one
   explicit line with grounds.

## Re-run obligation

Re-run, do not read:

- `python3 tools/coldsweep.py --selftest`; `python3 -m unittest
  tools.test_coldsweep` (or discover); the full Python and node suites; and
  the floor on **both** planes at HEAD. Lift the invocations from
  [`.githooks/pre-commit`](../../.githooks/pre-commit) and
  `.github/workflows/ci.yml` rather than guessing them.
- The count claim: the commit says 289 barred files were excluded on this
  tree. Reproduce with `--list-barred` at HEAD and say what the number is now
  and what it counts.
- The spelling claim: run the tool with `--also-exclude` in each of the four
  spellings the docstring names, plus an absolute path under the root, and
  compare the excluded counts.
- The banner claim: run `--include-barred` with a pattern and say what the
  banner prints, on which stream, and whether it reaches a pipeline consumer.
- The child-geometry claim: run the tool with `--root` pointed at a scratch
  clone whose records live somewhere other than `docs/sessions/`, and at a
  subdirectory of a repo, and say what is barred in each. Mutation probes
  belong in your own scratch clone under the session scratchpad, never in the
  worktree.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/` (the passes in which the three defect
instances were recorded especially), the board item `docs/roadmap/290-…/040`,
and the intent record for this delta. Sweep the tree with the tool under
review; if you use `--include-barred`, disclose it. The sibling `.deferred.md`
holds those references and the brief-writer's seeded questions; open it after
your findings are committed. Reconcile after, never anchor before. A taker
whose own onramp has already read the `SESSIONS.md` tail discloses that in
the verdict, as this brief-writer has.

Reading the *code* is not barred — the tool, its tests, its catalogue entry
and the rule-2 text are the delta. What is barred is the author's narrative of
why, and the verdicts that recorded the instances.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `SW`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/160-doctrine-review-owed/240-rule-4-cold-pass-queued-coldsweep.md`)
and rebuild the index in the same commit. Findings on the rule-2 edit are the
principal's to decide (rule 3); findings on the tool's code may carry the
author's `[rejected: grounds]` escape, but the author is not the taker, so
record them all and apply nothing.

---

## Verdict — 2026-08-17 13:45 UTC, reviewed at HEAD `574f133`

### Provenance and disclosures

**Who I am.** A cold reviewer on the **Fable** tier, spawned as a subagent by
an orchestrator session Mike opened 2026-08-17 at 1321 UTC, itself on the
Fable tier, under his standing cold-session instruction (*do any reviews and
any Fable-dependent work; write any briefs required*). The orchestrator wrote
none of the delta and none of this brief; it forms no finding and writes no
severity — every finding, severity and word below is mine. I was neither
started nor instructed by the authoring session (wt `rulings-0817`, landing
`613132e`) nor by the brief-writing session (wt `cold-run-0817-0955`); I have
edited no file the delta touches and edit only this brief. The deferred
sibling was moved out of the tree by the orchestrator before I started and
reaches me by message only after this text is committed (rule 1's context
partition). Rule 4's reviewer-plus-orchestrator shape applies: both hands are
on the named tier; the arrangement is disclosed in the claim, the queue
pointer and here.

**Circularity, named.** I swept the tree only with `tools/coldsweep.py` — the
tool under review — through a wrapper in the session scratchpad that adds
`--also-exclude` for the intent record on every run. `--list-barred` confirmed
that entry covered exactly one file. Any surprise the tool gave me during the
pass is recorded below as a finding about the tool, not worked around.
Surprises met: the excluded-file count moved between runs (298 → 302, parallel
passes writing into `docs/reviews/` — concurrency, not the tool); the
provenance line on stdout meant every filtered read of tool output had to
tolerate a non-hit line (SW5); the brief's `python3 -m unittest
tools.test_coldsweep` invocation fails on import (SW7).

**What I read that is barred or author-framed.** Not opened: `docs/SESSIONS.md`,
`docs/sessions/`, `docs/ROADMAP-DONE.md`, any file under `docs/reviews/` other
than this brief, the intent record `290-…/040`. Opened, disclosed: the queue
pointer `160/240` (open to me; it carries the author's lens-1 hint — I formed
my lens-1 reading from the code and probes first, then weighed it; my reading
overlaps it and goes further, SW1–SW3); the landing commit's message in full
via `git show --stat 613132e` (author's framing, same disclosure the
brief-writer made); board items `160/250` and `010/110`, surfaced by my own
sweeps, neither barred (`110` names `coldsweep` as unaffected by the
mixed-root defect — it is, for `--root`; the mirror lives in `--also-exclude`,
SW1). Names-only exposure: `git status` showed the three deleted `.deferred.md`
filenames and one untracked sibling brief's filename; `git ls-tree
--name-only` at `613132e` and `HEAD` for the count claim; a metadata-only walk
of the main checkout's tree (paths, never content) for SW3. My single-file
greps (`REVIEW.md`, `floor.py`, `tools/README.md`, two skill files, `ci.yml`,
the hook) were on non-barred files, not tree sweeps. `--include-barred` was
never used. No pending-diff scanner was run in the worktree (lens 4 states
the reach case). Records are written for a public repo: no machine paths
beyond the repo, scratch locations referred to generically.

**Delta as reviewed.** The five paths the pointer names, at HEAD:
`tools/coldsweep.py`, `tools/test_coldsweep.py`, `tools/README.md`
§ `coldsweep.py`, `docs/method/REVIEW.md` rule 2's sweep clause, `CHANGELOG.md`
*Added* entry. `613132e` also touched three record/board surfaces (the index,
the pointer, the intent record); out of the reviewable delta and, for the
intent record, barred.

### Lens 1 — approach and assumptions

Load-bearing assumptions, in my words, before the brief's framing:

- **A1. The defect was a *matching* defect** — a text prefix that did not
  match tool output — and comparing path parts closes the class.
- **A2. `--root` is a repo root, and the repo's records live where atelier's
  do** (`docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`,
  `docs/reviews/`).
- **A3. The tree under `--root` is one repo.**
- **A4. Being "the path of least resistance" displaces `grep`** — a reviewer
  who wants to search will reach for this instead.
- **A5. The four-path tuple is rule 2's bar** — same set, no wider, no
  narrower.

How they held. **A1 half-holds.** The `./`-prefix class is genuinely closed
(probe: the four docstring spellings each bar the same one file). But the tool
opens a new class of *its own* silent non-application: an absolute
`--also-exclude` (which the docstring claims works), a `..` path, a
case-different path and a mistyped path each exclude **nothing**, with no
warning, and the provenance line lists them as excluded (SW1). The tool never
checks that a bar landed. That is the ruling's defect — an exclusion that
silently does not apply — moved from `grep`'s prefix to the tool's own
anchoring. **A2 fails** on a subdirectory root and on a child whose
`.atelier-floor.json` declares `docs` elsewhere (the floor honours that key;
the tool hard-codes `docs/`) — in both, zero files are barred and the run
looks normal (SW2). **A3 fails on this estate:** the harness nests worktrees
under `.claude/worktrees/`, gitignored but on disk, and a sweep from the main
checkout root reads every sibling worktree's `SESSIONS.md`, `docs/sessions/`
and `docs/reviews/` — measured at 596 barred-by-name files in the searched set
while the provenance line reported 299 excluded (SW3). **A4 is unsupported by
the delta:** the tool is named at no surface a reviewer meets at the moment
of sweeping except REVIEW.md rule 2 — not the `review-brief` skill, not the
reviews template, not the onramp's companion list, no `/atelier:` command
(SW8); the harness's native search tool is one keystroke closer than
`python3 tools/coldsweep.py`. **A5 fails as written:** rule 2's prose bars
*prior reviews*; no doctrine surface names the other three paths as barred to
a cold reviewer; the tuple is the only statement of the set (SW4).

**Matching defect or habit defect?** Both, and the build answers only the
first. The three instances (as the delta describes them — I could not read
the verdicts) were reviewers *trying* to exclude and failing on spelling; that
is a matching defect and the parts comparison is the right fix for it. But
what a reviewer reaches for is a habit, and the rule-2 edit alone will not
move it — the same instrument (restating the rule) that the docstring says
"is measurably not the fix". **Counsel on altitude, labelled as counsel:**
keep the soft instrument as the stopping point *for now* — `GUARDS.md`'s
warning about a guard layer consuming the programme is right, and a
harness-level block on `grep`/`Grep` in a reviewer session is a new trust
surface that would want its own ruling — **but** two cheap things belong with
it before the rule-2 clause can honestly say "sweep with the tool": (i) make
the tool fail loud on its own silent geometries (SW1–SW3 — a bar that covers
zero files, a root that is not a repo root, a nested repo boundary), because a
guard that can silently not apply is the defect wearing a different coat; and
(ii) put the invocation where the reviewer's hand already is — the
`review-brief` skill's *Running it* section and the reviews template README,
so every brief's Process section carries it (SW8). Whether the bar should be
*enforced* by a reviewer-session hook is a real question and the principal's;
the evidence for it would be a fourth instance *after* (i) and (ii) land.

### Lens 2 — correctness and quality

Read whole, not the diff. `_parts()` / `is_barred()` / `walk()` / `search()`
traced; every claim below was probed in scratch trees or on the worktree with
`--list-barred` (which prints counts, never content).

- **Happy path is correct.** Repo-root `--root`, relative excludes, atelier
  layout: the four barred surfaces are excluded, siblings (`docs/sessions-x/`,
  `docs/SESSIONS.md.bak`) are not, nested files under a barred dir are, an
  empty entry bars nothing. `.git` and the noise set are skipped. Symlinked
  files and directories are never walked, on both interpreters present here
  (3.9 and 3.14) — the docstring's symlink line is accurate. NUL in the ninth
  KiB: the file is searched, no crash. Bad regex: exit 2 with the `re` message
  on stderr. No match: exit 1. Missing root: exit 2. All reproduced.
- **`--also-exclude` geometries** (SW1): four docstring spellings each cover
  1 file ✓; absolute path under root **0 files**; `docs/../docs/…` **0**;
  case-different **0**; nonexistent **0**. No warning in any of the four; the
  provenance line prints the entry verbatim as "excluded". The docstring's
  "and an absolute path under the root" is false — `_parts()` strips the
  leading `/` and compares machine-relative parts against repo-relative ones.
- **`--root` geometries** (SW2): `--root docs` and `--root tools` on the
  worktree → "4 barred path(s), 0 file(s) excluded", exit 0. Scratch child
  with `.atelier-floor.json` `{"docs": "notes"}` and records under `notes/` →
  all five record files are hits; provenance says 0 excluded. Scratch tree
  with `docs/sessions` a symlink to `store/sessions` → the store is searched
  under its real path (a bar for the link, a hole for the target).
- **Nested repos** (SW3): scratch tree with `.claude/worktrees/sib/docs/…` →
  the sibling's `SESSIONS.md` and `docs/reviews/v.md` are hits under the
  default bar. On the estate: the main checkout has two live nested
  worktrees; a metadata-only walk from its root keeps 1358 files under
  `.claude/worktrees/`, **596** of them rule-2 barred by name (2 × `SESSIONS.md`,
  2 × `ROADMAP-DONE.md`, 177 + 178 under `docs/sessions/`, 119 + 118 under
  `docs/reviews/`) while the top-level bar excludes 299. `.gitignore` names
  `.claude/worktrees/`; the tool does not read it, so gitignored material
  (`.env`-class files, `.claude/settings.local.json`) is searched too.
- **Unreadable file** (SW6): a mode-000 file is silently skipped in `search()`
  (`except OSError: continue`) and still counted in "over N file(s)"; no
  stderr, exit unchanged. That contradicts "a broken sweep is not a clean
  one" and the exit-2 contract for a failed search.
- **Provenance on stdout** (SW5): `coldsweep PAT | wc -l` = hits + 2; a
  pattern that matches the provenance text (`sessions`, `reviews`, `barred`)
  matches the tool's own output line; the `--include-barred` banner is on
  **stdout**, at the **end**, so `| head` drops it and a redirect captures it
  as a hit. The docstring and README both claim "drops into a pipeline".
- **`--list-barred` per-entry counts** are right; the total is right; an
  entry covering 0 files prints `(0 file(s))` — the only place the silent
  no-op is visible, and only if the reviewer runs it.
- **Selftest and tests** (SW7): selftest exercises one shape — spelling of a
  directory bar — plus sibling/prefix boundaries and exit codes; whether that
  is "the three real instances reduced to shapes" I cannot check without the
  barred verdicts, so I state only what it covers. Not covered by tests or
  selftest: `--also-exclude` through `_main`; an absolute exclude (claimed in
  the docstring); a subdirectory `--root`; a nested repo; the provenance
  stream; an unreadable file; the banner's content or stream.
  `test_case_insensitive_flag` asserts the function argument, not the `-i`
  flag. Every test I read asserts the property its name claims. Selftest
  prints its sub-runs' stderr (`bad pattern`, `a PATTERN is required`) before
  `selftest OK`, so a reader scanning sees two error lines in a passing run.
  `python3 -m unittest tools.test_coldsweep` (the brief's suggested form)
  fails: `ModuleNotFoundError: coldsweep` — the bare `import coldsweep`
  works only under `discover -s tools` or from inside `tools/`; the house is
  mixed (`test_board.py` inserts its own dir on `sys.path`; `test_licenscan.py`
  imports bare), so this is a note, not a defect of the delta.
- **Exit-code contract**: holds for match/no-match/bad-regex/no-pattern/bad-root;
  does not hold for the unreadable-file case (SW6). Provenance and banner do
  not affect exit codes.

### Lens 3 — completeness and harvest

- `REVIEW.md` rule 2 carries the clause; *The lifecycle* and rules 1/4 say
  nothing about how to sweep (no conflict, no second surface). `tools/README.md`
  and `CHANGELOG.md` carry it. **Not carrying it** (SW8): the `review-brief`
  skill (the surface that tells a reviewer how to run a pass — its *Running it*
  section names floor, tests, selftests, `/security-review`, and never a
  sweep), the reviews template README under `docs/build/templates/`, the
  onramp skill's companion-command list, `commands/` (no `/atelier:coldsweep`).
  A cold reviewer meets the tool only if it reads rule 2 in full before
  searching.
- `--exclude-dir` survives at `skills/create-repo/SKILL.md:161`
  (`grep -rn --exclude-dir=.git …`) — a scaffold-time scan, not a cold sweep;
  no finding. Nothing else in the live tree instructs a hand-written
  exclusion.
- **Child reach**: the README's `coldsweep.py` entry does not say how a child's
  reviewer invokes it (the house pattern is `$ATELIER_TOOLS` /
  `hooks.atelierTools`, with `--root .` from the child); and per SW2 `--root`
  alone would not honour a child's `docs` override, so the child story is
  incomplete on two counts.
- The intent record is a board item under `docs/roadmap/` and is barred by
  nothing by default; every pass must `--also-exclude` it by hand — the
  discipline the tool was built to remove, in miniature (SW9, counsel).
- Count claim reproduced: 289 tracked files under the four defaults at
  `613132e` (`git ls-tree`, names only). At HEAD: 299 tracked; on disk 297 at
  my first sweep (299 − 3 deferred siblings moved out + 1 untracked sibling
  brief), rising to 301 as parallel passes wrote; my sweeps report one more
  for the intent record. It counts regular files on disk — tracked or not,
  symlinks skipped — whose repo-relative path sits under an entry.

### Lens 4 — security and privacy

atelier is public. **Reach case stated:** this is a landed-delta review under
an orchestrator; the worktree's pending diff is other passes' in-flight
records, so the pending-diff scanner was not run (it would read their briefs
into this reviewer, the SL2 class); the delta is one Python tool, one test
file and three markdown edits, and the markdown class is empty for that
scanner regardless. The lens was worked by hand.

- **Machine paths reach stdout** (part of SW1): an absolute `--also-exclude`
  is echoed verbatim into the provenance line the tool tells the reviewer to
  paste into a verdict — the one line designed to be copied into a public
  record. `--root`'s not-a-directory error prints the resolved absolute path
  to stderr (minor; stderr is rarely pasted). Hit lines print root-relative
  paths ✓; the default provenance line names no machine path ✓.
- **What the tool reads** (part of SW3): every non-barred, non-noise file on
  disk under root — untracked and gitignored included. On this estate that
  reaches `.claude/settings.local.json` (the per-clone allowlist the
  `.gitignore` explains is deliberately unpublished) and any `.env`-class
  file; a hit in one prints its line. A `git ls-files -co --exclude-standard`
  source (rglob fallback for non-git roots) would close SW3's nested-worktree
  hole and this in one move; failing that, `.claude/worktrees` in `NOISE`.
- **`--include-barred` as a one-flag path**: it is, by design, with a banner
  between. Under rule 2's own text a wide sweep is not forbidden, so a soft
  exception is the right altitude; but the banner is last on stdout (SW5), so
  the disclosure prompt is the first thing a `| head` loses. Counsel: banner
  first, on stderr.
- No shell-out, no external code, no network; regex is the reviewer's own.
  Nothing else on this surface.

### Findings

- **SW1 — MAJOR.** `--also-exclude` silently excludes nothing for an absolute
  path under root (docstring: supported), a `..` path, a case-different
  spelling, or a mistyped path; no warning; the provenance line lists the
  entry as excluded and echoes an absolute machine path into the
  paste-into-verdict line. *Reproduce:* on the worktree, `--also-exclude
  <abs>/docs/roadmap/290-…/040-….md --list-barred` → `(0 file(s))`; the
  relative spelling → `(1 file(s))`. *Live trigger:* this pass's own reviewer
  instructions say to use absolute paths everywhere. *Remedy shape:* anchor an
  absolute exclude to root (`pointerscan`'s `(root / raw) if not
  Path(raw).is_absolute() else Path(raw).relative_to(root)` line), normalise
  `..`, and warn on stderr — or exit 2 — for any entry that covers zero files.
- **SW2 — MAJOR.** `--root` at a subdirectory, or at a child whose
  `.atelier-floor.json` declares `docs` elsewhere, bars zero files while the
  provenance asserts the four paths; a symlinked records dir leaves the real
  store searched. *Reproduce:* `--root docs --list-barred` on the worktree →
  0 excluded, exit 0; scratch child with `{"docs":"notes"}` → all records hit.
  *Remedy shape:* read the floor config's `docs` key when present; refuse or
  warn when root has no `.git` / when every default entry covers zero files
  ("the bar matched nothing — is `--root` the repo root?").
- **SW3 — MAJOR.** Nested harness worktrees under `.claude/worktrees/` are
  searched (596 rule-2 barred-by-name files from the main checkout root, two
  live siblings), as is all gitignored material. *Reproduce:* scratch tree
  with `.claude/worktrees/sib/docs/SESSIONS.md` → hit under the default bar;
  metadata walk of the main checkout as above. *Remedy shape:* gitignore-aware
  file source, or `NOISE += (".claude/worktrees",)` plus applying `BARRED`
  below any nested `.git` boundary.
- **SW4 — MODERATE (doctrine; the principal's, rule 3).** The tuple is the only
  statement of the four-path set. `REVIEW.md` rule 2's prose bars *prior
  reviews*; nothing in live doctrine names `docs/SESSIONS.md`, `docs/sessions/`
  or `docs/ROADMAP-DONE.md` as barred to a cold reviewer, so the tool labels
  three paths "rule-2 barred" that rule 2 does not name, and prose and tuple
  can drift with nothing tying them. `CLAUDE.md` onramp step 4 sends every
  session to the `SESSIONS.md` tail, which a cold pass contradicts without
  saying so (the brief-writer's disclosure is this collision, live).
  *Remedy shape:* name the set once in rule 2 (or a cold-sweep clause), have
  the tool cite that clause, and give the onramp a one-line cold-session
  exception — or rule the tuple canonical and say so in prose.
- **SW5 — MODERATE.** Provenance line and `--include-barred` banner go to
  stdout, after the hits: `| wc -l` is hits + 2, a pattern matching the
  provenance text matches the tool's own line, `| head` loses the banner, a
  redirect captures both as hits. Docstring and README both claim pipeline
  fitness. *Remedy shape:* diagnostics to stderr, banner first.
- **SW6 — MODERATE.** An unreadable file is silently skipped and counted as
  swept; exit code unchanged. Contradicts the tool's own "a broken sweep is
  not a clean one" and the exit-2 contract. *Reproduce:* `chmod 0` a file
  carrying the pattern → no hit, no stderr, "over N" includes it. *Remedy
  shape:* report each unreadable path on stderr and exit 2 (or a distinct
  code) when any file could not be read.
- **SW7 — minor.** Test and selftest gaps as listed under lens 2 (no
  `--also-exclude` through `_main`, no absolute-exclude test though claimed,
  no subdirectory root, nested repo, provenance stream, unreadable file, or
  banner test; `-i` tested as an argument not a flag; selftest prints
  sub-run error lines before `selftest OK`; module-form invocation fails on
  the bare import — mixed house convention).
- **SW8 — MODERATE (harvest).** The tool is named on no surface a reviewer
  meets at sweep time other than rule 2: not the `review-brief` skill, the
  reviews template README, the onramp companion list, or `commands/`; the
  README entry does not say how a child's reviewer invokes it, and `--root`
  alone would not honour a child's `docs` override (SW2). *Remedy shape:* one
  line each in the skill's *Running it* and the template; a `$ATELIER_TOOLS`
  invocation in the README entry.
- **SW9 — note (counsel).** The intent record must be `--also-exclude`d by
  hand on every pass — the removed discipline in miniature. Options: the
  queue pointer's *Intent record* ref becomes machine-readable and the tool
  takes `--pointer <path>`; or the brief template's Process section carries
  the exact `--also-exclude` line so it is copied, not composed.
- **SW10 — note.** Docstring/README/CHANGELOG describe the guard accurately for
  the happy path; the docstring's absolute-path claim (SW1) and "drops into a
  pipeline" (SW5) are the two overclaims. `[rejected: grounds]` remains
  available to the author on SW1–SW3, SW5–SW7 as ordinary code; SW4 and the
  rule-2 clause are the principal's.

### Overall

**PASS-WITH-FINDINGS — 3 MAJOR · 4 MODERATE · 1 minor · 2 note.** On the
geometry it was built and tested for — a repo-root `--root`, relative
excludes, atelier's layout, no nested repos — the guard is correct, its tests
pass, and it protected this pass. Off that geometry it fails **silently**
three ways (SW1–SW3), each the ruling's own defect class — a bar that does not
apply while the tool says it did — and one of them (SW3) is live on this
estate from the main checkout root today. Rider, stated plainly: the rule-2
clause "sweep the tree with `tools/coldsweep.py`" should not be leaned on
unqualified until SW1–SW3 land; a reviewer using it now should run
`--list-barred` first and read the per-entry counts, run from the worktree
root, and pass excludes relative.

### Re-run ledger (all at HEAD `574f133`, this worktree, 2026-08-17 13:33–13:41 UTC)

| Run | Result | What it counts |
|---|---|---|
| `python3 tools/coldsweep.py --selftest` | exit 0, `selftest OK` | 15 checks in-tool (two error lines printed by sub-runs, SW7) |
| `python3 -m unittest discover -s tools -p 'test_*.py'` | exit 0, **1344 tests OK** (325 s) | includes the 20 `test_coldsweep` tests |
| `python3 -m unittest tools.test_coldsweep` | exit 1, ImportError | the brief's module-form spelling; SW7 note, not a delta defect |
| `node --test instruments/*.test.js` | exit 0, 235 pass / 0 fail | |
| `floor.py --plane hook` | exit 0; 11 ✅ enforced, 4 👁️ warn-only | pointerscan warns on this pass's own queue pointer (`[grammar] instructs the reviewer` — board item `160/250`, already queued) |
| `floor.py --plane ci` | exit 0; secretscan 🟡 22 advisory (known), leakscan 🟡 no-terms (ci plane by design) | |
| `stampscan --warn` | exit 0; 1 identical region, 121 files suppressed | |
| `--list-barred` at HEAD | 4 defaults → 297 files (first sweep) / 301 (later); + 1 for the intent record | on-disk regular files under the entries; 289 tracked at `613132e` reproduces via `ls-tree` |
| four spellings + absolute + `..` + case + typo | 1 · 1 · 1 · 1 · **0 · 0 · 0 · 0** | SW1 |
| `--root docs`, `--root tools` | 0 excluded, exit 0 | SW2 |
| `--include-barred` banner | stdout, after hits, 3 lines, exit by hits | SW5 |
| scratch child `{"docs":"notes"}` | 5 record hits, 0 excluded | SW2 |
| scratch nested `.claude/worktrees/sib` | 2 sibling record hits under default bar | SW3 |
| main-checkout metadata walk | 1739 kept / 299 skipped; 596 nested barred-by-name | SW3 |
| unreadable file, NUL@9KiB, bad regex, no match | skipped silently (SW6) · searched OK · exit 2 · exit 1 | |
| Python 3.9 vs 3.14 | identical output on the hazard tree; symlinked dirs walked by neither | |

No suite result looked like interference; nothing was re-run for that reason.

### Follow-up checklist

- [ ] SW1 — anchor absolute/`..` excludes to root; warn or exit 2 on a
      zero-file entry; stop echoing machine paths.
- [ ] SW2 — honour the floor config's `docs`; refuse/warn when the default bar
      matches nothing.
- [ ] SW3 — gitignore-aware source or `.claude/worktrees` in `NOISE`; bar at
      nested repo boundaries.
- [ ] SW4 — the principal: name the four-path set in doctrine once, cite it
      from the tool; onramp step 4's cold-session exception.
- [ ] SW5 — provenance and banner to stderr, banner first; fix the docstring
      and README claims.
- [ ] SW6 — report unreadable files, exit 2.
- [ ] SW7 — tests for each of the above; quieten selftest sub-runs.
- [ ] SW8 — name the tool in the `review-brief` skill and the reviews
      template; child invocation in the README entry.
- [ ] SW9/SW10 — counsel; take or decline with grounds.
- [ ] Phase 2: reconcile against the sibling when released; fold and delete;
      update pointer `160/240`; rebuild the index (orchestrator).
