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

---

# Verdict — 2026-10-17 UTC

## Provenance (repeated, V7)

- **Reviewer:** a fresh `claude-fable-5-1` subagent (Fable tier, the principal-named
  review tier — checked at claim), spawned 2026-10-17 UTC by a Fable orchestrator
  through a standing prompt file for prefix `GT`. The orchestrator authored none of
  the delta and none of this brief, and held the `.deferred.md` sibling outside this
  reviewer's reach. Neither the delta's author (the 2026-10-05 queue run) nor the
  brief-writer started or instructed this session: rule 4's criterion passes.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`,
  HEAD `8acfff1` (confirmed an ancestor-or-equal of the brief's floor). Read-only
  git only; probes and the pre-/post-landing extractions ran in a private clone
  under this session's scratchpad, in a folder named `GT`.
- **Interruption, disclosed:** the pass was cut off by an API rate limit on
  2026-10-17 UTC after the unit tests and selftests had passed, and resumed in the
  same agent transcript; the differential runs and everything after them ran on
  resumption. No phase-1 text was written before the interruption.
- **What was read:** this brief; `docs/method/REVIEW.md` whole; the landing diff
  `c938b58^..c938b58` for the four delta files (diff only — the commit's message
  body stayed closed); both scanners and both test modules at HEAD;
  `tools/allowmarker.py`; `docs/method/GUARDS.md`; `docs/method/EVIDENCE.md` §15;
  `tools/README.md` §§ leakscan/secretscan; `CHANGELOG.md` lines 120–165;
  `.leakscanignore`, `.secretscanignore`, `.atelier-floor.json`,
  `.githooks/pre-commit`, `.github/workflows/ci.yml`, a grep of `tools/floor.py`;
  and, from the cold sweep, one table row of board item `300/020` and one paragraph
  of `260/120` (neither barred). The barred set — prior verdicts, `SESSIONS.md`,
  `docs/sessions/`, `ROADMAP-DONE.md`, the queue pointer, the sibling, items
  `110/130` and `115/280`, the landing commit's message body — was not opened.
- **Sweep:** `tools/coldsweep.py` with the brief's four `--also-exclude` paths, no
  `--include-barred` (444 files barred, 593 searched).
- **Exposure, disclosed:** the CI-plane floor run printed the 23 advisory findings'
  `path:line` locations (fixture files; no values). A 1 MiB cost probe overran its
  600 s budget, was moved to the background by the harness and stopped by this
  reviewer within about a minute; no other heavy process was running at the time.
- **`/security-review`:** discharged by grounds — the delta landed 2026-10-05, and
  this session's pending diff is other reviewers' drafts, so the scanner cannot be
  aimed at the work. The code-altitude read was done by hand (lens 4).

## Lens 1 — approach and assumptions

Load-bearing assumptions, named first and then tested:

1. **Every gate is a necessary condition, provable from the pattern text.** Tested
   rule by rule from the regex (table below), independently of the delta's tests,
   and then by three differential runs (gated vs ungated at HEAD; pre- vs
   post-landing; gated vs ungated at the landing commit) over the repo tree and a
   20,181-line corpus derived from every alternative of every gated rule. **Holds
   at HEAD** for all 15 leakscan gates, all 16 secretscan named gates, the assigned
   tail gate, the 32-character entropy floor and both marker literal pre-checks.
2. **The speed gain was worth any residual risk on a blocking guard.** The risk
   that matters is not a wrong gate today but a gate that goes stale when its rule
   widens — and that risk is carried by a hand-kept corpus, not by structure
   (GT2). Accepting the gates as landed is reasonable; the maintenance contract is
   under-built.
3. **Byte-identical output on two trees plus a fuzz corpus proves equivalence.**
   It proves equivalence over the inputs used. The regex derivation is the proof;
   the fuzz is corroboration. This pass did the derivation and re-drove the fuzz
   with an independent corpus (Unicode digits and whitespace that `\d`/`\s`
   accept, full-width look-alike separators the literals reject, boundary lengths,
   every marker spelling, overlapping MAC/IPv6 spans, every `--disable` shape the
   tests use plus two more). All identical.
4. **A gate keyed by rule name fails open when a rule is renamed.** True in the
   weak sense: `test_every_gate_names_a_real_rule` fails the suite on a stale name,
   so a rename is caught, not silently ungated. The failure mode that is *not*
   caught is a rule whose regex widens under an unchanged name (GT2).
5. **Lever 3 (one combined alternation) is rightly not built.** Verified: rules
   overlap on one span (a MAC is a valid IPv6 shape and is shadowed by D5; a
   payment card and an IRD number share digit runs) and carry per-rule
   validators, so a single leftmost-match alternation cannot reproduce rule-ordered
   per-rule findings. The recorded reason is sound.
6. **Unstated:** the gates change which regexes run, so they change the scanner's
   worst case. They make it *better* on lines that fail a gate and leave it
   *unchanged* on lines that pass one — and three pre-existing regexes are
   quadratic on long lines (GT1). The delta did not create that; it did not name
   it either, and its speed claim reads as if the worst case had moved.

## Lens 2 — correctness and quality

Both gate blocks and their tests read whole; `c938b58` diffed. Later commits on
the same files (`ffabef3`, `ded8d32`, `b609b4b`, `4dfaf8d`, `39a74b9`, `f4afb7a`)
changed no line mentioning a gate, confirmed by grepping the `e7575f7..HEAD` diff
of both scanners; the gates were reviewed at HEAD.

### Per-rule gate table (derived from the regex at HEAD)

Flags: no leakscan structural rule or secretscan named rule carries `re.IGNORECASE`
except the two key-context rules (`(?i)` inline), whose gates test only the
letter-free tail, so case folding (including the Kelvin sign and long s) cannot
reach them. All patterns are `str` patterns with Unicode `\d`/`\s`; every gate that
uses `\d` or `\s` is a `str` regex with the same classes, and every gate that uses
`str.count`/`in` tests a literal the rule also spells literally.

| Rule (leakscan) | Weakest condition every match satisfies | Gate | Verdict |
|---|---|---|---|
| private-key-header | ends in the literal `PRIVATE KEY-----` | that literal `in` | necessary |
| aws-access-key-id | starts with the 4-letter prefix | prefix `in` | necessary |
| jwt | contains `.eyJ` (second segment lead-in) | `.eyJ` `in` | necessary |
| email | contains `@` | `@` `in` | necessary |
| pii-key-context | tail `[:=]\s*["']?` + 2 value chars | `_PII_TAIL_RX` (same classes) | necessary |
| payment-card | 13+ digits, or `\d{4}` groups | `\d{4}` search | necessary |
| iban | match length ≥ 2+2+11 = 15 | `len(line) >= 15` | necessary; near no-op |
| mac-address | five `[:-]` separators | `count(":")+count("-") >= 5` | necessary |
| ipv4 | three literal dots | `count(".") >= 3` | necessary |
| ipv6 | each of 4 alternatives has ≥ 2 colons | `count(":") >= 2` | necessary |
| nz-bank-account | three literal hyphens | `count("-") >= 3` | necessary |
| nz-phone | tail `\d{3}[\s-]?\d{3,4}` | `\d{3}[\s-]?\d{3}` search | necessary |
| nz-address | ends in one of 20 suffix words, case-sensitive | same 20 literals, no flags | necessary |
| coordinates | one `,` and two literal `.` | `"," in` and `count(".") >= 2` | necessary |
| nz-ird | two literal hyphens | `count("-") >= 2` | necessary |

| Rule (secretscan) | Weakest condition every match satisfies | Gate | Verdict |
|---|---|---|---|
| private-key-header | literal tail | tail `in` | necessary |
| pgp-private-key | whole literal | whole literal `in` | necessary |
| aws-access-key-id | one of two 4-letter prefixes | either `in` | necessary |
| github-token | alt 1 has `gh`+`_`; alt 2 has `github_pat_` (which has `_`) | `_` and (`gh` or `github_pat_`) | necessary |
| slack-token | starts `xox` | `xox` `in` | necessary |
| slack-webhook | literal scheme+host+path prefix | that prefix `in` | necessary |
| google-api-key | starts `AIza` | `AIza` `in` | necessary |
| gcp-oauth-secret | starts `GOCSPX-` | `GOCSPX-` `in` | necessary |
| stripe-key | `k_live_` or `k_test_` | either `in` | necessary |
| anthropic-key | starts `sk-ant-` | `sk-ant-` `in` | necessary |
| openai-key | starts `sk-` | `sk-` `in` | necessary |
| npm-token | starts `npm_` | `npm_` `in` | necessary |
| twilio-key | starts `SK` (case-sensitive) | `SK` `in` | necessary |
| sendgrid-key | starts `SG.` | `SG.` `in` | necessary |
| jwt | contains `.eyJ` | `.eyJ` `in` | necessary |
| basic-auth-url | contains `://` and `@` | both `in` | necessary |
| assigned (SECRET_KEY_RX) | tail `[:=]\s*["']?` + 6 value chars | `_ASSIGNED_TAIL_RX` | necessary |
| high-entropy | `{32,}` token ⇒ line ≥ 32 chars | `len(line) >= 32`, test-pinned to the pattern | necessary |
| allow-marker (both) | `marker_rx` opens `\b` + escaped literal, no flags | `ALLOW_MARKER in line` | necessary |

Rules a gate names that no longer exist: none (test-pinned). Rules with no gate:
none in either table. `_shadow_spans`: skipping the shadowed rule when its own gate
fails drops nothing (there is no finding to suppress); skipping a shadower whose
gate fails drops nothing (it has no span). The `continue` after the entropy peek is
the last statement of the line loop at HEAD, so it skips nothing today (GT4 on the
fragility). The early `return []` skips only `_dedupe_same_span` and the marker
subtraction, both of which are no-ops on an empty list; no tally counter is
touched by either. The machine-local term list runs ungated (test-pinned, D1);
the path-name scan goes through `scan_lines` and is gated identically, which is
correct because the gates are necessary conditions.

**The tests' near-miss corpora** were written by hand from the same reading that
wrote the gates (one or a few positives per rule, random single-character
mutation), not derived from the regexes. The coverage assertion is per rule, not
per alternative. That is the hinge of GT2.

## Lens 3 — completeness and harvest

- `tools/README.md` describes what both guards catch and says nothing about
  gates; nothing there is now false. `docs/method/GUARDS.md` governs responses to
  findings, not detection, and makes no claim the gates touch.
- `CHANGELOG.md` (2026-10-05 entry) is the delta's one live-surface claim: output
  byte-identical (reproduced), "no rule, finding, suppression or exit code
  changed" (reproduced), and speed figures on a 50 MB corpus (partially
  reproduced, GT7).
