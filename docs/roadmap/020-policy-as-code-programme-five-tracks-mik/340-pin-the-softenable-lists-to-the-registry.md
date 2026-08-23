- [ ] **Pin the three softenable-set prose lists to `Scanner.advisory`
      (AP2, ruled 2026-08-23).** floor.py's docstring, ADR 0008 Decision 2
      (as amended 2026-08-23) and CONTRIBUTING's never-softened list each
      describe which scanners carry advisory forms; none is test-pinned to
      the registry, which is how the docstring and the ADR drifted wrong
      while CONTRIBUTING stayed right. One test: parse each prose list,
      assert it matches `advisory is None` over SCANNERS, so the next
      registry change reds the stale sentence instead of leaving it.
      review: not warranted — a queued test item recording an accepted
      ruling; the test earns review with its code.
