# Sibling to the staged-positional reader top-up — held under rule 1's split

Sibling of `docs/reviews/2026-10-28-1255-staged-positional-reader-topup-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the top-up's phase-1 findings are
committed.** Written 2026-10-28 UTC by session `29af7e91`, the brief-writer named in the brief's
provenance; it forms no finding and writes no severity. Fold this file in below the reconcile
and delete it at phase 2.

## Re-run results held back from the brief

Run once each by the brief-writer, 2026-10-28 between 12:54 and 13:40 UTC, from its worktree
root at `16c6511` (code identical to the API pass's `0a2b7a7`), on the principal's laptop, in
the foreground or watched to completion. Load averages were between about 14 and 53 throughout;
other sessions were live.

- **QU-a.** `python3` on `PATH` is 3.14; `/usr/bin/python3` is 3.9. The tracked hook calls
  `python3` from `PATH` (fail-closed if absent). A throwaway signed commit in a scratch repo
  succeeded with a good signature: the sandbox's signing limit is absent here.
- **QU-b.** The four delta test files, as given: `test_report` 71 OK, `test_leakscan` 219 OK,
  `test_secretscan` 174 OK, `test_conflictscan` 56 OK, each exit 0.
- **QU-c.** Full suite under `nice -n 10`: 2032 tests in 1197 s, **exit 1, one failure**:
  `test_pins.BoundedMemory.test_peak_memory_does_not_scale_with_sibling_count`, "scan did not
  finish in time". It is outside the delta and timing-bound; the machine's load was very high.
  Whether it reproduces at normal load was not checked.
- **QU-d, M7 only.** Run over a `git archive` extract (not a clone), whole files, no `-k`:
  unmutated and M7-mutated give the **same** result, five failures in the
  `StagedAbsolutePathTest` classes of the three guards, which come from the extract not being a
  git repo. `test_report` was 71 OK both ways. With the git-backed classes running this time,
  M7 is still caught by nothing. The other eight mutations were not re-run.
- **QU-f.** Floor at HEAD with the real term list: ci plane exit 0 (`leakscan` 🟡 because the
  ci plane does not pass `--require-terms`; `secretscan` 25 advisories; `pathscan` 3 warn-only
  missing-path findings in files outside the delta); hook plane exit 0.
- **QU-h.** The latest five `floor` runs on atelier's GitHub copy are all `success`; the most
  recent set up CPython 3.12.15.
- **Not run by the brief-writer:** QU-e (QS1 through a real commit), QU-g
  (`/security-review`; a headless brief-writer cannot aim it usefully), and the other eight
  mutations.

## Hypotheses (the brief-writer's suspicions, a floor not a fence)

1. **QS4 stands.** M7 survived the whole delta files with every git-backed class running, so
   the API pass's conclusion did not depend on the errors in its baseline. A clean-clone
   re-run should agree.
2. **QS9 narrows.** Its first half (the suite needs 3.10 or 3.11+) is real but bites only a
   host whose first `python3` is the system 3.9. On this laptop the shell's is 3.14 and CI's
   is 3.12. The open question is a git client or hook run with a stripped `PATH`, where
   `/usr/bin/python3` would come first. Its second half (fixtures inherit the host's signing
   config) is real wherever signing is unreachable, and here it is reachable.
3. **The API ledger's error attribution holds.** Every error and failure it charged to the
   sandbox is absent in QU-b. The full-suite failure in QU-c is a different, load-bound test
   that the API pass never reached.
4. **QS1 reproduces through a real commit.** The hook calls `floor.py --plane hook`, the same
   path the API pass drove, so a real `git commit` should let the staged key through when the
   scope is case-folded. On a case-sensitive CI runner the floor's existence check should block
   that scope, so the CI plane reds on push. But a push to a public remote already publishes
   what the hook let through, so the severity should stand.
5. **`/security-review` adds little.** The delta adds no subprocess or filesystem call driven
   by input, so it should find nothing beyond lens 4.
6. **Top-up or full re-run.** The API pass's judgement-forming work (the spelling table, the
   cwd probes, the child counts, the reading) was local and unaffected by its limits, and the
   missing checks so far confirm rather than change. That points to TOP-UP SUFFICES, unless
   QU-e or the remaining mutations turn something up. The one place a limit may have shaped
   judgement is truncation: the full suite's output was lost, and the reviewer did not chase
   it.
