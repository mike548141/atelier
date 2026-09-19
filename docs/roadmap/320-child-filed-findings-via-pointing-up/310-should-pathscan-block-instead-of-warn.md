- [ ] 🎯 **Should `pathscan` block instead of warn?** — Mike, 2026-09-19,
      ruling on `320/010`: *"we consider blocking instead of warning"*. A
      decision to weigh, not one taken.
      **What weighs on it, gathered from the board:** `pathscan` is warn-only
      on every plane today, and warn-only guards have a record here — the
      removed `plainscan` printed ~6,050 unread findings a commit (`020/360`).
      A path that no longer resolves is a real defect a reader hits, and a
      blocking check is read. Against: the known false-positive classes
      (`320/010` A–C, `320/170`) would block legitimate commits until fixed,
      and records legitimately name paths that no longer exist (they are
      excluded by default already, FR2).
      **When to decide:** after `320/010`'s declared roots ship and the
      children declare theirs, measure what is left per repo. If the residue
      is near zero, blocking costs little; if not, the residue says which
      class still needs fixing first. The measurement is the input, and the
      ruling is Mike's.
