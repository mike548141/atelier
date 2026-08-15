- [ ] 🎯 **P3 — the floor does not know whether a repo is public, and it should
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
