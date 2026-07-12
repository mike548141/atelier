# 2026-07-12 · session 49 — the reviewer-independence rule, drafted + cold-reviewed

Opus 4.8 (1m), resumed after a session limit. Mike asked what work remained;
after triage, the one agent-actionable open item was **REVIEW.md — encode
reviewer independence** (grounded 2026-07-12, the REACH case). Everything else in
the open queue awaits Mike's disposition (REACH A1–A8, session-38 join, signing
warn→block) or is a long-horizon north-star item.

## What was decided and done

**The rule, encoded in `method/REVIEW.md`** (`21b1524`). The REACH case (session
47) proved fresh context is necessary but not sufficient: a cold-context review
can still be *warm-questioned* — the author wrote its brief's attack questions,
every one aimed where the author was already looking; an un-briefed re-run found
eight findings, zero overlap, two MAJOR. Three edits:

1. New section *Independence is more than fresh context* — three rules that bind
   when the work's author commissions review of its own work: (1) the reviewer
   chooses its own attack surface, no author-seeded questions; (2) barred from
   prior reviews until its own verdict drafts; (3) findings on self-authored
   *doctrine* are the principal's disposition, not the author's.
2. Lifecycle step 1 (Brief) — author-commissioned exception: scope *what the work
   is* and stop.
3. Lifecycle step 4 (Disposition) — the `[rejected: grounds]` builder-overrule
   escape does not extend to doctrine the author itself wrote.

**Dogfooded.** The change is itself review-owed doctrine, so it was reviewed
*under the new rule*: an author-commissioned brief
(`reviews/2026-07-12-review-independence.md`) that scopes what-the-work-is and
seeds no attack questions; a cold background reviewer that chose its own surface;
and — as self-authored doctrine — a verdict that goes to Mike, not the author.

**Verdict: PASS-WITH-FINDINGS** (7 findings, 3 MAJOR / 3 MINOR / 1 NOTE). The
design ships — the insight is right, the mechanism (framing leaks through the
*ask*, not just the context) correctly named, the dogfood genuine. But three
MAJORs sit on the rule's own load-bearing axes:

- **I1** — the rule *overshoots its grounding*. REACH proposed the milder
  sufficient remedy (author questions as a *floor*, reviewer licensed to attack
  beyond them); REVIEW.md took the maximal "no author questions at all" without
  arguing the trade-off. Worse, the brief itself smuggled a verdict ("Grounded in
  the REACH case") — crossing the very steering line the rule forbids.
- **I2** — the *author≠principal* split the whole rule rests on is never defined
  and collapses in two real cases: a solo adopter who is both, and atelier's own
  convention where every commit is authored by Mike the principal (the disposition
  clause then names the same person on both sides).
- **I3** — the *doctrine-vs-code* line the carve-out rides is undefined and
  dodgeable: encode doctrine as a validator (which AUTONOMY actively tells the
  agent to do) and the author keeps the self-reject escape the rule meant to deny.

Plus I4–I7: rule-2 milestone mismatch (verdict-drafts vs findings-committed),
trigger over-generalises (rule 3 is doctrine-only; the mechanism is broader than
"the author writes the brief"), "proved" from n=1 (the exact defect REACH's own
A8 was docked for), and a PROPAGATION "resolved upward" vs "to the principal"
seam.

## The disposition point (Mike's, per the rule just written)

These findings are on **self-authored doctrine**, so — by the rule this session
encoded — the author records the verdict verbatim and applies **nothing** on its
own. I1–I7 await Mike's disposition, logged in the ROADMAP review-owed section.
Author's counsel on record: take I1–I5 + I7 (cheap, real seams; I2/I3 the two
that most need closing before this is cited as standalone), I6 a judgement call.

The rule fired on its very first use — and the strictest possible read (the
author holds off on its own doctrine findings) is exactly what it demanded of
itself.

## Owed / open

Unchanged from session 48's close, plus this session's addition:
- **REVIEW.md I1–I7 disposition** (new) — Mike's, then apply on his word.
- REACH re-review A1–A8 disposition; session-38 borderline join; signing
  warn→block flip (owner-debt-gated); the private-side rotations/checks.
