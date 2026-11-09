- [ ] 🔎 **A floor `disabled` entry carries a reason but no end date, so it
      cannot meet the rule that a check may be lowered only declared, reasoned
      and expiring (`020/170`).** Found by queue run 722ac2e2 on 2026-11-09 when
      it applied that rule. **Shape:** a build in `tools/floor.py` and the fleet
      view, warn-first so no child goes red. Also open: whether narrowing a
      check with `scope` or `flags` counts as lowering it (ruled a permanent
      fact on 2026-07-28; his to revisit).
      - **2026-11-10, warn-first build landed:** a floor `disabled` entry
        takes the legacy string or `{"why", "review-by"}`, the shape `advisory`
        uses. A missing or passed `review-by` warns on the floor line and the
        `floorfleet` board (🟡 undated, 🔴 passed with its age) and never
        changes an exit status; the 2026-12-09 bar on `disabled` board-design
        checks is untouched and still bites whatever date is declared. Read-only
        probe over the sibling repos' floor configs: no outcome changed. `scope`
        and `flags` narrowing is left as it was (the principal's to revisit).
        `tools/README.md` and `GUARDS.md` updated where they describe `disabled`.
      - [ ] **Open: turning this from a warning into a block: date and fleet
        probe owed.** Kept open on purpose: the rule (`020/170`) says a lowering
        must expire, and a warning does not enforce that.
