- [ ] **Every child inlines the same stale-`HEAD` drift bullet — a fleet
      sweep is owed.** The defect sits in the canonical floor region, so every
      repo that inlined that region carries it: `ros`, `tiki`, `docker-heap`,
      `shed`, and the rest of the thirteen. Each is one stale local checkout
      away from a doctrine check that reports clean while the house doctrine
      moves underneath it. The staler the checkout, the quieter the check —
      the wrong direction for a guard, since the case it most needs to catch
      is the one it most reliably misses. Sequence: fix the canonical region
      first (the item above), then apply at each child's next pin bump, the
      cadence the floor-template rollout already uses. `floorfleet` holds the
      child list, so the sweep's scope needs no fresh survey. Worth checking
      at the same time whether a child's pin can be *ahead* of its local
      atelier checkout, which is the exact state faves was left in before the
      pull. Raised by Mike, 2026-08-16, from a faves session's pin bump.
