---
action: create
description: Scaffold a new repo (or standardise an existing one) to your house conventions — the atelier repo standard, stamped with your identity from an instance profile. Use when asked to create a repo, start a project, or standardise/tidy an existing repo. Sizes the standard to the repo type; never fabricates docs it can't ground.
---

# Repo — create: deliver the house repo standard

This skill is the **delivery vehicle**. It does not *hold* the standard —
**atelier** does. atelier is the source of truth for repo shape and the
cross-cutting doctrine; this skill applies that source as a guided action.
It carries **no identity of its own** — the instance-local specifics a shareable
doc must not hold — eight facts today (git identity, remote account, workspace
path, copyright holder,
locale, exemplars, signing posture, doctrine source; `instance.yaml.example`
is the single source) — come from **your instance profile**, filled
once and read every run. That externalisation is what lets this skill travel in the plugin: you become
the principal it stamps. (Design: `docs/decisions/2026-07-21-0748-deinstance-create-repo-for-the-plugin.md`.)

Read the source, then act.

## Step 0 — resolve the doctrine source (two modes)

The standard, templates, and scanners live in atelier. Find them in one of two
modes, in this order:

- **Live mode** — a real atelier checkout is present (configured in your profile as
  `atelier_path`, or a sibling `../atelier` beside the target). Use it. This is the
  path for anyone who *contributes to* atelier: the new repo pins atelier's current
  git SHA and gets the latest templates.
- **Bundled mode** — only this plugin is present. The source is the plugin's own
  install directory (this skill ships inside a full atelier tree — `source: "./"`),
  which carries `docs/`, `docs/build/templates/`, and `tools/`. Read from there.

Set `$SRC` to whichever resolved. **Confirm the templates are readable**, not just
that the path exists — the load-bearing seeds the steps below stamp must each be
present (a structural check, not a count — counts rot as templates change):

```sh
for f in CLAUDE.md CONTRIBUTING.md LICENSE NOTICE gitignore \
         claude/settings.json workflows/floor.yml docs/reviews/README.md; do
  [ -r "$SRC/docs/build/templates/$f" ] || echo "MISSING: $f"
done                                     # expect: no output
```

Any `MISSING`, **stop and say so** (do not scaffold a repo wisdom-empty from
memory — a repo born without the doctrine block has inherited the costume, not
the doctrine).

**The source (read these first — do not re-derive their content here):**

- `$SRC/docs/build/REPO-STANDARD.md` — the standard: product-in-a-subfolder,
  sizing to the repo type, the standard file set, honest-CI, the two processes.
- `$SRC/docs/build/REPO-BOUNDARY.md` — *before* scaffolding: is this even its own
  repo, or a component/monorepo-folder? Advise proactively.
- `$SRC/docs/method/PROPAGATION.md` — the doctrine block every child repo carries,
  and how the SHA pin + drift check work. **You stamp this.**
- `$SRC/docs/build/templates/` — the seed files. One source, shared with the
  published methodology. You copy from here — you do not keep a second copy.

**Why this exists** (say it back before scaffolding — it drives the judgement
calls): repos where the *reasoning* is recorded, work is **peer-reviewed by an
independent session** (a more capable model where stakes are highest), and
behaviour is **tested for real** — not just repos with working code. That's the
atelier apex applied to repo-craft; the standard is how it lands.

## Step 1 — resolve the instance profile

The identity this skill stamps comes from `~/.atelier/instance.yaml` — **your**
profile, in your home directory, never in a repo, never committed (the same
boundary that keeps personal context out of every repo it does not belong in).

- **If it exists**, read it. Its keys drive every stamp below. The schema —
  every key, its shape, its default, and the why per key — is
  `instance.yaml.example` **beside this skill**: one source; this skill
  deliberately does not restate it.
- **If it is absent**, this is first run. **Fill it interactively**: walk the
  keys of `instance.yaml.example`, ask the principal for each (offer the
  example's defaults — `workspace_root` from where they keep code;
  `visibility: private`; `signing: false` until their machine is set up to
  sign), write `~/.atelier/instance.yaml`, and continue. Do not invent values;
  a profile that guesses identity is the exact failure this externalisation
  prevents. `exemplars` and `atelier_path` are optional — skip them if the
  principal has neither.

