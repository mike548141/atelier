# Sibling to the paragraph-projection and grace top-up — held under rule 1's split

Sibling of `docs/reviews/2026-10-28-1255-paragraph-projection-grace-topup-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the top-up's phase-1 findings are
committed.** Written 2026-10-28 UTC by session `29af7e91`, the brief-writer named in the brief's
provenance; it forms no finding and writes no severity. Fold this file in below the reconcile
and delete it at phase 2.

## Re-run results held back from the brief

Run once each by the brief-writer, 2026-10-28 between 12:54 and 13:45 UTC, from its worktree
root at `16c6511` (code identical to the API pass's `0a2b7a7`), on the principal's laptop.
Load averages were between about 14 and 53; other sessions were live.

- **PQ-a.** `test_board.py -v` as given, with signing on and reachable: 59 tests OK, exit 0.
- **PQ-b.** Full suite under `nice -n 10`: 2032 tests in 1197 s, **exit 1, one failure**:
  `test_pins.BoundedMemory.test_peak_memory_does_not_scale_with_sibling_count`, "scan did not
  finish in time". It is outside the delta and timing-bound, at very high load; whether it
  reproduces at normal load was not checked.
- **PQ-c.** Floor at HEAD with the real term list: ci plane exit 0 (`board` ✅; `leakscan` 🟡,
  no `--require-terms` on the ci plane; `pathscan` 3 warn-only missing-path findings outside
  the delta); hook plane exit 0.
- **PQ-d.** Children by count, `board --check` from the worktree's copy, read-only: 11 split
  boards; 11 exit 0; **2** pass only under the grace, which agrees with the API pass. For both
  of those 2, the latest ten GitHub runs ended `failure` **without a job starting**: the CI
  provider refused to start them for an account-level reason outside the repos. No log exists
  to read, and the grace line could not be observed in CI. Atelier's own floor runs, a public
  repo, are green. The hook-plane fallback (a real `git commit` over a synthetic old-form
  board) was **not run** by the brief-writer.
- **PQ-e.** Not run (a headless brief-writer cannot aim `/security-review` usefully).

## Hypotheses (the brief-writer's suspicions, a floor not a fence)

1. **PP9 is a portability note only.** On a host whose key is reachable, `StagedPlane` passes
   as given; the note stands as written.
2. **The API pass's floor and suite gaps hide nothing about the delta.** The floor is green and
   the one suite failure is a load-bound test elsewhere.
3. **Lens 1 (C) needs a qualification the API pass could not see.** It counted "CI →
   `floor.yml@main`, 11/11" from the committed workflows. For the 2 children still on the old
   form, the CI plane is not running at all at present. So "both planes flip together" on
   2026-11-18 is true of the code and false of what those children will see: until their CI
   jobs start again, only the hook will red. The same fact sharpens PP5. For those 2, the
   CHANGELOG at a pin bump is the only channel. The ⚠️ line cannot reach a CI log that is
   never written, and one of the two has not bumped its pin.
4. **The fallback hook run confirms the notice wording.** Through a real `git commit`, the
   hook should print the ⚠️ line and exit 0 before 2026-11-18, with the staged remedy carrying
   `--from-index`, as the API pass saw through the CLI.
5. **`/security-review` finds nothing.** The delta adds no subprocess and no new input path.
6. **Top-up or full re-run.** Every judgement-forming probe the API pass ran (the census, the
   identity check, the boundary table, the mutations with signing switched off) was local and
   disclosed, and the missing checks so far confirm it. That points to TOP-UP SUFFICES. The
   live-CI fact in hypothesis 3 is new evidence the API pass could not reach, but a top-up
   carries it without a full re-run.
