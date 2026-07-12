# Review brief — REVIEW.md reviewer-independence rule

**Author-commissioned.** Under the very rule under review, this brief scopes
*what the work is* and stops. It seeds no attack questions — the reviewer chooses
its own attack surface, names the load-bearing assumptions itself, and is barred
from no prior review here (there is none). Findings on this self-authored
doctrine are the principal's to disposition, not the author's.

## What the work is

`docs/method/REVIEW.md` gained a rule that fresh context is necessary but not
sufficient for an independent review. The change is three edits:

1. A new section, *Independence is more than fresh context*, between "Why review,
   and who reviews" and "What a review actually checks". It states three rules
   that bind when the work's author commissions the review of its own work:
   (1) the reviewer chooses its own attack surface, no author-seeded questions;
   (2) it is barred from prior reviews until its own verdict drafts;
   (3) findings on self-authored *doctrine* are dispositioned by the principal,
   not the author. Grounded in the REACH case (2026-07-12).

2. Lifecycle step 1 (Brief) gained an exception: when the work's author writes
   the brief, it scopes *what the work is* and stops.

3. Lifecycle step 4 (Disposition) gained a carve-out: the builder/owner's
   `[rejected: grounds]` escape does not extend to findings on doctrine the
   author itself wrote — those go to the principal.

The grounding is the session-47 REACH case: an author-briefed cold review passed
a doc clean on four pre-seeded questions; an un-briefed adversarial re-run found
eight findings, zero overlap, two MAJOR.

## Scope

The three edits above and their coherence with the rest of REVIEW.md. Nothing
else in `method/`.

---

<!-- reviewer's verdict appended below this divider -->

## Verdict: **PASS-WITH-FINDINGS**

**Reviewer:** fresh-context agent, 2026-07-12. Independence note: this brief
seeded no attack questions (per the rule under review), so the attack surface
below is my own; there is no prior review *of this change* to be anchored by. I
read the two REACH review files as the change's **grounding evidence** (the
brief cites them as the ground), not as prior verdicts on this work — rule 2 is
satisfied trivially here.

The core insight is right and well-grounded: *fresh context is necessary but not
sufficient*, and the mechanism — **framing leaks through the ask, not just
through the context** — is a genuine defect the REACH case exhibits cleanly
(eight findings, zero overlap, two MAJOR, on the axis the seeded questions
steered around). Encoding it as doctrine is correct, and erring strict matches
the house's "stricter/safer reading wins" instinct. I could not unseat the
section's spine.

But three **MAJOR** findings sit on the load-bearing axes the rule is built from
and never defines: it **overshoots its own grounding** (I1), its central
**author-vs-principal distinction is undefined and collapses in two real cases**
(I2), and the **"doctrine vs code" line the disposition carve-out rides is not a
clean cut** (I3) — and is dodgeable using a practice AUTONOMY actively
recommends. None unseats the design; all three should land before this is cited
as the standalone rule on review independence. The load-bearing assumptions I
attacked by name: (a) *author-seeded questions are pure contamination with zero
salvageable signal*; (b) *the author is always a different entity from the
principal*; (c) *"self-authored doctrine" is cleanly separable from code*. All
three are false or unstated as written.

## Findings

### I1 — MAJOR (approach): the rule overshoots its own grounding, and discards the author's legitimate signal without arguing why

The grounding document proposes the *milder* sufficient remedy. The REACH
re-review's transferable lesson (its closing paragraph): *"when the work is
doctrine, the brief's sharp questions should not **all** be authored by the
doctrine's author — **or at minimum** the reviewer must be licensed (as this
pass was) to choose its own attack surface **beyond** them."* Both halves keep
author questions and add reviewer freedom on top (a floor, not a fence).
REVIEW.md instead adopts the maximal cut — *"No author-seeded questions; the
brief scopes what the work is, not what to doubt about it"* — throwing away the
author's questions entirely.

The unnamed load-bearing assumption is that author-seeded questions are **pure
contamination with zero salvageable signal**. That is not obviously true: the
author knows where the hard trade-offs were and where the bodies are buried —
signal a cold reviewer must otherwise rediscover from scratch. The REACH failure
was that author questions were the *only* input and *bounded* the review; the
milder fix (keep them as a floor, license the reviewer past them) neutralises the
bounding without discarding the signal. The doctrine picks the stronger rule
without engaging the trade-off its own grounding case surfaced.

There is a second, subtler problem the maximal cut does not actually solve: the
line between *"scopes what the work is"* and *steering* is thin, and this very
brief crosses it — it states the change is *"Grounded in the REACH case"* as
settled scope, pre-empting the n=1 attack (see I6) that a reviewer might
otherwise mount. "Describe the work, don't seed questions" does not cleanly
exclude framing; a determined author steers through the description.

