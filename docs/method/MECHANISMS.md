# Mechanisms — which one a new need should take

A new need ("sessions keep doing X") can be met by several kinds of thing this
estate already runs. Until now the choice was made by precedent. This is the
guide to making it on purpose. It chooses among **mechanisms**; choosing among
**models** is `ECONOMICS.md`, and the one narrow membership question (does a
CLI belong in atelier) is ADR 0006.

**Status:** Mike approved a one-page guide on four axes, 2026-11-09 (board item
`400/010`; his pick from options offered, an answer, not a ruling in his
words). The axes are read out of fragments already in the doctrine, not
invented, and the order below is this guide's reading, offered for use and for
correction. It is not a decision tree anyone ruled.

## What is in play

| Mechanism | Where it lives | How it fires |
|---|---|---|
| **Guard** (policy as code) | `tools/` scanner, wired to the hook and CI floor | On every commit, unasked |
| **Hook** | `PreToolUse`, `Stop` and kin | Intercepts a tool call or turn, unasked |
| **Skill** | `skills/`, shipped in the plugin | By name, or reached for autonomously |
| **Slash command** | an action file under `skills/<subject>/`, run as `/atelier:<subject> <action>` | Only when deliberately invoked |
| **Instrument** | `instruments/` (ADR 0006) | A teammate runs the CLI directly |
| **MCP server** | `instruments/browser-fetch/` is the one in-estate example | Available to query mid-reasoning |

Doctrine text (a rule in `docs/method/`) is the zeroth option: when nothing
needs to fire, say it once, in its home, and point at it.

## Four axes, in the order to ask them

1. **Must a violation be blocked, or is it a judgement a session applies?**
   The programme's premise is directive first, enforced second
   (`GUARDS.md`). If a machine can decide it and the cost of a miss is real,
   build a guard. If it is judgement, it is doctrine text, or a skill if it
   is a procedure worth a checklist. Check first that the enforcement point
   can deliver the *remedy*, not only detect the fault: a `Stop` hook fires
   after the reply has streamed, so it can detect a bad reply and cannot retract
   it (`COMMUNICATION.md`, the reply plane that was unwired).
2. **Does it intercept automatically, or get invoked deliberately?**
   A hook fires unasked, which is its value and its risk (wrong moment, as
   above). A command and most skills wait to be reached for. An MCP server sits
   available to be queried repeatedly mid-reasoning, which none of the others
   do. Pick the weakest trigger that still catches the failure.
3. **Who needs it: one repo, or the estate?** A scanner is wired per repo by
   the floor. A skill ships once in the plugin and installs everywhere, *when
   installed at all* (`180/010`: the plugin nobody had installed). An instrument
   is a standing binary on one machine.
4. **What does it cost to carry?** A skill is an episodic context cost
   (`ECONOMICS.md`, heavy skills). A scanner runs near-free on every commit once
   built. An MCP server carries a standing connection and maintenance burden
   neither of the others does (`instruments/browser-fetch/` carries its own
   venv and browsers).

## Where it lives and what it is called

Whatever mechanism is chosen, a thing that helps the principal work with
Claude has **one home, atelier**, and a skill or slash command has **one
prefix, `/atelier:`**. The principal commissioned this on 2026-11-18 (his
words in board section `450`): he wanted every customisation "under one /
command so that they are easy to find as a group", because sessions had
named skills "whatever name made sense to you at the time".

- **A skill or command is born in the plugin** (`skills/`), which names it
  `/atelier:<subject> <action>`: every command is a subject, a space and an
  action, and a bare subject shows its menu. Not in `~/.claude/skills/`, not in
  `~/.claude/commands/`, not in a repo's `.claude/`.
- **The one exception is the bare `/atelier` menu** (`instruments/atelier-menu`),
  which has to be user-level because no plugin skill can answer a bare
  prefix. It lists the plugin's commands from their own front matter.
- **Private content does not move the home.** This repo is public. When a
  skill needs an estate's repo list, rulings or results, the skill is general
  and lives here; the estate's values sit in a private config it reads (the
  split `210/440` made: `ccfleet`'s JSON config, the drain's queue). A skill
  that cannot be split that way is a finding for the board, not a reason to
  ship it under another name.
- **The tripwire:** `tools/prefixhook.py`, wired as a `SessionStart` hook,
  names any skill or command outside the prefix at session open; `--check`
  gives a health sweep the same list as an exit code. It warns, never blocks:
  a misplaced skill costs findability, not harm (axis 1).
- **Moving an existing tool here from another repo is told to the principal
  first**, item by item. His condition, 2026-11-18, verbatim: *"tell me
  before you make changes like pulling a tool from another repo into
  atelier"*.

## Worked reading

- *"Never commit a credential"*: blockable, machine-decidable, estate-wide,
  near-free per run. **Guard.**
- *"Open a review the way the brief says"*: a procedure, judgement inside it,
  reached for by name. **Skill** (or command if it must never self-trigger).
- *"Show me what this session cost"*: a read-only CLI for one machine.
  **Instrument.**
- *"A rule about how to word a reply"*: judgement; the attempt to enforce it
  failed on axis 1's remedy test. **Doctrine text.**

## Not decided here

No ruling says when a second MCP server is worth building; axis 4 only prices
it. The board item that asked for this guide described the one MCP server as
third-party and never built in-estate; `instruments/browser-fetch/` is in this
repo, so that premise was stale, and this guide follows the tree. Whether the
table needs a seventh row is open.
