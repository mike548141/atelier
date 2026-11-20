- [x] (2026-08-03: applied, terminal) **TA-application-pass residue — TAA1–TAA3, RULED 2026-07-28 (Mike,
      plain-language walk-through with per-option impacts).** The terminal
      cold pass returned 0 MAJOR / 1 minor / 3 notes
      ([verdict](../../reviews/2026-07-28-1136-ta-application-cold.md)); the cycle
      is closed, and per rule 3 the residue was Mike's to decide.
      **TAA1** (minor) — a comment in `floor.py`'s scope guard still labels
      two fail-opens "(open)" that the same series shut → **FIX**: two-line
      comment edit re-labelling both members shut, TA1 pointer kept.
      **TAA2** (note) — the two 🟡 notes share one report field via `elif`,
      so a future softenable scanner with a cover flag would silently drop
      its scope-drift note → **JOIN THE NOTES** (chosen over the
      comment-only variant: same cost, and a joined note can't decay the way
      a comment relies on a future reader honouring it).
      **TAA3** (note) — AW6 doesn't say whether a second queued pointer over
      the same files discharges the delta-list widening duty → **HOLD for a
      third instance**, per the reviewer's counsel and the >2 promotion
      rule; this is the second recorded case.
      **Work owed: TAA1 + TAA2.**
