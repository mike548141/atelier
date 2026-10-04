# Cold pass — pathscan and linkscan stream and cap

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-04 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/640-rule-4-cold-pass-queued-bounded-pathscan-linkscan.md`.
**Why it earns a review:** two enforced guards were rewritten to read in a
stream and to stop reporting at a cap; a guard that caps can exit green past the
cap, and a streamed reader can miss what a whole-file reader found across a
chunk boundary.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-04 UTC
  with the prompt "Do all cold reviews and any other work dependent on fable",
  on the Fable tier (`claude-fable-5-1`), orchestrating six rule-4 passes (code,
  design and doctrine passes from a seventeen-pointer queue; the principal sized
  this sitting to the weekly allowance he had left). It wrote this brief from
  the queue pointer, the landing commits' subjects and file lists, and the delta
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

- `c1a3856` (2026-10-03) — pathscan: stream files and cap findings
- `d64c019` (2026-10-03) — linkscan: cap findings, memoise link resolution,
  linear reader
- `87f984f` (2026-10-03) — both: always print the over-cap count
- merge `6b1dc9a` carries the first two. ⚠️ `acb2c78` / `e5b44fe` (pathscan
  brace expansion) and `643cf80` (shared allow-marker grammar) touch the same
  files and are **outside** this delta — reviewed separately

Delta paths:

- `tools/pathscan.py`, `tools/linkscan.py`
- `tools/test_pathscan.py`, `tools/test_linkscan.py`
- the two tools' paragraphs in `tools/README.md`

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether each guard finds, at HEAD, every finding its pre-delta self found — run
both versions (parent of `c1a3856` and HEAD, in a scratch clone) over the repo's
own tree and over fixtures you build, and diff the findings and exit codes.
Fixtures: a finding that straddles any chunk or buffer boundary the streaming
introduces; a very long single line; a file with no trailing newline; CRLF and
lone-CR line ends; invalid UTF-8 and a BOM; a file of only NULs; an allow marker
and its target on either side of a boundary; a file larger than any size
threshold. For the cap: whether the exit code is still red when findings exceed
it, whether the count printed past the cap is true, whether a cap of findings
can hide a different file's findings, and whether the cap is a grounded number
or a fitted one. For linkscan's memoised resolution: whether a cached answer can
be wrong for a second link (relative links from different directories, anchors,
case-insensitive filesystems, a target created or removed during the run).
Whether the README paragraphs say what the tools do. **Non-goal:** the
brace-expansion and allow-marker changes named above.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Streaming presumes no finding needs more context than the reader holds; a cap
   presumes the reader of the output needs only "there are more". Test both
   against how the hook, CI and the floor's renderer actually consume these
   tools' output.
2. **Correctness & quality.** Read both tools and both test files whole. Diff
   the three commits. Run both test files, both `--selftest`s and the full suite
   once. Run the parent-versus-HEAD differential in *Scope* and record it. Time
   each tool on one large generated file and say whether the bounded-memory
   claim holds (measure peak RSS, do not infer it).
3. **Completeness / harvest.** `tools/README.md`, `docs/method/GUARDS.md`, the
   scanner registry in `tools/floor.py`, and any other guard that shares the
   reader or the cap helper. Is the cap's behaviour documented where a child
   would look, and do the other bounded guards cap the same way?
4. **Security & privacy** — mandatory. A guard that can be made to go quiet is a
   security defect. Check whether a committed file can push real findings past
   the cap, hide a finding behind a boundary, or make the tool exit 0 on error
   (unreadable file, decode error, exception in the stream). The house scanner
   is discharged by grounds (landed delta; the pending diff is other passes'
   drafts and this brief) — say so, and deliver the code-altitude read by hand,
   against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- both tools' test files and `--selftest`; the full Python suite once,
  foreground
- the parent-versus-HEAD differential over the repo tree and your fixtures
- peak memory and wall time on one large generated file, both versions
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
`docs/roadmap/160-doctrine-review-owed/640-rule-4-cold-pass-queued-bounded-pathscan-linkscan.md`
(it carries the author's own lens hints), and:

- `docs/reviews/2026-09-25-0715-bounded-guard-layer-cold.md`,
  `docs/reviews/2026-09-25-0715-secretscan-stream-pathscan-roots-cold.md`,
  `docs/reviews/2026-10-03-0448-pathscan-brace-expansion-cold.md`,
  `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`
- every item under `docs/roadmap/110-estate-duplication-exception-audit-mike/`
  and `docs/roadmap/115-guardrail-architecture-mike-commissioned/`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-1004 --also-exclude
docs/roadmap/160-doctrine-review-owed/640-rule-4-cold-pass-queued-bounded-pathscan-linkscan.md
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
with stable IDs (prefix `BP`: `BP1`, `BP2`, …) and severities (MAJOR / MODERATE
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
