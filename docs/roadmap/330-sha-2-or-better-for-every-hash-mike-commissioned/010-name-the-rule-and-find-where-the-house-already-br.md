- [~] **Give the rule a home, then sweep for where the house already breaks
      it.** Two halves, and the second is the one that earns the item.
  - [x] **Where the rule lives.** It is a *how we build* preference, not a safety
        floor — nothing catches fire if a hash is weak, so it does not belong at
        the apex. Likely `PRINCIPLES.md` or the conventions surface, as one line:
        **use SHA-2 or stronger (sha256/sha512, SHA-3, BLAKE2/3) for any hashing
        or checksum; never MD5 or SHA-1.**
  - [ ] **Then sweep the estate's own tools.** The commission is only worth the
        filing if the house obeys it. `grep -rn "md5\|sha1"` across `atelier/tools`
        and the children — verification scripts, manifest builders, cache keys,
        fingerprints, test fixtures. 🔎 **Expect false positives worth keeping:**
        a `.md5` file published by an upstream vendor is theirs to choose, and
        checking a download against it is correct even though the algorithm is
        weak. The rule governs what *we* emit, not what we verify against.
  - [ ] ⚠️ **Do not turn this into a scanner without thinking.** A `hashscan`
        would be cheap to write and would fire on every legitimate
        upstream-checksum case, on documentation quoting a historical digest, and
        on git's own object ids. The estate already carries a lesson about guards
        that flag more noise than signal. **Decide the rule first; decide whether
        it is mechanically checkable second, and separately.**
  - [x] 🔑 **Carry the class, not just the instance.** The useful generalisation is
        broader than hashing: **where the principal has a standing preference about
        a primitive, the agent should not pick one silently on adequacy grounds.**
        Compression, encoding, key sizes, cipher suites and RNG sources are the
        same shape. Worth one line alongside the rule, because the next instance
        will not be a hash.
      - 🔀 Tidied 2026-11-16 (C0553, verified high; Mike approved 2026-11-16):
        not an ask of Mike. He commissioned the SHA-2 rule (the section's
        title); giving it a home and sweeping for where the house breaks it
        (line 1) is agent work. Nothing above was changed; the original text is
        as it was. To revert: delete this line (its commit is listed in
        `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
      - 🔀 2026-11-16 (C0553): removed the 🎯 marker from this item's first line,
        because this ask is not Mike's (tidy line above). Original: that line
        began `- [ ] 🎯`. To revert: git revert this repo's marker commit (listed
        in `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
      🔒 CLAIMED 2026-11-16T11:11Z (claimed 2026-11-16-1111, wt: qr-78ca-principles) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).
      - 2026-11-16: the rule and its class line landed in
        `docs/method/PRINCIPLES.md` §5 (not `CONVENTIONS.md`, which declares the
        frame a value is read against; this is a build-time security choice),
        with the upstream-checksum, git-id and format-mandated exemptions.
        **Sweep, atelier only (tools/, instruments/, docs/, skills/, hooks and CI,
        read-only): no break found.** Everything we emit is SHA-256
        (`tools/leakscan.py:1580`, `instruments/ccarchive:660,797`,
        `instruments/ccmail:962`). Not breaks: `tools/secretscan.py:678-687`
        recognises MD5 fingerprints on read (emits none); `zlib.crc32` in
        `tools/leakscan.py:3492` builds PNG chunks and `crc32` in
        `instruments/ccmail.test.js:31` / `tools/test_leakscan.py:2243` builds
        PNG/zip fixtures (format-mandated). Two past review records ran `md5` as
        a same-file check (`docs/reviews/2026-10-18-0511-template-history-privacy-cold.md`,
        `docs/reviews/2026-08-15-1033-communication-floor-cold.md`), records not
        tooling, kept as written. Nothing is owed for atelier. **Still owed:** the
        sweep of the child repos (outside this repo), and the separate decision on
        whether a scanner is worth it.
      🔒 CLAIMED 2026-11-20T07:40Z (claimed 2026-11-20-0740, wt: atelier-qr-08cd-hashsweep) by queue-run
      session 08cd3b95 (Opus 5.5, principal-opened). Scope: the read-only sweep of the child repos.
