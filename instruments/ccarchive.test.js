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

// --- integrity: sha256 manifest + verify ---------------------------------

const { spawnSync } = require('node:child_process');
function runCli(...args) {
  const r = spawnSync('node', [SCRIPT, ...args], { encoding: 'utf8' });
  return { status: r.status, stdout: r.stdout, stderr: r.stderr };
}

test('sha256 is the known-answer hash of its input', () => {
  assert.equal(cc.sha256(Buffer.from('')),
    'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855');
  assert.equal(cc.sha256(Buffer.from('abc')),
    'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad');
});

test('contract: a run records a sha256 manifest matching the raw source bytes', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const manifest = cc.loadManifest(dest);
  const rels = ['-repo-a/uuid1.jsonl', '-repo-a/uuid1/subagents/agent-x.jsonl', '-repo-b/uuid2.jsonl'];
  for (const rel of rels) {
    assert.ok(manifest[rel], `manifest should record ${rel}`);
    assert.equal(manifest[rel].sha256, cc.sha256(fs.readFileSync(path.join(src, rel))));
  }
});

test('contract: --verify passes on an intact archive (exit 0)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const r = runCli('--verify', '--dest', dest);
  assert.equal(r.status, 0);
  assert.match(r.stdout, /every archived transcript matches/);
});

test('contract: --verify detects a mutated archive file (exit 1, names it)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  // Tamper: replace a .gz with a gzip of different content.
  const gzPath = path.join(dest, '-repo-b', 'uuid2.jsonl.gz');
  fs.writeFileSync(gzPath, zlib.gzipSync(Buffer.from('{"tampered":true}\n')));
  const r = runCli('--verify', '--dest', dest, '--json');
  assert.equal(r.status, 1);
  const out = JSON.parse(r.stdout);
  assert.deepEqual(out.mismatch, ['-repo-b/uuid2.jsonl']);
  assert.equal(out.missing.length, 0);
});

test('contract: --verify reports a deleted archive file as missing (exit 1)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.rmSync(path.join(dest, '-repo-b', 'uuid2.jsonl.gz'));
  const r = runCli('--verify', '--dest', dest, '--json');
  assert.equal(r.status, 1);
  const out = JSON.parse(r.stdout);
  assert.deepEqual(out.missing, ['-repo-b/uuid2.jsonl']);
});

test('manifest tracks the archive, not live sources: a pruned source keeps its entry', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const before = cc.loadManifest(dest)['-repo-b/uuid2.jsonl'].sha256;
  // Source pruned by Claude Code cleanup; .gz stays (append-only).
  fs.rmSync(path.join(src, '-repo-b', 'uuid2.jsonl'));
  runJson(src, dest);
  const after = cc.loadManifest(dest)['-repo-b/uuid2.jsonl'];
  assert.ok(after, 'pruned-source entry must survive');
  assert.equal(after.sha256, before);
  assert.equal(runCli('--verify', '--dest', dest).status, 0);  // still verifies
});

test('saveManifest is atomic (temp+rename) and writes deterministic key order', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ccarchive-mf-'));
  cc.saveManifest(dir, { 'z.jsonl': { sha256: '1' }, 'a.jsonl': { sha256: '2' } });
  const text = fs.readFileSync(cc.manifestPath(dir), 'utf8');
  assert.ok(text.indexOf('a.jsonl') < text.indexOf('z.jsonl'), 'keys sorted for stable diffs');
  assert.ok(!fs.existsSync(cc.manifestPath(dir) + '.tmp'), 'temp file renamed away');
  assert.deepEqual(cc.loadManifest(dir), { 'a.jsonl': { sha256: '2' }, 'z.jsonl': { sha256: '1' } });
});

// --- documentation convention (REPO-STANDARD: concise --help + a man page) --

test('--help is a concise digest that points at the man page', () => {
  const help = execFileSync('node', [SCRIPT, '-h'], { encoding: 'utf8' });
  assert.ok(help.split('\n').length <= 22, '--help should stay a one-screen digest');
  assert.match(help, /man ccarchive/, '--help must point at the full manual');
  for (const opt of ['--dest', '--verify', '--install-schedule']) assert.ok(help.includes(opt));
});

