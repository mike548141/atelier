---
name: create-repo
description: Scaffold a new repo (or standardise an existing one) to your house conventions — the atelier repo standard, stamped with your identity from an instance profile. Use when asked to create a repo, start a project, or standardise/tidy an existing repo. Sizes the standard to the repo type; never fabricates docs it can't ground.
---

# create-repo — deliver the house repo standard

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
boundary that keeps personal context out of a shareable repo).

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
   product in its subfolder (`site/`, `src/`, …). Do **not** commit
   `.claude/settings.local.json` (copy it in, but it stays gitignored — one
   person's ergonomics).
4. **Fill placeholders with grounded content** — never leave a lorem-ipsum
   ARCHITECTURE. Can't ground a doc yet? Stub with a visible `<!-- TODO -->` and
   say so (the apex applied to repo docs). LICENSE seeds from the templates
   (Apache-2.0, verbatim); fill its appendix line and the NOTICE copyright line
   with the year + `copyright_holder`. Apply `locale` spelling throughout.
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
   - `<owner/repo>` → `<remote.account>/<name>` (once the remote exists).
   - `<visibility fact>` → e.g. "PRIVATE (a push is not publication; making it
     public is a floor action)". The block's canonical text is atelier's
     PROPAGATION.md — the template carries a stamped copy; don't paraphrase it.
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
       '<atelier-path>\|<SHA>\|<owner/repo>\|<visibility fact>\|<plugin-path>\|<VERSION>' . \
                                        # expect: no hits ANYWHERE (all filled)
   # then run the block's own drift check VERBATIM —
   # live mode; expect empty:
   git -C "$SRC" log --oneline <stamped-SHA>..HEAD
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
   chmod +x .githooks/pre-commit
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
7. **Seed the first `docs/SESSIONS.md` entry**, commit, then create the remote and
   push. The authority for creating a *new* remote repo is **the principal's ask
   itself** (they invoked create-repo; a repo on their own account is what they
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
set; apply the **safe mechanical** bits uniformly (committed
`.claude/settings.json`, `.gitignore` hygiene, `git rm --cached` any committed OS
litter or `settings.local.json`); for **content docs** write only what you can
ground, else stub-and-flag — don't churn blindly. If the repo inherits house
doctrine and lacks the block, **stamp it** (step 5 above) at the current source
SHA/version. Commit; offer the push if the principal operates it as a remote.

**Don't touch a third-party repo** — check the remote's owner first (a repo whose
owner is not in your profile's `remote.account` is not yours to standardise).
