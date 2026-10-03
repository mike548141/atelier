# The exception register: every guard exception recorded, and narrowed to the string

**Status**: draft. Mike rules on acceptance. • **Date**: 2026-10-03

**Review**: queued. A rule-4 design cold pass is owed before acceptance
(`docs/roadmap/160-doctrine-review-owed/650-…`).

## Context

Mike, 2026-10-03, verbatim. He said he has had to repeat it "many many times",
and it was first asked for on 2026-09-12 (`roadmap/110-…/100`):

> I want any exception to be
> * Specified and recorded so that its clear that the exception exists, why it
> is necessary, who created it (e.g. session transcript ID, did I rule or did
> you do it automatically etc), when the exception was granted, and any other
> relevant and useful info
> * As narrow an exception as possible. I gave the example of a particular
> position in the file or string of characters rather than a whole line in a
> file, or the whole file, or a folder of files.
> For example if every line in a file is secrets then an exception for the file
> makes sense, but if it were one string in the file then only that string
> should be excluded.
> This should be true of binaries, files large and small etc

The part 1 audit (`110/100`, 2026-10-03) measured the gap.
- **26 exception mechanisms.** None records the session or whether Mike
  ruled. One has an expiry.
- **91 live line markers, all whole-line.** 92% are not rule-scoped.
- **33 ignore globs.** About 14 mask a whole file or folder for a handful of
  flagged lines.
- **`GUARDS.md` § *Who, why, when* says who and when "come from version
  control".** But every commit has one author, and `git blame` cannot name a
  session or tell a ruling from an agent's choice. That doctrine contradicts
  the standard, and this ADR replaces it.

## Decision (proposed)

**One register per repo, `.atelier-exceptions.jsonl`.** It holds one JSON object
per line, is append-friendly, and is diffable. Every guard reads it through
`tools/allowmarker.py`. **Every exception lives there.** Inline markers and ignore
globs are migrated into it (part 3) and then retired, so there is one place to
audit and one shape to check.

**Each entry records, and a guard refuses an entry that lacks any required
field:**

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | stable, e.g. `EX-2026-10-03-0641-a1b2` |
| `guard`, `rule` | yes | what it exempts; never "every rule" |
| `path` | yes | one file, or a glob only where the locator says so |
| `locator` | yes | **how narrow.** See below. |
| `why` | yes | the purpose (`REPO-STANDARD.md`'s purpose rule) |
| `granted_by` | yes | `principal-ruled` (with `ruling`, his verbatim words), `principal-answer` (a pick from a session's options), or `agent` (a session's own judgement) |
| `session` | yes | the transcript ID of the session that wrote it (`$CLAUDE_CODE_SESSION_ID`), or `human` |
| `granted` | yes | ISO-8601 UTC |
| `review_by` | for deferments | ISO date. An acceptance may omit it and must say why it never lapses. |
| `notes` | no | anything else useful |

**The locator is the narrowness, from the finest level up.** A guard uses the
finest level that covers the case. A coarser level must state why a finer one
cannot.
1. **`match`**: the SHA-256 of the exact matched string, plus the path. It
   exempts only that string, wherever it sits in that file, and survives lines
   moving. The secret itself is never stored. This is Mike's "string of
   characters".
2. **`span`**: path, line, start column, end column, and a hash of the line
   content. For a finding that is not a single string. It goes stale, and is
   reported, when the line changes.
3. **`line`**: path plus a line-content hash. Only when the whole line is the
   finding.
4. **`file`**: path plus the file's SHA-256. Only when every finding-bearing part
   of the file is exempt, e.g. a fixture file of fake secrets. **For binaries,
   this is G3's entry.** A changed file re-blocks.
5. **`glob`**: a path pattern. Only for a generated or store class where every
   file qualifies, and it must name the class.

**Guards report it.** Each run prints, per guard: the entries applied, the
entries that matched nothing (stale, which blocks like G3's stale entry), and the
entries that are coarser than the findings they cover. That last is the
"narrower one would do" check, made mechanical.

**A helper writes entries:** `tools/exception.py add --guard … --rule … --path …
--match-from-finding <finding-id> --why …`. It fills in `session`, `granted`
and `granted_by: agent` automatically. `principal-ruled` requires `--ruling
"<his words>"`. A session can never mark its own choice as his.

**Streaming is unchanged.** The register is read once per run into an index
keyed by (guard, rule, path). It holds no file content and is bounded by its
own size. Lookup is per finding, so no guard holds more.

## Rejected

- **Richer inline markers** (`x:allow:rule@col12-40#who#when`). They can't
  hold a session ID and a ruling quote without unreadable lines. They can't
  live inside a binary or JSON. And they scatter the audit across the tree.
- **Keep ignore files and add fields to them.** Two homes for one concept, and
  globs cannot express a string.
- **Rely on git for who and when.** It is measured to be unable to name a
  session or a ruling (part 1).

## Consequences

- Part 3 migrates atelier's 91 markers and 33 globs. Most become `match`
  entries, and the over-wide globs become per-string entries. Each child migrates
  at its pin bump.
- G3 (PR #97) is reworked onto this register as `file` entries, with an
  optional `match` for a metadata segment.
- `GUARDS.md` § *Who, why, when* and § *Granularity* are rewritten to point here
  (a character-span rung is added).
- **Open for Mike:** whether existing exceptions with no provenance migrate as
  `granted_by: unknown`, with a review-by forcing someone to look. The
  recommendation is yes, rather than inventing provenance.
