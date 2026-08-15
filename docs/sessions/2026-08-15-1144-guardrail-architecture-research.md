# Guardrail architecture — narrow guards, or one broad guard? (2026-08-15, 1144 UTC)

**Session:** Opus, worktree `guardrail-architecture-0815`.
**Shape:** research commissioned by Mike, run as a six-agent fan-out, landed as a
board section. No doctrine edited; every recommendation is queued, and the two
decisions the research surfaced are left as Mike's.

## What was asked

Mike commissioned it in his own words, kept verbatim in the section README
because the scope is exactly the kind a paraphrase narrows. The short form: what
guardrails can and should atelier build for itself and its children, and is the
fleet of narrowly scoped guards the right approach or should there be a broader
provenance check? His stated worry was that `datescan` could come to be read as
*a date must exist and be formatted a certain way*, and so force unintended
outcomes, miss the intended one, or cause damage.

## How it ran

Six agents. A rule-by-rule inventory of every guard, classified by whether each
rule checks syntax, presence, meaning or a relation. A verbatim recovery of
Mike's stated intent on the time dimension and on provenance, mined across every
repo's transcripts with `cctranscript`. External prior art. A case-file of every
recorded instance in this estate of a guard enforcing its letter and missing its
point. A doctrine-enforcement census. Two of the six spawned their own sweeps,
which is where the deepest material came from — roughly sixty dated divergence
incidents, against the seventeen the first pass had found.

## What it found

**The premise is confirmed, on the exact guard Mike named.** The 2026-07-23
`datescan` cold pass had already recorded it: well-built, aimed slightly off the
mistake that actually cost the sweep that grounded it.

**The example points at a different tool than the worry needs.** `datescan`
enforces `EVIDENCE.md` §7 over prose — state time absolutely — and never checks
that a date exists. `PRINCIPLES.md` §9, the rule that data carries the time
dimension its domain implies, has no guard anywhere in the estate. The gap is
total rather than a drift.

**The predicate is not narrowness.** Every serious divergence has one shape: the
fact that would license the exception sits outside the guard's evidence window.
No time axis, so records naming historical paths can never come clean. A window
of one document against a reader with years of context. A term list that cannot
say *public in this repo*. A parser that cannot tell a doc describing its syntax
from one using it. Syntax and presence checks drift at the same rate; the window
explains the variance. A second pattern is as clean — guards over machine-shaped
input barely drift, guards over prose drift constantly.

**So broadening would make it worse.** Same window, wider intent, and one
suppression then silences the whole concern. The external precedent is
unanimous in the other direction: consolidate engines, keep rules granular and
separately suppressible.

**And Mike had already ruled the shape of the answer**, on 2026-07-19 — fix the
source upstream rather than accumulating downstream mitigations — with the test
attached: a fix is downstream when it must be applied in several places and the
next will cost as many again. Ten to eleven copies of one loader, fourteen regex
sites to correct it once, is that signature exactly.

## Live defects surfaced

- **`stampscan`'s verdicts are inverted against the doctrine it enforces.** The
  doctrine permits compression and forbids narrowing; the scanner reds a
  compressed restatement and passes a declared narrowing, under the parent's own
  word for *stricter*. Found by the 2026-07-26 pass that was rejected in full on
  tier grounds, and **never re-found** by the accepted pass — verified by search.
- **The withdrawn-review convention's premise now has a counterexample.** It
  rests on real findings being re-found independently. This one was not.
- **A coined paraphrase is still cited on the board as a child repo's quoted
  words**, one citation live at head. Named by a cold pass on 2026-08-09,
  awaiting the ruling round.
- **A real credential in an exempt fixture file is invisible to the floor**, and
  the 2026-07-28 near-miss proves it. The exemptions are correct; the residual
  is that nothing inside an exempt file separates fictional from real.
- **`plainscan` has no allow-marker grammar at all** — found while writing this
  section, when two verbatim quotes from Mike could not be exempted from its
  long-sentence rule. Left standing rather than reworded.

## What landed

A new board section, `115-guardrail-architecture-mike-commissioned`, with nine
items: two decisions that are Mike's, four defects, three builds. Two findings
were deliberately **not** filed because they already have carriers — the
enforcement-ladder floor question and expiry-at-every-granularity — and are
pointed at rather than restated.

Index rebuilt in the same commit. Floor green on the ci plane, exit 0, with the
expected advisory tier on the two boundary scanners.

## Concurrency

A parallel session was live throughout, running cold review passes in its own
worktree with a dirty tree. Head moved under this session more than once, and
the line references given mid-session were against trees that had already moved
— re-verified at head before anything was written. No git write touched the
shared checkout; explicit-path staging throughout; no `git add -A`.

## What it did not do

No doctrine file was edited. No scanner was changed. The evidence-window rule is
proposed, not minted — it is a `GUARDS.md` addition and therefore Mike's, and it
would carry a rule-4 pointer when it lands.
