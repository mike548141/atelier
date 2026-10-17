- [ ] 🔎 **Hand-up: a scanner's `--selftest` prints its fixture findings in the floor's own shape, and a red run was diagnosed from them** `[S][tools]`. Handed up by a private child on 2026-10-17, under `PROPAGATION.md` § *Pointing up*. One measured misdiagnosis, with the job log as evidence; the fix is atelier's to choose. <!-- wrapscan:allow: a state line carries the whole state in one line so the index reads true -->

      **What happened.** The child's floor workflow — the thin caller of
      atelier's reusable `floor.yml` — has been red on every push since its
      first push after mid-September. The real cause is one enforced
      `secretscan` entropy finding in the child's own tree (inferred, not
      proved: a published URL's opaque query token, newly inside the net
      since `4001812` scoped the URL exclusion to scheme+host+path). That
      finding is the child's to resolve and is not this report. A session
      triaging the red from `gh run view <id> --log-failed` reported the
      cause instead as `conflictscan` findings on `docs/broken.md`,
      `docs/diff3.md` and a `docs/roadmap/10-track-a` path — none of which
      exist in the child's tree — and inferred that atelier's own fixtures
      were being scanned under the wrong root. The inference was wrong, and
      the log made it the natural reading.

      **Why the log reads that way** — measured on the child's run of
      2026-10-17, reusable workflow at `8acfff1`:
      1. The `scanner selftests` step **passed**, and its output carries
         finding-shaped lines. Six scanners' `--selftest` print
         `✗ <scanner>: N finding(s)` plus per-line findings against their
         temp fixtures: `board` six such lines, `datescan`, `pathscan`,
         `spellscan` and `wrapscan` two each, `conflictscan` one — that one
         naming `docs/broken.md` and `docs/diff3.md` with the full
         "commit blocked" wording and the remediation hint. `conflictscan`'s
         selftest gets there by calling its own `main()` on the fixture
         directory, which renders the human report before the selftest
         checks the exit code.
      2. The enforced `conflictscan` in the `scanner floor` step was
         **clean**. The step's only `##[error]` was `secretscan`.
      3. `gh run view --log-failed` returns the whole failed *job*, not the
         failed step: its output held 13 `selftest OK` lines from the passing
         step, and the lines carry no step name. So the reader meets fixture
         findings and real findings in one stream, same glyph, same wording,
         and only the `::error::` annotations tell them apart.

      **The class** is `370` — the report can lie while the work is fine. The
      work was right: the selftests proved the instruments, and the floor
      found one true thing. The channel put a proving-run's deliberate
      findings beside the floor's real ones with nothing to distinguish them.
      The fixture *paths* even look like a wrong-root scan — the exact failure
      the reusable workflow's own comment warns of ("atelier's own tree
      carries deliberate fake-secret fixtures that would false-positive") —
      so a reader primed by that comment lands on the wrong cause.

      **Not proposed, only listed** as the shapes a fix could take: a selftest
      that captures its `main()` output and prints only its verdict; a
      `selftest:` prefix on whatever a selftest does print; a `::group::` per
      scanner in the selftest step so its output folds; or one line at the
      end of that step saying the findings above are the selftest's, not the
      floor's. Which, if any, is atelier's call.

      **Not claimed:** that another reader would make the same misread; or
      that the child's own red is atelier's — it is a floating scanner
      tightening and finding a latent item in a child's tree, which ADR 0008
      says is the design, not drift.
