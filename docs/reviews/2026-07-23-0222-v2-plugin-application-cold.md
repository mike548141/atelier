# Review brief — v2-plugin application (rule-4 cold pass on the applied rulings)

- **Date**: 2026-07-23, 0222 UTC claim; findings committed 0232–0250 UTC (`date -u`).
- **Subject (refs only, as handed)**: the v2-plugin application — delta
  `ff8a07f` (the VP1–VP8 application) + the rebase resolution in `2271a44`,
  merge `0de6f52`; the shipped v2 plugin bundle 0.2.0.
- **Reviewer**: rule-4 cold reviewer, worktree `queue-reviews` (clean at
  HEAD `3107ea4`), read-only git, this one file the only write.

**Spawn provenance** (stated per REVIEW.md rule 4): this review was spawned by
a non-author taker session that the principal (Mike) opened and pointed at the
review queue on 2026-07-23; neither the plugin work's authoring/orchestrating
session nor its instructed workers started or instructed this review or this
reviewer; the taker authored none of the chain and gave the reviewer refs only.

## What the work is — as this reviewer establishes it from the deltas and HEAD

`2271a44` (authored 2026-07-21, re-committed 2026-07-23 in a rebase across
~155 main commits) is the v2 plugin widening: `create-repo` de-instanced into
the bundle (`skills/create-repo/SKILL.md` + `instance.yaml.example`, identity
externalised to an adopter-owned `~/.atelier/instance.yaml`), a two-mode
doctrine-source resolver (live checkout → git-SHA pin; bundled plugin → plugin-
version pin), and two thin command wrappers (`commands/worktree.md`,
`commands/fleet-pins.md`) over the bundled house tools. Manifests
0.1.0 → 0.2.0. `ff8a07f` applies the principal's VP1–VP8 rulings on that work:
a canonical bundled-mode doctrine-block variant in `PROPAGATION.md`, signing
externalised as a profile fact (honest default off), README "What you get"
corrected, the ls-count template guard replaced by a structural must-exist
check, schema single-sourced, markup fixed. `0de6f52` is the two-parent merge
that ships it. Both delta commits are self-authored doctrine by function (a
skill that stamps behaviour into other repos) — rules 3 and 4 apply: findings
here are the principal's to decide; this reviewer recommends and applies
nothing.

## Attack surface (the reviewer's own, named first)

1. **The rebase is the riskiest move** — ~155 commits crossed; a resolution
   can silently drop either side. Verify content-bearing files byte-identical
   across `1516ae1` (pre-rebase original) → `2271a44`, and that the one
   deliberate resolution (session-onramp) kept both sides.
2. **The bundle must be coherent as shipped** — README claims vs actual 0.2.0
   contents; manifests agree; every referenced tool/skill exists and runs.
3. **The applied rulings must not have left stale siblings** — a behaviour
   change (signing) applied at the skill without sweeping the doctrine docs
   that describe the same step is a live contradiction (PRINCIPLES §6).
4. **The stamped block is inherited by every scaffolded repo** — what it
   instructs a consuming session to trust and execute, and whether its
   bundled-mode drift check is sound across a plugin update.
5. **Retirement completeness** — the superseded baked-identity global skill:
   gone, and no living surface still points at it as current.
6. **Every "floor green" claim re-run at HEAD**, and the CHANGELOG's own
   unexercised flags checked against every surface that might present those
   paths as proven.

## Four lenses

1. **Approach & assumptions** — is externalise-don't-strip the right
   de-instancing; is the two-mode resolver's degradation honest.
2. **Correctness & quality** — do the applied rulings reproduce at HEAD; did
   the rebase introduce drift; proofs re-run.
3. **Completeness / harvest** — sweeps owed by the changes; stale references;
   retirement.
4. **Security & privacy** — design altitude for a bundle that stamps behaviour
   into other repos (trust surfaces a consuming repo inherits), plus the
   public-repo leak check; explicit discharge of what cannot be aimed.

**Deferred material** (not opened before findings were durably written below):
`docs/reviews/2026-07-22-1215-v2-plugin-deinstance-cold.md` (the prior verdict
and its §Decisions) and the ADR
`docs/decisions/2026-07-21-0748-deinstance-create-repo-for-the-plugin.md`.
Reconciliation sits in its own marked section at the end.

---

# Verdict — PASS-WITH-FINDINGS (no MAJOR)

**0 MAJOR · 2 minor · 1 LOW · 1 nit.** No MAJOR finding: under the
cycle-termination rule this pass **closes the v2-plugin cycle** — what follows
is decided into the backlog by the principal, and this application does not
spawn another full ceremony.

