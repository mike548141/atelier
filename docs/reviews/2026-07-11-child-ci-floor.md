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

# Verdict — PASS-WITH-FINDINGS (Fable, cold session, 2026-07-11)

**Bottom line:** the floor.yml design holds (sibling checkout, repo-scoping,
honest leakscan scope, commented licenscan, floating main), the numen evidence
is exactly as recorded — but the brief's sharpest question ("does the linkscan
fix close the class or just this instance?") has a decisive answer: **just the
instance.** The same masked-layer false negative was alive in secretscan and
leakscan at review time, plus two more members of the silent-success family the
linkscan review had already fixed in linkscan alone. Six findings N1–N6, every
one **[fixed]** this session, each proven broken live before fixing and proven
closed after; suite 196→205.

## Floor, reproduced (re-run rule — nothing taken on record)

- `linkscan --selftest` OK; whole tree clean; a planted break in `docs/build/`
  flags `missing-file` exit 1 and the tree is clean again on removal.
- Full tool suite at review start: **196 OK**. All four scanner selftests OK;
  scan triad + licenscan `--expect Apache-2.0` clean over the tree.
- numen happy path re-read from the live logs (`gh run view 29092514962`):
  conclusion `success` at `0958cd5`, all three scans ✓ in-log. Fail-closed
  re-read (`29092599385`, PR event at `b2b6dcb`): conclusion `failure`,
  secretscan ✓, leakscan ✓, **linkscan ✗ → `Process completed with exit code
  1`**. The brief's claims match the logs exactly.
- Templates as-if-scaffolded (`linkscan --root docs/build/templates …`): clean;
  the decisions-README was the only template with a placeholder link
  (assumption 7 **confirmed**).

## Findings (all [fixed] this session, each re-driven)

**N1 — the masking fix closed the instance, not the class (the sharpest
finding).** `d0870a4` dropped `build`/`dist` from *linkscan's* hardcode-skip;
**secretscan and leakscan still carried both names**. Proven live at review
HEAD: a well-formed `AKIA…` key planted in `docs/build/` scanned **green** on a
whole-tree secretscan — the doctrine layer unmasked for links was still masked
for secrets and leaks, in the two scanners whose false negative is costliest.
Fixed by mirroring `d0870a4` in both scanners (hardcode-skip now only
never-authored names); pinned by `test_content_dir_named_build_is_walked` in
both test files; planted key + planted IP in `docs/build/` re-driven red;
atelier's whole tree re-scanned clean with the layer newly in scope for all
three scanners.

**N2 — the L1 silent-success class also lived on in both boundary scanners.**
`secretscan --root x x` and `leakscan --root x x` with a nonexistent path
printed **“✓ clean” and exited 0** (linkscan post-L1 exits 2; licenscan already
exits 2). In floor.yml terms: a typo'd `repo` path would phantom-succeed the
publish-safety scans. Fixed: nonexistent path args are now a usage error, exit
2, both scanners; pinned.

**N3 — the child's documented false-positive hatch was dead in exactly the
floor.yml invocation.** `iter_files` computed `rel` via
`p.relative_to(root)` with an unresolved `p` — whenever CWD ≠ root (floor.yml
runs `--root repo repo` from the workspace) that raises and the silent fallback
yields a **CWD-relative** path, so the scanned repo's own
`.secretscanignore`/`.leakscanignore` globs never matched. Proven live: a child
`.secretscanignore` failed to suppress a fixture under the exact floor.yml
command. The hook and ci.yml only worked because CWD happens to equal root
there. Fixed by resolving both sides (mirrors linkscan's `_rel`, already
reviewed); pinned by a CWD≠root test in both test files, sanity-checked in both
directions (flags without the hatch, clean with it).

**N4 — trigger gap confirmed (assumption 1), and the header overclaimed.** The
header said "every push + PR"; the trigger said `push: branches: [main]`. A
feature branch pushed and never PR'd was scanned by nothing — and a push to
*any* branch is already publication (the commit is on the remote regardless of
merge). floor.yml now triggers on every push; the double-run cost on same-repo
PR branches is stated in-file and accepted (seconds, per-ref concurrency).
Pinned (`test_push_trigger_covers_every_branch`). Note, deliberately not
changed: `ci-python.yml`/`ci-static.yml` keep `branches: [main]` — correctness
CI gates the merge; the floor gates publication. And atelier's **own** `ci.yml`
(out of scope, already reviewed) carries the same narrow trigger — same
reasoning applies; flagged as an observation for its next touch.

