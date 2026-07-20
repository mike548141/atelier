# Cold pass — session-onramp operating-rhythm (deltas `674b70b`, `c25b8a4`)

- **Date/time**: 2026-07-20 1415 UTC (brief; claim stamped 1355)
- **Spawn provenance (rule 4)**: same taker as the sibling passes this
  session — Mike-spawned ("do any reviews waiting"), claim on `main`
  (`69b8de0`) before the worktree. This session authored none of the delta,
  the three method docs it edits, the block cue, or the authoring session's
  records. Taker-written brief.
- **Named exposure**: the ROADMAP `⏳` entry (author's evaluative account —
  "a reach gap, not a content gap", the quoted cue text, and the Watch seed
  on whether the cue earns its lines); `674b70b`'s commit message;
  `c25b8a4`'s subject line. Additionally this taker has just completed the
  concurrency-flip pass, which read `PROPAGATION.md`'s block and the template
  copy — the subject files of this pass — and recorded a finding (CF4)
  touching the same block. That is cross-pass context, named here; the risk
  runs toward *this* pass anchoring on its own prior findings, and is
  handled by attacking this delta on its own terms first.
- **Deferred material (opened only after findings are committed)**: the
  intent record `sessions/2026-07-20-1302-session-onramp-operating-rhythm.md`
  (the author's list of Mike's ~7 candidate instructions and the account of
  what was folded/dropped); the ROADMAP entry's *review:* paragraph.

## What the work is (refs only)

Commits `674b70b` and `c25b8a4`. In-scope files at HEAD:
`docs/method/CONCURRENCY.md` (§ Claiming work — claim-outranks-instruction),
`docs/method/MODEL-ECONOMICS.md` (session-hygiene item 7),
`docs/method/RECORD.md` (close/all-clear sharpening),
`docs/method/PROPAGATION.md` (child block — Session rhythm cue),
`docs/build/templates/CLAUDE.md` (the block's template copy), plus whatever
else those commits touched (to be enumerated from the diffs).

## Lenses and the taker's attack surface

Lens 1 — approach & assumptions (named first, taker's own):

- **A1 — "a reach gap, not a content gap" is the load-bearing reframe.** Yet
  the delta *writes new doctrine text* into three method docs. Test each
  edit: extraction of already-decided practice (the claim), or invention
  wearing extraction's label? The ground-everything rule turns on this.
- **A2 — every cue clause must have a home it points up to.** The cue's
  design is "points up for the full rule". Test each clause for a real,
  findable home at HEAD — a clause with no home breaks the design and
  becomes the block's only copy of a rule (un-propagatable, un-reviewable
  upstream). Suspect: "stay in the lane you were given" carries no
  parenthetical pointer.
- **A3 — compression must not widen the rule.** "Claim work before starting
  it" drops § Claiming work's qualifier (claiming keys on *selection from
  the shared queue*). Does the compressed form tax directly-assigned work
  with a claim it doesn't owe, or contradict the source?
- **A4 — the block's size discipline.** The block is spec'd lean; the cue
  adds lines to every child's always-loaded onramp. Where is the size spec,
  what does the block measure now, and does the cue pay its way against it?
- **A5 — two copies must not drift at birth.** The cue lands in
  `PROPAGATION.md` (canonical) and `build/templates/CLAUDE.md` (copy).
  Byte-compare them; a birth drift is a finding.

Lens 2 — correctness & quality: read all three method-doc edits at HEAD for
contradiction with their surrounding sections; re-run whatever mechanical
proofs the delta's records claim (test suite, sizescan — `c25b8a4` mentions a
size-signal rebalance).

Lens 3 — completeness / harvest: the delta claims ~7 candidate instructions
distilled to a cue of 4 clauses + 3 doc edits, with one candidate dropped as
ungrounded. After findings are committed, reconcile the deferred list against
what landed — anything silently dropped beyond the named one is a finding.

---

# Verdict — findings (committed before the intent record was opened)

**Provenance repeated (rule 4):** the taker named in the brief; author of
none of the delta. The intent record
(`sessions/2026-07-20-1302-session-onramp-operating-rhythm.md`) remains
unopened at this commit; reconcile follows in a separate commit after it is
read.

## Lens 1 — approach

