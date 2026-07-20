# Size-signal rebalance — from a line-count budget to a cold-content gate

**2026-07-20 · ~2025 UTC · Opus · wt: `atelier-size-signal-rebalance`**

Mike: *"Can you do the work queued for sizescan"* — the standing `⏳`/`[ ]`
follow-on from the 2026-07-20 onramp session: **rebalance the size signal.** This
session was the fresh focused session that item asked for.

## The ruling being applied (Mike, 2026-07-20)

The old gate made a **flat line-count budget (300) a hard CI failure** — redding
`main`'s ROADMAP at 315/300 for being *fulsome*, on a number grounded in nothing.
Mike's reframe: **cost is size × read-frequency.** A hot-path file (read every
session) pays its length every open; a cold store (grep-on-demand) is nearly
free. So the enemy is never size — it is **cold content sitting on the hot path**,
which is *always* losslessly fixable (move to the `-DONE` store) and pure cost.
Gate on *that*, never on length. No magic number.

## What shipped

1. **`tools/sizescan.py` reworked** — the gate now keys on **relocatable cold
   content**: a completed `[x]` item in a checkbox-worklog file (`ROADMAP.md`),
   the one crisply-detectable form. Line count is demoted to a pure **advisory**
   (a class *reference point* that reports but never fails a build). The static
   `GATED = {ROADMAP, SESSIONS}` set is **gone** — gating is now content-driven
   (`gated = cold_items > 0`), so it cannot drift. `budget_for`→`reference_for`,
   `DEFAULT_BUDGETS`→`SIZE_REFERENCE`, new `cold_item_count()`. The `[x]` matcher
   is anchored to a list bullet so a `[x]` in prose is not miscounted; only
   checkbox-worklog files (basename-keyed) count.
   - **Hatches**: `sizescan:allow` exempts a file fully; `sizescan:budget=N`
     quiets the size advisory only — it can **never** silence the cold-content
     gate (proven by test + selftest).
   - Suite **267→282**; selftest rewritten around the new contract (incl. the
     key reversal: *a large all-OPEN roadmap does not gate*).
2. **CI + floor** — `ci.yml` and `floor.yml` step retitled "cold content on the
   hot path"; comments rewritten to the new frame.
3. **`main`'s floor turned green the right way** — the 4 inline `[x]` items in
   `ROADMAP.md` were the relocatable cold content, so the fix was a **harvest,
   not a trim**: two were already in `ROADMAP-DONE` (deleted the duplicate
   stubs; doctrine pointer updated to name the triple cycle); two (the
   tripwire-split application, now superseded; the fleet-wide `hooks.atelierTools`
   fix) moved verbatim to the File-size completed section. `sizescan --check` →
   clean, exit 0.
4. **`method/RECORD.md`** — the module doc's size paragraph rewritten to the
   cold-content model; SESSIONS documented as advisory-only (a lean index has no
   `[x]`, so it never gates; the size nudge is what surfaces a flat-log
   regression).
5. **SR2 — `PROPAGATION.md` child-block spec re-grounded.** The dead "~15 lines"
   figure replaced with a **grounded shape**: one bullet per irreducible floor
   concern (seven today), which sizes the block at **~50 lines** — a figure
   derived from the block's *structure*, never from what it weighs today
   (measured 49). A concern leaves the block only by genuine redundancy, never by
   trimming a live safety statement.

## Judgement calls (flagged for the independent review)

- **The crisp detector is `[x]` only.** Prose-shaped cold content (resolved
  narrative under an open item, a closed-cycle write-up with no checkbox) is real
  but not machine-detectable without guessing, so it is **caught at review, not
  measured** — mirroring the tool's standing one-sided honesty on thinness. The
  size advisory is the *pointer* to that review.
- **SESSIONS moved to advisory-only.** A lean index carries no `[x]`, so it never
  gates; its flat-log regression mode is surfaced by the size advisory, not a
  gate. This is the faithful reading of "gate only on relocatable cold content,
  no magic number" — but it *is* a coverage change from the old SESSIONS budget
  gate, so it is named here for the reviewer.
- **Advisory reference numbers retained (non-gating).** Kept `SIZE_REFERENCE` as
  a pure advisory nudge (never a build failure). The alternative — deleting all
  numbers — was rejected because the advisory is what catches un-marked narrative
  and flat-log regressions. Open for the reviewer to challenge.

## Review status

The output warrants an independent review (**WARRANTED** — reverses a dated
ruling + reworks a gate with a silent-failure mode). Per REVIEW.md rule 4 and the
review-brief-independence rule, the author (this session) **queued a `⏳` item and
wrote no brief**; a non-author rule-4-eligible session takes it and writes the
brief. SR2's re-grounding rides with this cycle.

## Dates

At-rest stamps are **UTC** (`date -u` = 2026-07-20 2025); the session's local
calendar date is 2026-07-21 (NZ, UTC+12). Mike's ruling and this application fall
on the same UTC day (2026-07-20).
