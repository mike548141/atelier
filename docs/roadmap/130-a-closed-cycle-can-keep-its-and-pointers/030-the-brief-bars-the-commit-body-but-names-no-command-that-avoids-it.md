- [x] **FIXED 2026-10-18** (wt: atelier-qr-130-030)
      **The brief bars the landing commit's message body but names no command
      that avoids it, so reviewers leak it by the obvious `git show`.** Found by
      the 2026-10-17 review run (21 rule-4 cold passes, Fable reviewers under a
      Fable orchestrator). Every 2026-10-16 brief tells the reviewer to read the
      landing commit's "subject, stat and diff only" and bars its message body
      until phase 2. Four of the twenty-one reviewers disclosed reading the body
      anyway, each by a natural command: `git show <sha> -- <paths>` (prints the
      body before the diff; the FP, IX and RT passes), `git show --stat` (the TG
      pass). A fifth (TC) ran a hand `grep -rn` with a `./`-prefixed exclusion
      that matched nothing, the class `coldsweep` exists to end, and saw single
      barred lines before switching to the tool. Each treated the exposure as
      claims to re-drive and disclosed it in the verdict's provenance, so no
      pass is contaminated beyond its own disclosure, but five slips of one
      shape in one batch is a rule that is unfollowable as written
      (`REVIEW.md` rule 1's own lesson: reading is atomic), not five careless
      reviewers.
      - **Evidence:** the provenance sections of
        `docs/reviews/2026-10-16-1550-reviews-template-triggers-cold.md`,
        `2026-10-16-1550-first-prompt-prefix-cold.md`,
        `2026-10-16-1551-indexscan-guard-cold.md`,
        `2026-10-16-1551-shared-report-contract-cold.md` and
        `2026-10-16-1510-three-cues-cold.md`.
      - **A second brief-template defect from the same run:** the pre-flip-gate
        brief's own re-run line (`unittest tools.test_publishscan`) fails from
        the repo root (PF10), a recurrence of the round-2 pass's PL5; the brief
        template the 2026-10-16 briefs copy carries it.
      - **Proposed fix, for the house to weigh:** the brief (and the
        `review-brief` skill's template) names the exact body-free commands —
        `git show --stat --format=%s <sha>` for subject and stat,
        `git diff <sha>^ <sha> -- <paths>` for the diff — and says why the plain
        `git show` is barred; `coldsweep` gains a `--commit <sha>` form that
        prints exactly those, so the sweep tool and the commit read share one
        exclusion. The re-run line is corrected in the template and checked by
        a brief-writer running it once before writing it.
      - review: not owed until the fix lands; the fix touches the skill template,
        which is doctrine by function, so it queues its own ⏳ at landing.

  **Closed 2026-10-18** by a Mike-opened Opus 5.5 queue run, as proposed.
  `tools/coldsweep.py --commit <sha> [--path <p>]` prints the subject, stat
  and diff against the first parent, and never asks git for the body. Rule-2
  barred files (`docs/SESSIONS.md` and the like, which landing commits often
  touch) are left out of the diff too, and named by file only. Built by a
  Sonnet worker and read before merge. The new tests include a control that
  plain `git show` does print the body marker, so the absence checks are not
  vacuous. The tools suite went from 1916 to 1930 tests, all passing. A real
  run on `adf75a4` matched none of that commit's body lines. The
  `review-brief` skill now names the command and why `git show` is barred, and
  has the brief-writer run each re-run line once before writing it (the PF10
  defect). The skill text is doctrine by function, so its cold pass is queued
  at `160/930`.
