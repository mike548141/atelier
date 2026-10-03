# Toolbox — know what's available, don't rediscover it

Every session that has to re-learn "is ripgrep here? where's the venv? is `gh`
authenticated?" spends attention on something already known. The fix is a
**tool manifest**: a maintained record of the capabilities available and
approved, so the agent starts each session knowing its toolbox instead of
probing for it.

## Two things, kept separate

- **The practice (this doc).** *Keep a list. Record the approved tools, how to
  find them and how to install them. A listed tool that is missing may be
  installed. Upgrading a listed tool is a routine ask. A tool not on the list
  is confirmed first. Keep the list current.*
- **The expected toolbox (this doc too, public).** In Mike's own words
  (2026-10-03), the list of tools every session should expect lives **here in
  atelier**, with a method to find each one: *"I want you to include a list
  of tools to expect to be installed locally and how (a method) to find
  them, that does not necessarily mean paths need to be published
  publicly."* So the list
  carries **names, purposes, finding methods and install routes**, and never a
  machine's paths, hostnames, accounts or token scopes. Those last stay in the
  operator's person-level context (today `~/.claude/`).
  *Correction, recorded because the error repeated:* this section used to say
  the list "lives in the operator's person-level private context… never in a
  shareable repo". A child session's record (`roadmap/320-…/500`) also
  credited Mike with putting it in a private estate-root repo. **Neither was
  his.** Both were written by sessions. In his words: *"I've said Atelier many
  times it is claude session that keep saying a private repo not me"*
  (`320/510`). Which groups of tools are on the list was Mike's **answer** to
  options a session offered, which is not a ruling (`420/020`).

## The expected toolbox

A session should expect these to be installed. **Find** says how to locate
one that is not on `PATH`, and the method is below the table. **Get** says
how to install it when it is missing.

| Tool | For | Find (if not on `PATH`) | Get |
|---|---|---|---|
| `gh` | GitHub: PRs, runs, API | user bin | Homebrew |
| `aws` | AWS CLI | — | AWS's installer |
| `az` | Azure CLI | its own venv | pip into a venv, or Homebrew |
| `gcloud`, `gsutil`, `bq` | Google Cloud CLI | the SDK's own `bin` | Google's installer |
| `python3`, `pip3` | Python runtime | — | python.org installer |
| `node`, `npm`, `npx` | Node runtime | — | nodejs.org, or Homebrew |
| Playwright | browser automation | a Python package: `python3 -m playwright` | `pip install --user playwright`, then `python3 -m playwright install` |
| `git`, `make`, `curl`, `sqlite3` | core dev | — | Xcode command-line tools |
| `jq`, `rg` (ripgrep) | data and search | — | Homebrew |
| `ruff`, `mypy`, `pytest`, `pre-commit` | Python quality | pip user bin, or a venv | `pipx install` |
| `pipx` | isolated Python CLIs | pip user bin | `pip install --user pipx` |
| `brew` (Homebrew) | the installer for most rows | — | brew.sh. **Needs an admin password, so Mike runs it.** |
| GNU coreutils (`gtimeout`, `gtac`) | macOS has no `timeout` | Homebrew bin | `brew install coreutils` |
| `ffmpeg`, `ffprobe`, `yt-dlp` | media capture | user bin | Homebrew, or the projects' releases |
| `groff`, `mandoc` | man pages | — | `brew install groff`; `mandoc` ships with macOS |
| `pdftotext` | PDF text | Homebrew bin | `brew install poppler` |
| `docker` | containers | — | Docker Desktop, or Colima via Homebrew |
| `terraform`, `wrangler`, `cloudflared` | infrastructure, Cloudflare | `wrangler`: npm global bin | Homebrew; `npm i -g wrangler` |
| `nmap`, `openssl`, `sops`, `age`, `tcpdump`, `ike-scan` | network and security | `ike-scan`: per its repo's onramp | Homebrew (`tcpdump` and `openssl` ship with macOS) |
| `tiki`, `cctranscript`, `ccrepo`, `ccmail`, `ccarchive` | the estate's own tools | user bin | their repos' install steps (`instruments/` here) |

