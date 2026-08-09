# cctranscript — search across transcripts

Status: **BUILT 2026-08-09** (design pass 2026-07-27). Everything below is
implemented except where this banner says otherwise — the document is kept as the
design of record, not rewritten to match the build, so the places the build
*departed* from it stay legible.

Six claims below did not survive contact with the code or the live store, and the
build's own record carries the detail:

- **§4's "the refs are free" is wrong at file grain.** An `N.M` ref counts all
  preceding turns, so it cannot be computed from surviving lines alone — step 4's
  "parse only the lines that survive" and exact gate-invariant refs are mutually
  exclusive. The build chose correctness: a file that passes the gate is parsed
  whole. **DONE condition 13 is therefore only partially met** — a selective
  search runs at 1.22–1.32× a bare read, but a term present in every session
  reaches 3.7×. The flaky wall-clock guard was replaced with a structural one
  (`meta.sessionsParsed`, pinned by a test), which is the property the 1.5×
  condition was actually protecting.
- **§10's raw-line prefilter has an unmentioned false-negative class.** The gate
  reads raw JSON, where `"`, `\`, newline and occasionally non-ASCII are
  escaped — the live store holds 6 `ā` sequences against 6,698 raw `ā`. The
  build gates literal terms on an alternation of every form the term can take
  (measured free) and matches against the *decoded* text. For `--regex` the
  limitation is real and documented in NOTES rather than papered over.
- **§7's illustrated tool row shows the render's one-line summary.** The build
  excerpts the whole tool input instead: searching one chosen field is precisely
  the quiet wrongness §5 warns against.
- **§7 asks for `--top` in one sentence** but it appears in neither §3's surface
  list nor the DONE conditions. Built as ccrepo's documented per-level
  truncation, with what was hidden counted and printed.
- **The corpus figures are stale** — 440 sessions / 500 MB became 556 / 707 MB,
  and the bare-read floor with them (2.5–4.9 s, not 2.0–2.6 s).
- **The thinking-block count is stale** — 24,856 became 31,800. The load-bearing
  parts held exactly: 9 carry text, none after 2026-07-04.
Asked for by Mike (2026-07-26): *"Something that lets you search all the
transcripts using regex or for a simple term. If you give cctranscript a command
like `--repo` that limits the scope to search within."*

The gap is real and narrow. cctranscript resolves **one** session and renders it,
so it answers *"what happened in this session"* but not *"which session said
X"* — which is the question you actually have when you can't remember the
session. Everything needed to narrow the candidate set already exists; what's
missing is a way to ask a question *of* the set.

The roadmap left six questions open and pre-decided none. Five are settled below
on measured evidence; the sixth (`--materialise`) turned out to be settled
already by ratified doctrine rather than open at all (§8). **Two roadmap premises
were corrected by measurement** — the thinking layer is not searchable because it
is not written (§5), and search is I/O-bound rather than parse-bound, which makes
it roughly six times cheaper than the "reads every file" framing implied (§2).

Numbers below were measured on 2026-07-27 on the machine these instruments run
on (Node v24, macOS), against the live store at **440 sessions / 500 MB** and the
ccarchive mirror at **860 logs / 235 MB compressed → 680 MB of text**. Where a
claim is not measured, it says so.

## 1. What changes, in one line

`--search <term>` turns the existing `--list` sweep from *"here are the candidate
sessions"* into *"here are the turns that match"* — same discovery, same scoping
flags, same index shape, with the excerpt replacing the first-prompt column and
each row carrying the citable `N.M` reference you then open the session at.

It is **one flag plus a mode**, as the roadmap guessed — not a subcommand, and
not a second code path. `runList()` and `runTranscript()` already share
`pickSessions()`; search is a third consumer of the same pool.

## 2. What the measurements say

The roadmap framed this as *"the first cctranscript operation that reads **every**
file rather than resolving one"*, and treated that as the item's main cost risk.
That is directionally right and quantitatively pessimistic.

| Measurement | Result | Bearing |
|---|---|---|
| Read every live log, no parsing (I/O floor) | **≈2.0–2.6 s** | this is the whole budget |
| Read + `indexOf` per line, parse only hit lines | **2.0 s** | prefiltering is **free** over the I/O floor |
| Read + `JSON.parse` every line (174k lines) | **5.9 s** | naive parsing triples the cost for nothing |
| Case-insensitive via `text.toLowerCase()` | **4.3 s** | ❌ allocating a lowercased 500 MB copy |
| Case-insensitive via `/term/i.test(text)` | **1.8 s** | ✅ free — V8 matches without a copy |
| Same, decoding bytes as latin1 instead of UTF-8 | 0.9 s | ✋ fast and **wrong** — see §6 |
| Archive: gunzip + scan all 860 mirrors | **5.2 s** | archive search costs ≈2.5× live |
| Archive mirrors currently iCloud-evicted | **0 of 860** | today's snapshot, not a guarantee (§8) |

**The finding that matters most: search is I/O-bound, not parse-bound.** Every
byte must be read to know whether it matches, and reading is ≈2 s; everything
else is noise *if* the implementation prefilters on the raw line and parses only
the lines that survive. That inverts the obvious implementation — walk lines,
`JSON.parse`, inspect fields — which costs 5.9 s to reach the same answer.

**The second finding: the searchable text is a tiny fraction of the bytes.**

| Layer | Size | Share of raw |
|---|---:|---:|
| Prompts (`you`) | 6.3 MB | 1.3% |
| Replies (`claude`) | 6.4 MB | 1.3% |
| Thinking | **0.0 MB** | **0.0%** — see §5 |
| Tool-call inputs | 33.1 MB | 6.6% |
| Tool results | 124.2 MB | 24.8% |

The default view — prompts and replies — is **12.8 MB of 500 MB (2.6%)**. So the
cost of search is dominated entirely by *finding* the text, never by matching it,
and widening the search with `--tools` changes the runtime by nothing
measurable. This has a design consequence beyond performance, in §5.

## 3. The surface

```
  --search <term>       Find turns matching <term>; prints an index of hits.
  --regex               Treat <term> as a regular expression (default: literal).
  --case                Match case-sensitively (default: insensitive).
  --materialise         Also search iCloud-evicted archive mirrors (see §8).
  --since / --until     Narrow to a date range (see §9).
