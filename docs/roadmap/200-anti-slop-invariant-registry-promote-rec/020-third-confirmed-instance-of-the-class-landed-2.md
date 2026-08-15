- [ ] Third confirmed instance of the class landed 2026-08-03, and Mike ruled
      the mint queued here. The class: a test authored from the same mental
      model as the code it guards cannot falsify that model — mutation testing
      proves *wiring*, never *correctness*; when a test encodes a belief about
      an EXTERNAL system (library semantics, wire protocol, platform default),
      an authority outside the author's own code must enter the loop (read the
      library source, or capture the wire) before the test counts as evidence.
      The three instances, all in ros: (1) 2026-07-25 the RUN 9 "hermetic SSH
      connections" test recorded as mutation-verified had encoded asyncssh's
      `client_keys=[]`-means-load-defaults bug AS the invariant (fixed
      `321ff0f`); (2) same day, a capture harness wrapped the wrong asyncssh
      hook and reported `refusals_received: 0` everywhere — caught only because
      a *successful* login also read zero; (3) 2026-08-03 (ros RUN 12) the
      dual-psu power test asserted `psu2` — the exact internal-rail mislabel
      the multi-feed review had just disproven. Per PROPAGATION.md's ladder,
      three instances is the mint-doctrine threshold. Candidate text lives in
      ros memory `feedback_test_shares_code_assumption` (How-to-apply
      paragraph); likely home EVIDENCE.md or REVIEW.md — the drafting session
      decides, Mike signs off. Highest-risk sites to name: sentinel values
      (`[]` vs `None` vs omitted), falsy-but-not-absent distinctions, comments
      asserting third-party behaviour. *review: rides the doctrine change
      itself (a method/ edit is review material by standing rule).*
