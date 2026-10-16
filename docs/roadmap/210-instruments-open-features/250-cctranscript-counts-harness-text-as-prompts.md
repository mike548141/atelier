- [x] 🔎 **cctranscript counts some harness text as the principal's prompts**
      `[S][instruments]`. Found 2026-10-16 by the `020/180` worker while
      building `ccclose` on top of cctranscript's classifiers, and checked on
      a fixture before filing. `readTurns` treats every user-type record
      without a tool result as a turn of the principal's and numbers it as a
      new exchange. That includes records that are wholly a background-task
      notification, records the harness marks as meta, and an injected
      browser-instruction block joined onto a real prompt. On a synthetic
      fixture, `cctranscript --json` gave a task notification the principal's
      role and its own turn number. `ccclose` filters these for its list of
      asks, but keeps cctranscript's numbering so turn refs line up. **The
      work:** classify these records as harness text in cctranscript itself,
      decide whether they keep a turn number, and keep `ccclose`'s refs in
      step. Related: the authorship classification recorded in this repo's
      memory notes, where only part of one record type is the principal's
      typing.

      ✅ **Done 2026-10-16** (1501 UTC queue run, a Sonnet 5.5 worker;
      `cea247e`, merged on `main` after the orchestrator read it and
      corrected one NZ-local date). One classifier, `classifyUserRecord` in
      cctranscript, now answers "is this the principal's?" for `readTurns`,
      the `--list` label and `ccclose`, so they cannot disagree. Meta records
      and records made wholly of harness wrappers get the role `harness`:
      grey and clipped in the render, counted apart in the header, full text
      in `--json`. An injected browser-instruction block is stripped from the
      prompt it was joined to. **Harness text keeps its exchange number**, so
      refs already quoted in records do not move. That choice is the
      worker's and stands on that reason, and dropping the number is a
      one-place change if ever wanted. On 12 recent sessions, "you" fell
      from 181 to 56 with every last ref unchanged. Instruments suite: 443
      of 443. 🔎 Found, not fixed: a notification arriving as an
      `attachment` or `queued_command` record is still not read at all,
      while the same text as a user record now shows as harness. Filed as
      `210/260`. Review queued at `160/880`.
