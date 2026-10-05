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
const { execFileSync, spawnSync } = require('node:child_process');

const cc = require('./ccarchive');
const SCRIPT = path.join(__dirname, 'ccarchive');

// Manifest signing mints a key. Point it at a throwaway file so NO test ever
// writes into the real ~/.claude/ccarchive-signing.key (the default). Every
// spawned child inherits this via the environment, so archive runs sign under it.
// Signing-specific tests below override CCARCHIVE_KEYFILE per-run for isolation.
process.env.CCARCHIVE_KEYFILE =
  path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'ccarchive-key-')), 'signing.key');

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

// --- iCloud dataless-file awareness (pure) -------------------------------
// The bit-test is pure and exercised against the REAL st_flags value observed
// read-only on a genuinely dataless iCloud file (0x40000060 = SF_DATALESS +
// UF_COMPRESSED). Truly evicting a fixture is impossible on demand (and the tool
// must never evict anything), so real read-behaviour on an evicted file is
// unit-verified only through this classifier plus the simulate-seam tests below.

test('isDatalessFlags reads the SF_DATALESS bit (0x40000060 observed on a real evicted iCloud file)', () => {
  assert.equal(cc.isDatalessFlags(0x40000060), true);   // real value: dataless + compressed
  assert.equal(cc.isDatalessFlags(0x40000000), true);   // bare SF_DATALESS
  assert.equal(cc.isDatalessFlags(0x20), false);        // UF_COMPRESSED only — bytes still local
  assert.equal(cc.isDatalessFlags(0), false);           // ordinary file
  assert.equal(cc.isDatalessFlags(NaN), false);         // unparseable stat → treated as not evicted
});

test('isDataless is false for an ordinary local file and honours the simulate seam', () => {
  assert.equal(cc.isDataless(SCRIPT), false, 'this script is local — flags 0, not evicted');
  process.env.CCARCHIVE_SIMULATE_DATALESS = 'ccarchive';   // substring of SCRIPT's path
  try { assert.equal(cc.isDataless(SCRIPT), true, 'the seam forces the classification for tests'); }
  finally { delete process.env.CCARCHIVE_SIMULATE_DATALESS; }
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

// --- no scheduler (210/190) -----------------------------------------------
// ccarchive is run by hand. The old install/status/uninstall flags are refused by
// name — never silently ignored, which would run an ordinary archive instead.

test('the removed schedule flags are refused by name (exit 2), not run as an archive', () => {
  // Safety rail: these flags once wrote and loaded a real launchd job. Never spawn
  // them against a script that still carries that code (e.g. a copy of an old
  // version) — refuse to run the test at all, and point HOME at a throwaway dir.
  const scriptText = fs.readFileSync(SCRIPT, 'utf8');
  assert.ok(!/launchctl|LaunchAgents/.test(scriptText),
    'SCRIPT still contains scheduler code; refusing to spawn the removed flags against it');
  const { dir, src, dest } = makeTree();
  const env = { ...process.env, HOME: path.join(dir, 'fake-home') };
  for (const flag of ['--install-schedule', '--schedule-status', '--uninstall-schedule']) {
    const r = spawnSync('node', [SCRIPT, flag, '--source', src, '--dest', dest], { encoding: 'utf8', env });
    assert.equal(r.status, 2, `${flag} must fail`);
    assert.match(r.stderr, new RegExp(`${flag} was removed`));
    assert.doesNotMatch(r.stderr, /\n\s+at /, 'one clean line, no stack trace');
    assert.ok(!fs.existsSync(dest), `${flag} must not fall through to an archive run`);
  }
});

test('--help and the man page say the tool is run by hand and carry no scheduler flag', () => {
  const help = execFileSync('node', [SCRIPT, '-h'], { encoding: 'utf8' });
  assert.doesNotMatch(help, /schedule(?!\.)/, '--help offers no schedule flag');
  assert.match(help, /Run by hand/);
  const page = fs.readFileSync(path.join(__dirname, 'man', 'ccarchive.1'), 'utf8').replace(/\\-/g, '-');
  assert.match(page, /run by hand/i);
  assert.doesNotMatch(page, /^\.TP\n\.B --(install|uninstall)-schedule|^\.TP\n\.B --schedule-status/m,
    'no OPTIONS entry for a scheduler flag');
});

// --- integrity: sha256 manifest + verify ---------------------------------

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
  assert.deepEqual(fs.readdirSync(dir), ['manifest.json'], 'no temp file left in the directory');
});

// --- documentation convention (REPO-STANDARD: concise --help + a man page) --

test('--help is a concise digest that points at the man page', () => {
  const help = execFileSync('node', [SCRIPT, '-h'], { encoding: 'utf8' });
  assert.ok(help.split('\n').length <= 22, '--help should stay a one-screen digest');
  assert.match(help, /man ccarchive/, '--help must point at the full manual');
  for (const opt of ['--dest', '--verify', '--restore']) assert.ok(help.includes(opt));
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

// --- iCloud dataless awareness: --verify / --audit skip + --materialise --
// Fixtures can never be truly evicted, so behaviour is driven through the
// CCARCHIVE_SIMULATE_DATALESS seam (comma-separated path substrings the CLI
// treats as dataless). The tamper trick proves the SKIP means no read: a .gz
// corrupted to mismatch its manifest hash would fail a real --verify, so an
// exit-0 with it in `evicted` (not `mismatch`) can only mean it was never read.
function runCliSim(sim, ...args) {
  const r = spawnSync('node', [SCRIPT, ...args],
    { encoding: 'utf8', env: { ...process.env, CCARCHIVE_SIMULATE_DATALESS: sim } });
  return { status: r.status, stdout: r.stdout, stderr: r.stderr };
}

test('contract: --verify skips a dataless archive file (evicted, not read → exit 0 despite a tamper)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const rel = path.join('-repo-b', 'uuid2.jsonl');
  // Corrupt the .gz so a REAL read would MISMATCH — the skip is what keeps it green.
  fs.writeFileSync(path.join(dest, rel + '.gz'), zlib.gzipSync(Buffer.from('{"tampered":true}\n')));
  const r = runCliSim('uuid2', '--verify', '--json', '--dest', dest);
  assert.equal(r.status, 0, 'an evicted file is intact-in-cloud, not a verify failure');
  const out = JSON.parse(r.stdout);
  assert.deepEqual(out.evicted, [rel]);
  assert.equal(out.mismatch.length, 0, 'skipped, not read — so the tamper is not seen');
  assert.equal(out.ok, 2, 'the two non-evicted files still verify');
});

test('contract: --verify --materialise reads the dataless file (faults it back), catching the tamper (exit 1)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const rel = path.join('-repo-b', 'uuid2.jsonl');
  fs.writeFileSync(path.join(dest, rel + '.gz'), zlib.gzipSync(Buffer.from('{"tampered":true}\n')));
  const r = runCliSim('uuid2', '--verify', '--materialise', '--json', '--dest', dest);
  assert.equal(r.status, 1, 'materialise reads it, so the tamper is caught');
  const out = JSON.parse(r.stdout);
  assert.deepEqual(out.mismatch, [rel]);
  assert.equal(out.evicted.length, 0);
});

test('contract: --verify human output names the evicted skip without claiming it was verified', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const r = runCliSim('uuid2', '--verify', '--dest', dest);
  assert.equal(r.status, 0);
  assert.match(r.stdout, /1 evicted/);
  assert.match(r.stdout, /every checked transcript matches/);  // NOT "every archived"
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

test('contract: --audit leaves a changed file undetermined when its archive copy is dataless (exit 0)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.writeFileSync(path.join(src, '-repo-b', 'uuid2.jsonl'), '{"rewritten":"whole"}\n');  // would be mutated
  const r = runCliSim('uuid2', '--audit', '--json', '--source', src, '--dest', dest);
  assert.equal(r.status, 0, 'an undetermined (evicted archive copy) file is not proven drift');
  const out = JSON.parse(r.stdout);
  assert.equal(out.mutated.length, 0, 'not classified — the archived bytes were not faulted back');
  assert.deepEqual(out.evicted.map((e) => e.rel), [path.join('-repo-b', 'uuid2.jsonl')]);
});