**N5 — floor.yml ran no scanner selftests (ci.yml does).** A fetched scanner
that can no longer detect its own fixtures would have passed green. A selftests
step now runs before the scans; pinned, ordered-before-scans asserted. Residual
stated honestly: a truly *empty/no-op* scanner file passes `--selftest` exit 0
silently (proven with an empty `.py`) — that class is bounded by atelier's own
CI, which runs the full 205-test suite on every push to the `main` the children
fetch.

**N6 — the false-positive hatches were undocumented where a child would look
(assumption 2 confirmed).** A real child carrying its own fake-secret fixture
red-flags its floor with no hatch named in floor.yml — and pre-N3 the
ignore-file hatch it might have found in the scanner output *didn't work* under
floor.yml. The header now documents both hatches (allow-marker, root-relative
ignore globs) and that they travel with the repo; pinned
(`test_false_positive_hatches_documented`). Proven live end-to-end: planted key
in a child `build/` dir flags; `.secretscanignore` glob suppresses it; clean
child passes 0/0/0 — all with the exact floor.yml commands, CWD at the
workspace.

## The judgement calls (assumptions 4, 5, 9)

**Floating `atelier@main` — holds, attacked.** The strongest case against: a
broken or subverted atelier `main` silently neuters (or worse, weaponises —
CI code can read the private child's checkout and has network egress) every
child's floor at once, and unpinned runtime-fetched code is textbook
supply-chain surface. It survives because: (a) the trust root is *identical* —
a child already inherits atelier's doctrine and templates, and adopters are
told in-file to point at their own fork; (b) what `main` serves is itself
gated — hook, 205-test CI floor, and this review culture; (c) `contents: read`
caps the token, and the `ref:` pin is already in-file for anyone whose threat
model differs. The clincher is this very review: **N1–N3 reach every child's
next run with zero per-child bumps** — under a pinned SHA, every child would
still be running the masked scanners until someone remembered to bump. For a
security floor, freshness *is* the safety property. Residual named: the
private-tree-exfiltration case rests on atelier main staying trustworthy;
that is accepted for a single-principal estate and re-opens if atelier ever
takes external committers.

**Remaining `SKIP_DIR_NAMES` — holds, with a note.** `.git`, dep dirs, tool
caches: never human-authored. `.idea`/`.vscode` do ship *checked-in config*,
but markdown prose there is vanishingly rare and the miss cost is a few config
files, not a doctrine layer. Kept, residual stated here.

**Assumption 9 — the fail-closed proof generalises; the real-infra secret
drive is NOT owed.** Decided closed by composition: (a) the exact floor.yml
secretscan command blocks a planted well-formed key locally (re-driven this
session, exit 1); (b) run `29092599385` proves on real infra that a scanner's
exit 1 fails the job — and that mechanism is scanner-agnostic (identical step
shape, same runner). The only untested link would be GitHub treating one
`run:` step differently from its neighbour, for which there is no mechanism.
Deliberately not driven: planting even a fake-shaped secret in remote history
is precisely the noise this whole apparatus exists to prevent.

## Records honesty (lens 4)

Session 28's entry and this brief match the live evidence everywhere checked.
One over-readable line, now moot: `d0870a4`'s "whole floor re-proven green with
docs/build now in scope" was true **of linkscan only** — for secretscan and
leakscan the layer stayed masked until N1. Post-N1 the sentence is true of the
triad. The child-CI story (sessions 23/26/27 leaving it open, session 28
closing it on numen) is accurately told.

## Follow-ups (not blockers)

1. **numen should re-copy `floor.yml`** — the scanner fixes (N1–N3) reach it
   automatically via floating main, but the *workflow-file* fixes (N4 trigger,
   N5 selftests, N6 hatch docs) are baked into its copied YAML. One-file copy,
   next numen touch. Its frozen pre-scaffold hook (session 28's incidental)
   stands as already flagged.
2. **atelier's own `ci.yml` trigger** — same N4 reasoning (a never-PR'd branch
   push is unscanned by CI); out of this review's scope, take it on the next
   ci.yml touch.

**Gate cleared:** `floor.yml` may roll to further children (in its post-review
form), and the linkscan masking fix may be leaned on — it now actually covers
the class, in all three scanners.
