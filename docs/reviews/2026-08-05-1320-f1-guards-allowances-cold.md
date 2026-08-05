# Brief — F1 guard-governance rebuild + the allowance rules, rule-4 cold pass

**Queue ref (refs only):** the F1 guard-governance rebuild + Mike's three
allowance rules enforced across all twelve scanners. Delta:
`docs/method/GUARDS.md` (new) + `docs/method/README.md`; the twelve
scanners and their tests; one marker fix in a 2026-07-12 session record
(all landed 2026-08-05, merge `cee1753`). *Intent record:* the authoring
session record + the F1 intent cold pass rulings FG1–FG6 (Mike,
2026-08-03) + the D1 ruling (Mike, 2026-08-04) — opened at reconcile only.

**Pass type:** code/design cold pass (rule 4 — GUARDS.md is doctrine by
function; the scanner changes are the security floor).

**Provenance (rule 4):** reviewed by the same Mike-spawned Fable taker
session as the day's six other passes; the authoring session
(`guard-governance-allowances`) neither started nor instructed it. Claim
`b120d30` on `main` before the work. Brief written by the taker, cold.

# Verdict — PASS-WITH-FINDINGS · 0 MAJOR / 1 minor / 2 notes

**What was verified live at HEAD, not read from the delta's account:**

- Suite: **993 tests, OK.** The hook plane runs green on the live tree
  with the new suppressed-counts lines on every scanner.
- **Rule (c) is enforced, both mechanisms, probed live**: a reasonless
  allow-marker exempts nothing (the finding still fires — this also
  proves the author's own `\S`-regex defect fixed, since the empty-reason
  marker form is exactly the case it mis-parsed); a reasonless ignore
  glob is a **config error, exit 2**, with a message citing GUARDS.md and
  both accepted reason forms; a reasoned glob passes and is counted.
- **Rule (b) is live on every scanner**: clean results carry the
  suppressed count by mechanism (markers · globs · disabled rules), with
  known zeros printed and per-rule breakdowns where non-zero — observed
  across all twelve in a full hook run.
- **Rule (a) has an operational form**: the granularity table
  (line / check / repo) plus rule-scoped markers
  (the narrow `allow:<rule>:` form offered in the finding footers as the
  default counsel).
- **GUARDS.md discharges all six FG rulings**: FG1 — adoption is in the
  model (deferment at repo granularity, C3 named as the build) and P3's
  boundary is answered explicitly (rule in scope, mechanism out); FG2 —
  provenance-not-direction is *tested, not inherited*: the test is
  stated, the three existing lawful downward lanes found, the invariant's
  four conditions bind, and the E6d(i) supersession is **flagged 🎯 for
  Mike on the roadmap, in the doc, and in the session record — asked,
  not assumed**, with E6d(ii)/(iii) untouched; FG3 — the granularity
  axis and the acceptance/deferment split land verbatim; FG4 — the
  prior-art table is re-derived at pickup and the two corrections beyond
  the review's claims check out against this reviewer's own knowledge of
  the sources (Semgrep's confidence/likelihood/impact fields with
  computed severity; CodeQL's precision/security-severity vs
  problem.severity split; CVSS v4.0's Threat and Environmental groups);
  FG5 — the false-positive route is written as a specialisation of
  resolved-upward, not a second original; FG6 — discharged earlier by the
  pointerscan corpus, correctly absent here.
- **D1 as ruled**: the term list always runs; allow-markers exempt
  structural rules only. The consequence the author handed up is real and
  correctly scoped — with the C5-composed term list now in the machine
  config, a full-tree local scan reports the historical estate-root and
  identity mentions (89 findings on this machine at HEAD); the hook plane
  is unaffected by construction (staged lines only), CI never holds the
  term list, and the fix home is the operator's own list, exactly as D1's
  ruling reasoned.

## Findings

**GA1 (minor) — the reason-required loader is ten near-identical copies,
and the build's own diagnosis argues against that.** The survey that
motivated this work found the weak marker variant propagating *because*
the convention lived as twelve copy-pasted headers with no doctrine page;
the fix adds the doctrine page, then delivers the ignore-file rule as ten
per-scanner `load_ignore_globs` copies with no shared source. Each copy
is test-pinned, and GUARDS.md now anchors the convention — but the drift
mechanism is the one just named, and this same day's landings contain the
counter-pattern (`harvestscan` importing `pointerscan.is_pointer`, HV2).
Counsel: single-source the loader, or record standalone-copies as the
scanners' decided design with drift accepted; either answer, not silence.

**GA2 (note) — the first blocked commit on a historical mention will
confuse someone; this line is the sentence that saves the chase.** Any
future commit touching a line that carries an estate-root or identity
mention now blocks at the hook on the term-list rule, and the fix lives
in the operator's machine-local list (or a reword), never in an
allow-marker — D1 removed that route deliberately. The C5 ruling recorded
this interaction in advance; it is now live.

**GA3 (note) — "keeps the suppressed set retrievable" is discharged by
greppable markers plus JSON counts, not by a surface.** The JSON carries
counts by mechanism and rule; the set itself is retrievable only by
grepping the markers and reading the ignore files. Honest today; if the
standing-inventory question matters at the publication boundary the doc
itself names, a listing surface (or a floorfleet line) is the natural
build. Recorded so the claim is not read as a built feature.

## Reconcile (intent records opened after the findings above were committed)

Opened after the findings commit: the authoring session record
(`2026-08-05-1150-guard-governance-allowances.md`), the F1 intent cold
pass rulings FG1–FG6, and the D1 ruling in E7.

- **No contradictions; the account is unusually self-incriminating and
  checks out.** The survey figures (rule (c) in 3 of 12 markers, 1 of 8
  loaders; rule (b) in 1 of 12, `stampscan` the exemplar; `floor.py`
  already complete), the three defects the build caught — including the
  author's own `\S` regex failing rule (c) inside the change enforcing
  it, which this pass's reasonless-marker probe confirms fixed — and the
  stanza-or-trailing reason call with all 31 live glob entries passing
  unchanged.
- **GA1 is grounded in the account's own diagnosis**: "the convention
  lived as twelve copy-pasted module headers … whichever variant got
  copied next propagated" — the delivery reproduces that mechanism for
  the loader, which is why the finding asks for a decision rather than
  assuming the refactor.
- **GA2's count is wider than the account's** and both are right: the
  author recorded 3 identity-line findings from D1; the C5 term-list
  composition landed after their session, and at this pass's HEAD the
  full-tree local scan reports 89 — the same class, widened exactly as
  the C5 ruling predicted. Forward-only holds on both counts.
- **FG2's handling matches its ruling precisely**: hypothesis tested at
  design, E6d(i) supersession asked of Mike in three places, nothing
  reverted unilaterally.

## Disposition — the F1 review cycle CLOSES (0 MAJOR); rulings stay Mike's

A code/design cold pass returning **0 MAJOR** — the F1 cycle **closes,
terminal** per the no-MAJOR rule. The two 🎯 items the delta itself
queued (the E6d(i) supersession confirmation; the D1 identity-lines
consequence) are decision-owed, not review-owed, and stand untouched.
GA1 (minor) and GA2–GA3 (notes) join the day's ruling round.