test('a man page ships and is well-formed roff', () => {
  const page = path.join(__dirname, 'man', 'ccarchive.1');
  assert.ok(fs.existsSync(page), 'instruments/man/ccarchive.1 must exist');
  const roff = fs.readFileSync(page, 'utf8');
  assert.match(roff, /^\.TH CCARCHIVE 1 /m, 'a .TH title line');
  for (const sec of ['NAME', 'SYNOPSIS', 'DESCRIPTION', 'OPTIONS', 'EXAMPLES', 'SEE ALSO']) {
    assert.match(roff, new RegExp(`^\\.SH ${sec}`, 'm'), `a ${sec} section`);
  }
});

// --- the ruled review findings, pinned (F1–F4, 2026-07-17) ----------------

test('isSuspectShrink flags a smaller source only when rawBytes is recorded', () => {
  assert.equal(cc.isSuspectShrink(5, { rawBytes: 10 }), true);
  assert.equal(cc.isSuspectShrink(10, { rawBytes: 10 }), false);
  assert.equal(cc.isSuspectShrink(15, { rawBytes: 10 }), false);
  assert.equal(cc.isSuspectShrink(5, undefined), false);
  assert.equal(cc.isSuspectShrink(5, { fromArchive: true }), false);  // no raw-bytes anchor
});

test('contract: a shrunken source is refused (exit 1), archive untouched; --force overwrites', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const srcFile = path.join(src, '-repo-b', 'uuid2.jsonl');
  const gzFile = path.join(dest, '-repo-b', 'uuid2.jsonl.gz');
  const before = fs.readFileSync(gzFile);
  fs.writeFileSync(srcFile, '{}\n');                      // truncated: smaller than recorded
  const future = (Date.now() + 5000) / 1000;
  fs.utimesSync(srcFile, future, future);                 // newer mtime → would overwrite
  const res = spawnSync('node', [SCRIPT, '--json', '--source', src, '--dest', dest],
    { encoding: 'utf8' });
  assert.equal(res.status, 1, 'a refused shrink must exit non-zero');
  const report = JSON.parse(res.stdout);
  assert.deepEqual(report.refusedShrink, [path.join('-repo-b', 'uuid2.jsonl')]);
  assert.match(res.stderr, /REFUSED/);
  assert.ok(fs.readFileSync(gzFile).equals(before), 'the archived copy must be untouched');
  // --force is the operator's deliberate overwrite: it goes through and re-anchors.
  const forced = runJson(src, dest, '--force');
  assert.equal(forced.archived, 1);
  assert.equal(zlib.gunzipSync(fs.readFileSync(gzFile)).toString(), '{}\n');
});

test('insideGitWorkTree detects a .git ancestor at any depth', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ccarchive-git-'));
  fs.mkdirSync(path.join(dir, 'repo', '.git', 'objects'), { recursive: true });
  fs.mkdirSync(path.join(dir, 'repo', 'deep', 'inside'), { recursive: true });
  assert.equal(cc.insideGitWorkTree(path.join(dir, 'repo', 'deep', 'inside')), true);
  assert.equal(cc.insideGitWorkTree(dir), false);
});

test('contract: a dest inside a git work tree is refused; --allow-repo-dest proceeds', () => {
  const { dir, src } = makeTree();
  const repoDest = path.join(dir, 'fakerepo', 'archive');
  fs.mkdirSync(path.join(dir, 'fakerepo', '.git'), { recursive: true });
  const res = spawnSync('node', [SCRIPT, '--json', '--source', src, '--dest', repoDest],
    { encoding: 'utf8' });
  assert.equal(res.status, 1);
  assert.match(res.stderr, /refusing to archive into a git work tree/);
  assert.ok(!fs.existsSync(repoDest), 'nothing may be written behind the refusal');
  const allowed = runJson(src, repoDest, '--allow-repo-dest');
  assert.equal(allowed.archived, 3);
});

test('contract: an empty source against a non-empty archive exits 1, not silent success', () => {
  const { dir, src, dest } = makeTree();
  runJson(src, dest);
  fs.renameSync(src, path.join(dir, 'projects-moved'));   // layout drift
  const res = spawnSync('node', [SCRIPT, '--json', '--source', src, '--dest', dest],
    { encoding: 'utf8' });
  assert.equal(res.status, 1);
  assert.match(res.stderr, /yielded no transcripts/);
});

