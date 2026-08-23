# 🔇 Silence read as an answer — 2026-08-24

A sibling to [`370`](../370-the-report-can-lie-while-the-work-is-fine/README.md),
and deliberately **not** filed as another instance of it, because the remedy that
works there does not work here.

`370` is about a tool's **report** being corrupted while its work is fine — a
heredoc eating stdin, a script overwritten mid-run, a renderer doubling a sigil.
Every one of those is caught by *re-reading the report against the artefacts*,
which is exactly what `370/010` recommends.

**This is the case where there is no report to re-read.** A call fails, returns
nothing, and the nothing is consumed as data. The failure and the empty result
are byte-identical at the point of use, and no amount of care in reading the
output distinguishes them, because the output is the same in both worlds.

## The instance, from docker-heap on one night — two sessions, independently

Both were auditing which ZFS datasets carry snapshots. Both used the TrueNAS
middleware. Both wrote `2>/dev/null` and checked no exit code.

```sh
midclt call zfs.snapshot.query '[["dataset","~","wakatipu"]]' 2>/dev/null   # -> ""
```

Read as *"no snapshots exist"*. Re-run with stderr visible: `exit=1`,
`stdout_bytes=0`, stderr `Call timeout`. The middleware call had **timed out**.
It was not answering the question at all.

🔑 **And the conclusion drawn from it happened to be correct**, which is the part
that makes this worth a doctrine item rather than a bug report. The dataset
genuinely has no snapshots. Nothing downstream broke. Both sessions were an
inch from carrying a load-bearing claim on an instrument that had never looked.

## What catches it, and it is one line

**A positive control: ask the instrument to display a state you already know is
there, before you trust it to tell you a state is absent.**

```
taupo/media   (known to hold snapshots)  ->  198        # instrument works
taupo/wakatipu                            ->  0         # measured absence
```

Run against the same instrument, same session, same syntax. Without the first
line, the second line is indistinguishable from a broken tool. With it, the zero
is a measurement.

The same query against `taupo/media` — 198 snapshots — *also* returned nothing,
so one control line would have exposed it immediately.

## Why this is not just "check your exit codes"

That rule is true, and it is not sufficient, for three reasons found the same
night:

- **An exit code can be 0 and the answer still empty for the wrong reason.** The
  second session's query used a *substring* operator against a dataset name that
  a **separate pool** also carries. Anchored wrong, exit 0, honest tool, wrong
  question — and it failed toward *false reassurance*: "snapshots exist, you are
  protected."
- **The shell hides it structurally.** `x=$(cmd)` inside a larger pipeline, a
  `$(...)` in a `printf`, a value read into an `if` — none of these surface a
  non-zero status without deliberate work, and `2>/dev/null` is written
  reflexively to keep output clean.
- **It generalises past exit codes entirely.** A verification whose filter can
  only match the *broken* form of a value; a comparison that treats an absent
  file and an identical file the same; a guard matching a name convention the
  other copy does not use. None involves an exit code. All are the same defect:
  **the instrument cannot display the state it exists to detect.**

## The candidate rule

> **Before an instrument's negative result is allowed to carry weight, make it
> show you a positive.** Where the result will authorise something irreversible,
> that control is not optional.

Narrow on purpose. It is not "distrust your tools" — it is one cheap extra call,
against a known-present case, using the same instrument in the same run.
