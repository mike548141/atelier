- [x] 🔎 **Three enforced scanners still describe themselves as advisory**
      `[S][tools]`. Found 2026-10-05 by `300/020`'s re-rank pass. The
      docstrings of `datescan`, `wrapscan` and `spellscan`, their `--warn`
      help text, and their `tools/README.md` headings all say "advisory
      only", "never gates" or "it must not gate", and `datescan`'s docstring
      says it is "deliberately NOT in the blocking pre-commit hook". The floor
      registry wires all three blocking on the hook and on CI, and
      `floor.py --list` prints each one `enforced`. The registry is the
      authority, so the prose is stale: a reader who trusts the docstring will
      expect a warning and get a refused commit.
      **The work:** bring each scanner's own description in line with how the
      registry wires it, citing the change that promoted it, and leave the
      first-of-kind history as history rather than deleting it.

      ✅ **Fixed and merged 2026-10-05** (queue run, a Sonnet 5.5 worker;
      `4553814`). Docstrings, `--warn` help text and `tools/README.md` prose
      only, and no behaviour changed. Each of the three scanners now states
      its wiring with the commits that set it: CI blocking by Mike's ruling
      (`d24caec` for `datescan`, `4f1c10c` for `wrapscan` and `spellscan`,
      2026-07-23), and the hook plane via the registry (`40c7a22`,
      2026-07-25). The first-of-kind rollout is kept as past-tense history.
      `--warn` is described as the report-only mode the registry's advisory
      form uses, not as a reason the scanner must not gate. No other doc made
      the stale claim. Evidence: `datescan` output was byte-identical before
      and after; all three selftests pass; the CI plane exits 0; Node is
      406/406. The orchestrator changed the worker's "AS OF NOW" to a dated
      "verified 2026-10-05" so the wording does not drift. No rule-4 pass is
      owed: these are descriptions of landed wiring, not new doctrine or
      behaviour.
