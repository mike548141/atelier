- [x] 🔎 **RECORD.md's index rotation has lost its trigger** `[S][doctrine]`.
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
      - 2026-11-16 — ✅ **Done: a reading cost is the trigger, the move
        stays.** `RECORD.md` § *The session log* now says the index rotates
        when getting bearings from it takes more than the tail the read order
        loads, never at a length, and marks that trigger as the house reading,
        not a ruling. The rotation move itself is kept because Mike decided it
        (F3, 2026-07-14); only the dead budget trigger went. Dropping the
        sentence outright was weighed and not taken for that reason, and a
        calendar boundary was not taken because it rotates a log whose read
        cost has not changed.
      🔒 CLAIMED 2026-11-16T11:22Z (claimed 2026-11-16-1122, wt: qr-78ca-record) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).