- Copies of gated patterns elsewhere: none outside the two scanners (grep of
  `tools/` and `instruments/`). Between the two scanners, three named shapes are
  copied; one has diverged (GT5).
- The sweep surfaced board item `300/020` naming `110/130` as "inherits both"
  with the constraint "output must stay byte-identical" — consistent with the
  delta — and `260/120` citing `110/130`'s gate risk as a class. Nothing else.

## Lens 4 — security and privacy

Design altitude: the gates are a pure optimisation layered under two blocking
boundary guards; the threat is a false negative. Code altitude, by hand against the
OWASP Top 10 and ASVS: injection, XSS and auth classes do not apply (no network,
no HTML, no auth; stdlib only; input is repo text). The relevant classes are
**denial of service through regular expressions** (ASVS V5 input handling; CWE-1333)
and **data exposure in output** (ASVS V8). Exposure: unchanged — findings print
redacted excerpts as before, and the differential runs showed identical excerpts.
ReDoS: three pre-existing quadratic regexes are reachable on gate-passing lines
(GT1). Hunting the line a gate rejects that its rule would match: none found, by
derivation or by 20,181 adversarial lines in three configurations.

## Standing checklist V1–V7

- **V1** — The CHANGELOG's speed figures are stronger than what can be re-driven
  from the repo (GT7); the equivalence claim is exactly as strong as its evidence.
