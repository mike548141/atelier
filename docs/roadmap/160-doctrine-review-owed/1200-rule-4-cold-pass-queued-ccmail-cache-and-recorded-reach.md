- [ ] 🎯 **Rule-4 cold pass queued: `ccmail`'s cache is private and expires,
      and its domain-wide reach is written down (`210/130`).** A tool holding a
      credential now deletes files on a sweep. The authoring session (a
      principal-opened Opus 5.5 queue run, session 722ac2e2, 2026-11-09, in its
      ruling round, which dispatched the Sonnet worker that wrote it) queues this
      and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection; the
      pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccmail`, its tests and man page,
      `instruments/README.md`, `instruments/ccpdf/`,
      `docs/decisions/0006-instruments-in-atelier.md`, `CHANGELOG.md` — the commit
      that closes `210/130`, on `main`, 2026-11-09.
      *Questions worth the pass's time:* whether the sweep can delete anything
      outside its own cache; whether the addendum's threat table is complete.
      *Intent record:*
      [`../210-instruments-open-features/130-*`](../210-instruments-open-features/).
      *Brief:*
      `docs/reviews/2026-11-09-0153-ccmail-cache-and-recorded-reach-cold.md`,
      written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5
      brief-writer started by `74f2b8cd` (neither may run it); its
      held-back sibling holds one pointer block, 3 questions and 2
      facts. *Size:* large. The pass waits for his approval of Fable.
      🔒 2026-11-22T19:54Z: claimed for the Fable pass by a headless per-pass
      orchestrator (Opus 5.5, rule-4 off-tier orchestrator: it holds the
      partition and forms no finding), started by drain session eca14b23; the
      reviewer is a Fable 5.1 subagent, tier checked at selection. Neither is
      barred by the brief. The approval is his drain order of 2026-11-23,
      verbatim: *"Start a fable drain or whatever it is called now. Target 100%
      of weekly budget by 11.30am NZT todat"*. The held-back sibling is
      partitioned out of the review tree until act 1 is committed.
      ✅ 2026-11-22T20:17Z: PASS RAN (Fable 5.1, both acts; orchestrator as claimed).
      **Verdict: FAIL — 1 MAJOR, 2 MODERATE, 4 minor, 1 note (`CCR1`–`CCR8`).**
      Standing MAJOR, `CCR1`: the sweep deletes under whatever directory
      `CCMAIL_DEST` names (probed: `--status` removed four 40-day-old folders
      from an operator directory), while the man page says a chosen dest is
      never swept. MODERATE: `CCR2`, the old "stores nothing / your own mailbox"
      wording survives in the tool and ADR 0006; `CCR3`, the installed
      renderer predates the delta, so the pixel budget is not deployed.
      🎯 **Owed to him (rule 3, every finding is his):** (1) `CCR1`, how far
      the sweep may reach (counsel in the verdict); (2) `CCR3`, run
      `instruments/ccpdf/setup` once and whether install keeps it current;
      (3) `CCR7`, confirm or decline, in his own words, the standing
      per-route reach requirement on future instruments and the 30-day
      attribution; (4) bulk-approve the wording and small code fixes
      `CCR2`, `CCR4`, `CCR5`, `CCR6`, `CCR8` as one application commit.
      Recommendation: approve all four, `CCR1` first. *Routing:* an
      application session in this repo after his word; its diff earns its
      own cold pass. Verdict and folded sibling:
      `docs/reviews/2026-11-09-0153-ccmail-cache-and-recorded-reach-cold.md`.
      ✅ **Ruled 2026-11-22T23:25Z** (drain session eca14b23, a structured ask
      after the findings were laid out to him; picks verbatim):
      (1) `CCR1`, to "how far may the clean-up reach?": *"I accept your
      recommended option and want to cbe clear that you never delete any email
      from my gmail space. As a rule I only ever archive email, not delete. The
      only exception to that is the email that gmail deletes itself because its
      known SPAM in the spam folder. But I'm less concerned about deleting
      cached info"*. The recommended option was *"Own cache only"*: the sweep
      runs only in a root `ccmail` created itself, never one an environment
      variable supplied; `ID_RE` tightened to the sixteen-character id where a
      name is to be deleted; the man page's ENVIRONMENT entry says so; the
      probe becomes a test. His reservation, a check the build answers: no
      path in `ccmail` deletes mail in his mailbox (the cache is local files
      only).
      (2) `CCR3`: *"Claude installs + auto-keep (Recommended)"*: a session runs
      `instruments/ccpdf/setup`, and `instruments/install` rebuilds `ccpdf`
      when its source is newer than the installed binary.
      (3) `CCR7`: *"Yes, make it standing (Recommended)"* for (a), the
      per-route reach statement on every future credential-holding
      instrument, which joins the controls list the precedent clause points
      at; (b) goes in the bulk commit.
      (4) *"Approve all (Recommended)"*: `CCR2`, `CCR4`, `CCR5`, `CCR6`,
      `CCR8` and `CCR7` (b) as one application commit.
      *Routing:* an application session in this repo, not eca14b23; its diff
      earns its own cold pass.
