# Contributing to <name>

<!-- One line on what it is and its scope. Point at ARCHITECTURE. -->
Before changing anything, read [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
so a change doesn't run aground on a deliberate boundary.

## Development setup

```sh
<!-- how to run it and how to run the checks -->
```

Once per clone. The hook itself is **tracked** (`.githooks/pre-commit`, so it
travels with the repo and never goes stale), but git does not transport
*config* — so a fresh clone commits **unscanned** until these two lines are run.
Once wired, the hook fails closed rather than ever scanning nothing:

```sh
git config core.hooksPath .githooks
git config hooks.atelierTools "<atelier-path>/tools"
```

Prove it landed — this should print the checks and their state, not an error:

```sh
python3 "<atelier-path>/tools/floor.py" --list --plane hook
```

The hook names no scanner: it is a shim over `<atelier-path>/tools/floor.py`,
the one registry that this repo's CI reads too, so a check added upstream
applies here with no edit. To run a check **advisory** while re-baselining, or
to scope one to part of the tree, declare it in `.atelier-floor.json` at the
repo root — never by removing a check.

That file is also where this repo adds a check of its **own**, under `local`:
a rule that is genuinely repo-specific and could never be fleet-wide. Give it
a `run` path inside this repo and a `why`; it then runs beside the shared
checks and blocks the same commit. It cannot take a shared check's name, and a
declared check whose script is missing blocks rather than passing quietly. If
other repos would want the rule, it belongs upstream in atelier instead.

## What makes a good change

- **Stay in scope.** <!-- the non-goals -->
- **Test for real.** Say what you actually exercised, not just that tests
  pass. <!-- for web: which browsers/widths; for a CLI: which real inputs -->
- **New Zealand English** throughout (favourite, colour, organise);
  correct macrons on te reo Māori.
- **No personal data.** No addresses, contacts, health, family or
  business detail belongs in this repo.
- **Comments say _why_, not _what_** — constraints and non-obvious
  reasons only.
- **Record real decisions.** A short ADR in [`docs/decisions/`](docs/decisions/)
  when a choice rejects a plausible alternative or rests on hard-won
  evidence; a code comment for reversible ones.
- **Log the session.** Append a dated entry to
  [`docs/SESSIONS.md`](docs/SESSIONS.md) before finishing.

## Review

Significant or risky work gets a peer review before it's trusted — a more
capable model reviews the whole commitment: approach, assumptions, security &
privacy, and real-world behaviour, not just correctness. The trigger is
**commitment, not artefact**: a design or decision
others will build on earns one as much as a diff does, and earns it earlier,
when being wrong is still cheap. See
[`docs/reviews/README.md`](docs/reviews/README.md).
