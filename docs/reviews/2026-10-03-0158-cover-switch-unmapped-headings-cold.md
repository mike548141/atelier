# Cold pass — `stampscan --require-stamps` and blockscan's unmapped-heading report

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this pass's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-03 0158 UTC; the review runs under the
orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/430-rule-4-cold-pass-queued-the-cover-switch-and-unmapped-headings.md`.
**Why it earns a review:** both tools are guards. One decides whether a floor
block in a child is verbatim; the other decides whether a doctrine edit landed
inside a region a guard watches. A guard that reports clean over nothing, or
over a region it cannot see, is the inversion class this repo keeps finding.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the merges named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-03 with
  the prompt "Do all cold reviews and any other work dependent on fable", on
  the Fable tier (`claude-fable-5-1`). It wrote this brief from the queue
  pointer, the landing merges' subjects and `--stat` file lists, and the delta
  paths' names; it did not open the intent record.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree and
  outside the harness scratchpad (subagents can read the scratchpad), commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the authoring run told this session over the cross-session channel
  that the pointer existed and named the two features; nothing else from that
  run was read. Earlier in the same sitting this session commissioned read-only
  inventories of the board's open items and of every verdict in
  `docs/reviews/`, for a ruling round; the summaries it received include prior
  findings on both tools under review (the 2026-09-25 floor-verbatim pass on
  `stampscan`, and the naming-precedence and report-up-duty passes, which name
  `blockscan`'s heading map). Those summaries are the author-side framing this
  pass must meet cold; every line of them that bears on these tools has been
  moved to the sibling and kept out of this brief. The brief-writer also read
  the 2026-09-25 batch's staged-plane brief as a formatting template, the
  session index entries of 2026-09-19 to 2026-10-01, and, as doctrine at
  onramp, `docs/method/REVIEW.md`, `docs/method/00-APEX.md` and
  `docs/method/COMMUNICATION.md` § *Asking for a ruling* at HEAD.

## What the work is

Landing commits (diff these; review the paths at HEAD, `b7520a5` or later):

- `3cb2f64` (2026-10-03) — merge of `4e83dc3`: `stampscan --require-stamps`,
  so a run that checked nothing cannot pass (board `320/130`)
- `33b3c5f` (2026-10-03) — merge of `bd09b1b` and `172d767`: blockscan reports
  the headings its map cannot see, collapsing top-level ones to a count (board
  `320/340`)

Delta paths:

- `tools/stampscan.py` — the `--require-stamps` switch
- `tools/test_stampscan.py` — its tests
- `tools/blockscan.py` — the unmapped-heading report in `--check`
- `tools/test_blockscan.py` — its tests
- `tools/README.md` § *stampscan* and § *blockscan*

Neither commit touched `tools/floor.py`, `.github/workflows/ci.yml` or
`.githooks/pre-commit`; whether the new behaviour is reachable from any wired
invocation is yours to establish from those files at HEAD.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Driven, not read: in a scratch clone, run `stampscan` with and without the new
switch over a tree with zero stamped blocks, over a tree whose only stamps sit
inside fenced code, over a tree where the mixed-root invocation finds the
source but no child, and over a child that resolves the source through a pin.
Run `blockscan --check` over a doctrine file whose edit sits in a `###`
subsection under a mapped `##`, over a file with a heading the map has never
seen at each level, over a renamed heading, and over a heading inside a fenced
block; record what each run prints and what it exits. Compare every wired
invocation of both tools at HEAD (`floor.py` registry, `ci.yml`, the hook,
the child `floor.yml` template) with the invocations the tests exercise.
**Non-goals:** the board items that commissioned the work, and whether either
tool should be in the floor registry at all.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. A
   switch that makes "checked nothing" a failure presumes the tool can tell
   nothing from something: find the shape where the count is non-zero but the
   cover is still empty. A report of unmapped headings presumes the map's
   keying is the right unit: find the edit the new report still cannot see.