- **V2** — Re-run: both test modules, both selftests, the equivalence claim (three
  ways), the floor on both planes, the full Python suite, the instrument suite.
  Ledger below. One unrelated suite failure recorded (GT8).
- **V3** — The rule changed is scanner internals; README, GUARDS and the floor
  template carry no mirror of it. Nothing owed.
- **V4** — Two homes for leakscan's gate table in one module (GT3).
- **V5** — No internal contradiction found. The secretscan comment "none of the
  NAMED rules carries `(?i)`" is true at HEAD and is the premise of every
  case-sensitive literal gate; it is not test-pinned (folded into GT2's counsel).
- **V6** — Lens 4 above; `/security-review` discharged by grounds.
- **V7** — Provenance stated above and in the brief.

## Findings

### GT1 — MODERATE — three quadratic regexes remain reachable past the gates (pre-existing)

leakscan `email` (`\b[A-Za-z0-9._%+-]+@…`), secretscan `basic-auth-url`
(`\b[a-zA-Z][a-zA-Z0-9+.-]*://…`) and secretscan's `URL_RX` carve-out
(`\b[A-Za-z][A-Za-z0-9+.-]*://…`) each restart a greedy class run at every word
boundary and scan to end of line before failing on the literal that follows. On a
line made of short word-boundary-rich runs (digit-dash, `1.`, `sk-`, `eyJ.`)
without that literal, cost is O(n²): measured at 8K/16K/32K characters, the
regexes alone take 0.10/0.36/1.21 s (email), 0.07/0.11/0.42 s (basic-auth-url) and
0.04/0.15/0.55 s (URL_RX) — a ×4 per doubling. The gates skip these on lines that
lack the literal, which is why `scan_lines` at HEAD is 100× faster than ungated on
those lines; but one trailing `@`, one `://…@` tail, or (for `URL_RX`) any
32-character entropy token on the line re-opens the path: HEAD gated `scan_lines`
measured 0.08/0.33/1.29 s and 0.06/0.21/0.99 s on two such lines. Extrapolated,
a 1 MiB line costs about 22 minutes and the reader's own 4 MiB window about 6
hours — in a **blocking** pre-commit hook and a CI job, for one long line in a
minified asset or data row. A 1 MiB run of this probe exceeded 600 s and had to be
killed. The pre-landing module (`c938b58^`) shows the same ×4 scaling, so this is
charged to the rules, not to the gates; it is recorded here because the brief asked
for regex cost "now that gates change which regexes run", and because the delta's
speed claim invites the reading that the worst case moved. It did not.
*Counsel:* make the three runs non-backtracking — on Python ≥ 3.11 a possessive
quantifier (`[A-Za-z0-9._%+-]++@`, `[A-Za-z0-9+.-]*+://`) fails in one pass; where
the stdlib floor is older, an atomic group or a pre-scan for the literal followed
by a bounded backward match does the same. Pin with a timing test at two sizes
(linear ⇒ ~×2). The fix is to the regexes and is the principal's to decide (a
guard is doctrine by function).

