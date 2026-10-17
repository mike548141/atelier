# Cold pass — ADR 0008's 2026-10-16 boundary amendment and the ruleset bypass removal

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4, with a live platform read.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/820-rule-4-cold-pass-queued-adr-0008-boundary-amendment.md`.
**Why it earns a review:** it restates, in an ADR, the strength of the one control that stands
between atelier's `main` and every child's CI, and it pairs that text with a change made on the
platform rather than in git — a change no diff shows and no scanner re-reads.

## Spawn provenance

- **Author of the work under review:** the 2026-10-16 queue run that landed the commit below and
  made the platform change; its intent record is the session file dated 2026-10-16 0703 UTC that
  the pointer names (not opened by the brief-writer). The commit's trailer names an Opus model.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-17 by the
  Mike-opened Fable review session working in worktree `atelier-review-1017`, on Mike's 2026-10-16
  answer that a fresh Opus session writes these briefs. Neither it nor its orchestrator authored
  the delta or was started or instructed by its author. **Off-tier for review, disclosed: it forms
  no finding and writes no severity**, and stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, passing rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, the off-tier conditions of rule 4 apply and
  are disclosed in the claim, the pointer and the verdict. The reviewer repeats its own provenance
  in the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing): the four queue
  pointers it was assigned (160/820–850; refs-only), and 160/500 in full as the shape of a
  pointer's append line (its claim and its verdict summary for another pass included); the first
  lines of pointers 160/790, 160/800 and 160/860; the landing commit's subject, `--stat`, full
  message body (the author's account, with a principal quote) and diff on the delta path; the
  ADR's section headings and grep-hit lines of its 2026-08-23 amendment; single grep-hit lines
  from the commissioning board items named under *Deferred reading* — including one line from
  160/090 recording how a finding there was answered and which of its findings stand — and from
  `tools/floorfleet.py`, `CHANGELOG.md` and 115/180, met while sweeping for mirror sites; the
  `--help` text of `floorfleet` and `signscan`; filenames (not contents) of prior verdicts; the
  filenames and one append line of this run's other brief-writer (not its briefs); and its own
  harness-loaded memory index. It made no platform read. It did not open the intent record,
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, `docs/method/REVIEW.md` or any
  prior verdict. What its orchestrator read is the orchestrator's to disclose; it passed the
  brief-writer an instruction file, three templates (two 2026-10-16 briefs and a sibling) and a
  list of taken prefixes, and no evaluative content. Everything evaluative the brief-writer
  formed is in the sibling.

## What the work is

Landing commit (diff it on the delta path; review the path at HEAD, `b50db0c` or later):

- `93d3a14` (2026-10-16 11:46 UTC) — decisions: ADR 0008's boundary at its true strength; main's
  admin bypass removed (140/020)

Delta, the pointer's own list:

- `docs/decisions/0008-enforcement-is-called-not-copied.md` — the appended section *Amended
  2026-10-16 — the boundary as it now stands: three legs, three strengths*; read the whole ADR at
  HEAD, because the section supersedes the 2026-08-23 amendment above it and rests on the
  *Consequences* clause.
- **The platform state:** the `bypass_actors` list of the `main` ruleset the section names, set to
  empty through the API on 2026-10-16. There is no diff for this. Read it live (re-run list), and
  if the platform exposes the ruleset's change history, read that too.

The commit also touched board items, the generated index and the intent record; those are not
the delta. No later commit touches the ADR (`git log 93d3a14..HEAD -- docs/decisions/0008*` is
empty at the time of writing); confirm at your HEAD.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs and live behaviour. The
lenses organise it; they do not bound it. Non-goals are the only narrowing and are themselves
reviewable.

Probe, at least:

- **Each factual claim against the live platform.** Every statement the section makes about the
  ruleset — its id, `enforcement`, `created_at`, each rule type, `bypass_actors`, the effective
  rules on `main` — and about commit verification ("30 of the 30 latest"), re-read live and
  recorded with the read's own time. Say which claims were true at landing, which are true at
  your HEAD, and which cannot be re-driven.
- **The three legs and their stated strengths.** For each leg (branch protection, signed commits,
  review on the registry), what the section says enforces it, and whether that enforcer exists as
  described. Name what "in force for every account" means when the owner can edit the ruleset.
- **Every path that writes `main` after the change.** Direct pushes from a session, a PR merged
  through the platform, a child's hand-up PR, any workflow or bot that commits, a revert, a
  release. For each, whether a `required_signatures` rule with no bypass actor lets it through,
  and how it would fail if not. The section claims direct-to-`main` working is untouched; test it.
- **The machine check.** The section describes what `floorfleet`'s boundary row reads, what makes
  it red, unknown or green, and that it does not read the bypass list. Check each against
  `tools/floorfleet.py` and its tests at HEAD.
- **Supersession.** How the section relates to the 2026-08-23 amendment it supersedes and to the
  *Consequences* clause: what a reader landing on the ADR now believes, in order, and whether any
  other surface still states the superseded text.
- **The principal's words.** Separate each verbatim quote or attributed ruling from the wording
  around it; say where the surrounding text narrows, widens or re-reads what is attributed.

**Non-goals:** whether the principal should have chosen to drop the bypass (recorded as his
answer). How the change is recorded, what it claims, the platform's actual state and the residual
exposure are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether an
   ADR amendment is the right carrier for a statement of live platform state, how that statement
   is kept true after landing, and what an amendment that supersedes an amendment does to the
   ADR's readability.
2. **Correctness & quality.** Diff `93d3a14` on the ADR. Check every API path, field name, rule
   type, date and count in the section against a live read and against the code it names. Check
   every cross-reference (board keys, finding IDs, `REVIEW.md` rule 4) resolves to a passage that
   says what is claimed.
3. **Completeness / harvest.** Every surface still stating the old boundary — the ADR's own
   earlier text, `tools/floorfleet.py`'s docstring and comments, `docs/method/SIGNING.md`,
   `docs/method/GUARDS.md`, `docs/method/AUTONOMY.md`'s direct-to-`main` working, the board's
   section head for the AP1 control, `CHANGELOG.md`. Is a changelog entry owed for a platform
   change?
4. **Security & privacy** — mandatory, and the centre of this pass. Model the attacker the
   section names (holder of the owner's credentials) and any it does not: a compromised session
   with push rights, a compromised signing key, a CI token, a malicious hand-up PR. For each,
   what stops arbitrary code reaching `main` and then every child, and whether the section states
   that honestly. Say what is now visible after the fact and to whom. Describe, never quote,
   anything sensitive. `/security-review` is discharged by grounds (a landed prose delta plus a
   platform setting).

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing. Every platform call is a read: never a write
method, never an edit to the ruleset, never a test push to `main`.

- `gh api repos/mike548141/atelier/rulesets/<id>` and `gh api
  repos/mike548141/atelier/rules/branches/main`, recorded with the read time
- the ruleset's history, if the platform offers a read-only endpoint for it
- commit verification over a window you choose and name (the section's "30 latest", and the
  window since the change), from the platform's commit records
- `python3 tools/floorfleet.py --selftest`, `python3 tools/signscan.py --selftest`, and
  `python3 -m unittest discover -s tools -p 'test_floorfleet.py' -v`; the parent boundary row
  live only if you can scope `floorfleet` to atelier alone (`--help` first; by default it walks
  every repo beside the checkout, which this run must not do)
- `python3 tools/linkscan.py --root . .` and `python3 tools/leakscan.py --root . .`, exit codes
  read explicitly
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`)

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-17-*` brief — it is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Older checkouts and
  scratch trees go in a private clone under your session scratchpad, named by your prefix.
- No platform write of any kind. A probe that would need one is described in the verdict as a
  probe owed, for the principal to authorise.
- One heavy process at a time: the full Python suite at most once, in the foreground; never point
  a scanner at another repo on the machine.
- `/security-review` reads the session's pending diff, not this delta. Discharge it by grounds and
  do the code-altitude read by hand against the OWASP catalogue, or keep the tree clean when you
  spawn it — never with this brief or its sibling dirty.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never quote
  a secret, a token, an email address or a personal detail — this repo is PUBLIC.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/820-rule-4-cold-pass-queued-adr-0008-boundary-amendment.md`,
the sibling `docs/reviews/2026-10-17-0955-adr-0008-boundary-amendment-cold.deferred.md`, the
landing commit's message body (the author's account; read subject, stat and diff only), and:

- `docs/roadmap/140-ap1-ruled-and-half-applied-the-main-cont/` (the commissioning item and its
  section)
- `docs/roadmap/160-doctrine-review-owed/090-rule-4-review-queued-tier-fable-pass-type-code.md`

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/820-rule-4-cold-pass-queued-adr-0008-boundary-amendment.md
--also-exclude docs/reviews/2026-10-17-0955-adr-0008-boundary-amendment-cold.deferred.md
--also-exclude docs/roadmap/140-ap1-ruled-and-half-applied-the-main-cont --also-exclude
docs/roadmap/160-doctrine-review-owed/090-rule-4-review-queued-tier-fable-pass-type-code.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `BY`: `BY1`, `BY2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands, read times and results) and a follow-up checklist. Then STOP and commit
this file before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.
