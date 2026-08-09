// Stdlib-only tests for cctranscript — Node's built-in node:test + node:assert,
// zero third-party dep (mirrors tools/'s "stdlib only, no pytest" floor). Named
// *.test.js per node:test convention; the shell glob expands at run time, so a
// new test file is picked up without editing any command. Run:
//   node --test instruments/*.test.js
//
// Two layers:
//   1. Pure-function units — friendlyModel, wrap, styleInline, humanDelta,
//      dateOf/fmtTime, visLen/padLeftTo — required straight from the script
//      (its CLI is guarded by require.main === module, so nothing runs).
//   2. A schema-drift contract test — spawn the real CLI over a checked-in
//      synthetic fixture and assert the --json shape (role classification, model
//      mapping, timestamp/text extraction, --think/--tools gating). This is what
//      catches a Claude Code log-format change: if the .jsonl schema shifts, the
//      contract assertions fail loudly instead of the tool silently mis-rendering.

const test = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const zlib = require('node:zlib');
const { execFileSync } = require('node:child_process');

const cc = require('./cctranscript');

const SCRIPT = path.join(__dirname, 'cctranscript');
const FIXTURE = path.join(__dirname, 'fixtures', 'session-sample.jsonl');

// --- pure functions -----------------------------------------------------

test('friendlyModel maps the id table', () => {
  assert.equal(cc.friendlyModel('claude-opus-4-8'), 'Opus 4.8');
  assert.equal(cc.friendlyModel('claude-fable-5'), 'Fable 5');
  assert.equal(cc.friendlyModel('fable'), 'Fable');             // bare family
  assert.equal(cc.friendlyModel('claude-sonnet-5-20260101'), 'Sonnet 5'); // trailing date dropped
  assert.equal(cc.friendlyModel('claude-haiku-4-5-20251001'), 'Haiku 4.5');
  assert.equal(cc.friendlyModel('<synthetic>'), null);         // synthetic → no tag
  assert.equal(cc.friendlyModel(''), null);
  assert.equal(cc.friendlyModel(undefined), null);
  assert.equal(cc.friendlyModel('gpt-4'), 'gpt-4');            // unknown → passed through
});

test('contextOf counts the cached prefix, not just the fresh input', () => {
  // The whole point: a long session sends almost everything as cache_read, so
  // input_tokens alone would report a 400k conversation as a handful of tokens.
  assert.equal(cc.contextOf({ input_tokens: 12, cache_creation_input_tokens: 4000, cache_read_input_tokens: 8000 }), 12012);
  assert.equal(cc.contextOf({ input_tokens: 7 }), 7);        // missing cache fields → 0
  assert.equal(cc.contextOf(undefined), null);               // no usage → unknown, not 0
});

test('fmtTokens abbreviates to a magnitude you can read at a glance', () => {
  assert.equal(cc.fmtTokens(477189), '477k');
  assert.equal(cc.fmtTokens(84929), '85k');    // whole thousands from 10k up
  assert.equal(cc.fmtTokens(8532), '8.5k');    // a decimal below it, where it matters
  assert.equal(cc.fmtTokens(12012), '12k');
  assert.equal(cc.fmtTokens(1234567), '1.2M');
  assert.equal(cc.fmtTokens(940), '940');
  assert.equal(cc.fmtTokens(0), null);                       // nothing to report
  assert.equal(cc.fmtTokens(undefined), null);
});

test('wrap word-wraps, hard-breaks over-long tokens, and floors width', () => {
  assert.deepEqual(cc.wrap('the quick brown fox', 9), ['the quick', 'brown fox']);
  assert.deepEqual(cc.wrap('abcdefghijkl', 8), ['abcdefgh', 'ijkl']); // hard break at width
  assert.deepEqual(cc.wrap('', 10), ['']);                                // empty → one blank line
  assert.deepEqual(cc.wrap('   ', 10), ['']);                             // whitespace-only
  // Width below the 8-col floor is clamped up, not honoured literally.
  assert.deepEqual(cc.wrap('hello world', 3), ['hello', 'world']);
});