**Spawn provenance** (repeated per rule 4): this review was spawned by a
non-author taker session that the principal (Mike) opened and pointed at the
review queue on 2026-07-23; neither the plugin work's authoring/orchestrating
session nor its instructed workers started or instructed this review or this
reviewer; the taker authored none of the chain and gave the reviewer refs only.

**Residual rule-2 exposure, named not denied** (per REVIEW.md's
application-review sequencing): the deltas reviewed carry the prior verdict's
decision stamps in their commit messages, the CHANGELOG, and
ROADMAP/ROADMAP-DONE — all read pre-findings as part of the work itself. Two
lines of the prior verdict (VP7's text) also surfaced in a repo-wide grep for
global-skill references before findings were committed; the file itself was
not opened until the reconcile step. The findings below were formed from the
work at HEAD, but the ruling summaries were in view — that exposure is
structural to an application review and is declared here.

## What was re-run, with results (all at HEAD `3107ea4`, 2026-07-23 UTC)

- **Tests**: `python3 -m unittest discover -s tools` — **330 tests, OK**.
  `node --test instruments/*.test.js` — **150 pass, 0 fail** (the delta's
  "139" has since grown with later merges; all green).
- **Selftests** (nine): secretscan, leakscan, linkscan, licenscan, reviewscan,
  sizescan, signscan, worktree, pins — **all exit 0**.
- **Scanners as the pre-commit hook and floor invoke them**:
  `secretscan --root . .` ✅ · `leakscan --root . .` ✅ (structural + local
  terms) · `linkscan --root . .` ✅ · `reviewscan --root . .` ✅ (3
  post-boundary decision records carry review lines) ·
  `licenscan --expect Apache-2.0 .` ✅ · `sizescan --check --root . .` exit 0
  (one size-advisory on `docs/ROADMAP.md`, 480 lines — advisory never fails
  `--check`; not attributable to this delta).
- **The skill's own step-0 structural guard, verbatim** (`$SRC=.`): all eight
  load-bearing seeds present, no `MISSING` — the VP4 replacement check passes
  against the real templates tree.
- **Rebase drift probe**: `git range-diff 1516ae1^..1516ae1 2271a44^..2271a44`
  plus per-file `git diff 1516ae1 2271a44` over every plugin surface —
  `skills/create-repo/SKILL.md`, `instance.yaml.example`,
  `commands/{worktree,fleet-pins}.md`, both manifests: **byte-identical**. The
  only content-bearing difference is `skills/session-onramp/SKILL.md`, and
  that diff is exactly additive: main's queue-run companion sentence inserted
  into the branch's restructure, nothing dropped from either side. The VP5
  resolution claim **reproduces**.
- **Retirement**: `~/.claude/skills/` is empty; the superseded skill sits
  archived at
  `~/.claude/skills-retired/create-repo-baked-identity-retired-2026-07-23/`.
  Every in-repo reference to `~/.claude/skills/create-repo` lives in immutable
  records (sessions, prior reviews) or the deferred ADR — no living doctrine
  surface presents it as current. Retirement is **complete** (it post-dates
  the merge, per VP7's owed-after-merge status — done as recorded).
- **Bundle coherence**: README "What you get" names exactly what 0.2.0 ships
  (4 skills, 4 commands, docs bundled via root-as-plugin); both manifests say
  0.2.0; every `${CLAUDE_PLUGIN_ROOT}/tools/*.py` a command references exists
  and selftests green; profile keys the skill references all exist in
  `instance.yaml.example`.
- **CHANGELOG honesty flags**: "not yet exercised end-to-end — the interactive
  first-run fill and a bundled-mode scaffold" is carried in the CHANGELOG, the
  SESSIONS entry, and an explicit owed ROADMAP item. No surface at HEAD
  presents either path as proven — the claim discipline holds. (The delta's
  own commit message says "nothing here claims review" — accurate.)

**Lens-4 discharge lines.** `/security-review` was not run: this is a
landed-delta review with no pending diff to aim it at, and the work's file
class (markdown prose + JSON manifests) is barred by the scanner's own
exclusions — a clean pass would be definitionally empty and is weighed as
nothing, per REVIEW.md's SL2 caution. Supply-chain trust of the plugin install
channel itself (marketplace clone integrity) is Claude Code's surface, not
this bundle's — out of aim, named as such. What *was* assessed at design
altitude: the trust surfaces a consuming repo inherits are (a)
`hooks.atelierTools` → code executed on every commit — named in the hook's own
TRUST NOTE, same trust class as installing the hook, fail-closed; (b) the
stamped session-start drift command — git/grep against adopter-owned paths,
benign; (c) the identity profile — personal data lives at
`~/.atelier/instance.yaml`, outside every repo, never committed, placeholders
RFC 2606 with leakscan allow-markers; (d) scaffold defaults `visibility:
private`, publishing stays a floor action, remote creation requires the ask to
have included it. Public-repo leak check: all boundary scanners green at HEAD;
the only identity in the bundle is the author's own deliberate attribution.

## Findings

### VA1 · minor — VP2's signing change was not swept into the two doctrine docs that state the old behaviour

**Claim.** The application externalised signing (profile fact, default off;
the skill's bake now conditional) but left both parent doctrine surfaces
asserting the old unconditional bake, creating a live contradiction with the
very process document the skill tells the model to follow.

**Evidence.** `docs/method/SIGNING.md:51` — "`create-repo` additionally bakes
`commit.gpgsign=true` repo-locally — belt-and-braces so a new repo signs even
where global config has drifted." `docs/build/REPO-STANDARD.md:181` (step 1 of
the new-repo process): "set the git identity (instance-local) and bake
repo-local `commit.gpgsign=true`". The skill (`skills/create-repo/SKILL.md`,
Process block) now stamps `commit.gpgsign` **only when the profile's `signing`
fact is true**, with the rationale VP2 ruled. The skill's own step order says
"Follow REPO-STANDARD's 'new repo' process" and "read these first" — a bundled
adopter's model reads the unconditional instruction before reaching the
conditional one. PRINCIPLES §6: a refined learning sweeps its stale claims in
the same commit; `ff8a07f` touched neither file. (SIGNING.md:188's dated
done-log is immutable-history in character, but its "REPO-STANDARD's new-repo
process states the same" clause now propagates the stale claim from a living
doc.)

**Reviewer counsel.** Sweep both lines to the profile-gated form — e.g.
"bakes `commit.gpgsign=true` when the instance profile's `signing` fact says
the machine signs (default off; atelier-style profiles keep it on)" — and
annotate, not rewrite, the SIGNING.md done-log. Small, two-file, no behaviour
change: the executing surface is already correct, which is why this is minor
and not MAJOR.

### VA2 · minor — two shipped surfaces embed opposite assumptions about plugin-update semantics, and the bundled-mode drift check's soundness across an update is unproven

**Claim.** `commands/install-hook.md` tells the adopter a plugin update leaves
the stored scanner path "dangling" (a version-pinned copy), while the
bundled-mode doctrine block (PROPAGATION § The bundled-mode variant, stamped
by VP1's fix) stamps an absolute `<plugin-path>` and relies on
`grep '"version"' <plugin-path>/.claude-plugin/plugin.json` tracking the
*live* install. Both cannot be right. If an update relocates the install and
leaves the old copy readable, the stamped drift check **false-greens
silently** — it reads the stale copy, still sees the stamped `<VERSION>`, and
reports "no drift" while the doctrine moved: the exact failure PROPAGATION
exists to prevent. If the old path dies, the check fails visibly — acceptable.

**Evidence.** `commands/install-hook.md:44-49` ("after a **plugin update or
uninstall**… the stored scanner path is version-pinned to the installed plugin
copy, so an update leaves it dangling") vs `docs/method/PROPAGATION.md:186-193`
(the Source & drift bullet, absolute `<plugin-path>`). Which semantics the
harness actually has could not be grounded here: no atelier plugin is
installed on this machine to probe (`~/.claude/plugins/installed_plugins.json`
is empty — an observation about this machine, not a claim about any other),
and the plugins cache shows at least one unrelated plugin held as a copy, so
both semantics are live possibilities. This sits squarely inside the
already-flagged unexercised bundled-mode path.

**Reviewer counsel.** Fold the update case explicitly into the owed
exercise-e2e ROADMAP item: install 0.2.0, scaffold bundled-mode, update the
plugin, and observe whether the stamped path tracks, dangles, or goes stale —
then make the variant's bullet state what a missing path means (re-locate the
install, re-check) and reconcile install-hook.md's wording to the observed
behaviour. No text change before the observation: the honest fix here is the
exercise, not a guessed sentence.

### VA3 · LOW — the template's guidance comment carries the placeholder literals the stamp-proof grep hunts

**Claim.** `docs/build/templates/CLAUDE.md:1-16` names all six placeholders
(`<atelier-path>`, `<SHA>`, `<owner/repo>`, `<visibility fact>`,
`<plugin-path>`, `<VERSION>`) inside its guidance comment. A stamped child
that retains the comment trips step 5's whole-tree grep ("expect: no hits
ANYWHERE") even when correctly stamped. The failure is *visible* (it forces
comment deletion, arguably by design), but the instruction to delete the
comment lives only inside the comment itself; no skill step names it.

**Evidence.** The grep at `skills/create-repo/SKILL.md` step 5 vs the template
header; VP1's fix extended both (adding `<plugin-path>`/`<VERSION>` to comment
and grep) without closing the loop.

