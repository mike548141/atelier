# tools/ — atelier's mechanical controls

Doctrine informs; a *check* enforces. These are the checks. Zero third-party
dependencies — run them with the system `python3`.

## What these scans cannot see (read this before trusting a clean run)

A clean scan means **"no known shape matched"**, not "safe to publish". Per
EVIDENCE §14, an instrument states what it dropped — this is the triad's
standing residual, the classes each scan *structurally* cannot catch:

- **All three** scan line-by-line and text-only: anything **split across
  lines** (a concatenated secret, a PEM body pasted without its header, a
  folded YAML scalar) and anything inside a **binary container** (docx, PDF,
  sqlite, images — skipped silently on the first NUL byte) is invisible.
- **leakscan** matches literal terms and NZ-tuned structural shapes: a
  **paraphrased** personal fact ("the dog", "the house we bought last year"),
  a term not on the machine-local list, or a non-NZ address/phone shape sails
  through. The term list is only as good as its curation.
- **secretscan** no longer trades single-case hex away entirely — since E6b
  (2026-08-06) a **hex-encoded token outside a secret-named assignment** is
  REPORTED as an advisory finding rather than passing in silence. It still does
  not *block* on one, so the residual is now about response rather than
  blindness. Still uncaught in either tier: a novel vendor format that is
  neither assignment-anchored nor high-entropy-mixed-class, a literal secret
  that *begins* like an indirection (`$uperS3cret…` reads as `$VAR`), and a
  context-free credential shorter than 32 characters.
- **licenscan** sees SPDX-tagged headers and metadata declarations only: a
  vendored file carrying the **traditional prose licence header** with no
  `SPDX-License-Identifier` tag — the commonest real-world copyleft shape — is
  invisible. Dual-licence (`A OR B`) and `LicenseRef-` ids degrade to an
  *unknown-declaration* warn (friction, never a silent pass). A legitimately
  bundled copyleft component (the NOTICE case) **will block**; the
  allow-marker/ignore hatch, reason recorded, is the sanctioned way to say
  "bundled, not relicensed".

**linkscan** (a doc-integrity check, not a leak scan) is line-based too: it reads
inline `[text](path)` links and Markdown (ATX `#` + setext underline) headings
only. **Reference-style links** (`[text][ref]` + a `[ref]: …` definition), links
inside raw **HTML**, and a link whose `](…)` **spans two lines** are invisible to
it — as is any anchor slug where atelier's simplified slugger diverges from
GitHub's full CommonMark render (an exotic heading). Anchors minted by raw HTML
(`<a id=…>`, `<h2>`) aren't seen either, so a valid link into one **false
positives** (one `linkscan:allow` fixes it); the same goes for a link-shaped
example inside an **indented (4-space) code block**, which linkscan reads as
live text (GitHub renders it as code — fixing that would risk missing real
links in indented list items, the worse trade). It never touches the network,
so it says nothing about whether an external URL is alive.

Where the replacement path is **computable**, linkscan prints it (`↳ did you
mean: ../../tools/x.py`). Two cases qualify, both requiring a *unique* answer:
the path resolves from the **repository root** — the commonest break by far, a
root-relative path written inside a file two levels down — or exactly **one**
file in the tree carries that basename, the moved-or-renamed case. Two
candidates means guessing which, so it stays silent; a confident wrong
suggestion costs more than none. Suggestions are **advisory text only**: they
never change a verdict or an exit code, and nothing is rewritten for you.

**sizescan** (a hygiene check, not a safety scan) gates on **relocatable cold
content** — a completed `[x]` item on a checkbox-worklog file, whose fix is a
lossless move to the history store — and treats **length** as a pure advisory.
Cost is size × read-frequency, so the enemy is cold content sitting on the hot
path, never fulsomeness: a roadmap that is long purely from a genuine list of
*open* items is never failed, only reported. The gate says "this done item is
pure cost with a lossless fix, harvest it"; the advisory says "this file is long,
look at it" and never breaks a build. The judgement of whether a long all-open
file is fine or hiding resolved narrative stays human.