### GT2 — MODERATE — gate necessity is guarded by a hand-kept corpus, per rule not per branch

`GatesAreNecessary.test_a_rule_that_matches_always_passes_its_gate` proves the
gate only on lines the corpus happens to match, and asserts coverage per *rule*
(`exercised == set(GATES)`), so a rule with one matching positive counts as
covered however many alternatives its regex has. If a rule's regex is later
widened under the same name — a second key prefix added to leakscan's AWS rule (as
secretscan's already has), a new IPv6 form, a new token family in a multi-branch
rule — and no positive of the new shape is added, the stale gate rejects every
line of the new shape and the suite stays green. That is the "silent false negative
in a boundary scanner" the module comment names as the worst failure, with the
guard against it resting on a maintainer remembering to extend a tuple in a test
file. Structurally, the gates sit ~380 lines from the rules they condition
(`GATES` at line 613, `STRUCTURAL` at 237; `NAMED_GATES` at 795, `NAMED` at 344),
and a rule's declaration carries no mention of its gate, so the regex edit and the
gate edit never meet in one diff hunk. The secretscan premise "no NAMED rule
carries `(?i)`" is likewise a comment, not a test: a future `(?i)` rule paired with
a case-sensitive literal gate would be the same drift. No defect at HEAD; the
derivation above and the differential runs hold. *Counsel:* (a) declare the gate
beside the rule — a `gate` field on `Pattern`, set in `_p(...)`, with `GATES`
derived from it; (b) pin the premise: assert no NAMED/STRUCTURAL regex has the
IGNORECASE flag unless its gate is flag-aware; (c) replace per-rule coverage with
a corpus generated from the regexes (the brief's lens-2 ask), or at least assert
each top-level alternation branch is exercised. (a) is the one that changes the
maintainer's path; (b) is a two-line test.

### GT3 — minor — leakscan reads its gate table from two homes

`scan_lines` iterates the import-time snapshot `_GATED` (via `_active_rules`),
while `_shadow_spans` looks up the live `GATES` dict per call. Patching one
without the other splits behaviour: the delta's own equivalence test has to patch
`GATES`, `_GATED` and `_ACTIVE_CACHE` together to switch gating off, and a future
caller or test that patches only `GATES` gets gated rules with ungated shadows (or
the reverse). V4, one fact one home. *Counsel:* have `_shadow_spans` read the same
snapshot (pass the active tuple in, or look up through `_active_rules`), or build
the per-rule pairs from `GATES` at call time behind the existing memo.

### GT4 — minor — the entropy `continue` relies on an unpinned structural invariant

The early `continue` after `first = next(entropy, None)` is correct only while the
entropy pass is the last statement of the line loop — stated in a comment, pinned
by nothing. A step appended inside the loop later (a new line-level rule, a per-line
tally) would be silently skipped on every line without an entropy match, which is
nearly all of them. *Counsel:* wrap the entropy block in `if first is not None:`
so no `continue` is needed, or add a test that appends a sentinel step through a
seam and asserts it ran on a short line.

### GT5 — minor — a gated rule is copied between the scanners and has diverged

`aws-access-key-id` is one prefix in leakscan and two in secretscan;
`private-key-header` and `jwt` are textually identical copies. Each gate matches
its own copy, so nothing is wrong at HEAD — but this is where GT2's drift lands
first: harmonising leakscan's rule to secretscan's by copying the regex and not
the gate would silently drop the second prefix. The module docstrings defend the
duplication as deliberate self-containment; that is a fair trade, and it is also
the trade that makes a divergent gate possible. *Counsel:* a cross-pin test that
the three shared shapes are equal in both scanners (or that any difference is
declared in a comment the test reads), which keeps self-containment and removes
the silent half.

### GT6 — note — the brief's first re-run invocation does not run

`python3 -m unittest tools.test_leakscan tools.test_secretscan -v` fails with
`ModuleNotFoundError` (the test modules import their siblings as top-level names).
The working form is `python3 -m unittest discover -s tools -p 'test_leakscan.py'`
(and the same for secretscan), which is what the CI floor runs. Rule 1: the
brief's framing is attackable; this is a defect in the ask, not the work.

### GT7 — note — the CHANGELOG's speed figures cannot be re-driven exactly

"About 3× faster for leakscan and 4.6× for secretscan on a 50 MB corpus" names a
corpus that is not in the repo. On this pass's 650 KB match-dense corpus, gated vs
ungated at HEAD measured 11.9 → 4.4 s (2.7×) and 7.4 → 3.0 s (2.5×); the leakscan
figure is consistent, the secretscan figure is not reproduced (a match-dense
corpus flatters neither). V1: the equivalence claim is reproducible and the speed
claim is a reported measurement with no re-runnable input. *Counsel:* state the
corpus shape (or ship a generator) beside any future speed figure, or state the
figure as "measured once on a private corpus".

### GT8 — note — one unrelated failure in the full suite under load

`test_pins.BoundedMemory.test_peak_memory_does_not_scale_with_sibling_count`
failed once in the full-suite run (1916 tests, 655 s) with machine load averages
3.5–5.7 from other live sessions; the delta touches no file it reads. Recorded, not
charged: a memory-scaling assertion on a shared machine is the env-gated class, and
one run is not a diagnosis. The two delta test modules passed in isolation (152 and
169 tests).

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 3 minor · 3 note.** Every gate at
HEAD is a necessary condition for its rule, by derivation and by three independent
differential runs; the delta's byte-identical claim reproduces. The two MODERATEs
are a pre-existing quadratic worst case the gates mask but do not fix (GT1), and a
necessity contract whose only guard against future drift is a hand-kept corpus
(GT2). Nothing applied; all findings are for the principal.

## Re-run ledger (all 2026-10-17 UTC, worktree HEAD `8acfff1`, `nice -n 10`, foreground)

| Claim / check | How | Result |
|---|---|---|
| Delta test modules | `unittest discover -s tools -p test_leakscan.py` / `…secretscan.py` | 152 OK · 169 OK |
| Selftests | `tools/leakscan.py --selftest`, `tools/secretscan.py --selftest` | both OK, exit 0 |
| Gated = ungated at HEAD | monkeypatched module over clone tree + 20,181-line corpus, 3 disable sets each | identical, both scanners |
| Pre- = post-landing | `c938b58^` plain vs `c938b58` gated, same inputs | identical, both scanners |
| Gated = ungated at landing | `c938b58` both modes | identical, both scanners |
| Corpus reaches every gated rule | per-rule counts from the gated run | all 15 + all 19 fire |
| Adversarial cost | per-cell subprocess timing at 16K/32K, and 8K/16K/32K | GT1 (×4 per doubling) |
| Full Python suite (once) | `unittest discover -s tools -p 'test_*.py'` | 1916 run, 1 failure (GT8) |
| Instrument suite (once) | `node --test instruments/*.test.js` | 447 pass, 0 fail |
| Floor, hook plane | `floor.py --plane hook --root . --tools tools` | all enforced ✅, exit 0 |
| Floor, CI plane | `floor.py --plane ci --root .` | exit 0; secretscan 23 advisory 🟡; leakscan clean (structural + local) |
| Cold sweep | `coldsweep.py` + four `--also-exclude`, no `--include-barred` | 43 hits, 444 barred, 2 unbarred board lines read |

## Follow-up checklist (for the principal; nothing applied)

- [ ] GT1 — decide whether to make the three regexes non-backtracking and pin
      linearity with a timing test (Python floor permitting possessive quantifiers).
- [ ] GT2 — decide on declaring the gate beside its rule, pinning the no-`(?i)`
      premise, and per-alternative (or regex-derived) coverage.
- [ ] GT3 — one home for leakscan's gate table.
- [ ] GT4 — remove the `continue`'s dependence on loop order, or pin it.
- [ ] GT5 — cross-pin the three shared shapes between the scanners.
- [ ] GT6 — correct the re-run invocation in the brief template these briefs copy.
- [ ] GT7 — ground future speed figures in a re-runnable corpus.
- [ ] GT8 — re-run `test_pins.BoundedMemory` on a quiet machine before treating it
      as flaky.

### Reconcile

Phase 1 was committed as `8b13041` before any of the following was opened. Opened
for this step, on the orchestrator's release, 2026-10-17 UTC: the sibling's text
(as a message, not the file); the intent record
`docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md` (its `110/130`
section and the queue handoff); the queue pointer `160/720`; the landing and merge
commits' message bodies (`c938b58`, `e7575f7`); and the passages of the five named
prior verdicts that bear on these surfaces (located by grep, read in context). No
phase-1 text is revised below.

**Against the intent record and the commit bodies.** Every claim they make that
this pass could re-drive, it re-drove and reproduced: byte-identical output,
no rule/finding/suppression/tally/exit change, every gated rule exercised, lever 3
declined for the reason the source records. Two details sharpen phase-1 findings
rather than alter them. (i) The orchestrator "read every secretscan gate against
its pattern" and checked the no-`(?i)` premise for the *named* rules; the leakscan
gates are not recorded as read by anyone but their author. This pass derived both
tables and found them sound, so there is no gap at HEAD — but it is the premise
GT2 asks to pin. (ii) "The fuzz first caught two gate transcription errors of
mine, both fixed before this commit" is the strongest evidence in the record *for*
GT2: wrong readings of a pattern do happen, and the only thing that caught them was
the corpus — which is the one guard the design leaves to hand maintenance. The merge
body's "3.1× and 4.6×" is the figure GT7 could not re-drive; unchanged.

**Against the seeded questions.**

1. *Two AWS patterns, or one gate narrower than its pattern?* The patterns differ:
   leakscan's rule names one four-letter prefix, secretscan's names two, and each
   gate matches its own pattern exactly. Neither gate is narrower than its rule.
   Formed before reading this as GT5 (the divergence is the drift site, not a
   defect).
2. *Do any counted/literal gates miss a separator or suffix the pattern accepts?*
   No. Every separator the five named patterns accept is a literal ASCII character
   (`-`, `[:-]`, `\.`, `,`), and the suffix words are case-sensitive literals with
   no flag, so an en dash, a space or a different case does not match the *rule*
   either. Unicode digits and whitespace are accepted by `\d`/`\s` in the rules, but
   the gates that could be affected count literals the rule also spells literally
   (`nz-bank-account`, `nz-ird`, `mac-address`, `coordinates`) or use the same
   Unicode class (`nz-phone`, `payment-card`). The phase-1 corpus carried
   Arabic-Indic and full-width digits, no-break and em spaces, full-width colon,
   dot and at-sign, and U+2010 hyphen; gated and ungated output was identical.
   Answered in the phase-1 table.
3. *Is "no NAMED rule carries `(?i)`" also true of `re.compile` flags and of
   leakscan's structural rules?* Yes on both counts at HEAD: `_p(...)` passes
   `flags=0` for every rule in both tables, no call site sets a flag, and `(?i)`
   appears inline only in `PII_KEY_RX` and `SECRET_KEY_RX`, whose gates test a
   letter-free tail. The premise is true and unpinned — GT2's counsel (b) is the
   two-line test that pins it.
4. *Would the author's own generator ever produce the line that exposes a wrong
   gate?* Not if the wrong reading is shared by gate and positive: the positives
   are hand-written and the mutation is single-character, so a missing alternative
   is never generated (`EVIDENCE.md` §15). It did expose two transcription errors
   where the positive was right and the gate wrong, which is what it can do. The
   outside-the-author check for this delta is phase 1's derivation from the regex
   and its independently derived corpus; both found no wrong gate. This is GT2.
5. *Did the old no-finding path count or report anything the early `return []`
   skips?* No. With an empty list the old path called `_dedupe_same_span([])`
   (returns `[]`), iterated nothing, and touched no tally; `scan_lines` has no
   stale-marker accounting (markers are subtracted per finding only), and the
   advisory count is computed by the caller from the returned findings. Answered
   in phase 1 (lens 2).
6. *Rename or split: silent detach, or a gate inherited by a different pattern?*
   A rename detaches **loudly**: `test_every_gate_names_a_real_rule` fails the
   suite on a gate whose name matches no rule. Inheritance — a new or widened
   pattern under an existing gated name — is caught only if the corpus holds a
   positive of the new shape that the old gate rejects. Nothing structural pins
   it. This is GT2, and the structural remedy is GT2's counsel (a): declare the
   gate beside the rule so the two change in one hunk.

**Against the prior verdicts.**

- `2026-10-04-2215-bounded-pathscan-linkscan-cold.md`, **BP9**: found the same
  class in pathscan's scheme-URL pattern — quadratic on "a long run of dotted or
  hyphenated words", about a quarter of an hour per 1 MiB window — and recorded
  that "`110/130` covers regex cost per byte in leakscan and secretscan only".
  The landed `110/130` took lever 4 and did not touch per-byte regex cost on
  gate-passing lines, so the half BP9 left to this item is the half GT1 reports
  as open. GT1 stands at MODERATE; this reconcile raises its standing from "a
  pre-existing shape this pass happened to measure" to "the named remainder of a
  class a prior verdict already filed".
- `2026-09-25-0715-secretscan-stream-pathscan-roots-cold.md`: measured
  `basic-auth-url` and `URL_RX` at 25k/50k/100k characters on *base64 and
  alphanumeric runs*, found them linear, and recorded "no super-linear path
  found". That measurement is right for its input and does not generalise: a
  single alphanumeric run has a word boundary at one position, so the greedy
  class restarts once; GT1's inputs (`sk-`, `eyJ.`, `12-` repeated) place a
  boundary every three or four characters and reproduce ×4 per doubling on the
  same two regexes. The control was not comparable to the adversarial shape.
  Not a contradiction of that pass's data; a correction of its conclusion.
- `2026-10-03-0357-shared-allow-marker-grammar-cold.md` and
  `2026-08-09-0826-e7-leakscan-build-cold.md`: both concern the marker regex's
  scope backtracking (a scoped form re-parsing as unscoped). The delta's
  `ALLOW_MARKER in line` pre-check sits in front of that regex and alters neither
  its acceptance nor its backtracking — the pre-check is a necessary literal, and
  phase 1's corpus carried every marker spelling. Nothing to reconcile.
- `2026-10-04-2215-linear-line-reader-cold.md`: the reader's cost; names
  `110/130` only as the commissioning head. Nothing bears on the gates.

**Finding formed at reconcile.**

### GT9 — note (formed at reconcile) — per-byte regex cost: three sightings, no standing test

BP9 (pathscan, 2026-10-04), the 2026-09-25 pass's falsified-then-restored
hypothesis, and GT1's three regexes are the same defect class — a greedy class
restarting at every word boundary — found three times on three guards by hand
probes with different inputs, one of which drew the wrong conclusion from a
non-comparable control. `PROPAGATION.md`'s promotion rule (> 2 instances) is met.
*Counsel:* one shared timing test, applied to every guard's rule table, that runs
each pattern on a boundary-rich adversarial line at two sizes and asserts roughly
linear scaling — the control shape written down once, so no future probe has to
rediscover which input is adversarial.

**Overall line, restated after reconcile:** PASS-WITH-FINDINGS — 0 MAJOR ·
2 MODERATE · 3 minor · 4 note. No phase-1 severity changed; GT9 is new, at note.

## Deferred material — folded in at reconcile

# Deferred sibling — per-rule gates in leakscan and secretscan (160/720)

**Held under REVIEW.md rule 1's split. Open only after your phase-1 findings in
`docs/reviews/2026-10-16-1551-scanner-rule-gates-cold.md` are committed.** A
floor, never a fence: these questions were seeded by a brief-writer who read the
landing diff and commit body, so they carry that reading's framing. Reconcile
against them; do not let them narrow what you found.

## Intent record (not opened by the brief-writer)

- `docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md`

## Prior verdicts on the same surfaces (named, not opened)

Many verdicts name these two scanners. The nearest, for the reconcile:

- `docs/reviews/2026-10-04-2215-linear-line-reader-cold.md` (names 110/130)
- `docs/reviews/2026-10-04-2215-bounded-pathscan-linkscan-cold.md` (names 110/130)
- `docs/reviews/2026-09-25-0715-secretscan-stream-pathscan-roots-cold.md`
- `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`
- `docs/reviews/2026-08-09-0826-e7-leakscan-build-cold.md`

## The queue pointer's own lens hints

None. The pointer is refs-only, plus the orchestrator's brief-writing claim line.

## Seeded questions (the brief-writer's, from the diff)

1. leakscan gates `aws-access-key-id` on one four-letter prefix; secretscan
   gates its rule of the same name on two. Are the two patterns really different,
   or is one gate narrower than its pattern?
2. Several leakscan gates count ASCII hyphens or test ASCII literals
   (`nz-bank-account`, `nz-ird`, `mac-address`, `nz-address`, `coordinates`).
   Does any of those patterns accept a space, an en dash, a Unicode digit or a
   different letter case as a separator or suffix that the gate does not?
3. The commit says "none of the NAMED rules carries `(?i)`". Is that also true of
   flags passed to `re.compile`, and of the structural rules in leakscan, which the
   same sentence does not cover?
4. The differential fuzz (1.15M lines) and the near-miss tests were generated by
   the same author who wrote the gates. If a gate encodes a wrong reading of a
   pattern, would that generator ever produce the line that exposes it?
5. secretscan's new early `return []` when nothing was found: did the old path,
   after the loop, count or report anything a no-finding file still owes (a stale
   allow marker, an advisory tally, a dedupe counter)?
6. A gate is looked up by rule name. If a rule is later renamed or split, does the
   old gate silently detach (the rule runs ungated: slower, still safe) or can a
   new rule inherit a gate written for a different pattern (a gate that rejects
   lines the new pattern matches: a silent miss)? Is anything pinning that?
