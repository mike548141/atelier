- [x] **P2 — `publishscan` built and registry-wired blocking, 2026-07-29.**
      The guard for the class P1 exposed: it reds when a repo *tracks* a file
      whose publication weakens it, judging the **path** rather than the
      contents. That is the one question no other scanner here asks, and it is
      why `secretscan` and `leakscan` both passed `rpi`'s allowlist correctly —
      the file holds no credential and no personal fact; the exposure was its
      presence. 14 tests; driven live red on the real defect (staging the
      allowlist back into the index) and green on the tree; full suite 820 OK.
      Patterns carry their provenance rather than blurring it: the
      `.claude/settings*.json` pair is grounded in F1, the rest (`.mcp.json`,
      `.env*`, `.envrc`, `.netrc`, `.npmrc`, `.pypirc`, editor-local config) is
      named as standard practice. It offers an **advisory** form — unusual for
      a boundary check, and for an adoption reason rather than a severity one:
      eleven children track the allowlist today, and a blocking check arriving
      by propagation would red their next commit for a file nobody has told
      them about. It deliberately **allows** the self-describing guard files
      (`.atelier-floor.json`, the `.<scanner>ignore` set) — they map where the
      defences are weak *and* must travel for the floor to run, so that
      exposure is accepted and mitigated by requiring a stated reason for every
      exemption, never by hiding the files. **Residuals, stated:** it is a
      denylist, so a novel defence-mapping file passes until someone teaches it
      (P2a); and it cannot unpublish — history already pushed stays pushed.
      One design error, caught by `floor.py`'s own test suite rather than by
      review: the first cut hard-failed on a tree with no git, which would have
      made it unrunnable in every child's fixtures. Corrected to a visible
      exit-0 skip — with no git there is no tracked set to miss, so the claim
      is true rather than unverified — while every *other* git failure stays
      exit 2. (Moved from ROADMAP.md 2026-07-29, same commit that landed it.)
