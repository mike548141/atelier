# cclive — what any session on this machine is doing, holding or claimed on

Status: **designed 2026-11-09, build follows this note.** Written before the
build because nothing in `instruments/` or `tools/` has looked across repos at
live work: `ccclose` reads one repo and one session, `pins` and `floorfleet` read
doctrine state, and `CONCURRENCY.md` § *Claiming work* and § *The channel* both
stop at one checkout.

## 1. What it is, in one line

A read-only CLI a session runs at open. It answers, in one screen, *what is any
session, anywhere on this machine, doing, holding or claimed on right now?*, and
says what it looked at so that a blank line cannot read as "nothing is
happening".

## 2. Why it exists

Item `360/020`. The principal asked, 2026-09-12, for ways *"to improve how
parallel sessions to converse, coordinate, share"* and *"to track, claim, and
coordinate work planned and in progress"*. Offered mechanisms on 2026-11-09, he
answered *"Build a machine-wide view"* (an answer to options offered, not a
ruling). Everything else in the concurrency doctrine is per-repo. A session
opening one repo has no way to learn that another session is mid-flight in a
sibling, even where the two could coordinate over a shared credential, host or
subject.

## 3. Home, language, name

**`instruments/cclive`, Node, zero dependencies.** It observes the
teammateship, a session invokes it at a moment of its choosing and no hook does,
and its central input is Claude Code's transcripts: an instrument under ADR 0006.
Node also lets it `require` `ccclose` for the two things that must not fork:
`FRESH_MS` and the board adapter (§5).

## 4. No new shared state

The candidates the item named were a per-estate index, widening the channel, and
doing nothing yet. **All three are rejected or deferred for this tool.** An index
sessions write to is a new shared thing that goes stale the moment a session
dies, the failure `CONCURRENCY.md` § *Beyond the repo* already declined to take
on for marker files. The channel is awareness between sessions that are talking;
this answers the session that does not yet know who to talk to. Everything the
question needs already exists on disk, and every source below is written for
another reason. So `cclive` writes nothing and asks no session to do anything new.

## 5. What it reads

| Source | How | Cost |
|---|---|---|
| Repos | One level under each search root, a directory with a `.git` entry, as `tools/pins.py discover` walks | one `readdir` per root |
| Claims | `git grep` for a `[~]` line in the repo's board **at the newest of its `main`/`master`/`origin/main`/`origin/master`** | one spawn per repo |
| Worktrees | `git worktree list --porcelain`, then `git log --no-walk` for last-commit ages; a repo with no `.git/worktrees` directory has only its primary checkout and spawns nothing | two spawns per repo with linked worktrees |
| Live sessions | Mtime of `~/.claude/projects/*/*.jsonl` and `*/<session>/subagents/agent-*.jsonl` | one stat per recent file |
| Where a session is | The last `cwd`, `gitBranch` and `aiTitle` in the tail of a *fresh* transcript only | 256 KiB per fresh file |
| Load | `os.loadavg()` and core count | none |

**Why the ref, not the working tree.** A claim is a commit on the integration
branch, and the local `main` is often behind `origin/main`, because a worker lands
with `git push origin HEAD:main` from a worktree. Newest committer date across the
four candidate refs reads whichever is ahead, in one spawn, without fetching.

**Which board.** `ccclose`'s `board()` adapter, required rather than copied: a
generated index with its item store reads the store; a hand-kept `ROADMAP.md`
reads that file. A repo with no board reports claims as *unknown*, never zero.

**What counts as a claim.** A `[~]` state line at the left margin, or an indented
`[~]` carrying a `claimed <date>` stamp. The stamp is looked for across the item's
first paragraph, read with `git grep -A4` and `tools/board.py`'s own paragraph
rule: on a real board all eleven claims in one repo carried the stamp on line two,
because `wrapscan`'s width wraps a title and a claim sharing the first line. A
stamp that says it was released dates nothing. An indented `[~]` with no stamp is a
progress mark on a sub-bullet (one real board has 26 of them), so it is not
counted. A left-margin `[~]` with no stamp is counted separately as **undated**:
the same board has 52 such lines, most of them old, and the view keeps them to a
count so they don't bury the dated ones. `--all` lists them.

