- [ ] 🔎 **Drive binaries have the gap `ccmail` just closed for mail** (found
  2026-09-09, while building `ccmail`). The Google Drive connector's
  `download_file_content` returns a file **as a base64 string into the context
  window**. For a Google-native doc that is fine, and `read_file_content` covers
  it better still with a natural-language rendering. For a **binary** — a PDF, a
  scan, an image, a spreadsheet export — base64-into-context is the same failure
  `ccmail` was built to end: the bytes are reachable in principle and unusable in
  practice, and a multi-megabyte file would swamp the window it arrived in.
  **Evidence grade — read, not measured.** This is taken from the tool's own
  stated contract ("download the content of a Drive file as a base64 encoded
  string"), not from a run. It was deliberately **not** probed: confirming it
  means pulling a real binary into a real context window, which is the very cost
  the finding is about. Whoever takes this should measure it on a small file
  first, and record the true threshold rather than inheriting this estimate.
  🤔 **The open question is shape, not need.** `ccmail` already owns the pattern —
  authenticate narrowly, write to disk outside every repo, return a path, never
  the content — so the options are (a) a `--drive` mode on `ccmail`, which reuses
  the credential store and the work-tree guard but stretches a name that says
  *mail*, (b) a sibling instrument sharing the same internals, or (c) nothing,
  on the grounds that the connector's `read_file_content` already covers the
  documents anyone actually asks about and binaries in Drive are rare enough to
  handle by hand. Not decided here; (c) is a real answer and should not be
  assumed away.
  ⚠️ **Scope note:** the same shape may reach any connector that returns file
  content inline. Drive is the one observed; a sweep of the others has **not**
  been done, so treat this item as one instance, not the class.