test('contract: --verify fails on an unmanifested (injected) archive file and names it', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.writeFileSync(path.join(dest, '-repo-b', 'injected.jsonl.gz'), zlib.gzipSync('{"x":1}\n'));
  const res = spawnSync('node', [SCRIPT, '--verify', '--dest', dest], { encoding: 'utf8' });
  assert.equal(res.status, 1, 'an injected file must fail the verify');
  assert.match(res.stdout, /UNMANIFESTED.*injected\.jsonl/);
});

test('contract: --verify surfaces fromArchive entries distinctly (archive attesting itself)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.rmSync(cc.manifestPath(dest));                       // lose the manifest…
  fs.rmSync(path.join(src, '-repo-b', 'uuid2.jsonl'));    // …and one source is pruned
  runJson(src, dest);                                     // backfill: uuid2 from its .gz
  const res = spawnSync('node', [SCRIPT, '--verify', '--json', '--dest', dest],
    { encoding: 'utf8' });
  assert.equal(res.status, 0);
  assert.equal(JSON.parse(res.stdout).fromArchive, 1);
});

// --- audit: the live store vs the archive --------------------------------
// --verify checks the archive against its manifest; --audit checks the live
// store against the archive. Pure categorisation first, then behaviour.

test('auditCategorize buckets synced / changed / renamed / new / pruned by sha256', () => {
  const manifest = {
    'a.jsonl': { sha256: 'AA' },   // unchanged live
    'b.jsonl': { sha256: 'BB' },   // live differs → changed
    'c.jsonl': { sha256: 'CC' },   // live gone, content reappears at c2 → renamed
    'd.jsonl': { sha256: 'DD' },   // live gone, content unseen → pruned
  };
  const live = [
    { rel: 'a.jsonl', sha256: 'AA' },
    { rel: 'b.jsonl', sha256: 'BX' },
    { rel: 'c2.jsonl', sha256: 'CC' },   // c's content under a new path
    { rel: 'e.jsonl', sha256: 'EE' },    // wholly new
  ];
  const r = cc.auditCategorize(manifest, live);
  assert.deepEqual(r.synced, ['a.jsonl']);
  assert.deepEqual(r.changed, ['b.jsonl']);
  assert.deepEqual(r.renamed, [{ from: 'c.jsonl', to: 'c2.jsonl', ambiguous: false }]);
  assert.deepEqual(r.added, ['e.jsonl']);
  assert.deepEqual(r.pruned, ['d.jsonl']);
});

test('auditCategorize: a content match whose archived path is still live is a copy (new), not a rename', () => {
  const manifest = { 'a.jsonl': { sha256: 'AA' } };
  const live = [{ rel: 'a.jsonl', sha256: 'AA' }, { rel: 'copy.jsonl', sha256: 'AA' }];
  const r = cc.auditCategorize(manifest, live);
  assert.deepEqual(r.synced, ['a.jsonl']);
  assert.deepEqual(r.renamed, []);         // a.jsonl is present, so copy is not a move
  assert.deepEqual(r.added, ['copy.jsonl']);
});

test('classifyDivergence: a pure append is grown; a prefix loss is shrunk; anything else rewritten', () => {
  const base = Buffer.from('{"turn":1}\n{"turn":2}\n');
  assert.equal(cc.classifyDivergence(base, Buffer.concat([base, Buffer.from('{"turn":3}\n')])), 'grown');
  assert.equal(cc.classifyDivergence(base, base.subarray(0, 10)), 'shrunk');
  assert.equal(cc.classifyDivergence(base, Buffer.from('{"rewritten":true}\n')), 'rewritten');
  // Same length, different bytes → rewritten (the equal-content case never reaches here).
  assert.equal(cc.classifyDivergence(Buffer.from('aaaa'), Buffer.from('aaab')), 'rewritten');
});

test('contract: --audit on a store matching its archive is clean (exit 0, all synced)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const r = runCli('--audit', '--source', src, '--dest', dest, '--json');
  assert.equal(r.status, 0);
  const out = JSON.parse(r.stdout);
  assert.equal(out.synced, 3);
  assert.equal(out.mutated.length, 0);
  assert.equal(out.renamed.length, 0);
});