```

Everything else is **reused verbatim**, which was the roadmap's instruction and
survives scrutiny: `--repo <name>`, `--all`, `--from-archive`/`--dest`, `--tools`,
`--full`, `--json`, `--utc`, `--width`, `--color`. `--search` joins
`OWN_WITH_VALUE` so its term is never mistaken for the positional session.

**Naming.** `--search` is imperative, and the standing preference is for flags
that read as what they *select* (`--from-archive`, not `--archive`). That rule
targets a specific failure — ambiguity about the **direction of the action**,
where `--archive` could plausibly mean "write one" or "read one". `--search
<term>` carries no such ambiguity: the value is manifestly the thing looked for,
never a target acted upon, and it occupies the same mode slot as `--list`.
Weighed against `--matching` / `--containing`, `--search` is also the word Mike
used when asking. **Recommendation: `--search`.** Named here so the departure is
deliberate rather than accidental.

**Interaction with `--list`.** Search *is* a list, narrowed — `--search` implies
list-shaped output, so passing both is redundant rather than contradictory and
should be accepted silently. Passing a positional session with `--search` narrows
the sweep to that one session, which is the cheap and obvious way to grep inside
a transcript you already have open.

**Known wart, documented rather than fixed:** `-n/--last <k>` is already ignored
in `--list` mode (`runList` never reads `lastK`), and will be ignored in search
mode for the same reason — the mode returns a set, not a pick. Making `-n` mean
"the k-th *hit*" would give one word two meanings, which is worse than the
current silence. Worth a `NOTES` line in the man page.

## 4. Match unit and excerpt

**Match at turn grain; display a bounded excerpt.** The roadmap reached this
tentatively; the size distribution settles it, and more sharply than expected:

| Layer | n | median | p90 | p99 | max |
|---|---:|---:|---:|---:|---:|
| Prompt | 2,778 | 242 | 2,869 | 16,373 | **847,646** |
| Reply | 18,072 | 134 | 990 | 3,197 | 8,279 |
| Tool result | 40,664 | 1,306 | 7,523 | 29,894 | **680,187** |

The roadmap's worry was *"a hit inside a 3,000-line tool result is not a turn you
want printed"*. True — but the stronger finding is that **no layer is safe to
print whole**. Replies are genuinely small (max 8 KB), yet a single *prompt*
reaches 848 KB, because a pasted blob is a prompt. So excerpting is unconditional
and applies to every layer, rather than being a special case for tool output.

- One row per **matching turn**, not per match. A turn with three hits shows the
  first hit's excerpt and a `(3 hits)` count — rows stay proportional to turns
  rather than to term frequency.
- The excerpt is a **single line**, whitespace collapsed, centred on the match,
  budgeted against the resolved width (`TW`) with `…` on each truncated side.
  This reuses the existing 70-character first-prompt truncation idea, widened
  because context around the term is the point.
- Every row carries the citable **`N.M` reference** for the turn — and this is
  free, because the refs are already computed and, crucially, **gate-invariant**:
  `numberTurns` numbers only `you` (N) and `claude` (N.M) turns, both of which
  are collected regardless of `--tools`/`--think`. So a ref printed by a search
  run means the identical thing when you reopen the session with default flags.
  A hit in a tool call or result has no ref of its own; it reports the enclosing
  exchange's `N` plus a layer tag, which is the honest answer.

## 5. What is searched by default — and the layer that no longer exists

The roadmap asked whether the default should be prompts and replies only, or also
thinking and tool results, and proposed *"what the current view shows"* with the
existing gates widening the search the same way they widen the render. **That
default holds.** One vocabulary, not two: `--tools` widens both, `--full` widens
both.

🔎 **But the thinking half of the question is void, and this is a finding about
the existing tool, not only about search.** Across the whole live store there are
**24,856 thinking blocks, of which 9 carry any text** — and all nine fall between
2026-06-05 and 2026-07-04. Every block since carries a `signature` and no
content: the harness stopped writing thinking text to the log. Confirmed
behaviourally as well as by census — `cctranscript --think` renders no thinking
turns on current sessions, because `readTurns` gates on `(b.thinking || '').trim()`
and there is nothing to trim.

So: **`--think` cannot widen a search, because there is nothing to widen it to.**
The design does not add a thinking layer, and the man page should state the
limit plainly rather than leaving a flag that silently does nothing. (Whether
`--think` itself should now say so on every run is a separate question, raised in
§12 — it is a defect in the *existing* tool that this pass merely found.)

**The tool-output default, and how the omission is made loud.** The roadmap's
sharpest warning was that *"a search that silently skips tool output will be
quietly wrong the first time someone greps for a filename"*. That risk is real —
filenames live in tool inputs and results, which are 31% of the corpus. The
resolution is not to widen the default (that would bury prompts and replies under
40,664 tool results), but to make the boundary **impossible to mistake**, and the
measurement makes this cheap in a way it wouldn't normally be:

> Because the scan reads every byte of every file regardless, a whole-file
> `test()` against the unsearched layers costs **nothing extra**. So a run that
> finds nothing can say *"0 hits in prompts and replies — the term appears in 12
> sessions' tool output; add `--tools` to search it"*, and a run that finds some
> can footnote the same. The tool reports what it did **not** look at, every
> time, rather than leaving the user to infer it.

This is the estate's no-silent-caps rule applied at the point of use: the summary
line always names the layers searched, and the unsearched layers are reported as
a count rather than as silence.

## 6. Regex or plain, and how the user says which

**Literal by default; `--regex` opts into a pattern.** The roadmap's grounds hold
and need no elaboration: a path with a `.` in it must not silently become a
wildcard, and inferring intent from the string's shape is guessing. A literal
term is compiled to a regex internally with the metacharacters escaped, so both
paths share one matcher.

**Case-insensitive by default; `--case` opts into sensitivity.** People search
for `worktree`, not `Worktree`. The measurement decides *how*, and the obvious
implementation is the wrong one: `text.toLowerCase()` costs **4.3 s** (it
allocates a second 500 MB string), while `/term/i.test(text)` costs **1.8 s** —
free, because V8 folds case inside the matcher without copying.

🛑 **One fast option is rejected on correctness, and it matters here
specifically.** Decoding the file bytes as latin1 rather than UTF-8 halves the
scan to 0.9 s, because it skips UTF-8 decoding entirely. It also breaks every
non-ASCII search — a search for `Māori` would not match its own repo's
conventions doc. This estate writes macrons on te reo Māori by standing
convention, so the one shortcut that measurably pays is the one that quietly
fails on the text we most care about getting right. **Rejected; UTF-8
throughout.** Recorded so a future optimisation pass doesn't rediscover the
speed and miss the reason.

## 7. Output shape

An **index of hits, grouped by session**, ordered most-recent-session-first
(matching `--list`) and chronological within a session:

```
  a1b2c3d4  2026-07-26 14:22  [atelier]
     3.2  claude   …the --materialise asymmetry is deliberate, not a gap…
     7.1  claude   …no bulk-read operation for --materialise to name…   (2 hits)
     9    tool     Bash  grep -n 'materialise' instruments/README.md

  9f8e7d6c  2026-07-23 09:14  [ros]
    12.4  you      …should materialise stay opt-in when the archive…

  4 hits in 2 sessions · searched prompts+replies · 440 sessions swept in 2.1 s
  Term also appears in 12 sessions' tool output (add --tools).
