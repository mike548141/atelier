- [ ] 🔎 **A `gh api` read of the pre-flip platform settings** `[S][tools]`.
      Filed 2026-11-09 by `260/070`, which wrote the gate as a list a session
      follows and left the tool to this item. Today nothing reads these
      settings as a gate: `tools/publishscan.py` judges the tracked path set and
      cannot see a setting, and `tools/floorfleet.py` reads only atelier's own
      ruleset for the parent row (`115/180`). Its read helpers are the natural
      home, and `tools/floor.py`'s `visibility` line (`260/050`) is a precedent for a
      CI-plane read that fails soft. **Proposed shape:** one read-only report per
      named repo of the five settings in `docs/method/AUTONOMY.md`'s pre-flip
      list, with the value it read, for the gate to record. Report only, no
      writes. Every endpoint it needs answered on atelier on 2026-11-09. Fork-PR
      approval and branch protection cannot be read as set on a private
      free-plan repo, so the report must say *not available* rather than fail.
      Not built because `260/070` scoped it out. Not owed before a flip: the
      gate itself is the doctrine, and this only automates reading it.