test('contract: --audit flags a rewritten live transcript as mutated (exit 1)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  // Rewrite a live file to different content of the same-ish length (not a growth).
  fs.writeFileSync(path.join(src, '-repo-b', 'uuid2.jsonl'), '{"rewritten":"whole"}\n');
  const r = runCli('--audit', '--source', src, '--dest', dest, '--json');
  assert.equal(r.status, 1);
  const out = JSON.parse(r.stdout);
  assert.equal(out.mutated.length, 1);
  assert.equal(out.mutated[0].rel, path.join('-repo-b', 'uuid2.jsonl'));
  assert.equal(out.mutated[0].reason, 'rewritten');
});

test('contract: --audit treats a pure append as grown, not drift (exit 0)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const f = path.join(src, '-repo-b', 'uuid2.jsonl');
  fs.appendFileSync(f, '{"turn":"appended"}\n');   // archived bytes stay a prefix
  const r = runCli('--audit', '--source', src, '--dest', dest, '--json');
  assert.equal(r.status, 0, 'a growth between archive runs is normal, not drift');
  const out = JSON.parse(r.stdout);
  assert.equal(out.grown, 1);
  assert.equal(out.mutated.length, 0);
});

test('contract: --audit flags a truncated live transcript as shrunk (exit 1)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const f = path.join(src, '-repo-a', 'uuid1.jsonl');   // was two turns
  fs.writeFileSync(f, '{"turn":1}\n');                   // a prefix of the archived bytes
  const r = runCli('--audit', '--source', src, '--dest', dest, '--json');
  assert.equal(r.status, 1);
  const out = JSON.parse(r.stdout);
  assert.equal(out.mutated.length, 1);
  assert.equal(out.mutated[0].reason, 'shrunk');
});

test('contract: --audit detects a renamed live transcript (exit 1, names old → new)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  // Move a live session to a new path without re-archiving it.
  fs.renameSync(path.join(src, '-repo-b', 'uuid2.jsonl'), path.join(src, '-repo-b', 'renamed.jsonl'));
  const r = runCli('--audit', '--source', src, '--dest', dest, '--json');
  assert.equal(r.status, 1);
  const out = JSON.parse(r.stdout);
  assert.equal(out.renamed.length, 1);
  assert.equal(out.renamed[0].from, path.join('-repo-b', 'uuid2.jsonl'));
  assert.equal(out.renamed[0].to, path.join('-repo-b', 'renamed.jsonl'));
});

test('contract: --audit counts a pruned source as expected, not drift (exit 0)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.rmSync(path.join(src, '-repo-b', 'uuid2.jsonl'));   // Claude Code cleanup
  const r = runCli('--audit', '--source', src, '--dest', dest, '--json');
  assert.equal(r.status, 0);
  const out = JSON.parse(r.stdout);
  assert.equal(out.pruned, 1);
  assert.equal(out.mutated.length, 0);
  assert.equal(out.renamed.length, 0);
});

test('contract: --audit counts an unarchived live file as new, not drift (exit 0)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.writeFileSync(path.join(src, '-repo-b', 'fresh.jsonl'), '{"brand":"new"}\n');
  const r = runCli('--audit', '--source', src, '--dest', dest, '--json');
  assert.equal(r.status, 0);
  const out = JSON.parse(r.stdout);
  assert.equal(out.added, 1);
  assert.equal(out.mutated.length, 0);
});

test('contract: --audit human output names drift and exits 1', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.writeFileSync(path.join(src, '-repo-b', 'uuid2.jsonl'), '{"rewritten":"whole"}\n');
  const r = runCli('--audit', '--source', src, '--dest', dest);
  assert.equal(r.status, 1);
  assert.match(r.stdout, /REWRITTEN.*uuid2\.jsonl/);
});

test('drift guard: every flag --help prints appears in the man page (superset relation)', () => {
  const help = execFileSync('node', [SCRIPT, '-h'], { encoding: 'utf8' });
  const page = fs.readFileSync(path.join(__dirname, 'man', 'ccarchive.1'), 'utf8');
  // Roff hyphenates flags as \-\-flag; normalise the page before matching.
  const pageFlat = page.replace(/\\-/g, '-');
  const flags = [...new Set(help.match(/--[\w-]+/g))];
  assert.ok(flags.length >= 8, `expected a real flag list, got ${flags.length}`);
  for (const flag of flags) {
    assert.ok(pageFlat.includes(flag), `man page must document ${flag} (--help is the digest, the page the superset)`);
  }
});
