# Cold pass — the pre-flip gate learns from the first flip; publishscan --history

**Pass type:** doctrine and code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/740-rule-4-cold-pass-queued-the-pre-flip-gate.md`.
**Why it earns a review:** making a repository public cannot be undone. This delta
adds three binding steps to the one doctrine home of the gate run before that
moment, and a new mode of the guard the gate relies on to see what the flip will
publish; a gap in either is found only after the publication it was meant to stop.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is dated
  2026-10-05 11:20 UTC (an Opus orchestrator with dispatched workers; the pointer
  counts the workers' output as the run's authorship). Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by a
  Mike-opened Opus queue-run session (id prefix `abe96d8d`) on 2026-10-16 UTC, on
  Mike's answer that day that a fresh Opus session writes these briefs. It
  authored none of the delta. It is **off-tier for review, disclosed: it forms no
  finding and writes no severity**, and it stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that
  passes rule 4's criterion. The reviewer repeats its own provenance in its
  verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This
  brief-writer read: the queue pointer in full; the landing commit's subject,
  `--stat`, the `AUTONOMY.md` and `CHANGELOG.md` diffs, a keyword skim of the
  `publishscan.py` diff, **and the message body** (the author's own account); the
  subjects and `--stat` of later commits on the same files; `REVIEW.md` rules 1–4,
  the four lenses, the checklist and the lifecycle; the ask halves of two
  2026-10-04 briefs as templates; `docs/reviews/` filenames and filename-level
  greps (no prior verdict opened); the names, not contents, of the commissioning
  board items; and its harness-loaded memory index. Its orchestrator read the
  `docs/SESSIONS.md` index tail through 2026-10-16 (including the authoring run's
  one-paragraph summary) and the 2026-10-16 session record's close section, and
  passed on no evaluative content beyond the pointer list. Everything evaluative
  is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD):

- `89ff0d8` (2026-10-05 18:41 UTC) — publish: the pre-flip gate learns from the
  first flip (260/110); landed in merge `ce3f776` (2026-10-05 18:42 UTC)

Delta paths: `docs/method/AUTONOMY.md` (three new sub-bullets under the
making-public clause), `tools/publishscan.py` (`--history`, `history_findings`,
`run_history`, the streamed NUL reader, round-3 pattern `*.egg-info/`),
`tools/test_publishscan.py`, `tools/README.md` (publishscan section),
`CHANGELOG.md` (the 2026-10-05 entry).

**Later commits on the same files — not this delta; do not attribute them to
it.** `c1cef10` (2026-10-05 18:56 UTC) — publishscan reads the tip and staged
planes NUL-delimited (260/120; its own pass is 160/760); `CHANGELOG.md` and
`tools/README.md` have many later entries. Earlier, `ffabef3` had already moved
publishscan onto the shared report contract (160/730).

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

**The doctrine.** Whether each new bullet is executable by a session holding only
`AUTONOMY.md`: "the scrub runs last, over the gate's own records" — is there a
point at which the gate's records are final, or does writing the scrub's own
record reopen it? "A planted canary is reconciled shape by shape" — where are the
shapes listed, and what is the gate's state when one does not fire? "The doctrine
pin is current at the flip" — which tool or procedure is "the drift check
(PROPAGATION)", does it exist and run as named, and what is "the inlined floor"?
Whether the three bullets agree with `RECORD.md` § *The record is public*,
`PROPAGATION.md`, ADR 0005 and any repo-creation or publication skill that walks
the same moment. **The tool.** Whether `--history` sees every path a visibility
flip publishes. Build repos in a scratch area and test: a path added and deleted
on a branch merged long ago; a path added only on a side branch later merged; a
path added in a merge commit's own diff; a rename (with `--no-renames`); a path
on a pushed branch whose local remote-tracking ref was pruned; tags pointing at
non-commit objects; a path only in a stash; refs the hosting service publishes
that a clone does not fetch by default (pull-request refs, unreachable commits by
hash); submodule entries; names with newlines, non-ASCII bytes and leading dashes;
a commit message whose text looks like a path list. Whether the shallow-clone
refusal and the "not a git repository" path give the right exit code for a gate
that must not pass blind. **Non-goal:** the principal's choice to build all four
harvest items before the next flip.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that local branches, tags and remote-tracking refs approximate what
   the host will publish; that path names are the right unit (not content) for a
   history check; that opt-in is safe when the gate doctrine says the gate "runs"
   it — what enforces that it runs?
2. **Correctness & quality.** Read the three bullets in context and
   `publishscan.py`'s history mode and tests whole; diff `89ff0d8`. Record a table
   for the history cases above: published by a flip? reported? Check the
   streamed reader's parsing of git's `-z` header-and-names layout, the stderr
   drain and non-zero-exit path, and the "oldest adding commit" and "still
   tracked" fields.
3. **Completeness / harvest.** Every surface that describes the pre-flip gate or
   publishscan: `tools/README.md`, `docs/method/GUARDS.md`, `SECURITY.md`, ADR
   0005, `skills/` that cover creating or publishing a repo, and the child
   templates. Does each mention `--history` where it should, and does any still
   describe the gate without the three new steps? Is the changelog entry true?
4. **Security & privacy** — mandatory. The history mode shells out to git on a
   repo about to be published; check argument construction, repository-local
   config that could alter `git log` output or run commands, and whether output
   or findings can echo a private repo's name next to its scan state — the very
   join the first new bullet forbids. Never quote any such name in the verdict.
   `/security-review` is discharged by grounds (a landed delta; the pending diff
   is not the work) — say so, and deliver the code-altitude read by hand against
   the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_publishscan -v`; `python3 tools/publishscan.py
  --selftest`; `--help` shows `--history` and its refusal with `--staged`
- `python3 tools/publishscan.py --history --root .` on this repo and on your
  scratch fixture repos; a shallow clone of a fixture must exit 2
- the "default output byte-identical" claim, re-driven at landing on this repo
  and your fixtures only: `89ff0d8^` against `89ff0d8`, stdout, stderr and exit
  code (the commit's 29-repo measurement is not re-run — never point a scanner
  at other repos on the machine; say so)
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Fixture repos, shallow clones and older checkouts go in a private
  area under your session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground. Never point a scanner at any other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta, or keep the tree clean whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address, private repo
  name or personal detail — this repo is PUBLIC; describe and locate instead.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-16-1551-pre-flip-gate-history-cold.deferred.md`,
and the commissioning items `090`, `110` and `120` in
`docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/` (barred as a
section; `090` holds the harvest the bullets cite as evidence).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/740-rule-4-cold-pass-queued-the-pre-flip-gate.md
--also-exclude docs/reviews/2026-10-16-1551-pre-flip-gate-history-cold.deferred.md
--also-exclude docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, the history-case table,
findings with stable IDs (prefix `PF`: `PF1`, `PF2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with
counts, a re-run ledger, and a follow-up checklist. Then STOP and commit phase 1
unrevised before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3): record
all, apply nothing; counsel per finding is welcome, labelled and kept beneath it.
