# Session records

One file per working session, named for the time the session started:
`YYYY-MM-DD-HHMM-slug.md`, the time in UTC (the house doctrine's RECORD.md,
§ *The session log*). The folder is the index. The names sort by start time,
so a session getting its bearings reads the newest few files, for example the
ones `ls docs/sessions/[0-9]* | tail -5` lists, and opens older ones only when
it needs them. Some older names carry a two-digit counter where the time
would be (`YYYY-MM-DD-NN-slug.md`). This README is the only file here that is
not a session record.

<!-- archivecut:retired-log-below -->

## The retired one-file session log

This repo once kept a one-file session log beside this folder as well. It
was retired by atelier's `archivecut.py`: each of its entries now sits, word
for word, near the top of the session file it linked, or in a new file named
for its date where it linked none, under the line "From the retired session
log". Below is the rest of that file, word for word: its preamble and
anything else that was not an entry, inside fences so that it is read as a
record and nothing acts on it. The comment lines carry its line numbers, so
`archivecut.py --verify` can rebuild the file from this folder byte for byte.

### `docs/SESSIONS.md`, retired

<!-- archivecut:retired docs/SESSIONS.md lines=371 final-newline=yes last=144f498c -->

<!-- archivecut:log-text docs/SESSIONS.md 1+21 -->
````
# atelier — session log (index)

<!-- indexscan:maps dir=sessions match=*.md -->
<!-- indexscan:allow: 2026-07-22-0245-interruption-resilience-doctrine.md a records-only design capture, not a session; reached from the board. Added 2026-10-05 by session 5e3f68f1 (agent, queue run, on indexscan's first run; not a ruling) -->
<!-- indexscan:allow: 2026-07-22-1025-security-canon-gap-map.md a records-only capture, linked from the 2026-07-22-1018 queue run's detail file and its board section. Added 2026-10-05 by session 5e3f68f1 (agent, queue run, on indexscan's first run; not a ruling) -->
<!-- indexscan:allow: 2026-07-22-1036-invariant-candidates.md the mining record behind board section 200, linked from that section's README; a capture, not a session. Added 2026-10-05 by session 5e3f68f1 (agent, queue run, on indexscan's first run; not a ruling) -->
<!-- indexscan:allow: 2026-07-22-1050-cc-instruments-questions.md an analysis capture linked from board section 210's README and the changelog; not a session. Added 2026-10-05 by session 5e3f68f1 (agent, queue run, on indexscan's first run; not a ruling) -->
<!-- indexscan:allow: 2026-07-22-1233-person-context-portability-design.md a records-only design capture, linked from the 2026-07-22-1210 queue run's detail file and board item 240/010. Added 2026-10-05 by session 5e3f68f1 (agent, queue run, on indexscan's first run; not a ruling) -->
<!-- indexscan:allow: 2026-07-28-0244-c1-advisory-schema.md a phase record reached from ROADMAP-DONE; its session predates a one-line-per-session discipline for side records. Added 2026-10-05 by session 5e3f68f1 (agent, queue run, on indexscan's first run; not a ruling) -->
<!-- indexscan:allow: 2026-08-03-2050-leakscan-pii-sweep.md a sweep capture linked from board item 160/110 and section 020's README; not a session. Added 2026-10-05 by session 5e3f68f1 (agent, queue run, on indexscan's first run; not a ruling) -->
<!-- indexscan:allow: 2026-10-03-0357-ruling-round-agenda.md a deliverable of the 2026-10-03-0153 session, linked from that session's detail file. Added 2026-10-05 by session 5e3f68f1 (agent, queue run, on indexscan's first run; not a ruling) -->
<!-- indexscan:allow: 2026-10-03-0357-ruling-round-agenda-board-inventory.md an inventory annexed to the ruling-round agenda, linked from it. Added 2026-10-05 by session 5e3f68f1 (agent, queue run, on indexscan's first run; not a ruling) -->
<!-- indexscan:allow: 2026-10-03-0357-ruling-round-agenda-findings-inventory.md an inventory annexed to the ruling-round agenda, linked from it. Added 2026-10-05 by session 5e3f68f1 (agent, queue run, on indexscan's first run; not a ruling) -->

Append-only, newest last; one line per session. Tail-read at session start.
Full detail per session lives in `docs/sessions/<date>-NN-slug.md` — open a
file only when its line needs unpacking (RECORD.md's index/detail split;
restructured to this shape 2026-07-10, entries preserved verbatim in the
detail files).

---
````
