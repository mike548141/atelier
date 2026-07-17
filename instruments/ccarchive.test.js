// Stdlib-only tests for ccarchive — Node's built-in node:test + node:assert,
// zero third-party dep (mirrors cctranscript's tests and tools/'s "stdlib only"
// floor). Run:  node --test instruments/*.test.js
//
// Two layers:
//   1. Pure-function units — defaultDest, archivePathFor, shouldArchive,
//      humanBytes, listJsonl — required straight from the script (its CLI is
//      guarded by require.main === module, so nothing runs on require).
//   2. A behaviour contract test — spawn the real CLI over a synthetic source
//      tree in a temp dir and assert the mirror: .jsonl → .jsonl.gz round-trips
//      byte-identical, nested subagent logs are captured, non-.jsonl is ignored,
//      a second run is idempotent (0 archived), and the archive is append-only
//      (a source deleted after archival stays kept).

const test = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const zlib = require('node:zlib');
const { execFileSync } = require('node:child_process');

const cc = require('./ccarchive');
const SCRIPT = path.join(__dirname, 'ccarchive');

// --- pure functions ------------------------------------------------------

test('defaultDest points at the macOS iCloud Drive, from the given home', () => {
  assert.equal(cc.defaultDest('/Users/x'),
    '/Users/x/Library/Mobile Documents/com~apple~CloudDocs/cc-transcripts');
});

test('archivePathFor mirrors the source-relative path under dest with a .gz suffix', () => {
  assert.equal(
    cc.archivePathFor('/dest', '/src', '/src/-repo/abc.jsonl'),
    path.join('/dest', '-repo', 'abc.jsonl.gz'));
  // Nested subagent log keeps its full relative structure.
  assert.equal(
    cc.archivePathFor('/dest', '/src', '/src/-repo/uuid/subagents/agent-1.jsonl'),
    path.join('/dest', '-repo', 'uuid', 'subagents', 'agent-1.jsonl.gz'));
});

test('shouldArchive: missing mirror or a newer source archives; an up-to-date mirror skips', () => {
  assert.equal(cc.shouldArchive(100, null), true);   // no mirror yet
  assert.equal(cc.shouldArchive(200, 100), true);    // source newer
  assert.equal(cc.shouldArchive(100, 100), false);   // same time → skip
  assert.equal(cc.shouldArchive(100, 200), false);   // mirror newer → skip
});

test('humanBytes scales units and drops precision past ten', () => {
  assert.equal(cc.humanBytes(512), '512 B');
  assert.equal(cc.humanBytes(1536), '1.5 KB');
  assert.equal(cc.humanBytes(5 * 1024 * 1024), '5.0 MB');
  assert.equal(cc.humanBytes(48 * 1024 * 1024), '48 MB');
});

// --- filesystem walk + behaviour contract --------------------------------

// A fresh temp workspace with a source tree; returns { dir, src, dest }.
function makeTree() {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ccarchive-'));
  const src = path.join(dir, 'projects');
  const dest = path.join(dir, 'archive');
  fs.mkdirSync(path.join(src, '-repo-a', 'uuid1', 'subagents'), { recursive: true });
  fs.mkdirSync(path.join(src, '-repo-b'), { recursive: true });
  fs.writeFileSync(path.join(src, '-repo-a', 'uuid1.jsonl'), '{"turn":1}\n{"turn":2}\n');
  fs.writeFileSync(path.join(src, '-repo-a', 'uuid1', 'subagents', 'agent-x.jsonl'), '{"sub":true}\n');
  fs.writeFileSync(path.join(src, '-repo-b', 'uuid2.jsonl'), '{"other":"session"}\n');
  fs.writeFileSync(path.join(src, '-repo-a', 'notes.txt'), 'not a transcript');
  return { dir, src, dest };
}

function runJson(src, dest, ...flags) {
  const out = execFileSync('node', [SCRIPT, '--json', '--source', src, '--dest', dest, ...flags],
    { encoding: 'utf8' });
  return JSON.parse(out);
}

test('listJsonl finds every .jsonl at any depth and ignores other files', () => {
  const { src } = makeTree();
  const found = cc.listJsonl(src).map((p) => path.relative(src, p)).sort();
  assert.deepEqual(found, [
    path.join('-repo-a', 'uuid1.jsonl'),
    path.join('-repo-a', 'uuid1', 'subagents', 'agent-x.jsonl'),
    path.join('-repo-b', 'uuid2.jsonl'),
  ].sort());
});

test('listJsonl on a missing source is empty, not an error', () => {
  assert.deepEqual(cc.listJsonl(path.join(os.tmpdir(), 'ccarchive-does-not-exist-xyz')), []);
});

test('contract: mirrors every .jsonl to .jsonl.gz, byte-identical, ignoring non-jsonl', () => {
  const { src, dest } = makeTree();
  const j = runJson(src, dest);
  assert.equal(j.total, 3);
  assert.equal(j.archived, 3);
  assert.equal(j.skipped, 0);

  // The .txt was not mirrored.
  assert.ok(!fs.existsSync(path.join(dest, '-repo-a', 'notes.txt.gz')));

  // Each mirror gunzips back to the exact source bytes.
  for (const rel of ['-repo-a/uuid1.jsonl', '-repo-a/uuid1/subagents/agent-x.jsonl', '-repo-b/uuid2.jsonl']) {
    const gzPath = path.join(dest, rel + '.gz');
    assert.ok(fs.existsSync(gzPath), `${rel}.gz should exist`);
    const back = zlib.gunzipSync(fs.readFileSync(gzPath));
    assert.deepEqual(back, fs.readFileSync(path.join(src, rel)));
  }
});

