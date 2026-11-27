- [x] 🔎 **A repo declares its visibility in two places, `CLAUDE.md` and
      `.atelier-floor.json`, and nothing compares them.** Found 2026-11-16 UTC
      by the `020/220` census, slice 2
      (`docs/method/census/2026-11-16-1204-apex-autonomy-guards-propagation.md`).
      `floor.py`'s visibility check compares the config's declared value with
      GitHub's; the `CLAUDE.md` line a session reads first is compared with
      nothing, so the two can disagree and the session reads the unchecked
      one. **Owed:** decide which is canonical and either derive the other or
      add the comparison (a `floor.py` check that fails soft, as the
      visibility check does). Not fixed in passing.
      **Built (the comparison, not the ruling):** `tools/floor.py`'s CI plane
      now carries a `visibility-declared` line that reads the root `CLAUDE.md`'s
      first `**...visibility:**` label, takes the first `public`/`private` word
      near it, and compares it with `.atelier-floor.json`'s `visibility`. Soft
      throughout: agreement is the only green; a disagreement, a missing
      `CLAUDE.md`, an unreadable or negated line and a config with no
      `visibility` all show 🟡 "not compared", never as agreement; no exit
      status moves. No network; not on the hook plane. Described in
      `tools/README.md` and `tools/floor.py`'s `VISIBILITY` section. A read-only
      probe of the local sibling repos found no disagreement; most do not
      declare `visibility` in their config yet, so they are "not compared".
      **Still open, the principal's:** which declaration is canonical, and so
      whether the other should be derived rather than compared, and whether a
      disagreement should ever block.
      ✅ **Closed 2026-11-27 (session 4ce066ba, `atelier-c1`):** the owed work was
      "derive the other or add the comparison"; the comparison landed. Which file is
      canonical is left for the principal to raise if he wants a derivation instead;
      it is not owed work.
      review: not warranted — a soft line that never moves an exit status; its worst
      failure, a false agree, leaves a repo where it stood before the line existed,
      and `tools/test_floor.py` pins every shape measured across the estate.
