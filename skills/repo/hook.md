---
action: hook
description: Install atelier's git pre-commit scan hook into this repository (secret · leak · link, fail-closed).
---

Install atelier's **git pre-commit hook** into the current repository. It blocks a
commit that would put a plaintext secret or the shape of personal/estate data
into history, or leave a broken internal link, and it **fails closed** — a
missing scanner blocks the commit rather than waving it through.

This is a *git* hook, not a Claude Code event hook: a plugin cannot install it
automatically. The hook files are **tracked in the repo** (`.githooks/`, ADR 0008
decision 4), so they travel with a clone and stay current; git transports no
config, so `core.hooksPath` still has to be set **once per clone / per machine**.

Do this:

1. **Confirm a git repo and find its top level:** `git rev-parse --show-toplevel`.
   Work from there.

2. **Install the tracked hooks and point git at them** (the same steps as
   `/atelier:repo create` step 6):
   ```sh
   mkdir -p .githooks
   cp "${CLAUDE_PLUGIN_ROOT}/.githooks/pre-commit" .githooks/pre-commit
   # A clean `git merge` makes its commit without running pre-commit; this hook
   # hands the merged tree to the same checks (it needs pre-commit beside it).
   cp "${CLAUDE_PLUGIN_ROOT}/.githooks/pre-merge-commit" .githooks/pre-merge-commit
   # The commit-message plane: git runs pre-commit before the message exists,
   # so the checks that read a commit message run one hook later.
   cp "${CLAUDE_PLUGIN_ROOT}/.githooks/commit-msg" .githooks/commit-msg
   chmod +x .githooks/pre-commit .githooks/pre-merge-commit .githooks/commit-msg
   git config core.hooksPath .githooks
   ```
   Never copy them into `.git/hooks/`: that is untracked, so the hook would
   exist on one machine only, and once `core.hooksPath` is set git stops running
   it while it still sits there looking like the gate (`deadhook.py` names it).
   Remove a hook an earlier install left there.

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
   - Ask the clone whether its hooks are on: `python3 "${CLAUDE_PLUGIN_ROOT}/tools/deadhook.py" --status`.
     It names the directory git runs hooks from, whether the scanners resolve,
     and any dead hook left beside the live ones (exit 1 if commits would go
     unscanned or a dead floor hook is present).
   - Optionally stage a throwaway line containing a well-formed test secret, attempt
     a commit, and confirm the hook **blocks** it (exit non-zero); then remove it
     and confirm a clean commit **passes**. Report the result honestly.

Tell the user three things after installing: (a) **commit `.githooks/`**, so the
hook files travel with the repo, and that the hook guards **only this clone**
until then — every fresh clone or other machine needs `git config core.hooksPath
.githooks` and the scanner path above, or a re-run of `/atelier:repo hook`;
(b) after a **plugin update or uninstall**, re-run `/atelier:repo hook` in each
repo that has the hook (it also refreshes the tracked copies) — the stored scanner
path is version-pinned to the installed plugin copy, so an update leaves it
dangling (the hook then **blocks** commits rather than waving them through, by
design, until re-pointed); and (c) the escape hatches for a genuine false
positive (inline `…:allow:` markers / `.*scanignore` globs), and
`git commit --no-verify` for a real emergency only.