test('styleInline strips bold/link markers with colour off but keeps code backticks', () => {
  const off = cc.styleInline('**bold** and `code` and [t](u)', false);
  assert.equal(off, 'bold and `code` and t (u)');
  const on = cc.styleInline('**bold** and `code`', true);
  assert.match(on, /\x1b\[1m/);          // bold escape emitted
  assert.ok(!on.includes('`'));          // code rendered by colour, backticks gone
});

test('humanDelta formats compact durations, signed and unsigned', () => {
  assert.equal(cc.humanDelta(500), '+500ms');
  assert.equal(cc.humanDelta(3000), '+3s');
  assert.equal(cc.humanDelta(90000), '+1m30s');
  assert.equal(cc.humanDelta(3600000), '+1h');
  assert.equal(cc.humanDelta(3660000), '+1h1m');
  assert.equal(cc.humanDelta(3000, false), '3s');   // unsigned (span, not delta)
});

test('fmtTime/dateOf under --utc are deterministic; junk is handled', () => {
  const iso = '2026-01-02T03:04:05.000Z';
  assert.equal(cc.fmtTime(iso, true), '03:04:05'); // leakscan:allow: HH:MM:SS clock time, not an IPv6 address
  assert.equal(cc.dateOf(iso, true), '2026-01-02');
  assert.equal(cc.fmtTime('', true), '        ');       // 8 spaces
  assert.equal(cc.fmtTime('garbage', true), '        ');
  assert.equal(cc.dateOf(null, true), '');
  assert.match(cc.fmtTime(iso), /^\d\d:\d\d:\d\d$/);    // local: shape only (tz-agnostic)
});

test('visLen ignores ANSI; padLeftTo right-justifies by visible width', () => {
  assert.equal(cc.visLen('\x1b[1mhi\x1b[0m'), 2);
  assert.equal(cc.visLen('plain'), 5);
  assert.equal(cc.padLeftTo('hi', 5), '   hi');
  assert.equal(cc.padLeftTo('\x1b[1mhi\x1b[0m', 5), '   ' + '\x1b[1mhi\x1b[0m');
  assert.equal(cc.padLeftTo('toolong', 3), 'toolong'); // never truncates
});

test('numberTurns: prompts get N, text replies N.M resetting per prompt; think/tool unnumbered', () => {
  const turns = [
    { role: 'claude' },                 // reply before any prompt → exchange 0
    { role: 'you' }, { role: 'think' }, { role: 'claude' }, { role: 'tool' }, { role: 'claude' },
    { role: 'you' }, { role: 'claude' },
  ];
  cc.numberTurns(turns);
  assert.deepEqual(turns.map((t) => t.ref),
    ['0.1', '1', undefined, '1.1', undefined, '1.2', '2', '2.1']);
});

test('extractText concatenates text blocks and passes strings through', () => {
  assert.equal(cc.extractText('plain string'), 'plain string');
  assert.equal(cc.extractText([
    { type: 'text', text: 'a' }, { type: 'tool_use', name: 'x' }, { type: 'text', text: 'b' },
  ]), 'a\nb');
  assert.equal(cc.extractText(undefined), '');
});

// --- schema-drift contract test -----------------------------------------

function runJson(...flags) {
  const out = execFileSync('node', [SCRIPT, '--json', ...flags, FIXTURE], { encoding: 'utf8' });
  return JSON.parse(out);
}
const roles = (j) => j.turns.map((t) => t.role);
const models = (j) => j.turns.map((t) => t.model);

test('contract: repo/cwd recovered from the log', () => {
  const j = runJson();
  assert.equal(j.cwd, '/home/dev/synthetic-repo');
  assert.equal(j.repo, 'synthetic-repo');   // basename of the recorded cwd
});

test('contract: default classifies prompts vs replies, maps models, extracts text/time', () => {
  const j = runJson();
  // Default gates out thinking, tool calls, and tool-result carriers.
  assert.deepEqual(roles(j), ['you', 'claude', 'claude']);
  assert.deepEqual(models(j), [null, 'Opus 4.8', 'Sonnet 5']);
  assert.deepEqual(j.turns.map((t) => t.ref), ['1', '1.1', '1.2']); // citable refs in --json
  assert.equal(j.turns[0].text, 'Add a null check to the parser');
  assert.equal(j.turns[0].timestamp, '2026-01-02T03:04:05.000Z');
  assert.equal(j.turns[1].text, "I'll add the null check now.");
});

test('contract: context peak and final come off the usage records', () => {
  const j = runJson();
  // The fixture's second reply is deliberately smaller than the first, the
  // shape a compacted session leaves: the peak is what the session held, the
  // final only what survived. Reporting one as the other would be a lie.
  assert.equal(j.context.peak, 12012);
  assert.equal(j.context.final, 2105);
});

test('contract: subagent spawns are counted under either tool name, with their types', () => {
  const j = runJson();
  assert.equal(j.agents.started, 2);                        // Agent + the legacy Task name
  assert.deepEqual(j.agents.byType, { Explore: 1, unspecified: 1 });
  // The count is a property of the session, not of the view: it must not move
  // when the flags that gate *rendering* tool turns change.
  assert.equal(runJson('--full').agents.started, 2);
});

// --- agents started vs finished -----------------------------------------
// `started` comes off the spawn tool calls (a ceiling); `finished` off the
// sibling <uuid>/subagents/ directory of per-agent logs (one per agent that
// actually ran). The pair is the point: the gap is a skipped or stopped spawn.
// The one thing that must never happen is a silent zero where the store simply
// didn't say — so these pin the unknown path as hard as the counted one.

// A copy of the fixture with a sibling subagents/ store beside it, shaped as the
// harness writes it: <stem>/subagents/agent-<id>.jsonl (+ the .meta.json sidecar
// the harness also writes, which must not be counted as an agent). `ext` lets
// the archive case lay the same store down as .jsonl.gz.
function withSubagents(tag, n, ext = '.jsonl') {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), `cctranscript-${tag}-`));
  const file = path.join(dir, `${tag}.jsonl`);
  fs.copyFileSync(FIXTURE, file);
  const store = path.join(dir, tag, 'subagents');
  fs.mkdirSync(store, { recursive: true });
  for (let i = 0; i < n; i++) {
    fs.writeFileSync(path.join(store, `agent-a${i}${ext}`), ext === '.jsonl.gz' ? zlib.gzipSync('{}\n') : '{}\n');
    fs.writeFileSync(path.join(store, `agent-a${i}.meta.json`), '{"agentType":"Explore","spawnDepth":1}\n');
  }
  return file;
}

const head = (file, ...flags) => execFileSync('node', [SCRIPT, '--no-color', ...flags, file], { encoding: 'utf8' })
  .split('\n').filter((l) => l.trim())[1];
const jsonOf = (file, ...flags) => JSON.parse(
  execFileSync('node', [SCRIPT, '--json', ...flags, file], { encoding: 'utf8' }));

test('agents: a readable subagents/ directory gives the finished count', () => {
  const file = withSubagents('bothran', 2);
  const j = jsonOf(file);
  assert.equal(j.agents.started, 2);
  assert.equal(j.agents.finished, 2);
  assert.equal(j.agents.finishedKnown, true);
  assert.match(head(file), /2 agents started · 2 finished/);
  // The .meta.json sidecars sit in the same directory and are not agents.
  assert.equal(fs.readdirSync(path.join(path.dirname(file), 'bothran', 'subagents')).length, 4);
});

test('agents: started > finished — the gap a skipped or stopped spawn leaves', () => {
  const file = withSubagents('stopped', 1);   // fixture spawns 2, only 1 ever ran
  const j = jsonOf(file);
  assert.equal(j.agents.started, 2);
  assert.equal(j.agents.finished, 1);
  assert.match(head(file), /2 agents started · 1 finished/);
});

test('agents: finished may exceed started — a nested spawn logs to the same store', () => {
  // An agent that spawns its own agent writes into the principal's subagents/
  // directory, while `started` only ever sees the principal's own spawn calls.
  // Neither figure bounds the other, and clamping would hide the nesting.
  const j = jsonOf(withSubagents('nested', 3));
  assert.equal(j.agents.started, 2);
  assert.equal(j.agents.finished, 3);
});

