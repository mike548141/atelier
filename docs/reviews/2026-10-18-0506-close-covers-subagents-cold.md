# Cold pass — the close declaration covers subagents, and ccclose's identifiers form

**Pass type:** doctrine and code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-18 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/920-rule-4-cold-pass-queued-close-covers-subagents.md`.
**Why it earns a review:** it changes what "ready to close" must carry, in doctrine
every session reads at close, and adds the check that a session will cite as proof
that no agent is still running. Its worst failure is a ✅ on *Subagents finished*
while an agent is still live: the principal closes the tab on that signal and the
agent dies silently, which is the exact loss the rule exists to prevent. The
identifiers form prints a block designed to be pasted into records, some of them in
public repos, and every plain run now ends with it.

## Spawn provenance

- **Author of the work under review:** a Mike-opened Opus 5.5 queue run, 2026-10-18,
  which dispatched the Sonnet worker that wrote the code; the pointer counts the
  worker's output as the run's authorship. The same run widened the delta to the
  identifiers form, and the pointer was widened again on `main` (to `bdb1aba`) after
  this brief-writer's worktree was made. Not opened here beyond the pointer.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on
  2026-10-18 by a different Mike-opened Opus 5.5 queue run (worktree
  `atelier-qr-briefs-1018`), which authored none of this delta. This brief-writer
  authored none of it either. It is **off-tier for review, disclosed: it forms no
  finding and writes no severity**, and it stops after this brief, its sibling, and
  one other brief pair (160/940).
- ⚠️ **Channel contact, disclosed by the orchestrator** (roadmap `280/040`). The
  dispatching run was started by the principal directly; the authoring session neither
  started nor instructed it. While this brief was being written, the authoring session
  (one session throughout, `e1d4097c`) sent that run's orchestrator one cross-session
  file-set notice: `ccclose` had changed under a parallel worker, rebase before merging,
  and which commits had landed and widened two pointers. It carried no view of any
  delta. The orchestrator also read the close section of the authoring session's record
  and, before landing it, this brief and its sibling. Weigh that as you see fit.
- **Who takes the review:** a further cold Fable session, not yet started, that passes
  rule 4's criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier
  conditions apply and are disclosed in the claim, the pointer and the verdict. The
  reviewer repeats its own provenance in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This brief-writer
  read: its dispatch prompt; `skills/review-brief/SKILL.md`; `docs/method/REVIEW.md`
  lines 55–234; the queue pointers 160/920 and 160/940 in full, 160/780 in full
  (including its recorded verdict line on another surface), the head of 160/870 (the
  earlier ccclose pass) and the head of 160/900; the earlier ccclose brief
  `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md` lines 1–221 and its
  folded sibling, **and that file's heading outline, which carries the titles of its
  verdict's findings on ccclose** (a prior verdict on this tool, met for shape; its
  body was not read). Of the delta: `089fcdc` whole; `a738f85`'s design-note and
  README hunks; `4142efb`'s design-note hunk; `8b30ee6` whole; `bdb1aba`'s `RECORD.md`
  and man-page hunks — all read body-free
  through `tools/coldsweep.py --commit`, and subjects and stats only for every other
  commit named here. **No delta commit's message body was read.** It ran this brief's
  re-run lines once (below). It did not open the intent record, board items 210/280 or
  210/290, `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or
  `CHANGELOG.md`. Its harness also loaded the user-level and repo instruction files and
  a memory index. What its orchestrator read is the orchestrator's to disclose; it
  passed on a dispatch prompt naming the two pointers, a prefix suggestion, the
  pointer-append shape and one scope instruction (the out-of-scope line under *What
  the work is*), then one mid-task message saying the pointer had been widened to
  `bdb1aba` (named by id and subject), and no evaluative content. Everything evaluative is in the sibling.

## What the work is

Landing commits (diff them; review the paths at `main`, `bdb1aba` or later — nothing
on `main` touched the delta paths after it at the time of writing):

- `089fcdc` (2026-10-18 00:23 UTC) — record: the close declaration names every agent
  the session launched (020/420 parts 2-3). `docs/method/RECORD.md` (the agents bullet
  under *The all-clear carries its evidence*) and `docs/method/CONCURRENCY.md` (the
  close-out measurement sentence).