Refer to profile keys by name below (e.g. "stamp `git_identity`"); never
hard-code an identity into this skill.

## Process — a new repo

Follow REPO-STANDARD's "new repo" process; the mechanics that are *this skill's*
job (`WS` = `workspace_root` from the profile):

```sh
cd "$WS" && mkdir <name> && cd <name>
git init -q && git branch -M main
git config user.name  "<git_identity.name>"
git config user.email "<git_identity.email>"
# Signing posture comes from the profile's `signing` key — never hard-baked
# here. Signing is a machine property (global gpg.format=ssh + user.signingkey
# + allowed_signers; SIGNING.md, ADR 0007), so a bake on an unconfigured
# machine fails the very first commit. Only when the profile says the machine
# signs, stamp the repo-local intent — belt-and-braces so the repo signs even
# where global config drifted (atelier-style profiles keep signing on):
[ "<signing>" = "true" ] && git config commit.gpgsign true
```

1. **Boundary check first** (REPO-BOUNDARY) — if this isn't its own repo, say so
   before creating one.
2. **Size to the type** (REPO-STANDARD's table) — decide static / package / infra
   / docs, then seed only the matching set.
3. **Seed from `$SRC/docs/build/templates/`**, renaming as you copy:
   `gitignore`→`.gitignore`, `claude/`→`.claude/`,
   `workflows/ci-<type>.yml`→`.github/workflows/ci.yml`, and (for any repo
   inheriting house doctrine) `workflows/floor.yml`→`.github/workflows/floor.yml`
   — the scanner floor that runs atelier's public tools in CI (step 6). Put the
   product in its subfolder (`site/`, `src/`, …). Do **not** commit **either**
   `.claude/` settings file — copy both in for the ergonomics, both stay
   gitignored: `settings.local.json` because it is one person's preferences,
   and `settings.json` because an allowlist of what runs *unprompted* is
   reconnaissance once published (Mike ruled 2026-07-29; the template gitignore
   already covers both, so this is a check that the seeded ignore file was not
   trimmed).
4. **Fill placeholders with grounded content** — never leave a lorem-ipsum
   ARCHITECTURE. Can't ground a doc yet? Stub with a visible `<!-- TODO -->` and
   say so (the apex applied to repo docs). LICENSE seeds from the templates
   (Apache-2.0, verbatim); fill its appendix line and the NOTICE copyright line
   with the year + `copyright_holder`. Apply `locale` spelling throughout.
   **The board is the store form, not a file you type items into.** The template
   ships `docs/roadmap/` (a `README.md` carrying the legend, one starter section
   folder with its own `README.md`, one starter item file) and a generated
   `docs/ROADMAP.md`. Replace the starter item and section title with the repo's
   real first work (or stub-and-flag), then **regenerate the index — never
   hand-edit it**: `python3 "$SRC/tools/board.py" --rebuild` (in a child the
   rebuild command it writes is the portable `ATELIER_TOOLS` form, never your
   absolute path), and run `python3 "$SRC/tools/board.py" --check` to confirm.
   The index is not a template to fill: a hand-typed one fails the floor's
   `board` check. No `ROADMAP-DONE.md` is seeded; a done item stays in its own
   file as `[x]`.
5. **Stamp the doctrine block** in `CLAUDE.md` (the keystone — every repo that
   inherits house doctrine gets it). Fill the four placeholders:
   - `<atelier-path>` → the **sibling-relative** path to the doctrine source
     (`../atelier` when repos live beside an atelier checkout). Never stamp an
     absolute: sibling-relative survives the workspace moving and keeps the
     drift-check command the block hands every future session valid.
   - `<SHA>` → `git -C "$SRC" rev-parse --short HEAD` (live mode).
   - **Bundled mode stamps the canonical variant, verbatim.** With no sibling
     checkout, the block's canonical text is `$SRC/docs/method/PROPAGATION.md`
     § *The bundled-mode variant*: the same block with the heading line and the
     **Source & drift** bullet substituted exactly as written there — never
     improvised (the pin's referent becomes the plugin version; ADR 0002 fork,
     named in the design ADR). Its placeholders are `<plugin-path>` (the
     plugin's install directory — `$SRC`, absolute) and `<VERSION>` (the
     `version` in `$SRC/.claude-plugin/plugin.json`).
   - `<visibility check>` → the check that answers it in this repo:
     `` `gh repo view <remote.account>/<name> --json visibility` `` once a
     GitHub remote exists; with no remote, `` `git remote` prints nothing ``
     (PROPAGATION.md § *The standard child doctrine block*).
   - `<visibility fact>` → e.g. "PRIVATE (a push is not publication; making it
     public is a floor action)". The block's canonical text is atelier's
     PROPAGATION.md — the template carries a stamped copy; don't paraphrase it.
   - **Keep the two marker lines around the block** (`stamp:begin
     source=docs/method/PROPAGATION.md region=floor` and `stamp:end`, HTML
     comments, so invisible when rendered). They are load-bearing scaffold
     content, not template furniture: they are how the floor's `stampscan`
     finds this copy and checks it against the floor at this repo's pin, with
     the placeholder fills above put back. Strip them and the copy is never
     checked; leave the `source=` path as written, since it names atelier's
     file, read at the pin, not one in this repo.
   Also fill `<atelier-path>` in **every other stamped file that carries it**
   (same value): CONTRIBUTING's once-per-clone hook lines and
   `docs/reviews/README.md`'s pointer lines today — but grep for the placeholder
   rather than trusting this list to stay complete. Then **prove the stamp
   mechanically** — prose executed by a model drifts, so verify like an
   instrument, over the **whole tree**, never a named-file list (a grep scoped to
   two files once reported the stamp proven while a third file still carried its
   placeholders — cold-review finding F1, 2026-07-19):

   Delete the templates' guidance comments first — the grep treats a surviving
   comment (which names the placeholders) as an unfilled placeholder, by
   design.

   ```sh
   grep -rn --exclude-dir=.git \
       '<atelier-path>\|<SHA>\|<visibility check>\|<visibility fact>\|<plugin-path>\|<VERSION>' . \
                                        # expect: no hits ANYWHERE (all filled)
   # then run the block's own drift check VERBATIM —
   # live mode; expect empty (a failed step is no result, not no drift).
   # Step 6 bakes this tools path into git config; until then, the env var:
   export ATELIER_TOOLS="$(cd "$SRC/tools" && pwd)"
   A="${ATELIER_TOOLS:-$(git config hooks.atelierTools)}/..";
   git -C "$A" fetch -q && git -C "$A" log --oneline <stamped-SHA>..origin/main
   # live mode, the copy itself; expect exit 0 and `[identical]` (it reads the
   # floor at the stamped pin, so a dropped marker or a reworded line shows here):
   python3 "$ATELIER_TOOLS/stampscan.py" --require-floor-stamp --root . CLAUDE.md
   # bundled mode; expect exactly the stamped <VERSION>:
   grep '"version"' "$SRC/.claude-plugin/plugin.json"
   ```
