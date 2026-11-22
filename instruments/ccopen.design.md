# ccopen — the session-open reads, run as code

Status: **designed 2026-11-22; the build follows this note** (board `210/520`).
It is the twin of `ccclose` (`ccclose.design.md`, which it follows in shape:
home, four states, read-only, stable fields, one verdict line) and scales that
design down: seven reads instead of fifteen checks, and no transcript to
attribute work from, because a session that has only just opened has done
nothing yet.

## 1. What it is, in one line

A read-only CLI a session runs when it opens, from the session-open prompt. It
answers, from a fresh read of the repo, the host and GitHub, *what am I opening
onto, and is anything owing before I start?*, and ends with one verdict line.

## 2. Why it exists

The opening reads are today prose: `CLAUDE.md`'s read order, the session-open
prompt's "Anchor to doctrine", "Assume another session may be live" and "If a
session gets interrupted", and `CONCURRENCY.md` § *Surviving an interrupted
session*. A session narrates them from habit, and the one that skips a step
(the dirty tree it autostashed, the hand-up PR it never listed) skips it
silently. The principal, 2026-11-22, verbatim:

> *"Also do the same for anything else that we can build as deterministic code
> and hook into sessions instead of using the prompt. But be mindful in all of
> these changes that I only use the prompt when I think its useful too, there
> are some sessions where I purposely dont want to give some of the commands
> that are in the template prompt"*

**So `ccopen` is a command the prompt runs, never a hook.** A session he opens
without the prompt never runs it, because nothing wires it to session start.
The prompt gains one line that names it; the doctrine text it replaces stays,
since a session without the prompt still reads `CLAUDE.md`.

## 3. Home, language, name

`instruments/ccopen`, Node, zero dependencies, for the reasons `ccclose` is
(ADR 0006: invoked by a session at a moment of its choosing, never by a hook).
It `require`s `ccclose` (repo facts, the board adapter, the pin check, `gh`
readiness, `FRESH_MS`) and `cclive` (the live-work read), and does not copy
either. Where a helper was not exported, the build exports it, and that tool's
own tests run. The name pairs with `ccclose`.

## 4. The surface

```
ccopen [--root <dir>] [--json] [--no-fetch]
ccopen -h | --help
```

`--root` names the checkout (default: the current directory, resolved to its
git top level), as `ccclose` spells it. `--json` is the same data, every field
present on every run. `--no-fetch` skips the one write (below). No `--fix`:
read-only by contract.

Exit 0 unless a read is ❌ (1) or the usage is wrong (2).

## 5. Read-only, except one fetch

Every git call runs with `--no-optional-locks`, as `ccclose` does. The single
exception is `git fetch origin` in the repo, which `ccopen` says it did: ahead
and behind are meaningless against a stale ref, and `CLAUDE.md` step 1 syncs
first. It updates remote-tracking refs and touches no working tree.
`--no-fetch` skips it, and the sync line then says "as of the last fetch". The
pin read also fetches (inside `pins.py`, in the atelier checkout); under
`--no-fetch` it is measured offline against atelier's local `HEAD` instead
(`pins.py --head`) and says so.

## 6. The reads

Fixed set, fixed order, every run. Each ends in ✅ ready · ⚠️ look · ❌ recover
· ➖ not applicable (its input is absent; the line says why). A read never
passes on something it could not read: an unreadable input prints ⚠️
`unknown — <why>`. Details are indented under the line, lists capped at five
with the cut counted, and known zeros are printed.

1. **Kind of session** (*Anchor to doctrine first*). Atelier itself
   (`tools/pins.py` beside `docs/method/PROPAGATION.md`, as `ccclose` check 14
   tells it); a child (a pin `atelier@<sha>` or a floor stamp in `CLAUDE.md`),
   naming the pin; a repo without doctrine (⚠️: the prompt's minimum viable
   version applies, and the line names the queue file it found, `docs/ROADMAP.md`
   or `ROADMAP.md`, or says none); not a repo (➖).
