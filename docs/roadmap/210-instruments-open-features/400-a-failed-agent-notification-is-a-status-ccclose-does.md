- [~] (claimed 2026-11-09-1354, wt: atelier-qr-d0ca-instr2, session d0ca5d24) 🔎 **A `failed` agent notification is a status `ccclose` does not know,
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
