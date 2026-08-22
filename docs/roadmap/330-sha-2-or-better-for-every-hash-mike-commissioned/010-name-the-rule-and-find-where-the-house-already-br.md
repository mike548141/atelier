- [ ] 🎯 **Give the rule a home, then sweep for where the house already breaks
      it.** Two halves, and the second is the one that earns the item.
  - [ ] **Where the rule lives.** It is a *how we build* preference, not a safety
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
  - [ ] 🔑 **Carry the class, not just the instance.** The useful generalisation is
        broader than hashing: **where the principal has a standing preference about
        a primitive, the agent should not pick one silently on adequacy grounds.**
        Compression, encoding, key sizes, cipher suites and RNG sources are the
        same shape. Worth one line alongside the rule, because the next instance
        will not be a hash.
