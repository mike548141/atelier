# 🔐 SHA-2 or better for every hash — Mike-commissioned, 2026-08-22

A house-wide preference, filed here rather than in the repo that surfaced it,
because it applies to every repo and every tool the estate writes.

**His words, verbatim:** *"In general I don't like you using md5, I would prefer
sha2 for basically anything"*, refined a moment later to *"sha2 or better that
is"*.

**What surfaced it.** A `docker-heap` session verified a multi-thousand-file ZFS
dataset migration with `md5sum` before the owner deleted the original copy. The
verification was sound in substance — every file matched — but the primitive was
his to choose and he had not been asked. He asked for it re-run under SHA-256,
which it was, with the same result.

**Why it is a house rule and not a per-case judgement.** The obvious rebuttal —
that MD5 is adequate for detecting accidental corruption, which was the actual
property being relied on — is *true and beside the point*. A weak primitive
written into a verification script gets copied into a context where collision
resistance does matter, and the copy carries no memory of the reasoning that
made it acceptable the first time. The cost of always reaching for SHA-256 is
approximately zero; the cost of the habit is not.
