- [~] 🔎 **Three enforced scanners still describe themselves as advisory** (claimed 2026-10-05-1149, wt: atelier-qr-115-240)
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
