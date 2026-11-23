- [x] 🔥 **`modelguard` refuses plain SSH as a user named `claude`.** Handed
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
      ✅ **Done 2026-11-23** (queue run c7a1e36e, inline, within the hour
      it was reported): as the fix above says. Tests in
      `tools/test_modelguard.py`: six SSH/scp/rsync forms in LOOKUPS (they
      fail on the previous hook) and two remote-`claude` forms in BYPASSES;
      passes under the system Python 3.9 the hook is wired to. Covered by
      the `160/1450` re-check `210/470` asks for. Lesson for that re-check:
      the rewrite's fail-closed rule had no test drawn from the estate's
      ordinary host commands, only from session commands.
