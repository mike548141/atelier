- [x] **ccrepo + cctranscript ship untested** — DONE 2026-07-11 (session 35).
      They shipped with no tests (session 34), unlike the `tools/` scanners which
      each carry a unittest + `--selftest`; cctranscript had since grown real
      rendering logic (wrapping, markdown, model tags, right-align, exchange
      rules). Now floored with `node:test` + `node:assert` — **zero-dep, mirrors
      `tools/`'s stdlib-only pattern and sets the Node layer's test convention**
      (the first Node test surface; decision recorded in the session log). Minimal
      testability refactor only: each CLI entrypoint guarded by
      `require.main === module`, pure functions `module.exports`ed — no behaviour
      change, except one stated fix (an explicit `.jsonl` path now recovers its
      repo label via `cwdFromLog`, as every other route already did). Coverage:
      `instruments/cctranscript.test.js` — a `--json` output-contract test over a
      checked-in synthetic fixture (`fixtures/session-sample.jsonl`) asserting role
      classification, model mapping, timestamp/text extraction, and `--think`/
      `--tools` gating (this is what catches a Claude Code log-format change), plus
      pure-function units; `instruments/ccrepo.test.js` — pure functions and the
      aggregation fold over fixture ccusage rows. Wired into `ci.yml`'s floor job.
      Grounded in EVIDENCE §14 (an honest instrument's "ok" is a claim the apex
      governs). **Residual:** ccrepo's coverage is pure-functions + aggregation
      only — the `ccusage` `execFileSync` call, JSON parse, FX conversion, and
      table render sit behind an untested seam (aggregation was factored out to
      `aggregate()` to test the fold; the shell-out itself has no test double yet).