- `a738f85` (2026-10-18 00:27 UTC) — ccclose: add check 12, subagents finished.
  `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/ccclose.design.md`,
  `instruments/man/ccclose.1`, `instruments/README.md`.
- `4142efb` (2026-10-18 04:10 UTC) — ccclose: add --identifiers, the paste-ready
  identifiers block. The same instrument files except the README.
- `8b30ee6` (2026-10-18 04:10 UTC) — ccclose: print worktree paths under the home
  directory as ~/ in the identifiers block. `instruments/ccclose` only.
- `bdb1aba` (2026-10-18 05:06 UTC) — ccclose: a plain run ends with the identifiers
  block (210/300). `docs/method/RECORD.md` (the identifiers block's lead sentence),
  `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/man/ccclose.1`.

Read each body-free: `python3 tools/coldsweep.py --root . --commit <sha> [--path <p>]`
prints subject, stat and diff and never the message body. Plain `git show` is barred
here because it prints the body (the author's account) before the diff, and reading is
atomic (`REVIEW.md` rule 1).

**Commits on the same doctrine files that are not this delta.** Between `a738f85` and
`4142efb`, `140a190`, `1adf398`, `46320f8` and `6810b64` changed `RECORD.md` and
`CONCURRENCY.md`; they write the identifiers block's own doctrine text and are queued
pass 160/900's delta. The identifiers form here implements that text: test the code's
fidelity to it, but where a defect sits in the doctrine text itself, say so and leave
its charge to 160/900. The one exception is `bdb1aba`'s hunk in that same section of
`RECORD.md`, which is this delta.

**Later commits are out of scope.** Commits to these same files under board item
`210/290` (in flight while this brief was written, not on `main`) are not this delta
and carry their own queued pass; do not attribute them to it.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and
live behaviour. The lenses organise it; they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Check 12 against its design table.** The design note's *Subagents finished (12),
  precisely* section gives five states and the rule that combines them. Drive every
  state with a synthetic `subagents/` tree, and record which the code reaches and
  whether any input produces ✅ the table does not license.
- **What "finished" is read from.** The on-disk layout, the record shapes and the
  notification shapes the design names: are they the harness's real shapes, and were
  the fixtures derived from real transcripts or from the same reading that wrote the
  code? A shape the harness emits that the code does not read is a silent miss.
- **The doctrine bullet's claims.** `RECORD.md`'s new bullet makes a behavioural claim
  about the harness and an empirical one about past sessions. Re-drive what can be
  re-driven; mark the rest unverifiable with grounds. `CONCURRENCY.md` now names "the
  live agent list" as a measurement: what is that list, and can a session read it?
- **The identifiers form against its spec.** The seven fields, their order, the
  `none` and `by hand` rules, the commit-range rule, the board-change derivation, the
  worktree and branch reads, and the agents field — against `RECORD.md` § *The session
  log* at HEAD and the design note's §15. Since `bdb1aba` a plain run prints the block
  after its verdict: drive that path too, with `--json`, with a failing check and with
  reads that time out, and check the exit-code and field-set contracts still hold.
- **What the block carries into records.** Every field's source and what it can
  contain once pasted into a public record; the home-path rewrite and its edge cases;
  what `--json` keeps that the text form drops.
- **Mirror sites.** Every place the close declaration or `ccclose`'s check count is
  restated (skills, the session-open prompt, `TOOLBOX.md`, templates, the man page and
  `--help`): swept to match, or now claiming more or less than the tool proves.

**Non-goals:** the principal's asks that the close cover subagents and that the record
end with an identifiers block, which a plain run prints (quoted in their intent
records), the identifiers block's
doctrine text (160/900), and `210/290`'s later commits. The checks chosen, their states
and every word of the delta's own text are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that the agents directory beside a transcript is complete for the
   session; that the harness's notification records are a stable interface; that a
   live session's own running agents showing ❌ is the right answer rather than noise
   that trains sessions to ignore the line; that the identifiers form belongs in the
   close checker rather than its own tool.
2. **Correctness & quality.** Read the check-12 and identifiers code and tests whole;
   diff each build commit. Build a state table: one row per check-12 state and per
   identifiers field, with the input that reaches it and what prints.
3. **Completeness / harvest.** The design note against the code at HEAD, the man page
   and README against both, the doctrine sites in *Scope*, and any test the design
   promises that does not exist.
4. **Security & privacy** — mandatory. The tool reads every agent transcript and
   meta file beside the session's transcript and prints descriptions from them; the
   identifiers block is made to be pasted into public records; `--json` keeps absolute
   paths. Weigh each against the repo's purpose-based personal-data rule
   (`docs/build/REPO-STANDARD.md`). Never quote real transcript content in the
   verdict. `/security-review` is discharged by grounds (a landed delta; the pending
   diff is not the work) — say so, and do the code-altitude read by hand against the
   OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift invocations from `.github/workflows/ci.yml` rather than
guessing. Each line below was run once by the brief-writer and ran — the first three
both from its worktree root (at `f0d6238`, before `bdb1aba`) and from a `git archive`
export of `bdb1aba` in its scratchpad; nothing about their results is offered here.

- `node --test instruments/ccclose.test.js` (about 90 s on this machine), then the
  whole instruments suite once as CI runs it (`node --test instruments/*.test.js`),
  foreground, with a long timeout
- `mandoc -T lint -W style instruments/man/ccclose.1`; `node instruments/ccclose
  --help` by path
- live runs by path, never by bare name: throwaway git repos, a fake `HOME`, synthetic
  transcripts and synthetic `subagents/` trees in your scratchpad, `gh` stubbed through
  `CCCLOSE_GH`; drive each check-12 state and each identifiers field
- one run of `--identifiers` and of the full check against your own session in a
  scratch clone of this repo, after the throwaway runs; never against the shared
  checkout or another repo, and never paste its output into the verdict unredacted
- mutation, in a scratch clone: flip one load-bearing condition per check-12 state and
  per identifiers field, and record which tests fail
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and
  the hook plane as `.githooks/pre-commit` invokes it)

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is
  fine. Probes, fixtures, mutated copies and older checkouts go in a private clone under
  your session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: check `uptime` first, and run the
  instruments suite at most once whole, in the foreground. Never point a scanner or
  ccclose at any other repo on the machine. Never run an installed tool by bare name
  from `PATH`; instruments are symlinked onto it from another checkout.
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
`docs/sessions/`, every prior verdict in `docs/reviews/` (one is on this same tool),
the queue pointer, this brief's sibling
`docs/reviews/2026-10-18-0506-close-covers-subagents-cold.deferred.md`, the landing
commits' message bodies, and the intent and commissioning items:

- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/420-the-close-declaration-does-not-cover-subagents.md`
- the whole of `docs/roadmap/210-instruments-open-features/`, which holds the
  identifiers form's commissioning items (210/280, 210/300) and the in-flight 210/290; barred as
  a directory so that no item filename is put in front of you here

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/920-rule-4-cold-pass-queued-close-covers-subagents.md
--also-exclude docs/reviews/2026-10-18-0506-close-covers-subagents-cold.deferred.md
--also-exclude
docs/roadmap/020-policy-as-code-programme-five-tracks-mik/420-the-close-declaration-does-not-cover-subagents.md
--also-exclude docs/roadmap/210-instruments-open-features <pattern>`;
`--include-barred` only with disclosure in the verdict. The generated index
`docs/ROADMAP.md` repeats item titles; read it no further than your onramp needs, and
disclose it if you do. Reading the delta is never barred; the design note and the
doctrine hunks are part of the delta.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append
your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, what you read), per-lens answers, the standing checklist V1–V7 each
answered or discharged with grounds, the state table, findings with stable IDs (prefix
`CV`: `CV1`, `CV2`, …) and severities (MAJOR / MODERATE / minor / note), an overall
PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger, and a follow-up
checklist. Then STOP and commit phase 1 unrevised before opening the sibling. Edit no
other file.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding
notes against the seeded questions, the intent records and the prior verdict on this
tool, any finding formed at reconcile marked as such, and the overall line restated.
Never revise phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on doctrine, and on a tool that encodes it, are the principal's to decide
(rule 3): record all, apply nothing; counsel per finding is welcome, labelled and kept
beneath it.
