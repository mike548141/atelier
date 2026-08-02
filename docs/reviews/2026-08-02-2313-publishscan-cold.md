# Cold pass — `publishscan`, first-of-kind tooling (`8bdcfaa`)

- **Subject** — the new scanner `tools/publishscan.py`, its suite
  `tools/test_publishscan.py`, its registry entry in `tools/floor.py`, and its
  `tools/README.md` section. Landed `8bdcfaa`, 2026-07-29, by the 1418 session
  (Opus 5). Built, shipped, registry-wired blocking.
- **Type** — built work, first-of-kind: the first scanner in the floor that
  judges a file's *path* (should this exist in a published tree?) rather than
  its contents. First-of-kind is the full-ceremony trigger.
- **Scope** — the `8bdcfaa` diff and the four surfaces at HEAD; behaviour
  exercised live (its selftest, the suite, hand-driven red and green runs,
  probe cases the suite may have missed).
- **Spawn provenance** — rule 4: brief written by the taker, a Fable session
  Mike started 2026-08-02 and pointed at the review queue. The author session
  neither started nor instructed it. Cold from the refs-only pointer; the
  shared intent record stays unopened until all four queued verdicts are
  committed. One caveat, disclosed in the sibling publish-surface verdict:
  a sweep during that earlier pass surfaced the author's `SESSIONS.md` index
  entry — which includes an account of this scanner — before this brief was
  written. This reviewer therefore knows the author's claims (advisory form
  for children, per-pattern provenance, deliberate allowance of the
  self-describing guard files, a no-git hard-fail caught by `floor.py`'s
  suite). Handled by treating each exposed claim as an assertion to attack,
  not a fact.
- **Load-bearing assumptions to challenge**
  1. The worst failure mode is the false *negative* read as safety: a
     never-publish path present but unmatched (pattern gaps, path
     normalisation, case, nesting, symlinks, staged-vs-tree modes).
  2. The allowlist of self-describing guard files (and the template
     settings.json) is sound — and every exemption path requires a stated
     reason rather than opening a silent hole.
  3. The scanner is honest about what it does NOT check (contents; history;
     visibility of the repo it runs in).
  4. Registry wiring: blocking here, advisory form real and reachable for
     children; a tree with no git does not hard-fail (the claimed fix).
  5. The suite proves behaviour, not implementation — red cases genuinely
     red, exemption hatches tested, exit codes correct (`&&`-chain silent
     short-circuit is a known house hazard).
- **Grounding to re-run** — selftest; the full python suite; a hand-built
  fixture tree driven red then green; the pre-commit and staged planes; the
  no-git tree case.
- **Non-goals** — the publication-surface *doctrine* delta (`a9ab2cf`, its own
  pass); children's adoption; P3 (visibility-aware floor) and P5 (GitHub
  settings gate), which are queued work, not this delta.
- **Security scanner** — `/security-review` reads a pending diff; the work is
  landed. It cannot be aimed at this delta; discharged with that ground. The
  security lens runs manually: injection surfaces (path handling, subprocess
  use), and whether the scanner itself weakens the repo it guards
  (self-describing-file question, applied to the scanner's own config).
