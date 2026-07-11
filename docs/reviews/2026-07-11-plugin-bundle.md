# Review — the Claude Code plugin bundle (PR #3, branch `plugin-bundle`)

**Scope:** the v0.1.0 plugin/marketplace bundle (session 32) — range
`main...plugin-bundle` **plus the machine-facing install/marketplace
behaviour** (the part no diff-read catches). Net-new, first-of-kind,
public-facing tooling; the merge to main is the go-live act (the marketplace
resolves only from the default branch), so this review gates whether go-live
can be trusted. Don't-stack honoured: the builder (an earlier Opus session)
did not review its own bundle.

**Reviewer:** Fable, cold fresh-context session (2026-07-11), in an isolated
worktree; interrupted once by a session limit and resumed with context
intact. Live install verification was done at user scope and fully undone
(config verified clean after). Verdict below verbatim; disposition at the end.

---

## Cold review — plugin bundle (PR #3, branch `plugin-bundle`, range `main...origin/plugin-bundle`)

**VERDICT: PASS-WITH-FINDINGS** — the bundle does what it claims, the
builder's record is accurate where I re-ran it, and the merge-is-go-live
premise is proven true. Nothing blocks the merge; the findings below are
documentation/hardening follow-ups, none in the unsafe direction.

### Findings

1. **[Medium] Plugin updates silently invalidate every installed hook —
   undocumented.** `commands/install-hook.md` stores the resolved absolute
   scanner path in `git config hooks.atelierTools`. For a marketplace install
   that path is **version-pinned**:
   `~/.claude/plugins/cache/atelier/atelier/0.1.0/tools` (observed live;
   `installed_plugins.json` confirms per-version install paths, and uninstall
   marks the old copy `.orphaned_at` for pruning). So a plugin update to
   0.2.0 eventually leaves the stored path dangling in *every repo the hook
   was installed into*, and all their commits start blocking. The direction
   is correct — I proved live that a dangling path **blocks, never waves
   through** — but it is a foreseeable operational trap the command never
   mentions. Fix: add a third item to the command's closing "tell the user"
   list: *after a plugin update or uninstall, re-run `/atelier:install-hook`
   in each repo — the stored scanner path is version-pinned*. Consider also
   mentioning it in the README install section.

2. **[Low] `${CLAUDE_PLUGIN_ROOT}` inside SKILL.md bodies is unverified.** I
   proved the variable resolves in *command* context (the installed
   `/atelier:scan`, run headless in a foreign repo with no `tools/` of its
   own, found and ran the cache's scanners). Both skills
   (`skills/session-onramp/SKILL.md`, `skills/review-brief/SKILL.md`)
   reference doctrine via the same literal variable, but I could not exercise
   a skill invocation before hitting limits, and my docs-grounding subagent
   did not return. Failure mode is visible-and-recoverable (the model sees an
   unexpanded path but the docs sit adjacent to the skill's own location), so
   this is low. Fix: either verify once in a live session, or phrase the
   skill references location-relatively ("bundled with this plugin under
   `docs/method/`").

3. **[Nit] `session-onramp` advertises "two companion behaviours" but the
   bundle ships three** (`skills/session-onramp/SKILL.md`, closing
   paragraph) — `/atelier:install-hook` is omitted, and it is the mechanical
   gate the doctrine leans on hardest. Fix: name all three.

4. **[Nit] The branch predates `instruments/` on main.** Merge into current
   main is conflict-free (verified with `git merge-tree`: 0 conflicts), but
   post-merge the plugin will also ship `instruments/` as inert extra content
   nothing references. No action required; just be aware the shipped tree
   grows beyond what the CHANGELOG entry describes.

5. **[Note, not a bundle defect] Local-directory marketplace installs copy
   the working tree verbatim** — my install carried the worktree's untracked
   `tools/__pycache__/` and `.claude/settings.local.json` into the plugin
   cache. The real go-live path (GitHub) clones only tracked content, and the
   branch tracks nothing machine-local (verified via `git ls-tree`). Relevant
   only when testing from dirty checkouts.

### What I proved live vs statically vs could not verify

**Proved live:** `claude plugin validate` and `validate --strict` pass; local
marketplace add → user-scope install → all 4 components discovered (~320 tok
always-on, matching the record); the installed cache contains the **whole
repo including `tools/` and `docs/`** — the root-as-plugin one-source claim
holds at the consumer end. `/atelier:scan` exercised headless in a scratch
repo: scanners resolved from the plugin, and it honestly reported planted
licenscan and linkscan findings (my planted "secrets" were malformed shapes —
a 25-char AKIA and a low-entropy password; I confirmed directly that
well-formed AKIA/`ghp_` secrets **are** caught, so the clean report was
correct, not a miss). `install-hook`'s documented steps executed verbatim:
selftest OK, hook **blocked** a staged real-shaped secret (no commit
created), **passed** a clean commit, and **blocked fail-closed** on a
dangling tools path (the uninstall/move claim). Assumption 8 proven directly:
`claude plugin marketplace add mike548141/atelier` **fails today** (no
manifest on main) — the merge really is the go-live act, and the README's
install instructions only land with the merge that makes them true. Repo's
own gates re-run at the branch tip: all four scanners clean (leakscan with
the machine-local term list loaded, so the two-file `.leakscanignore`
exemption works against real data), `licenscan --expect Apache-2.0` clean,
exit-2 usage-error semantics confirmed, tools suite **205 OK** (matching the
builder's claim). **Verified statically:** manifest consistency (name/version
0.1.0/Apache-2.0 vs LICENSE), branch hygiene (diff is exactly 9 code/doc
files, no records, no personal data, correct authorship), hook resolution
chain in `tools/pre-commit.sample` matches what `install-hook.md` describes,
and every file the commands/skills reference ships in the install. **Could
not verify:** `${CLAUDE_PLUGIN_ROOT}` expansion specifically in skill (vs
command) context (finding 2), and the exact update-time cache lifecycle
beyond what the versioned layout and `.orphaned_at` marker imply (finding 1's
fix is worth making regardless). **Cleanup:** the plugin was uninstalled, the
marketplace removed, and I verified the config clean — `enabledPlugins` and
`extraKnownMarketplaces` empty, `installed_plugins.json` empty,
`known_marketplaces.json` back to `claude-plugins-official` only, the
orphaned cache copy removed, and the failed GitHub-add clone auto-cleaned by
the CLI. Nothing was pushed and no PR comment was made.

---

**Disposition (2026-07-11, same day, coordinating session — not the
reviewer):** findings 1–3 **[fixed] on the branch** (PR #3 updated): the
re-run-after-update warning added to install-hook's closing list; both
skills' doctrine references rephrased location-relative (finding 2's cheap
robust fix — no dependence on variable expansion in skill context); all three
companion behaviours named. Finding 4 noted (no action; the merge simply
ships `instruments/` too). Finding 5 is a test-methodology note, no action.
**Gate cleared — the merge (go-live) remains Mike's call.**
