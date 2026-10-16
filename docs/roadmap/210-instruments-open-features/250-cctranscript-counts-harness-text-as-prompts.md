- [ ] 🔎 **cctranscript counts some harness text as the principal's prompts**
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