test('agents: no subagents/ store but spawns recorded → finished is unknown, not zero', () => {
  // The checked-in fixture has no sibling store: spawns happened, nothing here
  // says whether they ran. A 0 would be a claim the evidence cannot support.
  const j = runJson();
  assert.equal(j.agents.started, 2);
  assert.equal(j.agents.finished, null);      // null, never 0
  assert.equal(j.agents.finishedKnown, false);
  assert.ok('finished' in j.agents, 'the key is always present, so absent-vs-zero is never the question');
  assert.match(head(FIXTURE), /2 agents started · finished unknown/);
});

test('agents: no spawns at all → finished is a known zero, the log proves it', () => {
  // No spawn call means no agent could have run: the zero is a fact off the log
  // itself, so it prints as one even with no directory to read.
  const none = variant('noagents', (t) => t.replace(/,\{"type":"tool_use","name":"(Agent|Task)"[^}]*\}\}/g, ''));
  const j = jsonOf(none);
  assert.equal(j.agents.started, 0);
  assert.equal(j.agents.finished, 0);
  assert.equal(j.agents.finishedKnown, true);
  assert.match(head(none), /0 agents started · 0 finished/);
});

test('agents: both tallies are taken before the view gating', () => {
  // --tools/--think change what you SEE; they must never change what the header
  // reports about the session.
  const file = withSubagents('gating', 1);
  for (const flags of [[], ['--tools'], ['--think'], ['--full']]) {
    const j = jsonOf(file, ...flags);
    assert.equal(j.agents.started, 2, `started moved under ${flags.join(' ') || 'default'}`);
    assert.equal(j.agents.finished, 1, `finished moved under ${flags.join(' ') || 'default'}`);
  }
});

test('agents: the two chips hold their place in every case (stable field set)', () => {
  // The summary line is read by comparing two sessions side by side, so the
  // field SET never varies — counted, zero and unknown all print both chips.
  const both = ['agents started', 'finished'];
  for (const line of [head(withSubagents('stable', 2)), head(FIXTURE),
                      head(variant('nospawn', (t) => t.replace(/,\{"type":"tool_use","name":"(Agent|Task)"[^}]*\}\}/g, '')))]) {
    for (const chip of both) assert.ok(line.includes(chip), `missing "${chip}" in: ${line}`);
  }
});

test('subagentDir resolves the store from a live log and an archive mirror alike', () => {
  assert.equal(cc.subagentDir('/p/-repo/abc.jsonl'), path.join('/p/-repo/abc', 'subagents'));
  assert.equal(cc.subagentDir('/p/-repo/abc.jsonl.gz'), path.join('/p/-repo/abc', 'subagents'));
});

test('the summary line reports the context peak; a log without usage omits it', () => {
  assert.match(head(FIXTURE), /12k context/);

  // Same fixture with the usage records stripped — an older log, or a
  // synthetic one. The chip disappears rather than claiming a context of 0.
  // This is the deliberate opposite of the agent chips, which hold their place
  // and say "unknown" instead: context has no fixed pair to keep aligned.
  const bare = variant('nousage', (t) => t.replace(/"usage":\{[^}]*\},/g, ''));
  assert.ok(!/context/.test(head(bare)), 'no usage records → no context chip');

  const one = variant('oneagent', (t) => t.replace(/,\{"type":"tool_use","name":"Task"[^}]*\}\}/, ''));
  assert.match(head(one), /1 agent started/);   // and one agent isn't "1 agents"
});

// A throwaway copy of the fixture with an edit applied — for the cases that
// need a log the fixture deliberately isn't (no usage records, no spawns).
function variant(tag, edit) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), `cctranscript-${tag}-`));
  const file = path.join(dir, `${tag}.jsonl`);
  fs.writeFileSync(file, edit(fs.readFileSync(FIXTURE, 'utf8')));
  return file;
}

test('contract: --tools admits tool calls and tool-result carriers, in order', () => {
  const j = runJson('--tools');
  assert.deepEqual(roles(j), ['you', 'claude', 'tool', 'tool', 'tool', 'result', 'claude']);
  assert.ok(j.turns[2].text.startsWith('Edit'));      // tool_use summarised
  assert.match(j.turns[3].text, /Agent.*other parsers/); // a spawn is a tool call like any other
  assert.match(j.turns[5].text, /file edited/);       // result carrier
});

test('contract: --think admits thinking blocks (only)', () => {
  const j = runJson('--think');
  assert.deepEqual(roles(j), ['you', 'think', 'claude', 'claude']);
  assert.equal(j.turns[1].text, 'Consider the empty-input edge case first.');
});

test('contract: --list on an explicit path recovers repo and a real timestamp', () => {
  const out = execFileSync('node', [SCRIPT, '--json', '--list', FIXTURE], { encoding: 'utf8' });
  const [entry] = JSON.parse(out);
  assert.equal(entry.repo, 'synthetic-repo');
  // The record comes from the same constructor as walked sessions: a real
  // stat mtime, not the old hardcoded 0 that rendered a blank timestamp.
  assert.ok(entry.lastActivity, 'explicit path must carry the file mtime');
  assert.ok(!isNaN(new Date(entry.lastActivity)));
});

test('requiring cctranscript never acts on the host argv (help lives in the CLI guard)', () => {
  const out = execFileSync('node',
    ['-e', 'require(process.argv[1]); console.log("host-alive")', SCRIPT, '-h'],
    { encoding: 'utf8' });
  assert.equal(out.trim(), 'host-alive');
});

test('contract: --full admits thinking, tools, and results together', () => {
  const j = runJson('--full');
  assert.deepEqual(roles(j), ['you', 'think', 'claude', 'tool', 'tool', 'tool', 'result', 'claude']);
  // Refs number only prompts and text replies; think/tool/result stay null.
  assert.deepEqual(j.turns.map((t) => t.ref), ['1', null, '1.1', null, null, null, null, '1.2']);
});

// --- archive mode: reading ccarchive's compressed mirror ----------------
// A throwaway archive shaped exactly as ccarchive lays it out:
//   <dest>/<encoded-repo>/<uuid>.jsonl.gz
// The contract: the same fixture renders identically whether read live or
// through the gzip mirror, and a --list over the archive never reads an
// evicted (dataless) file — asserted through the same CCARCHIVE_SIMULATE_
// DATALESS seam ccarchive's own tests use, since a real eviction can't be
// forced on demand.

