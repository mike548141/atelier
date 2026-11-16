- [ ] 🔎 **A repo declares its visibility in two places, `CLAUDE.md` and
      `.atelier-floor.json`, and nothing compares them.** Found 2026-11-16 UTC
      by the `020/220` census, slice 2
      (`docs/method/census/2026-11-16-1204-apex-autonomy-guards-propagation.md`).
      `floor.py`'s visibility check compares the config's declared value with
      GitHub's; the `CLAUDE.md` line a session reads first is compared with
      nothing, so the two can disagree and the session reads the unchecked
      one. **Owed:** decide which is canonical and either derive the other or
      add the comparison (a `floor.py` check that fails soft, as the
      visibility check does). Not fixed in passing.
