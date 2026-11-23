- [ ] 🔎 **Five defects the enforcement census found in slice 4.**
      Found 2026-11-23 UTC by `020/220` slice 4
      (`docs/method/census/2026-11-23-1559-access-conventions-documentation-glossary-mechanisms-principles.md`,
      rows named below); reported, not fixed in passing. The orchestrator
      (queue run 608d8123) checked the first, second and fourth against the tree.
      1. **PRINCIPLES' scope sentence is stale.** The opening says the
         precedence ladder resolves collisions "among the design principles
         §1–9"; §10 (posture) and §11 (evaluation) exist. Either the ladder
         covers them and the sentence widens, or it does not and says so.
      2. **DOCUMENTATION principle 6 binds "as a review question" that no
         review asks** (DOC8). Neither `REVIEW.md`'s checklist nor the
         `review-brief` skill carries it. Either the question joins the
         checklist or the binding sentence changes.
      3. **"Versioned like an API" has no version to read** (DOC3): no
         `--json` payload in `tools/` or `instruments/` carries a version
         field (31 of 47 tools emit JSON).
      4. **GLOSSARY's "stated bridge" points at a section that covers one of
         its senses.** The entry spans a gap, a hand-action and a standing
         exception; the section it names covers the hand-action sense only.
      5. **`instruments/ccfleet` derives a log suffix with SHA-1** (PRI25,
         against PRINCIPLES §5, SHA-2 or better). Not a security use, but the
         rule has no carve-out; the fix renames the log a resumed reviewer
         looks for, so it wants a read-both transition. It is also the one
         hit that stops a weak-hash guard (the census's top candidate for
         `020/240`) landing clean.
      ✅ **Item 5 fixed 2026-11-23** (queue run 608d8123, inline): the log
      name hashes with SHA-256; `pass_log` still finds a log left under the
      SHA-1 or hashless name, and a fresh pass sets all three aside. Test
      in `instruments/test_ccfleet.py`. Items 1–4 stay open: each is a
      choice of which side moves.
