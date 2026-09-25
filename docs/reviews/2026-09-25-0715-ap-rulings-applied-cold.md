# Cold pass — the AP rulings applied — the ADR 0008 amendment and its code surfaces

**Pass type:** code + doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/090-rule-4-review-queued-tier-fable-pass-type-code.md`.
**Why it earns a review:** an ADR control clause re-worded to describe a
boundary that is deliberately *not* enforced, plus the code and workflow
surfaces that clause describes — a wrong word here is inherited by every child
that calls the floor at `@main`.

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

- `501ec37` (2026-08-23) — the landing commit; it also carries the FR rulings'
  application to `tools/pathscan.py`, which is **outside** this pass's delta

Delta paths:

- `docs/decisions/0008-enforcement-is-called-not-copied.md` — the 2026-08-23
  amendment at the foot (AP1 truth re-word; AP2 list correction)
- `tools/floor.py` — the softenable-set docstring (note: the file was
  substantially edited on 2026-09-18 and 2026-09-20 by later, separately-queued
  work; review the docstring's claim as it stands at HEAD and name which later
  commit moved it, if any)
- `.github/workflows/floor.yml` — the two `env:`-routed signature steps (AP3)
- `tools/leakscan.py` + `tools/test_leakscan.py` — the explicit-terms-path error
  (AP4); the file was later rewritten to stream (2026-09-20), so check the AP4
  behaviour survived
- the queued board items `docs/roadmap/115-*/180-*.md` and
  `docs/roadmap/020-*/340-*.md` as the delta's own account of what it left open

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the amendment says the truth about `main`'s boundary as it stands at
HEAD — re-read the live state (`gh api
repos/mike548141/atelier/branches/main/protection`, `gh api
repos/mike548141/atelier/rulesets`) rather than trusting the amendment's
description of it — and whether the `env:`-routed signature steps close the
injection shape they were written against or only move it. Whether the
softenable set the docstring describes is the set the registry actually enforces
(read `SOFTENABLE`/equivalent against every `Scanner` entry). Whether the AP4
error path in `leakscan.py` fires on the shape it names and on the neighbouring
shapes it does not. **Non-goal, and it does not fence the risk:** the
principal's rulings (AP1–AP8) are not under review — only their application in
text and code.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   The amendment claims a control clause can be *honest about not being
   enforced* and still be the thing that makes a floating `@main` call safe —
   test whether an appended amendment that contradicts the clause above it
   leaves a reader with one truth or two. Consider whether "not enabled,
   deliberately" is a state the ADR can carry without a review line of its own.
2. **Correctness & quality.** Diff `501ec37` for the in-scope paths only. Trace
   the two workflow steps: does routing an untrusted value through `env:`
   actually stop shell interpolation for every consumer of that step, including
   any `run:` that re-expands it? Run the leakscan tests; construct the AP4
   error case by hand with a path that does not exist, a path that is a
   directory, and an empty file, and say what each prints and exits.
3. **Completeness / harvest.** Every other surface that describes `main`'s
   boundary or the softenable set: `tools/README.md`, `CONTRIBUTING.md` (the
   repo's and the template's), `docs/build/REPO-STANDARD.md`, `SECURITY.md`, the
   `floorfleet` boundary row added 2026-09-18. Do they agree with the amendment,
   or does one still state the pre-amendment claim?
4. **Security & privacy** — mandatory. atelier is PUBLIC. The amendment names
   what is *not* protected on `main` — is that disclosure itself an exposure (it
   tells an attacker the branch accepts unsigned, unreviewed pushes from any
   collaborator) or is it the honest floor the doctrine requires? Say which, as
   counsel. Check the workflow steps for the OWASP injection class they were
   written against and for the `pull_request_target` / fork-secrets class beside
   it. The house security scanner reads the session's pending diff, and in this
   shared worktree that is other passes' drafts — it is **discharged by
   grounds** here (landed-delta review); say so in one line and deliver the
   code-altitude read by hand.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_leakscan tools.test_floor
  tools.test_precommit` at HEAD; the full Python suite once (`python3 -m
  unittest discover -s tools`) and note the count
- `python3 tools/floor.py --validate` (or the invocation `.githooks/pre-commit`
  actually uses — lift it, don't guess) on the hook plane
- the live boundary read named in *Scope*, with the output recorded (redact
  nothing — it is public API data about a public repo)
- the `env:`-routing claim: reproduce a value containing `$(…)` and backticks
  flowing through the step in a scratch workflow dry-run or by reading the shell
  the step generates

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
`docs/roadmap/160-doctrine-review-owed/090-rule-4-review-queued-tier-fable-pass-type-code.md`
(it carries the author's own lens hints), and:

- the verdict `docs/reviews/2026-08-09-0824-ep-application-cold.md` (the AP
  verdict and its § *Rulings — 2026-08-23*, which is this delta's intent record)
- `docs/reviews/2026-07-26-2215-adr0008-enforcement-propagation-cold.md` (the EP
  verdict beneath it)
- `docs/ROADMAP-DONE.md` § *The EP application*

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/090-rule-4-review-queued-tier-fable-pass-type-code.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `AR`: `AR1`, `AR2`, …) and severities (MAJOR / MODERATE
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

Findings on doctrine are the principal's to decide (rule 3): record all, apply
nothing; your counsel per finding is welcome, labelled as counsel and kept
beneath the finding.
