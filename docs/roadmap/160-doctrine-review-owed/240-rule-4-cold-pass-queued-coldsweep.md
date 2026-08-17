- [ ] 🛑 **The coldsweep pass RAN 2026-08-17 and the cycle stays OPEN — three
      MAJORs stand; SW1–SW11 await Mike's ruling round.** The rule-4 Fable code
      cold pass (taker: a cold session Mike opened 2026-08-17 1321 UTC on the
      Fable tier, running the brief a *different* cold session wrote at 0955
      UTC, under a Fable-orchestrator-held context partition — reviewer and
      orchestrator both on the named tier) returned PASS-WITH-FINDINGS —
      3 MAJOR / 5 MODERATE / 2 minor / 1 note after reconcile (SW11 MODERATE
      added at reconcile from a seeded question and verified in code; SW9
      raised note → minor on a live instance one day after landing) →
      [`reviews/2026-08-17-1000-coldsweep-cold.md`](../../reviews/2026-08-17-1000-coldsweep-cold.md).
      The happy path — repo-root `--root`, relative excludes, atelier's layout,
      no nested repos — is correct: selftest OK, Python 1,344 / node 235, both
      floor planes green, the 289 barred-file count reproduced at the landing
      commit. Off that geometry **the bar silently does not apply while the
      provenance line says it did**, and that class is all three MAJORs:
      SW1 — an absolute, `..`, case-different or mistyped `--also-exclude`
      excludes nothing, no warning, and the absolute machine path is echoed
      into the paste-into-verdict line (this run's own reviewer instructions
      say "absolute paths everywhere"); SW2 — `--root` at a subdirectory or at
      a child whose floor config relocates `docs` bars zero files, exit 0;
      SW3 — nested harness worktrees under `.claude/worktrees/` (596 barred-by-
      name files from the main checkout, two live siblings) and all gitignored
      material are searched. MODERATEs: SW4 (doctrine, rule 3) — the tuple is
      the only statement of the four-path set; rule 2's prose bars prior
      reviews only, and onramp step 4 collides with the cold bar unstated
      (corroborated: the CMF verdict already recorded the exclusion as
      undefined in doctrine); SW5 — provenance line and banner on stdout after
      the hits break the claimed pipeline contract; SW6 — an unreadable file is
      silently skipped and counted as swept, exit unchanged; SW8 — the tool is
      named on no reviewer-facing surface but rule 2, and no child invocation
      story; SW11 — `--include-barred` silently drops every `--also-exclude`.
      Corpus ↔ instances at reconcile: the released verdicts carry **two**
      `./`-prefix instances (AA and RG, same 0710 run) and the selftest pins
      exactly that shape; the earlier "instances" were a different class
      (pending-diff exposure), and one prior pass excluded `.claude` by hand —
      practice the tool dropped (SW3). Findings on the tool's code may carry
      the author's `[rejected: grounds]` escape but the author was not the
      taker; SW4 is the principal's outright. Reviewer disclosures stand in
      the verdict: swept with the tool under review (circularity stated),
      landing commit read via `--stat`, board items `250` and `010/110` opened
      after sweeps surfaced them, `python3 -m unittest tools.test_coldsweep`
      fails on import (noted, not a delta defect).
      *Delta:* `tools/coldsweep.py` · `tools/test_coldsweep.py` ·
      `tools/README.md` § *`coldsweep.py`* · `docs/method/REVIEW.md` rule 2's
      sweep clause · `CHANGELOG.md` (landed `613132e`, wt: `rulings-0817`).
      *Intent record:* board item
      `290-ruling-round-2026-08-17-the-cold-run-find/040-build-the-cold-sweep-guard.md`.
      Brief written 2026-08-17 by a non-author Fable cold session (its three
      disclosures stand in the verdict); sibling folded in and deleted; wt:
      cold-run-0817-1321.