**Which session is where.** By the transcript's own `cwd`, longest-prefix matched
against every worktree of every scanned repo, realpath on both sides. The folder
a transcript is filed under is not used: it is the directory the session *started*
in, and the encoding is lossy. A subagent is matched by its own `cwd`, so an
orchestrator in one repo with a worker in another shows in both. A `cwd` under no
scanned repo goes in an *elsewhere* group: dropped, it would be the blank that
reads as nothing.

**Live means written within `FRESH_MS`.** Ten minutes, `ccclose`'s bound from a
census of 3,587 agent logs in which 99.9% of gaps between records were 600 s or
less. It is imported, not re-declared, so the two tools cannot disagree about what
"still running" means. `--fresh <minutes>` widens it for a question like "who was
here this past hour".

**The agent walk is bounded by the parent.** A session's `subagents/` directory is
listed only when its parent transcript was written in the last 24 hours. Without
the bound the walk costs 367 ms over 3,602 agent logs (measured on a loaded
machine); with it, 39 ms. No log of those 3,602 was written more than 0.2 hours
after its parent's last write, so a 24-hour gap is 120 times anything observed.
The limit it leaves, a subagent still writing a day after its parent went silent,
is stated in the man page.

## 6. What it prints

One screen: a header (time, load, roots scanned, what was skipped, transcripts
read), one TOTAL line, a section per repo with anything in it, one *quiet* line
listing the rest by name, and the limits, every run.

Fields are stable. Every repo header carries the same fields in the same order
and prints a known zero; an unknown prints as `?` with its reason. `--json` is the
same data, with every field present on every repo.

Ordering, so it reads at a glance: repos with a live session first, then by
newest activity; in a repo, live before quiet, then newest first. Claims and
worktrees cap at five per repo with the cut counted; sessions never cap, since
they are the point and are bounded by what is really running. `--all` lifts the
caps.

Cross-referencing is what makes it more than three lists. A claim line whose
stamp names a live session (its 8-hex id) or a worktree that has a live session in
it is marked `live`; a worktree with a live session in it, or named by a live
claim, is marked `live` (a worker can keep its session's starting directory while
it works by absolute path, so the claim is the second route). Neither is proof of
the other's absence, so the other mark says only `quiet`, and the limits line says
what `quiet` is worth.

## 7. Honest limits, in the output and the man page

- **A claim is a commit.** It stays until a commit removes it, so a claim whose
  session died reads the same as a live one. `live` is a positive match; `quiet`
  is no match, and that is all it is.
- **A quiet transcript might be a slow agent**, past the bound on one long
  command. And a session open and waiting on its operator writes nothing, so it
  reads as quiet while still holding a worktree.
- **Another machine's sessions are invisible.** Only this machine's transcript
  store is read. A claim made on another machine shows only once it has reached a
  ref here by a fetch, and `cclive` does not fetch.
- **Only what is under the roots.** A repo outside them is not scanned; the header
  names the roots and what was skipped, and a session working in one lands under
  *elsewhere*.

## 8. What stays out, and why

- **Open pull requests.** Network per repo; the principal's own answer noted the
  one-line open-PR check is already in the session onramp.
- **Dirty state.** A `git status` per worktree costs seconds on a large repo, and
  the view must answer in a second or two. It also would not change what a session
  does next: it reads "someone is there" from the session and the claim.
- **Process inspection** (`ps`, `lsof` for open `claude` processes). It would catch
  the idle-open session, but `lsof` is slow under exactly the load this is read
  during, and it is the only platform-specific source in the set. Transcripts carry
  the repo, the branch and the title; the process table carries a pid. Named as a
  limit instead.
- **Reading whole transcripts.** A fresh transcript's tail is enough, and the store
  holds files over 20 MB.
- **Locking, leases, or any write.** `CONCURRENCY.md` § *Beyond the repo* already
  declined a locking protocol.

## 9. Neighbours, so as not to take their ground

- `310/020` (what the estate owes the house): doctrine currency, one mechanism
  later. `cclive` says nothing about pins or floor copies.
- `320/640` (a question about the estate answered from one tree): search of records
  across repos. `cclive` reads claims and live state, not records or history.
- `320/650` (an estate fact learned in a child): where a fact is written. Not this.
- `360/010` (name what you launch): the announcements and owner markers are a
  channel for what a tool can't see, and `cclive` does not read containers or
  remote hosts.

## 10. Reused, and a twin declined

`FRESH_MS` and `board` come from `ccclose`, which already exports the first; the
second is a new export, and the only change this build makes to an existing tool.
Two copies of the bound would drift, and it is the one number both tools must
agree on.
