# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-ccapple-filter-first-cold.md` (`REVIEW.md` rule 1). Written
2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta. Open this
only after act 1 is committed. Everything here is a floor, never a fence, and none of it is a
finding.

## The brief-writer's own questions

1. `check_filters` and each search function now spell the flag list twice. What keeps the two in
step when a flag is added (V4)? Is there a subcommand or a flag that one has and the other lacks
today?
2. Does `any(value for _, value in flags)` agree with the old per-function tests on every falsy
value a caller can pass, including `--near` with a zero-like value and the empty string?
3. The `--limit < 1` check sits before `check_filters`, and `doctor`-style paths return earlier
still: map every path through `main()` before the gate and say whether any touches a store.
4. The changelog's "121 cases" is the whole module's count. Does the sentence claim more than the
two tests the delta added?
5. `assertNotIn("store", err)` is a substring test on a word that a flag or subcommand name could
later carry. Is it pinning the behaviour or the wording?

## What the brief-writer ran, and what it got

- `test_ccapple`: /usr/bin/python3 3.9: 121 tests OK, exit 0, about 15 s.
- `exit2`: all seven subcommands exit 2 under an empty HOME, each message naming the filters it
  needs, no traceback (3.9).
- `exit1`: exit 1, message `cannot read store` (3.9).
