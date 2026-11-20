- [x] **atelier's own CI** — DONE 2026-07-10 (Opus): `.github/workflows/ci.yml`
      (job `floor`) dogfoods the floor every review asserted by hand — the tool
      test suite, three scanner `--selftest`s, and the scan triad over the whole
      tree. Zero-dep stdlib means a public runner needs only Python. Honest
      scope baked into the header: secretscan/licenscan at full cover; **leakscan
      structural-only, deliberately no `--require-terms`** (its term list is
      machine-local by design — CI can't hold it and must not). Least-privilege
      (`contents: read`), concurrency-cancel. **Live-proven twice on GitHub** (7s,
      11/11 steps, no deprecation annotation after the `checkout@v5`/
      `setup-python@v6` bump) — not assumed; watched green.
