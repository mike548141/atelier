- [ ] 🔎 **A real credential pasted into an exempt fixture file is invisible to
      the floor, and it has already nearly happened.** Verified at HEAD
      2026-08-15: both `.leakscanignore` and `.secretscanignore` exempt
      `tools/test_leakscan.py`, `tools/test_secretscan.py` and
      `tools/test_signscan.py`. Every exemption is reasoned, narrow and correct
      under `GUARDS.md` — a scanner's own tests are by construction a wall of
      credential-shaped and leak-shaped fixtures, and scanning them yields only
      noise. This item does not argue for removing them.
      **The residual the exemption cannot see:** nothing inside an exempt file
      distinguishes a deliberately fictional shape from a real one. The
      2026-07-28 record names the live near-miss — two real values from a
      private repo went verbatim into a test file, on this public repo, and the
      floor passed them clean precisely because fixtures are exempt. It was
      caught by a last look, not by a gate. The record's own words: *"no gate
      would have caught this."*
      **Why this is the evidence-window rule's own worked example.** The
      licensing fact — *this string is fictional* — is not in the file, not in
      the scan, and not derivable from the value. It lives in the author's head
      at the moment of writing. That is the predicate exactly, and it says the
      answer is not a cleverer scanner.
      **Candidate shapes, none built, each cheap:** a canary requiring fixture
      values to carry a declared fictional-source marker; a commit-time prompt
      when an exempt fixture file grows; or accepting the gap explicitly in the
      ignore files' own reasons, which today state why the exemption is safe
      without naming what it gives up.
