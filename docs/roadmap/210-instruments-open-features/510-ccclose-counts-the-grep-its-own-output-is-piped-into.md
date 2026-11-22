- [ ] **Hand-up from a private child: `ccclose` blocks a close on the
      `grep` its own output is piped into.** Seen 2026-11-22. When a
      session runs `ccclose … | grep …` from the Bash tool, *Launched work
      finished* fails with one `live process: ugrep -G --ignore-files` that
      "carries this session's id". The pid is new on every run and the
      process is about 1 s old. That `ugrep` is the harness's `grep`
      stand-in on the receiving end of the same pipeline: a sibling of
      `ccclose`, not anything the session launched. The same run written to
      a file instead of a pipe passes the check. (The child's own
      backgrounded `ccclose … &`, used to catch the process, was then
      flagged as a detached launch. That one is correct.)
  - Cost: a session that reads the ❌ goes looking for a runaway process
    that does not exist, or learns to ignore the check.
  - Fix, one of: exclude processes in `ccclose`'s own process group or
    pipeline (the same session id with the same parent shell, started
    within a second of `ccclose` itself); or say in `--help` and `man
    ccclose` to write the output to a file, never pipe it. Add the piped
    case to the check's tests.