const ARCHIVE_UUID = '0f9e8d7c-0000-4000-8000-000000000000';
function makeArchive() {
  const dest = fs.mkdtempSync(path.join(os.tmpdir(), 'cctranscript-archive-'));
  const repoDir = path.join(dest, '-home-dev-synthetic-repo');
  fs.mkdirSync(repoDir, { recursive: true });
  const gz = path.join(repoDir, `${ARCHIVE_UUID}.jsonl.gz`);
  fs.writeFileSync(gz, zlib.gzipSync(fs.readFileSync(FIXTURE)));
  return { dest, gz };
}

test('contract: --from-archive renders a .gz mirror identically to the live log', () => {
  const { dest } = makeArchive();
  const live = runJson();
  const j = JSON.parse(execFileSync('node',
    [SCRIPT, '--json', '--from-archive', '--dest', dest, ARCHIVE_UUID], { encoding: 'utf8' }));
  assert.equal(j.source, 'archive');
  assert.equal(j.repo, 'synthetic-repo');   // cwd recovered through the gzip
  assert.deepEqual(j.turns, live.turns);    // same turns, byte-format-blind
});

test('contract: --dest alone implies --from-archive; --list finds the mirrored session', () => {
  const { dest } = makeArchive();
  const out = execFileSync('node',
    [SCRIPT, '--json', '--list', '--dest', dest, '--repo', 'synthetic-repo'], { encoding: 'utf8' });
  const [entry] = JSON.parse(out);
  assert.equal(entry.id, ARCHIVE_UUID);     // .jsonl.gz stripped to the uuid
  assert.equal(entry.repo, 'synthetic-repo');
  assert.match(entry.firstPrompt, /null check/);
  assert.equal(entry.evicted, false);
});

test('contract: an explicit .jsonl.gz path needs no flag at all', () => {
  const { gz } = makeArchive();
  const live = runJson();
  const j = JSON.parse(execFileSync('node', [SCRIPT, '--json', gz], { encoding: 'utf8' }));
  assert.equal(j.source, 'archive');
  assert.deepEqual(j.turns, live.turns);
});

test('contract: --list never reads an evicted mirror; --repo still finds it', () => {
  const { dest } = makeArchive();
  const out = execFileSync('node',
    [SCRIPT, '--json', '--list', '--dest', dest, '--repo', 'synthetic-repo'], {
      encoding: 'utf8',
      env: { ...process.env, CCARCHIVE_SIMULATE_DATALESS: ARCHIVE_UUID },
    });
  const [entry] = JSON.parse(out);
  assert.equal(entry.evicted, true);
  assert.equal(entry.firstPrompt, null);    // not read — reading would fault it back
  assert.equal(entry.cwd, null);            // cwd sniff skipped for the same reason
  assert.equal(entry.repo, 'repo');         // lossy folder-tail label, honestly
});

test('contract: archive mode counts the mirrored subagents/ store, and admits when it is missing', () => {
  // ccarchive captures every .jsonl at ANY depth and mirrors it at the same
  // relative path, so <dest>/<repo>/<uuid>/subagents/agent-*.jsonl.gz is really
  // there — the finished count is NOT live-only. Verified against a real archive
  // on 2026-07-26; the .meta.json sidecars are the part that doesn't survive.
  const { dest } = makeArchive();
  const store = path.join(dest, '-home-dev-synthetic-repo', ARCHIVE_UUID, 'subagents');

  // Before the store is laid down: mirrored session, no per-agent logs → unknown.
  const before = JSON.parse(execFileSync('node',
    [SCRIPT, '--json', '--from-archive', '--dest', dest, ARCHIVE_UUID], { encoding: 'utf8' }));
  assert.equal(before.agents.started, 2);
  assert.equal(before.agents.finished, null);
  assert.equal(before.agents.finishedKnown, false);

  fs.mkdirSync(store, { recursive: true });
  for (const n of ['agent-a1', 'agent-a2']) fs.writeFileSync(path.join(store, `${n}.jsonl.gz`), zlib.gzipSync('{}\n'));
  const after = JSON.parse(execFileSync('node',
    [SCRIPT, '--json', '--from-archive', '--dest', dest, ARCHIVE_UUID], { encoding: 'utf8' }));
  assert.equal(after.agents.finished, 2);
  assert.equal(after.agents.finishedKnown, true);

  // The nested store must not turn into a listed "session" of its own.
  const listed = JSON.parse(execFileSync('node',
    [SCRIPT, '--json', '--list', '--dest', dest, '--repo', 'synthetic-repo'], { encoding: 'utf8' }));
  assert.equal(listed.length, 1);
});

test('readLogText gunzips a .gz and passes plain files through', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'cctranscript-rlt-'));
  const plain = path.join(dir, 'a.jsonl');
  const gz = path.join(dir, 'a.jsonl.gz');
  fs.writeFileSync(plain, 'hello\n');
  fs.writeFileSync(gz, zlib.gzipSync('hello\n'));
  assert.equal(cc.readLogText(plain), 'hello\n');
  assert.equal(cc.readLogText(gz), 'hello\n');
});

test('isDatalessFlags: SF_DATALESS bit only (mirrors ccarchive)', () => {
  assert.equal(cc.isDatalessFlags(0x40000060), true);   // real evicted value
  assert.equal(cc.isDatalessFlags(0x20), false);        // UF_COMPRESSED alone
  assert.equal(cc.isDatalessFlags(NaN), false);
});

// --- --search ------------------------------------------------------------
// Every fixture below is SYNTHETIC and written here in the test: nothing from a
// real Claude Code log, no real session id, no real path under ~/.claude.
// Sessions are laid down in a throwaway HOME so the tool's own live-store
// discovery (~/.claude/projects/<encoded-repo>/<uuid>.jsonl) is what is
// exercised, rather than a single explicit path.