test('contract: --audit --materialise reads the dataless archive copy and flags the mutation (exit 1)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.writeFileSync(path.join(src, '-repo-b', 'uuid2.jsonl'), '{"rewritten":"whole"}\n');
  const r = runCliSim('uuid2', '--audit', '--materialise', '--json', '--source', src, '--dest', dest);
  assert.equal(r.status, 1);
  const out = JSON.parse(r.stdout);
  assert.equal(out.mutated.length, 1);
  assert.equal(out.evicted.length, 0);
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

// --- restore: archive → live store ---------------------------------------
// The inverse of --audit. Pure decision helpers first, then the two shapes
// (full / delta) driven over a fixture tree: bucket by bucket, plus the two
// safety rails — the newer-live refusal and the grown-bucket exclusion.

function runRestore(src, dest, ...flags) {
  const r = spawnSync('node', [SCRIPT, '--restore', '--json', '--source', src, '--dest', dest, ...flags],
    { encoding: 'utf8' });
  return { status: r.status, report: r.stdout ? JSON.parse(r.stdout) : null, stderr: r.stderr };
}

// The archived copy's stamped mtime (ms) — the reference the newer-live rule uses.
function gzMtimeMs(dest, rel) {
  return fs.statSync(path.join(dest, rel + '.gz')).mtimeMs;
}

test('classifyRestore: no live file is a plain restore (missing)', () => {
  const a = Buffer.from('{"turn":1}\n');
  assert.deepEqual(cc.classifyRestore(a, null, 1000, null, false), { action: 'restore', reason: 'missing' });
});

test('classifyRestore: an identical live file is skipped, never rewritten', () => {
  const a = Buffer.from('{"turn":1}\n');
  assert.deepEqual(cc.classifyRestore(a, Buffer.from('{"turn":1}\n'), 1000, 9999, false),
    { action: 'skip', reason: 'identical' });   // newer mtime is irrelevant when bytes match
});

test('classifyRestore: a live file the archive is a prefix of is ahead (grown) — skipped, not a target', () => {
  const a = Buffer.from('{"turn":1}\n');
  const live = Buffer.from('{"turn":1}\n{"turn":2}\n');   // archive is a strict prefix
  assert.deepEqual(cc.classifyRestore(a, live, 1000, 500, false), { action: 'skip', reason: 'ahead' });
});

test('classifyRestore: a diverged, newer live file is refused unless forced', () => {
  const a = Buffer.from('{"turn":1}\n{"turn":2}\n');
  const live = Buffer.from('{"rewritten":true}\n');
  assert.deepEqual(cc.classifyRestore(a, live, 1000, 5000, false), { action: 'refuse', reason: 'newer' });
  assert.deepEqual(cc.classifyRestore(a, live, 1000, 5000, true), { action: 'restore', reason: 'forced-newer' });
});

test('classifyRestore: a diverged, not-newer live file restores (the archive is at least as recent)', () => {
  const a = Buffer.from('{"turn":1}\n{"turn":2}\n');
  assert.deepEqual(cc.classifyRestore(a, Buffer.from('{"rewritten":true}\n'), 5000, 1000, false),
    { action: 'restore', reason: 'rewritten' });
  assert.deepEqual(cc.classifyRestore(a, a.subarray(0, 5), 5000, 1000, false),
    { action: 'restore', reason: 'shrunk' });
});

test('isInsideRoot: a target under the root passes; an equal or escaping path fails', () => {
  assert.equal(cc.isInsideRoot('/src', '/src/-repo/a.jsonl'), true);
  assert.equal(cc.isInsideRoot('/src', '/src'), false);              // the root itself is not a target
  assert.equal(cc.isInsideRoot('/src', '/src/../evil.jsonl'), false); // zip-slip escape
  assert.equal(cc.isInsideRoot('/src', '/elsewhere/x.jsonl'), false);
});

test('contract: --restore with no manifest exits 1 (nothing to restore from)', () => {
  const { dir } = makeTree();
  const emptyDest = path.join(dir, 'empty-archive');
  const r = runRestore(path.join(dir, 'projects'), emptyDest);
  assert.equal(r.status, 1);
  assert.match(r.stderr, /nothing to restore/);
});

test('contract: full --restore rebuilds a wiped live store, byte-identical, and re-audits clean', () => {
  const { dir, src, dest } = makeTree();
  runJson(src, dest);                                   // archive all three
  const originals = {};
  for (const rel of ['-repo-a/uuid1.jsonl', '-repo-a/uuid1/subagents/agent-x.jsonl', '-repo-b/uuid2.jsonl']) {
    originals[rel] = fs.readFileSync(path.join(src, rel));
  }
  fs.rmSync(src, { recursive: true });                  // the whole live store is lost
  assert.ok(!fs.existsSync(src));

  const r = runRestore(src, dest);
  assert.equal(r.status, 0);
  assert.equal(r.report.mode, 'full');
  assert.equal(r.report.restored.length, 3);
  for (const [rel, bytes] of Object.entries(originals)) {
    assert.deepEqual(fs.readFileSync(path.join(src, rel)), bytes, `${rel} restored byte-identical`);
  }
  // The rebuilt store now matches the archive.
  assert.equal(runCli('--audit', '--source', src, '--dest', dest, '--json').status, 0);
});

test('contract: full --restore is idempotent — a second run skips every identical file (exit 0)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const r = runRestore(src, dest);                      // store already matches archive
  assert.equal(r.status, 0);
  assert.equal(r.report.restored.length, 0);
  assert.equal(r.report.skipped.filter((s) => s.reason === 'identical').length, 3);
});

test('contract: delta --restore repairs a mutated live file, leaving synced siblings alone', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const rel = path.join('-repo-b', 'uuid2.jsonl');
  const f = path.join(src, rel);
  const archived = zlib.gunzipSync(fs.readFileSync(path.join(dest, rel + '.gz')));
  fs.writeFileSync(f, '{"rewritten":"whole"}\n');       // mutated (not a growth)
  const past = gzMtimeMs(dest, rel) / 1000 - 10;        // older than the archive → not in-flight
  fs.utimesSync(f, past, past);

  const r = runRestore(src, dest, '--delta');
  assert.equal(r.status, 0);
  assert.equal(r.report.mode, 'delta');
  assert.equal(r.report.considered, 1);                 // only the mutated file is a target
  assert.equal(r.report.restored.length, 1);
  assert.equal(r.report.restored[0].rel, rel);
  assert.equal(r.report.restored[0].reason, 'rewritten');
  assert.deepEqual(fs.readFileSync(f), archived, 'the mutated file is back to the archived bytes');
});

test('contract: delta --restore rehydrates a pruned (deleted) live file', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const rel = path.join('-repo-b', 'uuid2.jsonl');
  const archived = zlib.gunzipSync(fs.readFileSync(path.join(dest, rel + '.gz')));
  fs.rmSync(path.join(src, rel));                        // Claude Code cleanup / accidental delete

  const r = runRestore(src, dest, '--delta');
  assert.equal(r.status, 0);
  assert.equal(r.report.restored.length, 1);
  assert.equal(r.report.restored[0].reason, 'missing');
  assert.deepEqual(fs.readFileSync(path.join(src, rel)), archived);
});

test('contract: delta --restore re-materialises a renamed OLD path and leaves the live rename untouched', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const from = path.join('-repo-b', 'uuid2.jsonl');
  const to = path.join('-repo-b', 'renamed.jsonl');
  const archived = zlib.gunzipSync(fs.readFileSync(path.join(dest, from + '.gz')));
  fs.renameSync(path.join(src, from), path.join(src, to));   // move without re-archiving

  const r = runRestore(src, dest, '--delta');
  assert.equal(r.status, 0);
  assert.equal(r.report.restored.length, 1);
  assert.equal(r.report.restored[0].rel, from, 'restores the archived (old) path');
  // Old path re-materialised from the archive…
  assert.deepEqual(fs.readFileSync(path.join(src, from)), archived);
  // …and the live renamed copy at the new path is left exactly as it was.
  assert.deepEqual(fs.readFileSync(path.join(src, to)), archived);
});

test('contract: the grown bucket is never a restore target — full skips it (ahead), delta ignores it', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const rel = path.join('-repo-b', 'uuid2.jsonl');
  const f = path.join(src, rel);
  fs.appendFileSync(f, '{"turn":"appended-in-flight"}\n');   // archived bytes stay a prefix → grown
  const grownBytes = fs.readFileSync(f);

  // Full restore must NOT clobber it — the live tail would be lost.
  const full = runRestore(src, dest);
  assert.equal(full.status, 0);
  assert.equal(full.report.restored.find((x) => x.rel === rel), undefined, 'grown file is not restored');
  assert.ok(full.report.skipped.some((s) => s.rel === rel && s.reason === 'ahead'));
  assert.deepEqual(fs.readFileSync(f), grownBytes, 'the in-flight append survives a full restore');

  // Delta restore does not even consider it (it is not audit drift).
  const delta = runRestore(src, dest, '--delta');
  assert.equal(delta.status, 0);
  assert.equal(delta.report.considered, 0);
  assert.deepEqual(fs.readFileSync(f), grownBytes);
});

test('contract: a mutated live file NEWER than the archive is refused (exit 1), untouched; --force overwrites', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const rel = path.join('-repo-b', 'uuid2.jsonl');
  const f = path.join(src, rel);
  const archived = zlib.gunzipSync(fs.readFileSync(path.join(dest, rel + '.gz')));
  fs.writeFileSync(f, '{"maybe":"in-flight rewrite"}\n');    // diverged, not a growth
  const future = gzMtimeMs(dest, rel) / 1000 + 10;           // newer than the archive
  fs.utimesSync(f, future, future);
  const mutatedBytes = fs.readFileSync(f);

  const refused = runRestore(src, dest, '--delta');
  assert.equal(refused.status, 1, 'a newer live file must not be silently overwritten');
  assert.equal(refused.report.refused.length, 1);
  assert.equal(refused.report.refused[0].rel, rel);
  assert.equal(refused.report.refused[0].reason, 'newer');
  assert.deepEqual(fs.readFileSync(f), mutatedBytes, 'the live file is left intact behind the refusal');

  // The human report also names the refusal on a non-zero exit.
  const human = runCli('--restore', '--delta', '--source', src, '--dest', dest);
  assert.equal(human.status, 1);
  assert.match(human.stdout, /REFUSED.*uuid2\.jsonl/);
  assert.match(human.stdout, /newer than the archived copy/);

  // --force is the deliberate override.
  const forced = runRestore(src, dest, '--delta', '--force');
  assert.equal(forced.status, 0);
  assert.equal(forced.report.restored.length, 1);
  assert.equal(forced.report.restored[0].reason, 'forced-newer');
  assert.deepEqual(fs.readFileSync(f), archived);
});

test('contract: --restore --dry-run previews the plan and writes nothing', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const rel = path.join('-repo-b', 'uuid2.jsonl');
  fs.rmSync(path.join(src, rel));                            // a pruned file to rehydrate
  const r = runRestore(src, dest, '--delta', '--dry-run');
  assert.equal(r.status, 0);
  assert.equal(r.report.dryRun, true);
  assert.equal(r.report.restored.length, 1);                // reported…
  assert.ok(!fs.existsSync(path.join(src, rel)), '…but nothing written on a dry run');
});

test('contract: restore refuses a manifest key that would escape the live root (exit 1, writes nothing outside)', () => {
  const { dir } = makeTree();
  const src = path.join(dir, 'restore-target');
  const dest = path.join(dir, 'evil-archive');
  fs.mkdirSync(src, { recursive: true });
  // A hand-built manifest whose key climbs out of the source tree (zip-slip).
  cc.saveManifest(dest, { '../escaped.jsonl': { sha256: 'x', rawBytes: 1 } });
  const escapee = path.join(dir, 'escaped.jsonl');
  assert.ok(!fs.existsSync(escapee));

  const r = runRestore(src, dest);
  assert.equal(r.status, 1);
  assert.equal(r.report.errors.length, 1);
  assert.equal(r.report.errors[0].reason, 'escapes-root');
  assert.ok(!fs.existsSync(escapee), 'no write may land outside the live root');
});

test('contract: restore reports a manifest entry whose .gz is gone as an error (exit 1)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const rel = path.join('-repo-b', 'uuid2.jsonl');
  fs.rmSync(path.join(src, rel));                            // pruned live…
  fs.rmSync(path.join(dest, rel + '.gz'));                   // …and the archive copy is also gone
  const r = runRestore(src, dest, '--delta');
  assert.equal(r.status, 1);
  assert.equal(r.report.errors.length, 1);
  assert.equal(r.report.errors[0].reason, 'no-archive');
});

