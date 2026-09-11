- [ ] 🔎 **Why *is* the source smaller than the archived copy? — the shrink
  guard's premise has never been checked** (Mike filed 2026-09-11 from a live
  `ccarchive` run; investigate-only, no fix attached)

  **What he asked.** *"I'm glad that it has this safety guard because that is a
  sensible action. But I'm not sure why the source transcript is smaller than
  the one in the archive… is it matching two different transcripts incorrectly,
  is something mutating the source or archived transcript etc.."*

  **The observation.** A hand run refused **six** files and exited non-zero.
  Every one is a per-project memory `.md`; two of them are a project's memory
  index. Paths are deliberately not named here — they identify personal
  projects and private repos, and this repo is public (same care as
  [`210/010`](010-ccarchive-exits-1-on-every-scheduled-run-and-t.md)). The
  count was **two** when `210/010` was filed on 2026-08-09, so the class is
  growing, not static.

  ## 🤔 Why this is a separate item from `210/010`

  `210/010` asks what to do about the class, and its three options all assume
  the shrink is **real and legitimate** — whole documents rewritten smaller. It
  asserted that reading ("legitimately condensed") without ever diffing a source
  against its mirror. This item asks the prior question: **is the refusal
  telling the truth about what it compared?** If the pairing or the recorded
  size is wrong, `210/010`'s options are answers to a question that does not
  exist. Take this one first.

  ## 🔎 What the code actually compares — and it is not what the message says

  Read read-only at filing, `instruments/ccarchive`:

  - The guard fires only when a source is **both** newer than the mirror
    (`shouldArchive`) **and** smaller than `manifest[rel].rawBytes`
    (`isSuspectShrink`).
  - So the comparand is the **manifest's recorded byte count**, not the bytes
    sitting in the mirror. The stderr line says *"smaller than the archived
    copy"*, which is a claim about the mirror. Those are the same number only
    while the manifest and the mirror agree — that agreement is assumed, never
    verified on this path. This is the shape
    [`370`](../370-the-report-can-lie-while-the-work-is-fine/) names: the
    message can be wrong about its own evidence while the refusal is still the
    right call.
  - Pairing is by one relative path `rel`, used to locate both the mirror
    (`destRoot/rel.gz`) and the manifest entry, so a mis-pair needs two distinct
    sources normalising to the same `rel`, or a manifest key left behind by a
    renamed project directory. The layout-drift alarm does not cover that: it
    trips only when the walk yields **zero** sources against a non-empty
    manifest, so a *partial* rename passes silently.

  ## 📋 Hypotheses to discriminate, cheapest first

  1. **Benign condensation** — the mirror holds an older, longer revision of the
     same document. Confirm by decompressing the mirror and diffing against the
     source: same document, earlier state.
  2. **Manifest/mirror divergence** — `rawBytes` belongs to a different revision
     than the mirror actually holds. Check the recorded `sha256` against the
     mirror's decompressed content, and `rawBytes` against both real sizes.
  3. **Wrong pairing** — the source and the mirror are different documents.
     Falls out of (1)'s diff immediately, and would be the serious result.
  4. **Something mutating a copy after write** — either end changing outside the
     archive run. Distinguishable by mtimes and by whether the mirror still
     hashes to its manifest entry.

  All four are answerable read-only, without `--force` and without touching the
  archive. **Do not clear the red first** — a `--force` run overwrites the
  frozen mirrors and destroys the only evidence that separates these cases.

  ⚠️ **Record the result as a class, not as content.** The diffs will hold
  personal memory text; what comes back here is which hypothesis held and what
  the guard should therefore compare. The finding, not the file.