const you = (text, ts = '2026-01-02T03:04:05.000Z') => ({
  type: 'user', timestamp: ts, cwd: '/home/dev/synthetic-repo',
  message: { role: 'user', content: text },
});
const claude = (text, ts = '2026-01-02T03:04:20.000Z') => ({
  type: 'assistant', timestamp: ts,
  message: { role: 'assistant', model: 'claude-opus-4-8', content: [{ type: 'text', text }] },
});
const thinks = (text, ts = '2026-01-02T03:04:10.000Z') => ({
  type: 'assistant', timestamp: ts,
  message: { role: 'assistant', model: 'claude-opus-4-8', content: [{ type: 'thinking', thinking: text }] },
});
const calls = (name, input, ts = '2026-01-02T03:04:30.000Z') => ({
  type: 'assistant', timestamp: ts,
  message: { role: 'assistant', model: 'claude-opus-4-8', content: [{ type: 'tool_use', name, input }] },
});
const returns = (out, ts = '2026-01-02T03:04:35.000Z') => ({
  type: 'user', timestamp: ts, toolUseResult: { stdout: out },
  message: { role: 'user', content: [{ type: 'tool_result', content: out }] },
});

const UUID = (n) => `${String(n).repeat(8)}-0000-4000-8000-000000000000`;

// A throwaway live store: HOME points at it, so os.homedir()/.claude/projects is
// the temp tree. `sessions` is ordered oldest-first and the mtimes are stamped
// to match, so "most recent session first" is deterministic rather than a race.
//
// The stamp is never EARLIER than the log's own last timestamp, because a real
// log's mtime is its last write — and --search leans on exactly that fact for
// its --since skip. A fixture that broke the invariant would fail the tool for a
// property no real store has.
function makeStore(sessions) {
  const home = fs.mkdtempSync(path.join(os.tmpdir(), 'cctranscript-store-'));
  const dir = path.join(home, '.claude', 'projects', '-home-dev-synthetic-repo');
  fs.mkdirSync(dir, { recursive: true });
  let clock = Date.UTC(2026, 0, 2) / 1000;
  for (const [id, entries] of sessions) {
    const f = path.join(dir, `${id}.jsonl`);
    fs.writeFileSync(f, entries.map((o) => JSON.stringify(o)).join('\n') + '\n');
    const last = Math.max(0, ...entries.map((e) => Date.parse(e.timestamp) / 1000 || 0));
    const t = Math.max(clock, last);
    fs.utimesSync(f, t, t);
    clock += 86400;
  }
  return home;
}
function runIn(home, ...flags) {
  return execFileSync('node', [SCRIPT, '--repo', 'synthetic-repo', ...flags],
    { encoding: 'utf8', env: { ...process.env, HOME: home }, maxBuffer: 96 * 1024 * 1024 });
}
const searchJson = (home, ...flags) => JSON.parse(runIn(home, '--json', ...flags));
// Exit status + stderr for the argument-error cases.
function failIn(home, ...flags) {
  try { runIn(home, ...flags); return { code: 0, err: '' }; }
  catch (e) { return { code: e.status, err: String(e.stderr) }; }
}

test('search: a literal term matches metacharacters literally; --regex treats them as a pattern', () => {
  const home = makeStore([
    [UUID(1), [you('the gate lives in tools/floor.py today')]],
    [UUID(2), [you('a stray sibling named tools/floorZpy')]],
    [UUID(3), [you('and the literal string a.b*c[d] as typed')]],
  ]);
  // '.' stays a full stop: the literal finds the real path and nothing else.
  const lit = searchJson(home, '--search', 'tools/floor.py');
  assert.equal(lit.meta.hits, 1);
  assert.equal(lit.sessions.length, 1);
  assert.equal(lit.sessions[0].session, UUID(1));
  // Same string as a pattern: '.' is a wildcard, so the sibling matches too.
  const re = searchJson(home, '--search', 'tools/floor.py', '--regex');
  assert.equal(re.meta.hits, 2);
  assert.notEqual(lit.meta.hits, re.meta.hits, 'literal and --regex must disagree here');
  // And the other direction: '*' and '[' as characters vs as syntax.
  assert.equal(searchJson(home, '--search', 'a.b*c[d]').meta.hits, 1);
  assert.equal(searchJson(home, '--search', 'a.b*c[d]', '--regex').meta.hits, 0);
});

test('search: case-insensitive by default; --case narrows to the exact casing', () => {
  const home = makeStore([
    [UUID(1), [you('moved the branch to a Worktree first')]],
    [UUID(2), [you('one worktree per session')]],
  ]);
  assert.equal(searchJson(home, '--search', 'worktree').meta.sessionsMatched, 2);
  const strict = searchJson(home, '--search', 'worktree', '--case');
  assert.equal(strict.meta.sessionsMatched, 1);
  assert.equal(strict.sessions[0].session, UUID(2));
});

test('search: a macronised term survives the round trip, and is not confused with the bare vowel', () => {
  // The one measured shortcut this design rejects — decoding the log as latin1 —
  // would make this test fail while halving the sweep. UTF-8 throughout.
  const home = makeStore([
    [UUID(1), [you('the tohutō on Māori place names, e.g. Wairarapa')]],
    [UUID(2), [you('a Maori spelling with no macron at all')]],
  ]);
  const hit = searchJson(home, '--search', 'Māori');
  assert.equal(hit.meta.sessionsMatched, 1);
  assert.equal(hit.sessions[0].session, UUID(1));
  assert.match(hit.sessions[0].hits[0].excerpt, /Māori/);
  // Case folding reaches the macronised letter too, not just ASCII.
  assert.equal(searchJson(home, '--search', 'māori').meta.sessionsMatched, 1);
  assert.equal(searchJson(home, '--search', 'tohutō').meta.hits, 1);
});

test('search: a printed N.M ref resolves to the same turn when the session is reopened with default flags', () => {
  const home = makeStore([[UUID(5), [
    you('first ask'), thinks('unnumbered'), claude('first answer'),
    calls('Bash', { command: 'true' }), claude('the answer that mentions leakscan'),
    you('second ask'), claude('second answer'),
  ]]]);
  const j = searchJson(home, '--search', 'leakscan');
  assert.equal(j.sessions[0].hits.length, 1);
  const { ref, cited } = j.sessions[0].hits[0];
  assert.equal(ref, '1.2');
  assert.equal(cited, true);
  // Reopened with NO flags: the same ref, the same text. Gate-invariance is the
  // whole reason a search ref is worth printing.
  const reopened = JSON.parse(runIn(home, '--json', UUID(5)));
  const turn = reopened.turns.find((t) => t.ref === ref);
  assert.ok(turn, `ref ${ref} must exist in the default render`);
  assert.match(turn.text, /leakscan/);
});

