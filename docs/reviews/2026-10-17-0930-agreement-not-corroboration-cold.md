# Cold pass — agreement is not corroboration, minted in EVIDENCE

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/780-rule-4-cold-pass-queued-agreement-is-not-corroboration.md`.
**Why it earns a review:** it adds a rule to the evidence ladder every session climbs — what
counts as the *independent corroboration* rung — and promotes it to doctrine under the >2
promotion rule, so every repo that inherits `EVIDENCE.md` inherits the new test.

## Spawn provenance

- **Author of the work under review:** the 2026-10-16 queue run whose intent record is the
  session file dated 2026-10-16 07:03 UTC that the pointer names (not opened by the
  brief-writer). The landing commit's trailer names an Opus model; the run's orchestrator wrote
  this delta itself, not through a worker.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-17 by the
  Mike-opened Fable review session working in the worktree `atelier-review-1017`, on Mike's
  2026-10-16 answer that a fresh Opus session writes these briefs. Neither it nor its
  orchestrator authored the delta or was started or instructed by its author. **Off-tier for
  review, disclosed: it forms no finding and writes no severity**, and stops after this brief and
  its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, passing rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, the off-tier conditions of rule 4 apply and
  are disclosed in the claim, the pointer and the verdict. The reviewer repeats its own provenance
  in the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing): the four queue
  pointers it was assigned (160/780–810; refs-only, no claim line yet) and, as a shape example,
  the 160/500 pointer with its claim line; the delta lists of eight neighbouring pointers (160/700,
  720, 730, 760, 820, 830, 850, 860), read to find overlaps; the landing commit's subject,
  `--stat`, diff and **full message body** (the author's account); `docs/method/REVIEW.md` rules
  1–4; three user-local templates — the ask halves of the 2026-10-16 expected-toolbox and
  scanner-rule-gates briefs, and the whole expected-toolbox sibling, seeded questions included
  (another pass's framing, on other surfaces); HEAD text of the delta and of the passages named in
  *Scope*; one or two grep-hit lines from the commissioning item and from `115/060`; filename-level
  greps of `docs/reviews/` (no file there opened); and its harness-loaded memory index and
  instruction files. It did not open the intent record, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or any file under `docs/reviews/`. Its orchestrator passed it an
  instruction set (pointers, templates, staging rules, prefixes already taken) and no evaluative
  content about the delta; what the orchestrator read is its own to disclose in its claim.
  Everything evaluative the brief-writer formed is in the sibling.

## What the work is

Landing commit (diff it on the delta path; review the path at HEAD, `8acfff1` or later):

- `b572594` (2026-10-16 07:16 UTC) — method: mint "agreement is not corroboration" in EVIDENCE
  (200/090)

Delta path (the pointer's own scope): `docs/method/EVIDENCE.md` §13, the one paragraph the commit
adds, headed **A second voice is not a second angle unless it opened the source** (21 added
lines; at HEAD it sits between the ladder's closing paragraph and *Handing the question to the
principal*). No later commit touches `EVIDENCE.md`; confirm that.

The commit also touched board items, the session index, the intent record and another item's
held draft; those are not the delta.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs and live behaviour. The
lenses organise it; they do not bound it. Non-goals are the only narrowing and are themselves
reviewable.

Probe, at least:

- **What the rung now means.** Read §13's ladder, its *independent corroboration* rung and §4
  ("its own corroboration") against the new paragraph. Build a case table: a second party that
  opened the *same* artefact as the first; one that opened a different artefact derived from the
  first; a tool's output; the principal agreeing; a cold reviewer agreeing with a prior verdict;
  a subagent re-reading text its parent quoted to it; a party that re-ran a probe rather than
  opening a file. For each, what does the paragraph say, and does a reader reach one answer?
- **The grounding, re-driven.** The paragraph cites three instances and where each is kept:
  `CONCURRENCY.md` § *Re-run, don't reason*, the board item `115/060`, and `CONCURRENCY.md`
  § *Orchestrated queue runs*. Open each cited surface and say whether it records what the
  paragraph says it records. (The fourth citation, `200/090`, is the commissioning item, barred
  until phase 2 — check it at reconcile.)
- **The promotion rule, as written.** `PROPAGATION.md` § *When a rule keeps breaking* states the
  >2 promotion rule. Does this minting meet that rule as the rule is worded, and is the rung it
  chose (a doctrine paragraph) the one that section's ladder would pick?
- **One fact, one home.** `CONCURRENCY.md` states the same rule at two places (its *Re-run,
  don't reason* bullets and its *Orchestrated queue runs* account). Which is now the home, does
  each copy point to it, and do the copies still agree in wording and reach (`EVIDENCE` §9,
  `PROPAGATION.md` § *One statement, stamped copies*)?
- **The sibling rule left behind.** The paragraph names a second rule and declines to promote it.
  Is that statement accurate, and is a doctrine paragraph the place for it?
- **Where it reaches.** Which surfaces children and the plugin's skills read restate the evidence
  ladder or its corroboration rung, and do any now disagree?

**Non-goals:** the decision to promote this rule at all (the >2 rule's threshold itself). Whether
the minting meets that rule, the wording, its placement and its consistency are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether
   "which artefact did it open" is the right test for independence, and whether a rule about who
   opened what can be followed by a reader who cannot see the other party's reads.
2. **Correctness & quality.** Diff `b572594` on `docs/method/EVIDENCE.md`. Check every
   cross-reference in the new paragraph resolves to a passage that says what is claimed. Record
   the case table from *Scope*.
3. **Completeness / harvest.** Every surface that states the corroboration rung or the rule:
   `EVIDENCE.md` §§2, 4, 13; the two `CONCURRENCY.md` sites; `REVIEW.md`'s independence rules;
   `README.md` and `docs/method/README.md` summaries; the plugin's skills; `CHANGELOG.md`. Is a
   changelog entry or a stamp owed?
4. **Security & privacy** — mandatory. The paragraph cites real episodes in a public repo: check
   it names no private repo, person, host or account beyond the recorded exceptions, and that the
   cited board items carry nothing that should not be public. Describe, never quote, anything
   sensitive. `/security-review` is discharged by grounds (a landed prose delta).

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/linkscan.py --root . .` and `python3 tools/pathscan.py --warn --root . docs` —
  the paragraph's links and backtick paths, exit codes read explicitly
