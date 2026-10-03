# Cold pass — ccarchive's manifest checkpoints and stale-entry heal

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this pass's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-03 0357 UTC; the review runs under the
orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/460-rule-4-cold-pass-queued-the-manifest-checkpoints.md`.
**Why it earns a review:** ccarchive holds the only durable copy of every session transcript; a change to how its manifest is written and repaired is a change to whether that copy can be trusted after an interrupted run.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-03 with
  the prompt "Do all cold reviews and any other work dependent on fable", on
  the Fable tier (`claude-fable-5-1`), orchestrating six rule-4 passes queued
  by that run. It wrote this brief from the queue pointer, the landing commits'
  subjects and `--stat` file lists, and the delta paths' names; it did not open
  the intent record.
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
  that the pointer existed and named its subject in a phrase; nothing else from
  that run was read. Earlier in the same sitting this session commissioned
  read-only inventories of the board's open items and of every verdict in
  `docs/reviews/`, for a ruling round; the summaries it received include prior
  findings on the surfaces under review. Those summaries are author-side
  framing this pass must meet cold; every line of them that bears on this delta
  has been moved to the sibling and kept out of this brief. The brief-writer
  also read the 2026-09-25 batch's staged-plane brief as a formatting template,
  the session index entries of 2026-09-19 to 2026-10-01, and, as doctrine at
  onramp, `docs/method/REVIEW.md`, `docs/method/00-APEX.md` and
  `docs/method/COMMUNICATION.md` § *Asking for a ruling* at HEAD.

## What the work is

Landing commits (diff these; review the paths at HEAD, `17c75a9` or later):

- `0264387` (2026-10-03) — merge of `5870927`: ccarchive checkpoints the manifest and heals a lagging entry (board `210/170`)

Delta paths:

- `instruments/ccarchive` — the checkpoint writes and the heal path
- `instruments/ccarchive.test.js` — its tests
- `instruments/man/ccarchive.1` — the page's account of both

`instruments/README.md` and the ADR 0006 record did not change; whether they still describe the tool is yours to establish.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Driven, not read: in a scratch archive, run an archive pass and kill it part way (SIGKILL, and separately a full disk or a read-only manifest path); inspect the manifest and the archive for agreement; run `--verify`; then run again and record what heals, in which direction, and what is reported. Construct each lagging shape by hand (archive entry newer than manifest, manifest entry with no archive file, hash mismatch, a truncated source that is newer) and drive the heal over each. Confirm the shrink guard and `--force` still behave as the man page says. **Non-goal:** the board item that commissioned the work, and encryption at rest.

## The four lenses

1. **Approach & assumptions.** A checkpoint presumes a write order that survives a crash: find the interleaving where the manifest claims an entry the archive lacks, or the reverse. A heal presumes it can tell lagging from corrupt: find the case where healing overwrites the good copy.
2. **Correctness & quality.** Read all of `instruments/ccarchive` and its tests. Run `node --test instruments/*.test.js`, the man-page superset test, `--help`, and every state in *Scope*. Check every new exit path is in EXIT STATUS.
3. **Completeness / harvest.** Every surface that states the archive's integrity contract: man page, `instruments/README.md`, the ADR 0006 record's ccarchive addendum, `CHANGELOG.md`. Does each still hold at HEAD?
4. **Security & privacy** — mandatory. The tool writes to a durable store from untrusted source files and heals on its own judgement. Check the heal cannot be steered by a crafted source (timestamp, size, hash collision shape), that temp files and partial writes land with safe modes, and that a symlinked source or destination is handled. The house scanner is discharged by grounds (landed delta; the pending diff is this brief) — say so, and deliver the code-altitude read by hand, against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `node --test instruments/*.test.js` (foreground, once)
- `instruments/ccarchive --help`; the man page's option superset test
- every crash and heal state in *Scope*, in a scratch archive under your clone

## House rules for this run

- You work in the shared review worktree `/Users/mike/worktrees/atelier-review-430`
  (branch `review-430-1003`), read-only except for THIS brief file. Other
  reviewers are working there at the same time on their own briefs; never open
  another `docs/reviews/2026-10-03-*` file — it is another pass's framing. Run
  **no git command that writes** there (no add, commit, stash, checkout,
  worktree, reset, clean). Read-only git (`log`, `show`, `diff`, `blame`) is
  fine. Mutation probes, scratch children and checkouts of older commits go in
  your own clone: `git clone /Users/mike/worktrees/atelier-review-430
  <scratchpad>/MC/probe` under the session scratchpad, named by your
  prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full suite at most once,
  in the foreground with a long timeout; if a memory-probe test times out, note
  it as environmental and re-run that test file alone before recording it.
  Never scan any tree outside the worktree or your scratch clone, and never
  point a scanner at the machine's other repos. Other sessions are live on this
  machine and in this repo's primary checkout; touch nothing there.
- `/security-review` is **discharged by grounds**: it reads the session's
  pending diff, which here is other passes' drafts and this brief, and this is a
  landed-delta review. State that line in your lens-4 answer and deliver the
  code-altitude read by hand.
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
`docs/roadmap/160-doctrine-review-owed/460-rule-4-cold-pass-queued-the-manifest-checkpoints.md`
(it carries the author's framing and this pass's claim line), and:

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` (the
  intent record)
- the board item `docs/roadmap/210-*/170-*.md` (the commission)
- the verdicts `docs/reviews/2026-07-17-1000-adr0006-ccarchive-preserve-cold.md` and `docs/reviews/2026-07-17-1157-cli-docs-applied-cold.md`
- `docs/roadmap/210-*/020-*.md`, `210-*/030-*.md`, `210-*/160-*.md` (open ccarchive items)

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-430 --also-exclude
docs/roadmap/160-doctrine-review-owed/460-rule-4-cold-pass-queued-the-manifest-checkpoints.md
--also-exclude docs/roadmap/210-instruments-open-features <pattern>` — rule 2's
default bar plus the items above; `--include-barred` only with disclosure in
the verdict. Reading the *delta* is never barred: the code, its tests, the
README entries and the registry are the subject. What is barred is the author's
narrative of why, and the verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `MC`: `MC1`, `MC2`, …) and severities
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
