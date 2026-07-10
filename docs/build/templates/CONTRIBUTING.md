# Contributing to <name>

<!-- One line on what it is and its scope. Point at ARCHITECTURE. -->
Before changing anything, read [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
so a change doesn't run aground on a deliberate boundary.

## Development setup

```sh
<!-- how to run it and how to run the checks -->
```

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

Significant or risky changes get a peer review before they're trusted — a
more capable model reviews approach, assumptions and real-world behaviour,
not just correctness. See [`docs/reviews/README.md`](docs/reviews/README.md).