test('search: a turn matching three times is one row with a count of 3', () => {
  const home = makeStore([[UUID(6), [
    you('sizescan then sizescan again and sizescan once more'),
  ]]]);
  const j = searchJson(home, '--search', 'sizescan');
  assert.equal(j.sessions[0].hits.length, 1, 'one row per matching turn, not per match');
  assert.equal(j.sessions[0].hits[0].hits, 3);
  assert.equal(j.meta.hits, 3);
  assert.match(runIn(home, '--no-color', '--search', 'sizescan'), /\(3 hits\)/);
});

test('search: an 800 KB prompt yields one bounded single-line excerpt', () => {
  // No layer is safe to print whole: a pasted blob is a prompt, and the largest
  // prompt measured in the live store is 848 KB.
  const filler = 'lorem ipsum dolor sit amet '.repeat(16000);   // ~430 KB each side
  const home = makeStore([[UUID(7), [you(filler + '\nthe NEEDLE is in here\n' + filler)]]]);
  const j = searchJson(home, '--search', 'NEEDLE');
  const ex = j.sessions[0].hits[0].excerpt;
  assert.ok(!ex.includes('\n'), 'the excerpt is a single line');
  assert.ok(ex.length <= 160, `excerpt must stay within its budget, got ${ex.length}`);
  assert.match(ex, /NEEDLE/);
  assert.match(ex, /^…/); assert.match(ex, /…$/);   // truncated on both sides
  // And the human row honours the resolved width.
  for (const line of runIn(home, '--no-color', '--width', '100', '--search', 'NEEDLE').split('\n')) {
    assert.ok(line.length <= 100, `row overran the width: ${line.length}`);
  }
});

