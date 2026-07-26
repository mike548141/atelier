# 2026-07-26 · 1120 UTC · the floor grows a repo-local extension point

**Model**: Opus 5 (1M context), build. **Final state**: three commits on atelier
main, 694 Python tests green (+21), floor 9/9 clean, worktree closed, review
queued ⏳.

## The ask

Mike, in full: *"Create a repo-local extension point"*. Four words, and no
match anywhere in the repo for that phrase — so the first work was reading, not
writing.

The reading landed it: `ROADMAP.md`'s open item *"Where does the registry
live?"*, whose own proposal (mining record, 2026-07-22 § How the registry would
be checked, item 2) reads *"shared floor, local append, child may
narrow-not-contradict. Ties REPO-STANDARD."* The 🎯 rulings that item waited on
were made on 2026-07-23 — all twelve candidates shared-floor — leaving exactly
one half unbuilt: the local one.

Mid-turn, Mike relayed the finding that had prompted the ask, from a `ros`
session, explicitly not his own words:

> atelier's new floor gives a child repo nowhere to declare a repo-specific
> check — `.atelier-floor.json` only marks known scanners advisory/disabled, and
> the tracked hook is deliberately scanner-agnostic. ros's tripwire, whose
> blocklist names the estate tokens themselves, can never live in a shared repo.
> Either atelier grows a repo-local extension point, or ros documents a
> deliberate divergence. Until then the hook plane is thinner than before
> `be59492`, with CI as the backstop.

That confirmed the reading and, more usefully, supplied the worked case. The
design stopped being an inference from a roadmap line and became an answer to a
repo that had actually lost a check.

## What was wrong

Every knob `.atelier-floor.json` had was **subtractive**: `advisory`,
`disabled`, `scope`, `flags` — each one a way to say *less* of atelier's floor
runs here. There was no addition, anywhere, and the tracked pre-commit shim is
scanner-agnostic on purpose (that is what makes a check added upstream reach
every child with no edit).

So a repo holding a rule that could never be fleet-wide had two options, both
bad:

- **keep a bespoke hook** — which takes the repo out of propagation entirely,
  and is the precise defect ADR 0008 was written to end; or
- **lose the check** — which is what ros did, honestly and on the record.

The estate's own doctrine already names the right shape: `PROPAGATION.md`'s
shared anchor plus local append. It had been applied to prose and never to
enforcement.

## What was built

`local` in `.atelier-floor.json` — checks the child declares, owns and ships:

```json
"local": {
  "tripwire": {
    "run": "tools/tripwire.py",
    "why": "estate tokens never enter a commit",
    "planes": ["hook"],
    "args": ["--staged", "--root", "{root}"],
    "scope": ["src"]
  }
}
```

Three properties keep it an extension point rather than a hole, and each is a
test:

| Property | How it is held |
|---|---|
| it only **ADDS** | a local name colliding with a registered scanner is a hard config error; `run` must resolve inside the repo; invoked directly, never through a shell |
| it fails **CLOSED** | a declared check whose script is missing BLOCKS, as a missing shared scanner does — declaring a check you do not ship is not a way to look guarded |
| it is **VISIBLE** | `--list` (with a fleet/local column), `--json` (a `local` field), the render (`· local`), and `floorfleet`'s board (`➕ name local — why`) |

Four decisions worth keeping:

- **One softening vocabulary.** A local check named in `advisory`/`disabled`
  reads identically to a fleet one, because a board reader should not need to
  know a check's provenance to know what happened to it. The honest difference
  is stated in the docstring rather than hidden: a fleet scanner's advisory
  swaps in *that scanner's* `--warn` form, so its output says warning; the floor
  cannot know a local check's flags, so advisory there downgrades the **result**,
  not the invocation — it stops blocking, but its output still looks alarming.
- **A hook-only local check still LISTS on CI**, as `skipped (not declared on
  the ci plane)`. ros's tripwire is exactly the machine-local-data shape that
  leakscan already has, so hook-only is legitimate — but silence on the CI plane
  is indistinguishable from a check that ran and passed, which is `floor.py`'s
  founding defect in miniature.
- **`scope`/`flags` are refused for local names.** Those blocks exist to bend a
  check the child did *not* write. A local check's scope and arguments belong
  beside its declaration — one fact, one home, and nobody reads two blocks to
  learn what actually ran.
- **The execute bit is checked before invoking a non-`.py` check.** Without it
  `subprocess` raises `PermissionError` and takes the whole floor down with a
  traceback, which reads as broken tooling rather than as the config error it is.

## What was NOT built, and is not implied

The mining record's proposal covers **two** layers, and only one is now built.
The **verifier/checklist** layer — V1–V7 and a child's own review catalogue —
still has no seam, and cannot get a sensible one until *"Codify V1–V7 as the
always-loaded reviewer checklist"* decides what a checklist entry even is. The
ROADMAP item now says the scanner half is answered and the checklist half is
open, in those words, so the built half cannot be read as covering the other.

`tools/README.md` is deliberately untouched. It documents the scanners; every
floor *concept* — advisory, disabled, scope, flags — lives in `floor.py`'s
docstring, and this one is there too. Adding a floor section for this feature
alone would have put half the concepts in each place.

## Honest limits

- **The seam runs the child's own code, and that is the trust model.** `run` is
  contained to the repo and never shell-interpreted, but a repo that can commit
  a script can already run it in its own CI. The seam does not widen that; it
  makes it declared.
- **`floorfleet` reports a local check as DECLARED, never as working.** It reads
  workflow and config text off a default branch and never fetches the script.
  Whether the script exists is `floor.py`'s question, answered where the repo is
  — and it fails closed there. A malformed `local` block renders rather than
  killing the board for the other twelve children.
- **Nothing about ros is fixed by this commit.** The seam exists; adopting it is
  ros's own work, in ros's own repo, and its ROADMAP item stays open there.

## Records

`review`: **WARRANTED and queued ⏳** — this edits `REPO-STANDARD.md` and adds a
surface every child may declare against, so it is self-authored doctrine by
function and REVIEW rule 4 binds. Queued in the ROADMAP, not spawned. One note
on the AWA2 window: the two build commits were made on a worktree branch and the
pointer was queued before the branch reached `main`, so no window exists where
landed doctrine sat unpointed — but the pointer was not in the same *commit* as
the work, and that is the letter of the rule.
