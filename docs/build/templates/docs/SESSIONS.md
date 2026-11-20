# <name> session log (index)

One line per working session, newest LAST. The index is append-only: an entry
is never edited or reordered once written. At session start read the tail
(e.g. `tail -30 docs/SESSIONS.md`); the full history is for grepping. Append an
entry before finishing a session.

Keep each entry to one line. When a session is substantial, put its detail in
`docs/sessions/<YYYY-MM-DD>-<HHMM>-<slug>.md` (`HHMM` in UTC, from `date -u`;
no shared counter) and point at it from the index:

`- [<date> · <HHMM> UTC · <title>](sessions/<file>.md) — <one-line outcome>`

A session with nothing worth a detail file takes a plain line, as below.
atelier's `docs/method/RECORD.md` § *The session log* is the full rule.

- **<YYYY-MM-DD>**: Repo created and scaffolded to the house conventions.
  Next: <the first real task>.
