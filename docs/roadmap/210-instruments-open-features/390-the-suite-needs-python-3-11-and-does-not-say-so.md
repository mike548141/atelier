- [~] (claimed 2026-11-09-1242, wt: atelier-qr-d0ca-hygiene, session d0ca5d24) 🔎 **The Python test suite needs 3.11 or later and does not say so.**
      Routed from the `160/970` cold pass (PQ2) by queue run 722ac2e2 on
      2026-11-09. `tools/README.md` and the test modules do not state the
      floor, so a run on an older interpreter fails in ways that read as
      defects. **Shape:** one README line plus a `sys.version_info` guard
      that says what is wrong.
