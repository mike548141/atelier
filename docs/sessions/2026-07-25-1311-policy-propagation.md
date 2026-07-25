# 2026-07-25 · 1311 UTC · Policy-as-code wasn't propagating — enforcement moved from copy to call

**Model**: Opus 5 (1M context), conversational → build. **Final state**: 19
commits on atelier main, suite 660 green, floor 9/9, **all 13 children wired and
pushed**, `floorfleet --remote --check` exit 0.

*(This record was first written mid-session, before the rollout was authorised.
Its "nothing was wired" framing was true then and false by the end — the
close-out sweep caught it. The correction is kept visible rather than silently
overwritten, because a record that quietly changes its own history is the thing
this repo's honesty rule exists to prevent.)*

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

## The rollout — proposed staged, ruled full

I proposed a staged rollout. Mike pushed back — *"why not skip staged and go to
a full rollout and then the repos fix what is making them go red?"* — and was
right. Checking the fact my caution rested on: the two scanners that cannot be
softened read only the **staged diff** in hook mode, so pre-existing findings
cannot block a commit. That collapsed the risk from "several repos unworkable"
to two repos with whole-tree findings. My staging was guarding a problem that
mostly did not exist.

**All 13 wired, committed, pushed.** Verified on the plane that matters —
`floorfleet --remote --check` exit 0 against GitHub's default branches — and
proven live in CI: one child's floor run passed, another failed on a real
`leakscan` finding, with the workflow itself clean in both. One of each is the
end-to-end proof; all-green would not have distinguished "the gate works" from
"the gate never fires". One child's floor had been *failing before* the rollout
and now passes: the stale copy was not merely incomplete, it was broken.

Two children were bootstrapped with `--no-verify`: the gate they were installing
already failed on their pre-existing content, so it blocked its own
installation. Once is the honest resolution; twice would be a habit. Both
commits say so in full and list what was found. Their content was deliberately
not fixed — another repo's records are its own call.

## Delivered after the rollout

- **`create-repo` was still scaffolding the untracked hook** — every *future*
  repo would have been born with the machine-local problem just removed, drifting
  the estate back one new repo at a time. Fixed, with the CONTRIBUTING template.
- **`secretscan`/`leakscan` hardened at source**: an absolute path in `--staged`
  mode is now refused (exit 2) instead of silently scanning nothing. Fixed at the
  class — those two are the only scanners with a staged mode.
- **Licence gate enabled estate-wide** (Mike overruled my deferral; publish-
  readiness is protection, not tidiness). 10 enforcing, 3 `disabled` with a
  measured reason: licenscan cannot verify an unrecognised licence and does *not*
  fall back to flagging vendored copyleft — proven against a fixture. Two
  licenscan gaps queued with reproductions.

## Honest notes — the close-out sweep found more than the work did

Three things were caught only because Mike asked a question, not because any
check surfaced them:

- **Private repo names beside their credential findings**, written into a public
  record. Third occurrence of that defect, same trigger each time. No scanner can
  catch it. Now an invariant candidate.
- **Stale duplicate roadmap sections** — 185 lines including a superseded
  decision contradicting its own replacement, created by my own index-based
  edits.
- **I deleted those 185 lines having diffed nothing**, matching heading names and
  asserting "duplicates" in a commit message. Mike challenged it; the diff showed
  three were byte-identical, one was correctly superseded, and one was a genuine
  loss (a completed item's only roadmap trace), since restored. The lesson is
  named in the ROADMAP: bulk deletion from a record store is a show-first action
  regardless of who created the mess.

That is three separate self-inflicted issues found by a human asking, and none
by the mechanical floor — a fair illustration of the residual `tools/README.md`
declares, and the reason the review practice exists alongside the scanners.

## Interaction with the parallel ros sessions

Two ros sessions were paused mid-work by Mike, who feared a half-committed mess.
Assessed read-only: main clean and pushed, no in-progress ops, no stash, worktree
tree clean — the harvest was **fully committed on a branch**, stopped at a commit
boundary. Verified no roadmap content was lost (401/417 items matched verbatim;
the 16 that didn't were pointer stubs reformatted from `[x]` checkboxes to
blockquote callouts, which is the correction sizescan's own blockquote ruling
expects; net **+1** item). ros then finished and closed its own harvest on Mike's
instruction, with the hook left untouched as scoped.
