- [ ] 🎯 Third confirmed instance of the class landed 2026-08-03, and Mike ruled
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

      ✍️ **Drafted and landed 2026-10-05; Mike's sign-off is what is still
      owed** (queue run, an Opus 5.5 worker; `be9a3ae`). The rule is
      `EVIDENCE.md` **§15, "A test cannot falsify its own code's
      assumption"**. The drafting session chose EVIDENCE.md over REVIEW.md
      because the rule is about what a passing test is evidence *of*: a
      belief about an external system is the author's own inference
      however green the test runs (§2). That binds the builder when the
      test is written, not only the reviewer later. It names the item's
      three highest-risk sites and cites the three instances with no
      estate detail. One correction to this item's own wording: instance
      1 was not a library bug. The library behaved as designed, and the
      wrong belief was in the code and its test. §15 says it that way. The
      doctrine pass is queued at `160/710`. 🎯 **Mike signs off on the
      wording and the home**, per this item. It goes to him in plain
      language at the run's close. Until he does, the rule stands as
      landed doctrine under review.
