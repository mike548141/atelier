# 2026-08-21 · 2312 UTC · Three channels, and the instrument that reads one

**Tier:** Opus 5 (1M). **Worktree:** `three-channel-findings-0822`.
**Commission:** Mike, mid-turn — *"If there are any review briefs to write do
those as well"* — plus a question he routed here through a `cbom` session:
*"pass that question to atelier for it to look into"*, after telling that
session *"Suggest it to atelier repo for doctrine + guards"*.

The mid-turn arrival is not incidental. It is the exact channel this session
then spent its time proving invisible.

## The briefs: none written, and that was Mike's call

Queue state at the moment it was read: six `⏳` pointers, four already run
(`160/080` closed, `160/090`, `160/260` and `300/040` open past their passes),
and **two brief-less** — `310/050` (the pointing-up route) and `160/270` (this
session's own doctrine, landed 2026-08-19). No unrun brief was waiting.

⚠️ **That reading went stale while the question was with Mike, and the record
says so rather than reading as though it hadn't.** A parallel session wrote
`310/050`'s brief and stopped on it — `reviews/2026-08-21-0820-pointing-up-cold.md`,
merged as PR #40 — so by the time this worktree was cut there was **one**
brief-less pointer, not two, and one unrun brief waiting for a Fable reviewer.
Nothing here was written on the stale reading: the ruling below was *stop*, and
stop is correct either way. It is recorded because a queue read is only ever
true at its timestamp, and this one had a peer resolving the same item inside
the same window.

`160/270` was never a question: this session authored that doctrine, and rule 4
puts the brief in the hands of the non-author who takes the item.

`310/050` was a genuine ambiguity and it went to Mike rather than being resolved
here. Rule 4 says tier is checked **at selection** and the taker writes the
brief, which bars an Opus session; the 2026-08-17 orchestrator clause says the
bar binds *"the judgement that forms findings, not every hand the pass passes
through"*, and a brief forms no finding. Both readings are available on the
text. **Mike ruled: stop** — leave it for a Fable session. So nothing was
written, and the queue is unchanged by this session.

The ambiguity itself is **not** resolved by his ruling — he chose the safe
action for one item, he did not rule on the reading. The next off-tier session
that finds a brief-less pointer will face the same fork. That is worth a clause
one day; it is not this session's to write.

## The question he routed here, answered

**Does `COMMUNICATION.md`'s 6,704-reply measurement rest on a corpus that
under-read the principal?** No. The corpus is **assistant replies** of 200+
characters, and every published metric is computed inside a reply. The only
metric needing a boundary — first use of a reference code in a session — needs a
*session* boundary, not a prompt. Nothing is conditioned on the prompt, so the
mis-bucketing the filer described has nothing to bucket. Recorded at `020/330`.

⚠️ **The limit is stated in the item rather than smoothed over:** the measuring
script was not preserved, so this is a reconstruction from the four published
metrics, not a read of the code that produced them.

## What the check turned up instead, and it is atelier's own

The filer's mechanism is real, and it bites the house harder than it bites the
question. **A message the principal types while a session is working is not a
user message.** It lands as `type:"attachment"` · `attachment.type:
"queued_command"`, text in `.prompt`.

**Measured across the whole live store** — and the first measurement here was
**wrong**, corrected within the day rather than quietly restated. The original
(4,433 opening against 2,237 mid-turn, *"33.5%"*) counted **system-injected
text as the principal's messages**: task notifications, cross-session messages
and system reminders arrive in both records. Classified the same way on both
sides, counting only what he typed: **3,013 opening against 965 mid-turn —
24.3%**. By repo: `docker-heap` 38.5% · `cbom` 36.1% · `faves` 34.7% · `kainga`
28.6% · `shed` 23.4% · `ros` 19.1% · `atelier` 18.9%. Only **43.3%** of
`queued_command` records are human-typed at all.

🔑 **The mistake is this finding's own shape, one level up.** A channel's
record *type* is not its *authorship*. Reading `queued_command` as "he typed
this" is the same error as reading `type == "user"` as "this is everything he
typed" — and it was made while writing the item that names the second one. The
defect is unchanged and still large: about **one in four** of his typed
messages is invisible to a `type == "user"` read.

🔥 **`cctranscript` reads channel one only, and says otherwise.** Both selection
points key on `o.type === 'user' && !o.toolUseResult` (`:498` replay, `:315`
header). Proven live, not inferred from the code: a `queued_command` in a real
atelier transcript is absent from `cctranscript --full` on that exact file, and
`--search … --all` returns **0 hits in 0 sessions across 669 sessions** while
printing `searched prompts+replies`. The tool asserts coverage it does not have,
so *"did he ever ask for X?"* returns a **confident zero**. Filed as a defect at
`210/100`, not as a feature request — the `--agents` gap beside it is a
widening; this is a documented capability returning a wrong answer.

**Third channel, same class:** an `AskUserQuestion` selection arrives as a
`tool_result` and is outside `prompts+replies` too. A patch that adds only
`queued_command` must not claim the principal's input is covered.

## The two proposals, filed and not written

- `320/070` — a mid-turn instruction is a **first-class instruction** (home it
  before the turn ends, `GUARDS.md`'s no-home duty applied to an *arrival mode*),
  and an audit of what the principal asked for states which channels it read.
- `320/080` — `quotescan`, checking quotations attributed to the principal
  against the corpus, with the 🛑 that matters: on the obvious corpus it
  **accuses him of fabricating his own instructions**. The filer's first pass
  flagged 51 quotations, including all nineteen mid-turn commissions that define
  its repo's scope; as a blocking check the indicated remedy would have been to
  delete his real instructions as fabrications. So `320/070` lands in the same
  commit as the scanner or the scanner does not land.

Both are Mike's to rule — `320/080` touches `GUARDS.md`'s fourth requirement,
his 2026-08-17 ruling, and `320/070` is a doctrine edit.

## Not claimed

Nothing was fixed. `cctranscript` still reads one channel of three; the
three-channel fact has no doctrine home yet; the child's 51- and 115-finding
counts are its measurements of its own repo, recorded as reported. The
mechanism behind them is what reproduced here — the counts are not.
