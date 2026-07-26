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

Where a repo has a **deployable/product artefact**, it lives in a subfolder
(`site/`, `src/`, `pkg/`, …), never mixed with repo scaffolding at the root. The
root holds only meta: README, `docs/`, licence, CI, tools. This keeps *what
ships* cleanly separable from *how the repo is run* — you can point a build, a
publish step, or a reviewer at the product folder without dragging the
scaffolding, and the scaffolding can grow without polluting the artefact.
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

Seed from `build/templates/` (they live alongside this standard, one source
the skill and the published methodology share), then **fill every
placeholder with real, grounded content**. A lorem-ipsum ARCHITECTURE is
worse than no ARCHITECTURE — it reads as truth and isn't. If you cannot
ground a doc yet (you don't understand the project), write the stub with a
visible `<!-- TODO -->` and *say so*, rather than inventing. This is the apex
applied to repo docs: a claim no stronger than its evidence — see
`method/EVIDENCE.md`.

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
- **SECURITY.md** — a private-disclosure policy, seeded **only once the repo is
  public or about to be** — a private repo has no external reporter, so like
  LICENSE and the licenscan gate this is a publish-time artefact, not a birth
  file. Scope it to what the repo *ships*; state the response expectation
  honestly (a solo-maintained repo says best-effort, no guaranteed timeline) and
  claim no bug bounty that does not exist — the apex forbids a claim stronger
  than its evidence. It points reporters at GitHub Private Vulnerability
  Reporting — and **enabling PVR in the repo's settings is part of the same
  seeding act, verified with
  `gh api repos/<owner>/<repo>/private-vulnerability-reporting` →
  `enabled: true`** (a policy
  that routes through a disabled switch is a broken control — SC1,
  2026-07-23); the finding severity + recurrence-prevention practice it names
  is `method/REVIEW.md`'s security lens. Seed from `templates/SECURITY.md`; atelier's
  own root `SECURITY.md` is the worked example. (Grounded: the 2026-07-22
  security-canon gap map.)
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
- **.github/workflows/floor.yml** — the *scanner* floor, for any repo that
  inherits house doctrine: the CI backstop to the pre-commit scan hook (which
  only guards the clone it's installed in). It checks atelier out beside the repo
  and runs its public `tools/` scanners — the current roster and what each
  gates is `tools/README.md`'s to state, not re-enumerated here (an inline
  list went stale three scanners running) —
  against the tree on every push + PR — one source, no vendored copy, no drift.
  Distinct from `ci.yml` (which gates *correctness*); this gates *publish-safety*.
  licenscan is a publish gate, left commented until the repo settles a licence.
- **.atelier-floor.json** — what the repo decides about that floor, and the only
  place it decides it: where its records live, the licence it asserts, which
  checks run advisory or disabled (with a reason), and — under `local` — checks
  the repo **adds** for itself. The layering mirrors doctrine exactly
  (`method/PROPAGATION.md`): a shared floor, a local append, and the child may
  narrow but never contradict. So a rule that is genuinely this repo's — a
  tripwire whose blocklist could never live in a shared repo, say — gets a home
  that keeps the repo *inside* propagation, instead of the bespoke hook that
  takes it out. A local check may not take a fleet check's name, and one whose
  script is missing blocks rather than passing quietly. The test of where a rule
  belongs is not how specific it feels: if another repo would want it, it goes
  upstream to atelier's registry, where every repo gets it.

**docs/** (present to the degree the type earns — see sizing):

- **ARCHITECTURE.md** — compact current-truth: the stack and *why* it's that way.
  It compresses away the deliberation; the ADRs keep it.
- **ROADMAP.md** — lean, read every session; spill completed detail to
  `ROADMAP-DONE.md` once it grows.
- **SESSIONS.md** — the append-only session index (detail-on-demand in
  `sessions/`). Tail-read at session start; append before finishing. This is
  `method/RECORD.md`'s mechanism — the repo just hosts it.
- **ECONOMICS.md** — the repo's model/token policy. General shape (which
  model builds, which reviews, session hygiene) is `method/ECONOMICS.md`;
  the repo file carries only what's repo-local, or points up entirely.
- **decisions/** — ADRs named `<YYYY-MM-DD>-<HHMM>-<slug>.md` (`HHMM` in UTC —
  `date -u`, ADR 2026-07-15; coordination-free, per `method/CONCURRENCY.md`;
  files named under retired schemes keep their names). Write one when a decision
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
- **An installed CLI ships both `--help` and a man page — different jobs, not
  two copies of one.** Scope: a tool the repo **installs onto an operator's
  machine** (published to `PATH`, used away from the repo) documents itself in
  two registers; a repo-internal script that runs in place — hooks, CI steps,
  checks invoked from the repo root — owes a good `--help` only. This is the
  sizing table's man-page row given its boundary, and it is why atelier's own
  `tools/` scanners carry no pages: they run in place, in this repo and in
  children's hooks, never installed onto a machine.
  - **`--help` — the digest.** Concise and scannable, fits a screen: a one-line
    synopsis, the options as a flat list, and at most a closing line or two
    saying what the tool does and where the manual is (`… full manual:
    man <tool>`). It serves the user who already knows the tool and wants a
    reminder — it is *not* where rationale or worked examples belong.
  - **`man <tool>(1)` — the full reference.** Plain language: what the tool is and
    *why*, every option explained, and the sections a digest can't carry —
    `FILES`, `EXAMPLES`, `EXIT STATUS`, `NOTES`, `SEE ALSO`. It serves the user
    learning the tool or needing depth.

  The man page is the superset; `--help` is its digest. The one thing both must
  carry is the options list, so that duplication is where drift lives: keep
  prose detail in **one** place (the page), and where the repo has tests, pin
  the superset relation mechanically — assert every flag `--help` prints
  appears in the page (atelier's `instruments/` tests do). Ship pages as roff
  under a `man/` dir and have the installer publish them to
  `~/.local/share/man/man1` — auto-found on macOS/BSD `man` and man-db Linux,
  which derive the manpath from `PATH`; a hard-set `MANPATH` environment
  variable overrides that derivation, the one common gotcha. Worked example:
  atelier's `instruments/` (`man/ccarchive.1` + a one-screen `--help`).

## Process — a new repo

1. Create the directory and `git init`; set the git identity (instance-local)
   and, **when the instance profile's `signing` fact says the machine signs**
   (default off), bake repo-local `commit.gpgsign=true` — belt-and-braces so a
   signing machine's repo signs even
   where global config drifted; signing itself is a machine property (SIGNING.md).
2. Seed the file set from `templates/`, sized to the type; put the product in its
   subfolder.
3. Fill placeholders with grounded content; stub-and-flag what you can't ground.
4. Seed the first SESSIONS entry and, if the repo inherits house doctrine, stamp
   the CLAUDE.md doctrine block at the current atelier SHA
   (`method/PROPAGATION.md`).
5. Commit. Create the remote **private** by default; push is recoverable, so it
   needs no confirmation — *publishing* (public, or widening audience) does.
6. Set **delete-branch-on-merge** on the new remote (`gh repo edit
   --delete-branch-on-merge`) — the landed half of CONCURRENCY's "every branch
   ends put away", made automatic at birth so merged branches never linger.

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
