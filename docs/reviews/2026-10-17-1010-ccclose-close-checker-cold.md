# Cold pass — ccclose, the close-out checker

**Pass type:** code and design cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/870-rule-4-cold-pass-queued-ccclose.md`.
**Why it earns a review:** it is a first-of-kind instrument that encodes `RECORD.md`'s
close declaration as code: what it passes is what a session will cite as proof that
nothing is owed. It runs `git`, `gh` and a repo's own `tools/board.py`, reads every
project's transcripts, attributes work by a time window, and joined the expected
toolbox, so every session on the machine may now reach for it.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is dated
  2026-10-16 15:01 UTC (an Opus orchestrator with dispatched workers; the pointer counts
  the worker's output as the run's authorship; the build commits' trailers name an Opus
  model). The `TOOLBOX.md` row landed in that run's close commit. Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-17
  by the Mike-opened Fable review session working in worktree `atelier-review-1017`, on
  Mike's 2026-10-16 answer that a fresh Opus session writes these briefs. It authored
  none of the delta. It is **off-tier for review, disclosed: it forms no finding and
  writes no severity**, and it stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes
  rule 4's criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier
  conditions apply and are disclosed in the claim, the pointer and the verdict. The
  reviewer repeats its own provenance in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This brief-writer
  read: its instruction file; the four queue pointers it was assigned (160/860–890) in
  full, and 160/500 in full as the shape of an append line (including that item's
  result line); the staging directory's file listing, and the first 50 lines of one
  peer brief of this batch (160/850) and its append, for shape; the landing commits'
  subjects, `--stat` **and message bodies** (the author's own account, including the
  merge's and the close commit's, which carry principal answers); the close commit's
  `TOOLBOX.md` diff; `instruments/ccclose.design.md` whole at HEAD; `instruments/ccclose`
  in part (its help text, helpers, wrapper and bypass tables, board, claim and floor
  checks, and `collect`'s head) and a function outline; the README's ccclose section;
  the later commit's diff on `instruments/ccclose`, the design note and the README;
  three templates in full; `docs/reviews/` filenames and filename-level greps (no prior
  verdict opened); and its harness-loaded memory index. Writing the other three briefs
  of its set, it also read those deltas' diffs and message bodies, and grep-hit lines
  of a sweep that included single lines of board items 115/290 and 115/320. It did not
  open the intent
  record, the commissioning item, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or `docs/method/REVIEW.md`. What its orchestrator read is the
  orchestrator's to disclose; it passed on an instruction file, three templates and a
  list of taken prefixes, and no evaluative content. Everything evaluative is in the
  sibling.

## What the work is

Landing commits (diff them; review the paths at HEAD, `2f9cfe4` or later):

- `ef3673a` (2026-10-16 15:59 UTC) — instruments: design note for ccclose, the
  close-out checker (020/180)
- `4eda680` (2026-10-16 16:17 UTC) — instruments: build ccclose, the close-out checker
  (020/180)
- `6ccbc7a` (2026-10-16 16:23 UTC) — merge: ccclose, the close-out checker (020/180).
  The merge changes none of the delta paths against `4eda680` (checked); it also
  carries a `CHANGELOG.md` entry
- `09a61b4` (2026-10-16 21:18 UTC) — session-close: record Mike's two close answers;
  install ccclose. Only its `docs/method/TOOLBOX.md` hunk is this delta

Delta paths: `instruments/ccclose`, `instruments/ccclose.test.js`,
`instruments/ccclose.design.md`, `instruments/man/ccclose.1`, the ccclose section and
any other ccclose lines of `instruments/README.md`, and the estate's-own-tools row of
the expected-toolbox table in `docs/method/TOOLBOX.md`.

**A later commit on the same files — not this delta; do not attribute it to it.**
`cea247e` (2026-10-16 16:43 UTC, merged in `99f4c2a`) — cctranscript: classify harness
text in user records instead of counting it as prompts. It replaced ccclose's own
wrapper list and record classification with cctranscript's, and rewrote design-note §6.
It is pass 160/880's subject. Review ccclose at HEAD, but where a defect sits in a hunk
`cea247e` wrote, say so and leave its charge to that pass; diff `4eda680` against
`cea247e^` to tell them apart. Nothing touches the delta paths after `99f4c2a`.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and
live behaviour. The lenses organise it; they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Each check against its design row.** The design note's §7 table gives, per check,
  what it reads and when it fails or is not applicable. For all eleven, drive each state
  the row names and record which the code reaches, and whether any input can produce a
  ✅ the row does not license ("a check never reports a pass it could not read for").
- **Attribution.** The window heuristic, the live session's window running to now, the
  8-character id prefix rule, and the claim-date rule. Test the claim checks against
  the claim lines actually on this repo's board at HEAD (their position in the item,
  their leading characters, the case and shape of the date), not only the fixtures'.
- **The floor check.** The sha chosen, per-workflow latest run, the red and green
  conclusion sets, pending, no runs, `gh` missing or unauthenticated — against
  `RECORD.md`'s floor-at-head rule and what `gh run list` returns at the cap.
- **Read-only, in fact.** Every subprocess ccclose starts and every file it opens.
  `--no-optional-locks` covers git; does anything else write (`gh`'s own caches,
  `python3` byte-compiling a repo's `board.py`)? Which code from the repo under check
  does it execute, and with what?
- **The heuristics' errors.** The close-ask patterns and the workaround-command table:
  for each, a false negative on a phrasing or command shape the house actually uses,
  and a false positive a session would have to answer every close.
- **The output contract.** Field-set stability, caps and whether a capped list says it
  was cut, the `unknown` versus `0` rule, `--json` parity with the text form, exit
  codes, and the help-versus-man drift guards the design names.
- **Where a session is told to run it.** `RECORD.md`, `CONCURRENCY.md`, the onramp and
  queue-run skills, `TOOLBOX.md`: is the tool referenced where a closing session would
  look, and does any text now claim more than the tool proves?

**Non-goals:** the principal's decision to build a close-out checker and his acceptance
shape (quoted verbatim in the design note), and the model-router idea the design marks
out of scope. The checks chosen, their states and the wording around the quote are in
scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Among
   them: that a transcript window attributes work well enough to print a ❌; that a
   tool whose passes are cited as evidence may rest three checks on "never fails"; that
   `instruments/` is the right home for something with a doctrine role (ADR 0006).
2. **Correctness & quality.** Read `instruments/ccclose` and its tests whole; diff the
   two build commits. Build the check table from *Scope*, one row per check and state,
   with the input that reaches it. Check whether the tests' fixtures were derived from
   the board's real claim grammar and real `gh` output or from the same reading that
   wrote the code.
3. **Completeness / harvest.** The design note against the code at HEAD (every "added in
   the build" mark, every claim of reuse); the man page and README against both; the
   `CHANGELOG.md` entry; the doctrine sites in *Scope*; `instruments/install` and the
   README's install section, now that the toolbox lists the tool.
4. **Security & privacy** — mandatory. Transcript discovery reads every project folder
   under the operator's Claude directory; `--session` accepts any path; the asks list
   quotes the principal's prompts into output that is "pasted into records" — in a
   PUBLIC repo. `CCCLOSE_GH` chooses which binary runs. A checked repo's own
   `tools/board.py` is executed. Weigh each. Never quote real transcript content in the
   verdict. `/security-review` is discharged by grounds (a landed delta; the pending diff
   is not the work) — say so, and do the code-altitude read by hand against the OWASP
   catalogue.

## Re-run obligation

Re-run, do not read. Lift invocations from `.github/workflows/ci.yml` (the instruments
job) rather than guessing.

- `node --test instruments/ccclose.test.js`, then the whole instruments suite once as CI
  runs it (`node --test instruments/*.test.js`), foreground
- `mandoc -T lint instruments/man/ccclose.1`; `node instruments/ccclose --help` by path
- live runs by path, never by bare name: build throwaway git repos, a fake `HOME` and
  synthetic transcripts in your scratchpad, stub `gh` through `CCCLOSE_GH`, and drive
  each state in the check table; snapshot `.git` (index, refs, lock files, mtimes)
  before and after to test the read-only claim
- one run against your own scratch clone of this repo, only after the read-only claim
  has held on a throwaway; never against the shared checkout or another repo
- mutation, in a scratch clone: flip one load-bearing condition per check and record
  which tests fail
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and
  the hook plane as `.githooks/pre-commit` invokes it)

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is
  fine. Probes, fixtures, mutated copies and older checkouts go in a private clone under
  your session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the instruments suite at most once
  whole, in the foreground. Never point a scanner or ccclose at any other repo on the
  machine. Never run an installed tool by bare name from `PATH`; instruments are
  symlinked onto it from another checkout.
- `/security-review` reads the session's pending diff: discharge it by grounds for this
  landed delta, or keep the tree clean whenever you spawn it — never with this brief or
  its sibling dirty.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ English.
  Never quote a secret, placeholder token, email address, personal detail or real
  transcript text — this repo is PUBLIC; describe and locate instead.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.deferred.md`,
the landing commits' message bodies (the author's account; read subjects, stats and
diffs only), and the commissioning and neighbouring items:

- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/180-the-mechanisable-form-of-it.md`
- `docs/roadmap/210-instruments-open-features/250-cctranscript-counts-harness-text-as-prompts.md`

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/870-rule-4-cold-pass-queued-ccclose.md
--also-exclude docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.deferred.md
--also-exclude
docs/roadmap/020-policy-as-code-programme-five-tracks-mik/180-the-mechanisable-form-of-it.md
--also-exclude
docs/roadmap/210-instruments-open-features/250-cctranscript-counts-harness-text-as-prompts.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is
never barred; the design note is part of the delta.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append
your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, what you read), per-lens answers, the standing checklist V1–V7 each
answered or discharged with grounds, the check table, findings with stable IDs (prefix
`CL`: `CL1`, `CL2`, …) and severities (MAJOR / MODERATE / minor / note), an overall
PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger, and a follow-up
checklist. Then STOP and commit phase 1 unrevised before opening the sibling. Edit no
other file.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding
notes against the seeded questions and the intent record, any finding formed at
reconcile marked as such, and the overall line restated. Never revise phase-1 text.
Then fold the sibling in below the reconcile and delete it.

Findings on a tool that encodes doctrine are the principal's to decide (rule 3): record
all, apply nothing; counsel per finding is welcome, labelled and kept beneath it.
