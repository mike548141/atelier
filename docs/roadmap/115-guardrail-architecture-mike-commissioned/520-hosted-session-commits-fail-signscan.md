- [ ] 🔎 **28 commits made by hosted cloud sessions fail `signscan`, and
      `SIGNING.md` says nothing about them.** Found 2026-11-23 UTC by
      `020/220` slice 5; re-run by queue run 608d8123 the same hour:
      `signscan --allowed-signers allowed_signers --boundary 450b10d --warn`
      over atelier's `main` gives 2575 good, 29 bad, 72 deferred (GitHub
      web-flow). 28 of the bad are SSH-signed with a key not in
      `allowed_signers` ("No principal matched"), committer `Claude`, dated
      2026-10-17 and 2026-10-18 (the cloud Fable run of that weekend); one
      is unsigned (`0a949b4b`). Under warn-first they are warnings; the
      flip to blocking turns them red, and history cannot be re-signed
      without a rewrite. What is owed: say in `SIGNING.md` how a commit
      made by a hosted session is trusted (its key added to the trust list
      with a validity window, a recorded exception for that range, or
      hosted sessions barred from committing to `main`), and decide it
      before the flip. Adding a key to the trust list widens who can sign
      as the house, so the choice is the principal's.
      *Measured 2026-11-23 ~19:20 UTC (same run), for his question whether
      trusting the key opens his risk to anyone using the hosted product:*
      GitHub marks the 28 commits verified, against the committer account
      `claude` (the vendor's no-reply address), not his account; his account's
      only signing key is atelier's own. So the key is held for a shared
      vendor identity, not for him, and adding it to `allowed_signers`
      would make a signature from that identity read as the house's.
      **It is one key for every customer:** the signing key is the
      vendor account's published `claude-prod-signing-key`, and the same
      fingerprint signs cloud-session commits in three unrelated owners'
      public repos (checked by `ssh-keygen -Y check-novalidate` over each
      commit's signature). Trusting it would make any hosted-session
      commit, anyone's, read as the house's. Pushing to his repo still needs his
      access, so the trust list's loss would be authorship proof, not
      write access.
