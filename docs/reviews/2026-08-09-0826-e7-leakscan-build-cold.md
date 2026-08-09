# Cold pass — the E7 leakscan build (D2–D6 fixes + the G1/G2/G4/G6/G7 builds)

**Pass type:** code cold pass (rule-4 queued — an application of ruled
decisions; the applier's judgement produced the delta).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-06, and the session that landed the 2026-08-09 follow-up on the same
  surfaces (see *What the work is*).
- **Who spawned this review:** the principal (Mike), in a session he opened on
  2026-08-09 and pointed at the review queue — rule 4's worked example. His
  words: *"Please do any review work that waiting."*
- **Author's non-involvement:** the taker session authored no part of this
  delta, was neither started nor instructed by the authoring sessions, and
  wrote this brief as the non-author taker. Rule 4's single criterion is met,
  and the tier was checked at selection.
- **Orchestration shape:** the review runs under an orchestrator holding a
  context partition — the intent-record references are withheld from this brief
  and handed to the reviewer only after its own findings are durably written.

## What the work is

Code landed 2026-08-06 plus a 2026-08-09 follow-up on the same surfaces,
reviewed at HEAD:

1. [`tools/leakscan.py`](../../tools/leakscan.py) and
   [`tools/test_leakscan.py`](../../tools/test_leakscan.py) — the D2–D6 fixes
   and the G1/G2/G4/G6/G7 builds; the suite grew 53 → 114, then 114 → 119 in
   the follow-up.
2. [`tools/leakscan-terms.example.txt`](../../tools/leakscan-terms.example.txt)
   — the `forms:` syntax.
3. The `CHANGELOG.md` entry (2026-08-06), and the 2026-08-09 follow-up: the
   scoped `local-term` marker (delta widened per the landing-commit rule).

## Hard constraint — read before running anything

**atelier is a PUBLIC repo.** The scanner under review exists to keep
machine-local terms out of it. The operator's real term list is machine-local
(`$ATELIER_LEAKSCAN_TERMS`, else `~/.claude/leakscan-terms.txt`), outside
every repo by design.

- Probe with a **scratch term list** written to the session scratchpad only.
  Do not read the operator's real list into your context, do not modify it,
  and never point a probe at it.
- **Never write any machine-local term** — or any private repo's name — into
  any file in any repo, including your verdict and any scratch file inside a
  working tree. Counts and classes only.

## Scope

Widest the work admits: the intent of each fix and build as the code expresses
it, the `forms:` syntax design, the scoped-marker design, the code, the tests,
and live behaviour on both planes (staged and tree). **Non-goals:** none
narrows the delta. The reviewer does not decide findings' dispositions;
residue joins the principal's ruling round per house practice.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Does the `forms:` syntax cover the shapes a real term takes, and
   does the scoped marker's scope model leave a hatch wider than the finding
   it suppresses?
2. **Correctness & quality** — run the suite; probe the scanner live with a
   scratch term list on both planes; verify marker scoping suppresses exactly
   the scoped class and nothing else, and that exit codes hold.
3. **Completeness / harvest** — which term shapes or file classes escape;
   does the example file teach the syntax the code actually implements?
4. **Security & privacy** — mandatory and central: this delta *is* the
   privacy control. Check for bypasses — a term reachable through an encoding
   or splitting the `forms:` model misses, a marker scope that silently
   swallows a genuinely new leak, ignore-file precedence making a term
   unreachable where it should bind. Your verdict itself must honour the hard
   constraint above. The house security scanner reads pending diffs; this is
   a landed-delta review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read, at least: the suite-count claims (53 → 114 at the
2026-08-06 landing, 114 → 119 at the follow-up) and the full suite at HEAD
(house invocations in [`.githooks/pre-commit`](../../.githooks/pre-commit)),
a live probe with a scratch term list on both planes, the `forms:` syntax
against the example file, and the scoped `local-term` marker's behaviour on
the three published-identity lines it exists for.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, and every prior verdict
in `docs/reviews/`. The intent record (the sweep record and the ruling the
delta applies) is held by the orchestrator and will be provided on receipt of
your committed findings. Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `LK`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.

---

# Verdict — cold rule-4 pass (Fable), phase 1

## Provenance (repeated)

- **Pass type:** code cold pass, rule-4 queued application of ruled decisions.
- **Tier:** Fable — the principal-named review tier (ruling 2026-08-04); checked
  at selection.
- **Author of the work under review:** the sessions that landed the 2026-08-06
  E7 build (`d740899`) and the 2026-08-09 follow-ups (`c827705` scoped hatch,
  `8276a54` quote fix) on the same surfaces.
- **Who ran this review:** a session the author neither started nor instructed,
  taking the queued `⏳` item. Rule 4's single criterion is met.
- **Reviewed at:** HEAD `0ca92f4`. Working tree: the shared read-only reviewer
  worktree; no git mutations run here. All live probes ran against scratch
  fixtures / scratch git repos under the session scratchpad.
- **Hard constraint honoured:** every probe used a SCRATCH term list. The
  operator's real machine-local list was never read, never pointed at, never
  named. Scratch lists carried only fictional terms plus the repo's *already
  published* identity name (ADR 0005 worked example) as a stand-in. No
  machine-local term or private repo name appears in this verdict — counts and
  classes only.
- **Orchestration:** the intent-record references are orchestrator-held under
  the rule-1 context partition and were not read before these findings were
  durably written. A Reconcile section follows on their receipt.

## Load-bearing assumptions I named first (lens 1)

Before reading the brief's framing as settled, the assumptions this delta rests
on — each one attackable:

1. **The `forms:` separator class `[\s._-]` is "the forms a name actually leaks
   as."** Load-bearing: if a real leak form falls outside that class, an opt-in
   `forms:` term gives false confidence. Attacked — see LK3 (`/` and `+` absent;
   the path plane is slash-delimited) and LK2 (no Unicode normalisation).
2. **A malformed allow-marker fails closed.** The contract comment and D1 both
   promise "narrow" — a scoped marker never silently exempts a leak it did not
   name, and "a typo fails closed." Attacked and *falsified* for one shape — see
   LK1: a scoped marker with a missing reason, or a space in a composed scope,
   backtracks to the UNSCOPED (all-structural) form, silently widening beyond
   what was named.
3. **The scoped `local-term` hatch opens only the deliberate route and cannot
   reach the term layer by accident.** Held — every probe confirms the term
   layer is unreachable unless `local-term` is named explicitly with a reason;
   the empty/backtracked forms never touch it (LK1's one saving bound).
4. **Structural-only cover on CI + full cover on the hook (`--require-terms`) is
   an honest, declared split.** Held — floor registry wires `--require-terms` on
   hook, plain on CI, and renders 🟡 partial on CI; fail-closed on a typo'd
   `--terms` path confirmed (resolve_terms_path returns None → exit 2 under
   `--require-terms`).
5. **The suite is the detection contract** (canary count pinned, both
   directions). Held — 122 tests green at HEAD in a git repo; canary and
   placeholder counts pinned; the two suites guard each other.

## Per-lens answers

### Lens 1 — approach & assumptions

Sound in the main. The three-layer split (structural / key-context / literal),
the find-first-subtract-second discipline, and the deliberate-hatch complement
to D1 are the right shapes, grounded in real rulings. The `forms:` syntax covers
the *common* leak forms (slug, snake, dotted, camel, run-together, double-space
— all re-verified, all match) but not every shape a real term takes (LK2, LK3).
The scoped-marker scope model is correct in intent but its *parser* leaves a
hatch wider than the finding it suppresses under one malformed-input class
(LK1) — the exact failure the lens is told to hunt.

### Lens 2 — correctness & quality

Suite counts re-run, not read, at the landing commits (inside a git repo so the
`git diff --cached` test class runs):

| Commit | Meaning | Suite | Result |
|---|---|---|---|
| `d740899~1` | before E7 build | **53** | OK |
| `d740899` | E7 landing (2026-08-06) | **114** | OK |
| `c827705~1` | before follow-up | 114 | OK |
| `c827705` | scoped-hatch follow-up (2026-08-09) | **119** | OK |
| HEAD `0ca92f4` | + quote fix `8276a54` | **122** | OK |

The brief's `53 → 114` and `114 → 119` claims reproduce **exactly**. HEAD is 122
because the same-day quote fix (`8276a54`, same surfaces, in-delta) adds three
tests. Full tools suite at HEAD via the house invocation
(`python3 -m unittest discover -s tools`): **1210 tests, OK**. Hook-plane floor
in a scratch clone with a scratch term list: leakscan ✅ enforced, exit 0.

Caution for any re-runner: run the leakscan suite from **inside a git repo**. In
a bare scratch dir the `StagedAbsolutePathTest` class reports 2 spurious
failures — `git diff --cached` exits 129 with no repo, so the absolute-path
branch is never reached (LK4). Behaviour stays fail-closed (exit 2); only the
test's message assertion trips. Not a shipping defect.

Live probes with a scratch term list, both planes:
- **Tree plane** — planted fictional leaks (term, slug, regex-family, email,
  IPv4, DOB key) all flag; `local-term`-scoped and `ipv4`-scoped markers
  suppress exactly their class and are counted in the tally. Exit 1.
- **Staged plane** (scratch git repo) — staged term + IP flag, exit 1; a
  rename-only to a term-carrying filename and a new binary/empty file with leaky
  names all pass **clean** at the added-line level. That is correct for
  `--staged` (it scans added *content*, and `+++ b/` path lines are not added
  content) but note the asymmetry: **G2 path-name cover holds on the tree/CI
  plane but not on the staged hot path for a rename or an empty/binary file** —
  a new file whose *name* carries a leak, added with no leaky content, is not
  caught until CI. Recorded as a reach note, not a finding: the code's staged
  branch does call `scan_path_name`, but only over `staged_added_lines()` keys,
  which a rename/empty-add does not populate.
- Marker scoping verified: unscoped exempts all structural never term; scoped
  exempts only its class; a *reasoned* typo scope exempts nothing (fails closed,
  correct). Exit codes hold across every case.

### Lens 3 — completeness / harvest

The example file (`leakscan-terms.example.txt`) teaches the syntax the code
actually implements — `forms:` joins words with "whitespace, dots, underscores
or hyphens," which is precisely `[\s._-]`, and it states the line-based limit
and the word-boundary ignores. No overclaim; the worked example's match/ignore
lists all reproduce. Gaps are in the *design's* reach, not the doc's honesty:
LK2 (normalisation) and LK3 (`/`, `+` separators, salient because G2 scans
slash-delimited paths). The don't-add discipline (compact digit runs stay
key-context-only) holds in code and tests.

### Lens 4 — security & privacy (central; this delta *is* the control)

**Reach case (landed-delta):** the house `/security-review` scanner reads
pending diffs; this is a landed-delta review, so it has no diff to aim at. It is
discharged here in one line with grounds, per REVIEW.md — the review substitutes
live behavioural probes on both planes against scratch fixtures, which is the
reach that applied.

Bypass hunt, the three classes the brief names:

- **An encoding/splitting the model misses.** Found two. LK2: no Unicode
  normalisation, so an NFD-encoded macron name evades an NFC term (and vice
  versa) — directly relevant to a te-reo-heavy estate. LK3: the derived-form
  separator omits `/`, so a name split across path components evades even a
  `forms:` term on the very plane (G2) that reads paths.
- **A marker scope that swallows a genuinely new leak.** Found — LK1, the
  central finding. A scoped marker whose scoped form is malformed (missing
  reason, or a space in a composed scope) backtracks and re-parses as the
  UNSCOPED all-structural form. The marker *reads* as narrow to a human but
  *behaves* as exempt-all-structural, silently exempting any co-located
  structural leak the author never named. This is the unsafe (under-block)
  direction of exactly the silent-marker class the 2026-08-09 quote fix just
  closed in the *safe* direction. Saving bound: it can never reach the term
  layer (verified), and the tally still counts each suppressed rule.
- **Ignore-file precedence making a term unreachable.** Confirmed and sound as
  designed — a `.leakscanignore` glob suppresses the whole file including term
  hits (the widest allowance), but is reason-gated (unreasoned ⇒ exit 2,
  verified) and counted. The current in-tree globs are narrow (specific files +
  two dirs, no `*`). Note LK5 flags only the standing property that a future
  broad glob would silently disable term cover for its paths.

Your verdict honours the hard constraint: no machine-local term, no private repo
name, counts and classes only.

## Findings

- **LK1 — MODERATE (argues MAJOR).** A scoped allow-marker collapses to the
  unscoped all-structural form when its scoped segment is malformed — a missing
  reason (`leakscan:allow:ipv4:`) or a space in a composed scope
  (`leakscan:allow:email, ipv4: reason`). The optional rule group fails to
  parse, the regex backtracks, and `leakscan:allow` + `:` + the intended
  rule-name's first letter re-matches as an unscoped marker with that word as
  its "reason." Effect: every structural rule on the line is silently exempted,
  strictly wider than the author named — the unsafe direction of the
  silent-marker class. Violates the D1 / rule-(a) narrow-scope invariant and the
  contract comment's "a typo fails closed." Bounds that cap severity: it never
  reaches the term layer (the highest-confidence layer stays enforced, probed),
  the tally still counts the suppressed rules, and no in-tree marker is currently
  in the vulnerable shape (latent, not live). The MAJOR argument: it is a silent
  *under-block* on the privacy control, worse in direction than the over-block
  the project treated as a real Fixed defect the same day. **Test gap:** no
  canary for a reasonless scoped marker, nor a spaced composed scope, on a line
  bearing a second leak. Recurrence-prevention (proposed, not applied): fail the
  scoped form closed when it carries no reason instead of backtracking to
  unscoped, and add both canaries. Disposition is the principal's.

- **LK2 — minor.** Term and `forms:` matching does not Unicode-normalise. An
  NFD-decomposed macron name does not match an NFC term literal (and vice
  versa); probed both directions. Estate-relevant (macrons on te reo Māori names
  are pervasive per house convention), low likelihood (needs a normalisation
  mismatch between term and text). No overclaim in docs; this is a reach gap.

- **LK3 — minor.** The derived-form separator class `[\s._-]` omits `/` and `+`,
  so a name spread across path components (`jane/q/public.md`) or an email
  localpart tag (`jane+q+public`) evades even a `forms:` term. Salient because
  G2 scans repo-relative paths, which are slash-delimited — the one plane where
  `/` between name parts is the expected shape. The example file does not claim
  to cover these, so it is a design-reach gap, not a doc defect.

- **LK4 — note.** `StagedAbsolutePathTest` asserts stderr message text, but when
  cwd is not a git repo the `git diff` failure branch fires first (exit 129 →
  reported as "git diff failed", still exit 2). Behaviour stays fail-closed; only
  the assertion is cwd-fragile. Re-runners must run the suite inside a git repo
  to avoid two spurious failures. Not a shipping defect.

- **LK5 — note.** Reviewer awareness, not a defect: a `.leakscanignore` glob
  suppresses the term layer for matched paths (ignore precedes the term list).
  This is the documented widest allowance, reason-gated (exit 2 if unreasoned,
  verified) and tallied. Current globs are narrow. Flagged only so a future
  broad glob is recognised as silently disabling term cover for its paths.

- **Staged-plane G2 asymmetry** (folded into lens 2, not a separate LK): a
  rename-only or empty/binary add whose *name* carries a leak is caught on the
  tree/CI plane but not on the staged hot path. If the ruling round wants it
  tracked, promote to a finding; recorded here as a reach note.

## Overall

**PASS-WITH-FINDINGS.** 5 findings (0 MAJOR, 1 MODERATE, 2 minor, 2 note), plus
one reach note. The numbers hold — every re-run claim in the brief reproduces
exactly (53 → 114 → 119; full suite green; both planes live-proven). The delta
is well-built and honestly recorded. The one substantive finding (LK1) is a
latent silent-widening hole in the marker parser that the lens-4 mandate exists
to catch; it is bounded (never the term layer, always tallied) and not currently
triggered by any in-tree marker. No finding's disposition is decided here —
residue joins the principal's ruling round.

## Follow-up checklist

- [ ] LK1 — principal to rule: fail a reason-less or malformed scoped marker
      closed rather than backtracking to unscoped-all-structural; add the two
      missing canaries (reasonless scoped marker + spaced composed scope, each
      on a line with a second structural leak). MODERATE, argues MAJOR.
- [ ] LK2 — decide whether to NFC-normalise both term and scanned text before
      matching. minor.
- [ ] LK3 — decide whether the derived-form separator should include `/` (path
      plane) and/or `+`. minor.
- [ ] LK4 — optional test hardening: skip or guard `StagedAbsolutePathTest` when
      cwd is not a git repo so the intended assertion is what fails. note.
- [ ] LK5 — no action; operator-awareness note for future `.leakscanignore`
      edits.
- [ ] Staged-plane G2 asymmetry — decide whether to promote to a tracked
      finding.

## Reconcile

Written after the phase-1 verdict above was durably committed, on receipt of
the deferred references: the sweep record
`docs/sessions/2026-08-03-2050-leakscan-pii-sweep.md` and the 2026-08-04 E7
ruling harvested to `docs/ROADMAP-DONE.md` § "E7 built". Only those two
surfaces were opened; the phase-1 text above is unrevised. Anything new here
is marked post-reconcile.

### Agreements

- **The delta is the ruling, faithfully.** Every fix and build I verified live
  matches the ruling's verbatim terms: D1 as (a) with the term list always
  running (probed, held in every case); D2 as (a) — `::` or four-plus groups;
  D3–D6 as ruled (33 computed netmasks + resolvers, capitalised-word suffix
  guard, MAC/IPv6 shadowing with the disabled-shadower and exempted-span
  clauses, exact all-zeroes match); G1/G2/G4/G6/G7 funded and delivered as
  described; G5 deferred and G3 absent from the funded list, matching the
  build's own "not built, untouched" statement.
- **The verification claims cross-check.** The ruling record's "leakscan
  53 → 114" is exactly what my re-run reproduced at `d740899`; the sweep's
  probe classes (the personal-data key block, the bracketed phone form, the
  slug/camel/snake/double-space forms of a listed name) all now flag in my
  scratch probes, closing the sweep's "covered by nothing" list where the
  ruling funded it.
- **The priced limits were respected by phase 1.** The record prices several
  limits by name — the initials form outside G6, line-based derivation, the
  Amex 4-6-5 grouped spelling, issuer digits outside 2–6, hyphen-slugged
  addresses in filenames, the RFC 3849 prefix left fail-safe. My phase-1
  correctly raised none of these as findings; they are decided residue, not
  gaps.

### Divergences — what the ruling did not price

- **LK1 stands, severity unchanged (MODERATE, argues MAJOR).** The ruling's D1
  intent is *narrow* — "allow-markers exempt structural rules only", the
  GUARDS narrow/noisy/reasoned triad — and nothing in the sweep or the ruling
  contemplates the marker parser's failure mode. LK1 breaks the ruling's
  intent (a malformed scoped marker silently widens to all-structural) while
  honouring its letter (the term list still always runs — probed). The ruling
  did not price this shape; it remains new residue for the ruling round.
- **LK2 and LK3 stand.** G6 was ruled and funded as "separator variants",
  which the build implements exactly (`[\s._-]`); Unicode normalisation and
  the `/`/`+` separators sit outside what the ruling considered. Reach gaps
  beyond the ruling, not deviations from it.
- **The staged-plane G2 asymmetry is sharpened by the sweep's own frame.**
  The sweep's closing section ("Worth stating, not a defect") already holds
  the consequence that a term leak missed by the hook plane is never detected
  again by anything, because CI runs structural-only by design. My reach note
  is a concrete new instance inside that held frame: a rename-only or
  empty/binary add whose *name* carries a term passes the staged hot path,
  and the one plane that could catch the term never sees it. The sweep held
  the class in general; the delta's G2 build closed the tree plane but not
  this staged shape. This strengthens the case for promoting the reach note
  to a tracked finding; the disposition stays the principal's.

### Post-reconcile additions (from the record, verified before writing)

- **LK6 — note (post-reconcile).** The ruling record states "a path has no
  inline marker hatch — `.leakscanignore` is the only escape", and the code's
  `scan_path_name` docstring says the same. A phase-1 probe (run before the
  record was opened, omitted from the phase-1 write-up as contrived) falsifies
  the claim's letter: `scan_path_name` reuses `scan_text`, so a filename that
  itself contains marker text plus a reason self-exempts its own path
  findings. Accidental occurrence is vanishingly unlikely and an adversary is
  outside this tool's threat model, hence note severity — but the record's
  claim and the docstring are wrong as written, and a one-line fix (skip
  marker parsing on the path plane) would make them true.
- **G3 status flag (no LK id — a tracking question, not a code finding).** The
  ruling record shows G3 ruled BLOCKING (an unscannable or metadata-bearing
  binary blocks, one-time reasoned marker for legitimate images) yet outside
  this delta, per the build's own honest statement. Whether G3 remains queued
  as open work lives on surfaces barred to this review; the ruling round
  should confirm it is still tracked, because the staged-plane reach note
  above and G3 touch the same file class from different sides.

### Status after reconcile

No phase-1 finding changes status: LK1 MODERATE (argues MAJOR), LK2 minor,
LK3 minor, LK4 note, LK5 note, all as written. One post-reconcile addition:
LK6, note. Overall line unchanged — **PASS-WITH-FINDINGS**, now 6 findings
(0 MAJOR, 1 MODERATE, 2 minor, 3 note) plus the reach note, which the sweep's
own frame argues should be tracked. Verdict finalised.
