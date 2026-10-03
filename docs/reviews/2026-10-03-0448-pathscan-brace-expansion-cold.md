# Cold pass — pathscan's brace expansion and inline `./` skip

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this pass's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-03 0448 UTC; the review runs under the
orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/490-rule-4-cold-pass-queued-pathscan-brace-expansion.md`.
**Why it earns a review:** pathscan is the guard that says a path a doctrine
file cites still exists. A change to what it counts as a path reference decides
both what it stops flagging and what it can no longer see; a wrong skip is a
stale reference that reads as clean.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-03 with
  the prompt "Do all cold reviews and any other work dependent on fable", on
  the Fable tier (`claude-fable-5-1`), orchestrating seven rule-4 passes queued
  by that run. It wrote this brief from the queue pointer, the landing commits'
  subjects and `--stat` file lists, and the delta paths' names; it did not open
  the intent record or the pull request.
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
  writing): this session found the pointer on `main`; earlier in the sitting
  the authoring run had told it over the cross-session channel that a pathscan
  change was held as a draft pull request for the principal's ruling, and the
  landing merge's subject says the principal ruled. Earlier in the same sitting
  this session commissioned read-only inventories of the board's open items and
  of every verdict in `docs/reviews/`, for a ruling round; the summaries it
  received include prior findings on pathscan. Those summaries are author-side
  framing this pass must meet cold; every line of them that bears on this delta
  has been moved to the sibling and kept out of this brief. It also ran pathscan
  once over the whole tree to identify a standing warn-only finding on the hook
  plane, and read the finding list's first eight lines. The brief-writer read
  the 2026-09-25 batch's staged-plane brief as a formatting template, the
  session index entries of 2026-09-19 to 2026-10-01, and, as doctrine at onramp,
  `docs/method/REVIEW.md`, `docs/method/00-APEX.md` and
  `docs/method/COMMUNICATION.md` § *Asking for a ruling* at HEAD.

## What the work is

Landing commits (diff these; review the paths at HEAD — the worktree carries
`main` at `57b9764` or later, which includes the delta):

- `e5b44fe` (2026-10-03) — merge of `acb2c78`: pathscan expands brace groups and
  skips inline-span command invocations (pull request 96)

Delta paths:

- `tools/pathscan.py` — candidate extraction: brace-group expansion, and the
  skip for an inline code span that is a `./` command invocation
- `tools/test_pathscan.py` — its tests

`tools/README.md` § *pathscan*, `tools/floor.py` and the workflows are not in
the merge's file list; whether they still describe and wire the tool correctly
is yours to establish. Note that a separate merge the same day (`5d087ec`)
single-sourced pathscan's allow-marker and ignore-file code into
`tools/allowmarker.py`; that change is another pass's subject, but its effect on
this delta's behaviour is in scope.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Driven, not read: build a fixture doctrine tree whose prose cites paths in every
brace shape — a single group, two groups in one path, a nested group, an empty
alternative, a group with spaces, an unbalanced brace, a brace inside a fenced
block, a shell-style `${VAR}` and a `{{ template }}` that are not path groups, a
group whose expansions partly exist and partly do not — and every inline `./`
shape: a real command invocation, a real relative path that happens to start
with `./`, a `./` path with arguments, a `./` inside a longer span. Run pathscan
with `--json` over that tree at the landing commit's parent and at HEAD in a
scratch clone and diff the outputs; every difference is either a declared
behaviour change or a finding. Then run it over this repo's gated scope at both
commits and account for every finding that appeared or disappeared.
**Non-goals:** whether pathscan should block rather than warn, and the board
items that commissioned the change.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself.
   Expanding a brace group presumes the braces are a path shorthand: find the
   text that is not, and record what the tool now reports. Skipping an inline
   `./` span presumes it is a command, not a citation: find the stale path the
   skip now hides.
2. **Correctness & quality.** Read all of `tools/pathscan.py` and its tests.
   Run `--selftest`, `python3 -m unittest tools.test_pathscan` (or the form the
   suite actually uses — lift it from CI), the full Python suite once in the
   foreground with a long timeout, and every state in *Scope*. Check the
   expansion is bounded on a pathological input.
3. **Completeness / harvest.** Every surface that says what pathscan catches
   and does not: `tools/README.md`, the module docstring's false-negative list,
   `--help`, the floor registry `why`, `CHANGELOG.md`. Do they describe the two
   new behaviours and their residuals?
4. **Security & privacy** — mandatory. The tool reads files named by argv and a
   scope declaration and prints path text from them: check an expansion that
   resolves outside the root, a group that explodes combinatorially, and control
   or bidi characters in a cited path. The house scanner is discharged by
   grounds (landed delta; the pending diff is this brief) — say so, and deliver
   the code-altitude read by hand, against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/pathscan.py --selftest`; pathscan's unit tests; the full
  Python suite once (foreground, long timeout)
