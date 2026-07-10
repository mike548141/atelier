# tools/ — atelier's mechanical controls

Doctrine informs; a *check* enforces. These are the checks. Zero third-party
dependencies — run them with the system `python3`.

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
partial cover, never silently weaker.

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
  `.git/hooks/pre-commit` (`chmod +x`). It runs **both** `secretscan --staged`
  and `leakscan --staged` and aborts the commit on any finding. This is the
  primary control. For a subtree/networking repo, edit the hook's leakscan
  invocation to add the `--disable`/path scoping above.
- **CI** — run both scanners with `--json` on every push (belt and braces; a
  hook only protects the machine that has it installed).

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

## Tests

```sh
cd tools && python3 -m unittest      # stdlib only, no pytest — covers all three tools
```
