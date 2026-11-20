- [x] **A2 — the hook plane's `leakscan` cover was asserted, never enforced.**
  The hook template runs `leakscan --require-terms`. A `Scanner` may name the
  flag giving it full cover, so a plane omitting it renders **🟡 partial**
  rather than ✅ — CI's `leakscan` is structural-only permanently and now says
  so every run. `floorfleet` reports whether **this machine** carries a term
  list: a machine fact, not a per-child one, so it goes on the board once and
  asks `leakscan`'s own resolver rather than re-implementing the lookup.