2. **Correctness & quality.** Read all of both tools and both test files. Run
   each tool's `--selftest`, its unit tests, and the full Python suite once.
   Drive every state in *Scope*. Check the collapsed top-level count against
   the uncollapsed list for the same tree.
3. **Completeness / harvest.** Every surface that describes either tool's
   contract: `tools/README.md`, the module docstrings, `--help`, the floor
   registry's `why`, `CHANGELOG.md`, and the child template's workflow. Does
   each say what the tool now does, and does any wired caller pass the new
   switch?
4. **Security & privacy** — mandatory. Both tools read files named by argv and
   print paths and heading text; check argument handling against a path with
   a leading `-` or spaces, a heading containing control or bidi characters,
   and a map entry that names a path outside the root. The house scanner is
   discharged by grounds (landed delta; the pending diff is this brief) — say
   so, and deliver the code-altitude read by hand, checked against the OWASP
   catalogue where the work has a code surface.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/stampscan.py --selftest`; `python3 tools/blockscan.py
  --selftest`; `python3 -m unittest tools.test_stampscan tools.test_blockscan`;
  the full Python suite once (`python3 -m unittest discover -s tools`, in the
  foreground)
- the floor on both planes at HEAD
- every state in *Scope*, driven in a scratch clone

## House rules for this run

- You work in the review worktree `/Users/mike/worktrees/atelier-review-430`
  (branch `review-430-1003`), read-only except for THIS brief file. Run **no git
  command that writes** there (no add, commit, stash, checkout, worktree,
  reset, clean). Read-only git (`log`, `show`, `diff`, `blame`) is fine.
  Mutation probes, scratch children and checkouts of older commits go in your
  own clone: `git clone /Users/mike/worktrees/atelier-review-430
  <scratchpad>/CU/probe` under the session scratchpad.
- One heavy process at a time on this machine: run the full Python suite at
  most once, in the foreground with a long timeout; never scan any tree outside
  the worktree or your scratch clone, and never point a scanner at the
  machine's other repos. Other sessions are live on this machine and in this
  repo's primary checkout; touch nothing there.
- `/security-review` is **discharged by grounds**: it reads the session's
  pending diff, which here is this brief, and this is a landed-delta review.
  State that line in your lens-4 answer and deliver the code-altitude read by
  hand.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" and would
  block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ English.
  Never quote a secret, a placeholder token, an email address or any personal
  detail — this repo is PUBLIC; describe, don't quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/430-rule-4-cold-pass-queued-the-cover-switch-and-unmapped-headings.md`
(it carries the author's framing and this pass's claim line), and:

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` (the
  intent record)
- the board items `docs/roadmap/320-*/130-*.md` and `docs/roadmap/320-*/340-*.md`
  (the commissioning items), and `docs/roadmap/160-*/340-*.md`, `160-*/360-*.md`,
  `160-*/300-*.md` (pointers that carry prior verdicts' outcome lines on these
  tools)
- the verdicts `docs/reviews/2026-09-25-0715-floor-verbatim-cold.md`,
  `2026-09-25-0715-naming-precedence-cold.md` and
  `2026-09-25-0715-report-up-duty-cold.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-430 --also-exclude
docs/roadmap/160-doctrine-review-owed/430-rule-4-cold-pass-queued-the-cover-switch-and-unmapped-headings.md
--also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up
--also-exclude docs/roadmap/160-doctrine-review-owed <pattern>` — rule 2's
default bar plus the items above; `--include-barred` only with disclosure in
the verdict. Reading the *delta* is never barred: the code, its tests, the
README entries and the registry are the subject. What is barred is the author's
narrative of why, and the verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `CU`: `CU1`, `CU2`, …) and severities (MAJOR / MODERATE
/ minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with the commands and their results, and a follow-up checklist.
Then STOP and report to the orchestrator that phase 1 is written. Do not open
the sibling (it is not in the tree); do not edit the queue pointer, the board,
or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
record, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings are the principal's to decide (rule 3): record all, apply nothing;
your counsel per finding is welcome, labelled as counsel and kept beneath the
finding.
