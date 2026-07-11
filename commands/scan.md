---
description: Run atelier's publish-safety scanners (secret · leak · licence · link) over this repo and report findings.
argument-hint: "[path] (optional; default: the whole repo)"
allowed-tools: Bash(python3:*)
---

Run atelier's four publish-safety scanners over the current repository and report
what they find, honestly. They are zero-dependency stdlib Python and live in this
plugin at `${CLAUDE_PLUGIN_ROOT}/tools/` — nothing to install. Scan target:
`$ARGUMENTS` if given, otherwise the whole repo (`.`).

Run all four from the repository root, in this order. Each exits **0** = clean,
**1** = findings, **2** = usage error (a bad/nonexistent path — treat exit 2 as a
real failure, never as "clean"):

1. **secretscan** — plaintext credentials that must never reach git history (runs
   in every repo, whatever its visibility — a burned secret is burned regardless):
   `python3 "${CLAUDE_PLUGIN_ROOT}/tools/secretscan.py" --root . .`
2. **leakscan** — personal / estate data that must not enter a shareable repo. Its
   structural patterns always run; a machine-local literal term list
   (`~/.claude/leakscan-terms.txt`) loads *if present* and otherwise it degrades to
   structural-only with a warning (that list is machine-local by design — never in
   a repo):
   `python3 "${CLAUDE_PLUGIN_ROOT}/tools/leakscan.py" --root . .`
3. **licenscan** — one coherent, compatible licence across the repo (a *publish*
   gate: no LICENSE hard-fails as all-rights-reserved):
   `python3 "${CLAUDE_PLUGIN_ROOT}/tools/licenscan.py" .`
4. **linkscan** — internal Markdown links (paths + anchors) resolve, whole tree:
   `python3 "${CLAUDE_PLUGIN_ROOT}/tools/linkscan.py" --root . .`

Then report: for each scanner, clean or the specific findings (file · line · why).
If anything is a **false positive**, tell the user the two hatches that travel with
their repo — an inline allow-marker on the flagged line
(`secretscan:allow: <reason>` / `leakscan:allow:` / `licenscan:allow:` /
`linkscan:allow:`), or a root-relative glob in the matching
`.secretscanignore` / `.leakscanignore` / `.licenscanignore` / `.linkscanignore`.

Do not soften a real finding. A secret or a leak reaching a public repo is the
exact failure this command exists to prevent; report it first and plainly.