2. **Sync** (`CLAUDE.md` step 1). Working-tree files changed (listed), and
   ahead/behind against the branch's upstream, else the default branch's remote
   ref. Dirty is ⚠️ *someone else may be editing: take a worktree, never
   autostash*. Behind and clean is ⚠️ with the pull command (`git pull
   --rebase` on a clean tree only). Ahead, diverged, detached and a failed
   fetch are ⚠️ too, each said in words.
3. **Live work** (*Assume another session may be live*). `cclive`'s own read
   for this repo: transcripts written in the last ten minutes whose working
   directory is in it, `[~]` claims matched to them, worktrees they are in. The
   calling session (`$CLAUDE_CODE_SESSION_ID`) is excluded. Any other live
   session, live claim or live worktree is ⚠️ *coordinate; skip claimed items*.
   No board means claims print unknown, never zero.
4. **Interrupted predecessor** (*If a session gets interrupted*;
   `CONCURRENCY.md` sweep table). Residue no live session explains: dated `[~]`
   claims no live session or worktree matches, linked worktrees other than this
   one that no live session is in (each with its changed-file count), local
   branches (not the default, not this one, not at a live worktree, not the head
   of an open PR; each `merged` or `not merged`), and stash entries. Any is ❌
   *recover first*. The sweep is run on every open, not only on the tell
   ("a last commit, then silence, and no closing session file"), because a tool
   cannot read silence; the tell's number (commits after the newest session
   file's commit) is printed as context and drives no state, since in a repo
   with parallel sessions it is nonzero most of the time.
5. **Hand-up PRs** (`CLAUDE.md` step 6). `gh pr list --state open`: a head ref
   `report-` or `handup/`, or *hand-up* in the title. In atelier itself any is ❌
   (landing one is the first act of the session that finds it); in another repo
   it is ⚠️, since landing is atelier's. `gh` missing or not authenticated is ⚠️
   unknown; no GitHub remote is ➖. The count of other open PRs is printed.
6. **Pin currency** (*If a peer or parent repo has moved on*). `ccclose`'s
   check 14, unchanged: `tools/pins.py --json --child <repo>`. A pin behind with
   the floor unchanged is ⚠️ (read the delta, then decide); a floor that moved,
   a floor copy that differs, or a pin ahead, diverged or unknown is ❌. ➖ for
   atelier itself and for a repo with no pin.
7. **Newest session files** (`CLAUDE.md` step 4). The newest three names in the
   session folder at the integration ref, so the session reads them. ➖ with no
   session folder; a repo that only keeps the retired one-file index says so.

**Verdict**: `✅ ready to start`, `⚠️ look first: <each ⚠️ read, in words>`, or
`❌ recover first: <each ❌ read, in words>` (❌ wins when both).

## 7. Honest limits, printed or in the man page

- **No live session is not proof of none.** A session open and waiting on its
  operator writes nothing, so a quiet claim or worktree can still be live; the
  read says "no live session matched", and ❌ in read 4 means *read the residue
  and decide*, never *it is yours to delete* (`CONCURRENCY.md`: an orphan is
  reclaimed on the evidence, not a timer; and another session's recovery is not
  yours, § *Stay in your lane*).
- **Another machine's sessions are invisible**, and a claim made there reaches
  a ref here only after a fetch.
- **A branch no live worktree holds** may belong to a live session between
  commits; read 4 lists it and the session judges.
- **Counts from a stale ref** after `--no-fetch` are as of the last fetch.

## 8. What is not mechanised

- **Which of the principal's words govern this run**: the prompt's *This run*
  section is his, not the repo's.
- **Reading `00-APEX.md`, `README.md`, `ROADMAP.md` and the session files'
  contents.** `ccopen` names the files; reading them is the point.
- **The reflog after the last close** (a sweep row): local, noisy and
  unattributable. **Whether a dirty tree is the session's own predecessor's or
  a peer's**: the read says what proves each (a live session) and no more.
- **A cold reviewer.** The session log is on the review rules' barred list
  (`REVIEW.md` rule 2); a cold pass does not run `ccopen`, whose reads 4 and 7
  look at the record. This is a property of the prompt (a review brief never
  includes it), stated in the man page.
