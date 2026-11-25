- [x] ⏳ **Rule-4 cold pass queued: `ccfleet`, the `fleet-sweep` and
      `review-drain` skills, and `modelguard` (`210/440`).** A first-of-kind
      instrument that starts headless sessions with a permission mode
      across every repo, two skills that reach every plugin user, and a
      hook that denies tool calls, so the authoring session (559edaec, Opus
      5.5, headless, started by an estate health sweep, orchestrator session
      58027096, 2026-11-14) queues this and does not take it or brief it.
      *Tier:* the principal-named review tier, checked at selection.
      *Pass type:* code and design cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccfleet`,
      `instruments/ccfleet.example.json`, `instruments/test_ccfleet.py`,
      `instruments/README.md`, `skills/fleet-sweep/`,
      `skills/review-drain/`, `tools/modelguard.py`,
      `tools/test_modelguard.py`, `tools/README.md`, `CHANGELOG.md` (the
      commit that lands `210/440`, on `main`, 2026-11-14).
      *Intent record:*
      [`../210-instruments-open-features/440-ccfleet-per-repo-billed-headless-sessions-and-two-skills.md`](../210-instruments-open-features/440-ccfleet-per-repo-billed-headless-sessions-and-two-skills.md).
      No brief yet: a brief-writer that is not session 559edaec writes it.
      **Widened 2026-11-18 (session 84b7932e, board `450/010`):** the
      delta now also covers the three commits that closed `ccfleet`'s
      generic gaps and added to both skills (`17f158d2`, `d9d1589e`,
      `a025636e`, landed by `a025636e`). Write the brief over the code as it
      stands at that head, so the paid pass reviews what will run. Neither
      session 559edaec nor session 84b7932e (which commissioned the gap
      fixes) writes the brief. **This pass gates the estate's drain switch**
      (`450/010` row 2): the principal chose, 2026-11-18, to switch the
      weekly drain only after this pass is clean, and for this one pass
      *"Normal priority (Recommended)"* (his pick; the rest of `450`'s
      passes are low). **Drain priority: normal (principal, 2026-11-18).**
      **Widened again 2026-11-18:** add `1eb42f54` (three faults the first
      real estate run found: fresh `kit_dir`, failing queue `next`, dry
      passes' `END` line). The brief covers `main` at or after it.
      🔒 CLAIMED 2026-11-20T08:25Z (claimed 2026-11-20-0825, wt: atelier-qr-08cd-brief1450) by queue-run
      session 08cd3b95 (Opus 5.5, principal-opened). Scope: write the brief and its held-back sibling; no pass run.
      **Brief written 2026-11-20 UTC:**
      [`docs/reviews/2026-11-20-0813-ccfleet-fleet-sweep-review-drain-modelguard-cold.md`](../../reviews/2026-11-20-0813-ccfleet-fleet-sweep-review-drain-modelguard-cold.md),
      over `main` at `71c867bc` (all six delta commits, through
      `1eb42f54`, plus the manual page). Its held-back sibling is held
      user-local, outside the repo, every worktree and every
      scratchpad. Brief-writer: a worker (Opus 5.5) of queue run
      `08cd3b95`, which authored, started and instructed none of the
      delta; it formed no finding and will not start the pass. Barred
      from running it: `08cd3b95` and its workers, and `559edaec`,
      `58027096`, `78ca9153`, `84b7932e` with all they started. The pass
      stays `⏳` for a criterion-passing cold Fable session, on the
      principal's explicit permission for Fable work.
      🔓 2026-11-20 UTC: queue run 08cd3b95 releases its brief-writing claim at
      the landing; the pass itself stays open and `⏳`.
      💬 **Fable approved for one pass, conditioned, 2026-11-20 UTC**, through the
      device at queue run 08cd3b95's close, his answer verbatim, typed in place
      of the options: *"I approve one pass so that ccfleet can be fixed and is
      ready to use. But the parallel session working in this repo right now is
      making changes based on my directions and they may change what it is the
      reviewer is reviewing. Once that session is finished we can update the
      brief if things have changed and then run the one fable review"*. So:
      one Fable pass, run only after that session has finished; first check
      `git log` on the delta paths since the brief's pinned head and, if they
      moved, update the brief (by a session that may write it) before the pass.
      The run that wrote the brief neither updates it nor starts the pass.
      `cclive` at the time of the answer showed no other atelier session on
      this machine, so which session he means is not identified here.
      **Delta moved, 2026-11-20 (session 64f984ac, the parallel session
      named above; finished):** one commit landed on this pass's paths
      since `71c867bc`: `c60dee8b`, on `instruments/ccfleet` (`drain`
      requires and calls `queue.ranked` before the first pick),
      `instruments/test_ccfleet.py`, `instruments/ccfleet.example.json`,
      `instruments/man/ccfleet.1` and `skills/review-drain/SKILL.md`
      (§ *Rank and route the whole queue first*). It closes no item; its
      own cold pass was queued as `160/1660`. If this pass's updated brief
      takes `c60dee8b` in, `160/1660` folds into it and closes on its
      verdict. Session 64f984ac is an author of this delta and neither
      briefs nor runs this pass.
      **Brief updated 2026-11-20 UTC to `bd9f6a9b`** by a brief-writer
      worker of queue run 08cd3b95 (which authored, started and
      instructed none of the delta): it takes in `c60dee8b` (session
      64f984ac, the ranking gate) and `bd9f6a9b` (session 19378351, the
      fleet sweep's board and scope rules); no other commit touched the
      delta paths. `160/1660` is folded in: one pass, one verdict, closing
      both. Barred from running the pass now also: 64f984ac and 19378351
      with all they started. The principal's approval stands for one Fable
      pass, over a delta that has stopped moving: `cclive` at the update
      still showed both author sessions live, so the pass first re-checks
      the brief's since-line and stops if it is not empty.
      🔀 **Correction, 2026-11-20 UTC (queue run 08cd3b95):** the line above
      reading "The run that wrote the brief neither updates it nor starts the
      pass" was this run's own wording, not the principal's, and it was too
      wide. His words were "we can update the brief if things have changed";
      a brief-writer that authored none of the delta may update its brief
      (`REVIEW.md` rule 4 bars authors, and the brief-writer from running the
      pass). So this run updated the brief and still neither starts nor runs
      the pass. Before the pass: check that session 19378351, an author of
      `bd9f6a9b`, has finished, and that the since-line in the brief is empty.
      🔁 **Brief updated again, 2026-11-21 UTC (queue run 08cd3b95, orchestrator):** the
      since-line was no longer empty: `b68cf410` (a worker of 19378351, already barred) reworded
      the fleet sweep's healthy item 6 and two prompt templates. Taken in as question 30; the
      rest of that commit stays with its own pass, `160/1700`. Since-line empty at `b68cf410`.
      **Delta, 2026-11-21 (session 64f984ac, an author, so barred as before):**
      the since-line is no longer empty: this commit rewrites
      `skills/review-drain/SKILL.md` § *Rank and route the whole queue first*
      so routes order by when each budget lapses, cost breaking a tie (the
      principal's clarification of "cheapest"). Take it in before the pass,
      as with `c60dee8b`; the question to add: does the lapse-first route and
      the spill rule (the local route never takes from a budget lapsing
      sooner) match the principal's words as summarised there.
      🔁 **Brief updated a third time, 2026-11-21 UTC (queue run 08cd3b95, orchestrator):**
      `e002ea22` taken in as question 31, with the author's question attributed to it; the
      principal's words stay private, the skill's paraphrase is what the reviewer reads.
      Since-line empty at `e002ea22`.
      🔒 CLAIMED 2026-11-22T01:16Z (claimed 2026-11-22-0116, wt: atelier-rv1450) by session
      5106cf48 (Opus 5.5, principal-opened), as orchestrator of the one approved Fable pass.
      Off-tier, disclosed: it forms no finding and writes no severity; it holds the context
      partition, spawns one fresh Fable reviewer in its own worktree and commits the records.
      Checked first: the since-line is empty at `e002ea22`; author sessions 64f984ac and
      19378351 have finished (no live atelier session but this one). Not barred: it authored,
      started and instructed none of the delta and wrote no brief.
      ❌ **PASS RAN 2026-11-22** (one fresh Fable reviewer on the laptop, the principal's
      2026-11-20 approval, in worktree `atelier-rv1450`, under the off-tier orchestrator session
      5106cf48, which formed no finding; act 1 at `1b98b593`, act 2 and the folded sibling at
      `a297c90c`, in
      [`docs/reviews/2026-11-20-0813-ccfleet-fleet-sweep-review-drain-modelguard-cold.md`](../../reviews/2026-11-20-0813-ccfleet-fleet-sweep-review-drain-modelguard-cold.md),
      pinned at `f767033a`). **FAIL — 2 MAJOR · 10 MODERATE · 10 minor · 3 notes** (FL1–FL25;
      FL23–FL25 formed at reconcile). **Paid review work can be lost or misread: yes.**
      **MAJOR:** **FL1** a cut-off pass can be read as DONE, its claim released and its worktree
      force-removed with the verdict uncommitted; **FL2** the launched list records offers, not
      starts, so a dry run or an outage ends a later drain on a false "queue empty".
      **MODERATE:** FL3 a killed pass leaves no session id; FL4 the close step deletes a waiting
      pass's live log; FL5 the sweep's staleness test fits a cut-off pass's worktree; FL6 `run`
      deletes a cut-off worker's work; FL7 `modelguard` passes 23 launch shapes with no model;
      FL8 the sweep's "adopt every no-pin repo" widens the principal's words and has no step;
      FL9 the reviewer prompt drops two rule-2/4 reader duties; FL10 no threat enumeration, and
      the example ships the widest permission mode; FL11 the lapse-first routing drops "when
      near" and keeps "unsure means the dearer route"; FL23 the private-name guard misses names
      joined by `-` or `_`. Minor FL12–FL19, FL24, FL25; notes FL20 (a canary cut-off-and-resume
      before any real drain), FL21 (shipping the two skills to every plugin user is the
      principal's call), FL22.
      🎯 **The principal's (rule 3):** every finding, nothing applied. The estate's drain switch
      (`450/010` row 2) stays off: this pass did not come back clean. Judgement calls inside the
      batch: FL8, FL11 (readings of his words), FL10, FL18 (where an approval rule lives), FL21.
      After the fixes, a re-check pass is owed and needs his Fable approval.
      🔓 2026-11-22 UTC: session 5106cf48 releases its claim; the item stays open for the
      principal's decision.
      💬 **The principal's answer, 2026-11-22 UTC (session 5106cf48, AskUserQuestion; an
      answer, not a ruling):** *"Fix all as advised (Recommended)"*, to an option reading: one
      fix item for all 25 as counselled; the five judgement calls taken the reviewer's way
      (adoption scoped to repos the config lists, never another owner's; unsure means the local
      route; the example drops the bypass permission mode; the approval rule stays an adopter
      setting, not generic doctrine; both skills stay in the plugin); then a canary on a
      throwaway repo, then he is asked about the Fable re-check. Carried by `210/470`.
      🔁 **Re-check briefed 2026-11-24 UTC** with `160/1790`, one pass, one
      verdict: [`docs/reviews/2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md`](../../reviews/2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md)
      (queue run 0b4f93ef's brief-writer; the principal's pick and approval
      are recorded on `160/1790`).
      🔒 CLAIMED 2026-11-25T02:05Z (claimed 2026-11-25-0205, wt: atelier-a9) for the
      RK Fable pass by session 4a34637a (`atelier-a9`, Opus 5.5, principal-opened,
      fresh: it authored, started and instructed no part of the delta or the
      brief). **Off-tier orchestrator, disclosed (rule 4):** it holds the context
      partition, keeps the held-back sibling (by count only here) outside the
      tree, commits the records and releases the sibling after act 1 is
      committed; it forms no finding and writes no severity. The reviewer is a
      fresh Fable subagent it spawns, process-only prompt recorded in the
      verdict. Since-line at `7544c943` empty. One pass, one verdict, closing
      `160/1450`, `160/1790` and `160/1740` and reviewing `450/030`.
      ✅ **PASS RAN 2026-11-25 UTC** (one fresh Fable reviewer, in worktree `atelier-a9`, under
      the off-tier orchestrator session 4a34637a, which formed no finding; act 1 at `60938dc9`,
      act 2 and the folded sibling in the next commit), in
      [`docs/reviews/2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md`](../../reviews/2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md), pinned at `2111e260`, FL ledger re-driven at `60938dc9`.
      **PASS-WITH-FINDINGS — 0 MAJOR · 11 MODERATE · 14 minor · 4 notes** (`RK1`–`RK29`;
      `RK29` formed at reconcile).
      **Re-check:** all 25 first-pass findings re-driven; both MAJORs (`FL1`, `FL2`) fixed as
      counselled; 21 fixed as counselled, 1 another way, 2 partly (`FL17`, `FL20`), 1 decided with
      no change; none unfixed or regressed. Two fixes moved risk (`FL1`/`FL14` to `RK3`, `FL7` to
      `RK9`) and the rename undercut `FL9` (`RK2`); those ride on `160/1790`.
      🔓 2026-11-25 UTC: session 4a34637a releases its claim; the re-check is done and this
      item closes. Every RK finding is the principal's to rule, on `160/1790`.
