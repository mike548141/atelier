- [x] **licenscan gap — map known PyPI trove classifiers to SPDX ids.**
      (claimed 2026-08-05-1243, wt: queue-batch-0806)
      `"License :: OSI Approved :: Apache Software License"` is the **correct**
      PyPI trove classifier for Apache-2.0 — established packaging practice, not
      an error — but licenscan reads it as an unrecognised declaration and blocks.

      **Evidence (2026-07-25).** One child hit this with a `pyproject.toml` that
      *already* carried a correct SPDX `license` field; the classifier beside it
      was flagged anyway. Marked in place with the reason, because the repo was
      right and the tool was wrong.

      **Why it matters beyond one repo.** Every Python package in the estate will
      carry these classifiers, so this recurs by construction — and each recurrence
      trains someone to reach for an allow-marker on a *correct* line, which is
      how a scanner's findings stop being believed.

      **Fix shape.** A small lookup from the OSI-approved trove classifier strings
      to their SPDX ids, applied before the unrecognised-declaration check. The
      set is small, stable and published. Where a classifier is genuinely
      ambiguous (a family name covering several versions), degrade to the existing
      unknown-declaration *warn* rather than guessing a version — friction, never
      a silent pass. **Test to write with it:** the Apache trove classifier
      alongside an Apache-2.0 `license` field reports clean.
