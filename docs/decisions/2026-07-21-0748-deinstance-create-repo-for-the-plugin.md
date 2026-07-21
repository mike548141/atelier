# De-instance create-repo: externalise identity into an adopter profile

**Status**: accepted • **Date**: 2026-07-21

**review**: ⏳ queued — doctrine-substantive (it changes the provenance model of
`PROPAGATION.md` / ADR 0002 for adopters who hold only the plugin), self-authored,
so REVIEW rule 4 binds: pointer queued, **no brief written here**, a non-author
taker writes it and reviews this decision together with the build it authorises.
The build lands via PR, reviewed before merge (the v1-bundle path).

## Context

The v2 plugin widening was chosen 2026-07-13 (Mike's call): spend the next
deliberate widening on making the plugin carry doctrine *as behaviour* — de-instance
`create-repo` so it travels in the bundle, and ship `worktree` + `fleet-pins` as
plugin commands. The roadmap gated it: **scoping pass first, then the build.** This
ADR is that scoping pass, ruled.

The two skills already in the bundle — `session-onramp`, `review-brief` — de-instanced
for free because they **carry zero instance facts**: pure doctrine-application, ship
as-is. `create-repo` is the opposite. Its *entire function is to stamp house
identity* into a new repo — git identity, remote account, workspace path, copyright
holder, locale, exemplar repos, the doctrine-source location. Strip those and the
skill has nothing left to do. So de-instancing here is not *removal*; it is
**externalisation** — the same move that keeps Mike's own identity in `~/.claude/`
and out of this public repo.

A second fact shapes the design: the plugin's `source` is `./` (marketplace.json),
so **the plugin already ships the whole repo** — `docs/method/`, `docs/build/templates/`,
`tools/` all travel in the install directory (`session-onramp` already reads doctrine
from there). No second copy of doctrine needs packaging. But `create-repo` today is a
**global** skill (`~/.claude/skills/`), not in the bundle at all, and it reads its
source from a *sibling* checkout (`$PP/atelier/…`) and pins that checkout's git SHA.
An adopter has no sibling checkout — only the plugin.

Seven instance facts are baked into the current skill: workspace root; git identity;
remote host + account + default visibility; default copyright holder; locale;
exemplar repos; and the doctrine/templates/tools source location.

## Decision

Three rulings (Mike, 2026-07-21 — "I accept your recommendations"):

1. **Externalise the seven facts into an adopter-owned profile.** A single file
   the adopter owns — `~/.atelier/instance.yaml` — read on every run. The bundled
   skill **fills it interactively on first run** (asks the seven facts, writes the
   file) and reads it silently thereafter. It lives in the adopter's home, never in
   a repo, never committed — the same boundary that keeps Mike's context in
   `~/.claude/`. This is the "you become the principal" framing the other bundled
   skills state, made concrete: the profile *is* the adopter declaring themselves.

2. **Two-mode doctrine-source resolver.**
   - *Live mode* — a real atelier checkout is configured or present beside the
     target → read the standard/templates/tools from it and pin its **git SHA**.
     This is Mike's path and any atelier contributor's; no regression, the new repo
     still pins the current doctrine SHA and gets the latest templates.
   - *Bundled mode* — only the plugin is present → read from the plugin's own
     install directory and pin the **plugin version** as provenance.

3. **The SHA pin degrades to plugin-version provenance in bundled mode.** The
   doctrine block `create-repo` stamps hands every future session a drift-check
   (`git -C ../atelier log <SHA>..HEAD`). An adopter with no sibling checkout cannot
   run that; in bundled mode the stamp records the plugin version and the drift-check
   the block carries degrades to a plugin-version comparison. Named here because it
   forks ADR 0002 ("the SHA is the version") for the plugin-only adopter — the pin
   still exists, its *referent* changes.

Accompanying build (same widening, design-trivial, no separate ruling): relocate
the skill to `skills/create-repo/` in the plugin, and wrap the existing house tools
`tools/worktree.py` and `tools/pins.py` as the `worktree` and `fleet-pins` plugin
commands. Version bump on the plugin + marketplace manifests.

## Rejected

- **Strip the instance facts, as with the other two skills.** Impossible: the
  skill's function *is* to stamp them. Nothing survives the strip.
- **Adopter edits the skill file per install (fork).** Defeats "travels in the
  plugin", and rebuilds the exact divergence-by-neglect that `PROPAGATION.md`
  forbids — an unmarked second source free to drift on every plugin update.
- **Environment variables for the profile.** Brittle, invisible, no single durable
  source; a shell-session property, not an adopter identity.
- **Package a second copy of doctrine/templates into a plugin subfolder.**
  Unnecessary — `source: "./"` already ships the whole repo. A second copy would be
  the N-copies anti-pattern inside the doctrine that forbids it.

## Consequences

- **The plugin gains a stateful precondition** the other skills lack: the instance
  profile must exist (or be filled) before `create-repo` can act. One-time first-run
  friction, then invisible. The fill step is the de-instancing made visible.
- **Provenance forks by mode.** Live mode preserves the doctrine-SHA pin unchanged;
  bundled mode pins a plugin version. The drift-check the stamped block carries must
  branch on which — a real, named change to how propagation works for plugin-only
  adopters, not a silent one. It earns the review this ADR queues.
- **The personal-data boundary is preserved, not weakened.** Identity, account,
  paths, holder all live in the adopter's `~/.atelier/`, never a repo — the same
  rule that made it safe to make this repo public.
- **Not done, and owed** (the build this ADR authorises): the de-instanced skill
  itself; the `instance.yaml` schema + its interactive fill, *proven* not asserted;
  the `worktree` + `fleet-pins` command wrappers; the manifest version bump; and the
  rule-4 review before merge. Shipping the widening (the merge / go-live) stays
  Mike's deliberate call, never the agent's initiative.
