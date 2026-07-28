# Review brief — the TA1–TA9 application (rule-4 cold pass)

- **Date:** 2026-07-28 1136 UTC
- **Reviewer tier:** Fable (matches the queue's stated tier)
- **Spawn provenance:** taken from the ROADMAP `⏳` queue by a session Mike
  opened with "Please do any review work" — the rule-4 worked example. The
  session authored none of the TA chain: not the Track A application, not the
  prior cold pass, not this application. The applier session did not spawn
  this review. Claim commit `d930d7b` on main.

## What the work is (refs only, from the queue pointer)

The application of the TA1–TA9 rulings from the Track A application cold
pass. The reviewed cycle carried a MAJOR, so the cycle is open and this
application earns its own pass; `docs/method/REVIEW.md` was edited in the
delta, which is self-authored doctrine (rule 3/4 territory — findings on it
are Mike's to decide).

**Delta under review:** commits `3fb6437`, `321bbd3`, `0ca4b75`, `d80f9d8`,
`f204fba`, and the queue commit `f3a3cd4`. Files: `tools/floor.py`,
`tools/floorfleet.py`, `tools/test_floor.py`, `tools/test_floorfleet.py`,
`tools/test_precommit.py`, `docs/method/REVIEW.md`,
`docs/sessions/2026-07-27-2301-track-a-fail-opens.md`, plus `f3a3cd4`'s
records hunks.

**Context at HEAD:** a later commit (`549930b`, C1 phase 1) touched the same
enforcement files and carries its own queued `⏳`. This review examines the TA
delta's diffs and current behaviour at HEAD; defects introduced by the C1
delta belong to that review, but any interaction between the two is in scope
here.

## Sequence and deferred material

Per REVIEW.md's application-review sequence: the reviewer meets the work
cold, commits its own findings first, and only then opens the deferred
material to reconcile. Deferred until findings are committed:

- the intent record
  [`2026-07-28-0214-ta-findings-application`](../sessions/2026-07-28-0214-ta-findings-application.md)
- the prior verdict
  [`2026-07-28-0123-track-a-application-cold`](2026-07-28-0123-track-a-application-cold.md)
  and any decision stamps on it
- the evaluative harvest hunks in `f3a3cd4` (`ROADMAP-DONE.md` and the
  intent record's content)

The residual exposure of an application review — commit messages carry the
finding IDs and one-line ruling summaries, so some framing leaks through the
delta itself — is named here, not denied.

## Scope — widest the work admits, four lenses

1. **Approach & assumptions** — are these the right fixes for what the
   commit subjects claim to fix? Attack the load-bearing assumptions in the
   new guard/cover/estate-discovery logic on their own merits.
2. **Correctness & quality** — do the diffs do what their messages claim; is
   anything overclaimed or silently narrowed; are the tests real tests
   (wrong tests verify nothing).
3. **Completeness / harvest** — what the application should have covered and
   didn't; whether the queue pointer's delta list is complete (AW6);
   whether landing = queuing held (AWA2/TA9 — the pointer commit is 6
   minutes after `f204fba`).
4. **Security & privacy** — the delta edits the security floor's enforcement
   plane (`floor.py`, `floorfleet.py`): scope-widening, path handling,
   worktree discovery, YAML reading are all attack surface. `/security-review`
   reach: this is a landed-delta review with no pending diff, so the scanner
   cannot be aimed at the work; discharged on those grounds — the mechanical
   floor here is the repo's own scan suite plus the test suites, re-run live.

**Live proofs to re-run:** the full test suites (`test_floor.py`,
`test_floorfleet.py`, `test_precommit.py`, and the rest of `tools/` +
`instruments/`), the pre-commit floor scan, and the specific probes the
commit messages claim (scope-path guard, shrunken-cover labelling, worktree
estate discovery) — exercised at HEAD, red legs where reconstructible.

**Non-goals:** the C1 delta's own merits (its queued review covers it); the
prior cycle's un-appealed rulings themselves (Mike's decisions are not
re-litigated — what is reviewable is whether the application implemented
them faithfully, which is reconcile-step work).

---

# Verdict — PASS-WITH-FINDINGS (0 MAJOR / 1 minor / 3 notes)

- **Date:** 2026-07-28, verdict committed before any deferred material was
  opened (intent record, prior verdict, and `f3a3cd4`'s harvest hunks all
  unread at this point; a reconcile addendum follows below).
- **Provenance, repeated per rule 4:** reviewer is a Mike-spawned "do any
  review work" session on Fable, author of nothing in the TA chain; the
  applier did not spawn this review. Claim `d930d7b`.
- **Terminal per the close rule:** no MAJOR finding, so the Track A review
  cycle **closes** with this pass. The findings below are decided into the
  backlog — the decisions are Mike's (the delta is enforcement code and
  self-authored doctrine; rule 3 applies).

## What was re-run, and what it proved

Every live claim in the delta's commit messages was re-exercised, not read:

- **Suites:** 759 tools tests + 207 instruments tests green at HEAD; 733
  green re-run at `d80f9d8` in a detached worktree, matching that commit's
  claimed count exactly. (A first re-run from a bare `git archive` failed on
  39 errors — environmental, no `.git` context; stated so the record shows
  the false leg was the probe's, not the work's.)
- **TA1 red legs, both members:** `{"scope": {"secretscan": ["/etc"]}}`
  exits 0 at `3fb6437` (pre-fix) and 1 at HEAD with the parse-time message;
  a relative in-tree symlink pointing outside exits 0 at `3fb6437` and 1 at
  HEAD with the run-guard message. The defect and both shut doors reproduce.
- **TA5 red leg:** `evaluate_parent` over a fixture whose only floor line is
  commented out classifies `wired` at `d80f9d8^` and `absent` at HEAD.
- **TA6:** importing `test_precommit` at HEAD creates no temp artefact.
- **TA7 live leg:** `floorfleet` run from *this* review's worktree renders
  the parent row labelled `atelier (parent)` plus 13 children, all wired —
  the exact claim in `d80f9d8`.
- **Blast radius (`321bbd3`):** re-measured against the live estate — 14
  configs, 2 declaring `scope`, 4 unique declared paths, all relative and
  in-tree. Exact match, which matters on a programme whose figures have been
  wrong in both directions before.
- **TA9 self-compliance:** push telemetry shows the pointer commit
  `f3a3cd4` left in the same push as the four work commits (02:17:13Z), so
  the grammar the delta wrote ("never in a follow-up push") was met by the
  delta itself. `3fb6437` was pushed alone at 01:54Z, before TA1's ruling,
  consistent with its honesty-repair framing.
- **Floor:** the pre-commit scan ran green on this review's own commits.
- `/security-review` discharge: landed-delta review, no pending diff the
  scanner can be aimed at; the mechanical floor here is the scan suite and
  the test suites above (grounds per the brief).

## Lens findings

**TAA1 (minor — correctness/honesty, lens 2).** `321bbd3` shut both
outside-the-repo members of the scope class but the series landed without
updating the class-members comment `3fb6437` had written a few lines below,
which continued to assert both members "(open)" and "TA1; awaiting a
ruling" through `f204fba`/`f3a3cd4` — the landed state under review claimed
two fail-opens were open after its own earlier commit had shut them. An
out-of-delta commit (`549930b`) later appended a correcting tail, but only
the tail: at HEAD the same paragraph still labels the two members "(open —
`/etc` and `..` both pass `.exists()` …)" and then says "both the
outside-the-repo members are shut above". A comment in the enforcement
plane asserting a fail-open exists where none does is the same record-drift
class TA8 fixes, in the opposite direction. Remedy: a two-line comment edit
re-labelling the members shut, with the TA1 pointer kept.

