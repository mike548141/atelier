# REPO-STANDARD — the shape every project repo takes

The repo-craft standard: the one shape a software project repo takes, and why.
`method/` is estate-wide and mostly non-code; this is specifically about
**software project repos** — what files exist, where the product lives, what CI
is honest, and how a repo is born or brought up to standard.

This layer owns **repo shape**. It does *not* re-state the cross-cutting
doctrine — where `method/` already owns a rule, this points up rather than
copying it (a second copy drifts). The pointers are load-bearing, not
decoration: read them when they fire.

## The default that binds: product in a subfolder

Where a repo has a **deployable/product artifact**, it lives in a subfolder
(`site/`, `src/`, `pkg/`, …), never mixed with repo scaffolding at the root. The
root holds only meta: README, `docs/`, licence, CI, tools. This keeps *what
ships* cleanly separable from *how the repo is run* — you can point a build, a
publish step, or a reviewer at the product folder without dragging the
scaffolding, and the scaffolding can grow without polluting the artifact.
(Learned the hard way; the static-site exemplar arrived at `site/`
independently.)

It is a strong default, not an invariant — the sizing table below carries the
two honest exceptions (an infra repo *is* its config tree; a docs repo's content
may live at root). Departing anywhere else needs a stated reason, per
`method/PRINCIPLES.md`'s stated-exception rule.

## Size the standard to the repo type

**Not every element fits every repo.** Decide the type first, then apply the
matching set. Ask only if genuinely ambiguous — the type is usually obvious from
what the repo is for.

| Type | Product goes in | Honest CI | Type-specific extras |
|---|---|---|---|
| Static / web site | `site/` | stdlib link-check | NOTICE if it bundles third-party code |
| Package / library / CLI | `src/` or `pkg/` | lint + type-check + test matrix | man page if it exposes a CLI |
| Infra / config | the config tree as-is | lint the config if a linter exists; **if none does, a stated no-gate note, never a silent absence** | secrets policy if it holds any |
| Docs / reference | content at root or `content/` | link-check (optional) | — |

Sizing is a judgement, not a menu: a five-file static site does not need an ADR
directory on day one, and an infra repo's "CI" may honestly be a config linter
and nothing more — but "nothing at all" is only honest when it is *written
down* (the honest-CI rule below: an uncovered gap is documented, not silent).
Apply what earns its place; stub the rest with a note (below).

## The standard file set

Seed from `build/templates/` (they live alongside this standard, one source the
skill and the published methodology share), then
**fill every placeholder with real, grounded content**. A lorem-ipsum ARCHITECTURE is worse than no ARCHITECTURE — it reads as
truth and isn't. If you cannot ground a doc yet (you don't understand the
project), write the stub with a visible `<!-- TODO -->` and *say so*, rather than
inventing. This is the apex applied to repo docs: a claim no stronger than its
evidence — see `method/EVIDENCE.md`.

**Root:**

- **README.md** — public-facing: what it is, *why*, a structure table, run/setup,
  develop, licence.
- **CLAUDE.md** — the AI session onramp. Session-start read order
  (ARCHITECTURE → ROADMAP → tail of SESSIONS), hard constraints, layout, the dev
  loop. For any repo that inherits house doctrine this also carries the standard
  doctrine block (inlined safety floor + SHA-pinned pointer + drift check) — its
  canonical text and wiring live in `method/PROPAGATION.md`, not here.
- **CONTRIBUTING.md** — dev setup, what makes a good change, and the two record
  disciplines (comments say *why*; log the session; ADR the re-litigable
  decisions) — those disciplines are `method/RECORD.md`; CONTRIBUTING points a
  human contributor at them in repo-local terms.
- **CHANGELOG.md** — Keep-a-Changelog shape, newest first; everything under
  _Unreleased_ until there is a reason to tag. The SHA is the version
  (`decisions/` records why); the CHANGELOG is the human-readable index.
- **LICENSE** — one permissive default, chosen per repo. The house default is
  Apache-2.0 (`decisions/0004`). Set the copyright line to the right holder.
- **NOTICE** — only if the repo bundles third-party code; list each component and
  its licence.
- **.gitignore** — always ignores OS litter and the *personal* Claude settings
  (`.claude/settings.local.json`); add language litter per type
  (`__pycache__/`, `node_modules/`, `.venv/`).
- **.claude/settings.json** — the **committed** permission allowlist, so routine
  commands (test/build/lint) don't prompt on every run. The personal
  `.claude/settings.local.json` (e.g. an accept-edits default) stays **gitignored**
  — it is one person's ergonomics, not the repo's policy.
