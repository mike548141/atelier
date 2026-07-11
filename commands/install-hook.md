---
description: Install atelier's git pre-commit scan hook into this repository (secret · leak · link, fail-closed).
allowed-tools: Bash(git:*), Bash(cp:*), Bash(chmod:*), Bash(python3:*), Bash(cd:*)
---

Install atelier's **git pre-commit hook** into the current repository. It blocks a
commit that would put a plaintext secret or personal/estate data into history, or
leave a broken internal link, and it **fails closed** — a missing scanner blocks
the commit rather than waving it through.

This is a *git* hook, not a Claude Code event hook: a plugin cannot install it
automatically, and git transports neither hooks nor config — so this must be run
**once per clone / per machine**.

Do this:

1. **Confirm a git repo and find its hooks dir** (respects worktrees / custom
   `core.hooksPath`):
   `git rev-parse --show-toplevel` and `git rev-parse --git-path hooks`.

2. **Install the hook:**
   ```sh
   cp "${CLAUDE_PLUGIN_ROOT}/tools/pre-commit.sample" "$(git rev-parse --git-path hooks)/pre-commit"
   chmod +x "$(git rev-parse --git-path hooks)/pre-commit"
   ```

3. **Point the hook at this plugin's bundled scanners.** Critical: `${CLAUDE_PLUGIN_ROOT}`
   only exists inside Claude Code — at `git commit` time it is undefined. So store
   the **resolved absolute path**, not the literal variable:
   ```sh
   git config hooks.atelierTools "$(cd "${CLAUDE_PLUGIN_ROOT}/tools" && pwd)"
   ```
   (The hook resolves its scanners as: `ATELIER_TOOLS` env → `git config
   hooks.atelierTools` → in-repo `tools/`. The absolute path above is what makes it
   work from a repo that has no scanners of its own.)

4. **Prove it once** (don't assume — this is the whole point of the hook):
   - Confirm the scanners are reachable: `python3 "$(git config hooks.atelierTools)/secretscan.py" --selftest`.
   - Optionally stage a throwaway line containing a well-formed test secret, attempt
     a commit, and confirm the hook **blocks** it (exit non-zero); then remove it
     and confirm a clean commit **passes**. Report the result honestly.

Tell the user three things after installing: (a) the hook guards **only this
clone** — every fresh clone or other machine must re-run
`/atelier:install-hook`; (b) after a **plugin update or uninstall**, re-run
`/atelier:install-hook` in each repo that has the hook — the stored scanner
path is version-pinned to the installed plugin copy, so an update leaves it
dangling (the hook then **blocks** commits rather than waving them through, by
design, until re-pointed); and (c) the escape hatches for a genuine false
positive (inline `…:allow:` markers / `.*scanignore` globs), and
`git commit --no-verify` for a real emergency only.