**TAA2 (note — completeness, lens 3).** The TA3 note shares `Result.partial`
with the TA4 cover note via `elif`, so a scanner with its full-cover flag
absent *and* scope paths missing would report only the cover note — the
scope-drift signal this fix exists to surface would be silently dropped.
Unreachable today: the only scanner with a `full_cover_flag` has no
advisory form, so its missing scope blocks at the guard first. But nothing
pins that invariant; a future softenable scanner with a cover flag re-opens
a silent-shrink hole inside the fix for one. A joined note, or a comment
naming the invariant, closes it.

**TAA3 (note — doctrine grammar, lens 1; decision Mike's).** After the TA
pointer was queued, `549930b` touched four of its delta files and did not
widen the TA delta list — it queued its *own* `⏳` over the same files
instead. Coverage is complete across the two open reviews, but AW6's
grammar ("a later commit that touches a queued delta's doctrine surfaces
widens the pointer's delta list") does not say whether a second queued
pointer discharges the widening duty. Same shape as the gap TA9 closed for
"the same commit". Worth a one-line grammar clarification if a third case
appears; recorded here as the second.

**TAA4 (observation — positive).** The delta's guards fail in the safe
direction throughout: the comment-stripping lexer can only *remove* text,
so it can lose a match (false `absent`, a red the operator investigates)
but cannot manufacture one (false `wired`, a green that hides a dropped
floor); `_inside` resolves both sides and returns not-inside on `OSError`/
`ValueError`; the outside-guard's hardcoded `enforced`-on-block follows the
existing "scanner missing" idiom for hard config failures. No security
finding; the lens ran at both altitudes over the guard code, path handling,
and the fixture git usage.

## Verdict

The nine rulings were applied faithfully on the evidence available cold:
every mechanical claim re-ran true, the tests pin both the defect and the
over-correction directions, and the one substantive lapse (TAA1) is the
delta failing its own honesty bar in a comment, not in behaviour. Cycle
closed; TAA1–TAA3 to Mike.

---

## Reconcile (written after the verdict above was committed; the intent
## record, the prior verdict, and the harvest hunks now opened)

**Ruling faithfulness, verified per ruling.** Mike's rulings were TA1 →
(a) and TA2–TA9 → fix all eight. TA1's application matches counsel (a) in
full — lexical refusal at parse plus resolved containment where the path
exists — and the one extension beyond the ruling's letter (`local.*.scope`
held to the same rule) is named as a widening *inside* the ruled class in
the code, the intent record, and the harvest; the "named, not hidden"
discipline held. TA4's fixed-at-the-claim-not-the-mechanism limit is
likewise stated in all three places rather than rounded up. TA2, TA3, TA5,
TA6, TA7 match their rulings as re-proven above; TA8's grounding checks
out — the ADR 0008 verdict grades EP2 **MAJOR** and its reconcile narrowed
blame, not grade, so the restored wording is correct; TA9's grammar is in
REVIEW.md as the intent record describes, and this series obeyed it.

**The environment claim, completed.** The intent record claims both suites
green with the term list present *and* absent. The cold pass above re-ran
only the present leg; re-run absent (`HOME` redirected, the env var
cleared): 759 green at HEAD. The claim reproduces both ways.

**Findings, reconciled — nothing overturned:**

- **TAA1 stands, sharpened.** The intent record closes with "Open from
  this session: nothing", and neither it nor the harvest mentions the
  class-members comment `321bbd3` left claiming two shut members open and
  "awaiting a ruling" that had been made. The prior verdict's TA1 had
  called out that comment's *overclaim* ("the rest of that class"); the
  application corrected it into an underclaim and then out-dated it in the
  same series. Same comment, third state, still not true at landing.
- **TAA2 stands** as a latent-interaction note; no ruling constrains the
  `elif` shape, so it contradicts nothing.
- **TAA3 stands**, and the prior verdict's TA9 is its sibling: TA9 fixed
  the "which commit" gap in AWA2's grammar, TAA3 records the "which
  pointer widens" gap. This is the second case; a third earns the
  one-line clarification.
- **TAA4 unchanged.**

The intent record's blast-radius table matches my independent re-measure
row for row (14 / 2 / 4-unique / 0 failing). Its probe table reproduced in
full under this pass's re-runs.

**Verdict after reconcile: unchanged — PASS-WITH-FINDINGS, 0 MAJOR /
1 minor / 3 notes. The Track A review cycle CLOSES** (no-MAJOR terminal
rule; this pass reviewed the application of a MAJOR-carrying pass's
rulings, and none of its own findings reach MAJOR). TAA1–TAA3 are decided
into the backlog for Mike; per the terminal rule this close spawns no
further ceremony.