```

`--json` carries the same structure — an array of sessions each holding an array
of hits (`ref`, `role`, `timestamp`, `excerpt`, `hits`), plus a `meta` block
naming the layers searched, the sessions swept, and any skipped for eviction.
This mirrors ccrepo's precedent of the machine format being *wider* than the
table rather than a different shape.

**No default result cap, deliberately.** A broad term will emit thousands of
rows. The temptation is a default limit, but there is no grounded basis for a
number — picking one from today's corpus size is exactly the fitted-threshold
failure the estate's own rule forbids, and a silent truncation reads as "that's
all there is". `--top <n>` is available for those who want it (same word as
ccrepo, same operation — truncating a ranked list), the grouping keeps long
output scannable, and a pager or `head` handles the rest. Honest and unbounded
beats arbitrary and quiet.

## 8. Eviction and `--materialise` — settled by doctrine, not open

The roadmap flagged this as the item's one doctrinal loose end: `instruments/README.md`
justifies cctranscript having **no** `--materialise` flag on the explicit grounds
that *"`cctranscript` never reads every file"* — and search makes that
justification stale, so the note *"has to be revisited in the same change, not
afterwards"*.

Revisited, the answer is not a judgement call. **Flags-follow-operation** (ratified
by Mike, 2026-07-23) says vocabulary is uniform whenever the operation is shared,
and a flag is added when the tool genuinely performs the operation it names.
Search *is* the bulk read. So cctranscript acquires `--materialise` with exactly
ccarchive's and ccrepo's meaning, and the README's asymmetry note is rewritten in
the same commit — from "cctranscript has no bulk-read operation" to "cctranscript
had none until `--search`, which is why it now carries the flag". The note keeps
its role as the worked example of the rule; the example simply gains its second
act, where the operation appeared and the word followed it.

Behaviour, matching the two siblings:

- Evicted mirrors are **skipped by default** and **counted in the summary** —
  *"3 mirrors not searched (evicted); `--materialise` reads them"*. A skipped
  file is never silently absent from a result set that claims completeness.
- `--materialise` faults the bytes back, with the cost owned by the user who
  asked for it.
- `isDataless()` already exists in cctranscript (ported from ccarchive for the
  `--list` path), so this is a reuse, not a new mechanism.

Measured today: **0 of 860 mirrors are evicted**, so the flag would currently
change nothing. That is a snapshot of one machine on one day and no basis for
skipping the work — iCloud's Optimise Storage evicts on pressure, and the design
must be correct on the day it does.

## 9. `--since` / `--until` — yes, and the semantics must match exactly

The roadmap asked whether ccrepo's `--since`/`--until` should join cctranscript's
scoping vocabulary, noting flags-follow-operation answers yes only if the
operation is genuinely shared. **It is now, and it wasn't before.** Resolving one
session made a date range meaningless (`-n k` was the whole selector); narrowing
a *set* before sweeping it is precisely ccrepo's operation. Same word, same
meaning.

One trap to avoid, because it would make the same flag mean two things:

- ccrepo filters on **message timestamps**. cctranscript's `sessionRecord` has
  `mtime`, which is last-activity, not per-message.
- Filtering candidate files on mtime alone would therefore *drift* from ccrepo's
  semantics. Instead: use mtime only as a **safe skip** for `--since` (a file
  whose last activity precedes the window cannot contain a message inside it),
  and then filter the **hits themselves** by their own turn timestamp for both
  bounds. The result is identical to ccrepo's meaning, and the cheap prefilter is
  a pure optimisation that can never change the answer.
- `--until` gets no mtime skip — a long session can start before the bound and
  end after it. Stated because the asymmetry looks like an oversight otherwise.

## 10. Implementation sketch

The shape follows from §2 and is deliberately small:

1. `pickSessions()` unchanged — it already yields the scoped pool.
2. Apply the `--since` mtime skip (§9).
3. Per file: read once (gunzipping in archive mode via the existing
   `readLogText`); run the whole-file `test()` — miss means skip the file
   entirely, and also feeds the unsearched-layer report of §5.
4. On a hit, split to lines and `test()` each raw line; `JSON.parse` **only** the
   lines that survive. This is the step that keeps the run at the I/O floor.
5. Reuse `readTurns`-equivalent extraction on the parsed lines to get role, text
   and timestamp; number refs with `numberTurns` over the session's `you`/`claude`
   turns.
6. Excerpt, group, print.

Step 4 is the one place the implementation must resist the obvious. A note in the
code should say why, or a later tidy-up will "simplify" it into the 5.9 s version.

## 11. What DONE looks like — testable conditions

- [ ] `--search` with a literal term containing `.`, `*` and `[` matches those
      characters literally and finds a real path in the corpus.
- [ ] `--regex` with the same string matches as a pattern; the two disagree, and
      a test asserts they disagree.
- [ ] Default matching is case-insensitive; `--case` narrows the result set on a
      term that differs only in case.
- [ ] A search for a non-ASCII term with a macron matches a turn containing it.
- [ ] A hit's printed `N.M` ref resolves to the same turn when the session is
      reopened with **default** flags (the gate-invariance claim of §4, asserted
      not assumed).
- [ ] A turn matching three times yields one row with a hit count of 3.
- [ ] An 800 KB prompt containing the term yields a bounded single-line excerpt.
- [ ] With tool layers unsearched, a term present only in tool output yields zero
      hits **and** a report naming the count of sessions whose tool output holds
      it; `--tools` then finds them.
- [ ] `--think` does not widen the search, and the man page says why.
- [ ] An evicted mirror is skipped, counted in the summary, and read under
      `--materialise` (via `CCARCHIVE_SIMULATE_DATALESS`, the existing test seam).
- [ ] `--since`/`--until` filter on turn timestamps, and a session spanning the
      `--until` bound returns only its in-window hits.
- [ ] `--json` carries hits, refs and the `meta` block including skipped counts.
- [ ] A full-corpus literal search completes within the I/O floor — no more than
      ≈1.5× a bare read of the same files (the regression guard for step 4).
- [ ] `instruments/README.md`'s `--materialise` note is rewritten **in the same
      commit** as the flag lands (§8), and the vocabulary table gains the row.
- [ ] `man/cctranscript.1` gains `--search` with `EXAMPLES` and the `NOTES` lines
      on thinking, on `-n` being inert, and on the unsearched-layer report.

## 12. Raised, not solved — for the roadmap

- **`--think` is a flag that no longer does anything** on current logs (§5). Not
  this item's to fix, but it should not sit undocumented now that it's known.
  Options range from a `NOTES` line to printing a one-line notice when `--think`
  is passed and no thinking text exists in the log.
- **Subagent logs are not searchable.** There are **417** of them live, and
  ccarchive mirrors them, but `allSessions()` walks one directory level so they
  are outside the pool. "Where did the agent find X" is a plausible question and
  this design does not answer it. Deferred rather than smuggled in: a subagent
  log has no identity in the `--repo`/session vocabulary yet, and inventing one
  is a larger change than a search flag. A `--agents` widening is the obvious
  shape if it's wanted.

## 13. Deferred / out of scope

- **An index or cache.** A full live sweep is ≈2 s and an archive sweep ≈5 s. An
  index would trade that for staleness, invalidation and a second store to keep
  honest — a poor trade at this corpus size. Revisit only if the corpus grows an
  order of magnitude; the number to watch is the sweep time, not the file count.
- **Relevance ranking.** Results are chronological. Ranking implies a scoring
  model, which implies tuning, on a corpus where recency is already the strongest
  signal you have.
- **Multi-term boolean queries** (`A AND B`, `A NEAR B`). `--regex` covers the
  realistic cases; a query language is a different product.
- **Searching `history.jsonl`** (the typed-prompt stream ccarchive captures under
  `_external/`). Different grain — keystrokes, not turns — and it has no session
  identity to index a hit against.

## 14. Review posture

This pass is **records-only** and authors no doctrine, so nothing is queued now.
Review is **WARRANTED when it moves from design to build**: the build edits
`instruments/README.md`'s flag-vocabulary note, which is the worked example of a
ratified rule (§8), and that is a doctrine-adjacent change even though the rule
itself is only being *applied*. Same posture as the ccarchive encryption design
pass took, for the same reason.