**The reach reframe is sound, and the ordering was right.** The delta
authored the home rules first (three method docs, each stamped with its
2026-07-20 grounding) and then made the cue *point up* — mechanism-before-
content respected, no rule invented to fill a heading. The claim-outranks
rule is a genuine sharpening (the yield moved one step earlier than the
rejected-push, onto a marker the instruction predates); item 7 and the
all-clear sharpening both read as extraction of Mike's repeated instructions,
not invention. One clause breaks the pattern — SR1.

## Findings

- **SR1 (MEDIUM, lens 1/2 — a cue clause with no home).** "Stay in the lane
  you were given" is the only cue clause with no parenthetical pointer — and
  nothing to point to: no method doc at HEAD states a lane/boundary rule
  (swept `method/*`; every "lane" hit is DATA-PROTECTION's unrelated
  "slow lane" or "plane"). The commit message confirms it: "focus on given
  work" was *folded into the cue*, not authored into a home doc. So the
  block — a compression layer whose own label says "points up for the full
  rule" — is now the **canonical and only** home of a rule, which makes that
  rule un-reviewable and un-propagatable upstream, and quietly falsifies the
  "6 of 7 already grounded" reframe for this clause. The practice *is* real
  (the 2026-07-20 cmd-Q recovery honoured the ros/atelier boundary and even
  cited "per CONCURRENCY" — a citation to a rule that doesn't exist as
  written). *Taker's counsel: author the lane rule properly — a short
  passage in `CONCURRENCY.md` (it already owns claim-boundaries and the
  repo-boundary bearings) — and give the clause its pointer; or drop the
  clause until the rule exists.*
- **SR2 (MEDIUM, lens 2 — the block's size spec is dead text).** 
  `PROPAGATION.md` instructs "keep it under **~15 lines of substance**"; the
  fenced block measures **48 lines** at HEAD (~41 before this cue). The spec
  was already broken before this delta; the cue added seven more lines
  against a spec it visibly exceeds threefold, with the contradiction
  unacknowledged in the doc itself (the ROADMAP Watch names it, the doc does
  not). Per the ground-numeric-limits rule this resolves one of two ways —
  re-ground the spec in the block's class (it is the hottest path in the
  fleet: every child session, every open — exactly the size×read-frequency
  frame the new rebalance item establishes) or shrink the block to spec.
  Leaving a spec every reading contradicts trains readers to ignore specs.
  *Taker's counsel: fold the block-spec re-grounding into the size-signal
  rebalance item's scope, and meanwhile fix the number to what the block's
  class honestly needs.*
- **SR3 (LOW, lens 2 — compression widens the rule).** "Claim work before
  starting it" drops the source's qualifier — claiming keys on *selection
  from the shared queue* (`CONCURRENCY.md`). As written the cue taxes
  directly-assigned, non-queue work with a claim it doesn't owe. Five words
  ("work you take off the shared queue") close it; the adjacent pointer
  mitigates but the block is what children actually read every session.
- **SR4 (LOW, lens 2 — vocabulary).** "Before your final verdict" imports
  review vocabulary into a general-session cue; `RECORD.md`'s own terms are
  the close of a *sequence* and the all-clear. A child session not running a
  review may not recognise itself in "verdict". *Counsel: "before you
  declare the work wrapped".*

## Lens 2/3 — verifications run clean

- **Cue parity**: the `PROPAGATION.md` and template copies byte-match, and
  parity is *mechanically enforced* — `test_templates.py` extracts the fenced
  canonical block and compares the stamped copy; suite re-run: 20 OK.
- **Sizescan red**: re-run at HEAD — exactly one gated red, `ROADMAP.md` 411
  (budget 300), matching the author's "deliberately left red, not hacked"
  account. Honest handling confirmed (the exemption mechanisms existed and
  were not abused to green the build).
- **Item 7 ↔ item 1**: the "one task per session, seen from the overload
  side" citation matches item 1's actual sharpened wording — no misquote.
- **The size-signal rebalance item** carries its own `*review: WARRANTED…*`
  line — compliant with the 07-18 "omission is the bug" remedy, and its
  direction (hot-path metering) is the frame SR2 wants to borrow.
- **The decoupling** (`c25b8a4` reversing `674b70b`'s one-coordinated-edit
  sequencing) left the concurrency-flip block catch-up with no vehicle —
  recorded as the sibling pass's CF4 (homeless propagation half); noted
  here for the cross-reference, not double-counted.