- **.github/workflows/ci.yml** — a *real* correctness gate sized to the repo.
  **Honest CI** is the rule: it must actually gate correctness, and where it
  *cannot* cover something (does the page look right? does the radio associate?),
  say so in a comment and leave that as a documented human step. A green check
  that proves nothing is a phantom-success — the exact failure mode `method/`
  names an instrument must never have.

**docs/** (present to the degree the type earns — see sizing):

- **ARCHITECTURE.md** — compact current-truth: the stack and *why* it's that way.
  It compresses away the deliberation; the ADRs keep it.
- **ROADMAP.md** — lean, read every session; spill completed detail to
  `ROADMAP-DONE.md` once it grows.
- **SESSIONS.md** — the append-only session index (detail-on-demand in
  `sessions/`). Tail-read at session start; append before finishing. This is
  `method/RECORD.md`'s mechanism — the repo just hosts it.
- **MODEL-ECONOMICS.md** — the repo's model/token policy. General shape (which
  model builds, which reviews, session hygiene) is `method/MODEL-ECONOMICS.md`;
  the repo file carries only what's repo-local, or points up entirely.
- **decisions/** — numbered ADRs `NNNN-slug.md`. Write one when a decision
  **rejected a plausible alternative** or **rests on hard-won evidence**; skip it
  for reversible choices (a code comment covers those). The when-to-ADR rule is
  `method/RECORD.md`.
- **reviews/** — peer-review briefs: scope + the load-bearing assumptions to
  challenge + the real-world check. The brief-on-top / verdict-below lifecycle
  and the independent-reviewer principle are `method/REVIEW.md`.

## Repo-craft conventions

- **Comments say _why_, not _what_** — platform quirks, non-obvious constraints,
  the reason a thing is the way it is. Restating the code in prose is noise.
  (The general form is `method/RECORD.md`; it lands here as a code-review bar.)
- **No personal / instance data in a shareable-bound repo.** Names, health,
  family, finance, estate topology, machine-local paths — none of it belongs in a
  repo that may widen its audience. This is enforced mechanically, not
  remembered: run the leak/secret scans (`method/`'s safety tooling) as hooks.
- **Grounded, not invented** — see the file-set note; it applies to every doc,
  every commit message, every ROADMAP claim.
- **Private-first** — new repos default private; widening audience is a floor
  action (`method/AUTONOMY.md`, `decisions/0003`).
- **Don't standardise a third-party repo.** Check the remote's owner before
  touching anything; a repo under someone else's org is not yours to reshape.

## Process — a new repo

1. Create the directory and `git init`; set the git identity (instance-local).
2. Seed the file set from `templates/`, sized to the type; put the product in its
   subfolder.
3. Fill placeholders with grounded content; stub-and-flag what you can't ground.
4. Seed the first SESSIONS entry and, if the repo inherits house doctrine, stamp
   the CLAUDE.md doctrine block at the current atelier SHA
   (`method/PROPAGATION.md`).
5. Commit. Create the remote **private** by default; push is recoverable, so it
   needs no confirmation — *publishing* (public, or widening audience) does.

## Process — standardise an existing repo

1. **Audit** against the file set: what's present, what's missing, what's wrong.
2. Apply the **safe mechanical** bits uniformly — committed
   `.claude/settings.json`, `.gitignore` hygiene, remove any committed OS litter
   or personal settings (`git rm --cached`). These are low-risk and uniform.
3. For **content docs** (ARCHITECTURE / ROADMAP / ADRs): write only what you can
   ground in the actual project. Otherwise stub-and-flag. **Don't churn blindly**
   — a plausible-but-wrong doc is a regression, not progress.
4. Commit (recoverable — proceed); offer the push if the repo is operated as a
   remote.

## What lives elsewhere (the instance/delivery split)

This standard is the readable, forkable **source**. The concrete machinery is
two hops away, on purpose:

- **Delivery vehicle** — the `create-repo` skill applies this standard as a
  guided action. It carries the instance-local specifics a shareable doc must not
  (exemplar repo names, git identity, the `gh` account, the workspace path,
  house-convention locale, the default copyright holder). It *inherits from this
  doctrine* rather than re-encoding it, and it **stamps the standard doctrine
  block + SHA pin** (`method/PROPAGATION.md`) into every new repo's CLAUDE.md —
  so no delivery path leaves a repo born wisdom-empty.
- **Templates** — the seed files, in `build/templates/`, alongside this standard:
  the skill and the published methodology share one source. The skill seeds from
  here (renaming `gitignore`→`.gitignore`, `claude/`→`.claude/`,
  `workflows/`→`.github/workflows/`) and fills the placeholders. The CLAUDE.md
  template carries a *stamped copy* of the doctrine block whose canonical text is
  `method/PROPAGATION.md` — a pin bump reviews that wording.