// --- manifest signing: tamper-evidence (HMAC-SHA256) ---------------------
// The sha256 manifest catches accidental corruption but not a tamperer who
// rewrites a .gz AND the manifest to match. Signing closes that: a detached
// HMAC over the manifest bytes, keyed off the archive volume. Pure verdict units
// first, then the write→verify→tamper behaviour, then failure semantics and
// rotation. Every spawn runs under a throwaway CCARCHIVE_KEYFILE (top of file);
// tests needing key isolation override it per-run.
const crypto = require('node:crypto');

// A run under a specific signing-key file (isolates no-key / wrong-key / rekey).
function runCliKey(keyFile, ...args) {
  const r = spawnSync('node', [SCRIPT, ...args],
    { encoding: 'utf8', env: { ...process.env, CCARCHIVE_KEYFILE: keyFile } });
  return { status: r.status, stdout: r.stdout, stderr: r.stderr };
}
function freshKeyFile() {
  return path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'ccarchive-k-')), 'k.key');
}

test('keyId is a stable 12-hex fingerprint; distinct keys fingerprint distinctly', () => {
  const k = crypto.randomBytes(32);
  assert.match(cc.keyId(k), /^[0-9a-f]{12}$/);
  assert.equal(cc.keyId(k), cc.keyId(Buffer.from(k)));            // deterministic
  assert.notEqual(cc.keyId(k), cc.keyId(crypto.randomBytes(32))); // key-dependent
});

test('macEqual is a constant-time hex compare that rejects malformed / short input', () => {
  const a = crypto.createHmac('sha256', 'k').update('x').digest('hex');
  assert.equal(cc.macEqual(a, a), true);
  assert.equal(cc.macEqual(a, a.slice(0, -2) + '00'), false);
  assert.equal(cc.macEqual(a, 'deadbeef'), false);   // length mismatch
  assert.equal(cc.macEqual(a, 'nothex!!'), false);   // unparseable
  assert.equal(cc.macEqual('', ''), false);          // empty is never a match
});

test('verifySignature: verified / tampered / key-mismatch / unsigned / no-key', () => {
  const key = crypto.randomBytes(32);
  const bytes = Buffer.from('{"a.jsonl":{"sha256":"1"}}\n');
  const good = { algorithm: 'HMAC-SHA256', keyId: cc.keyId(key), mac: cc.computeMac(key, bytes) };

  assert.equal(cc.verifySignature(bytes, good, key).state, 'verified');
  // Manifest bytes changed after signing → same key, MAC no longer matches.
  assert.equal(cc.verifySignature(Buffer.from('{"a.jsonl":{"sha256":"2"}}\n'), good, key).state, 'tampered');
  // A signature made by a different key.
  const other = crypto.randomBytes(32);
  const foreign = { algorithm: 'HMAC-SHA256', keyId: cc.keyId(other), mac: cc.computeMac(other, bytes) };
  assert.equal(cc.verifySignature(bytes, foreign, key).state, 'key-mismatch');
  // No signature at all, but a key present → migratable.
  assert.equal(cc.verifySignature(bytes, null, key).state, 'unsigned');
  // No key → unverifiable, whether or not a sig is present.
  assert.equal(cc.verifySignature(bytes, good, null).state, 'no-key');
  assert.equal(cc.verifySignature(bytes, null, null).state, 'no-key');
});

test('contract: an archive run signs the manifest (sidecar written) and --verify reports it verified', () => {
  const { src, dest } = makeTree();
  const j = runJson(src, dest);
  assert.equal(j.signed, true);
  const sig = JSON.parse(fs.readFileSync(path.join(dest, 'manifest.json.sig'), 'utf8'));
  assert.equal(sig.algorithm, 'HMAC-SHA256');
  assert.match(sig.mac, /^[0-9a-f]{64}$/);
  // The MAC is over the exact manifest bytes.
  const key = cc.loadKey(process.env.CCARCHIVE_KEYFILE);
  assert.equal(sig.mac, cc.computeMac(key, fs.readFileSync(path.join(dest, 'manifest.json'))));

  const r = runCli('--verify', '--dest', dest, '--json');
  assert.equal(r.status, 0);
  assert.equal(JSON.parse(r.stdout).signature.state, 'verified');

  const human = runCli('--verify', '--dest', dest);
  assert.match(human.stdout, /manifest signature verified/);
});

test('contract: editing any manifest byte (no hash change) is caught by the signature alone (exit 1)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  // Flip a non-hash field: the .gz still matches its recorded sha256, so the hash
  // pass is untouched — only the signature can catch this.
  const mf = cc.loadManifest(dest);
  mf['-repo-b/uuid2.jsonl'].archivedAt = '1999-01-01T00:00:00.000Z';
  cc.saveManifest(dest, mf);                                 // rewrites bytes, does NOT re-sign
  const r = runCli('--verify', '--dest', dest, '--json');
  assert.equal(r.status, 1);
  const out = JSON.parse(r.stdout);
  assert.equal(out.signature.state, 'tampered');
  assert.equal(out.mismatch.length, 0, 'the hash check still passes — the signature is what fails');
});

test('contract: the closed caveat — a rewritten .gz AND a matching manifest hash is still caught (exit 1)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const rel = '-repo-b/uuid2.jsonl';
  // A sophisticated tamperer: forge the transcript AND update the manifest hash so
  // the sha256 check would pass. Before signing, --verify passed here (the caveat).
  const forged = Buffer.from('{"forged":"history"}\n');
  fs.writeFileSync(path.join(dest, rel + '.gz'), zlib.gzipSync(forged));
  const mf = cc.loadManifest(dest);
  mf[rel].sha256 = cc.sha256(forged);                        // hash now matches the forgery
  cc.saveManifest(dest, mf);                                 // …but the tamperer can't re-sign
  const r = runCli('--verify', '--dest', dest, '--json');
  assert.equal(r.status, 1, 'the signature catches what the hash cannot');
  const out = JSON.parse(r.stdout);
  assert.equal(out.mismatch.length, 0, 'hash agrees with the forged .gz — the OLD gap');
  assert.equal(out.signature.state, 'tampered', 'the manifest no longer matches its signature');
});

test('contract: --verify with no key is UNVERIFIABLE, not green — never silently passes (exit 1)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);                                        // signed under the shared test key
  const absent = path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'ccarchive-nokey-')), 'missing.key');
  const r = runCliKey(absent, '--verify', '--dest', dest, '--json');
  assert.equal(r.status, 1, 'an unverifiable signature must not exit 0');
  assert.equal(JSON.parse(r.stdout).signature.state, 'no-key');
  assert.ok(!fs.existsSync(absent), '--verify must NOT mint a key (that would defeat the check)');
});

test('contract: a missing signature on a key-present archive prompts migration, not green (exit 1)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.rmSync(path.join(dest, 'manifest.json.sig'));           // legacy / removed signature
  const r = runCli('--verify', '--dest', dest, '--json');
  assert.equal(r.status, 1);
  assert.equal(JSON.parse(r.stdout).signature.state, 'unsigned');
  assert.match(runCli('--verify', '--dest', dest).stdout, /NOT signed/);
});

test('contract: a legacy unsigned manifest is migrated (signed) by the next ordinary run', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.rmSync(path.join(dest, 'manifest.json.sig'));           // simulate a pre-signing archive
  assert.equal(runCli('--verify', '--dest', dest, '--json').status, 1);   // unsigned → fails
  runJson(src, dest);                                        // an ordinary run re-signs it
  const r = runCli('--verify', '--dest', dest, '--json');
  assert.equal(r.status, 0);
  assert.equal(JSON.parse(r.stdout).signature.state, 'verified');
});

test('contract: a signature from a different key is flagged key-mismatch (exit 1)', () => {
  const { src, dest } = makeTree();
  const keyA = freshKeyFile();
  runCliKey(keyA, '--json', '--source', src, '--dest', dest);   // signed by key A
  const keyB = freshKeyFile();
  cc.mintKey(keyB);                                             // a real, different key
  const r = runCliKey(keyB, '--verify', '--dest', dest, '--json');   // verified with key B
  assert.equal(r.status, 1);
  assert.equal(JSON.parse(r.stdout).signature.state, 'key-mismatch');
});

test('contract: --rekey rolls the key and re-signs; the old key no longer verifies, the new one does', () => {
  const { src, dest } = makeTree();
  const key = freshKeyFile();
  runCliKey(key, '--json', '--source', src, '--dest', dest);
  const before = fs.readFileSync(key, 'utf8');
  const oldSigMac = JSON.parse(fs.readFileSync(path.join(dest, 'manifest.json.sig'), 'utf8')).mac;

  const rk = runCliKey(key, '--rekey', '--dest', dest, '--json');
  assert.equal(rk.status, 0);
  const out = JSON.parse(rk.stdout);
  assert.equal(out.rekeyed, true);
  assert.equal(out.manifestSigned, true);
  assert.notEqual(fs.readFileSync(key, 'utf8'), before, 'the key file was replaced');
  const newSigMac = JSON.parse(fs.readFileSync(path.join(dest, 'manifest.json.sig'), 'utf8')).mac;
  assert.notEqual(newSigMac, oldSigMac, 'the manifest was re-signed under the new key');

  // The rolled-in key verifies the re-signed manifest.
  assert.equal(runCliKey(key, '--verify', '--dest', dest, '--json').status, 0);
});

test('contract: --rekey with no manifest yet still mints a ready key (exit 0)', () => {
  const dest = fs.mkdtempSync(path.join(os.tmpdir(), 'ccarchive-rk-'));
  const key = freshKeyFile();
  const rk = runCliKey(key, '--rekey', '--dest', dest, '--json');
  assert.equal(rk.status, 0);
  assert.equal(JSON.parse(rk.stdout).manifestSigned, false);
  assert.ok(fs.existsSync(key), 'the key is minted even without a manifest to sign');
});

test('the signing key is minted mode 0600 (readable only by its owner)', () => {
  const { src, dest } = makeTree();
  const key = freshKeyFile();
  runCliKey(key, '--json', '--source', src, '--dest', dest);
  assert.equal(fs.statSync(key).mode & 0o777, 0o600);
});

