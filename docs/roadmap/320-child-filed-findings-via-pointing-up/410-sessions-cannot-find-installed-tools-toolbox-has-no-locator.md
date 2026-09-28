- [ ] 🎯 **PROPOSAL, hand-up from a private child — sessions cannot find tools
      that are installed but off `PATH`; `TOOLBOX.md` owns the practice, the
      instance it prescribes does not exist, and nothing says how to LOCATE a
      tool** `[M][doctrine][instruments]` — filed 2026-09-28 by a private
      child's session on the principal's request. A findability defect plus a
      commission to rule on, not a claim that the house is silent.

      ## What the principal asked (his words, 2026-09-28)

      > We really do need a better way to know what tools are already
      > available across every claude session, and every repo (or work without
      > a repo) because we have Azure cloud CLI, a PIP version I believe;
      > Github CLI; AWS CLI; Cloudflare CLI; nmap; openssl; sshd; I'm pretty
      > sure playwright and various other tools. And they are not always in the
      > path statement. Could be in Claude memory or some other way.
      > Potentially Atelier would even list the software that's expected to be
      > installed locally (pre-approved) and a relative path to find it on any
      > of the computers that use atelier (without giving out computer
      > hostnames or full paths).

      ## Evidence (measured in the child's session unless marked)

      - **Near-miss on the floor, 2026-09-28.** A session concluded Playwright
        was absent and was about to ask to install it — an *unapproved-tool
        install* is a floor stop. The principal corrected it. Playwright's
        Python package is installed for the system Python's user site (its CLI
        under `~/Library/Python/<ver>/bin`, off `PATH`). Its cached browsers
        are a few builds newer than the library expects, so it works only when
        launched with `executable_path=` pointing at the cached build.
      - **A false "not installed", 2026-09-27** (from the child's record, not
        re-measured here). A session told the principal no Azure tools
        existed. The Azure CLI is a pip install in a venv under
        `~/.local/`, off `PATH`; its dynamic extension install then fails
        because it shells out to `az` on `PATH`.
      - **One `PATH` probe, one machine, 2026-09-28.** On `PATH`: `gh`, `aws`,
        `nmap`, `node`, `terraform`, `openssl` (which is **LibreSSL** on
        macOS — a quirk that has bitten TLS work before), `sshd`, `jq`,
        `ffmpeg`, `yt-dlp`, `wrangler`. **Off `PATH` but installed:** `az`,
        `playwright`, `ike-scan` (reached via a repo-specific env var). **Not
        found where probed:** `cloudflared` (may run in a container — not
        checked), `pwsh`, `kubectl`, `docker`, `tofu`.
      - **Where the knowledge lives today — four partial homes, none of which
        travels.** The principal's user-level onramp names one tool directory;
        one child's onramp carries an "environment gotchas" list; that child's
        session memory holds one-off notes; per-repo allowlists carry commands.
        A session in any *other* repo or with no repo sees none of the
        repo-scoped three.

      ## What the house already has — and what is missing

      **`TOOLBOX.md` already owns the practice**, so this is not a new rule
      from scratch: keep a manifest, approved-but-missing may be installed
      (`AUTONOMY.md` line 34), unapproved is confirmed first. What failed:

      1. **The instance does not exist.** `TOOLBOX.md` puts it in the
         operator's person-level context (`~/.claude/`); no manifest file is
         there (measured, one machine). The estate root's machine records carry
         hardware fields and no software field (measured).
      2. **Two homes are named for it.** `TOOLBOX.md` says person-level
         `~/.claude/`; the floor's estate-resources bullet lists *"shared
         estate tooling"* under the private estate root. A session cannot tell
         which to read or write. **Ambiguous** in § *Pointing up*'s sense.
      3. **The fields miss the failure.** Per tool it records name, status,
         *how to get it*, auth. It does not record **how to find it** — env
         var, `$HOME`-relative path, `command -v` — or known quirks. Every
         incident above is a tool that *was* installed.
      4. **Nothing reads it at session open.** `TOOLBOX.md` is item 10 in the
         method README; neither the floor block nor the session-open prompt
         points at the manifest. The floor names the install stop but not the
         list that decides "approved".

      ## Options — offered as an order, not an either/or

      | | What | Buys | Costs / risks |
      |---|---|---|---|
      | **A** | Memory / onramp notes only (today) | Free | Per-repo; does not travel; the measured failure |
      | **B** | Resolve the home (item 2), add *locate* + *quirks* fields, create the instance manifest in the private home, and point the floor or session-open at it | Every session reads one list; closes all three incidents | Someone keeps it current; a stale entry misleads as well as a missing one |
      | **C** | B plus a small probe in `tools/` (e.g. `toolscan.py`) run at open: reads the private manifest, reports each tool *present / off-`PATH` (found via its locator) / missing* — names and states only, never absolute paths or hostnames | Staleness surfaces itself; "approved?" becomes a lookup, so the install stop is checkable | Another instrument to maintain; must run on every OS the estate uses |
      | **D** | Publish the approved list in atelier itself, as the principal floated | One public place, no private dependency | 🚩 **Cuts against the 2026-07-29 allowlist ruling** (`TOOLBOX.md` § *The command allowlist*): a public list of what a session may install or run unprompted turns prompt-injection reconnaissance from a guess into a plan. Same reasoning, same exposure |

      **Recommendation: B, then C.** B is mostly writing and fixes the incidents
      that happened; C makes it self-checking once B has a list to read.
      **The split for the principal's "relative path" idea:** atelier publishes
      the *shape* — the schema, the locator kinds (`command -v`, env var,
      `$HOME`-relative candidate path), the probe, and generic quirks that
      name no machine (a Python package whose browser cache runs ahead of the
      library; macOS `openssl` being LibreSSL). The private home holds the
      *instance* — which tools are approved and where each sits relative to
      `$HOME`. That honours his "no hostnames or full paths" and keeps D's
      exposure closed. **Where D's cost is a judgement about his own risk
      appetite, that call is his** — the recommendation rests on the existing
      ruling, not on new analysis.

      **What this item does not settle:** which of the two private homes wins
      (item 2) — both are the principal's, and the choice is about where he
      wants to maintain it, not about safety.

      ## Where it would land

      `TOOLBOX.md` (fields, home, pointer); the floor's estate-resources bullet
      or `session-open/` for the read-at-open pointer; `tools/` for C. No
      doctrine or tool is written by this filing.

      ## Principal's ruling (2026-09-28, via the child's ask device)

      Put to him with the options table above and a recommendation; he chose
      both recommended answers:

      - **Order: B, then C.** The private approved-tools manifest with *locate*
        and *quirks* fields, read at session open; then the probe that reports
        present / off-`PATH` / missing by name only. A and D are not taken.
      - **Home: the private estate-root repo**, not person-level `~/.claude/`
        — this settles item 2's ambiguity; `TOOLBOX.md`'s pointer moves to
        match.

      The state line above still carries the 🎯 because the filer touches only
      the body; the landing session drops it and names the build owed.
