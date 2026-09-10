- [ ] **REPORT — two secretscan defects: the entropy net scores a published
      URL's path segments as a credential, and `--staged` reports the wrong
      line number for any path containing a space** `[S][tools]` — filed from
      a private child, 2026-09-10, via § *Pointing up*. Evidence available.

      Both were measured in one session while committing a generated document.
      They are unrelated in cause and are filed together only because one
      masked the other: the wrong line number sent the investigating session
      to an unrelated stylesheet rule, and the real finding was 765 lines away.

      ## Defect 1 — a published URL is not a credential

      The `high-entropy` rule evaluates tokens without regard to whether they
      sit inside a URL. A documentation link's path segments score well above
      the threshold:

      | Token shape | Length | Entropy |
      |---|---:|---:|
      | a vendor guide's nested path ending in a hyphenated page name | 61 | **4.7** |
      | a full `https://` documentation URL | 80 | 4.66 |
      | a government publication's dated upload path | 80 | 4.52 |

      **This blocks the commit outright**, at `medium` severity with
      `response: block`.

      🛑 **Why it matters beyond one commit.** It fires on any document that
      cites its sources — which is the shape of every rigorous document a child
      repo produces. The better a document's provenance, the more certainly it
      blocks. In the reporting case the trigger was a **sources table**, added
      precisely to make claims checkable.

      ⚠️ **And the suppressions available are all the wrong width.** The line
      marker cannot be used because the artefact is **generated** — a marker
      written into it is destroyed on the next render — which is the same seam
      `320/140` already reports from another direction. That leaves the file
      glob, which stops scanning a whole document; and this house's own
      `.secretscanignore` conventions argue at length that reaching for a glob
      first hides the thing the glob was supposed to be safe around.

      **What the child did meanwhile**, offered so the workaround is visible
      rather than silent: the renderer now appends a `secretscan:allow` marker
      to a generated line carrying **two or more external links**, with the
      cost declared in its docstring — it exempts one line, so a credential in
      a table that also carries two external links would pass unseen. That is
      narrower than a glob and it is still a workaround, not a fix.

      **Suggested shape, offered as a suggestion and not a design.** Exclude a
      token that is a path segment of a URL, or that is preceded by a scheme
      within the same token run. A credential pasted into a query string would
      still be caught by the assigned-value rules, which are the
      high-confidence ones and are unaffected.

      ## Defect 2 — `--staged` mis-locates a finding when the path has a space

      With a staged file whose name contains a space, `secretscan --staged
      --json` returns a path with a **trailing tab** and a line number that is
      not the finding's line:

      ```
      "path": "some/dir/01 Report.html\t",   "line": 230
      ```

      Scanning the same file directly — `secretscan <path>` — reports the same
      single finding at **line 995**. Line 230 in that file is a stylesheet
      rule containing nothing resembling a secret.

      The trailing tab points at the cause: git's `--stat`/name output is being
      split on whitespace, so a filename containing a space is truncated and
      the remainder is misread. The truncated name apparently still resolves
      far enough to scan *something*, which is why this presents as a wrong
      line rather than as an error.

      ⚠️ **The cost is a session sent to the wrong evidence.** A blocked commit
      is a stop-and-investigate event; the tool names a location, and the
      location is wrong. Here that produced a detour of several minutes and a
      false conclusion — that the finding was in generated CSS — before the
      direct scan corrected it. A file with a space in its name is ordinary in
      any repo that generates documents for people to read.

      ## What is NOT being asked

      No change to the blocking behaviour of either rule is proposed. Defect 1
      is about which tokens the net should consider; defect 2 is a parsing bug.
      Consideration and remediation are the house's.