test('contract: a second run is idempotent — nothing changed, nothing re-archived', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const j2 = runJson(src, dest);
  assert.equal(j2.archived, 0);
  assert.equal(j2.skipped, 3);
});

test('contract: a changed source is re-archived; an unchanged sibling is not', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  // Rewrite one session with a strictly newer mtime.
  const changed = path.join(src, '-repo-b', 'uuid2.jsonl');
  fs.writeFileSync(changed, '{"other":"session"}\n{"turn":"appended"}\n');
  const now = new Date();
  fs.utimesSync(changed, now, new Date(now.getTime() + 5000));

  const j = runJson(src, dest);
  assert.equal(j.archived, 1);
  assert.equal(j.skipped, 2);
  const back = zlib.gunzipSync(fs.readFileSync(path.join(dest, '-repo-b', 'uuid2.jsonl.gz')));
  assert.match(back.toString(), /appended/);
});

test('contract: append-only — a source deleted after archival stays kept', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.rmSync(path.join(src, '-repo-b', 'uuid2.jsonl'));
  const j = runJson(src, dest);          // source gone
  assert.equal(j.total, 2);              // only two sources remain
  // The archived copy of the deleted session is untouched.
  assert.ok(fs.existsSync(path.join(dest, '-repo-b', 'uuid2.jsonl.gz')));
});

test('contract: --dry-run reports would-archive but writes nothing', () => {
  const { src, dest } = makeTree();
  const j = runJson(src, dest, '--dry-run');
  assert.equal(j.archived, 3);
  assert.equal(j.dryRun, true);
  assert.ok(!fs.existsSync(dest), 'dest must not be created on a dry run');
});

test('requiring ccarchive never acts on the host argv (the CLI lives behind the guard)', () => {
  const out = execFileSync('node',
    ['-e', 'require(process.argv[1]); console.log("host-alive")', SCRIPT, '-h'],
    { encoding: 'utf8' });
  assert.equal(out.trim(), 'host-alive');
});

// --- schedule management -------------------------------------------------
// Pure builders + the read-only status query only. Never spawn --install-
// schedule / --uninstall-schedule from tests: on a developer's Mac that would
// mutate their real launchd state.

test('schedulePaths derives the launchd + log paths under the given home', () => {
  const p = cc.schedulePaths('/Users/x');
  assert.equal(p.label, 'com.ccarchive.archive');
  assert.equal(p.plistPath, '/Users/x/Library/LaunchAgents/com.ccarchive.archive.plist');
  assert.equal(p.logPath, '/Users/x/Library/Logs/ccarchive.log');
});

test('resolveScriptPath prefers ~/.local/bin/ccarchive when present, else the fallback', () => {
  const home = fs.mkdtempSync(path.join(os.tmpdir(), 'ccarchive-home-'));
  const fallback = '/repo/instruments/ccarchive';
  // No installed entrypoint yet → fallback.
  assert.equal(cc.resolveScriptPath(home, fallback), fallback);
  // Create the installed symlink target → it wins.
  fs.mkdirSync(path.join(home, '.local', 'bin'), { recursive: true });
  const installed = path.join(home, '.local', 'bin', 'ccarchive');
  fs.writeFileSync(installed, '#!/usr/bin/env node\n');
  assert.equal(cc.resolveScriptPath(home, fallback), installed);
});

test('launchdPlist emits a valid agent with the given command, interval and log', () => {
  const xml = cc.launchdPlist({
    label: 'com.ccarchive.archive', nodePath: '/usr/local/bin/node',
    scriptPath: '/Users/x/.local/bin/ccarchive', intervalSeconds: 86400,
    logPath: '/Users/x/Library/Logs/ccarchive.log',
  });
  assert.match(xml, /<key>Label<\/key>\s*<string>com\.ccarchive\.archive<\/string>/);
  assert.match(xml, /<string>\/usr\/local\/bin\/node<\/string>/);
  assert.match(xml, /<string>\/Users\/x\/\.local\/bin\/ccarchive<\/string>/);
  assert.match(xml, /<key>StartInterval<\/key>\s*<integer>86400<\/integer>/);
  assert.match(xml, /<key>RunAtLoad<\/key>\s*<true\/>/);
  assert.match(xml, /<string>\/Users\/x\/Library\/Logs\/ccarchive\.log<\/string>/);
});

test('launchdPlist XML-escapes paths so an & in a home path cannot break the plist', () => {
  const xml = cc.launchdPlist({
    label: 'com.ccarchive.archive', nodePath: '/usr/local/bin/node',
    scriptPath: '/Users/a&b/ccarchive', intervalSeconds: 86400,
    logPath: '/Users/a&b/log',
  });
  assert.ok(xml.includes('/Users/a&amp;b/ccarchive'));
  assert.ok(!xml.includes('/Users/a&b/ccarchive'));  // raw & would be invalid XML
});

test('cronLine is a daily entry invoking node on the script', () => {
  assert.equal(cc.cronLine('/usr/local/bin/node', '/Users/x/.local/bin/ccarchive'),
    '0 3 * * * /usr/local/bin/node /Users/x/.local/bin/ccarchive');
});

test('contract: --schedule-status is read-only and exits 0 on any platform', () => {
  // Safe everywhere: on macOS it queries launchctl (no mutation); elsewhere it
  // prints the cron equivalent. Either way, output and a clean exit.
  const out = execFileSync('node', [SCRIPT, '--schedule-status'], { encoding: 'utf8' });
  assert.ok(out.length > 0);
});
