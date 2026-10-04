# Cold pass — personal data held by purpose, with recorded exceptions

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-04 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/630-rule-4-cold-pass-queued-pii-by-purpose.md`.
**Why it earns a review:** the personal-data rule of a public repository and of
the template every child is created from was re-worded from a visibility rule to
a purpose rule; a loose word here is what lets a private detail into a public
tree, in this repo and in every child that copies the template.

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

- `1ffefc7` (2026-10-03) — build: personal data is held for a purpose, with
  recorded exceptions

Delta paths:

- `docs/build/REPO-STANDARD.md` — the personal-data bullet
- `docs/build/templates/CLAUDE.md` — the personal-data constraint
- `docs/build/templates/CONTRIBUTING.md` — the personal-data constraint
- `CLAUDE.md` (this repo's own) — the first hard constraint

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the four statements say the same rule, and whether that rule is workable
by a session that has only the sentence in front of it. Read each at HEAD and
diff `1ffefc7`. Test the wording against cases: a public repo, a private repo, a
repo that changes visibility, a template copied into a new child before anyone
has recorded an exception, a commit message, a session record, a review verdict,
a fixture file, git history. For each, does the text say what may be written,
who decides an exception, where it is recorded, in what form, and what happens
to an exception that is found unrecorded? Whether "purpose" is defined well
enough to refuse something, or can justify anything. Whether the exceptions this
repo itself holds (the published author identity and account name) are in fact
each declared where they appear — find every occurrence and check. Whether the
rule and the enforcing guard agree: read `tools/leakscan.py`'s documented
behaviour, its ignore file and its inline markers as they stand, and say where
the text promises more than the guard enforces or the guard enforces what the
text no longer says. Whether a child reading only its stamped template gets a
rule that is complete without atelier's own files. **Non-goal:** the principal's
rule itself, which the delta quotes — its placement, the wording around it and
its consistency are the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Separate the words the delta attributes to the principal from the wording the
   authoring run put around them, and say where the surrounding text narrows,
   widens or re-reads what is quoted. Ask whether a purpose rule is weaker or
   stronger than the visibility rule it replaced, for a public repo
   specifically.
2. **Correctness & quality.** Read the four passages and every sentence that
   cross-refers to them. Check the four agree term by term (who, what, where
   recorded, which exceptions). Run the case list in *Scope* and record a table.
   Check every link and anchor the passages cite resolves.
3. **Completeness / harvest.** Every other surface that states a personal-data
   rule or the old visibility framing: `docs/method/` (SECRETS, GUARDS,
   CONVENTIONS, the apex, PROPAGATION's floor region), `SECURITY.md`,
   `CONTRIBUTING.md` (this repo's own), `README.md`, the create-repo skill,
   `tools/README.md`, and the stamped floor block if the rule is part of it.
   Which still state the old rule, and is the template's stamp version or
   changelog owed a bump for children to notice?
4. **Security & privacy** — mandatory. This lens is the subject. Hunt for the
   reading of the new text under which a session could commit personal data to
   this public repository and call it compliant; check whether the delta itself,
   or the records around it, introduced any personal detail. Never quote any
   such detail in the verdict — describe and locate it. `/security-review` is
   discharged by grounds (a prose doctrine delta already landed; the pending
   diff is other passes' drafts) — say so.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- the leak guard on both planes at HEAD, and tree-wide, with exit codes read
  explicitly
- find and count every recorded personal-data exception in this repo and check
  each is declared where it appears
- the stamp and block guards over the template files (`stampscan`, `blockscan`),
  to see whether the delta kept the stamped regions in step
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
`docs/roadmap/160-doctrine-review-owed/630-rule-4-cold-pass-queued-pii-by-purpose.md`
(it carries the author's own lens hints), and:

- every item under `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-1004 --also-exclude
docs/roadmap/160-doctrine-review-owed/630-rule-4-cold-pass-queued-pii-by-purpose.md
--also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `PI`: `PI1`, `PI2`, …) and severities (MAJOR / MODERATE
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