test('defaultKeyFile is under ~/.claude and CCARCHIVE_KEYFILE overrides it', () => {
  assert.equal(cc.defaultKeyFile('/Users/x'), '/Users/x/.claude/ccarchive-signing.key');
  const saved = process.env.CCARCHIVE_KEYFILE;
  try {
    process.env.CCARCHIVE_KEYFILE = '/tmp/override.key';
    assert.equal(cc.resolveKeyPath('/Users/x'), '/tmp/override.key');
    delete process.env.CCARCHIVE_KEYFILE;
    assert.equal(cc.resolveKeyPath('/Users/x'), '/Users/x/.claude/ccarchive-signing.key');
  } finally { process.env.CCARCHIVE_KEYFILE = saved; }
});

// --- widened capture: tool-result sidecars, memory, top-level history -----
// ccarchive keys everything on the source-relative path + ".gz", so a non-.jsonl
// file is first-class the moment the walk allowlists it. These tests cover the
// three new classes end to end (capture → verify → audit → restore), the
// documented exclusions, the external history.jsonl reach-up, and backwards
// compatibility with an archive written before the classes existed.

// A wider fixture than makeTree(): a transcript, a subagent log with its
// metadata sidecar, both tool-result sidecar shapes (modern tool-results/ and
// legacy toolu_), two memory .md files, an excluded WebFetch PDF, an excluded
// .meta.json OUTSIDE subagents/ (the scoping decision, exercised end to end),
// and the top-level history.jsonl that lives ONE LEVEL ABOVE projects/.
// Every byte here is synthetic: no real session, agent id or path appears.
function makeWideTree() {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ccarchive-wide-'));
  const src = path.join(dir, 'projects');
  const dest = path.join(dir, 'archive');
  const uuidDir = path.join(src, '-repo-a', 'uuid1');
  fs.mkdirSync(path.join(uuidDir, 'tool-results'), { recursive: true });
  fs.mkdirSync(path.join(uuidDir, 'subagents'), { recursive: true });
  fs.mkdirSync(path.join(src, '-repo-a', 'memory'), { recursive: true });
  fs.writeFileSync(path.join(src, '-repo-a', 'uuid1.jsonl'), '{"turn":1}\n');
  fs.writeFileSync(path.join(uuidDir, 'subagents', 'agent-a1.jsonl'), '{"sub":true}\n');
  fs.writeFileSync(path.join(uuidDir, 'subagents', 'agent-a1.meta.json'),
    JSON.stringify({ agentType: 'general-purpose', description: 'a synthetic agent',
      toolUseId: 'toolu_synthetic', spawnDepth: 1, model: 'a-model' }) + '\n');
  fs.writeFileSync(path.join(uuidDir, 'tool-results', 'big-output.txt'), 'LARGE TOOL OUTPUT PAYLOAD\n');
  fs.writeFileSync(path.join(uuidDir, 'toolu_01ABC.json'), '{"legacy":"sidecar"}\n');
  fs.writeFileSync(path.join(src, '-repo-a', 'memory', 'MEMORY.md'), '# index\n- entry\n');
  fs.writeFileSync(path.join(src, '-repo-a', 'memory', 'entry.md'), 'some learned context\n');
  fs.writeFileSync(path.join(src, '-repo-a', 'webfetch-abc.pdf'), '%PDF-1.4 fake\n');   // excluded
  fs.writeFileSync(path.join(src, '-repo-a', 'stray.meta.json'), '{"outside":"subagents"}\n'); // excluded
  fs.writeFileSync(path.join(dir, 'history.jsonl'), '{"prompt":"hi"}\n');               // above projects/
  return { dir, src, dest };
}

test('captureClass allowlists transcripts, subagent metadata, tool-result sidecars and memory; excludes the rest', () => {
  assert.equal(cc.captureClass(path.join('-repo', 'uuid.jsonl')), 'transcript');
  assert.equal(cc.captureClass(path.join('-repo', 'uuid', 'subagents', 'a.jsonl')), 'transcript');
  assert.equal(cc.captureClass(path.join('-repo', 'uuid', 'subagents', 'a.meta.json')), 'subagent-meta');
  assert.equal(cc.captureClass(path.join('-repo', 'uuid', 'tool-results', 'big.txt')), 'tool-result');
  assert.equal(cc.captureClass(path.join('-repo', 'uuid', 'tool-results', 'big.json')), 'tool-result');
  assert.equal(cc.captureClass(path.join('-repo', 'uuid', 'toolu_01ABC.txt')), 'tool-result');
  assert.equal(cc.captureClass(path.join('-repo', 'memory', 'MEMORY.md')), 'memory');
  assert.equal(cc.captureClass(path.join('-repo', 'memory', 'entry.md')), 'memory');
  // Excluded by allowlist — an unrecognised file is not swept in.
  assert.equal(cc.captureClass(path.join('-repo', 'webfetch-abc.pdf')), null);
  assert.equal(cc.captureClass(path.join('-repo', 'notes.txt')), null);
  assert.equal(cc.captureClass(path.join('-repo', 'README.md')), null);   // .md NOT under memory/
});

// The recorded judgement: the subagent-meta class is matched by name but SCOPED
// to a subagents/ directory, so an unseen .meta.json elsewhere stays excluded by
// default like any other unrecognised file. Pinned as a test because the two
// readings are indistinguishable on today's store (every real sidecar sits under
// subagents/) and only a test keeps the narrower one from drifting wider.
test('captureClass scopes the subagent .meta.json to a subagents/ directory, not *.meta.json anywhere', () => {
  assert.equal(cc.captureClass(path.join('-repo', 'uuid', 'subagents', 'agent-a1.meta.json')), 'subagent-meta');
  // Nested deeper under subagents/ still counts — the check is on the path, not a fixed depth.
  assert.equal(cc.captureClass(path.join('-repo', 'uuid', 'subagents', 'nested', 'a.meta.json')), 'subagent-meta');
  // Outside subagents/, a .meta.json is NOT captured, at any level.
  assert.equal(cc.captureClass(path.join('-repo', 'stray.meta.json')), null);
  assert.equal(cc.captureClass(path.join('-repo', 'uuid', 'stray.meta.json')), null);
  assert.equal(cc.captureClass(path.join('-repo', 'uuid', 'tool-results', 'x.meta.json')), 'tool-result');
  // A subagents/ file that is neither a log nor a .meta.json is still excluded.
  assert.equal(cc.captureClass(path.join('-repo', 'uuid', 'subagents', 'scratch.txt')), null);
});

test('listCaptured mirrors the allowlist across a wide tree and skips the WebFetch PDF', () => {
  const { src } = makeWideTree();
  const found = cc.listCaptured(src).map((p) => path.relative(src, p)).sort();
  assert.deepEqual(found, [
    path.join('-repo-a', 'memory', 'MEMORY.md'),
    path.join('-repo-a', 'memory', 'entry.md'),
    path.join('-repo-a', 'uuid1.jsonl'),
    path.join('-repo-a', 'uuid1', 'subagents', 'agent-a1.jsonl'),
    path.join('-repo-a', 'uuid1', 'subagents', 'agent-a1.meta.json'),
    path.join('-repo-a', 'uuid1', 'tool-results', 'big-output.txt'),
    path.join('-repo-a', 'uuid1', 'toolu_01ABC.json'),
  ].sort());
});

test('history.jsonl is reached one level above the source root and keyed under _external/', () => {
  assert.equal(cc.historySource(path.join('/x', '.claude', 'projects')),
    path.join('/x', '.claude', 'history.jsonl'));
  assert.deepEqual(cc.externalSources(path.join('/x', '.claude', 'projects')),
    [{ abs: path.join('/x', '.claude', 'history.jsonl'), rel: path.join('_external', 'history.jsonl') }]);
  // CCARCHIVE_HISTORY overrides the reach-up for testing/relocation.
  process.env.CCARCHIVE_HISTORY = '/tmp/h.jsonl';
  try { assert.equal(cc.historySource(path.join('/x', '.claude', 'projects')), '/tmp/h.jsonl'); }
  finally { delete process.env.CCARCHIVE_HISTORY; }
});

test('liveAbsFor redirects an external rel above the source root, mirrors ordinary rels under it', () => {
  const src = path.join('/x', '.claude', 'projects');
  assert.equal(cc.liveAbsFor(src, path.join('_external', 'history.jsonl')),
    path.join('/x', '.claude', 'history.jsonl'));
  assert.equal(cc.liveAbsFor(src, path.join('-repo', 'uuid.jsonl')),
    path.join(src, '-repo', 'uuid.jsonl'));
});

test('contract: a wide run captures sidecars, memory and history byte-identical, and verifies', () => {
  const { src, dest, dir } = makeWideTree();
  const j = runJson(src, dest);
  assert.equal(j.total, 8, '7 under-root captures + the external history.jsonl');
  assert.equal(j.archived, 8);
  // The excluded WebFetch PDF is not mirrored — nor is a .meta.json outside subagents/.
  assert.ok(!fs.existsSync(path.join(dest, '-repo-a', 'webfetch-abc.pdf.gz')));
  assert.ok(!fs.existsSync(path.join(dest, '-repo-a', 'stray.meta.json.gz')),
    'a .meta.json outside subagents/ is not captured (the class is scoped)');
  // Each captured class gunzips back to the exact source bytes.
  const checks = [
    [path.join(dest, '-repo-a', 'uuid1', 'subagents', 'agent-a1.meta.json.gz'),
      path.join(src, '-repo-a', 'uuid1', 'subagents', 'agent-a1.meta.json')],
    [path.join(dest, '-repo-a', 'uuid1', 'tool-results', 'big-output.txt.gz'),
      path.join(src, '-repo-a', 'uuid1', 'tool-results', 'big-output.txt')],
    [path.join(dest, '-repo-a', 'uuid1', 'toolu_01ABC.json.gz'),
      path.join(src, '-repo-a', 'uuid1', 'toolu_01ABC.json')],
    [path.join(dest, '-repo-a', 'memory', 'MEMORY.md.gz'),
      path.join(src, '-repo-a', 'memory', 'MEMORY.md')],
    [path.join(dest, '_external', 'history.jsonl.gz'), path.join(dir, 'history.jsonl')],
  ];
  for (const [gz, srcFile] of checks) {
    assert.ok(fs.existsSync(gz), `${gz} should exist`);
    assert.deepEqual(zlib.gunzipSync(fs.readFileSync(gz)), fs.readFileSync(srcFile));
  }
  // The external history is first-class in the manifest under its reserved rel…
  const mf = cc.loadManifest(dest);
  assert.ok(mf[path.join('_external', 'history.jsonl')], 'history.jsonl is a manifest entry');
  // …and the signature covers the new entries exactly like the old ones.
  const r = runCli('--verify', '--dest', dest, '--json');
  assert.equal(r.status, 0);
  assert.equal(JSON.parse(r.stdout).signature.state, 'verified');
});

