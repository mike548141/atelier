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

test('contract: --tools admits tool calls and tool-result carriers, in order', () => {
  const j = runJson('--tools');
  assert.deepEqual(roles(j), ['you', 'claude', 'tool', 'result', 'claude']);
  assert.ok(j.turns[2].text.startsWith('Edit'));      // tool_use summarised
  assert.match(j.turns[3].text, /file edited/);       // result carrier
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
  assert.deepEqual(roles(j), ['you', 'think', 'claude', 'tool', 'result', 'claude']);
  // Refs number only prompts and text replies; think/tool/result stay null.
  assert.deepEqual(j.turns.map((t) => t.ref), ['1', null, '1.1', null, null, '1.2']);
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

test('contract: --archive renders a .gz mirror identically to the live log', () => {
  const { dest } = makeArchive();
  const live = runJson();
  const j = JSON.parse(execFileSync('node',
    [SCRIPT, '--json', '--archive', '--dest', dest, ARCHIVE_UUID], { encoding: 'utf8' }));
  assert.equal(j.source, 'archive');
  assert.equal(j.repo, 'synthetic-repo');   // cwd recovered through the gzip
  assert.deepEqual(j.turns, live.turns);    // same turns, byte-format-blind
});

test('contract: --dest alone implies --archive; --list finds the mirrored session', () => {
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
