# Cold pass — the doctrine-reporting duty, the route's three shapes, and the no-harm rules for a hand-up

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/300-rule-4-cold-pass-queued-report-up-duty.md`.
**Why it earns a review:** this is the rule by which every repo in the fleet
reports a defect in the house doctrine to the parent; if the route is wrong or
harmful, defects stop arriving or arrive in a form that damages the public
parent.

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

- `5bb78f2` (2026-08-24) — the landing commit
- `54201e0` (2026-09-18) — the widening: step 3's "self-removing" reworded
  (`310/110`)
- ⚠️ `48c181f` (2026-09-20) — later, separately-queued work (`160/360`) rewrote
  § *The route* rule 2 and the first two bullets of § *Report without harming
  the parent*. Review this delta's surfaces at HEAD and name what the later
  commit changed

Delta paths:

- `docs/method/PROPAGATION.md` § *Pointing up* — the widened subtitle; the new §
  *The duty — every repo reports, atelier remediates*; the three filing shapes
  inside § *The route* step 1; the new § *Report without harming the parent*
- `docs/method/PROPAGATION.md` § *The standard child doctrine block* — the
  bullet-count sentence, and the `floor` region's new **Doctrine problems point
  up** bullet
- `docs/build/templates/CLAUDE.md` — the same bullet, stamped
- `CLAUDE.md` — atelier's own § *Hard constraints* gains the duty

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the three filing shapes cover the cases a child actually meets (a child
with no remote; a child whose principal is not atelier's; a private child whose
finding cannot be stated without private detail) — the fleet's hand-ups since
2026-08-24 are the evidence: read the merged `320/…` items at HEAD as *data
about which shape each took*, not as verdicts. Whether the no-harm rules are
checkable by the parent at merge (what does a parent session actually run to
verify a hand-up did no harm) or only aspirational. Whether the bullet-count
sentence is right by counting at HEAD. **Non-goal:** the principal's commission
of the duty.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   duty says *every repo reports, atelier remediates* — attack whether a duty
   with no check behind it is the class the house keeps re-breaking, and whether
   the route's step 1 gives a child enough to file without reading atelier's
   internals.
2. **Correctness & quality.** Diff the three commits for the in-scope paths.
   Check every cross-reference resolves at HEAD; check the stamped bullet is
   inside the floor region the scanner compares; count the bullets.
3. **Completeness / harvest.** Search for every other surface describing how a
   child reports: `skills/`, `docs/build/REPO-STANDARD.md`, `CONTRIBUTING.md`
   and its template, `SECURITY.md` (does the security-disclosure route and the
   doctrine-report route agree on where a *security* doctrine defect goes?).
4. **Security & privacy** — mandatory. atelier is PUBLIC and hand-ups arrive
   from private children. The no-harm rules are the privacy control: test them
   against the worst case — a child whose finding *is* a leak (a term, a path, a
   person) — and say whether the rules as written stop the finding from carrying
   the leak into the parent's public board. Discharge the house scanner by
   grounds in one line.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `stampscan`, `blockscan` (if registered), `linkscan`, `pathscan` over
  `docs/method`, `docs/build`, `CLAUDE.md` at HEAD, floor invocations
- the floor on both planes at HEAD
- the bullet count, by counting

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
`docs/roadmap/160-doctrine-review-owed/300-rule-4-cold-pass-queued-report-up-duty.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-08-23-1314-recovery-then-five-defects-in-the-instruments.md`
  and `docs/sessions/2026-09-18-0114-queue-run-hand-up-fixes.md`
- the board items `docs/roadmap/310-*/110-*.md` and the
  `320-*/…reachable-parent…` item that the landing commit widened

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/300-rule-4-cold-pass-queued-report-up-duty.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `RU`: `RU1`, `RU2`, …) and severities (MAJOR / MODERATE
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
