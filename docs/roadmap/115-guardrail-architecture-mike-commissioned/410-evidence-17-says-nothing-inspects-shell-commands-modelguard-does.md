- [ ] 🔎 **`EVIDENCE.md` §17 says its class is not mechanisable because
      "nothing inspects a session's shell invocations"; `tools/modelguard.py`
      does.** Found 2026-11-16 UTC by the `020/220` census, slice 1 (row
      CON21), and checked by the orchestrator of queue run 78ca9153 the same
      hour. `modelguard` is a Claude Code `PreToolUse` hook that reads the
      command text a session hands to Bash, before it runs, and denies a
      `claude` start with no `--model`. So the premise of §17's **No guard**
      sentence (a check in the same invocation as the act it guards) is false
      on this harness: a `PreToolUse` reader could see `<check> && <act>` or
      `<check>; <act>` in one command. Whether it *should* (false positives on
      every compound command; the hook fails open and does not exist in a
      cloud session, `020/460`) is the open design question, not the
      wording. **Owed:** correct §17's premise, and decide whether its class
      gets a warn-only `PreToolUse` reader, ranked by `020/240`'s value test.
      Doctrine, so its own cold pass when changed. Not fixed in passing, per
      the house rule that a doctrine defect is reported, not patched quietly.
