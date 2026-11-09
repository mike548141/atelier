- [~] (claimed 2026-11-09-1242, wt: atelier-qr-d0ca-scan, session d0ca5d24) 🔎 **A floor `disabled` entry carries a reason but no end date, so it
      cannot meet the rule that a check may be lowered only declared, reasoned
      and expiring (`020/170`).** Found by queue run 722ac2e2 on 2026-11-09 when
      it applied that rule. **Shape:** a build in `tools/floor.py` and the fleet
      view, warn-first so no child goes red. Also open: whether narrowing a
      check with `scope` or `flags` counts as lowering it (ruled a permanent
      fact on 2026-07-28; his to revisit).