**board** (a records-hygiene check, board-store ADR 2026-08-15) guards the one
derived file the split board keeps: `ROADMAP.md` is generated from the per-item
files under `docs/roadmap/`, and a commit whose index is stale against them
fails with the remedy printed (`board.py rebuild`; after a merge conflict on
the index, rebuilding *is* the resolution). Done items render `✅` in the index
— never `[x]`, so sizescan's cold-content gate cannot fire on a generated line.
A repo with no `docs/roadmap/` directory is out of scope and passes saying so.
Stated residual: the check compares worktree to worktree — the staged-plane
seam (harvestscan's HV4 discipline) is a queued follow-up on the board.

**reviewscan** (a records-hygiene check) proves only **presence**: a decision
record carries *a* review line. Whether "not warranted" was the honest call —
or a queued pointer was ever taken — is exactly the judgement a validator
can't make; the review practice owns it. Roadmap sections aren't scanned at
all (deliberate — see the tool's docstring), so a design entry there rests on
convention alone.

**publishscan** judges the **path, never the contents** — the one scanner here
that does. It cannot tell you a tracked `.env` is empty or a tracked allowlist
is harmless; it says the file should not be in the repo at all. It is a
denylist, so it knows only the shapes it was taught, and it deliberately
*allows* the guard declarations (`.atelier-floor.json`, the `.<scanner>ignore`
files) that also map where the defences are weak — they must travel for the
floor to run, so that exposure is accepted and mitigated by requiring a stated
reason for every exemption, not by hiding the files.

The scans are the mechanical floor, not the whole boundary: the human
pre-publish scrub (and the review practice) owns the residual above.

## Supply chain — zero-dep *is* the control, and its residual

These tools take **zero third-party dependencies** (stdlib Python, and Node's
built-in `node:test` for `instruments/`), and that is a deliberate
**supply-chain control**, not merely a convenience: a dependency you do not have
is a dependency that cannot ship a vulnerability into the build
(`method/PRINCIPLES.md` §8, *design out the work* — depending on nothing designs
out the whole class of dependency-vulnerability screening). It is the reason this
repo runs no SCA scanner, no Dependabot, no lockfile audit: there is almost
nothing to screen. **"Almost"** is the honest word — the control shrinks the
surface to near-zero, it does not zero it, and the residual is named here rather
than pretended away:

- **CI actions are SHA-pinned, not tag-pinned.** The floor and CI workflows
  consume a few third-party GitHub Actions (`actions/checkout`,
  `actions/setup-python`, `actions/setup-node`). A version *tag* (`@v5`) is
  mutable — its owner can repoint it at new code — so every such action is pinned
  to a **full commit SHA** with the tag kept as a trailing comment
  (`@<sha> # v5`), in `.github/workflows/ci.yml` and in the child
  `docs/build/templates/workflows/` a child copies. A pin is bumped
  deliberately, re-resolving the SHA (`gh api repos/<owner>/<repo>/git/ref/tags/<tag>`
  — checking `.object.type` first: an **annotated** tag returns a *tag object*,
  not a commit, so dereference it
  (`gh api repos/<owner>/<repo>/git/tags/<sha> --jq .object.sha`, or
  `git ls-remote --tags <url> '<tag>^{}'`) before pinning;
  a moved tag can no longer ship code into a trusted build silently. (Grounded:
  the 2026-07-22 security-canon gap map; SC3, 2026-07-23.)
- **The toolchain is a trusted, unpinned dependency — stated, not hidden.** The
  scanners still trust the runner's `python3`, `node`, `git`, and `gh`, the OS,
  and the runner image itself. These are dependencies even though no manifest
  lists them; the floor pins the *actions* but not the interpreter builds
  (`setup-python`/`setup-node` request a version line, not a SHA of the
  toolchain). That is an accepted residual for a zero-dep doctrine repo, named
  here so it is a known limit rather than an invisible one.
- **No SBOM / artefact signing yet — deferred with a stated trigger.** There is
  no software bill of materials at rest and no release-artefact signing; both are
  deferred to the first published *artefact* (`method/SIGNING.md`, layer 2 — the
  trigger is a package or binary someone else installs). Until an artefact
  exists there is nothing to bill or sign, and standing the machinery up would be
  ceremony.
- **Scanner distribution to children is decided — fetch at CI.** A child's CI
  floor checks atelier out beside the repo and runs these scanners from that
  checkout (`docs/build/templates/workflows/floor.yml` — one source, no
  vendored copy); the per-clone hook covers the local clone. (SC2 sweep,
  2026-07-23 — the earlier "deferred call" wording predated floor.yml.)
- **Child CI trusts `atelier@main` for scanner code — by design.** The floor
  template fetches the scanners at floating `main` (newest detection is
  safest — rationale in floor.yml's header) while the *trust list* and
  doctrine are read at the child's pinned SHA. Detection floats, trust roots
  pin — the asymmetry is deliberate, named here where the residuals live
  (SC5, 2026-07-23). Stated at strength: the float is also a standing grant —
  a write to atelier's `main` runs code in every child's floor job, bounded
  by the job's `contents: read` permissions and no step secrets; a child
  wanting the opposite trade pins `ref:` exactly as the trust list pins
  (SCA1, 2026-07-23).

## `leakscan.py` — keep personal/estate data out of a shareable repo

The apex + AUTONOMY floor forbid personal, health, family, financial or
estate-topology detail from entering a repo that can go public. `leakscan` is the
machine that enforces that boundary, so a leak fails the commit instead of
reaching the remote.

### Two layers (why the scanner itself leaks nothing)

| Layer | Where it lives | What it catches |
|---|---|---|
| **Structural patterns** | in `leakscan.py` (shareable) | the *shape* of sensitive data — emails, IPv4/IPv6, MACs, private-key headers, AWS keys, JWTs, NZ address/phone shapes, coordinates. Names no real value. **Always runs.** |
| **Literal terms** | `~/.claude/leakscan-terms.txt` (**machine-local, never in a repo**) | the actual names, addresses, medications, device IDs, deal figures of one estate. This list *is* the leak if committed, so it stays outside every repo. |

If no local list is found, the scan runs structural-only and **says so loudly** —
partial cover, never silently weaker. For automation that only reads exit codes,
loud isn't enough: pass **`--require-terms`** on a hook/CI line that *expects*
full cover and the scan fails closed (exit 2) when the list is absent, instead
of reporting a degraded pass a script can't tell from a full one.

### Usage

```sh
python3 tools/leakscan.py                 # scan the whole repo
python3 tools/leakscan.py --staged        # scan only staged additions (the hook)
python3 tools/leakscan.py path/to/file    # scan specific paths
python3 tools/leakscan.py --json          # machine-readable, for CI/composition
python3 tools/leakscan.py --selftest      # prove the engine on this box
```

Exit codes (fail-safe — only a clean scan is zero): `0` clean · `1` findings
(blocks the commit) · `2` usage/config error.

### The local term list

Point the scanner at your literal terms one of three ways (first that exists
wins): `--terms <path>`, `$ATELIER_LEAKSCAN_TERMS`, or the default
`~/.claude/leakscan-terms.txt`. Format — one per line, `#` comments, blank lines
ignored:

```
# literal, matched case-insensitively on whole words
Some Person
23 Example Road                     # leakscan:allow: doc example
# a raw pattern for families of identifiers
regex:ACME-\d{4}
```

See `leakscan-terms.example.txt` for a fuller template. **Never commit your real
list** — it belongs in `~/.claude/`, which travels with you, not with any repo.

### Exempting a false positive

A leak-scanner over-flags on purpose (a false positive costs a comment; a false
negative costs a leak). Two escape hatches, both visible and greppable:

- **Per line** — append `# leakscan:allow: <reason>` (or `<!-- leakscan:allow:
  … -->` in Markdown) to the offending line.
- **Per path** — add a glob to `.leakscanignore` at the repo root. Keep it short;
  every entry is a hole in the boundary.

### Networking repos & scanning a subtree

A networking codebase is *full* of IPs and MACs by nature — scanning it whole
buries the real signal (leaked names, addresses, subnets) under thousands of
legitimate structural hits. Two levers handle this:

- **`--disable ipv4,ipv6,mac-address`** silences the network-shape rules while
  keeping the PII/secret catches (email, address, coordinates, private keys, AWS
  keys) and *all* local-term matching. Unknown rule names are a usage error.
- **Positional paths in `--staged` mode** restrict the scan to a subtree — so a
  mostly-private repo can guard only its shareable part. `leakscan --staged
  tiki/` scans only staged additions under `tiki/`; the private inventory/secrets
  are left alone (they hold real data by design).

Together they give the pattern for a private repo with an open-sourceable
subtree — scan the new lines of that subtree only, minus the network noise:

```sh
leakscan --staged --disable ipv4,ipv6,mac-address tiki/
```

### Wiring it in

- **Pre-commit hook** — copy `tools/pre-commit.sample` to
  `.git/hooks/pre-commit` (`chmod +x`). It runs `secretscan --staged` and
  `leakscan --staged` over the staged diff, plus `linkscan` over the **whole
  tree**, and aborts the commit on any finding. This is the primary control.
  (linkscan is whole-tree, not staged, on purpose: a link breaks when a
  *different* file is renamed or deleted, so the file that goes stale is usually
  not the one in your diff — see `linkscan.py` below.) For a subtree/networking
  repo, edit the hook's leakscan invocation to add the `--disable`/path scoping
  above.
  - **In a repo that doesn't carry the scanners** (any create-repo child — the
    scanners live only here), point the hook up:
    `git config hooks.atelierTools <atelier-path>/tools` (or `ATELIER_TOOLS`
    env, which wins). The hook **fails closed**: if a scanner it's asked to run
    can't be resolved, the commit is *blocked with an explanation*, never
    silently skipped — the pre-fix hook skipped silently and committed a planted
    secret (2026-07-10, the create-repo exercise). Contract pinned by
    `tools/test_precommit.py`.
- **CI** — in a repo that carries the scanners (atelier itself), run both with
  `--json` on every push (belt and braces; a hook only protects the clone that
  has it installed). A child repo runs the same scanners through its **CI
  floor**, which checks atelier out beside the repo and fetches them at CI
  time (`docs/build/templates/workflows/floor.yml`); the per-clone hook still
  guards local commits. (Swept 2026-07-23, SC2 — this note predated floor.yml.)

## `secretscan.py` — keep plaintext credentials out of git history

leakscan guards the *public* boundary; `secretscan` guards one that exists in
**every** repo, private ones included: a credential committed in plaintext is
burned the moment it lands in history — history is forever and a private repo can
be shared or leaked later. So this runs everywhere, and pairs with the SECRETS
doctrine's other half: **detect → rotate immediately → the burn cost is minutes.**

### Two detector classes

| Class | Catches | Confidence |
|---|---|---|
| **Named credentials** | vendor formats that are a secret by construction — private-key/PGP headers, AWS/GitHub/Slack/Google/Stripe/Anthropic/OpenAI/Twilio/SendGrid/npm tokens, JWTs, `user:pass@host` URLs | high; flags on shape alone |
| **Assigned + entropy** | a key that *names* a credential (`password`, `api_key`, `token`, `client_secret`…) assigned a long, high-entropy value that isn't a placeholder or indirection; plus a conservative context-free high-entropy net | medium; the workhorse for home-grown secrets matching no vendor format |

### Two responses (E6b, 2026-08-06)

A finding carries a **response** as well as a rule, and only one of them touches
the exit code:

| Response | Rules | Exit code |
|---|---|---|
| **block** | every named format, `assigned-secret`, and `high-entropy` — unchanged, byte for byte, from before the tier existed | `1` |
| **advisory** | `low-variety-entropy` — an unbroken 32+ character run with no credential-named key beside it (hex digests, single-case blobs) | `0` |

The blocking set never shrinks; the advisory tier is coverage that did not exist
before, opened on the path `HIGH_ENTROPY_RX`'s mixed-class requirement had shut.
An advisory finding nobody reads is cover rather than coverage, so it ships with
its consumers: the pre-commit hook prints them at the commit that would introduce
them, every CI push re-prints **all** of them tree-wide, and `floor.py`'s board
carries a `🟡 N advisory finding(s)` count read from that run's output — no state
file, so nothing to go stale and nothing to quietly vanish.

It deliberately does **not** flag the safe indirections — `!secret foo` (tiki),
`${VAR}`, `$(cmd)`, `<placeholder>` — those are the *correct* way to reference a
secret. It skips variable/attribute/call values (`password=admin_password`),
public-key material (`ssh-ed25519 …`, `public_key:`), **public-key fingerprints**
(`SHA256:…`, colon-joined hex — public by definition, matched whole-shape so a
near-miss still flags), and URL paths, which are the dominant false positives in
real source. The report prints only a redacted fingerprint (length + entropy),
never the secret value.

### Usage

```sh
python3 tools/secretscan.py                 # scan the whole repo
python3 tools/secretscan.py --staged        # scan only staged additions (the hook)
python3 tools/secretscan.py path/to/file    # scan specific paths
python3 tools/secretscan.py --json          # machine-readable, for CI/composition
python3 tools/secretscan.py --selftest      # prove the engine on this box
```

Exit codes match leakscan (`0` clean **or advisory-only** · `1` blocking
findings · `2` usage/config error).
Escape hatches mirror it too: `# secretscan:allow: <reason>` per line, a glob in
`.secretscanignore` per path, and `--disable <rule>` to quiet a noisy rule (a
named rule, `assigned`, `high-entropy`, or `low-variety-entropy`) while keeping
the rest. A true
positive is never just exempted — **remove it, move it to the secret store, and
rotate it.**

## `licenscan.py` — the pre-publish licence gate

The third member of the publish triad. leakscan keeps personal data out;
secretscan keeps credentials out; both guard *content*. `licenscan` guards the
licence story: publish a repo whose licence is missing, self-contradictory, or
carries someone else's copyleft code and you grant the wrong rights (or, with no
LICENSE, none — the default is all-rights-reserved). Unlike the other two it is a
**pre-publish** check, not an every-commit one: a private repo carries licence
mess harmlessly; it only bites at the public boundary that `AUTONOMY` already
gates.

### Three checks, rising specificity

| Check | Catches | Severity |
|---|---|---|
| **LICENSE present + recognised** | an open repo with no LICENSE (all-rights-reserved by default), or a LICENSE body no known SPDX licence matches (read as a declared custom licence since 2026-08-05 — the per-file header checks keep running; only declaration comparison is skipped) | high / medium |
| **Declarations agree** | metadata that names a *different* licence than LICENSE — `pyproject.toml`, `package.json`, `Cargo.toml`, `*.gemspec`, `setup.cfg`, a README shields.io badge — i.e. the repo contradicting itself | high |
| **No incompatible header** | a file with an `SPDX-License-Identifier` differing from the repo licence — copyleft (GPL/AGPL/LGPL/MPL) into a permissive repo is a **block** (can't be relicensed on publish); permissive-into-permissive is a warn | high / medium |

The compatibility judgement is deliberately **conservative and advisory** — it
flags for a human, it is not legal advice, and it does not encode the deep cases
(e.g. Apache-2.0/GPLv2). It encodes the one that bites in practice:
copyleft-into-permissive.

### Usage

```sh
python3 tools/licenscan.py                      # scan the repo in cwd
python3 tools/licenscan.py path/to/repo         # scan a specific repo root
python3 tools/licenscan.py --expect Apache-2.0  # assert the licence (CI); fail if LICENSE differs
python3 tools/licenscan.py --json               # machine-readable, for CI/composition
python3 tools/licenscan.py --selftest           # prove the engine on this box
```

Exit codes match the others (`0` clean · `1` findings, publish blocked · `2`
usage/config error). Escape hatches mirror them: `# licenscan:allow: <reason>`
per line (a deliberately dual-licensed file, or a header in test data), a glob in
`.licenscanignore` per path. Because it's a publish gate, wire it into the
**pre-publish** scrub (alongside the leak/secret pass) and CI's release job — not
the per-commit hook.

## `worktree.py` — one worktree per line of work

`method/CONCURRENCY.md` says every independent line of work gets its own git
worktree — own checkout, own branch, **outside iCloud** (a live `.git` index in
iCloud corrupts under sync) — reconciling on `main` via PR/merge. Said once
that's easy; at 11pm it's the forgotten rule. This makes the right thing the
one-liner and bakes the guards in.

| Command | Does | Guard it encodes |
|---|---|---|
| `worktree start <feature>` | checkout at `~/worktrees/<repo>-<feature>`, branch `<feature>` | **refuses an iCloud base**; branches off the integration branch so a line never inherits a half-done branch |
| `worktree list` | every worktree + ahead/behind, dirty, age | flags **stale** (diverged for days = merge hazard) and **dirty** (leaked file handle) trees |
| `worktree land [<feature>]` | push the branch + open a PR back to `main` | refuses to land `main` onto itself or with uncommitted changes; falls back to a local-merge instruction when there's no remote |
| `worktree remove <feature>` | `git worktree remove`, guarded | **refuses to delete uncommitted or unmerged work** without `--force` — losing work is the failure mode the whole doctrine exists to prevent |

### Usage

```sh
python3 tools/worktree.py start perf-harness   # fork a line of work
python3 tools/worktree.py list                 # hygiene view (--json for tooling)
python3 tools/worktree.py list --check         # exit 1 if any tree is stale/dirty (CI/hooks)
python3 tools/worktree.py land perf-harness    # push + PR back to main
python3 tools/worktree.py remove perf-harness --delete-branch
python3 tools/worktree.py --selftest           # prove the guard logic offline
```

Zero-dep, `--json` on every command (the orchestrator seam), fail-safe exit
codes (0 ok · 1 a guard tripped · 2 environment error). Real-world side-effects
stay serialised: this forks *build-time* lines only — applying a change to a live
device is still one-at-a-time and announced (CONCURRENCY "the safety rail").

## `pins.py` — the fleet view of who is stale on the doctrine

`method/PROPAGATION.md` makes staleness observable one repo at a time: each
child's `CLAUDE.md` carries a pin (`atelier@<SHA>`) and a session-start drift
check. That is per-child and pull-based — a child only shows it's behind when a
session opens in it. `pins` is the roll-up: stand in atelier, get one answer to
"across the whole fleet, who is behind, and by how much?".

It is deliberately **read-only**. Bumping a pin stays a per-repo
human-in-the-loop act (PROPAGATION §5 — read the delta, judge it bears on that
repo, then move the pin). This tool never edits a child; it turns per-child
observability into a fleet view and nothing more.

| Status | Means | Mark |
|---|---|---|
| `current` | pin == atelier HEAD | ✓ |
| `behind` | pin is an ancestor of HEAD — N house commits since | → |
| `ahead` | HEAD is an ancestor of pin — child pinned newer (atelier not pulled here?) | ! |
| `diverged` | neither is an ancestor — pin on a different history | ✗ |
| `unknown` | atelier has no such object — bad/rewritten pin, or unfetched | ? |
| `no-pin` | `CLAUDE.md` exists but names no atelier pin | · |

### Usage

```sh
python3 tools/pins.py                    # discover children under atelier's parent, report
python3 tools/pins.py --log              # also print the commits each stale child would inspect
python3 tools/pins.py --child ../ros     # report only named repo(s) (repeatable; skips discovery)
python3 tools/pins.py --root ~/code      # search a different root (repeatable)
python3 tools/pins.py --json             # machine-readable, for a dashboard / CI gate
python3 tools/pins.py --check            # exit 1 if any child is not current (CI/hooks)
python3 tools/pins.py --selftest         # prove the parse + classification offline
```

Discovery walks one level under each search root (default: atelier's parent dir)
for git repos whose `CLAUDE.md` carries a pin; atelier itself is excluded. An
unreadable root degrades to a warning, not a crash (fail-safe). Exit codes match
the others: `0` every child current · `1` at least one not current · `2`
environment error (not an atelier repo, HEAD unreadable, a named child missing) —
so a fleet it *couldn't* verify never reports green.

## `linkscan.py` — keep the doctrine's internal pointers resolving

atelier's architecture is **"thin anchor, fat pointer"** (`method/PROPAGATION.md`):
a child inlines a safety floor and *points up* to canonical doctrine; a doc states
a bearing and *points* to its case-law. The whole graph is only as sound as its
links. A relative link that 404s — a renamed file, a moved doc, a typo'd `#anchor`
— is a silent hole: the reader is told "see X" and X isn't there. `linkscan` is the
machine that catches it before a reader (or an adopter) does.

Scope is deliberately narrow — a sharp honest check beats a broad flaky one:

- **Internal links only.** `[text](path)` / `![alt](path)` with a relative or
  root-relative (`/…`) destination. External schemes (`http`, `https`, `mailto`,
  `tel`, …) and protocol-relative `//host` are **skipped** — verifying them means
  the network, which is a different, flakier tool's job.
- **File existence** — the path must resolve (relative to the linking file, or the
  repo root for a leading `/` — GitHub resolves those against the repository root
  too), to a real file *or* directory, with the **on-disk casing matched exactly**
  (a case-insensitive local disk hides a mismatch GitHub 404s) and the target
  **inside the repo root** (GitHub serves nothing above it — a `../…` that
  resolves on this machine is still a 404 for every reader).
- **Anchor existence** — a `#fragment` into a Markdown target (or same-file) must
  match a heading anchor **exactly** (GitHub fragment matching is exact —
  `#A-Section` never reaches `#a-section`; the report says what to write
  instead). ATX (`#`) and setext (underline) headings both mint anchors. `#L42`
  line anchors are line references, not headings, and are skipped; anchors into
  non-Markdown targets aren't validated (nothing to validate against).

Links inside fenced (` ``` `) or inline (`` `…` ``) code are ignored — they're
examples, not live pointers. Wiki-style `[[name]]` memory links aren't Markdown
links and are out of scope by design. A deliberately dangling pointer is exempted
with `<!-- linkscan:allow: <reason> -->` on the line, or a glob in
`.linkscanignore`.

### Usage

```sh
python3 tools/linkscan.py                 # scan the whole repo
python3 tools/linkscan.py docs/method      # scan a subtree / named files
python3 tools/linkscan.py --root . .       # explicit root for /… links + .linkscanignore
python3 tools/linkscan.py --json           # machine-readable, for CI
python3 tools/linkscan.py --selftest       # prove the engine offline
```

Exit codes match the others: `0` every internal link resolves · `1` at least one
break · `2` usage/config error — so a scan it *couldn't* complete never reports
green. See the residual note at the top for what it structurally cannot catch.

**Wiring** — unlike the licence gate, linkscan runs on both the **pre-commit
hook** and **CI**, always over the **whole tree** (not `--staged`): a link goes
stale when a *different* file is renamed or deleted, so the file to re-check is
rarely the one in the diff. It is cheap (stdlib, no network) so the hot-path cost
is negligible, and it is the one gate that catches a 404 *before* a push
publishes it. A repo that keeps its tree link-clean pays nothing; a deliberately
dangling pointer uses `linkscan:allow` / `.linkscanignore`.

## `sizescan.py` — keep cold content off the always-loaded files

A session resumes cold by reading a handful of files at the start — the roadmap
(what's open), the session index (where the last one stopped), the README, the
architecture note. `RECORD.md` prescribes the fix for when they bloat — the
**current-truth / history split** (open items stay; completed detail moves to
`ROADMAP-DONE.md`; a flat session log becomes an index + `docs/sessions/`). The
split works, but nothing *triggered* it: it got done once by hand and the
discipline decayed silently — a sibling roadmap reached 3000+ lines, each
finished item accreting a running log of how it got done, no signal firing.
`sizescan` is that missing signal.

**Cost is size × read-frequency (2026-07-20 ruling)**, so the enemy is never
fulsomeness — it is **cold content on the hot path**: content that is finished
(no longer live current-truth) yet still loaded every session. `sizescan` fires
on exactly that, and only where the fix is mechanical and lossless:

- **The gate** fires on **relocatable cold content** — a completed `[x]` item on
  a checkbox-worklog file (`ROADMAP.md`), whose whole remedy is a lossless move
  to `ROADMAP-DONE.md` (the current-truth/history split). The gate can never
  demand a reword: it fires only when a machine can name the fix as a move. It
  never fires on length.
- **Length is a pure advisory** — the line count reports (a class reference
  point: `ROADMAP` ~300, `SESSIONS`/`README`/`ARCHITECTURE` ~250, `CLAUDE` ~200,
  where the fleet's healthy files sit) but **never fails a build**. A file long
  purely from live open items is fine; the number is a prompt to look for
  un-marked resolved narrative, not a ceiling to golf under.

Narrow in two further deliberate directions:

- **It meters only the files meant to stay lean** — `ROADMAP.md`, `SESSIONS.md`,
  `ARCHITECTURE.md`, plus the **root** `README.md` and `CLAUDE.md` (a nested
  `tools/README.md` is a reference index, read on demand — not metered, so the
  signal stays sharp). A long *reference* doc (`PRINCIPLES.md`, a doctrine file)
  is read on demand, not every session, so it isn't metered either.
- **It ignores the append-only stores by design** — `ROADMAP-DONE.md`,
  `CHANGELOG.md`, `SPECS.md`, and anything under `sessions/`, `reviews/`,
  `decisions/`, or archive dirs. Those are the *destinations* the split moves
  detail into; flagging them would punish the very fix the tool encourages.

Prose-shaped cold content (resolved narrative under an *open* item) and thinness
aren't mechanically detectable — they stay **caught at review, not measured** (the
standing one-sided honesty: the tool never fails on what it can't name losslessly).
A legitimately long all-open file can quiet the advisory with an inline
`sizescan:budget=N` (grounded in its class, never its current length), opt out
with `sizescan:allow`, or a glob in `.sizescanignore` — none of which silences the
cold-content gate; for that, harvest the `[x]` items.

### Usage

```sh
python3 tools/sizescan.py                  # report over the whole repo (length advisory + any cold content)
python3 tools/sizescan.py --root repo repo  # scan a child from atelier
python3 tools/sizescan.py --check          # gate: exit 1 only if a file has relocatable cold content
python3 tools/sizescan.py --json           # machine-readable
python3 tools/sizescan.py --selftest       # prove the engine offline
```

**The gate has a narrow bite.** Cold content is a recoverable hygiene threshold
with a lossless fix — harvest the `[x]` item aside — so a bare `sizescan`
**reports and exits 0** (drop it in CI to surface the advisory numbers without
breaking a build); `--check` gives it teeth, but **only on cold content, never on
length**. Exit codes: `0` clean or length-advisory-only · `1` cold content
present **and** `--check` · `2` usage/config error (a scan that read nothing is
never green — fail-loud, not fail-open).

**Wired into the gate (2026-07-20).** `sizescan --check` runs in atelier's
`ci.yml` and the child `floor.yml` in cold-content mode. Because it gates only on
a lossless move, it is safe to stack: it can red a build only when the fix is
`git mv`-shaped, never when it would demand a reword.

## `reviewscan.py` — decision records state their review judgement

`REVIEW.md`'s remedy made *declining* a review an act: every durable design
record carries a `review:` line — a queued pointer or an explicit
`not warranted — <grounds>` — because a reader can disagree with a stated
judgement but not with a blank. This is the structural half of that rule: it
reds any record under a `docs/decisions/` directory, named on the
coordination-free `YYYY-MM-DD[-HHMM]-slug.md` scheme and dated on or after
**2026-07-21** (the day the templates began prompting for the field — frozen
records are append-only and never flagged), that carries no review line.
Presence only, by design; scope deliberately excludes roadmap headings (a lint
there fires on prose — the `2026-07-18-0820` record's grounds). Exemption
hatch: `reviewscan:allow: <reason>` on any line. Deliberation:
`docs/decisions/2026-07-21-0744-review-line-artefact.md`.

```sh
python3 tools/reviewscan.py --root . .        # scan a repo
python3 tools/reviewscan.py --root . docs/decisions   # a decisions dir directly
python3 tools/reviewscan.py --selftest        # prove it against fixtures
```

A path arg may be a tree, a `docs/decisions/` dir itself, or a single record
file — an explicitly-named path is scanned, never silently matched by nothing
(the 2026-07-21 cold pass's RS1). The review line must carry a non-empty
value, and a `review:` quoted inside a code fence doesn't count (RS2/RS3).

## `publishscan.py` — no machine-local config is tracked

Every other scanner here asks *does this file contain something private?* This
one asks *does publishing this file, whatever it holds, help someone attack the
repo?* They come apart: `rpi`'s committed `.claude/settings.json` published the
exact list of commands an AI session runs **unprompted** — while going public
opened untrusted inbound (issues, PRs) into those sessions — and both content
scanners passed it correctly, because it holds no credential and no personal
fact. **The exposure was the file's presence, not its contents** (rpi F1,
2026-07-29; Mike ruled the same day that the allowlist is untracked
*everywhere*, not only on public repos, because a visibility-conditional rule
becomes wrong at the moment of the flip).

Patterns carry their provenance in the source: the `.claude/settings*.json`
pair is grounded in that finding; `.mcp.json`, `.env*`, `.envrc`, `.netrc`,
`.npmrc`, `.pypirc` and editor-local config are standard practice, named as
such rather than dressed up as findings. Hatch: a glob in
`.publishscanignore` — there is deliberately **no line marker**, because a
reason written inside a file that should not exist is an exemption no reviewer
would ever see.

```sh
python3 tools/publishscan.py --root .            # the tracked set (CI plane)
python3 tools/publishscan.py --root . --staged   # what this commit adds (hook)
python3 tools/publishscan.py --root . --warn     # advisory while a repo cleans up
python3 tools/publishscan.py --selftest          # prove it against fixtures
```

A tree with no git skips visibly at exit 0 — not a fail-open, since nothing is
tracked and so nothing can be published from it. Every *other* git failure (git
absent, repo corrupt) is exit 2: a broken scan is not a pass.

## `datescan.py` — absolute-UTC dating discipline (FIRST-OF-KIND, advisory only)

Seam S3 (2026-07-22 invariant-candidates review): a dated record states
ISO-8601 absolute dates stamped from `date -u`, never a relative-time word
("today", "yesterday", "last week") whose meaning drifts with the reader's
"now" — grounded in a real miss, the standing correction that cost a
five-file sweep when a record was stamped from local NZ time instead of UTC.
Two checks over `docs/**` Markdown by default: a **relative-time-word
denylist**, and an **ISO/UTC shape check** (a non-ISO absolute date like
`23/07/2026` or `July 23, 2026`; an ISO-*shaped* date that isn't a real
calendar day, e.g. `2026-13-40`).

**This scanner has not yet earned an independent review** (don't-stack), so
it is wired into CI **advisory-only** (`--warn`, always exit 0) and
deliberately **not** in the blocking pre-commit hook.

Exemptions, deliberately generous (a false positive costs a comment; a noisy
scanner trains itself away): a fenced code block or blockquoted line (quoted
external text), an inline `` `code span` ``, and — the hard case — a
relative-time word immediately flanked by a matching quote pair (`"today"`)
is read as a MENTION (prose *about* the word) rather than a USE, exactly the
shape the rule's own worked examples use. This is a punctuation heuristic,
not a parser: unquoted prose about relative time still false-positives, and
is meant to be closed with `datescan:allow`. The rule's third clause — "a
dated maintenance edit carries its date" — is **not** mechanically checked;
naming an edit's intent isn't a shape a text scanner can see honestly, so
that clause stays caught at review, same honesty as sizescan's
prose-cold-content residual.

```sh
python3 tools/datescan.py                 # scan docs/** (default scope)
python3 tools/datescan.py --root . docs    # explicit — the CI invocation
python3 tools/datescan.py --warn           # report findings, always exit 0
python3 tools/datescan.py --json           # machine-readable
python3 tools/datescan.py --selftest       # prove the engine offline
```

Exit codes: `0` clean, or `--warn` given · `1` findings without `--warn` · `2`
usage/config error. Escape hatches mirror the sibling scanners:
`<!-- datescan:allow: <reason> -->` per line, a glob in `.datescanignore` per
path.

## `wrapscan.py` — line-wrap / column hygiene (FIRST-OF-KIND, advisory only)

Seam S1 (2026-07-22 invariant-candidates review): Markdown prose under
`docs/**` wraps at the house width; a line **materially over** it reds —
concretely at or beyond `LINE_LIMIT + 1` (86 cols at the shipped limit of 85).
Grounded in a real repeat: the same over-wide-line class shipped **three
cycles running** (`SL7` → `AC1` at 122 cols → `IR3`), each fix re-introducing
the next, because nothing mechanical caught a judgement the reviewer kept
re-making. This scanner is that column count.

**Not yet reviewed** (don't-stack) — wired CI **advisory-only** (`--warn`,
always exit 0), **not** in the blocking pre-commit hook.

Column length is a character count, honest for the house's ASCII prose but not
a true display-width measure (a stated Unicode caveat). Four exemptions,
each with its honest limit documented in-header: **fenced/indented code**
(the indented rule is per-line, so it also exempts some wrappable indented
prose — a false negative accepted over a false positive inside real code);
**table rows** (any `|`-bearing line — a bare heuristic, not a table parser);
**ATX headings**; **reference-style link definitions**; and **single
unbreakable-token overflow** (a URL/path/long identifier with no legal wrap
point in the overflow — this *will* let through prose that merely ends in one
long word, the accepted line-local trade-off). Setext underlines are correctly
not special-cased.

```sh
python3 tools/wrapscan.py                  # scan docs/** (default scope)
python3 tools/wrapscan.py --root . docs     # explicit — the CI invocation
python3 tools/wrapscan.py --warn            # report findings, always exit 0
python3 tools/wrapscan.py --limit 100       # tune the column limit
python3 tools/wrapscan.py --json            # machine-readable
python3 tools/wrapscan.py --selftest        # prove the engine offline
```

Exit codes: `0` clean, or `--warn` given · `1` findings without `--warn` · `2`
usage/config error. Escape hatches mirror the sibling scanners:
`<!-- wrapscan:allow: <reason> -->` per line, a glob in `.wrapscanignore` per
path.

## `spellscan.py` — NZ-English spelling (FIRST-OF-KIND, advisory only)

Seam S5 (2026-07-22 invariant-candidates review): `docs/**` uses NZ-English
spelling (artefact, organise, colour, behaviour…). The premise is that a
scanner catches the convention the eye skips — the mining found `artifact`
used 15+ times across `method/` despite the rule, caught as a finding only
twice; the class is **under-detected, not rare**.

**Not yet reviewed** (don't-stack) — wired CI **advisory-only** (`--warn`,
always exit 0), **not** in the blocking pre-commit hook.

The denylist is generated from stem lists, one source of truth: an
`-ize/-ise` + `-yze/-yse` verb family (with a smaller `-ization/-isation`
subset that **excludes** stems whose noun is irregular — `recognize` →
`recognition`, not `recognization` — so it never invents a word), plus
hand-listed irregulars (artifact, the colour/behaviour/defence/centre
families, catalogue, favour, honour, fulfil). Matched case-insensitively as
whole words. **`license`/`practice` are deliberately excluded**: they are
US/NZ noun-verb homographs (NZ `licence`/`license`, `practice`/`practise`)
that need part-of-speech tagging to call correctly, and a bare heuristic would
false-flag every `LICENSE` heading and `SPDX-License-Identifier` — the honest
call is to leave them to review, documented in-header.

Exemptions mirror datescan (fenced/inline code, blockquotes, quote-flanked
MENTION) plus two this class needs: URL/path tokens (slash-detected, so
`actions/upload-artifact` is exempt for free) and a small `ALLOWLIST_PHRASES`
for bare-prose API terms (`artifact attestations`, `upload-artifact`…);
ALL-CAPS tokens read as identifiers/filenames. Honest limit: a legitimate
API term in bare prose still false-positives and is meant to be closed with an
inline-code span, the allowlist, or `spellscan:allow`.

```sh
python3 tools/spellscan.py                 # scan docs/** (default scope)
python3 tools/spellscan.py --root . docs    # explicit — the CI invocation
python3 tools/spellscan.py --warn           # report findings, always exit 0
python3 tools/spellscan.py --json           # machine-readable
python3 tools/spellscan.py --selftest       # prove the engine offline
```

Exit codes: `0` clean, or `--warn` given · `1` findings without `--warn` · `2`
usage/config error. Escape hatches mirror the sibling scanners:
`<!-- spellscan:allow: <reason> -->` per line, a glob in `.spellscanignore` per
path.

## `harvestscan.py` — a removed roadmap item arrived somewhere (advisory only)

The third member of `sizescan`'s family, and the only one that loses work: an
item **removed** from `ROADMAP.md` that arrives nowhere. Every other check reads
a file as it stands; this failure exists only as a difference between two
versions. It fingerprints an item's *content*, never its title — a healthy
roadmap retitles and re-homes constantly, and title-matching was measured at a
near-total false-positive rate.

**Scoped, and the scope is why it is wired at all.** Unscoped it fired on one
roadmap commit in four and was shelved on its author's own counsel. Its cold
pass measured the variant the shelving never did, and the principal overturned
the verdict on that measurement (HV1, 2026-07-29): scoped to
`--only-bulk-deletes` — a change shedding ≥ 50 **net** lines from `ROADMAP.md` —
the whole history holds 6 in-scope commits, of which 3 warn, including the
incident that motivated it. Net, not delete-only: that incident was +48/−184.

```sh
python3 tools/harvestscan.py --root . --staged --only-bulk-deletes  # the hook plane
python3 tools/harvestscan.py --root . .        # working tree vs HEAD, no gate
python3 tools/harvestscan.py --against <rev>   # against another revision
python3 tools/harvestscan.py --replay          # re-measure over the whole history
python3 tools/harvestscan.py --selftest        # prove the matching logic offline
```

Exit codes: `0` always for findings — **warn-only, never blocking**, because its
similarity threshold is honestly ungrounded and a check that cannot ground its
constant may not red a build · `2` usage/config error.

## `pointerscan.py` — the queued-review pointer, refs-only and true (advisory only)

Two guards on one parse of `ROADMAP.md`'s queued-review pointers:

- **grammar** — a pointer that seeds the reviewer's first question steers the
  pass it is queuing, against the ceiling `ROADMAP.md` and `REVIEW.md` both
  state. Fires on a question inside a pointer, plus a short list of
  reviewer-direction forms. Pass type and tier are **lawful** fields: they route
  the review; they say nothing about the delta's merits.
- **cycle state** — an item asserting a review is owed while carrying the verdict
  of the review that ran, with the state it is *actually* in named (reviewed,
  ruled, applied) rather than only the contradiction.

The scope decision — **what makes an item a queued-review pointer** — is settled
in the module docstring on the four recorded specimens, and it is the load-bearing
part: the marker glyph alone misses the specimen that was still live when this
shipped. `harvestscan` imports that decision rather than keeping a second copy.

It lints **no field into existence** anywhere — the 2026-07-18-0820 record
rejected a lint demanding a review line under every roadmap heading, and
`reviewscan` honours that refusal. This forbids content in one narrow,
self-identifying item type instead, which is a different rung.

```sh
python3 tools/pointerscan.py --root . docs   # explicit — the floor's invocation
python3 tools/pointerscan.py --json          # machine-readable
python3 tools/pointerscan.py --selftest      # prove the rules on the specimens
```

Exit codes: `0` always for findings — **warn-only**; a pointer is fixable in the
commit that writes it, which is the one moment the fix costs nothing · `2`
usage/config error. Escape hatch: `pointerscan:allow: <reason>` anywhere in the
item.

## `plainscan.py` — prose lands on the first pass (FIRST-OF-KIND, advisory only)

The mechanical floor under `COMMUNICATION.md`, which until 2026-08-09 had none
and said so in its own enforcement clause. Four rules, each named with what
grounds it, because two of them carry a house number and two need none:

| Rule | Fires on | Grounded in |
|---|---|---|
| **P1** | a short code (`F1`, `C5`, `SL2`) used with nothing saying what it points at | published — digital.govt.nz: expand on first use |
| **P2** | an uncommon acronym never expanded and absent from `GLOSSARY.md` | published — the same clause |
| **P3** | a sentence over the word limit (default 35) | **house call** — no plain-language authority checked publishes a cap |
| **P4** | a bracketed aside over the char limit (default 40) sitting mid-sentence | house doctrine, dated — `COMMUNICATION.md` 2026-07-15 |

**Why it exists.** Doctrine alone was measured and found not to be a control.
Across 6,704 assistant replies in 1,094 session transcripts, the rules above
were broken in 37%–67% of replies depending on the rule, and **the rate did not
fall after they were written down** — reference-ID density rose between July and
August 2026 while the rule against it sat in doctrine. Of every reference code's
first use in a session, 86% arrived with no gloss at all.

**Two planes off one engine.** `scan_text()` is the whole rule set and it takes
a string. The repo plane is this CLI, in the floor registry. The reply plane is
`tools/hooks/plain-reply.py`, a Claude Code `Stop` hook that lints
`last_assistant_message` and returns `{"decision": "block"}` so an unreadable
reply is rewritten before the principal reads it. Same lesson as `floor.py`'s
registry, one surface over: the rules are not reimplemented per plane.

The reply plane **fails open**, alone among this estate's gates, and the trade is
stated rather than accidental: `secretscan` failing open burns a credential for
good, while this failing open lets one clumsy reply through — and a linter that
can wedge a live session is worse than the defect it catches. It also gives up
after two blocked rewrites of one turn, saying so visibly in the transcript.

```sh
python3 tools/plainscan.py                     # scan docs/** (default scope)
python3 tools/plainscan.py --root . docs       # explicit — the floor's invocation
python3 tools/plainscan.py --warn              # report findings, always exit 0
python3 tools/plainscan.py --rules P1,P4       # a subset
python3 tools/plainscan.py --sentence-limit 45 # the house numbers are flags
python3 tools/plainscan.py --json              # machine-readable
python3 tools/plainscan.py --selftest          # prove the engine offline
```

Exit codes: `0` clean, or any findings under `--warn` · `1` findings · `2`
usage/config error. Escape hatch: a path glob in `.plainscanignore`. An acronym
is cleared estate-wide by giving it a `GLOSSARY.md` entry — the designed remedy,
not an exemption.

**Advisory, deliberately.** It lands `--warn` on both planes in the registry:
atelier's own docs return ~7,900 findings on the first run, and a blocking form
would red every commit in the estate on day one and teach everyone
`--no-verify`. `wrapscan` and `spellscan` landed the same way. The two house
numbers are the principal's to rule on before any move to blocking.

**The reply plane is LIVE (ruled 2026-08-09).** The `Stop` hook is installed in
the principal's `~/.claude/settings.json` at **45 words / 60 characters** — his
ruling, on a calibration against his own transcripts showing that setting would
have fired on 30.6% of historical replies. Note the asymmetry and that it is
deliberate: the reply plane **blocks**, the repo plane only warns. Chat is where
the defect was measured and where the fix is free (rewrite before sending);
committed prose meets a corpus written before the rule existed.

Installed form — `command` + `args` is the exec form, so no shell parses the
path, and the interpreter is pinned rather than PATH-resolved:

```json
{ "hooks": { "Stop": [ { "hooks": [ {
  "type": "command",
  "command": "/usr/bin/python3",
  "args": ["<atelier>/tools/hooks/plain-reply.py"],
  "timeout": 15
} ] } ] } }
```

The pin is `/usr/bin/python3` because it is always present on the machine and a
hook must not depend on a login shell's PATH. It is Python 3.9 there; both files
carry `from __future__ import annotations`, which is what lets modern type hints
run on it.

## `stampscan.py` — an inlined copy still equals its canonical parent (advisory)

Where a child repo or a template **inlines** a floor or a pull-quote of canonical
doctrine, the copy must equal its parent — or *legitimately narrow* it, declared
— never silently drop or contradict an item. The corpus paid for this class three
times before there was a scanner: `create-repo` C3 (nothing kept the stamped block
equal to PROPAGATION's canonical text), `method-layer` P1 (an inlined floor
silently dropped "new trust surfaces"), `foundation` Q2 (a pull-quote listed 4 of
6 floor items) — each caught by a human reading two files side by side.

The mechanism is a marker pair. The parent names a **region** with
`<region>:begin` / `<region>:end` HTML comments; the copy wraps itself in
`stamp:begin source=<path> region=<name>` / `stamp:end`. Both are HTML comments,
so stamping changes nothing visible. The convention itself is doctrine and lives
in [`docs/method/PROPAGATION.md`](../docs/method/PROPAGATION.md), beside the one
region it declares — including who may declare a `narrow=` (the child, with a
written reason) and the rule that **narrowing to nothing is drift**, not a narrow.

**Markers are recognised only outside fenced code and inline code spans**, like
every sibling scanner. That is not a nicety: a stray marker is a config error,
`--warn` never downgrades one, and before the fix any document that merely
*documented* this syntax reddened the whole floor — which is why the scanner sat
unwired for two weeks (2026-07-26 cold pass ST1). The named residual is a raw,
line-start marker in bare prose, which is indistinguishable from a real one;
rendered Markdown hides raw HTML comments, so genuine documentation uses a code
span anyway, and `.stampscanignore` nets the stores that quote probe material raw.

```sh
python3 tools/stampscan.py --warn --root . .   # the advisory CI invocation
python3 tools/stampscan.py --root . docs       # docs only, gating
python3 tools/stampscan.py --json              # machine-readable
python3 tools/stampscan.py --selftest          # prove the engine offline
```

Exit codes: `0` clean, or `--warn` with drift findings only · `1` drift, without
`--warn` · `2` usage/config error — a malformed stamp, an unresolvable source or
region, or a `source=` resolving **outside** `--root` (traversal and absolute
paths both escaped before; a crafted stamp could aim the scanner at any file on
the machine and get a line of it echoed in the drift hint). A config error is
**never** downgraded by `--warn`. Escape hatches: `stampscan:allow: <reason>`
anywhere inside a stamped block exempts that block; a path glob in
`.stampscanignore` exempts a file from being scanned for stamps of its own
(it stays usable as a canonical `source=` target).

**Wired advisory in atelier's own `ci.yml` only** — deliberately *not* in the
`floor.py` registry, which would reach every child at once (ADR 0008). The
template ships a stamp pinned at `source=docs/method/PROPAGATION.md`, a path that
exists only here, so a scaffolded child running it would exit 2; the child-side
resolution story also has to be **pin-aware**, since a child pinned at
`atelier@<SHA>` may lawfully differ from atelier@main. That is ST3, still open.

## Tests

```sh
cd tools && python3 -m unittest      # stdlib only, no pytest — covers every tool here
```
