# Cold review (rule 4) — ADR 0008: enforcement is called, not copied

**Subject (refs only):** ADR
[`0008-enforcement-is-called-not-copied.md`](../decisions/0008-enforcement-is-called-not-copied.md)
and the surfaces it governs at HEAD: `tools/floor.py`, `tools/floorfleet.py`,
`tools/pre-commit.sample`, `.githooks/`, `.github/workflows/floor.yml`,
`docs/build/templates/workflows/floor.yml`, the two 2026-07-25 sections of
`docs/method/PROPAGATION.md` (enforcement propagates by call; enumeration not
assumption), `.atelier-floor.json`, and their test files. Establish the
enacting commit set yourself with `git log --oneline --since=2026-07-25
--until=2026-07-26 -- <those paths>` (the first is `40c7a22`); the same-day
follow-on hardening commits on `tools/secretscan.py` / `tools/leakscan.py`
(absolute-path refusal in `--staged`) and the create-repo CONTRIBUTING
template are in scope.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer and
SESSIONS index one-liners before writing this stub, and a git-log grep
incidentally surfaced the *subject lines* of a withdrawn earlier pass on this
item (quarantined under `docs/reviews/withdrawn/`, wrong tier, not accepted —
its findings are dead and are not reading for this redo). Nothing evaluative
from any of those sources appears above the divider; the seeded question from
the queue pointer sits below it, deferred.

**The reviewer's first acts:** establish what the work is from the ADR, the
delta, and HEAD yourself; name the load-bearing assumptions and attack surface
as your own before anything else; run all four lenses at the widest scope the
work admits (`docs/method/REVIEW.md` — the lenses organise scope, never bound
it; the ADR's decision and its stated alternatives are as reviewable as the
code). Re-run every "live-proven" claim the delta's commit messages, the ADR,
and the CHANGELOG entries make; a proof that no longer reproduces is a finding.

