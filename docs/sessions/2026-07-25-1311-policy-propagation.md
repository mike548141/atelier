# 2026-07-25 · 1311 UTC · Policy-as-code wasn't propagating — enforcement moved from copy to call

**Model**: Opus 5 (1M context), conversational → build. **Worktree**:
`worktree-policy-propagation`. **Branch state at write**: 5 commits, suite 656
green, no child repo touched.

## The ask

Mike, opening: *"some of the policy we have written into atelier, things we
specifically made 'policy as code' because otherwise doctrine may not be
enforced, is not propagating to child repos."* Then, sharper, mid-session:
*"I want the things we write as policy written into the child repos and I want
to know 100% that its been done for the current and future repos. How do we do
that"* — and on the measurement: *"unacceptable to remain that way"*.

## What was actually wrong

The scanners were already one-source: a child vendors no scanner code, CI fetches
`atelier@main` at run time. But the **list of which scanners run** was copied into
each child at scaffold time — 247 lines of `floor.yml` per repo, plus four
hard-coded `run_scan` lines per clone. **Code was shared; policy was vendored.**

Measured: 13/13 children drifted from the template; **12/13 ran none of the five
checks added since they were scaffolded** (`sizescan`, `datescan`, `wrapscan`,
`spellscan`, `reviewscan`). `kainga` alone was current, only because it was
scaffolded after the update. Every hook in every clone was additionally
machine-local, `.git/hooks/` being untracked.

Two corrections to the incoming framing, both material:

- **ros was not "a repo with no CI".** It has CI and a `floor.yml`; the file was
  simply a stale copy. That changes the fix from "wire one repo" to "stop
  vendoring", which is a 13-repo fix.
- **`floor.yml`'s template *did* run sizescan.** The child copies didn't. The gap
  was distribution, not the template.

The doctrinal hole: `PROPAGATION.md` prescribes thin anchor / fat pointer for
doctrine *prose* and closes by warning "do not mistake the anchor for the
enforcement" — and the enforcement layer was the half that got vendored.

## Delivered

| Commit | What |
|---|---|
| `40c7a22` | `tools/floor.py` — one registry, two planes; reusable workflow; child template 247 → ~30 lines naming no scanner; hook becomes a shim |
| `e64c79a` | per-scanner `scope` + `flags` (the networking-repo case); **fixed a fail-open of my own** |
| `d0aea38` | tracked `.githooks/` + `core.hooksPath`; atelier's own CI onto the floor it ships |
| `78e1d20` | ADR 0008 + `PROPAGATION.md` — enforcement propagates by call; conformance is enumerated |
| `91e78f4` | `tools/floorfleet.py` contract tests |

Design commitments worth carrying forward:

- **Nothing is silently absent.** The old opt-out was deleting a line — invisible
  the moment it was done. A repo that doesn't enforce a check declares it
  `advisory` or `disabled` (with a reason) in `.atelier-floor.json`, and
  `floorfleet` reads those out estate-wide.
- **Softening is not the child's call.** Boundary and integrity scanners have no
  advisory form; `flags` refuses the mode-changing arguments outright.
- **The parent is not special.** atelier runs the floor it ships, scoped by its
  own config. A parent with a private list is the same bug one level up.

## Honest notes

- **I shipped a fail-open into the working tree and the tests caught it.** The
  first `_render` passed **absolute** paths to the staged scanners. `secretscan`
  and `leakscan` filter the staged diff by prefix against git's repo-relative
  path list, so an absolute path matches nothing — and a scan matching nothing
  exits 0. Every boundary check silently passed. Only the planted-secret commit
  tests failed. Fixed, and both shapes now pinned. Recorded because it is the
  same shape as the defect being fixed: a check that runs, reports success, and
  covers nothing.
- **I briefly mis-flagged ros's hook** as carrying that same defect. It doesn't —
  `--staged … tiki/` is a correct *relative* prefix and does block. Corrected in
  the same turn, before any change was made to ros.
- **A `private-key-header` finding in one child**: BEGIN and END markers on one
  line, zero base64 body — prose describing key-file format, not key material.
  Mike's read (nothing burned) was right; the literal token was a private-key
  header rather than the public key he named. No rotation; wants an allow-marker.
  Kept repo-generic deliberately — see the boundary-findings note in ROADMAP.
- `floorfleet` proves a repo **calls** the floor, never that the floor is green
  there. Conformance and compliance are separate claims and the tool says so.

## Not done — deliberately, and why

**No child repo was touched.** Measuring first showed that wiring blind would
have been wrong: one child returns >30k `secretscan` hits from committed
device-config captures (Mike agreed: scoping, not secrets), and the boundary
scanners have no advisory form, so several repos would have gone red-and-blocked
rather than red-and-visible. The rollout needs per-repo scoping decisions that
did not exist when this session started. Staged plan proposed and awaiting
ratification (see ROADMAP).

## Interaction with the parallel ros sessions

Two ros sessions were paused mid-work by Mike, who feared a half-committed mess.
Assessed read-only: main clean and pushed, no in-progress ops, no stash, worktree
tree clean — the harvest was **fully committed on a branch**, stopped at a commit
boundary. Verified no roadmap content was lost (401/417 items matched verbatim;
the 16 that didn't were pointer stubs reformatted from `[x]` checkboxes to
blockquote callouts, which is the correction sizescan's own blockquote ruling
expects; net **+1** item). ros then finished and closed its own harvest on Mike's
instruction, with the hook left untouched as scoped.
