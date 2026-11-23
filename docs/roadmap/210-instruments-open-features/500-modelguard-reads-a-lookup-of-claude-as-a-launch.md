- [~] **`modelguard` refuses a Bash call that only looks up the `claude`
      binary.** Seen 2026-11-22 (session 12a41aa2): `ls … ; command -v claude`
      was blocked as "starts a Claude session with no `--model`". A lookup
      (`command -v`, `which`, `type`, `ls` of the path) starts nothing. The cost
      is small (re-word the command), but a guard that refuses harmless work
      teaches sessions to route around it. Fix: treat `claude` as a launch only
      in command position, not as the argument of a lookup; add the case to
      `tools/test_modelguard.py`.
      *(claimed 2026-11-23 UTC, session c7a1e36e, wt: atelier-qr-c7a1-skills)*
