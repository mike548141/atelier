- [x] 🎯 **P3 — the floor does not know whether a repo is public, and it should
      (ADR-worthy).** Mike, 2026-07-29: *"we will need additional guards, or to
      run the existing guards at a higher level of protection for public vs
      private repos."* Today visibility appears in the registry only as prose
      (`licenscan` is described as a publish gate; the `leakscan` `why` line
      says "a repo that **can** go public"). Nothing reads the actual state, so
      the same declaration means two very different risk positions. The shape to
      decide: visibility becomes a **declared, verifiable input** to `floor.py`
      (declared in `.atelier-floor.json`, cross-checked against the platform so
      a stale declaration is itself a finding), and on a public repo the floor
      tightens — advisory checks lose their advisory hatch, `licenscan` becomes
      mandatory, `publishscan` (P2) engages. Open question this must answer:
      what happens to a repo whose declaration says private and whose platform
      says public — that is a **live breach**, and the floor should say so
      loudly rather than fail on a config mismatch.
  - [ ] 💬 **Mike's answer, 2026-11-09 (to options queue run 722ac2e2 offered; an
        answer, not a ruling):** *"Yes, with the loud alert"*: each repo declares its visibility in its floor config, cross-checked against GitHub, public repos get the stricter checks, and a says-private-is-public mismatch is red. **Overlap noted by him the same day:** build on the daily visibility check already filed under `390/020`, never a second one.
  - [x] ✅ **DONE 2026-11-09 — first part APPLIED** by queue run 722ac2e2 (a Sonnet
        worker, read by the orchestrator before landing), per his answer:
        `"visibility"` in `.atelier-floor.json`, validated, and a CI cross-check in
        which says-private-is-public is red; every other mismatch and a missing
        declaration only warn, so no child turns red. No second daily check.
        Follow-ups, not built: what a public declaration tightens, a fleet column,
        and exporting the token in the floor template. Cold pass `160/1180`.