test('contract: --verify catches a tampered external history .gz (first-class in the manifest)', () => {
  const { src, dest } = makeWideTree();
  runJson(src, dest);
  const rel = path.join('_external', 'history.jsonl');
  fs.writeFileSync(path.join(dest, rel + '.gz'), zlib.gzipSync(Buffer.from('{"tampered":1}\n')));
  const r = runCli('--verify', '--dest', dest, '--json');
  assert.equal(r.status, 1);
  assert.deepEqual(JSON.parse(r.stdout).mismatch, [rel]);
});

test('contract: --audit on a wide store matching its archive is clean, every class synced', () => {
  const { src, dest } = makeWideTree();
  runJson(src, dest);
  const r = runCli('--audit', '--source', src, '--dest', dest, '--json');
  assert.equal(r.status, 0);
  const out = JSON.parse(r.stdout);
  assert.equal(out.synced, 8, 'all seven under-root captures plus history are in sync');
  assert.equal(out.mutated.length, 0);
  assert.equal(out.renamed.length, 0);
});

test('contract: --audit flags a mutated tool-result sidecar and delta --restore repairs it', () => {
  const { src, dest } = makeWideTree();
  runJson(src, dest);
  const rel = path.join('-repo-a', 'uuid1', 'tool-results', 'big-output.txt');
  const f = path.join(src, rel);
  const archived = zlib.gunzipSync(fs.readFileSync(path.join(dest, rel + '.gz')));
  fs.writeFileSync(f, 'TAMPERED PAYLOAD\n');                 // rewritten, not a growth
  const past = gzMtimeMs(dest, rel) / 1000 - 10;             // older than the archive → repairable
  fs.utimesSync(f, past, past);

  const a = runCli('--audit', '--source', src, '--dest', dest, '--json');
  assert.equal(a.status, 1);
  const out = JSON.parse(a.stdout);
  assert.equal(out.mutated.length, 1);
  assert.equal(out.mutated[0].rel, rel);

  const rr = runRestore(src, dest, '--delta');
  assert.equal(rr.status, 0);
  assert.equal(rr.report.restored.length, 1);
  assert.deepEqual(fs.readFileSync(f), archived, 'the sidecar is back to the archived bytes');
});

test('contract: full --restore rebuilds sidecars, memory and the external history to their real homes', () => {
  const { src, dest, dir } = makeWideTree();
  runJson(src, dest);
  const rels = [
    path.join('-repo-a', 'uuid1.jsonl'),
    path.join('-repo-a', 'uuid1', 'subagents', 'agent-a1.jsonl'),
    path.join('-repo-a', 'uuid1', 'subagents', 'agent-a1.meta.json'),
    path.join('-repo-a', 'uuid1', 'tool-results', 'big-output.txt'),
    path.join('-repo-a', 'uuid1', 'toolu_01ABC.json'),
    path.join('-repo-a', 'memory', 'MEMORY.md'),
    path.join('-repo-a', 'memory', 'entry.md'),
  ];
  const originals = {};
  for (const rel of rels) originals[rel] = fs.readFileSync(path.join(src, rel));
  const historyBytes = fs.readFileSync(path.join(dir, 'history.jsonl'));

  fs.rmSync(src, { recursive: true });                       // whole live store lost
  fs.rmSync(path.join(dir, 'history.jsonl'));                 // and the external file too

  const r = runRestore(src, dest);
  assert.equal(r.status, 0);
  assert.equal(r.report.restored.length, 8);
  for (const [rel, bytes] of Object.entries(originals)) {
    assert.deepEqual(fs.readFileSync(path.join(src, rel)), bytes, `${rel} restored byte-identical`);
  }
  // The external history restores ABOVE the source root, never under projects/_external/.
  assert.ok(!fs.existsSync(path.join(src, '_external', 'history.jsonl')),
    'an external capture is not written back under the projects root');
  assert.deepEqual(fs.readFileSync(path.join(dir, 'history.jsonl')), historyBytes);
  // The rebuilt store re-audits clean.
  assert.equal(runCli('--audit', '--source', src, '--dest', dest, '--json').status, 0);
});

test('contract: the shrink guard covers new classes — a shrunk memory file is refused, --force overrides', () => {
  const { src, dest } = makeWideTree();
  runJson(src, dest);
  const rel = path.join('-repo-a', 'memory', 'MEMORY.md');
  const f = path.join(src, rel);
  fs.writeFileSync(f, '#\n');                                 // smaller than the recorded size
  const future = (Date.now() + 5000) / 1000;
  fs.utimesSync(f, future, future);                          // newer mtime → would otherwise overwrite
  const res = spawnSync('node', [SCRIPT, '--json', '--source', src, '--dest', dest], { encoding: 'utf8' });
  assert.equal(res.status, 1, 'a shrink is refused for a memory file just as for a transcript');
  assert.ok(JSON.parse(res.stdout).refusedShrink.includes(rel));
  const forced = runJson(src, dest, '--force');              // the deliberate override
  assert.ok(forced.archived >= 1);
});

test('contract: a subagent .meta.json is manifested, tamper-detected and restored beside its log', () => {
  const { src, dest } = makeWideTree();
  const rel = path.join('-repo-a', 'uuid1', 'subagents', 'agent-a1.meta.json');
  runJson(src, dest);

  // Manifest/integrity inclusion is structural — the manifest keys on <rel> for
  // every class alike — so the sidecar carries its own sha256 and raw size.
  const mf = cc.loadManifest(dest);
  assert.ok(mf[rel], 'the sidecar is a first-class manifest entry');
  assert.equal(mf[rel].sha256, cc.sha256(fs.readFileSync(path.join(src, rel))));
  assert.equal(mf[rel].rawBytes, fs.statSync(path.join(src, rel)).size);
  assert.equal(runCli('--verify', '--dest', dest, '--json').status, 0);

  // A mutated archive copy is caught, exactly like a transcript's.
  fs.writeFileSync(path.join(dest, rel + '.gz'), zlib.gzipSync(Buffer.from('{"tampered":1}\n')));
  const v = runCli('--verify', '--dest', dest, '--json');
  assert.equal(v.status, 1);
  assert.deepEqual(JSON.parse(v.stdout).mismatch, [rel]);

  // Restore mapping: an ordinary (non-external) rel, so it comes back beside its
  // log under subagents/ — never flattened, never under a reserved prefix.
  const { src: src2, dest: dest2 } = makeWideTree();
  runJson(src2, dest2);
  const original = fs.readFileSync(path.join(src2, rel));
  fs.rmSync(path.join(src2, rel));
  const r = runRestore(src2, dest2, '--delta');
  assert.equal(r.status, 0);
  assert.ok(r.report.restored.some((x) => x.rel === rel), 'the pruned sidecar is a delta-restore target');
  assert.deepEqual(fs.readFileSync(path.join(src2, rel)), original, 'restored byte-identical, in place');
});

// The shrink guard on a ~160-byte JSON document that can legitimately be
// rewritten. Two halves, because only one of them is a real cost: a FIRST
// capture is never refused however small the file, and only a rewrite that
// shrinks is. Safe-over-silent, and --force is the documented way through.
test('contract: the shrink guard ignores a tiny first capture and refuses a shrunk .meta.json rewrite', () => {
  const { src, dest } = makeWideTree();
  const rel = path.join('-repo-a', 'uuid1', 'subagents', 'agent-a1.meta.json');
  const f = path.join(src, rel);

  // Half one: the initial capture of a small file is not a shrink — nothing to
  // compare against, so no refusal (the guard needs an existing mirror).
  const first = runJson(src, dest);
  assert.deepEqual(first.refusedShrink, []);

  // Half two: Claude Code rewrites the sidecar with a field dropped — smaller,
  // newer, and a legitimate rewrite rather than truncation. Refused, loudly.
  fs.writeFileSync(f, JSON.stringify({ agentType: 'general-purpose', toolUseId: 'toolu_synthetic' }) + '\n');
  assert.ok(fs.statSync(f).size < first.files.find((x) => x.rel === rel).rawBytes);
  const future = (Date.now() + 5000) / 1000;
  fs.utimesSync(f, future, future);
  const res = spawnSync('node', [SCRIPT, '--json', '--source', src, '--dest', dest], { encoding: 'utf8' });
  assert.equal(res.status, 1, 'a shrunk JSON sidecar is refused like any other class');
  assert.ok(JSON.parse(res.stdout).refusedShrink.includes(rel));
  // The archived copy is untouched by the refusal — the old bytes still verify.
  assert.equal(runCli('--verify', '--dest', dest, '--json').status, 0);
  // --force is the deliberate way through, and the archive verifies after it.
  const forced = runJson(src, dest, '--force');
  assert.ok(forced.files.some((x) => x.rel === rel && x.action === 'archived'));
  assert.equal(runCli('--verify', '--dest', dest, '--json').status, 0);
});

// Roadmap claim under test (the "backfill is free" item): archiveOnce walks the
// WHOLE live tree every run and shouldArchive returns true whenever no mirror
// exists, so a newly-allowlisted class needs no backfill pass, no flag and no
// new code — the next ordinary run takes every such file still on disk, however
// old it is. Emulated by a sidecar that appears in the live tree with a long-past
// mtime after the archive was already written: indistinguishable, to the tool,
// from one that predated the capture class.
test('backfill: an ordinary run takes a never-archived sidecar however old its mtime, with no flag', () => {
  const { src, dest } = makeWideTree();
  const rel = path.join('-repo-a', 'uuid1', 'subagents', 'agent-a1.meta.json');
  const bytes = fs.readFileSync(path.join(src, rel));
  fs.rmSync(path.join(src, rel));

  const first = runJson(src, dest);                  // an archive with no sidecar in it
  assert.ok(!fs.existsSync(path.join(dest, rel + '.gz')));
  assert.ok(!cc.loadManifest(dest)[rel]);

  // The sidecar is (back) on disk, last written a year ago — stale by any mtime
  // reading, yet unarchived: destMtimeMs === null is what decides.
  fs.writeFileSync(path.join(src, rel), bytes);
  const yearAgo = (Date.now() - 365 * 24 * 3600 * 1000) / 1000;
  fs.utimesSync(path.join(src, rel), yearAgo, yearAgo);

  const second = runJson(src, dest);                 // no --force, no new flag
  assert.equal(second.archived, 1, 'exactly the unarchived sidecar');
  assert.equal(second.skipped, first.archived, 'everything already archived is left alone');
  assert.ok(second.files.some((x) => x.rel === rel && x.action === 'archived'));
  assert.deepEqual(zlib.gunzipSync(fs.readFileSync(path.join(dest, rel + '.gz'))), bytes);
  assert.ok(cc.loadManifest(dest)[rel], 'and it lands in the manifest on the same run');
  assert.equal(runCli('--verify', '--dest', dest, '--json').status, 0);
});

