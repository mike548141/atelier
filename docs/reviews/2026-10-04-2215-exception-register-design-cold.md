# Cold pass — the exception-register design, before it is accepted or built

**Pass type:** design cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-04 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/650-rule-4-cold-pass-queued-exception-register-design.md`.
**Why it earns a review:** a draft ADR that would change how every guard in
every repo records an exception; reviewed now, a wrong shape costs a redraft,
and reviewed after the build it costs fourteen scanners and every child's
markers.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-04 UTC
  with the prompt "Do all cold reviews and any other work dependent on fable",
  on the Fable tier (`claude-fable-5-1`), orchestrating four rule-4 passes (code
  and design passes from a seventeen-pointer queue; the principal sized this
  sitting to the weekly allowance he had left). It wrote this brief from the
  queue pointer, the landing commits' subjects and file lists, and the delta
  paths' names; it did not open the intent record or any prior verdict on these
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

- `0013025` (2026-10-03) — decisions: draft the exception register

Delta paths:

- `docs/decisions/2026-10-03-0641-the-exception-register.md` (draft, 114 lines)

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

This is a design review per `docs/method/REVIEW.md` § *Review the design, not
only the build*: the subject is a decision not yet taken. Whether the design
solves the problem it states, and whether that is the right problem. Read the
mechanisms it would replace or sit beside as they stand at HEAD — the inline
allow markers and their shared grammar in `tools/`, every ignore file
(`.leakscanignore` and its siblings), the floor's softening configuration, and
the deferment and allowance doctrine in `docs/method/GUARDS.md` and neighbours —
and test the draft against them: what does each existing exception become, can
every one be expressed, and what is the migration for this repo and for a child
that floats at the floor's `@main`? Whether the record's fields can all be
supplied at the moment an exception is made, by an agent and by a person, and
who checks them. Whether "narrowest unit" is decidable by a tool for text and
for binary files, and what happens when the excepted content moves, is
reformatted, or is duplicated. Whether the register can go stale, be bypassed,
or itself leak what it excuses (this repo is public; a register that quotes the
excepted string publishes it). Alternatives the draft did not weigh. What the
smallest first build would be and what it must prove. **Non-goal:** none
declared by the draft is binding on you; the principal's own words quoted in the
draft are the commission and are not under review — their interpretation is.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first,
   before reading the draft's own list if it has one. Separate what the
   principal's quoted words require from what the draft adds, and say where the
   draft narrowed, widened or re-read them.
2. **Correctness & quality.** Internal consistency and buildability: walk three
   real exceptions from this repo (one inline marker, one ignore-file glob, one
   softened guard) through the design end to end and record where each step is
   underspecified. Check every factual claim the draft makes about the current
   tools by running or reading them.
3. **Completeness / harvest.** What the draft leaves out: migration, the hook
   and CI planes, children and the template, the records and doctrine that would
   need to change, the review and ruling it needs before build, and its relation
   to open ADRs and drafts under `docs/decisions/`.
4. **Security & privacy** — mandatory. A register of exceptions is a map of
   where the guards do not look. Consider who can add to it, whether an addition
   is reviewable in a diff, whether it can be widened silently, and whether it
   discloses secrets, personal data or private repositories' names by recording
   them. `/security-review` is discharged by grounds (a prose design; no code
   delta) — say so.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- every factual claim in the draft about a tool's current behaviour: run the
  tool or read the code and record agreement or not
- count the live exceptions in this repo by mechanism (inline markers by guard,
  ignore-file lines, softened guards) so the migration's size is measured
- the floor on both planes at HEAD (the draft is a tracked file)

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
`docs/roadmap/160-doctrine-review-owed/650-rule-4-cold-pass-queued-exception-register-design.md`
(it carries the author's own lens hints), and:

- every item under `docs/roadmap/110-estate-duplication-exception-audit-mike/`
  and `docs/roadmap/115-guardrail-architecture-mike-commissioned/`
- `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md` and
  `docs/reviews/2026-08-05-1320-f1-guards-allowances-cold.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-1004 --also-exclude
docs/roadmap/160-doctrine-review-owed/650-rule-4-cold-pass-queued-exception-register-design.md
--also-exclude docs/roadmap/110-estate-duplication-exception-audit-mike
--also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `XR`: `XR1`, `XR2`, …) and severities (MAJOR / MODERATE
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
