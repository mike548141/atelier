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

---

## Verdict — PASS-WITH-FINDINGS (1 MAJOR / 1 minor / 2 notes)

Reviewer: the taking session (Fable, spawn provenance in the brief; the
partial exposure via the `SESSIONS.md` index entry is disclosed there and in
the sibling publish-surface verdict). Every author claim exposed early was
re-derived from the artefact before being credited.

### Findings

- **PB1 — MAJOR (correctness; the tool's own named worst failure).** The
  pattern table is depth-blind for most of its entries, and the gap is
  mechanical, not missing fleet knowledge. `fnmatch` globs are not
  path-aware — `*` spans `/` — so `*/.env` covers a bare `.env` at any
  depth, but every other machine-local entry matches at the repo root only.
  Probes at HEAD: `packages/api/.npmrc` MISS (per-package `.npmrc` is a
  classic token carrier in monorepos), `sub/.env.production` MISS (the
  "canonical secret carrier" class, one directory down), nested
  `.mcp.json`, `.claude/settings.json`, `.envrc` all MISS. Meanwhile
  `.idea/**/*` is redundant (`.idea/*` already spans depths) — evidence the
  author believed the globs were path-aware, which is exactly the belief
  that produced the gaps. The module's denylist honesty ("a novel file
  passes until someone adds it") does not cover this: these are the *listed*
  files at unlisted depths, green-stamped as "none in the never-publish
  class". P2a (teach it the fleet's shapes after P7's sweep) is adjacent
  but distinct — no sweep is needed to fix a matching defect.
  *Counsel:* match the machine-local dotfile set (`.env*`, `.envrc`,
  `.netrc`, `.npmrc`, `.pypirc`, `.mcp.json`) by basename at any depth, and
  the directory-qualified pair (`.claude/settings*.json`,
  `.vscode/settings.json`, `.idea/`) by path suffix; add the probe rows
  above to the suite red-leg. Blocking-reach widens across children, so the
  decision is the principal's (rule 3); the advisory hatch already exists
  for any child the widening reds.
- **PB2 — minor (honesty of a stated mitigation).** The module docstring and
  commit message state the accepted guard-file exposure is "mitigated by
  requiring a stated reason for every exemption" — but `.publishscanignore`
  accepts a bare glob: comments are optional, no reason is required, and
  the remediation text itself demonstrates adding a glob with no reason.
  The no-line-marker design is sound and well argued; the *required reason*
  is claimed but unenforced — the same claim/enforcement seam as the queued
  leakscan `--require-terms` ci-plane gap (P4). *Counsel:* either enforce a
  trailing `# reason` per glob line (exit 2 on a bare one), or restate the
  mitigation as convention until it is.
- **PB3 — note (robustness).** `--root` pointed at a repo *subdirectory*
  silently narrows the scan: `git -C <subdir> ls-files` returns only that
  subtree, yet the output reports "N tracked path(s)" as if whole-repo, and
  root-anchored patterns can no longer match. The registry always passes
  the true root, so the floor is unaffected; a hand run is not. *Counsel:*
  resolve `git rev-parse --show-toplevel` and rebase, or name the subtree
  in the output.
- **PB4 — note (cleanup).** Drop `.idea/**/*` (redundant under PB1's fix or
  without it); one entry per intent keeps the provenance table honest.

### Lens results

1. **Approach & assumptions** — the path-not-contents question is real and
   correctly novel here; the layers-not-alternatives split against
   secretscan/leakscan is clean; the deliberate allowance of the
   self-describing guard files is well reasoned and bite-tested (they must
   travel for the floor to run). The no-`{scope}` registry decision is
   right and carries its ADR 0008 grounds in place. Assumption 1 (false
   negatives) failed → PB1. Assumption 2 partially failed → PB2.
2. **Correctness & quality** — exit-code discipline is right (0/1/2,
   fail-safe; no-git tree is a *complete scan of an empty set*, argued and
   tested, not a fail-open); JSON, warn, staged planes all behave as
   documented and are suite-covered; remediation output teaches the right
   two commands.
3. **Completeness / harvest** — the suite bite-proves red, green, both
   planes, hatch, warn, JSON shape, selftest, and the no-git leg; "14 new
   tests" verified by count; the commit's live-red claim re-driven on this
   tree (red staging the allowlist back, exit 1; green after unstaging,
   exit 0). What it does not cover is PB1's depth rows.
4. **Security & privacy** — the scanner itself adds no injection surface
   (no shell string interpolation; subprocess arg-vector git calls; stdlib
   only). Applied to itself: `.publishscanignore` would be a
   self-describing file — consistent with the accepted-exposure argument,
   and PB2 is the honesty gap in that acceptance. `/security-review`
   discharged in the brief (landed delta, no pending diff to aim at).

### Grounding re-run

Selftest OK; full python suite 820 OK at HEAD (includes the 14 here); node
suite 207 pass; live red/green re-driven on this tree as above; no-git leg
exercised by suite. Registry entry renders in the floor (visible in this
session's own pre-commit output as `publishscan enforced`).

Rule 3 applies: counsel is labelled; decisions are the principal's. PB1's
MAJOR keeps this delta's cycle open past its application.
