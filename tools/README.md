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

### Wiring it in

- **Pre-commit hook** — copy `tools/pre-commit.sample` to
  `.git/hooks/pre-commit` (`chmod +x`). It runs `leakscan --staged` and aborts
  the commit on a finding. This is the primary control.
- **CI** — run `python3 tools/leakscan.py --json` on every push (belt and
  braces; a hook only protects the machine that has it installed).

### Tests

```sh
cd tools && python3 -m unittest      # stdlib only, no pytest
```