test('compat: an old (jsonl-only) archive still verifies; new-class live files audit as new, not drift', () => {
  const { src, dest } = makeTree();          // the original fixture: no sidecars/memory/history
  runJson(src, dest);                        // an archive written before the widened capture
  assert.equal(runCli('--verify', '--dest', dest, '--json').status, 0);

  // The upgraded tool now sees new-class files appear beside the transcripts.
  fs.mkdirSync(path.join(src, '-repo-a', 'uuid1', 'tool-results'), { recursive: true });
  fs.writeFileSync(path.join(src, '-repo-a', 'uuid1', 'tool-results', 'out.txt'), 'payload\n');
  fs.mkdirSync(path.join(src, '-repo-a', 'memory'), { recursive: true });
  fs.writeFileSync(path.join(src, '-repo-a', 'memory', 'MEMORY.md'), '# mem\n');

  // They are additive: `new`, never drift against an old archive — verify stays clean.
  const a = runCli('--audit', '--source', src, '--dest', dest, '--json');
  assert.equal(a.status, 0, 'new-class files are additive, not drift');
  assert.equal(JSON.parse(a.stdout).added, 2);
  assert.equal(runCli('--verify', '--dest', dest, '--json').status, 0);

  // The next ordinary run captures them, and the archive still verifies.
  const j = runJson(src, dest);
  assert.equal(j.archived, 2, 'the two new-class files are archived; the three transcripts are unchanged');
  assert.equal(runCli('--verify', '--dest', dest, '--json').status, 0);
});

// --- manifest durability + healing (210/170) ------------------------------
// A run that dies part-way must not leave mirrors ahead of the manifest, and a
// manifest that already lags must heal on the next ordinary run.

function runEnv(env, ...args) {
  return spawnSync('node', [SCRIPT, ...args], { encoding: 'utf8', env: { ...process.env, ...env } });
}

// Every mirror under dest has a manifest entry whose hash is the gunzipped bytes.
function assertManifestCoversMirrors(dest) {
  const manifest = cc.loadManifest(dest);
  const rels = cc.listArchivedRels(dest);
  for (const rel of rels) {
    assert.ok(manifest[rel], `manifest must cover ${rel}`);
    const raw = zlib.gunzipSync(fs.readFileSync(path.join(dest, rel + '.gz')));
    assert.equal(manifest[rel].sha256, cc.sha256(raw));
    assert.equal(manifest[rel].rawBytes, raw.length);
  }
  return rels;
}

test('a run that dies after K mirrors leaves the manifest covering them, and still signed', () => {
  const { src, dest } = makeTree();
  const r = runEnv({ CCARCHIVE_TEST_FAIL_AFTER: '2' }, '--json', '--source', src, '--dest', dest);
  assert.notEqual(r.status, 0, 'the simulated death must surface as a failure');
  assert.match(r.stderr, /simulated death/);
  const rels = assertManifestCoversMirrors(dest);
  assert.equal(rels.length, 2, 'exactly the mirrors written before the death');
  assert.equal(runCli('--verify', '--dest', dest).status, 0, 'manifest and signature agree');
  // The next ordinary run completes the rest and the archive is whole.
  runJson(src, dest);
  assert.equal(assertManifestCoversMirrors(dest).length, 3);
  assert.equal(runCli('--verify', '--dest', dest).status, 0);
});

test('checkpointing every mirror also leaves a covered, signed manifest after a death', () => {
  const { src, dest } = makeTree();
  const r = runEnv({ CCARCHIVE_CHECKPOINT_EVERY: '1', CCARCHIVE_TEST_FAIL_AFTER: '3' },
    '--json', '--source', src, '--dest', dest);
  assert.notEqual(r.status, 0);
  assert.equal(assertManifestCoversMirrors(dest).length, 3);
  assert.equal(runCli('--verify', '--dest', dest).status, 0);
});

// Make the manifest lag the mirror, as a killed run leaves it: rawBytes and
// sha256 describe a shorter prefix, re-signed so only the lag is under test.
function makeStale(src, dest, rel) {
  const manifest = cc.loadManifest(dest);
  const prefix = fs.readFileSync(path.join(src, rel)).subarray(0, 4);
  manifest[rel] = { sha256: cc.sha256(prefix), rawBytes: prefix.length, archivedAt: 'old' };
  cc.saveManifest(dest, manifest);
  cc.signManifest(dest, cc.ensureKey(process.env.CCARCHIVE_KEYFILE));
}

test('an ordinary run does NOT rewrite a lagging entry from the source (MC1)', () => {
  // The heal was pulled: a source replaced by an older, shorter copy must never
  // be recorded as the truth against an intact mirror.
  const { src, dest } = makeTree();
  runJson(src, dest);
  const rel = path.join('-repo-b', 'uuid2.jsonl');
  makeStale(src, dest, rel);
  const before = cc.loadManifest(dest)[rel];
  runJson(src, dest);
  assert.deepEqual(cc.loadManifest(dest)[rel], before);
  assert.equal(runCli('--verify', '--dest', dest).status, 1, 'the lag stays visible to --verify');
});

test('an ordinary run leaves an equal-size skipped entry untouched', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const rel = path.join('-repo-b', 'uuid2.jsonl');
  const manifest = cc.loadManifest(dest);
  manifest[rel].archivedAt = 'marker';
  cc.saveManifest(dest, manifest);
  runJson(src, dest);
  assert.equal(cc.loadManifest(dest)[rel].archivedAt, 'marker');
});

// --- hardening, part A (210/190, 210/200; HL4/5/7/8/9/10, MC2/5/6/9) -------
// Atomic mirror writes, one-bad-file-never-aborts, a clean top-level failure,
// restore-checks-before-writing, read-only modes that move nothing.

const asRoot = typeof process.getuid === 'function' && process.getuid() === 0;
const REL_B = path.join('-repo-b', 'uuid2.jsonl');
const REL_A = path.join('-repo-a', 'uuid1.jsonl');

function listDir(dir) { return fs.readdirSync(dir).sort(); }

// Rewrite a source with new bytes and a clearly newer mtime, so the next run
// re-archives it.
function touchNewer(file, text) {
  fs.writeFileSync(file, text);
  const t = new Date(Date.now() + 60_000);
  fs.utimesSync(file, t, t);
}

test('writeFileAtomic writes via a temp, stamps the mtime, replaces the target and leaves no temp', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ccarchive-aw-'));
  const target = path.join(dir, 'x.gz');
  fs.writeFileSync(target, 'old');
  cc.writeFileAtomic(target, Buffer.from('new bytes'), { atimeSec: 1_700_000_000, mtimeSec: 1_700_000_123 });
  assert.equal(fs.readFileSync(target, 'utf8'), 'new bytes');
  assert.equal(Math.round(fs.statSync(target).mtimeMs / 1000), 1_700_000_123);
  assert.deepEqual(listDir(dir), ['x.gz'], 'no temp left behind');
});

test('writeFileAtomic cleans its temp up when the write fails, and the target survives', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ccarchive-aw-'));
  const target = path.join(dir, 'taken');
  fs.mkdirSync(target);                       // a directory cannot be renamed over by a file
  assert.throws(() => cc.writeFileAtomic(target, Buffer.from('x')), (e) => !(e instanceof TypeError));
  assert.deepEqual(listDir(dir), ['taken'], 'the failed write left no temp');
});

test('contract: a mirror is replaced, never opened in place (a hard link to the old inode keeps the old bytes)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const mirror = path.join(dest, REL_B + '.gz');
  const keep = path.join(dest, 'kept-old-inode');
  fs.linkSync(mirror, keep);
  const oldBytes = fs.readFileSync(keep);
  touchNewer(path.join(src, REL_B), '{"other":"session","grown":true}\n');
  assert.equal(runJson(src, dest).archived, 1);
  assert.deepEqual(fs.readFileSync(keep), oldBytes, 'an in-place write would have changed both names');
  assert.equal(zlib.gunzipSync(fs.readFileSync(mirror)).toString(), '{"other":"session","grown":true}\n');
  assert.notEqual(fs.statSync(mirror).ino, fs.statSync(keep).ino);
  assert.equal(runCli('--verify', '--dest', dest).status, 0);
});

test('contract: a symlink planted at a mirror path is replaced, never written through (HL9)', () => {
  const { dir, src, dest } = makeTree();
  runJson(src, dest);
  const victim = path.join(dir, 'victim.txt');
  fs.writeFileSync(victim, 'do not touch');
  const mirror = path.join(dest, REL_B + '.gz');
  fs.rmSync(mirror);
  fs.symlinkSync(victim, mirror);
  const j = runJson(src, dest);
  assert.equal(j.archived, 1, 'the link is not a mirror, so the session is archived again');
  assert.equal(fs.readFileSync(victim, 'utf8'), 'do not touch', 'nothing was written through the link');
  assert.ok(!fs.lstatSync(mirror).isSymbolicLink(), 'the link itself was replaced by a regular file');
  assert.equal(runCli('--verify', '--dest', dest).status, 0);
});

test('contract: a symlinked directory inside the archive is refused and named, not written through', () => {
  const { dir, src, dest } = makeTree();
  runJson(src, dest);
  const outside = path.join(dir, 'outside');
  fs.mkdirSync(outside);
  fs.rmSync(path.join(dest, '-repo-b'), { recursive: true });
  fs.symlinkSync(outside, path.join(dest, '-repo-b'));
  const r = runCli('--json', '--source', src, '--dest', dest);
  assert.equal(r.status, 1, 'a refused write fails the run at the end');
  const j = JSON.parse(r.stdout);
  assert.deepEqual(j.unwritable.map((u) => u.rel), [REL_B]);
  assert.deepEqual(fs.readdirSync(outside), [], 'nothing landed outside the archive');
  assert.equal(j.archived, 0);
});