- the floor on both planes at HEAD
- the fixture-tree `--json` diff and the gated-scope diff, parent against HEAD

## House rules for this run

- You work in the review worktree `/Users/mike/worktrees/atelier-review-430`
  (branch `review-430-1003`), read-only except for THIS brief file. Never open
  another `docs/reviews/2026-10-03-*` file — each is another pass's verdict on a
  sibling delta. Run **no git command that writes** there (no add, commit,
  stash, checkout, worktree, reset, clean). Read-only git (`log`, `show`,
  `diff`, `blame`) is fine. Before you start, confirm the delta is present:
  `git -C /Users/mike/worktrees/atelier-review-430 merge-base --is-ancestor
  e5b44fe HEAD` must exit 0; if it does not, stop and report. Mutation probes,
  fixture trees and checkouts of older commits go in your own clone: `git clone
  /Users/mike/worktrees/atelier-review-430 <scratchpad>/PX/probe` under the
  session scratchpad.
- One heavy process at a time on this machine: run the full suite at most once,
  in the foreground with a long timeout (allow 20 minutes); if a memory-probe
  test times out, re-run that test file alone before recording it. Never scan
  any tree outside the worktree or your scratch clone, and never point a
  scanner at the machine's other repos. Other sessions are live on this machine
  and in this repo's primary checkout; touch nothing there.
- `/security-review` is **discharged by grounds**: it reads the session's
  pending diff, which here is this brief, and this is a landed-delta review.
  State that line in your lens-4 answer and deliver the code-altitude read by
  hand.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" and would
  block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ English.
  Never quote a secret, a placeholder token, an email address, a private
  repo's name or any personal detail — this repo is PUBLIC; describe, don't
  quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/490-rule-4-cold-pass-queued-pathscan-brace-expansion.md`
(it carries the author's framing and this pass's claim line), pull request 96's
description and comments, and:

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` (the
  intent record)
- every item under `docs/roadmap/320-child-filed-findings-via-pointing-up/`
  (the commissioning items are among them)
- every item under `docs/roadmap/160-doctrine-review-owed/` and
  `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/` (pointers that
  carry prior pathscan verdicts' outcome lines)

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-430 --also-exclude
docs/roadmap/320-child-filed-findings-via-pointing-up --also-exclude
docs/roadmap/160-doctrine-review-owed --also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec <pattern>` — rule 2's
default bar plus the items above; check each `--also-exclude` path exists before
relying on it, and use `--include-barred` only with disclosure in the verdict.
Reading the *delta* is never barred: the code, its tests, the README entry and
the registry are the subject. What is barred is the author's narrative of why,
and the verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read, at which SHA), per-lens
answers, findings with stable IDs (prefix `PX`: `PX1`, `PX2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, a re-run ledger with the commands and their results, and a
follow-up checklist. Then STOP and report to the orchestrator that phase 1 is
written. Do not open the sibling (it is not in the tree); do not edit the queue
pointer, the board, or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
record, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings are the principal's to decide (rule 3): record all, apply nothing;
your counsel per finding is welcome, labelled as counsel and kept beneath the
finding.
