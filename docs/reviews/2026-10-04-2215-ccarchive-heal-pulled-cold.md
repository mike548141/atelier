# Cold pass — ccarchive's skip-path heal pulled

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-04 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/510-rule-4-cold-pass-queued-the-heal-pulled.md`.
**Why it earns a review:** ccarchive holds the only durable copy of every
session transcript; this delta removes a repair path that an earlier pass found
could overwrite a good archived copy, and a removal that is incomplete, or that
strands the state the repair existed for, leaves that copy untrustworthy in a
different way.

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

- `1da9101` (2026-10-03) — ccarchive: pull the skip-path heal
- `5870927` (2026-10-03) — the earlier commit that added the checkpoint and the
  heal; context for what was removed, already reviewed separately — review what
  `1da9101` left standing, not `5870927` afresh

Delta paths:

- `instruments/ccarchive`
- `instruments/ccarchive.test.js`
- `instruments/man/ccarchive.1`

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Driven, not read. Whether the removal is complete: no code path at HEAD lets the
source overwrite an intact mirror copy without the shrink guard or `--force`.
Whether what the removed path used to repair is now reported, silently skipped,
or left permanently wrong — construct each lagging shape by hand in a scratch
archive (a manifest entry behind its archive file, an archive file with no
manifest entry, a hash mismatch in each direction, a source truncated after it
was archived, a run killed between copy and checkpoint) and run an archive pass
then `--verify` over each, recording what changes, what is reported and the exit
code. Whether the manifest checkpoint that remains is still correct without the
heal beside it. Whether the tests removed or rewritten leave the surviving
behaviour pinned, and whether a test now asserts the overwrite cannot happen.
Whether the man page describes the tool as it stands. **Non-goal:** encryption
at rest, and the board items that commissioned the work.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Pulling a repair presumes the state it repaired is either rare, harmless, or
   caught elsewhere: find which, and test it. Ask whether removal was the
   narrowest safe answer or whether it trades one integrity failure for a
   quieter one.
2. **Correctness & quality.** Read all of `instruments/ccarchive` and its tests.
   Diff `1da9101`. Run `node --test instruments/*.test.js`, `--help`, and every
   state in *Scope*. Check every exit path is in the man page's EXIT STATUS and
   no dead code, flag, message or test fixture of the removed path survives.
3. **Completeness / harvest.** Every surface that states the archive's integrity
   contract: the man page, `instruments/README.md`, the ADR 0006 record's
   ccarchive material, `CHANGELOG.md`, `--help`. Does each still hold at HEAD,
   and does any still promise the removed repair?
4. **Security & privacy** — mandatory. The tool writes a durable store from
   source files it does not control. Check no remaining path lets a crafted or
   damaged source (timestamp, size, truncation, symlink) replace or shadow a
   good archived copy, and that partial writes land safely. The house scanner is
   discharged by grounds (landed delta; the pending diff is other passes' drafts
   and this brief) — say so, and deliver the code-altitude read by hand, against
   the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `node --test instruments/*.test.js` (foreground, once)
- `instruments/ccarchive --help`; the man page's option superset test
- every lagging and crash state in *Scope*, in a scratch archive under your
  clone, never against the real archive or `~/.claude`

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
`docs/roadmap/160-doctrine-review-owed/510-rule-4-cold-pass-queued-the-heal-pulled.md`
(it carries the author's own lens hints), and:

- `docs/reviews/2026-10-03-0357-manifest-checkpoints-cold.md` (the prior verdict
  on the heal)
- `docs/reviews/2026-07-17-1000-adr0006-ccarchive-preserve-cold.md` and
  `docs/reviews/2026-07-17-1157-cli-docs-applied-cold.md`
- every item under `docs/roadmap/210-instruments-open-features/`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-1004 --also-exclude
docs/roadmap/160-doctrine-review-owed/510-rule-4-cold-pass-queued-the-heal-pulled.md
--also-exclude docs/roadmap/210-instruments-open-features <pattern>` — rule 2's
default bar, plus `--also-exclude` for the items above; `--include-barred` only
with disclosure in the verdict. Reading the *delta* is never barred: the code,
its tests, the doctrine text and the catalogue entries are the subject. What is
barred is the author's narrative of why, and the verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `HL`: `HL1`, `HL2`, …) and severities (MAJOR / MODERATE
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
