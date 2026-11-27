- [x] 🔎 **28 commits made by hosted cloud sessions fail `signscan`, and
      🔒 Claimed by session 9c5fa72c (`atelier-fa`, Opus 5.5), principal-opened by
      `/atelier:work run`.
      (claimed 2026-11-27-0915, wt: atelier-qr-9c5f-signscan)
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
      💬 **Answered 2026-11-23 ~19:50 UTC (session 608d8123, AskUserQuestion, after the measurement above was put to him in plain terms), his pick:** *"Accept + cloud hands back"*
      (option text: *"Same, and cloud sessions never land changes on main
      themselves; your own sessions land them"*, the "same" being: accept
      the 28 as past history and do not trust the vendor key). **Now build
      work, owed here:** record the 2026-10-17/18 range (and the unsigned
      2026-09-16 merge) as an accepted exception that `signscan` reads, so
      the flip does not red on history; leave `allowed_signers` as it is;
      and say in `SIGNING.md` that a hosted session hands its work back (a
      branch or PR) for a local session to land, never committing to
      `main` itself. The build earns its own cold pass.
      ✅ **Done 2026-11-27 (session 9c5fa72c queue run, `atelier-fa`).** Built
      as ruled. `signscan --accepted <file>` reads a list of accepted
      commits: one full commit id per line under a stated reason (the house
      reason grammar), no ranges, no committer-wide entries, abbreviations
      refused; a listed commit that fails is reported and counted as
      *accepted*, apart from good and bad, and never blocks; an unlisted
      commit, including a new one by the same committer, still fails; a
      malformed list exits 2 even under `--warn`. `.signscanaccept` lists the
      29 by full id; `ci.yml` passes it beside the trust list (still
      `--warn`); `allowed_signers` untouched. `SIGNING.md` gains § *Commits
      made by hosted sessions* with the ruling in his words and the
      hand-back rule. Measured over `450b10d..HEAD` from the worktree:
      before, 2826 good, 29 bad, 72 deferred (the 28 plus `0a949b4b`, matching
      the count above); after, in blocking mode with the list, 2826 good,
      0 bad, 29 accepted, 72 deferred, exit 0. The flip itself is not made
      here. Cold pass owed.
      - Commitment: an exception list a security guard reads, that excuses
        exactly the named commits and nothing else, and that fails loudly
        when it is malformed, so the flip to blocking can rest on it.
      - Worst failure: the list excuses more than it names (a prefix, a
        parse quirk, or a later commit treated as listed), so an unsigned or
        foreign-signed commit lands on `main` and reads as accepted history.
      - Why the floor misses it: under warn-first no run can fail on
        signatures at all, and the tests use throwaway unsigned repos, so a
        widening shows only as a smaller bad count that nobody compares.
