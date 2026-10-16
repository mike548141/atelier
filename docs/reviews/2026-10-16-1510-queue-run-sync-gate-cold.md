# Cold pass — the queue-run skill's sync step gains the status-first gate

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/520-rule-4-cold-pass-queued-queue-run-sync-gate.md`.
**Why it earns a review:** the skill is the delivery vehicle every queue run loads; its first act
on a shared checkout decides whether a peer's uncommitted work is preserved or shelved. A small
wording change here is executed verbatim by every orchestrator that loads it.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run that landed the commit below; its
  intent record is the session file dated 2026-10-03 0144 UTC that the pointer names (not opened
  by the brief-writer). The commit's trailer names an Opus model.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by the Mike-opened
  Opus queue-run session `abe96d8d` on 2026-10-16, on Mike's answer of that date that a fresh Opus
  session writes these briefs. Neither it nor its orchestrator authored the delta or was started
  or instructed by its author. **Off-tier for review, disclosed: it forms no finding and writes no
  severity**, and stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, passing rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, the off-tier conditions of rule 4 apply and
  are disclosed in the claim, the pointer and the verdict. The reviewer repeats its own provenance
  in the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing): the seven queue
  pointers it was assigned (160/500, 520–570; refs-only, each ending in the orchestrator's claim
  line); the seven landing commits' subjects, `--stat` lists, full message bodies (the author's
  account) and diffs on the delta paths; `docs/method/REVIEW.md` in full; the ask halves of two
  2026-10-04 briefs as templates; HEAD text of the neighbouring surfaces named in *Scope*; single
  grep-hit lines from unrelated board items and old `CHANGELOG.md` entries; filenames (not
  contents) of prior verdicts; and its own cross-session memory index. It did not open the intent
  record, the commissioning board item, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or any prior verdict. Its orchestrator read the `docs/SESSIONS.md` index
  tail (entries through 2026-10-16, including the authoring run's one-paragraph summary) and the
  2026-10-16 session record's close section, and passed no evaluative content beyond the pointer
  list. Everything evaluative the brief-writer formed is in the sibling.

## What the work is

Landing commit (diff it on the delta path; review at HEAD, `2e2da81` or later):

- `d6a3faf` (2026-10-03) — skills: queue-run reads git status before it pulls (200/100 C1)

Delta path: `skills/queue-run/SKILL.md`, step 2 (*Sync + onramp*). A later commit, `b218f1e`,
edited step 6 of the same file (another pass's subject); check it did not move step 2.

## Scope

Widest the work admits; the lenses organise it, they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Parent agreement, term by term.** Step 2 against `docs/method/CONCURRENCY.md` § *Integration
  hygiene* (the opening bookend's two gates) and § *The trigger*, the floor region in
  `docs/method/PROPAGATION.md`, its stamped copy in `docs/build/templates/CLAUDE.md`, and this
  repo's own `CLAUDE.md` read order step 1. Compare: what counts as "yours", what "stop" means,
  "no upstream" against "no remote", and the order of status, pull and onramp.
- **The skill's own contract.** Its header comment calls it a stamped copy that may compress its
  parent, never contradict it, and names restating standing rules as the drift it exists to
  avoid. Judge step 2 against that header, and check whether any guard watches this file.
- **An orchestrator's cases.** Walk the step for: a primary checkout dirty with a peer's work when
  the run must claim on `main` from the primary first (CONCURRENCY § *Claiming work*); a run
  resumed after a context cut with its own uncommitted work; worker output left in the primary;
  only untracked files; a detached HEAD; an upstream that is set but unreachable; a branch with a
  remote but no upstream. For each: what does the run do next, and is that written anywhere?
- **After "move to a worktree".** Which base does the new worktree take if the pull never ran?
- **Distribution.** The skill ships to other repos; say how a child receives this change.

**Non-goal:** the status-first rule itself in CONCURRENCY (already doctrine). Its restatement and
fit in the skill are the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether a
   skill step that restates its parent was the right fix for a skill step that contradicted it.
2. **Correctness & quality.** Diff `d6a3faf`. Run the case table above and record it.
3. **Completeness / harvest.** Every other place that tells a session to pull at start: the
   `session-onramp` skill, the session-open prompt under `docs/method/session-open/`, `README.md`,
   the plugin bundle. Which still carry the ungated bookend?
4. **Security & privacy** — mandatory. The hazard is integrity: a peer's work shelved onto a
   shared stash stack, popped by someone else, or absorbed into a commit. Say whether the new step
   closes each path. No code surface: `/security-review` is discharged by grounds.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- the step itself, driven in a private scratch clone with a second linked worktree holding
  uncommitted edits: run the commands the step names in its order and record what happens
- `python3 tools/stampscan.py --warn --root . .` and `python3 tools/pathscan.py --root . .`
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`)

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-16-1510-*` file — it is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Every probe that
  stashes, pulls or checks out runs in a private clone under your session scratchpad, named by
  your prefix — never against a live checkout.
- One heavy process at a time: the full Python suite at most once, in the foreground; never point
  a scanner at another repo on the machine.
- `/security-review` reads the session's pending diff, not this delta. Discharge it by grounds, or
  keep the tree clean when you spawn it — never with this brief or its sibling dirty.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never quote
  a secret, a placeholder token, an email address or a personal detail — this repo is PUBLIC.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/520-rule-4-cold-pass-queued-queue-run-sync-gate.md`, the
sibling `docs/reviews/2026-10-16-1510-queue-run-sync-gate-cold.deferred.md`, the landing commit's
message body (the author's account; read subject, stat and diff only), and the commissioning
item
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/520-rule-4-cold-pass-queued-queue-run-sync-gate.md
--also-exclude docs/reviews/2026-10-16-1510-queue-run-sync-gate-cold.deferred.md --also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `SY`: `SY1`, `SY2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results) and a follow-up checklist. Then STOP and commit this file
before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.
