- [ ] 🔎 **The scanners' exempted test files rest on a promise nothing
      checks: "deliberately fictional", so real key material can land there
      unseen.** `.secretscanignore` exempts `tools/test_secretscan.py`,
      `tools/test_leakscan.py` and `tools/test_signscan.py` whole, on the
      stated ground that their fixtures are fictional or example-shaped. No
      check holds them to it. Found 2026-11-06 by queue run 722ac2e2 at its
      own landing of `320/790`: the worker's fix added four real throwaway
      private keys (EC and RSA PKCS#8, SEC1, PKCS#1) to
      `tools/test_secretscan.py` as fixtures, every check passed, and only the
      orchestrator's read caught it before the push (the branch was amended
      to synthetic DER; nothing reached `main`). The keys were never in use,
      but a public repo carrying working private keys draws every third-party
      scanner, and the next one need not be throwaway.
      **A possible shape, to judge:** keep the exemption, and add a narrow
      check that does run on the exempted files, for what "fictional" is
      meant to exclude: a base64 run that decodes to a private-key DER form
      (a SEQUENCE opening with an INTEGER version, the test `320/790` added in
      reverse), or a real PEM private-key block with a body that decodes.
      Fixtures that need a private-key shape build it at test time, as
      `synthetic_private_der` in `tools/test_secretscan.py` now does.
      Not taken by the finding run: it changes what a guard exempts, and the
      run had already stopped.