test('contract: a pre-planted manifest temp symlink is not followed (MC9)', () => {
  const { dir, src, dest } = makeTree();
  fs.mkdirSync(dest);
  const victim = path.join(dir, 'victim.txt');
  fs.writeFileSync(victim, 'do not touch');
  fs.symlinkSync(victim, path.join(dest, 'manifest.json.tmp'));
  assert.equal(runCli('--json', '--source', src, '--dest', dest).status, 0);
  assert.equal(fs.readFileSync(victim, 'utf8'), 'do not touch');
  assert.equal(runCli('--verify', '--dest', dest).status, 0);
});

test('contract: a dead run\'s leftover temp is ignored by verify and audit, then removed by the next run', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const dead = path.join(dest, '-repo-b', '.uuid2.jsonl.gz.99999999.deadbeef.tmp');
  const alive = path.join(dest, '-repo-b', `.uuid2.jsonl.gz.${process.pid}.cafef00d.tmp`);
  fs.writeFileSync(dead, 'half a gzip');
  fs.writeFileSync(alive, 'another run is writing this');
  const v = runCli('--verify', '--json', '--dest', dest);
  assert.equal(v.status, 0, 'a temp is not an unmanifested mirror');
  assert.deepEqual(JSON.parse(v.stdout).unmanifested, []);
  assert.equal(runCli('--audit', '--source', src, '--dest', dest).status, 0);
  assert.ok(fs.existsSync(dead), 'read-only modes remove nothing');
  const j = runJson(src, dest);
  assert.equal(j.staleTempsRemoved, 1);
  assert.ok(!fs.existsSync(dead), 'the dead run\'s temp is swept');
  assert.ok(fs.existsSync(alive), 'a temp whose process is still running is never touched');
});

test('--dry-run sweeps nothing', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const dead = path.join(dest, '-repo-b', '.uuid2.jsonl.gz.99999999.deadbeef.tmp');
  fs.writeFileSync(dead, 'x');
  runJson(src, dest, '--dry-run');
  assert.ok(fs.existsSync(dead));
});

// --- 210/200: an evicted (dataless) mirror never aborts a run ---------------
// Field log: every failure was `Unknown system error -11 ... open '<mirror>.gz'`
// from fs.writeFileSync — the in-place rewrite of a mirror whose bytes iCloud had
// evicted. A fixture cannot be genuinely evicted, so a mirror made unopenable
// (mode 000) under the dataless-simulation seam stands in: any open of it fails.

test('contract: re-archiving a session whose mirror is evicted does not open the mirror (210/200)', { skip: asRoot }, () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const mirror = path.join(dest, REL_B + '.gz');
  touchNewer(path.join(src, REL_B), '{"other":"session","grown":true}\n');
  fs.chmodSync(mirror, 0o000);
  const r = spawnSync('node', [SCRIPT, '--json', '--source', src, '--dest', dest],
    { encoding: 'utf8', env: { ...process.env, CCARCHIVE_SIMULATE_DATALESS: 'uuid2' } });
  assert.equal(r.status, 0, `the run must finish: ${r.stderr}`);
  assert.equal(JSON.parse(r.stdout).archived, 1);
  assert.equal(zlib.gunzipSync(fs.readFileSync(mirror)).toString(), '{"other":"session","grown":true}\n');
  assert.equal(runCli('--verify', '--dest', dest).status, 0);
});

test('contract: the run\'s tail backfill reports an evicted unmanifested mirror as not checked, and carries on', { skip: asRoot }, () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.rmSync(path.join(src, REL_B));            // pruned source: only the mirror is left
  const manifest = cc.loadManifest(dest);
  delete manifest[REL_B];
  cc.saveManifest(dest, manifest);
  fs.chmodSync(path.join(dest, REL_B + '.gz'), 0o000);
  const r = spawnSync('node', [SCRIPT, '--json', '--source', src, '--dest', dest],
    { encoding: 'utf8', env: { ...process.env, CCARCHIVE_SIMULATE_DATALESS: 'uuid2' } });
  assert.equal(r.status, 0, 'an evicted mirror is not a failure');
  assert.deepEqual(JSON.parse(r.stdout).offloaded, [REL_B]);
  const human = spawnSync('node', [SCRIPT, '--source', src, '--dest', dest],
    { encoding: 'utf8', env: { ...process.env, CCARCHIVE_SIMULATE_DATALESS: 'uuid2' } });
  assert.match(human.stdout, /1 mirror not checked \(offloaded/);
});

test('isOffloadError recognises the EDEADLK shape Node reports on Darwin; readMirror classifies every failure', { skip: asRoot }, () => {
  assert.equal(cc.isOffloadError({ code: 'EDEADLK' }), true);
  assert.equal(cc.isOffloadError({ errno: -11, code: 'Unknown system error -11' }), process.platform === 'darwin');
  assert.equal(cc.isOffloadError({ code: 'ENOENT', errno: -2 }), false);
  assert.equal(cc.isOffloadError(null), false);

  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ccarchive-rm-'));
  const good = path.join(dir, 'good.gz');
  fs.writeFileSync(good, zlib.gzipSync(Buffer.from('hello')));
  assert.deepEqual(cc.readMirror(good), { ok: true, buf: Buffer.from('hello') });
  assert.equal(cc.readMirror(path.join(dir, 'absent.gz')).kind, 'missing');
  fs.writeFileSync(path.join(dir, 'plain.gz'), 'not gzip at all');
  assert.equal(cc.readMirror(path.join(dir, 'plain.gz')).kind, 'corrupt');
  fs.writeFileSync(path.join(dir, 'cut.gz'), zlib.gzipSync(Buffer.from('hello world, a longer body')).subarray(0, 12));
  assert.equal(cc.readMirror(path.join(dir, 'cut.gz')).kind, 'corrupt');
  fs.writeFileSync(path.join(dir, 'locked.gz'), 'x');
  fs.chmodSync(path.join(dir, 'locked.gz'), 0o000);
  assert.equal(cc.readMirror(path.join(dir, 'locked.gz')).kind, 'unreadable');
});

test('contract: an unreadable manifest is a clean fatal error, never "corrupt → set aside and start fresh"', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const mp = path.join(dest, 'manifest.json');
  fs.rmSync(mp);
  fs.mkdirSync(mp);                            // exists but cannot be read as a file (EISDIR)
  const r = runCli('--source', src, '--dest', dest);
  assert.equal(r.status, 2);
  assert.match(r.stderr, /manifest\.json .* could not be read/);
  assert.ok(fs.statSync(mp).isDirectory(), 'the manifest path was not moved aside');
  assert.deepEqual(listDir(dest).filter((n) => n.includes('corrupt')), []);
});

// --- HL8: one bad source never aborts the run -------------------------------

test('contract: an unreadable source file is skipped, named (plain + json), and the run exits 1 at the end', { skip: asRoot }, () => {
  const { src, dest } = makeTree();
  const bad = path.join(src, REL_A);
  fs.chmodSync(bad, 0o000);
  try {
    const r = runCli('--json', '--source', src, '--dest', dest);
    assert.equal(r.status, 1);
    const j = JSON.parse(r.stdout);
    assert.deepEqual(j.unreadable.map((u) => [u.rel, u.stage]), [[REL_A, 'read']]);
    assert.equal(j.archived, 2, 'the files around it are still archived');
    assert.equal(runCli('--verify', '--dest', dest).status, 0, 'and the manifest was saved and signed');
    const h = runCli('--source', src, '--dest', dest);
    assert.equal(h.status, 1);
    assert.match(h.stdout, /✗ UNREADABLE -repo-a\/uuid1\.jsonl/);
  } finally { fs.chmodSync(bad, 0o644); }
});

test('contract: an unreadable source directory is skipped and named, and everything else is archived', { skip: asRoot }, () => {
  const { src, dest } = makeTree();
  fs.mkdirSync(path.join(src, '-repo-c'));
  fs.writeFileSync(path.join(src, '-repo-c', 'locked.jsonl'), '{"x":1}\n');
  fs.chmodSync(path.join(src, '-repo-c'), 0o000);
  try {
    const r = runCli('--json', '--source', src, '--dest', dest);
    assert.equal(r.status, 1);
    const j = JSON.parse(r.stdout);
    assert.deepEqual(j.unreadable.map((u) => [u.rel, u.stage]), [['-repo-c', 'walk']]);
    assert.equal(j.archived, 3);
  } finally { fs.chmodSync(path.join(src, '-repo-c'), 0o755); }
});

test('contract: a source that cannot be statted (gone between walk and read, or no search permission) is skipped, not fatal', { skip: asRoot }, () => {
  const { src, dest } = makeTree();
  fs.mkdirSync(path.join(src, '-repo-d'));
  fs.writeFileSync(path.join(src, '-repo-d', 'a.jsonl'), '{"x":1}\n');
  fs.chmodSync(path.join(src, '-repo-d'), 0o444);   // listable, but its entries cannot be statted
  try {
    const r = runCli('--json', '--source', src, '--dest', dest);
    assert.equal(r.status, 1);
    const j = JSON.parse(r.stdout);
    assert.deepEqual(j.unreadable.map((u) => [u.rel, u.stage]), [[path.join('-repo-d', 'a.jsonl'), 'stat']]);
    assert.equal(j.archived, 3);
  } finally { fs.chmodSync(path.join(src, '-repo-d'), 0o755); }
});

test('contract: --audit skips and names an unreadable live file instead of crashing (exit 1)', { skip: asRoot }, () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const bad = path.join(src, REL_A);
  fs.chmodSync(bad, 0o000);
  try {
    const r = runCli('--audit', '--json', '--source', src, '--dest', dest);
    assert.equal(r.status, 1);
    assert.deepEqual(JSON.parse(r.stdout).unreadable.map((u) => u.rel), [REL_A]);
  } finally { fs.chmodSync(bad, 0o644); }
});

// --- HL5: an undecompressable mirror is named, never a stack trace ----------

function corruptMirror(dest, rel, how) {
  const p = path.join(dest, rel + '.gz');
  const good = fs.readFileSync(p);
  if (how === 'truncated') fs.writeFileSync(p, good.subarray(0, Math.floor(good.length / 2)));
  else if (how === 'plain') fs.writeFileSync(p, 'this is not gzip');
  else { const bad = Buffer.from(good); bad[bad.length - 6] ^= 0xff; fs.writeFileSync(p, bad); }   // flipped CRC byte
}

