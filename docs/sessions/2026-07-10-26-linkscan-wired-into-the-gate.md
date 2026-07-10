# 2026-07-10 · linkscan wired into the gate — CI + pre-commit, whole-tree (Opus)

The build session after the linkscan review (session 25) cleared its gate. The
reviewer deliberately didn't wire its own same-day fixes into the gate
(don't-stack, fourth application); this session — fresh context, not the
reviewer — does the wiring. ROADMAP called it "a two-line change." It wasn't,
and the gap between "a linkscan line in the hook" and what linkscan actually *is*
was the whole substance of the session.

## The one real design call

The two existing scanners in the hook (secretscan, leakscan) are **boundary**
checks: they read the **staged diff** and block *new* violations you are
introducing. linkscan is an **integrity** check, and a broken internal link is a
property of the whole doc graph, not of any one staged line — a link goes stale
when a *different* file is renamed or deleted, so the file that breaks is usually
**not** the one in your diff. linkscan therefore has no `--staged` mode and
shouldn't: staged-scoping would give false confidence, missing the exact
rename-breaks-others case the tool exists to catch. So in both gates it runs
**whole-tree**.

That raised the honest question the ROADMAP line glossed: linkscan catches a
*recoverable* defect (fix the link in a follow-up), unlike the boundary scanners
which block *irreversible* harm (a burned secret, published personal data). A
principled split would be "hook = irreversible only, CI = integrity." What tipped
it to **both** gates: atelier's real workflow is push-to-main, where CI runs
*after* the push — i.e. after publication. For a public repo whose entire
architecture is "thin anchor, fat pointer," the pre-commit hook is the only gate
that catches a 404 *before* a reader hits it. Wiring it into the hook honours
what linkscan was built for. Recorded, not buried: the recoverability nuance and
the child-repo friction are both stated (below), so Mike can pull it back to
CI-only if he prefers that line.

## What changed

- **`ci.yml`** — a `linkscan --selftest` line in the selftests step and a
  whole-tree `linkscan --root . .` step, mirroring the triad. Header updated:
  the checks are now "the leak/secret/licence publish triad, plus linkscan's
  internal-link integrity check."
- **`pre-commit.sample`** — linkscan added as a whole-tree integrity check.
  `run_scan` generalised: the hardcoded `--staged` moved out of the helper to
  the call sites, so each scanner declares its own mode (`secretscan --staged`,
  `leakscan --staged`, `linkscan --root <root> <root>`). The fail-closed
  missing-scanner guard stays in the directly-called helper (its `exit 1` must
  abort the commit, which it can't from inside a `$(...)` subshell — the reason
  the guard wasn't factored behind command substitution). Header documents the
  distinct whole-tree contract; the block-message now names `linkscan:allow` /
  `.linkscanignore`.
- **`test_precommit.py`** — three new tests + one hardened. The crux is
  `test_rename_breaking_unstaged_link_blocks`: a two-commit setup where the
  second commit only `git rm`s the target, leaving the linking file out of the
  diff — a staged-only scan waves it through, linkscan-over-the-tree blocks it.
  Plus broken-link-blocks and valid-link-passes. `test_in_repo_fallback_blocks`
  now also copies `linkscan.py` so it blocks on the *secret* it's testing, not a
  fail-closed on a scanner the hook now runs. Suite **187→190**.
- **`tools/README.md`** — hook "Wiring it in" now lists three scanners (one
  whole-tree, with the why); linkscan's own section gained a **Wiring**
  paragraph (it's the one integrity tool that lives on both hook and CI).
- Installed atelier hook refreshed from the sample, so **this very commit
  dogfoods the new gate** (tree is linkscan-clean, proven).

## Grounded, not assumed

Ran the full CI-equivalent set locally before committing: 190 tests OK; four
`--selftest`s OK; secretscan/leakscan/licenscan(`--expect Apache-2.0`)/linkscan
all clean over the whole tree (linkscan exit 0). The hook tests drive real `git
commit`, so the whole-tree contract is proven on the actual commit path, not just
asserted. GitHub CI still to be watched green on the pushed SHA (REVIEW re-run
rule) — done post-push this session.

## Residual, stated

A **scaffolded child repo inherits the stricter whole-tree contract**: its entire
doc tree must stay link-clean to commit, where the boundary scanners only judge
the diff. Cheap for a repo that keeps its tree clean; for a messy one it's real
friction. The hatches are `linkscan:allow` (per line), `.linkscanignore` (per
path), and `--no-verify` (emergency). Named here rather than discovered by an
adopter.

## Left open (don't-stack, and the honest edges)

- **Wire the public scanners into child CI** — still the open half of the CI
  story (a child checks out `mike548141/atelier` and runs its public `tools/`).
  `ci.yml` is the reference to adapt. Untouched this session.
- linkscan's own structural residuals (reference-style links, raw-HTML links,
  two-line `](…)`, indented-code false-positives, slugger divergence) stand as
  documented in `tools/README.md` — unchanged; this session wired the tool, it
  didn't widen it.