**Re-run obligations:** `python3 tools/floor.py --plane ci` (whole-tree floor
at HEAD) · `python3 tools/floor.py --selftest` · `python3 -m unittest discover
-s tools` · `node --test instruments/*.test.js` ·
`python3 tools/floorfleet.py --check` (and `--remote --check` if `gh` is
available — read-only) · the planted-secret / fail-open regression tests in
`tools/test_precommit.py` and `tools/test_floor.py`. Lens 4 runs at both
altitudes: this is a security floor — supply-chain posture of the call-not-copy
mechanism is in scope, checked against open catalogues, not recalled.
`/security-review` reaches only pending diffs; on a landed delta discharge it
in one explicit line with grounds.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/` (quarantined). Do not grep git
history for review commits; confine git archaeology to the delta surfaces
named above. Open the deferred section below the divider — and the intent
record it names — only after your findings are durably written to this file;
then append the reconcile, named as such.

Findings carry stable IDs (**EP1…**), each with claim / evidence / counsel;
close with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL** and severity counts
(MAJOR/minor/LOW/nit). This is self-authored doctrine by function (an ADR plus
policy-as-code that governs every repo): REVIEW.md rules 3–4 govern — every
finding is counsel, the decisions are the principal's, and nothing is applied
in this pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* [`sessions/2026-07-25-1311-policy-propagation.md`](../sessions/2026-07-25-1311-policy-propagation.md)

*The queue pointer's seeded question (a floor, never a fence):* aim at the one
real trade — moving every repo onto a floating `@main` caller swaps a slow
silent failure (vendored copies drifting stale) for a fast loud estate-wide
one (a bad push to atelier breaking every child's floor at once). Is that the
right trade for a *security* floor?

## Reviewer's attack surface (named before re-runs — cold pass, 2026-07-26)

Established independently from the ADR, the enacting commits (`40c7a22`,
`e64c79a`, `d0aea38`, `78e1d20`, `6998c2a`, plus follow-ons `f526dea`,
`c3ef60d`, `76f4acc` on the same surfaces) and HEAD `9aef298`. The work: one
scanner registry (`tools/floor.py`, two planes), a reusable CI workflow called
`@main` by thin child callers, a tracked hook shim, declared opt-outs in
`.atelier-floor.json` (advisory/disabled/scope/flags/local), and estate
enumeration (`tools/floorfleet.py`). Load-bearing assumptions I will attack:

1. **Fail-closed is real, not asserted.** Every claimed blocking path — missing
   scanner, missing local script, unparseable config, unknown name, forbidden
   flag — must actually block when driven, including through the shell shim
   (`.githooks/pre-commit`), which has its own failure modes (`python3` absent,
   non-executable hook, `set -e` semantics) outside floor.py's tests.
2. **The staged-plane path-shape defect is actually dead.** The absolute-path
   silent pass was the delta's own near-miss; I re-drive the planted-secret
   tests and check for surviving relatives of the same shape (`{scope}`
   rendering, `scope` overrides that don't exist in the tree, prefix matching).
3. **The softening boundary holds.** `flags` refuses mode-changers by a
   blocklist (`FORBIDDEN_FLAGS`) — blocklists underblock. Can a child change
   what a check *means* through a flag not on the list (`--disable` on
   leakscan already weakens; ignore-globs; `docs` retarget; `scope` narrowing
   to a near-empty real subtree)?
4. **The classifier is text-matching.** `floorfleet.classify` regexes workflow
   text; a repo can *look* wired while running nothing (job-level `if:`,
   disabled workflow, caller in a non-workflow dir?) — the docstring concedes
   some of this; I test where the concession undersells.
5. **Supply chain of call-not-copy.** Floating `@main` moves trust: anyone with
   write to atelier's main owns every child's CI (and the hook executes
   whatever `hooks.atelierTools`/`ATELIER_TOOLS` points at, env winning over
   config). Checked against current published guidance on reusable-workflow
   pinning, not recalled; the ADR's own G7 contrast (trust roots never float)
   is the internal standard the decision must survive.
6. **The ADR's evidence claims reproduce.** 13 children / 12 stale, 15
   findings in 4 repos, suite counts, "atelier runs the floor it ships" — what
   is still checkable at HEAD gets re-checked, not trusted.
7. **The seeded reviewer question** (ADR lines 5–8): floating `@main` trades
   slow silent failure for fast loud estate-wide failure — is the blast-radius
   mitigation (contract tests on the registry) proportionate, and is the trade
   stated honestly in the consequences?

Lenses: (1) correctness of the mechanism and its tests; (2) doctrine coherence
(PROPAGATION.md additions vs REVIEW/APEX and the ADR's rejected alternatives);
(3) operator experience (adopting-repo red, error remedies, template honesty);
(4) security at both altitudes (the floor as a control, and the floor as an
attack surface).

---

## Verdict — cold rule-4 pass, 2026-07-26 (Fable)

**PASS-WITH-FINDINGS** — 3 MAJOR · 4 minor · 1 LOW · 1 nit.
*(Pre-reconciliation counts. One finding was added in the Reconciliation section
below after the deferred material was opened: revised total 3 MAJOR · 5 minor ·
1 LOW · 1 nit, same verdict.)*

The mechanism is real and it works: the registry is one source, the estate is
enumerated, fail-closed is driven by real commits rather than asserted, and the
near-miss the delta caught itself is now pinned in three places. Every MAJOR
below is the same shape as the defect ADR 0008 exists to end — a declared cover
that is smaller than it reads, with no instrument that says so — reached
through the *subtraction* routes the design added at `e64c79a` rather than the
ones it closed.

### What was re-run, with results

| Obligation | Result |
|---|---|
| `python3 tools/floor.py --plane ci --root .` (whole tree, HEAD `9aef298`) | ✅ rc 0, nine scanners enforced; sizescan prints a non-blocking size advisory on `docs/ROADMAP.md` |
| `python3 tools/floor.py --selftest` | ✅ rc 0 — `ok (9 scanners, 0 failure(s))` |
| `python3 -m unittest discover -s tools` | ✅ `Ran 694 tests … OK` — matches `f526dea`'s claim of 694 exactly |
| `node --test instruments/*.test.js` | ✅ 207 pass, 0 fail |
| `python3 tools/floorfleet.py --selftest` | ✅ rc 0 |
| `python3 tools/floorfleet.py --check` (local, `--atelier` at the main checkout) | ✅ rc 0 — 13/13 children wired, shim current, hook tracked |
| `python3 tools/floorfleet.py --remote --check` (`gh`, read-only) | ✅ rc 0 — 13/13 wired on their GitHub default branches |
| `tools/test_precommit.py` planted-secret + fail-open set (verbose) | ✅ all ok, including the `core.hooksPath` real-commit route, the executable-bit check and the sample/tracked-copy diff |
| `tools/test_floor.py` (49 tests) | ✅ OK, including `test_staged_scope_is_repo_relative_never_absolute` and the four flag-smuggling guards |
| `tools/test_secretscan.py`, `tools/test_leakscan.py`, `tools/test_floorfleet.py`, `tools/test_templates.py` | ✅ OK via `unittest discover` |
| Absolute-path refusal (`6998c2a`), driven directly | ✅ absolute in `--staged` → rc 2 with the working form named; no-positional whole-diff cover still blocks a planted credential fixture → rc 1; relative non-matching prefix → rc 0, silently clean (see EP1) |
| Tracked hook vs canonical sample | ✅ byte-identical, mode `0755` |
| ADR evidence still checkable at HEAD | ✅ 13 children; ✅ atelier runs the floor it ships (`.github/workflows/ci.yml:137`, own scoping in `.atelier-floor.json`); ⚠️ the "12 of 13 stale" and "15 findings, 4 repos" measurements are pre-wiring history and are not re-runnable now — accepted as recorded, not re-proven |

Two invocation notes for the next reviewer: `python3 -m unittest tools.test_secretscan`
fails on import (the suites `import secretscan` directly and rely on discovery's
`sys.path`); use `discover -s tools -p <file>`. And `floorfleet` run from inside
a `.claude/worktrees/` checkout discovers nothing (rc 2) — its search root is
the checkout's parent; pass `--atelier` at the main clone.

**`/security-review` discharged, with grounds:** it reaches pending diffs only,
and this delta is landed with a clean tree at `9aef298`; nothing is pending for
it to read. Lens 4 was run manually at both altitudes instead — the floor as a
control (EP1–EP3) and the floor as an attack surface (EP7), the latter checked
against current published Actions hardening guidance rather than recall.

---

### EP1 — `scope` removes cover from the two scanners that may never be softened, and nothing enumerates it · **MAJOR**

**Claim.** The design's safety argument is a pair: boundary and integrity checks
have no advisory form (`tools/floor.py:519-524`, selftest `:814-815`), and every
softening is a declaration read out estate-wide. `scope` breaks the pair. It
applies to *any* scanner, including `secretscan` and `leakscan`, and it is the
one declaration no board reads — so a repo can reduce a boundary check to a
subtree, or to nothing, and read green everywhere.

**Evidence.** Driven at HEAD in a throwaway repo carrying a live-shaped
credential fixture at its root:

- `{"scope": {"secretscan": ["docs"], "leakscan": ["docs"]}}` → both scanners
  report clean, the render shows `✅ secretscan enforced` / `✅ leakscan
  enforced`, floor rc 0. The credential is untouched at the root.
- `{"scope": {"secretscan": ["nosuchtree"]}}` → `⏭ secretscan skipped (no
  nosuchtree tree in this repo)`, rc 0, by the deliberate branch at
  `tools/floor.py:743-749`. A boundary check that runs nowhere, one JSON typo
  from a check that runs everywhere.
- The same hole through `flags`: `{"flags": {"secretscan": ["nope/"]}}` on the
  hook plane appends a non-matching repo-relative prefix — `✅ secretscan
  enforced`, rc 0, a staged credential fixture unread. `FORBIDDEN_FLAGS`
  (`:291`) is a blocklist of four mode flags; a *positional* narrows cover
  without touching it. This is the absolute-path defect of `e64c79a`/`6998c2a`
  reached through a config file instead of a rendering bug — and `6998c2a`
  closed only the absolute spelling, not the non-matching-relative one.
- `docs` is a third door: a records-tree name that does not exist skips every
  prose check by the same branch.

**Not theoretical.** Of the two `.atelier-floor.json` files in the estate that
declare either key, one child declares **both `scope` and `flags` on
`leakscan`** — the worked networking case `tools/floor.py:83-89` and ADR:59-63
describe. That is legitimate and reviewed; the finding is that its cover
reduction appears on no board, in no `--json`, and in no exit code.

**Counsel.** Three options, in increasing strength. (a) Print `scope`, `flags`
and a non-default `docs` on the `floorfleet` board and in `--json`, beside
`advisory`/`disabled` — the cheapest fix, and the one the design already claims
(EP2). (b) Make a `scope`/`flags` declaration on a scanner whose `advisory` is
`None` require a stated reason, exactly as `disabled` does — a boundary check's
cover reduction is at least as reviewable as its removal. (c) Refuse a `scope`
that resolves to nothing for a no-advisory-form scanner, rather than skipping
it: the skip branch is right for a code-only repo with no records tree, and
wrong for `secretscan`. The principal decides; (a) plus (b) looks proportionate.

### EP2 — "read out estate-wide by `floorfleet`" does not reproduce · **MAJOR**

**Claim.** The sentence that justifies letting `flags` weaken a check is a
statement of fact about another tool, and that fact is false at HEAD.

**Evidence.** `tools/floor.py:417-419`: "This genuinely weakens a check, which
is why it lives in a committed file that `floorfleet` reads out estate-wide —
declared and visible, never quietly applied." Commit `e64c79a` makes the same
claim for both keys ("Both live in the committed .atelier-floor.json and are
read out estate-wide by floorfleet"), and ADR:59-63 leans on it. But
`ChildFloor` (`tools/floorfleet.py:139-153`) carries `advisory`, `disabled` and
`local` only; `evaluate` (`:240-263`) reads exactly those three keys; `render`
(`:284-289`) prints exactly those three. Neither `scope` nor `flags` nor `docs`
appears anywhere in `tools/floorfleet.py` — confirmed by grep and by the live
board above, which shows no line for the one child that declares both.

**Counsel.** This is the delta's only claim that is wrong rather than
incomplete, and it is load-bearing for EP1's severity — so fix the mechanism
(EP1a) rather than the sentence. If the board columns are deferred, the comment,
the ADR line and the CHANGELOG entry should say "declared in a committed file"
and stop there. Under this repo's apex, a claim about a sibling tool's behaviour
is either verified or not made.

### EP3 — the hook plane's "full cover" for `leakscan` is asserted, never enforced · **MAJOR**

**Claim.** The two-plane design rests on an explicit asymmetry: CI is
structural-only *and declared so*, while "the full cover lives on the hook"
(`tools/floor.py:36-44`, ADR:50-52). Nothing on the hook plane requires the
machine-local term list. A clone without one gets CI-grade cover from its
pre-commit gate while every artefact says otherwise.

**Evidence.** `leakscan.py:289` offers `--require-terms`, which fails when no
list is found. The hook template (`tools/floor.py:226-231`) omits it — the only
`--require-terms` mention in the whole delta is the CI-side comment at `:228`
explaining its absence *there*. Driven at HEAD with the term list pointed at a
non-existent file and a bare `HOME`: `⚠ no local term list found — scanned
STRUCTURAL patterns only`, then `✅ leakscan enforced`, floor rc 0. The warning
sits ten lines above a green tick, in scanner prose the hook prints on every
commit; `floorfleet` has no column for it, so the estate cannot see which clones
have real personal-data cover.

**Note on scope.** The behaviour predates this delta; the *claim* is new here —
this delta is where the plane asymmetry became doctrine and got written into the
registry and the ADR. It is in scope for that reason, and the counsel is small.

**Counsel.** Add `--require-terms` to the hook template. It fails closed with
the remedy `leakscan` already prints, and it makes the sentence true. If a
first-run block on a fresh clone is judged too sharp, then the honest fallback
is to downgrade the wording to "full cover *when a term list is present*" and
give `floorfleet` a terms column — but the block is the better answer: this is
the boundary the public-repo rule depends on.

### EP4 — a SHA-pinned caller does not freeze the policy · **minor**

**Claim.** The documented escape hatch from the accepted estate-wide blast
radius is "children may pin deliberately" (ADR:87-90, `floor.yml:22-28`).
Pinning the `uses:` ref does not do that: the reusable workflow checks atelier
out at `inputs.atelier-ref`, default `main`, so a pinned child still runs the
registry and scanners from atelier's tip. Only the transport is frozen.

**Evidence.** `.github/workflows/floor.yml:58-64` (input default `main`) and
`:86-92` (`ref: ${{ inputs.atelier-ref }}`). The shipped caller
(`docs/build/templates/workflows/floor.yml:80-84`) passes no `atelier-ref`.
`tools/floorfleet.py:131-133` therefore mislabels: `pinned — propagation frozen
here` when propagation is not frozen. ADR:87-88 calls this alternative
"Reproducible", which for scanner behaviour it is not.

**Counsel.** Document that a deliberate pin is two edits (`uses:@<sha>` *and*
`atelier-ref: <sha>`), and reword the board's `pinned` detail to "workflow
pinned; scanners still float unless `atelier-ref` is set too". Cheap, and it
matters precisely for the reader who is acting on the ADR's own mitigation.

### EP5 — the registry-driven selftest loop reads the wrong root · **minor**

**Claim.** The loop that proves the instruments before trusting their pass
enumerates the registry against the runner's workspace, not the calling repo. Its
`disabled` filter is therefore inert, and a child's own checks are never
selftested at all.

**Evidence.** `.github/workflows/floor.yml:105` runs `floor.py --list --plane
ci` with no `--root`, so it resolves `.` — the workspace holding `repo/` and
`atelier/` as siblings and no config — while the floor step twelve lines down
(`:113`) correctly passes `--root repo`. Consequences, both verified locally by
driving `--list` with and without the right root: a child that declares a
scanner `disabled` still has it selftested (harmless noise), and a child's
`local` checks never appear in the loop, so the one class of check atelier has
never reviewed is exempt from the 2026-07-11 N5 prove-the-instrument gate the
step exists to enforce. Latent inverse in the parent: `.github/workflows/ci.yml:95`
uses the same shape with the *correct* root, so the day atelier declares a local
check its own CI will run `tools/<name>.py --selftest` and go red unless that
script answers `--selftest`.

**Counsel.** Pass `--root repo` at `:105`, and then decide deliberately what
proving means for child-owned code: skip `local` in the loop (with a comment
saying the child's CI owns it), or require a local check to answer `--selftest`
and say so at the seam's declaration site. Either is fine; the current state is
neither, and it reads as covered.

### EP6 — ADR 0008 no longer describes the mechanism it governs · **minor**

**Claim.** ADR 0008's Decision section has five numbered clauses and no mention
of the repo-local seam. A reader of the decision record concludes a child may
only subtract from the floor, when since `f526dea` a child may add a check of
its own that runs inside the floor, on both planes, from the child's own script.

**Evidence.** ADR:46-81 — decision 2 states what a repo may declare
(`advisory`, `disabled`, `scope`, `flags`) and closes "What a repo may **not**
do is change whether a check blocks"; nothing about `local`. `f526dea` touched
`tools/` only; `76f4acc` placed the seam's doctrine in `tools/floor.py:76-128`,
`docs/build/REPO-STANDARD.md`, the CONTRIBUTING template and the caller header —
every point of use, deliberately and well — but not the ADR. The ADR file is
unchanged since `78e1d20`.

**Counsel.** One clause (a Decision 6, or two lines on decision 2) pointing at
`tools/floor.py`'s seam section. The seam's own merits are not this pass's
business — its review pointer is separately queued — but ADR 0008 is the record
this pass reviews, and per this repo's own convention the re-litigable decision
belongs in it.

### EP7 — the trust-surface comparison in *Rejected* is asserted, not argued · **minor**

**Claim.** ADR:93-95 dismisses the sync-bot alternative as "a much larger trust
surface than a read-time `uses:`". That is true on credentials and false on code
execution, and only the first half is stated. A floating `uses:` executes
unreviewed atelier code in every child's CI on every push; a bot needs write
access but emits reviewable diffs. The decision is still defensible — it is not
shown to be.

**Evidence.** `.github/workflows/floor.yml:74-79` applies the opposite
reasoning two files over, SHA-pinning third-party actions precisely because a
movable ref can be repointed at new code; ADR:97-99 and `floor.yml:125-129`
apply it again to the signing trust root (2026-07-12 review G7: a floated trust
root would let anyone with write to atelier mint trust for every child). The
same sentence structure describes the registry, which floats. Checked against
current published guidance rather than recalled: Actions hardening guidance
treats every floating `uses:` as a supply-chain entry point while explicitly
accepting `@main` for internal callees *inside the same trust boundary* — so
the decision sits on the boundary claim, and the operative control is who can
write atelier's `main`, which the ADR never names. ADR:113-115 does name the
public-visibility dependency, which is the adjacent risk handled well.

**Counsel.** Add one clause to the Consequences: the control that makes floating
`@main` safe is atelier `main`'s own protection (branch protection, signed
commits, review on the registry), not the pin — and a compromise there is
arbitrary code in every child's CI, not merely a broken floor. That converts an
accepted risk into a named, checkable one.

### EP8 — `wired` is a text match, and trigger shape is not in the conceded blind spots · **LOW**

**Claim.** `floorfleet` classifies on workflow text and concedes it cannot see a
job that never runs (`tools/floorfleet.py:71-74`). Trigger shape belongs in that
list and is, unlike the Actions-API cases, cheap to read from the same text: a
caller whose `on:` has only `workflow_dispatch` reports `wired ✅` while nothing
runs on push. Symmetrically, a repo calling the floor from a differently-named
workflow file reports `absent 🛑` — fail-safe, so much less serious.

**Evidence.** `tools/floorfleet.py:104` (fixed `FLOOR_PATH`), `:123-136`
(`classify` reads only the `uses:` line and scanner names), `:71-74` (the
concession, which names conditions and disabled workflows but not triggers).

**Counsel.** Either parse `on:` for `push`/`pull_request` and add a state, or add
five words to the concession. The concession is enough for now; silence is not.

### EP9 — a missing `python3` prints only how to bypass · **nit**

**Claim.** The hook guards `floor.py`'s absence with a three-line remedy but not
the interpreter's, so the one actionable line a contributor sees on a machine
without `python3` is the `--no-verify` bypass.

**Evidence.** `tools/pre-commit.sample:57-63` (the floor.py guard, with remedy)
versus `:65` (bare invocation). Driven with `python3` off `PATH`: `line 65:
python3: command not found` then `To bypass in a genuine emergency
(discouraged): git commit --no-verify`, rc 1. Fail-closed holds — rc is non-zero
by every route tested, including no `git` at all (rc 127) — so this is presentation
only.

**Counsel.** A `command -v python3` guard mirroring the one above it.

---

### What held under attack

- **Fail-closed is real, on every route driven.** Missing `floor.py`, missing
  individual scanner, missing local script, non-executable local script,
  unparseable config, unknown scanner name, reasonless disable, `advisory` on a
  scanner with no advisory form, `--warn`/`--json` smuggled through `flags`,
  `local` colliding with a fleet name, `local.run` climbing out of the repo or
  going absolute, `local` on no plane — all block, all with a stated remedy. The
  `core.hooksPath` route is exercised by a real refused commit, not by
  resemblance, and the tracked copy is diffed against the sample and
  mode-checked. This is the delta's strongest work.
- **The absolute-path near-miss is dead in three places** — refused by both
  boundary scanners with rc 2 and a named working form, never emitted by
  `_render` (`tools/floor.py:605-616`), and pinned by tests in four suites.
  Whole-diff cover with no positional still blocks, so the private-repo scoping
  route is genuinely untouched.
- **The plane split is honest where it is declared.** CI's structural-only
  `leakscan` is stated in the registry, the workflow header and the ADR, and the
  registry refuses `--require-terms` there for the right reason. EP3 is the
  hook's *unstated* half, not this.
- **`local` only ever adds.** The collision, escape, absolute-path, reasonless
  and plane guards all hold, off-plane local checks list as `skipped` rather
  than passing, and the `advisory`-semantics difference for a local check is
  documented at the point a reader meets it.
- **Enumeration is fail-safe and true.** `unknown` and `absent` both count as
  red, `--check` exits non-zero, the comment-stripping guard against
  false-`vendored` is selftested, the fork-owner case classifies as wired, and
  the remote plane — the one that answers what actually runs — agrees with the
  local plane across all thirteen children.
- **The parent is not special, in fact and not just in prose.** `ci.yml:137`
  runs the shipped floor with atelier's own scoping declared the way a child
  declares it, and the whole-tree run is green at HEAD.
- **The seeded question (ADR:5-8) is answered honestly in the ADR itself.**
  The trade — slow silent staleness for fast loud estate-wide breakage — is
  named as a consequence, not buried; the "newest is safest" grounding is the
  same reasoning already on the record for the scanner code, and the contrast
  with the never-floating signing trust root is drawn explicitly in both the
  ADR and the workflow. My reading: the trade is right for a *floor*, and the
  registry's contract tests are proportionate to breakage-by-accident. What it
  does not cover is breakage-by-malice (EP7) or the mitigation that does not
  work as documented (EP4) — neither of which changes the answer.

### Reviewer's own residuals, owned

- The pre-wiring measurements (12/13 stale; 15 findings in 4 repos) are
  historical and not re-runnable at HEAD; I checked only what survives (child
  count, current wiring, suite count) and accepted the rest as recorded.
- `--remote` was run read-only via `gh` and reports the default branches; it
  cannot prove the Actions runs succeed, which the tool correctly disclaims.
- I read child `.atelier-floor.json` files to test whether EP1 is live. Nothing
  from a private child's tree is reproduced here beyond the scanner names it
  declares against — the class of the finding, not the estate's contents.

---

## Reconciliation — after reading the deferred section and the intent record

Read only after the findings above were durably written and the floor re-run
green with them in place. The intent record is
`docs/sessions/2026-07-25-1311-policy-propagation.md`. It **withdraws nothing**.
It sharpens three findings, adds one, and supplies evidence for two claims I
could not re-run. The withdrawn-directory ban was honoured throughout this phase.

**Revised counts: 3 MAJOR · 5 minor · 1 LOW · 1 nit.** Verdict unchanged:
**PASS-WITH-FINDINGS**.

### Sharpened

- **EP1 — sharpened, and now grounded in the author's own stated invariant.**
  The record's design commitment reads: "Softening is not the child's call.
  Boundary and integrity scanners have no advisory form; `flags` refuses the
  mode-changing arguments outright" (record:63-64). That is the intent my probe
  defeats without touching a flag at all — a non-matching positional prefix
  through `flags`, or a narrowed `scope`, reduces a boundary check's cover while
  every mode-changing argument stays refused. So this is not a disagreement about
  what the design should do; the implementation does not reach the invariant its
  author wrote down. Sharper still: the record calls the absolute-path fix "Fixed
  at the **class** — those two are the only scanners with a staged mode"
  (record:118-120). The class is not "absolute paths"; it is "a positional that
  matches no staged path". Absolute is one member and is now refused (rc 2); the
  non-matching relative member still exits 0. EP1 is the unfixed remainder of the
  class the record claims closed.
- **EP1's live case — sharpened in the work's favour.** The record shows the one
  child that scopes and flags `leakscan` was verified rather than assumed: the
  author briefly mis-flagged that hook, then confirmed its relative prefix is
  correct and does block, and corrected before touching the child (record:78-80).
  So EP1 is purely about *visibility* of a reviewed, deliberate cover reduction —
  not a claim that any child is misconfigured. That is how the counsel should be
  read.
- **EP2 — narrowed to its true home.** The record's own wording is accurate: it
  says `floorfleet` reads out `advisory`/`disabled` (record:59-62) and never
  claims it reads `scope`/`flags`. The false claim therefore lives in
  `tools/floor.py:417-419` and in commit `e64c79a`'s message, not in the session
  record. EP2 stands unchanged in substance and shrinks in blame.

### Added

- **EP10 — the "prove it landed" command proves the weaker of the two claims ·
  minor.** Commit `c3ef60d` states the distinction explicitly: "'I ran the config
  lines' and 'the hook works' are different claims" — then supplies
  `floor.py --list --plane hook` (`docs/build/templates/CONTRIBUTING.md:23-27`),
  which proves the tools path resolves and the config parses. It does not prove
  git will invoke the hook: a mistyped or unset `core.hooksPath` leaves that
  command printing a clean registry while every commit goes unscanned — the exact
  residual the surrounding prose names two lines earlier. *Counsel:* have it
  print `git config --get core.hooksPath` as well, or use `git hook run
  pre-commit` (git ≥ 2.36), which exercises the real route. Surfaced during
  reconciliation from the follow-on commit rather than from the intent record;
  recorded here rather than silently folded above.

### Evidence the record supplies that I could not re-run

- **End-to-end proof of the rollout exists and is better than all-green.** One
  child's floor run passed and another failed on a real `leakscan` finding, with
  the workflow clean in both (record:99-105) — deliberately, because all-green
  would not distinguish "the gate works" from "the gate never fires". My own
  re-run could only show 13/13 wired on both planes. Corroborates the "what held"
  section; independently unverified by me.
- **Two children were bootstrapped with `--no-verify`** because the gate blocked
  its own installation, each commit saying so and listing what was found
  (record:107-111). That is the adoption cost the ADR's "adopting repos will go
  red first" consequence predicts, discharged honestly. No finding: it is a
  recorded, bounded exception, and the record itself draws the line ("once is the
  honest resolution; twice would be a habit").

### My own enumeration error, owned

The brief's path list omitted `tools/test_floorfleet.py`, so my
`git log` window missed **`91e78f4`** (floorfleet contract tests, 186 lines,
suite 640 → 656) — the record names it at line 55. No finding changes: I ran
that suite (23 tests, OK) via `unittest discover`, and re-read `floorfleet.py`
in full. But my enacting set was five commits plus three follow-ons when it
should have been six plus three, and I established it from a path list rather
than widening it once I had the tool inventory.

### The seeded question, answered against the record

The deferred pointer asks the same question ADR:5-8 asks, and the record adds
the fact that most changes my answer: the rollout risk I would have weighed
against the floating trade was **measured, not assumed** — the two scanners that
cannot be softened read only the staged diff on the hook plane, so pre-existing
findings cannot block a commit, which collapsed the blast radius from "several
repos unworkable" to two repos with whole-tree findings (record:89-97). The
author proposed staging, the principal overruled it, and the check that resolved
it was a fact about the mechanism rather than a preference. My verdict stands:
**for a floor, the trade is right** — newest is safest, staleness was the
measured failure, and the contract tests are proportionate to
breakage-by-accident. The two gaps remain as filed: the documented escape hatch
does not work as written (EP4), and breakage-by-malice is unnamed (EP7). Neither
is an argument for pinning; both are arguments for saying out loud that the
control is atelier `main`'s own protection.
