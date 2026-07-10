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
- **secretscan** deliberately trades away single-case hex (git SHAs would
  drown it): a **hex-encoded token outside a secret-named assignment** is not
  caught, nor is a novel vendor format that is neither assignment-anchored nor
  high-entropy-mixed-class, nor a literal secret that *begins* like an
  indirection (`$uperS3cret…` reads as `$VAR`).
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

The scans are the mechanical floor, not the whole boundary: the human
pre-publish scrub (and the review practice) owns the residual above.

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
  has it installed). **A child repo cannot do this yet** — it has no scanners
  and CI has no atelier path; scanner distribution (vendor / fetch / publish)
  is the deferred supply-chain call (ROADMAP), so a child's only scan gate is
  the per-clone hook. That gap is stated, not silent.

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

It deliberately does **not** flag the safe indirections — `!secret foo` (tiki),
`${VAR}`, `$(cmd)`, `<placeholder>` — those are the *correct* way to reference a
secret. It skips variable/attribute/call values (`password=admin_password`),
public-key material (`ssh-ed25519 …`, `public_key:`), and URL paths, which are
the dominant false positives in real source. The report prints only a redacted
fingerprint (length + entropy), never the secret value.

### Usage

```sh
python3 tools/secretscan.py                 # scan the whole repo
python3 tools/secretscan.py --staged        # scan only staged additions (the hook)
python3 tools/secretscan.py path/to/file    # scan specific paths
python3 tools/secretscan.py --json          # machine-readable, for CI/composition
python3 tools/secretscan.py --selftest      # prove the engine on this box
```

Exit codes match leakscan (`0` clean · `1` findings · `2` usage/config error).
Escape hatches mirror it too: `# secretscan:allow: <reason>` per line, a glob in
`.secretscanignore` per path, and `--disable <rule>` to quiet a noisy rule (a
named rule, `assigned`, or `high-entropy`) while keeping the rest. A true
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
| **LICENSE present + recognised** | an open repo with no LICENSE (all-rights-reserved by default), or a LICENSE body no known SPDX licence matches (can't verify the rest) | high / medium |
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

## Tests

```sh
cd tools && python3 -m unittest      # stdlib only, no pytest — covers all six tools
```