6. **Wire the safety scans** as a pre-commit hook (the repo will hold real
   content). The scanners live in the source — one source; **do not copy them into
   the child**. Install the hook and **bake the tools path** so the child resolves
   them; the hook **fails closed** (blocks the commit) if it ever can't scan, so a
   scaffolded repo can never commit unscanned:

   ```sh
   # TRACKED hooks dir, not .git/hooks — the hook FILE then travels with the
   # clone and stays current (ADR 0008). .git/hooks/ is untracked, so a hook
   # installed there exists on exactly one machine: on 2026-07-25 every guard in
   # every child in this estate was machine-local, and a fresh clone would have
   # started with none.
   mkdir -p .githooks
   cp "$SRC/.githooks/pre-commit" .githooks/pre-commit
   cp "$SRC/.githooks/pre-merge-commit" .githooks/pre-merge-commit  # a clean `git merge` skips pre-commit
   cp "$SRC/.githooks/commit-msg" .githooks/commit-msg  # git runs pre-commit before the message exists
   chmod +x .githooks/pre-commit .githooks/pre-merge-commit .githooks/commit-msg
   git config core.hooksPath .githooks
   # Absolutise: a relative path here only resolves from the main checkout, so
   # the fail-closed hook would block every WORKTREE commit (fleet-wide bug,
   # 2026-07-19 — ten children were born with a relative `../atelier/tools`).
   git config hooks.atelierTools "$(cd "$SRC/tools" && pwd)"
   ```

   The hook **names no scanner** — it is a shim over the source's `tools/floor.py`
   registry, the same list the CI floor reads (ADR 0008). Never add a scanner
   line here; add it to the registry, where every repo gets it.

   `core.hooksPath` still has to be set **once per clone** — git transports
   config, no. So the tracked directory fixes staleness, not installation: the
   scaffolded CONTRIBUTING + CLAUDE.md carry the once-per-clone instructions
   (step 5 fills their `<atelier-path>`) — don't strip them, and
   `floorfleet` is what catches a clone where nobody ran it. The hook is the
   repo's **local** gate; `.github/workflows/floor.yml` (seeded in step 3) is the
   **CI backstop** — a ~30-line caller of the source's reusable floor workflow,
   so a check added upstream reaches this repo with no edit here, ever.

   **Prove the hook once**: stage a fake secret and confirm the commit is
   blocked — a hook that scans nothing is the exact failure this step exists to
   prevent, and it has happened here for real (2026-07-10).

   If this repo needs to run a check **advisory** while it re-baselines, or needs
   a check **scoped**/**tuned** to its subject matter, declare that in
   `.atelier-floor.json` at the repo root — never by dropping a scanner. A
   declaration is visible estate-wide via `floorfleet`; a missing line is not.
7. **Write the first session file**, `docs/sessions/<date>-<HHMM>-<slug>.md`
   (the start time in UTC, from `date -u`; the template's
   `docs/sessions/README.md` explains the folder), commit, then create the remote and
   push. The authority for creating a *new* remote repo is **the principal's ask
   itself** (they invoked `/atelier:repo create`; a repo on their own account is what they
   asked for) — not "push is recoverable", which justifies only the push. If the
   ask didn't clearly include a remote (e.g. standardise-existing, or a local
   experiment), **confirm before creating it**; and *publishing* — public or any
   audience-widening — is always a floor action, never on your own initiative.

```sh
git add -A && git commit -m "chore: scaffold to the house standard"
<remote.host> repo create "<remote.account>/<name>" --<remote.visibility> \
    --source=. --remote=origin --push
<remote.host> repo edit "<remote.account>/<name>" --delete-branch-on-merge
```

The `--delete-branch-on-merge` edit is part of the standard, not an option:
CONCURRENCY's "every branch ends put away" makes the landed half automatic so a
new repo never regrows the merged-branch-lingers class.

## Process — standardise an existing repo

Follow REPO-STANDARD's "standardise" process. In short: **audit** against the file
set; apply the **safe mechanical** bits uniformly (`.gitignore` hygiene,
`git rm --cached` any committed OS litter **or either `.claude/settings*.json`**
— a repo standardised before 2026-07-29 will still be tracking the allowlist);
for **content docs** write only what you can
ground, else stub-and-flag — don't churn blindly. If the repo inherits house
doctrine and lacks the block, **stamp it** (step 5 above) at the current source
SHA/version. Commit; offer the push if the principal operates it as a remote.

**The board and the session log are record stores, not content docs.** If the
repo has no `docs/roadmap/`, seed the store form from the templates (as in step
4) rather than a one-file `ROADMAP.md`. If it has a **one-file board** (a
monolithic `ROADMAP.md` of entries), do not rewrite it or re-type its items:
point at the store conversion, which is healthy item 6 of `skills/fleet/sweep.md`.
A frozen `ROADMAP-DONE.md` is cut into its store by `tools/archivecut.py`, and
a one-file session log (`SESSIONS.md`, with any `SESSIONS-ARCHIVE.md`) is
retired into `docs/sessions/` by the same tool's `--cut` (`010/270`); never by
hand. Never overwrite an existing board's item files with the
template's starter ones.

**Don't touch a third-party repo** — check the remote's owner first (a repo whose
owner is not in your profile's `remote.account` is not yours to standardise).
