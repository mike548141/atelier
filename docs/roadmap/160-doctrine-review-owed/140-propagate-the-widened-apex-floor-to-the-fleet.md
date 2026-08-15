- [ ] **Propagate the widened apex floor to the fleet children** — the remaining
  half (the in-repo restatement sweep is DONE, `a4740c4`, →
  [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)). Each child copies the floor block
  statically, so they adopt the
  three-element floor + honesty-precondition clause at their next pin bump /
  harvest, per-child commits. **Ungated 2026-07-23** (apex cycle closed on Mike's
  AWA accept-all). The canonical child floor block now lives at
  `docs/build/templates/CLAUDE.md` (byte-identical to PROPAGATION's inlined
  block) — children align to it. Pairs naturally with the `floor.yml`
  cold-content gate + `pull_request`-trigger adoption already queued below (same
  pin-bump lane).
