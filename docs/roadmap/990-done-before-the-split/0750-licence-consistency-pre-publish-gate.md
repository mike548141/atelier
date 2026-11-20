- [x] **Licence-consistency pre-publish gate** (A11) — DONE 2026-07-10 (Opus):
      `tools/licenscan.py`, the third pre-publish scan (leakscan · secretscan ·
      licenscan). Three checks — LICENSE present + SPDX-recognised, every
      declaration (pyproject/package.json/Cargo/gemspec/setup.cfg/README badge)
      agrees, no incompatible `SPDX-License-Identifier` header (copyleft-into-
      permissive blocks). Conservative + advisory, `--expect <SPDX>` for CI,
      zero-dep, allow-marker + `.licenscanignore` hatches, `--selftest`. 35 tests
      (suite 98→133). *Correction (2026-07-10 review, B1): the original
      "live-proven clean on atelier" claim here was **false at the commit that
      recorded it** — the scan flagged its own unexempted test fixtures at HEAD;
      any mid-build clean run didn't survive to the commit. Fixed (`.licenscanignore`,
      same reasoned exemption as the sibling scans) and re-proven:
      `--expect Apache-2.0` exit 0 at the review session's close.* Reviewed
      2026-07-10 (the batch review, B1–B3 fixed: `-only`/`+` SPDX suffixes,
      prose-header residual stated).
