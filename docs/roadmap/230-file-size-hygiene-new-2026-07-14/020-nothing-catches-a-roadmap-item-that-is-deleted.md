- [ ] 🎯 **Nothing catches a roadmap item that is deleted rather than harvested**
      — Mike's standing worry ("losing the queue of ideas"), audited in full
      2026-07-26 and found **clean in atelier** (362 commits, 540 items ever,
      zero confirmed losses →
      [`sessions/2026-07-26-1030-roadmap-integrity-audit.md`](../../sessions/2026-07-26-1030-roadmap-integrity-audit.md)).
      Clean today, unguarded tomorrow. `sizescan` covers the two *adjacent*
      failures — an `[x]` left on the hot path (cold-content gate) and a live
      `[ ]`/`[~]`/`⏳` buried in an archive (harvest-integrity gate) — but an
      item **removed from `ROADMAP.md` that arrives nowhere** passes every
      check. The tri-state grammar already forbids it (flip `[x]` with a
      disposition, then harvest; never delete), so this is a rule with no
      forcing function — the fourth instance of that family.
      **What a guard would do, in plain terms:** on commit, compare the staged
      `ROADMAP.md` against `HEAD`; for every checkbox item that disappeared,
      require that it either turns up in an archive store in the same commit or
      carries an explicit dated exemption. Cheap, and it fails loudly at the one
      moment a human could still say "wait, that wasn't a duplicate".
      **The trade to rule on:** the audit's false-positive rate was near-total
      because a healthy roadmap rewrites an item's title at every state change
      *and* re-homes items under reframing sections — both look exactly like a
      deletion. A naive guard would therefore cry wolf on ordinary good
      housekeeping, and a guard that cries wolf gets `allow`-markered into
      silence. So: **(a)** build it and accept it must match on content
      fingerprints rather than titles, **(b)** make it advisory-only — it
      *reports* every disappearance for the committing session to confirm, never
      blocks, or **(c)** decline the mechanism and accept the manual audit as
      the control, now that one exists and is cheap to repeat against this
      record. *review: WARRANTED if built — a first-of-kind gate.*
