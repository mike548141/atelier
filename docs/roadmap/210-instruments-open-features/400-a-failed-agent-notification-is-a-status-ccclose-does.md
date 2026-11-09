- [x] 🔎 **A `failed` agent notification is a status `ccclose` does not know,
      and the one signal that separates a dead agent cleanly.** Found 2026-11-09
      by queue run d0ca5d24 while measuring `210/070`. Of 3,587 real agents the
      parent recorded `<status>failed</status>` for 50, none of which ended on
      `end_turn`. `ccclose` reads any status outside completed, killed and
      stopped as "notified with status failed, which ccclose does not know"
      and warns, so a dead agent shows as an unknown, not as a failure.
      **Shape:** name `failed` as its own state in `ccclose` check 12 (a fail,
      printed on its own count), and decide whether `cctranscript`'s header
      should count notification statuses from the parent log it already reads,
      without opening any agent log. Read the status census first; the other
      statuses seen are `completed`, `killed` and `stopped`.
  - 2026-11-10: done. `failed` is its own state in `instruments/ccclose` check
    12: a fail, judged before the launch's `tool_result`, counted as `failed` in
    the summary line, `--json` `counts` and the identifiers block (known zero
    when none); an unrecognised status still warns. Pinned in
    `instruments/ccclose.test.js`; `instruments/ccclose.design.md` and
    `instruments/man/ccclose.1` carry it. Second question: `cctranscript`'s
    header is left as it is. A task notification also covers background
    commands (a real log shows "Background command" summaries), so a count
    from the parent log alone would mix them with agents; each notification
    arrives in up to three carrier shapes and needs de-duplicating by task id;
    and the header's chips are compared across records. `ccclose` is where a
    status is judged.