**Fix:** either (a) adopt the grounded milder rule — author questions permitted
as a **floor**, reviewer explicitly licensed to choose its own surface *beyond*
them and to treat the author's framing (including "what the work is") as itself
attackable; or (b) keep the maximal cut but *argue* why the author's seam-
knowledge is not worth preserving and add a guard that "what the work is" states
facts, not settled verdicts (e.g. "grounded in X" becomes "the author's claimed
grounding is X — test it").

### I2 — MAJOR (coherence/completeness): the author≠principal split is the load-bearing axis and is never defined; it collapses in two real cases

Rule 3 and the step-4 carve-out both route disposition *"to the principal, not
the author."* The entire independence gain rests on the author and the principal
being **distinct entities**. That precondition is never stated, and "principal"
is nowhere defined in `method/` (APEX only glosses it as "the human it serves").
The rule delivers independence only under the implicit atelier configuration:
author = the building **agent**, principal = a distinct **human**. It breaks in
two cases that are not edge cases:

1. **Single-operator adopter.** `method/` is shareable doctrine. A solo developer
   who adopts atelier, writes their own doctrine, *and is their own principal*
   satisfies "the principal dispositions" by dispositioning their own findings —
   rule 3 becomes vacuous and the independence silently dissolves. The rule fails
   **exactly where an adopter most needs to be warned**, and says nothing.

2. **atelier's own attribution convention.** By this repo's Git-identity rule <!-- leakscan:allow: quotes atelier's own published git-identity convention (ADR 0005 worked example); author's own attribution, not personal data -->
   every commit is authored `Mike Clements` — and Mike is the principal. The <!-- leakscan:allow: same author's-own-attribution convention as CLAUDE.md; public throughout the repo -->
   change under review is literally `author: Mike Clements <mike@cxi.nz>`. Read <!-- leakscan:allow: author's own published git identity (commit trailers, CLAUDE.md); ADR 0005 named worked example, not personal data -->

   against the commit record, *"findings are the principal's to disposition, not
   the author's"* names the same person on both sides. The intent (the **agent**
   that built the work cannot self-certify) is clear, but the doctrine's own
   words, applied against the repo's own authorship convention, do not carry it.

**Fix:** define both terms at first use — *author* = the agent (or party) that
produced the work; *principal* = the deciding human the agent serves — and state
explicitly that the rule presupposes they are distinct. Add the honest carve-out
for when they are **not**: when the author *is* the principal (solo operator, or
a human writing their own doctrine), rule 3 gives nothing and the only remaining
independence is the cold reviewer's own findings on the record — say so rather
than implying a separation that isn't there.

### I3 — MAJOR (definability): "self-authored doctrine vs code" is asserted as a clean cut but isn't — and the seam is dodgeable via a practice AUTONOMY recommends

The step-4 carve-out and rule 3 both hinge on a bright line: the `[rejected:
grounds]` escape stays *"sound for code, unsound when one agent both wrote the
doctrine and judges the challenge to it."* So **code** keeps the author's
self-reject escape; **doctrine** goes to the principal. Two problems:

- **The line is undefined.** Is an ADR doctrine? A `build/` standard? A review
  brief? The child `CLAUDE.md` inlined floor? The `method/` corpus is clearly
  doctrine and app source clearly code, but the middle is wide and the rule gives
  no test.

- **The house's own practice erases the line.** AUTONOMY's load-bearing corollary
  is *"Encode the policy, don't just remember it… move it into code/config/schema
  where every model hits it."* A validator, a schema, or a CI gate that **encodes
  doctrine** is code by file-type and doctrine by function. Under the carve-out as
  written, the same policy gets the author's self-reject escape when expressed as
  a validator and loses it when expressed as prose — so an author can **keep the
  escape by encoding its doctrine as code**, which is the very move AUTONOMY tells
  it to make. The rule can be satisfied to the letter while defeated in substance.

**Fix:** define "doctrine" for this rule by **function, not file type** — a rule
that governs future agent behaviour, wherever it lives (prose, ADR, schema,
validator, gate). If policy-as-code is meant to keep the [rejected] escape,
justify why a challenge to encoded policy is safe to self-reject when the same
challenge to prose policy is not; I do not think it is.

### I4 — MINOR (correctness/internal): rule 2's headline and its gloss set two different bars

The bold headline says *"Barred from prior reviews **until its own verdict
drafts**."* The gloss one line down says the reviewer *"reads it only after
**committing its own findings** — to reconcile, never to anchor."* "Verdict
drafts" and "findings committed" are different milestones — a reviewer commits
findings first, *then* drafts the verdict, and may revise the verdict on reading
the prior (the REACH re-review did exactly this: findings drafted, prior read,
"does reading it change my verdict? No"). As written the headline bars reading
until a later point than the gloss allows.

**Fix:** align the headline to the grounded milestone — *"Barred from prior
reviews until its own findings are committed"* — and let the verdict be the step
that may move on reconciliation.

### I5 — MINOR (scope): the trigger over-generalises rule 3, and under-scopes the actual mechanism

