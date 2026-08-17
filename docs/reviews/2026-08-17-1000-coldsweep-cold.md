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
