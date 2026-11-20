- [x] **Apply wrapscan review findings WS1–WS6 + implement option-a scope** —
      DONE 2026-07-23 (queue run 0959, Sonnet `ceb3fda`, Opus-verified/merged).
      WS1 option-A scope live (`ci.yml` gates `docs/method docs/build
      docs/decisions`, `.wrapscanignore` the record/log/review stores);
      the 3 genuine over-wraps fixed (REPO-STANDARD:52, SIGNING:83,
      CONCURRENCY:232); WS2 tightened (structural pipe signal), WS4 sibling
      allow-marker padding exempted, WS3 accepted-and-documented as a gate-time
      residual (reprocessing an unclosed fence would false-positive on truncated
      pasted code — worse failure mode), WS5 documented wart. Suite 497 green,
      gated scope 0 findings. Stays ADVISORY — no flip. The wrapscan flip
      precondition (clean run over the gated doctrine surface) is now MET; the
      flip stays Mike's go/no-go (live in ROADMAP.md).
