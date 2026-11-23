- [x] **`modelguard` refuses a Bash call that only looks up the `claude`
      binary.** Seen 2026-11-22 (session 12a41aa2): `ls … ; command -v claude`
      was blocked as "starts a Claude session with no `--model`". A lookup
      (`command -v`, `which`, `type`, `ls` of the path) starts nothing. The cost
      is small (re-word the command), but a guard that refuses harmless work
      teaches sessions to route around it. Fix: treat `claude` as a launch only
      in command position, not as the argument of a lookup; add the case to
      `tools/test_modelguard.py`.
      ✅ **Done 2026-11-23** (queue run c7a1e36e, with `210/470`'s FL7 by the
      same Opus worker): `modelguard` treats `claude` as a launch only in
      command position, so `command -v`, `which`, `type`, `whence`, `hash`
      and `ls`/`stat`/`readlink` of the path pass (26 lookup cases in
      `tools/test_modelguard.py`), while FL7's 41 bypass shapes are denied.
      After a head it does not know, a later `claude` word with arguments
      still counts as a launch (fail closed), so a rare harmless command
      like `docker run --name claude img` is refused; checked by the run
      against ordinary session commands, which all pass, and under the
      system Python 3.9 the hook is wired to. Covered by the `160/1450`
      re-check that `210/470` asks for.