The section opens *"three rules bind when the work's author commissions the
review of its own work,"* but rule 3 only bites on **doctrine** — for an
author-commissioned *code* review, rule 3 does not apply. The umbrella trigger
claims all three bind when only two do.

Separately, the mechanism the section correctly identifies — *framing leaks
through the ask* — is **broader than "the author writes the brief."** Any
brief-writer who shares the target's blind spots reproduces it: a coordinating
agent that shepherded the work but didn't "author" it; or the author simply
**dictating the questions through a proxy** who types the brief. A rule scoped to
the literal author is trivially evadable by whoever holds the pen.

**Fix:** scope rules 1–2 to *"any brief written by, or on the framing of, the
party whose work is under review"* (not just the nominal author), and mark rule 3
as the doctrine-only sub-rule it is.

### I6 — NOTE (honesty/overclaim): "proved" from n=1 — the exact defect the grounding case flagged in itself

The section says the REACH case *"proved"* the gap and *"proved fresh context
alone doesn't deliver it"* (twice). One case is strong evidence, not proof — and
this is precisely the n=1 overclaim the grounding document flagged as a **defect
in REACH** (its own finding A8: *"generality overclaimed from n=1… the house rule
is stub-and-say-so, not round-up"*). The new section repeats, about its own
grounding, the error its grounding case was docked for. Under the apex (*"never a
claim stronger than its evidence"*) this should read *"demonstrated in one
case"* / *"showed,"* not *"proved."*

**Fix:** soften both instances; optionally add the honest note that this is
generalised from a single case and untested beyond it — the same clause REACH's
A8 fix added.

### I7 — MINOR (coherence): two unreconciled resolution paths for "a doctrine finding the author can't self-reject"

The new carve-out routes such findings *"to the principal."* PROPAGATION's
layer-override rule already routes doctrine conflicts a different way: *"resolved
upward… the stricter/safer reading wins until the conflict is resolved upward…
children point up."* For a **child repo**, "upward" is the parent doctrine
(atelier), which is not the same address as "the principal" (the human). A reader
holding both docs gets two different destinations for the same class of
unresolved doctrine finding.

**Fix:** one clause reconciling them — e.g. the principal dispositions the
*verdict*, and where the finding is a parent/child doctrine conflict the
resolution still flows upward per PROPAGATION; the two are the same act seen from
governance vs. layering, not rival routes.

## Follow-up checklist

- [x] I1 — reconcile the rule with its grounding: adopt the milder "author
      questions as a floor + reviewer licensed beyond them," or argue the maximal
      cut and guard "what the work is" against smuggled verdicts
- [x] I2 — define author and principal; state the distinct-entities precondition;
      add the honest carve-out for when author *is* principal
- [x] I3 — define "doctrine" by function not file-type; close the policy-as-code
      escape hatch
- [x] I4 — align rule 2's headline to "findings committed"
- [x] I5 — rescope the trigger (brief-writer, not nominal author; rule 3 is
      doctrine-only)
- [x] I6 — soften "proved" to match the evidence; optional n=1 honesty clause
- [x] I7 — reconcile "to the principal" with PROPAGATION's "resolved upward"

## Close

The design is sound and ships as doctrine: the fresh-context-is-not-sufficient
insight is real, the framing-leaks-through-the-ask mechanism is correctly named,
and the dogfooding (this brief seeds no questions) is genuine. None of I1–I7
unseats it. But I1–I3 are three MAJORs on the rule's own load-bearing axes — it
is stronger than its grounding warrants, its author/principal distinction is
undefined and collapses for solo adopters and under this repo's own commit
attribution, and its doctrine/code line is neither defined nor dodge-proof.
Until those land, this should not be cited as the standalone authority on review
independence. Findings go to the principal (Mike) for disposition; per the rule
under review, the author records this verbatim and applies nothing on its own.

---

## Disposition (2026-07-13, Mike — the principal)

All seven **[fixed]**, batched with F1–F7 of
`2026-07-13-review-doctrine-second-pass.md`, applied by a session that authored
neither the doctrine nor this verdict.

- **I1 [fixed — with the principal's own strengthening]:** Mike chose the
  floor-not-fence model and added a clause neither review proposed: seeded
  questions influence *by their very existence* — topic and tone suggest where
  "the risk" lives — so the reviewer chooses its own surface before weighing
  the author's list. Encoded in rule 1 and lifecycle step 1.
- **I2–I5, I7 [fixed]** as recommended: author/principal defined with the
  distinct-entities precondition and the solo-operator gap stated (I2);
  doctrine defined by function, policy-as-code escape closed (I3); rule-2
  milestone aligned to findings-committed (I4); trigger rescoped to
  brief-carries-the-author's-framing, rule 3 marked doctrine-only (I5);
  to-the-principal and resolved-upward reconciled as one act in step 4 (I7).
- **I6 [fixed]:** "proved" softened; treated as apex-required, not optional —
  extended by F3's uncontrolled-n=1 clause and standing test.
