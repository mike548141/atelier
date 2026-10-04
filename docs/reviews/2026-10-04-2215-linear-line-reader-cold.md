# Cold pass — the linear line reader in three guards

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-04 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/660-rule-4-cold-pass-queued-linear-reader.md`.
**Why it earns a review:** the line reader in the secret, leak and
conflict-marker guards was rewritten for speed; these are the guards a public
repo's every commit depends on, and a reader that splits or joins lines
differently changes what they see without any test of theirs noticing.

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

- `55426a1` (2026-10-03) — leakscan: linear line reader
- `633f6e9` (2026-10-03) — secretscan: linear line reader
- `b5cc3c4` (2026-10-03) — conflictscan: linear line reader
- ⚠️ `643cf80` (shared allow-marker grammar) touches the same files and is
  **outside** this delta — reviewed separately

Delta paths:

- the line readers in `tools/leakscan.py`, `tools/secretscan.py`,
  `tools/conflictscan.py`
- their tests in `tools/test_leakscan.py`, `tools/test_secretscan.py`,
  `tools/test_conflictscan.py`

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether each new reader yields exactly the lines, line numbers and byte offsets
the old one did, for every input — extract old and new readers (parent of each
commit against HEAD, in a scratch clone) and run them differentially over the
repo's tree and over generated inputs: empty file; no trailing newline; CRLF,
lone CR, mixed; a line longer than every buffer; a line ending exactly on each
buffer boundary and one byte either side; a multi-byte UTF-8 character and a
CRLF pair split across a boundary; invalid UTF-8; NULs; a BOM; form feeds,
vertical tabs and the Unicode line separators that `str.splitlines` honours and
a byte split on newline does not. Property-test it with random inputs and random
chunk sizes if the chunk size can be injected. Then at tool level: seed a
fixture secret, a fixture term and a conflict marker at each of those positions
and confirm each guard still finds it with the right line number, and that an
allow marker still binds to the same line. Whether the three readers are one
function or three copies, and if copies, whether they differ. Whether the
linear-time claim holds — measure it. **Non-goal:** the allow-marker grammar
change named above, and what the guards' patterns match.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   "Linear, same output" is two claims; the tests may prove the first and assume
   the second. Establish what definition of a line each guard needs (its
   findings quote line numbers and its allow markers bind by line) and whether
   the new reader keeps it.
2. **Correctness & quality.** Read the three readers and their tests whole. Diff
   the three commits. Run the three test files, the three `--selftest`s and the
   full suite once. Run the differential and the tool-level seeding in *Scope*
   and record a table. Time old against new on a large many-line file and on one
   enormous line.
3. **Completeness / harvest.** Every other guard that reads lines (`grep -n` for
   the reader's name and for per-line slicing across `tools/`): which still
   carry the old shape, and is that recorded anywhere a reader of
   `tools/README.md` would find? Do the README paragraphs for the three guards
   still describe them?
4. **Security & privacy** — mandatory. These are the secret and leak guards of a
   public repository. Any input on which the new reader yields less than the old
   is a way to commit a secret unseen: hunt for it specifically, including an
   attacker-chosen line ending or boundary position. Use fixture strings you
   invent that are not real credentials and never quote them in the verdict. The
   house scanner is discharged by grounds (landed delta; the pending diff is
   other passes' drafts and this brief) — say so, and deliver the code-altitude
   read by hand, against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- the three test files and `--selftest`s; the full Python suite once, foreground
- the old-versus-new reader differential, with the input classes in *Scope*
- the tool-level seeding at boundary positions, all three guards
- old-versus-new timing on two large generated files
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
`docs/roadmap/160-doctrine-review-owed/660-rule-4-cold-pass-queued-linear-reader.md`
(it carries the author's own lens hints), and:

- `docs/reviews/2026-09-25-0715-bounded-guard-layer-cold.md`,
  `docs/reviews/2026-09-25-0715-secretscan-stream-pathscan-roots-cold.md`,
  `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`
- every item under `docs/roadmap/110-estate-duplication-exception-audit-mike/`
  and `docs/roadmap/115-guardrail-architecture-mike-commissioned/`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-1004 --also-exclude
docs/roadmap/160-doctrine-review-owed/660-rule-4-cold-pass-queued-linear-reader.md
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
with stable IDs (prefix `LN`: `LN1`, `LN2`, …) and severities (MAJOR / MODERATE
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
