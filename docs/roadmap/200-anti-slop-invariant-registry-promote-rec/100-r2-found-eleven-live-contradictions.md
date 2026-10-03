- [ ] 🔎 **The R2 survey found eleven places where the doctrine's own copies
      already disagree** `[M][doctrine]`. Found 2026-10-03 by `040`'s
      claim-keyed duplication pass. Each is filed here as a defect with its
      evidence, per `CLAUDE.md`'s report-don't-patch rule, and none is fixed
      in passing. Six were re-read first-hand by the orchestrator before
      filing (C1, C2, C4, C5, C6, C10). The rest are as the survey reported
      them. Line numbers are at `729c74b`.
    - [x] **C1 (contradiction, safety floor).** `skills/queue-run/SKILL.md:49`
          tells a run to `git pull --rebase --autostash` with no status-first
          gate. `CONCURRENCY.md:177-189`, the floor block and atelier's own
          `CLAUDE.md` say: check status first, and stop and move if the dirty
          work is a peer's. The skill's own header says it "may compress,
          never contradict".
    - [x] **C2 (contradiction).** `REPO-STANDARD.md:222` says to create the
          remote private, and that "push is recoverable, so it needs no
          confirmation". `skills/create-repo/SKILL.md:213-219` says the
          authority is the principal's ask, *not* "push is recoverable", and
          to confirm when the ask didn't include a remote.
    - [x] **C3 (drift).** `RECORD.md:230` says there is no harvest step, and
          `RECORD.md:275` calls harvesting part of the close.
          `CONCURRENCY.md:915`, `skills/queue-run/SKILL.md:74` and
          `session-open-prompt.md:123` list "roadmap harvested"
          unqualified. Only `RECORD.md:233-236` reconciles them, by board
          mode.
    - [ ] **C4 (contradiction).** `CONCURRENCY.md:20-21` says the external
          venv is shared across worktrees. `STORAGE.md:56-59` says an
          in-repo `.venv` has been the norm since 2026-07-14.
    - [ ] **C5 (internal).** `CONCURRENCY.md:53` and `:60` say "two cues",
          and the bullets beneath list three.
    - [ ] **C6 (dangling pointer).** `SECRETS.md:76` and `:270` cite
          `DATA-PROTECTION.md`'s "stated-bridge rule", which that file does
          not contain. The rule is at `PRINCIPLES.md:265`.
    - [ ] **C7 (drift, highest stakes).** The always-confirm floor is listed
          five times with three memberships: `AUTONOMY.md:39-110` (the full
          set), `00-APEX.md:85-88` and `:111-115` (no unapproved-tool
          install), `method/README.md:14-16` (no trust surface, no
          unapproved tool), and a reworded list in
          `skills/session-onramp/SKILL.md:42-51`.
    - [ ] **C8 (drift).** The template reviews README hard-codes "on Opus"
          and "Fable" (`:15`, `:26-28`, `:84-85`). The template ECONOMICS
          says to apply fixes on the workhorse, and `ECONOMICS.md:326-338`
          makes the mid tier the executor. The README's own header says it
          carries nothing that can go stale.
    - [ ] **C9 (drift).** "What earns review" is listed six times and the
          lists differ (`REVIEW.md:395-436`, `ECONOMICS.md:350-371`,
          `skills/review-brief`, the template reviews README, the template
          CONTRIBUTING, `PROPAGATION.md:771-777`).
    - [ ] **C10 (contradiction).** `skills/review-brief/SKILL.md:87-92`
          says to apply findings "the same session". `REVIEW.md` rule 3 says
          the author applies nothing on self-authored doctrine until the
          principal decides. The skill also uses a PASS / FAIL vocabulary
          `REVIEW.md` does not define.
    - [ ] **C11 (drift).** The scope of "no personal data":
          `REPO-STANDARD.md:170-173` and atelier's `CLAUDE.md` scope it to
          repos bound for sharing. The child templates (`CLAUDE.md:131`,
          `CONTRIBUTING.md:103`) state it unconditionally.
      **Pattern worth naming:** four of the eleven (C1, C2, C8, C10) are a
      **skill or template that says it compresses its parent and then
      contradicts it**. That is the unwatched-stamp class `040` measured.
      `stampscan`'s region mechanism, extended to those artefacts, is the
      obvious lever. Whether to extend it is a decision, not a fix, so it
      is not taken here. Every fix above edits doctrine, so each is owed
      its rule-4 pass when it lands.
      💬 **Mike's answer, 2026-10-03, to a session's "fix one by one, or bind them
      mechanically" question:** *"ok one by one"*. It is recorded as an answer, not a
      ruling (`420/020`). Each contradiction is fixed separately, with its own
      rule-4 pass.
      ✅ **C1 fixed 2026-10-03.** `skills/queue-run/SKILL.md` step 2 now reads
      `git status` first, stops and moves on a peer's dirty work, and skips
      the pull with no upstream, as `CONCURRENCY.md` says. Pass queued at
      `160/520`.
      ✅ **C2 fixed 2026-10-03, in the more careful direction, and that choice
      is the session's.** `REPO-STANDARD.md` step 5 now matches the
      create-repo skill. The authority to create a remote is the principal's
      ask, not "push is recoverable", and if the ask didn't include a remote,
      confirm first. Neither side cited a ruling (`17ccbde` and `2271a44`), so
      the stricter reading wins until Mike says otherwise. Pass queued at
      `160/530`.
      ✅ **C3 fixed 2026-10-03.** RECORD's harvest trigger and the close lists
      in `CONCURRENCY.md` and `session-open-prompt.md` now say "harvest" only
      for a monolithic board, matching RECORD's own split-board rule. The
      queue-run skill's step 6 now says "roadmap close" too. Pass
      queued at `160/540`.
