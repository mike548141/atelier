- [x] 🔧 **A dry drain tells the queue refusing before its seal from the queue failing (the
      `DP17` leftover of `210/630`).** Today a dry drain reads any ordinary nonzero exit of the
      queue's `next` as "not sealed" and exits 0, so a broken queue rehearses as merely
      unsealed. The fix: the queue contract gains a refusal exit code for "not sealed", the
      reference queue uses it, and a dry drain reads only that code as "not sealed", any other
      failure as a queue error (exit 1).
      💬 **His answer, 2026-11-26 ~03:20 UTC (session 5e236e34, `atelier-cd`, AskUserQuestion;
      an answer, not a ruling)**, asked whether to accept the three `210/630` leftovers as
      recorded, on this one, verbatim: *"(2) This needs to be fixed."*
      🔒 CLAIMED 2026-11-26T03:25Z (wt: `atelier-cd-dp17`) by principal-opened session
      5e236e34 (`atelier-cd`, Opus 5.5), the author of the `210/630` fixes. It lands before
      `160/1870` is briefed, so that one review covers it; this session neither briefs nor runs
      that review.
      ✅ **Done 2026-11-26 UTC** (session 5e236e34): the contract's not-sealed code is exit 3
      (`QUEUE_NOT_SEALED_RC` in `ccfleet`, `NOT_SEALED` in the reference queue, both in the
      manual's queue interface and `skills/review/run.md`); a dry drain reads any other failure
      of `next`, exit 1 included, as a queue error. `test_dp17_…` gains the exit 1 and 2 rows
      and was seen failing on the old reader; `test_q2_…` pins the reference queue's 3.
      `test_ccfleet` and `test_ccfleet_dp` OK. Adopter action in the changelog: the estate
      root's queue must refuse with exit 3. Covered by `160/1870`.
