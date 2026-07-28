# Review brief — the estate-root naming rule, widened (rule-4 cold pass)

- **Date:** 2026-07-28 1216 UTC
- **Reviewer tier / spawn provenance:** Fable; the Mike-spawned "do any
  review work" session that closed the TA and C1 passes earlier the same
  day. It authored none of this delta — not the widening (`0810efe`), not
  the pre-landing corrections (`bd16d1c`) — and was not spawned by the
  authoring session. Claim `2b6f57b` on main.

## What the work is (refs only)

The `PROPAGATION.md` estate-resources paragraph, widened to bind the
estate-root naming rule to the **property** (public) rather than to
categories of repo. Delta: the paragraph as landed across `0810efe` and
`bd16d1c`. Intent record (deferred): the 2026-07-28 addendum on
[`2026-07-27-2301-track-a-fail-opens`](../sessions/2026-07-27-2301-track-a-fail-opens.md).
Named exposure: both commit messages, which carry the authoring and
pre-landing-review framing — claims to test, not settled scope. This pass
is the queued post-landing rule-4 review; the pre-landing pass was a
different reviewer's and its corrections are part of the delta under test.

## Scope — four lenses

Attack the widened rule's edges (does "bind the property" actually close
the class, including at a property *flip*); re-run every figure in the
paragraph independently (the counts are the paragraph's evidence, and this
programme's figures have been wrong in both directions); verify the
forward-only rule has held since landing; verify the paragraph itself, and
everything written since, withholds the name. Security lens: this delta
*is* the security lens — the check is whether the withholding posture is
coherent and whether the text leaks by structure what it withholds by
name. `/security-review` discharged: landed markdown-only delta, outside
the scanner's file class and with nothing in flight.

---

# Verdict — PASS-WITH-FINDINGS (0 MAJOR / 1 minor / 2 notes)

Committed before the intent-record addendum was opened; reconcile below.
Provenance as in the brief, repeated per rule 4: non-author taker session,
not spawned by the authoring session.

## Re-run and verified

- **The counts reproduce exactly** on an independent word-boundary sweep
  at `bd16d1c`: **63 mentions across 19 files**; **19** in the three
  current-truth records; the earlier "eight places" was indeed a ~8x
  undercount. One figure reproduces only approximately: "**10** of those
  lines sit beside what it holds" comes out at 8–9 depending on which
  co-occurrence nouns the net includes — the rhetorical point (the name
  repeatedly sits beside sensitive nouns) holds; the precise integer is
  net-dependent and the paragraph states it as fact.
- **Zero ordinary-English-word occurrences confirmed** by eyeballing all
  match contexts: every one is a repo reference (possessives, paths,
  session titles) — the C5 premise-correction is real, and a naive
  substring sweep (which returns 471 by matching inside "pushed",
  "finished", "published") is exactly the cry-wolf shape C5's original
  premise feared; the word-boundary form is not.
- **Forward-only has held**: zero new mentions in lines added since
  `bd16d1c`, including the three review-cycle closes this session pushed.
- **The paragraph withholds what it claims to withhold**: it names the
  root's existence and posture, never its name; the B1 unblocking text
  upstream does the same.

## Findings

**ER1 (minor — lens 1, the widening's own lesson one step further): the
rule says nothing at the property flip.** A private child's onramp names
the estate root *by design* ("named only in a private child's own
onramp"), and making a private repo public is already on the always-stop
floor — but neither the floor's wording nor this paragraph connects them:
nothing says the making-public confirmation includes scrubbing the
estate-root name first. At the flip, the mentions are not yet published,
so a pre-flip scrub buys back everything — the opposite economics of the
forward-only case — and the repo class most likely to flip (a child being
open-sourced) is the class the rule *instructs* to carry the name. Bind
the property, and the property can change: the flip is where this rule
will next break. Remedy shape: one line in the always-stop floor's
making-public entry naming the scrub as part of the confirmation.

**ER2 (note — lens 3): the "local-path convention" is pointed at but
defined nowhere.** Both the floor block and the paragraph tell a public
tree to reference the root "by local-path convention", but no text —
public or pointed-to — says where that convention is written down. For
this estate it is carried in session memory and private onramps; an
adopter reading only the public doctrine cannot discharge the rule. One
sentence saying where the convention lives (each estate defines it in its
private root's onramp) closes it without naming anything.

**ER3 (note — lens 2): the "10 lines" figure is stated as fact but is
net-dependent** (8–9 under reasonable co-occurrence sets). Immaterial to
any ruling — recorded because this programme's history is precisely that
unverifiable-as-stated figures decay into wrong ones, and this one was
minted in the same commit that corrected an 8x undercount.

## Verdict

The widening is sound, its self-corrections are honest and re-verified,
and the rule has held in the days since it landed. The one substantive
finding is the flip gap (ER1) — the same class of hole the widening
closed, one transition further on. **Cycle closes** (0 MAJOR, terminal
rule); ER1–ER3 to Mike.

---

## Reconcile (verdict committed first; the intent-record addendum now open)

**The intent record reconciles clean.** The 2026-07-28 SESSIONS.md
addendum entry tells the same story the paragraph and both commit
messages tell, with the pre-landing pass's three corrections carried
honestly (the 8→63 undercount stamped, not swapped; the C5 premise
correction; the widened rule broken by its own widening commit, recorded
as evidence for C5). Every figure it states reproduced under this pass's
independent sweep except the net-dependent "10" (ER3, unchanged).

**ER4 (note, new at reconcile — pointer precision):** the queue pointer
and the addendum's own link name
`sessions/2026-07-27-2301-track-a-fail-opens.md` as the intent record's
home, but that file contains no addendum — the record is the SESSIONS.md
*entry* itself. A taker meeting the pointer cold greps the named file and
finds nothing (this one did). Cheap fix: pointers to addendum-entries say
"the SESSIONS.md entry of <date>" rather than linking the file the entry
extends.

**ER1, ER2 stand** — the addendum, like the paragraph, is silent at the
private→public flip and does not say where the local-path convention
lives.

**Verdict after reconcile: unchanged — PASS-WITH-FINDINGS, 0 MAJOR /
1 minor / 3 notes (ER4 added at reconcile). The cycle CLOSES** (no-MAJOR
terminal rule); ER1–ER4 decided into the backlog for Mike.