for (const how of ['truncated', 'plain', 'flipped']) {
  test(`contract: --verify names a ${how} mirror as CORRUPT, checks the rest, exits 1 (no stack trace)`, () => {
    const { src, dest } = makeTree();
    runJson(src, dest);
    corruptMirror(dest, REL_B, how);
    const r = runCli('--verify', '--json', '--dest', dest);
    assert.equal(r.status, 1);
    const j = JSON.parse(r.stdout);
    assert.deepEqual(j.corrupt.map((c) => c.rel), [REL_B]);
    assert.equal(j.ok, 2, 'the other mirrors were still checked');
    const h = runCli('--verify', '--dest', dest);
    assert.match(h.stdout, /✗ CORRUPT -repo-b\/uuid2\.jsonl/);
    assert.doesNotMatch(h.stderr, /\n\s+at /);
  });
}

test('contract: --restore names an undecompressable mirror, restores the rest, exits 1', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  corruptMirror(dest, REL_B, 'plain');
  fs.rmSync(path.join(src, REL_A));
  fs.rmSync(path.join(src, REL_B));
  const r = runRestore(src, dest);
  assert.equal(r.status, 1);
  assert.deepEqual(r.report.errors.map((e) => [e.rel, e.reason]), [[REL_B, 'corrupt-archive']]);
  assert.ok(fs.existsSync(path.join(src, REL_A)), 'the intact mirror was still restored');
  const h = spawnSync('node', [SCRIPT, '--restore', '--source', src, '--dest', dest], { encoding: 'utf8' });
  assert.match(h.stdout, /✗ ERROR -repo-b\/uuid2\.jsonl .*will not decompress/);
});

test('contract: delta --restore and --audit survive an undecompressable mirror', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  corruptMirror(dest, REL_B, 'truncated');
  touchNewer(path.join(src, REL_B), '{"changed":true}\n');
  const a = runCli('--audit', '--json', '--source', src, '--dest', dest);
  assert.equal(a.status, 1);
  assert.deepEqual(JSON.parse(a.stdout).mutated.map((m) => [m.rel, m.reason]), [[REL_B, 'archive-corrupt']]);
  const r = runRestore(src, dest, '--delta', '--dry-run');
  assert.equal(r.status, 1);
  assert.deepEqual(r.report.errors.map((e) => e.reason), ['corrupt-archive']);
});

test('contract: the run\'s tail backfill names an undecompressable mirror, still saves the manifest, exits 1', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.rmSync(path.join(src, REL_B));            // pruned: only the mirror remains
  const manifest = cc.loadManifest(dest);
  delete manifest[REL_B];
  cc.saveManifest(dest, manifest);
  corruptMirror(dest, REL_B, 'plain');
  touchNewer(path.join(src, REL_A), '{"turn":1}\n{"turn":2}\n{"turn":3}\n');   // a real mirror written this run
  const r = runCli('--json', '--source', src, '--dest', dest);
  assert.equal(r.status, 1);
  const j = JSON.parse(r.stdout);
  assert.deepEqual(j.corrupt.map((c) => c.rel), [REL_B]);
  assert.equal(j.archived, 1);
  assert.ok(cc.loadManifest(dest)[REL_A].rawBytes > 20, 'the mirror written this run reached the manifest');
  assert.ok(!cc.loadManifest(dest)[REL_B], 'the bad mirror stays unmanifested, so --verify keeps flagging it');
  assert.equal(runCli('--verify', '--dest', dest).status, 1);
});

// --- MC5: one top-level catch -----------------------------------------------

test('contract: a fatal error is one clean stderr line and exit 2; under --json a structured error object', () => {
  const { dir, src } = makeTree();
  const notADir = path.join(dir, 'a-file');
  fs.writeFileSync(notADir, 'x');
  const r = runCli('--source', src, '--dest', notADir);
  assert.equal(r.status, 2);
  assert.equal(r.stderr.trim().split('\n').length, 1, 'one line, no stack');
  assert.match(r.stderr, /^ccarchive: /);
  assert.equal(r.stdout, '');
  const j = runCli('--json', '--source', src, '--dest', notADir);
  assert.equal(j.status, 2);
  const out = JSON.parse(j.stdout);
  assert.equal(typeof out.error, 'string');
  assert.ok('code' in out);
});

test('contract: the simulated mid-run death exits 2 with one clean line, not a stack trace', () => {
  const { src, dest } = makeTree();
  const r = runEnv({ CCARCHIVE_TEST_FAIL_AFTER: '1' }, '--source', src, '--dest', dest);
  assert.equal(r.status, 2);
  assert.doesNotMatch(r.stderr, /\n\s+at /);
});

// --- HL7: restore checks the bytes before it writes -------------------------

test('contract: restore refuses an archived copy that fails its recorded sha256 and writes nothing (HL7)', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const live = path.join(src, REL_B);
  const good = fs.readFileSync(live);
  // Rot: the mirror is valid gzip but no longer the captured bytes.
  fs.writeFileSync(path.join(dest, REL_B + '.gz'), zlib.gzipSync(Buffer.from('bad')));
  const old = new Date(Date.now() - 3_600_000);
  fs.writeFileSync(live, '{"edited":"live"}\n');       // diverged, and older than the mirror: a restore target
  fs.utimesSync(live, old, old);
  for (const flags of [[], ['--force'], ['--dry-run']]) {
    const r = runRestore(src, dest, ...flags);
    assert.equal(r.status, 1, `flags ${flags}`);
    assert.deepEqual(r.report.refused.map((x) => [x.rel, x.reason]), [[REL_B, 'hash-mismatch']]);
    assert.equal(r.report.restored.filter((x) => x.rel === REL_B).length, 0);
    assert.equal(fs.readFileSync(live, 'utf8'), '{"edited":"live"}\n', 'the live file was not overwritten');
  }
  assert.notDeepEqual(good, fs.readFileSync(live));
  const h = spawnSync('node', [SCRIPT, '--restore', '--source', src, '--dest', dest], { encoding: 'utf8' });
  assert.match(h.stdout, /✗ REFUSED -repo-b\/uuid2\.jsonl — the archived copy no longer matches/);
});

test('contract: restore of an entry with no recorded sha256 is refused as unverified unless --force', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const manifest = cc.loadManifest(dest);
  delete manifest[REL_B].sha256;
  cc.saveManifest(dest, manifest);
  const original = fs.readFileSync(path.join(src, REL_B));
  fs.rmSync(path.join(src, REL_B));
  const r = runRestore(src, dest);
  assert.equal(r.status, 1);
  assert.deepEqual(r.report.refused.map((x) => [x.rel, x.reason]), [[REL_B, 'unverified']]);
  assert.ok(!fs.existsSync(path.join(src, REL_B)));
  const f = runRestore(src, dest, '--force');
  assert.equal(f.status, 0);
  assert.equal(f.report.restored.find((x) => x.rel === REL_B).unverified, true);
  assert.deepEqual(fs.readFileSync(path.join(src, REL_B)), original);
});

test('contract: restore writes by rename and leaves no temp file in the live store', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  fs.rmSync(path.join(src, REL_B));
  assert.equal(runRestore(src, dest).status, 0);
  assert.deepEqual(listDir(path.join(src, '-repo-b')), ['uuid2.jsonl']);
});

// --- HL10: read-only modes move nothing; a set-aside is never overwritten ---

test('contract: --verify, --audit, --restore (and --dry-run) never move an unparseable manifest', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const mp = path.join(dest, 'manifest.json');
  fs.writeFileSync(mp, '{ this is not json');
  const before = fs.readFileSync(mp);
  const files = listDir(dest);
  for (const args of [['--verify'], ['--audit'], ['--restore'], ['--restore', '--dry-run'], ['--restore', '--delta']]) {
    const r = runCli(...args, '--json', '--source', src, '--dest', dest);
    assert.equal(r.status, 2, args.join(' '));
    assert.equal(JSON.parse(r.stdout).code, 'EMANIFEST');
    assert.deepEqual(fs.readFileSync(mp), before, `${args.join(' ')} left the manifest byte-identical`);
    assert.deepEqual(listDir(dest), files, `${args.join(' ')} created and moved nothing`);
  }
  const d = runCli('--dry-run', '--json', '--source', src, '--dest', dest);
  assert.equal(d.status, 0);
  assert.match(d.stderr, /a real run would set it aside/);
  assert.deepEqual(fs.readFileSync(mp), before);
  assert.deepEqual(listDir(dest), files);
});

test('contract: a write-mode run sets an unparseable manifest aside under a timestamped name, never overwriting an earlier one', () => {
  const { src, dest } = makeTree();
  runJson(src, dest);
  const mp = path.join(dest, 'manifest.json');
  fs.writeFileSync(mp, 'first corruption');
  runJson(src, dest);
  fs.writeFileSync(mp, 'second corruption');
  runJson(src, dest);
  const kept = listDir(dest).filter((n) => n.startsWith('manifest.json.corrupt-'));
  assert.equal(kept.length, 2, 'both casualties are kept');
  assert.deepEqual(kept.map((n) => fs.readFileSync(path.join(dest, n), 'utf8')).sort(),
    ['first corruption', 'second corruption']);
  assert.ok(!listDir(dest).includes('manifest.json.corrupt'), 'the old fixed name is gone');
});

// --- MC6: the repo-dest guard resolves symlinks ------------------------------

test('contract: a dest that is a symlink into a git work tree is refused (MC6)', () => {
  const { dir, src } = makeTree();
  const tree = path.join(dir, 'worktree');
  fs.mkdirSync(path.join(tree, '.git'), { recursive: true });
  fs.mkdirSync(path.join(tree, 'out'));
  const link = path.join(dir, 'innocent-looking');
  fs.symlinkSync(path.join(tree, 'out'), link);
  assert.equal(cc.insideGitWorkTree(link), true);
  assert.equal(cc.insideGitWorkTree(path.join(link, 'not-yet-created')), true, 'a not-yet-existing dest resolves via its nearest real ancestor');
  const r = runCli('--source', src, '--dest', link);
  assert.equal(r.status, 1);
  assert.match(r.stderr, /refusing to archive into a git work tree/);
  assert.deepEqual(fs.readdirSync(path.join(tree, 'out')), []);
  assert.equal(runCli('--source', src, '--dest', link, '--allow-repo-dest').status, 0);
});