**Known quirks, generic to macOS rather than to any one machine:**
- macOS `openssl` is LibreSSL.
- macOS ships no `timeout`. Use `gtimeout` from coreutils.
- A Playwright install's browser cache can run ahead of the library.
- A tool installed into a venv shells out to *itself* by name. The Azure
  CLI's extension installer does, and fails when the venv's `bin` is not on
  `PATH`.

**How to find a tool that is not on `PATH`.** Stop at the first step that
finds it:
1. `command -v <tool>`, and `which -a` for every copy.
2. **The installer's own location**, asked of the installer rather than
   guessed:
   - pip user installs: `$(python3 -m site --user-base)/bin`. Each Python
     version has its own, so try each `python3`.
   - npm globals: `$(npm prefix -g)/bin`.
   - Homebrew: `$(brew --prefix)/bin`.
   - Google Cloud SDK: its `bin` under the install folder.
   - venv-installed CLIs: a `*venv*/bin` under `~/.local`.
   - App-bundled CLIs: inside the `.app`, e.g. Wireshark's `tshark`.
3. **Python packages that are also CLIs:** run them as modules from the
   interpreter that has them, e.g. `python3 -m playwright`, trying each
   interpreter `which -a python3` lists.
4. **Found but off `PATH`:** call it by its full path for this session, and
   say so. Editing a shell profile to fix `PATH` changes the machine, so ask
   first.
5. **Not found anywhere:** it is missing. Install it under the rule below.

## The install rule (ties to AUTONOMY)

- **Listed and missing → install it.** That is a normal action, and needs no
  ask (`AUTONOMY.md`). Use a trusted package manager, then use the tool. If
  the install needs an admin password (Homebrew itself, a `.pkg` installer),
  prepare the exact command and hand it to Mike, because a session cannot
  type his password.
- **Listed but out of date → ask, as a routine step.** Mike, 2026-10-03:
  *"You should still ask for apprval from the principal before upgrading but
  it should be considered a normal action for you to undertake."* So upgrading
  is not a floor stop. Batch upgrade asks with the session's other questions.
- **Not on the list → confirm first.** New tooling is a new capability and a
  new trust surface, and that is the owner's call (`AUTONOMY.md`'s floor).
- **When a session finds a tool the list lacks, or a better finding method,
  it updates this list** in the same commit as the work that needed it.

## The command allowlist is part of this

A repo's `.claude/settings.json` allowlist is the machine-checkable half of the <!-- pathscan:allow: gitignored by design since the P1 untrack ruling — never on disk in a fresh checkout -->
manifest for *shell commands* — the commands the agent may run unprompted. It's
the "approved" column for the command layer. The manifest in this doctrine sits
one level up: it also covers higher-level tools and connected services that
aren't single shell commands, and it says how to acquire the ones that are
approved but absent.

**The allowlist is machine-local, never committed** (Mike ruled 2026-07-29;
grounded in `rpi`'s post-flip cold pass, F1). It is a list of what runs
*without a human in the loop*, so publishing it converts prompt-injection
reconnaissance from a guess into a plan — the same reasoning that stops a
public repo naming the estate-root repo. The content scanners cannot help here:
the file holds no credential and no personal fact, so `secretscan` and
`leakscan` correctly pass it. **The exposure is the file's existence in the
tree, not its contents** — which is why the guard for this class has to ask a
different question from every scanner that came before it. The rule is uniform
rather than public-only: a visibility-conditional rule becomes wrong at the
moment of the flip, which is the moment attention is elsewhere.

The cost is real and named: the allowlist stops being a shared, reviewable
record of what a repo's sessions may do unprompted, and each clone re-prompts
until it is seeded from the template. That trade was taken deliberately — the
reviewable record can be rebuilt from a template that is *not* per-repo state,
whereas a published allowlist cannot be unpublished. The residual is also
named (PS2 ruled 2026-08-02; PSA1 ruled 2026-08-03): the seed templates
themselves stay published, so the estate *default* remains mapped — a repo
whose live allowlist never diverges from seed is still described exactly by
the public template, and the sibling `settings.local.json` template
discloses one further default (`acceptEdits` — edits apply without per-edit
approval). What the untracking hides is each repo's divergence from those
defaults, not the defaults themselves.

*Bearing: the expected toolbox above is this estate's list, published by
ruling. What stays machine-local is the per-machine detail: accounts, token
scopes, the per-repo command allowlists and exact paths. A peer adopting
atelier replaces the table with their own.*