test('search: tool layers are unsearched by default, counted anyway, and --tools finds them', () => {
  const home = makeStore([[UUID(8), [
    you('unrelated prompt'),
    calls('Grep', { pattern: 'harvestscan', path: '/home/dev/synthetic-repo' }),
    returns('matched harvestscan in three files'),
    claude('done'),
  ]]]);
  const off = searchJson(home, '--search', 'harvestscan');
  assert.equal(off.meta.hits, 0);
  assert.equal(off.meta.toolOnlySessions, 1, 'the unsearched layer reports as a count, not silence');
  assert.deepEqual(off.meta.layersSearched, ['prompts', 'replies']);
  assert.match(runIn(home, '--no-color', '--search', 'harvestscan'),
    /Tool output not searched: the term is in 1 session's tool calls or results \(add --tools\)/);
  // A stated zero, not an absent line, when the term really isn't there either.
  assert.match(runIn(home, '--no-color', '--search', 'nowhere-at-all'),
    /Tool output not searched: no session holds the term there either/);

  const on = searchJson(home, '--search', 'harvestscan', '--tools');
  assert.equal(on.meta.hits, 2);                       // the call's input and the result
  assert.deepEqual(on.sessions[0].hits.map((h) => h.role), ['tool', 'result']);
  // A tool hit has no citable ref of its own: it cites the exchange it sits in.
  assert.deepEqual(on.sessions[0].hits.map((h) => h.ref), ['1', '1']);
  assert.deepEqual(on.sessions[0].hits.map((h) => h.cited), [false, false]);
  assert.deepEqual(on.meta.layersSearched, ['prompts', 'replies', 'tools']);
});

test('search: --tools reads the whole tool call, not the one-line render summary', () => {
  // toolSummary keeps ONE field for the transcript; a search that read only that
  // would answer "no" for a filename sitting in any of the others.
  const long = 'x'.repeat(400);
  const home = makeStore([[UUID(9), [
    you('go'), calls('Bash', { command: `echo ${long}`, description: 'run publishscan' }),
  ]]]);
  assert.equal(cc.toolSummary('Bash', { command: 'echo hi', description: 'run publishscan' }),
    'Bash  echo hi');                                   // the render's view: one field
  assert.match(cc.toolSearchText('Bash', { command: 'echo hi', description: 'run publishscan' }),
    /publishscan/);                                     // the search's view: all of it
  assert.equal(searchJson(home, '--search', 'publishscan', '--tools').meta.hits, 1);
});

test('search: --think does not widen the search, because the log holds no thinking text', () => {
  const home = makeStore([[UUID(1), [
    you('go'), thinks('a stampscan thought no current log would carry'), claude('done'),
  ]]]);
  for (const flags of [[], ['--think'], ['--full']]) {
    const j = searchJson(home, '--search', 'stampscan', ...flags);
    assert.equal(j.meta.hits, 0, `--think widened the search under ${flags.join(' ') || 'default'}`);
    assert.equal(j.meta.thinkingSearched, false);
    assert.ok(!j.meta.layersSearched.includes('thinking'));
  }
  // And the man page says why, rather than leaving a flag that silently does nothing.
  const page = fs.readFileSync(path.join(__dirname, 'man', 'cctranscript.1'), 'utf8');
  assert.match(page, /cannot widen a search/);
  assert.match(page, /31,800\nthinking blocks exactly/);
  assert.match(page, /carry any text, all of them between 2026-06-05 and 2026-07-04/);
});

test('search: --since/--until filter on each turn\'s own timestamp, not the file mtime', () => {
  // A session that spans the --until bound must return only its in-window hits:
  // mtime is last-activity, so filtering candidates on it alone would drift from
  // ccrepo(1)'s per-message meaning. --utc pins the day boundary for the test.
  const home = makeStore([[UUID(2), [
    you('reviewscan on the second', '2026-01-02T12:00:00.000Z'),
    claude('reviewscan again on the fifth', '2026-01-05T12:00:00.000Z'),
  ]]]);
  const all = searchJson(home, '--utc', '--search', 'reviewscan');
  assert.equal(all.meta.hits, 2);
  const early = searchJson(home, '--utc', '--search', 'reviewscan', '--until', '20260103');
  assert.equal(early.meta.hits, 1);
  assert.equal(early.sessions[0].hits[0].ref, '1');
  const late = searchJson(home, '--utc', '--search', 'reviewscan', '--since', '2026-01-04');
  assert.equal(late.meta.hits, 1, 'dashes are tolerated in the date');
  assert.equal(late.sessions[0].hits[0].ref, '1.1');
  // The file was NOT skipped on mtime for --until: its last activity is after
  // the bound, and a long session can start before one and end after it.
  assert.equal(early.meta.sessionsSwept, 1);
  assert.equal(early.meta.skippedOutOfRange, 0);
});

test('search: --since skips a file whose last activity precedes the window, and counts the skip', () => {
  const home = makeStore([
    [UUID(3), [you('linkscan, long ago', '2026-01-02T12:00:00.000Z')]],
    [UUID(4), [you('linkscan, recently', '2026-01-03T12:00:00.000Z')]],
  ]);
  const j = searchJson(home, '--utc', '--search', 'linkscan', '--since', '20260103');
  assert.equal(j.meta.hits, 1);
  assert.equal(j.meta.sessionsSwept, 1);
  assert.equal(j.meta.skippedOutOfRange, 1);   // a pure optimisation, still reported
  assert.match(runIn(home, '--no-color', '--utc', '--search', 'linkscan', '--since', '20260103'),
    /1 session\(s\) skipped: last activity precedes --since/);
});

test('search: --json carries hits, refs and a meta block whose zeros all print', () => {
  const home = makeStore([[UUID(1), [you('pathscan here'), claude('and pathscan there')]]]);
  const j = searchJson(home, '--search', 'pathscan');
  for (const k of ['term', 'regex', 'caseSensitive', 'source', 'layersSearched',
    'thinkingSearched', 'since', 'until', 'timezone', 'materialise', 'top',
    'truncatedSessions', 'truncatedRows', 'sessionsInScope', 'sessionsSwept',
    'sessionsParsed', 'sessionsMatched', 'hits', 'skippedEvicted',
    'skippedOutOfRange', 'unreadable', 'toolOnlySessions', 'elapsedMs']) {
    assert.ok(k in j.meta, `meta.${k} must print on every run, zero included`);
  }
  assert.equal(j.meta.skippedEvicted, 0);      // a known zero prints as one
  assert.equal(j.meta.truncatedRows, 0);
  const [s] = j.sessions;
  for (const k of ['session', 'repo', 'cwd', 'lastActivity', 'hits']) assert.ok(k in s);
  for (const k of ['ref', 'cited', 'role', 'timestamp', 'excerpt', 'hits']) assert.ok(k in s.hits[0]);
});

test('search: the whole-file gate is the cost control — a swept file that misses is never parsed', () => {
  // This is the regression guard for the one step the implementation must resist
  // simplifying. Parsing every line of every file costs ~3x the I/O floor for
  // the identical answer, so the guard is structural (how many files were
  // parsed) rather than a wall-clock ratio that would be flaky in CI.
  const sessions = [];
  for (let i = 1; i <= 12; i++) sessions.push([UUID(i % 10) + `-${i}`, [you(`filler ${i}`)]]);
  sessions.push(['aaaaaaaa-0000-4000-8000-00000000000f', [you('the licenscan needle')]]);
  const j = searchJson(makeStore(sessions), '--search', 'licenscan');
  assert.equal(j.meta.sessionsInScope, 13);
  assert.equal(j.meta.sessionsSwept, 13);
  assert.equal(j.meta.sessionsParsed, 1, 'only the file that survived the gate may be parsed');
  assert.equal(j.meta.hits, 1);
});

test('search: --top truncates per level and prints what it hid', () => {
  const home = makeStore([
    [UUID(1), [you('signscan d')]],
    [UUID(2), [you('signscan e')]],
    [UUID(3), [you('signscan a'), claude('signscan b'), claude('signscan c')]],
  ]);
  const j = searchJson(home, '--search', 'signscan', '--top', '2');
  assert.equal(j.sessions.length, 2);
  assert.equal(j.meta.truncatedSessions, 1);
  assert.equal(j.meta.truncatedRows, 1);       // the 3-row session keeps 2
  // The counters above the cut still describe the whole sweep, not the slice.
  assert.equal(j.meta.sessionsMatched, 3);
  assert.match(runIn(home, '--no-color', '--search', 'signscan', '--top', '2'),
    /--top 2: 1 session\(s\) and 1 row\(s\) hidden/);
});

test('search: sessions are most-recent-first, hits chronological within one', () => {
  const home = makeStore([
    [UUID(1), [you('secretscan, older session')]],
    [UUID(2), [you('secretscan, first turn', '2026-01-02T01:00:00.000Z'),
               claude('secretscan, second turn', '2026-01-02T02:00:00.000Z')]],
  ]);
  const j = searchJson(home, '--search', 'secretscan');
  assert.deepEqual(j.sessions.map((s) => s.session), [UUID(2), UUID(1)]);
  assert.deepEqual(j.sessions[0].hits.map((h) => h.ref), ['1', '1.1']);
});

test('search: bad arguments exit 2 with the reason, never a silent empty result', () => {
  const home = makeStore([[UUID(1), [you('anything')]]]);
  const bad = [
    [['--search', '('], ['--regex'], /not a valid regular expression/],
    [['--search', 'x', '--since', 'yesterday'], [], /--since takes a date as YYYYMMDD/],
    [['--search', 'x', '--until', '2026-1-2'], [], /--until takes a date as YYYYMMDD/],
    [['--search', 'x', '--top', '0'], [], /--top must be a positive integer/],
    [['--search', ''], [], /--search needs a term/],
  ];
  for (const [args, extra, re] of bad) {
    const { code, err } = failIn(home, ...args, ...extra);
    assert.equal(code, 2, `expected exit 2 for ${args.join(' ')}`);
    assert.match(err, re);
  }
  // A search that finds nothing is an answer, not a failure.
  assert.equal(failIn(home, '--search', 'definitely-not-present').code, 0);
});

test('search: --list alongside --search is redundant, not contradictory — accepted in silence', () => {
  const home = makeStore([[UUID(1), [you('a floorfleet mention')]]]);
  const shape = (s) => { const j = JSON.parse(s); delete j.meta.elapsedMs; return j; };
  assert.deepEqual(shape(runIn(home, '--json', '--list', '--search', 'floorfleet')),
    shape(runIn(home, '--json', '--search', 'floorfleet')));
});

test('search: a session argument narrows the sweep to that one session', () => {
  const home = makeStore([
    [UUID(1), [you('datescan over here')]],
    [UUID(2), [you('datescan over there')]],
  ]);
  assert.equal(searchJson(home, '--search', 'datescan').meta.sessionsInScope, 2);
  const one = searchJson(home, '--search', 'datescan', UUID(2));
  assert.equal(one.meta.sessionsInScope, 1);
  assert.equal(one.sessions[0].session, UUID(2));
});

test('search: an evicted archive mirror is skipped and counted; --materialise reads it', () => {
  const { dest } = makeArchive();
  const flags = ['--json', '--dest', dest, '--repo', 'synthetic-repo', '--search', 'null check'];
  const evictedEnv = { ...process.env, CCARCHIVE_SIMULATE_DATALESS: ARCHIVE_UUID };
  const skipped = JSON.parse(execFileSync('node', [SCRIPT, ...flags], { encoding: 'utf8', env: evictedEnv }));
  assert.equal(skipped.meta.skippedEvicted, 1);
  assert.equal(skipped.meta.sessionsSwept, 0);
  assert.equal(skipped.meta.hits, 0);
  assert.equal(skipped.sessions.length, 0);
  assert.match(execFileSync('node', [SCRIPT, '--no-color', ...flags.slice(1)], { encoding: 'utf8', env: evictedEnv }),
    /1 mirror\(s\) not searched \(evicted\); --materialise reads them/);

  const forced = JSON.parse(execFileSync('node', [SCRIPT, ...flags, '--materialise'],
    { encoding: 'utf8', env: evictedEnv }));
  assert.equal(forced.meta.materialise, true);
  assert.equal(forced.meta.skippedEvicted, 0);
  assert.equal(forced.meta.sessionsSwept, 1);
  assert.equal(forced.meta.hits, 2);      // the fixture says it in a prompt and a reply
  assert.equal(forced.meta.source, 'archive');
});

test('search: the archive is searched through the gzip, same answer as the live log', () => {
  const { dest } = makeArchive();
  const j = JSON.parse(execFileSync('node',
    [SCRIPT, '--json', '--dest', dest, '--repo', 'synthetic-repo', '--search', 'null check'],
    { encoding: 'utf8' }));
  assert.equal(j.meta.source, 'archive');
  assert.equal(j.meta.hits, 2);
  assert.deepEqual(j.sessions[0].hits.map((h) => h.ref), ['1', '1.1']);
});

// --- search units --------------------------------------------------------

test('escapeRegex neutralises every metacharacter that could change a literal search', () => {
  const re = new RegExp(cc.escapeRegex('a.b*c[d]+e(f)?^$|{g}\\h'));
  assert.ok(re.test('a.b*c[d]+e(f)?^$|{g}\\h'));
  assert.ok(!re.test('axbbcd'));
});

test('rawForms covers the shapes a literal takes inside a raw .jsonl line', () => {
  assert.deepEqual(cc.rawForms('plain'), ['plain']);          // nothing to escape
  assert.ok(cc.rawForms('say "hi"').includes('say \\"hi\\"'));
  assert.ok(cc.rawForms('Māori').includes('M\\u0101ori'));     // the rare escaped spelling
  assert.ok(cc.rawForms('Māori').includes('Māori'));           // and the common raw one
});

test('scanText returns the first match and the total count, and survives an empty match', () => {
  assert.deepEqual(cc.scanText(/ab/, 'xxabyyab'), { count: 2, at: 2, len: 2 });
  assert.deepEqual(cc.scanText(/zz/, 'nothing'), { count: 0, at: -1, len: 0 });
  // A pattern that matches the empty string would never advance without the guard.
  assert.equal(cc.scanText(/a*/, 'baa').count, 3);   // '' at 0, 'aa' at 1, '' at 3
});

test('excerptAround centres on the match, collapses whitespace, and stays inside the budget', () => {
  const long = 'a'.repeat(500) + ' TERM ' + 'b'.repeat(500);
  const ex = cc.excerptAround(long, 501, 4, 40);
  assert.ok(ex.length <= 40, `got ${ex.length}`);
  assert.match(ex, /TERM/);
  assert.equal(ex[0], '…');
  assert.equal(ex[ex.length - 1], '…');
  // Short enough to print whole: no ellipses, whitespace collapsed to one line.
  assert.equal(cc.excerptAround('one\n\ttwo   three', 5, 3, 40), 'one two three');
});

// --- documentation convention (REPO-STANDARD: concise --help + a man page) --

test('--help is a concise digest that points at the man page', () => {
  const help = execFileSync('node', [SCRIPT, '-h'], { encoding: 'utf8' });
  // A one-screen digest: fits a standard 24-row terminal (trimEnd drops the
  // trailing newline console.log adds, so this counts content lines).
  assert.ok(help.trimEnd().split('\n').length <= 24, '--help should stay a one-screen digest');
  assert.match(help, /man cctranscript/, '--help must point at the full manual');
  for (const opt of ['--repo', '--list', '--full']) assert.ok(help.includes(opt));
});

test('a man page ships and is well-formed roff', () => {
  const page = path.join(__dirname, 'man', 'cctranscript.1');
  assert.ok(fs.existsSync(page), 'instruments/man/cctranscript.1 must exist');
  const roff = fs.readFileSync(page, 'utf8');
  assert.match(roff, /^\.TH CCTRANSCRIPT 1 /m, 'a .TH title line');
  for (const sec of ['NAME', 'SYNOPSIS', 'DESCRIPTION', 'OPTIONS', 'EXAMPLES', 'EXIT STATUS', 'SEE ALSO']) {
    assert.match(roff, new RegExp(`^\\.SH ${sec}`, 'm'), `a ${sec} section`);
  }
});

test('drift guard: every flag --help prints appears in the man page (superset relation)', () => {
  const help = execFileSync('node', [SCRIPT, '-h'], { encoding: 'utf8' });
  const page = fs.readFileSync(path.join(__dirname, 'man', 'cctranscript.1'), 'utf8');
  // Roff hyphenates flags as \-\-flag; normalise the page before matching.
  const pageFlat = page.replace(/\\-/g, '-');
  const flags = [...new Set(help.match(/--[\w-]+/g))];
  assert.ok(flags.length >= 8, `expected a real flag list, got ${flags.length}`);
  for (const flag of flags) {
    assert.ok(pageFlat.includes(flag), `man page must document ${flag} (--help is the digest, the page the superset)`);
  }
});
