- [~] (claimed 2026-10-04-2329, wt: atelier-ccarchive-1005) **`ccarchive --install-schedule` recreates a login job Mike removed —
      drop it** (handed up by a private child, 2026-10-05, over the channel;
      Mike: *"yes hand them over"*)

      On 2026-10-05 Mike removed ccarchive's launchd agent
      (`com.ccarchive.archive`, shown in Login Items as "Node.js Foundation")
      from his Mac. His standing rule now: no background jobs, and never a
      script running under an interpreter as a login item. The one exception
      is `ssh-add`, which fixes a problem reboots cause. ccarchive now runs by
      hand, prompted by a shed board item when the archive is 28 or more days
      old.

      `--install-schedule` (with `--schedule-status` and
      `--uninstall-schedule`) still writes and loads exactly the job he
      removed. **Remove `--install-schedule` and `--schedule-status`**; update
      `--help` and the man page to say the tool is run by hand.
      `--uninstall-schedule` may stay, to clean up an old install on another
      machine — the builder's call; drop it too if it adds nothing once the
      install path is gone.

      *Supersedes:* `210/010` ("ccarchive exits 1 on every scheduled run") —
      there is no more scheduled run for that item's shrink-guard exit to
      affect. Leave `210/010` open; note this on it when the fix lands, don't
      close it in passing.
