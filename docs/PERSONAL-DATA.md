# Personal data atelier holds — the one list

atelier is a public repo. This file is the **only** place that lists the personal
data it holds on purpose. If a piece of personal data is not here, atelier does
not hold it, and a session that finds some has found a breach, not an oversight
to document around.

**The list is closed.** In a public repo a personal-data exception is the
principal's alone to grant, in his own words (`build/REPO-STANDARD.md` § *Personal
data*). A session never adds an entry on its own judgement: it stops, asks him
through the question device, and writes his answer here only when it is a grant.
The entries below are the whole list until he adds to it.

**Kept true by a test.** `tools/test_personal_data.py` reads this file, then
checks every tracked file: a listed string standing in a file no entry names
fails the suite, an entry naming a place where its string no longer stands
fails it, and so does a personal-data allow-marker in a file that no entry
names. Edit this file and the files together, or the suite is red.

**What counts.** Real people's names, contact details and addresses; health,
family and financial detail; identifiers that point at one person, such as an
account name. Not counted, so not listed: invented example people and addresses
in fixtures (`example.test` addresses, documentation-range IPs), which describe
no one, and the machine-local term list, which is never in a repo.

**Granted by.** Each entry says how it was granted. *His words* means a quotation
of him, stored verbatim where cited. *His call* means a decision he made that
a decision record keeps, not necessarily in his exact words. Neither is an agent's
own choice, and neither is a ruling unless the cited record says so.

**Records.** The record stores (session logs, review verdicts, board items, the
roadmap indexes) are append-only history. They are listed as stores because
rewriting history is not remediation on a public repo (`method/RECORD.md`); a
new entry in one may repeat a listed string, and may not add an unlisted one.

## PD1 — the hosting account name

- **Data:** `mike548141`
- **Why held:** it is the repo's own address and its attribution. Clone and
  marketplace-install commands, the CI workflow that calls atelier's floor, and
  the plugin manifests name it, and a reader cannot reach the repo without it.
  Purpose test: replacing it with a placeholder would break the command it sits in.
- **Granted by:** his words, 2026-10-03, quoted in `build/REPO-STANDARD.md`:
  there will be exceptions "like my github account".
- **May stand in:** `.claude-plugin/*.json`, `.github/workflows/*.yml`,
  `CHANGELOG.md`, `CLAUDE.md`, `README.md`, `docs/PERSONAL-DATA.md`,
  `docs/build/REPO-STANDARD.md`, `docs/build/templates/workflows/floor.yml`,
  `docs/decisions/*.md`, `tools/floorfleet.py`, `tools/test_floorfleet.py`,
  `tools/test_templates.py`, and the record stores `docs/ROADMAP-DONE.md`,
  `docs/SESSIONS.md`, `docs/reviews/*.md`, `docs/roadmap/**`,
  `docs/sessions/*.md`.

## PD2 — the author's full name

- **Data:** `Mike Clements` <!-- leakscan:allow:local-term: author's own published attribution; the list that declares it (ADR 0005), adopters substitute their own -->
- **Why held:** attribution. The plugin manifests carry it as author and owner,
  and the repo's convention line names the git identity commits are made under.
  Purpose test: attribution fails if the author is anonymous.
- **Granted by:** his call, recorded in `decisions/0005-going-public.md`
  (2026-07-10): published as a named worked example, "the name is attribution".
- **May stand in:** `.claude-plugin/*.json`, `CLAUDE.md`, `docs/PERSONAL-DATA.md`,
  and the record stores `docs/reviews/*.md` and `docs/sessions/*.md`.

## PD3 — the author's email address

- **Data:** `mike@cxi.nz`, `cxi.nz` <!-- leakscan:allow:email,local-term: author's own published git identity; the list that declares it (ADR 0005) -->
- **Why held:** it is the address on the commits and the principal of the signing
  trust list. Purpose test: a commit and a signature need an identity to verify.
- **Granted by:** his call, recorded in `decisions/0005-going-public.md`
  (name and email "frozen onto" the commits, accepted knowingly) and
  `decisions/0007-ssh-commit-signing.md` (the signing trust list).
- **May stand in:** `CLAUDE.md`, `allowed_signers`, `docs/PERSONAL-DATA.md`, and
  the record stores `docs/reviews/*.md` and `docs/sessions/*.md`.

## PD4 — the author's first name

- **Data:** `Mike` (not pinned to files by the test)
- **Why held:** the doctrine is addressed to its principal by name, as a worked
  example an adopter replaces with themselves. Purpose test: the doctrine reads
  as a real decision by a real person, not a floated abstraction.
- **Granted by:** his call, recorded in `decisions/0005-going-public.md`
  (voice: "named, not genericised").
- **May stand in:** anywhere in docs, skills and tools that speaks to the
  principal. **Honest limit:** a given name is an ordinary word in running prose,
  so no test can pin it to files. Entry PD4 is the only unpinned one.

## PD5 — the git author identity on every commit

- **Data:** the author and committer name and email recorded in the commit
  headers (no file holds it; the two names are PD2 and PD3).
- **Why held:** git writes it, and no marker can live in a commit header. History
  already published cannot be recalled.
- **Granted by:** his call, recorded in `decisions/0005-going-public.md`:
  rewriting history to a generic identity was rejected.
- **May stand in:** commit headers only. It is not a licence for the same
  details in a commit message body.
