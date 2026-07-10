# Fable review — the child-CI scanner floor + the linkscan masking fix

**Status:** brief (ask on top). Verdict appended below the divider after the
review runs. **Run this cold** — a fresh session, not the window that built it
(`REVIEW.md`: independence is about context, not just model tier; the builder's
reasoning must not ride along).

**Range under review** — two atelier commits plus one cross-repo artifact:

- `bafeaa3` — `docs/build/templates/workflows/floor.yml` (the child-CI scanner
  floor) + its `test_templates.py` pins + create-repo/REPO-STANDARD wiring
  (built atelier session 27, never yet run on a live child at brief time — now it
  has been; see below).
- `d0870a4` — `tools/linkscan.py` drops `build`/`dist` from `SKIP_DIR_NAMES`;
  `tools/test_linkscan.py` gains the regression pin; the decisions-README
  **template** placeholder link is code-spanned.
- **Cross-repo evidence (not in atelier):** `mike548141/numen` commit `0958cd5`
  adopted `floor.yml` and was the first real-child exercise. The reviewer can
  read numen's `floor.yml`, its `.github/workflows/README.md`, and the two GitHub
  Actions runs cited below — but numen is **private and out of review scope**;
  treat it as the live test rig, not code to audit.

**Why it earns a review before it's trusted as a gate.** `floor.yml` is net-new
CI tooling in the scan-triad class: a check whose clean exit automation reads as
"safe", now the *only* CI backstop for every doctrine-inheriting child. Its worst
failure is the **false negative** — green while a secret/leak/broken-link sits in
the child's tree — because it manufactures confidence in exactly the
publish-safety boundary the whole model leans on. The `linkscan` fix is in the
same class and was *provoked by this very exercise*: driving `floor.yml` against
numen exposed that linkscan had been **silently skipping atelier's own
`docs/build/` layer for four sessions** (24–27) because `build` sat in its
hardcode-skip set — a live false negative, the cardinal sin the linkscan review
(session 25) was built to prevent, which slipped through anyway. That is the
sharpest thing on the table: *the instrument reported clean while blind to a
whole layer* (§14 silent-success). Attack whether the fix closes the class or
just this instance.

Per REVIEW's re-run rule: every "proven live" claim below was re-driven this
session, not read from a prior record — including the two that a prior session
got wrong (session 24's "whole tree clean (55 files, 36 links)" was false; the
build layer was never walked).

## What the work is (context for the reviewer)

Read first: `method/PROPAGATION.md` (why the pointer graph is load-bearing),
atelier's own `.github/workflows/ci.yml` (the honest-scope pattern floor.yml
mirrors — leakscan structural-only), `tools/README.md` (the "what these scans
cannot see" residual list), and the `floor.yml` header (its design calls are
documented in-file, not buried).

- **`floor.yml`.** A language-agnostic scanner floor a child drops in *beside*
  its `ci.yml`. On `push:[main]` + `pull_request` it checks `mike548141/atelier`
  out as a **sibling** (`path: atelier`) and runs atelier's public
  secret/leak/link scanners against the child's own tree (`path: repo`). No
  vendored scanner copy, no secret. Design calls, all in the header: **floats
  `atelier@main`** (a security floor wants newest; also keeps CLAUDE.md's pin the
  sole doctrine-version SHA — a second stamped SHA here would be a new drift
  surface; `ref:` commented for reproducible-CI wanters); **leakscan
  structural-only** (its term list is machine-local by design — CI cannot hold
  it, mirrors ci.yml); **linkscan whole-tree**; **licenscan commented** (it
  hard-fails with no LICENSE → a *publish* gate, wrong to default-on for a
  private child). Scan scoped to `repo/`, not the whole workspace — atelier's own
  tree carries deliberate fake-secret fixtures that would false-positive
  (load-bearing, not cosmetic). `contents: read`, concurrency-cancel.
