- [~] 🔥 **`modelguard` refuses plain SSH as a user named `claude`.** Handed
      over mid-run 2026-11-23 ~12:09Z by a peer queue-run session in a
      private child, class only: after the `210/470` rewrite went live,
      `ssh -i <key> claude@<host> 'sh -s' < script` and `ssh -i <key> -l
      claude <host> 'sh -s' < script` were both refused as "starts a Claude
      session with no --model"; the same command passed before. Every repo
      that reaches its hosts as that SSH user is blocked from routine host
      reads. Cause: `command_name` drops everything after `@` (meant for
      `claude@1.2`, a package version), so `claude@host` reads as the
      binary; and `ssh` is an unknown head, so the fail-closed rule fires
      on any later `claude` word with arguments (`-l claude host`).
      **Fix:** strip `@…` only when it is a version or tag; read `ssh`'s
      options and destination as data and only its remote command as code
      (so `ssh host claude -p …` is still refused); `scp`, `sftp` and
      `rsync` are data heads.
      *(claimed 2026-11-23 UTC, session c7a1e36e, wt: atelier-qr-c7a1-claims)*