**Reviewer counsel.** One clause in step 5 — e.g. "delete the template's
guidance comments first; the grep treats a surviving comment as an unfilled
placeholder" — or an explicit note that the grep hit on the comment is the
intended nudge. Cosmetic either way.

### VA4 · nit — the skill's intro enumerates seven facts; the profile now carries eight

**Claim.** `skills/create-repo/SKILL.md:11-14` lists "(git identity, remote
account, workspace path, copyright holder, locale, exemplars, signing
posture)" — VP2's eighth fact was added by *replacing* the doctrine-source
fact in the list rather than extending it; `instance.yaml.example` carries
both (`signing` and `atelier_path`), and ROADMAP-DONE says "eight instance
facts". **Counsel**: add "doctrine source" back (or say "eight — see
`instance.yaml.example`", which is the single source VP6 established anyway).

## Reconciliation — deferred material (opened only after the findings above were durably written)

Opened at 0240 UTC, after VA1–VA4 were durably written above: the prior
verdict `docs/reviews/2026-07-22-1215-v2-plugin-deinstance-cold.md` (including
its §Decisions) and the ADR
`docs/decisions/2026-07-21-0748-deinstance-create-repo-for-the-plugin.md`.
Each of Mike's rulings checked against what actually ships at HEAD:

- **VP1 [fixed] — applied faithfully, fix reproduces.** The canonical
  bundled-mode variant exists in `PROPAGATION.md` § *The bundled-mode variant*
  with exactly the two substitutions the ruling required; the skill's step 5
  stamps it verbatim with a runnable version check; the template header names
  the variant; the extended placeholder grep covers `<plugin-path>`/
  `<VERSION>`; the ADR carries the dated implemented note in Consequences.
  (My VA2 pressure-tests the version check's soundness *across a plugin
  update* — a question beyond the ruling's frame, not drift from it; VA3 is a
  loose end of the mechanism VP1's fix extended.)
- **VP2 [fixed] — applied faithfully at the surfaces the ruling named; the
  sweep it implied was incomplete.** `signing` is the eighth profile fact,
  honest default off, the bake profile-gated, the ADR corrected by an
  append-only Amended note exactly as ruled ("the enumeration of seven above
  stands"). VA1 (SIGNING.md / REPO-STANDARD still stating the old
  unconditional bake) is not drift from the ruling — those files were not in
  VP2's evidence — but it is the PRINCIPLES §6 same-commit sweep the fix owed
  and missed. VA4's seven-item intro list was introduced *by* `ff8a07f`
  itself (the rewrite swapped "doctrine source" out for "signing posture"
  rather than extending to eight) — attributable to the application delta,
  consistent with the ADR's eight-fact reality.
- **VP3 [fixed] — reproduces.** README "What you get" states 0.2.0's actual
  contents; the false "follow in a later version" line is gone from the tree.
- **VP4 [fixed] — reproduces.** The structural must-exist check replaces the
  ~19-file ls count; run verbatim against the real templates tree it passes
  with no `MISSING`.
- **VP5 [fixed] — reproduces, byte-verified.** All plugin content surfaces
  identical across `1516ae1` → `2271a44`; the sole content-bearing resolution
  (session-onramp) is exactly additive — main's queue-run sentence inserted
  into the branch's restructure, nothing dropped from either side. The prior
  verdict's feared silent-drop did not occur.
- **VP6 [fixed] — reproduces.** One schema home (`instance.yaml.example`,
  now "your-account"); the skill's step 1 points at it and restates nothing.
- **VP7 confirmed — done as recorded.** The superseded baked-identity global
  skill retired post-merge same day, archived machine-locally
  (`skills-retired/create-repo-baked-identity-retired-2026-07-23`); no living
  repo surface presents it as current.
- **VP8 [fixed] — reproduces.** The step-1 tail markup is clean at HEAD.

**Net of reconcile:** all eight rulings were applied faithfully; every
decision stamp's fix reproduces live. Nothing above is overturned; VA1–VA4
stand as written, with VA1/VA4 now attributed precisely (sweep gap and
enumeration swap in `ff8a07f`). No finding rises to MAJOR on reconcile — the
no-MAJOR verdict stands, and with it the cycle's terminal close.

*Per REVIEW.md rule 3, VA1–VA4 are the principal's to decide; this reviewer
recommends and applies nothing.*
