# Cold pass — per-rule pre-filter gates in leakscan and secretscan

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/720-rule-4-cold-pass-queued-scanner-gates.md`.
**Why it earns a review:** the two blocking guards that keep personal data and
credentials out of a public repo, and out of every child, now skip a rule's regex
on any line its gate rejects. A gate that is not strictly necessary is a silent
false negative on the house's most important boundary, and the change was
justified as invisible.

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
  `--stat`, diff **and message body** (the author's own account); the subjects
  and `--stat` of later commits on the same files; `REVIEW.md` rules 1–4, the four
  lenses, the checklist and the lifecycle; the ask halves of two 2026-10-04 briefs
  as templates; `docs/reviews/` filenames and filename-level greps (no prior
  verdict opened); the names, not contents, of the commissioning board items; and
  its harness-loaded memory index (one-line notes, some about these guards'
  history). Its orchestrator read the `docs/SESSIONS.md` index tail through
  2026-10-16 (including the authoring run's one-paragraph summary) and the
  2026-10-16 session record's close section, and passed on no evaluative content
  beyond the pointer list and a one-line note that these guard files changed
  later. Everything evaluative is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD):

- `c938b58` (2026-10-05 12:53 UTC) — leakscan, secretscan: gate each rule behind
  a provably necessary cheap test; landed in merge `e7575f7` (2026-10-05 12:54 UTC)

Delta paths: `tools/leakscan.py` (`GATES`, `_active_rules`, the gate checks in
`_shadow_spans` and `scan_lines`, the marker-literal pre-check),
`tools/secretscan.py` (`NAMED_GATES`, `_ASSIGNED_TAIL_RX`, `HIGH_ENTROPY_MIN_LEN`,
the entropy-first reordering, the early `return []`), and their tests
`tools/test_leakscan.py` and `tools/test_secretscan.py`.

**Later commits on the same files — not this delta; do not attribute them to
it.** A diff of the two scanners from `e7575f7` to HEAD shows no changed line
that mentions a gate; confirm that, then review the gates at HEAD.

- `ffabef3` (2026-10-05) — shared exit and report lines (its own pass, 160/730)
- `ded8d32` (2026-10-05) — a namespaced finding ID on every line (160/750)
- `b609b4b` (2026-10-05) — test files run every class on a direct run
- `4dfaf8d` (2026-10-05) — staged-plane guards read git-quoted paths (160/760)
- `39a74b9` (2026-10-16) — read the staged diff by its structure, not by how a
  line looks (115/280); a shared staged-diff reader in `tools/report.py`
- `f4afb7a` (2026-10-16) — leakscan reports a staged finding at its real line

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

For **every** gated rule in both tables, derive from the rule's regex at HEAD —
its flags, character classes, alternations, optional parts and lookarounds — the
weakest condition every match must satisfy, and compare it with the gate. Do this
from the pattern, independently of the delta's tests (`EVIDENCE.md` § 15 is
the reason). Pay attention to: flags set at compile time rather than inline
(`re.IGNORECASE`, `re.ASCII`, `re.UNICODE` digit and whitespace classes, which
match non-ASCII digits, dashes and spaces that `str.count("-")` and literal
checks do not); every alternative of a multi-branch pattern (cloud key prefixes,
token families, address suffixes, IPv6 forms, phone shapes); patterns built from
a vocabulary at import time; rules a gate dictionary names that no longer exist,
and rules that exist but have no gate. Then the structural changes: is
`ALLOW_MARKER in line` necessary for the marker regex on every spelling the
shared grammar accepts (case, spacing)? Does `_shadow_spans` skipping a shadower
whose gate fails ever drop a span that suppressed a finding before? Is secretscan's
`continue` after the entropy probe still the last step of the line loop at HEAD,
and does the early `return []` skip any tally, stale-marker or advisory
accounting the old path ran? Whether leakscan's machine-local term list and the
path-name scan pass through gates, and should. **Non-goals:** levers 1–3 of the
commissioning item (binary skip, size threshold, one combined alternation) — but
the recorded reason for not building lever 3 is itself reviewable.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   The central one: that every gate is a *necessary* condition, proven from the
   pattern text. Others: that the speed gain was worth any residual risk on a
   blocking guard; that byte-identical output on two trees plus a generated fuzz
   corpus proves equivalence; that a gate keyed by rule name fails open when a
   rule is renamed.
2. **Correctness & quality.** Read both gate blocks and their tests whole; diff
   `c938b58`. Build a per-rule table: pattern summary, derived necessary
   condition, gate, verdict, and a counter-example line wherever they differ.
   Check whether the tests' near-miss corpora were derived from the regex or from
   the same reading that wrote the gates.
3. **Completeness / harvest.** `tools/README.md`'s description of both guards;
   `docs/method/GUARDS.md`'s claims about what the guards catch; any other
   scanner that copies one of these patterns (a divergent copy of a gated rule
   is a place a gate can be missing or wrong).
4. **Security & privacy** — mandatory. This lens is the subject: hunt the line a
   gate rejects that the rule would match. Build counter-examples from synthetic
   values only — never a real credential, term-list entry or personal detail, and
   never quote one in the verdict. Also check regex cost on adversarial long lines
   now that gates change which regexes run. `/security-review` is discharged by
   grounds (a landed delta; the pending diff is not the work) — say so, and deliver
   the code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_leakscan tools.test_secretscan -v`;
  `python3 tools/leakscan.py --selftest` and `python3 tools/secretscan.py
  --selftest`
- the equivalence claim, re-driven: in a scratch clone, run each scanner at HEAD
  with its gate table emptied (monkeypatched, not edited in the worktree) and
  with it intact, over the repo tree and over your own adversarial corpus;
  compare stdout, stderr and exit code
- the old-versus-new claim at landing: `c938b58^` against `c938b58` on the same
  corpus, so a difference introduced later is not charged to this delta
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Probes, monkeypatched runs and older checkouts go in a private
  clone under your session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground; a differential corpus sized to finish in minutes, under `nice`.
  Never point a scanner at any other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta, or keep the tree clean whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — this repo is PUBLIC; describe and locate instead. Counter-example
  lines in the verdict are described by shape, not pasted, where they would trip
  the guards on commit.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-16-1551-scanner-rule-gates-cold.deferred.md`,
and the commissioning item `130` in
`docs/roadmap/110-estate-duplication-exception-audit-mike/`, and item `280` in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/` (a later finding on a
neighbouring surface).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/720-rule-4-cold-pass-queued-scanner-gates.md
--also-exclude docs/reviews/2026-10-16-1551-scanner-rule-gates-cold.deferred.md
--also-exclude docs/roadmap/110-estate-duplication-exception-audit-mike
--also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, the per-rule gate table,
findings with stable IDs (prefix `GT`: `GT1`, `GT2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with
counts, a re-run ledger, and a follow-up checklist. Then STOP and commit phase 1
unrevised before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a
guard is doctrine by function): record all, apply nothing; counsel per finding is
welcome, labelled and kept beneath it.
