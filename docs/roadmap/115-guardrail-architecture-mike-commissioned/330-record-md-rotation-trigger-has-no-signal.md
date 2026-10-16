- [ ] 🔎 **RECORD.md's index rotation has lost its trigger** `[S][doctrine]`.
      Found 2026-10-16 by the `270` (c) worker, not changed there, because
      it is doctrine beyond that item. `docs/method/RECORD.md` § *The session
      log* says `SESSIONS.md`, like the roadmap, "rotates" once it "outgrows
      its budget". The only thing that ever measured that budget was
      sizescan's size advisory, removed on Mike's ruling (no arbitrary size
      limits, 2026-10-05; "Remove it", 2026-10-16). So the rule now names a
      trigger nothing reads. **The question:** what tells a session the
      index should rotate, if not a number? Candidates to weigh, not
      decided: a reading cost the session can see (the tail it loads at
      open), rotation at a fixed calendar boundary, or dropping the rotation
      sentence because the per-file detail split already keeps the index
      lean. Whichever it is must not reintroduce a line or size limit.
