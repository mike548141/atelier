- [x] **Cold review of the signing doctrine (SIGNING.md + ADR 0007)** — RAN
      2026-07-12 (cold fresh-context agent; every mechanical claim live-driven
      in a scratch repo, GitHub claims grounded in current docs):
      **PASS-WITH-FINDINGS**, verdict in `reviews/2026-07-12-signing-doctrine.md`.
      The core design proved out live — config block verbatim-correct, and the
      crown-jewel claim (bounded retirement keeps old signatures verifiable)
      is true: git passes the committer timestamp as verify-time. 10 findings
      G1–G10, all addressed same day; pre-activation, so every fix was a text
      edit — exactly what review-before-activation was for. The three
      blocking: verification made **two-plane** (GitHub's own merge commits —
      two already on `main` — are GPG-signed by the web-flow key and would
      have red-flagged the repo on first activation; the `gh api` verification
      check closes it spoof-safe), the badge-persistence claim was **inverted**
      vs current GitHub behaviour (removing a key does NOT un-verify history —
      corrected in SIGNING.md + ADR 0007 addendum), and quoted
      `valid-after="…"` timestamps mandated (the man page's unquoted form
      fails to parse on the estate's own ssh-keygen). Plus: trust list
      resolved at the child's pin, never floating `main` (a floated trust
      root defeats the blast-radius argument); custody, boundary-stub, and
      backdating honesty. Decision unchanged; activation still gates on Mike
      registering a key.