- **The linkscan fix.** `SKIP_DIR_NAMES` now holds only names that are *never*
  human-authored prose (VCS, deps, tool caches). `build`/`dist` are gone: a
  content dir can legitimately share the name (atelier's `docs/build/`), the tool
  cannot tell "build output" from "content named build" by name, and guessing
  wrong masks a doctrine layer — the worse error. A repo with a real build-output
  dir names it in `.linkscanignore`. The scaffolded decisions-README template
  shipped `[0001](0001-slug.md)` inside an HTML comment — invisible under
  atelier's skipped `docs/build/templates/` path, but a real linkscan break the
  moment a child scaffolds it to `docs/decisions/`. Now a single-line code span.
- **Proven live this session (re-driven, not read):**
  - atelier: `linkscan --selftest` OK; whole tree **now walks `docs/build/`**
    (proven by planting a break there → exit 1) and is clean; full suite
    **195→196** OK; the scan triad + three selftests all green over the tree.
  - numen happy path — GitHub Actions run **29092514962**, green in 8s: atelier
    fetched as sibling, `repo/` scanned, `✓ secretscan` / `✓ leakscan (structural
    only)` / `✓ linkscan`. The real-infra proof `floor.yml` never had.
  - numen fail-closed — a throwaway PR (`#1`, since closed, branch deleted)
    planted one broken link; run **29092599385** went **red**: secretscan ✓,
    leakscan ✓, **linkscan ✗** (exit 1 → job failure). The scan numen's *frozen
    local hook does not even run* is the one CI caught — the backstop thesis,
    end-to-end.
  - templates scanned as-if-scaffolded (root at `docs/build/templates`): clean —
    the decisions-README was the *only* template shipping a placeholder link.

Out of scope (note, don't spend budget): the scanners' own internals (each
already reviewed / briefed); atelier's own `ci.yml` (reviewed); whether to build
a full CommonMark linkscan (judge the residual's honesty, not scope expansion).

## Scope — four lenses, run all four

1. **`floor.yml` false-negative surface** (most important). What can a child
   push that this CI reports green while it is genuinely unsafe? Named suspects to
   attack, not an exhaustive list:
   - **Trigger gaps.** It runs on `push:[main]` + `pull_request`. A push to a
     feature branch that is never PR'd is *never scanned by CI*. Combined with a
     stale/absent local hook (below), is there a path where a secret reaches a
     child's history with zero automated catch? Is that acceptable or a hole to
     name?
   - **The `repo/` scoping.** It exists because atelier's own fixtures would
     false-positive. But a *real child* can also carry a legitimate fake-secret
     fixture (a security repo, a scanner of its own). Then the child's own floor
     false-positives on its own tree with no hatch documented in `floor.yml`.
     Is that a real risk, and where would the child learn the fix?
   - **Silent scanner-absence.** If a future atelier refactor renames/moves
     `tools/secretscan.py`, the `run:` step errors (red) — good. But if it moved
     to a path that *exists but is empty/no-op*, would the step pass green? Judge
     whether floor.yml can phantom-succeed the way the pre-commit sample once did
     (session 19's fail-open defect — the §14 class).
2. **`atelier@main` as a supply-chain trust.** Every child's CI executes
   whatever atelier's `main` HEAD scanners are, fetched at run time. A broken or
   subverted atelier main silently breaks — or worse, *neuters* — every child's
   floor at once. Is floating-main the right call for a security gate, or does the
   "newest is safest" argument lose to "reproducible and pinned is safest"? The
   header commits to floating; attack that commitment, don't just accept the
   rationale. (If you flip it, note the cost: a second SHA to keep in sync with
   CLAUDE.md's pin.)
3. **The linkscan masking fix — class vs instance.** `build`/`dist` are gone.
   (a) Is the *remaining* `SKIP_DIR_NAMES` truly all "never human-authored"?
   Could a repo legitimately keep prose under `.vscode/` or `.idea/` (some do
   ship docs there)? (b) Does dropping `build`/`dist` create a *new*
   false-positive class for real children with generated-markdown build dirs, and
   is `.linkscanignore` a real hatch or a hatch nobody will find? Where is it
   documented for a child? (c) The four-session-long false negative: is there
   evidence of *other* content that was masked and is only now visible — i.e., is
   the "196 tests / tree clean" claim honest *after* unmasking, or does the newly
   visible layer hide a real break the code-span fix merely papered over?
4. **Correctness & honesty of the records.** The child-CI story spans sessions
   23/26/27 all leaving it "open"; numen's docs claimed "the only automated gate
   is the hook" (now corrected). Are the atelier + numen session entries and this
   brief honest about what was *proven on real infra* vs asserted? In particular:
   the fail-closed proof used a broken link, not a planted secret — is that a
   sufficient stand-in for "floor.yml blocks a secret in CI", or is the secret
   path still only proven locally (session 27's `act` run) and owed a real-infra
   drive?

## The load-bearing assumptions to attack (grounded, falsifiable)

Each is a claim the work rests on. Damage it with a probe, or confirm it by
re-driving — don't reason about it.

1. **A push to a non-main, never-PR'd branch is scanned by nothing** (CI triggers
   miss it; a stale hook may too). Falsify by finding a trigger that covers it, or
   confirm and judge whether it's an acceptable gap for a publish-safety floor.
2. **A real child carrying its own fake-secret fixture would make its floor
   false-positive**, with no hatch named in `floor.yml`. Construct the case.
3. **`floor.yml` cannot phantom-succeed on a moved/empty scanner** the way the
   pre-commit sample did (session 19). Try to make a scan step exit 0 while
   proving nothing.
4. **Floating `atelier@main` is the right trust model for a security gate.**
   Argue the strongest case *against* (a bad atelier main neuters all children at
   once) and decide if the header's rationale survives it.
5. **`SKIP_DIR_NAMES` after the fix contains only never-authored names.** Find a
   real repo convention that ships prose under one of the remaining entries.
6. **Dropping `build`/`dist` does not create an unhatched false-positive class**
   for children with generated-markdown build output. Build the counter-case and
   check the hatch is discoverable.
7. **The decisions-README was the only template shipping a placeholder link.**
   Re-scan all templates as-if-scaffolded and confirm (or find another).
8. **The post-unmasking "tree clean / 196 OK" is honest** — the newly visible
   `docs/build/` layer hides no real break the code-span fix merely hid. Re-drive.
9. **The fail-closed proof (broken link, red run 29092599385) generalises to a
   secret** — or it doesn't, and the real-infra secret-block is still owed
   (only `act`-proven, session 27). Decide which, and if owed, say so.

## How to run it

Cold session. Reproduce the floor first (atelier `linkscan --selftest`; whole
tree incl. a planted `docs/build/` break; full suite). Then re-drive the two
numen runs' *claims* against the live logs (`gh run view --log`), not the
summaries here. Land findings as `N1..` with a fix each where you can, applied +
re-driven same session per house practice. Append the verdict below the divider.

---