- `python3 tools/leakscan.py --root . .`, exit code read explicitly
- `python3 tools/wrapscan.py --root . docs` and `python3 tools/spellscan.py --root . docs`
- `git log --oneline b572594..HEAD -- docs/method/EVIDENCE.md` — empty, or each commit named
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and
  `--plane hook`)

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-16-*` or `docs/reviews/2026-10-17-*` file — it
  is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Older checkouts and
  scratch trees go in a private clone under your session scratchpad, named by your prefix.
- One heavy process at a time: the full Python suite at most once, in the foreground; never point
  a scanner at another repo on the machine.
- `/security-review` reads the session's pending diff, not this delta. Discharge it by grounds and
  do the code-altitude read by hand against the OWASP catalogue, or keep the tree clean when you
  spawn it — never with this brief or its sibling dirty.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never quote
  a secret, a placeholder token, an email address or a personal detail — this repo is PUBLIC.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/780-rule-4-cold-pass-queued-agreement-is-not-corroboration.md`,
the sibling `docs/reviews/2026-10-17-0930-agreement-not-corroboration-cold.deferred.md`, the
landing commit's message body (the author's account; read subject, stat and diff only), and the
commissioning item:

- `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/090-two-corroboration-failures-worth-minting-from.md`

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/780-rule-4-cold-pass-queued-agreement-is-not-corroboration.md
--also-exclude docs/reviews/2026-10-17-0930-agreement-not-corroboration-cold.deferred.md
--also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/090-two-corroboration-failures-worth-minting-from.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `EC`: `EC1`, `EC2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results) and a follow-up checklist. Then STOP and commit this file
before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.
