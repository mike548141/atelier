# 2026-08-09 · 0708 UTC · The C5 cold pass, and the `add -A` sweep that was owed (Opus orchestrating, one Fable reviewer)

Mike opened with *"Give me a full list of work to do in this repo"*, then —
reading the list back — sent the ask this session is really about:

> I want a cold fable review of C5, I'm not sure I trust the findings of the
> session that decided that

Two pieces of work came out of it, plus one board sweep that answered a
question the roadmap had left open at its last close.

## The full list

112 open items and 7 queued reviews, extracted from `ROADMAP.md` and grouped
for reading rather than re-filed. Worth recording because the shape was not
obvious from inside the file: **25 items are blocked on Mike's ruling**, not on
build capacity, and three of those collapse into the single residue-ruling
sitting the board already schedules. `ROADMAP.md` is the sole open-work store —
no other doc in the tree carries `[ ]` items.

## The C5 cold pass

**Provenance.** The C5 re-measurement was authored by `f83a6f7`. This session
authored no part of it, held no commits here, and was opened by Mike, so
rule 4's single criterion was met and stated in both brief and verdict. Tier
Fable, checked at selection.

**One deliberate choice in the brief, worth recording.** The summary line that
reached Mike in the full list — *"the question shrank materially after
`c827705`"* — was the authoring session's own framing, lifted from the roadmap
while building the list. Restating it in the brief would have been rule 1's
warm-questioning defect arriving through the orchestrator instead of the
author. It was kept out of the brief's account of the work and entered instead
as an assumption to attack. The pass reached its own conclusion on that
question; the framing did not travel.

The brief's other load-bearing choice was the **re-run table**: thirteen
measured claims named individually, with the instruction to reproduce rather
than read. The failure mode this pass existed to catch is a premise recorded
as measured that was not, and a general "verify the numbers" would not have
forced it.

**Verdict: PASS-WITH-FINDINGS — 2 MAJOR / 4 MODERATE / 3 minor / 3 notes**
([brief + verdict](../reviews/2026-08-09-0708-c5-term-list-remeasure-cold.md)).

The distrust was **misplaced about the measurement and well placed about the
framing**. All thirteen claims reproduce exactly at the states the sweep
measured; the pass calls it the best-verified figure set the programme has
produced, and the denominator attack came back clean. What failed:

- **C5R1 (MAJOR)** — the "sharpest cost" is mis-composed. One of the six
  children has been public since 2026-07-29, so its lines are the guard
  *working*, not friction; and only ~6 of the 58 are the onramp act doctrine
  prescribes.
- **C5R2 (MAJOR)** — the 2026-08-06 deletion precedent is misdescribed against
  its own ADR, whose recorded ground was proportionality, not an absent hatch.
- **C5R3** — a phrase the item quotes from a child repo exists in no child
  repo, and a second roadmap item already cites it. A testimony loop caught
  before it hardened.
- **C5R4** — every atelier-side figure was falsified by drift within hours.
  This both proves the item's enforcement-gap thesis and means the re-ruling
  must ride on classes, never a frozen number.
- **C5R5 + C5R6** — option 1's scope grants would live in an unversioned,
  unreviewable machine-local file, and writing one for this repo's records
  silently answers the scrub-vs-accept question recorded as un-ruled. One
  ruling, not two.

**Verified independently before relaying**, because a MAJOR resting on a
cross-repo fact in a *public* tree is not something to pass on unchecked: the
public child's visibility, the presence of the two lines, and the false
all-clear in its own record were each confirmed from the artefacts. All three
hold. The refs stay out of the public verdict and went to Mike directly.

## The `add -A` sweep — the answer is zero

The board's last close asked whether any other repo held a never-publish file
untracked-and-unignored, one `git add -A` from re-tracking. Measured across all
24 repos on the machine and every never-publish pattern at any depth: **29 such
files, 27 safe, 2 tracked, zero exposed.** Cross-checked against an independent
`find` control returning the same 29 paths.

**The guard was deliberately not built.** Recurrence earns a check, not
severity, and the population is one instance already remediated in the commit
that caused it.

**The sweep's real yield was elsewhere:** one of the two remaining red floors
is red for a cause nobody had named — its allowlist was never untracked at
all, only the `.local` variant ignored. Same half-done shape one step earlier,
and far cheaper than the frozen-capture story assumed to be blocking it.
Verified by running the scanner against that tree. Which repo it is stays off
the public board; both are private.

## What this session did not do, on purpose

- **Did not rule.** C5R1–C5R12 are counsel; the decision is Mike's (rule 3).
- **Did not fix another repo.** Both the red-floor cause and the public
  child's false all-clear are work-locality items for sessions in those repos.
- **Did not scrub the live lines** in this file. The standing-gap item records
  that ruling as owed, and the audit paragraph is another session's landed
  work.

## Grounding it produced

The withholding above is itself the fourth instance in one day of the
name↔posture join being the natural thing to write — and the third caught
before landing. Recorded against the item that tracks it.
