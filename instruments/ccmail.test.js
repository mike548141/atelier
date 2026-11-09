/*
 * ccmail tests — node:test/node:assert, no npm.
 *
 * What is tested here is everything that does not need Google: the MIME part
 * walk, the selector grammar, filename safety, the git-work-tree guard, and the
 * Office extractors. The network surface (token refresh, the two Gmail calls)
 * is deliberately not mocked — a mock of an API this thin proves only that the
 * mock was written to match the code, and the real proof is a live run, which
 * the man page's own EXAMPLES are.
 *
 * The Office extractors get real containers: the helper below writes a genuine
 * ZIP (stored, uncompressed) so `unzip` reads the fixture exactly as it reads a
 * file that came off a mail server. A fixture that only satisfied our own
 * parser would prove nothing about the format.
 */
'use strict';

const test = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { spawnSync } = require('node:child_process');

const cc = require('./ccmail');

const HAVE_UNZIP = spawnSync('unzip', ['-v']).status === 0;

// --- a minimal stored-ZIP writer, so the Office fixtures are real ------------

function crc32(buf) {
  let c;
  const table = crc32.table || (crc32.table = (() => {
    const t = new Int32Array(256);
    for (let n = 0; n < 256; n++) {
      c = n;
      for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1;
      t[n] = c;
    }
    return t;
  })());
  let crc = -1;
  for (let i = 0; i < buf.length; i++) crc = (crc >>> 8) ^ table[(crc ^ buf[i]) & 0xFF];
  return (crc ^ -1) >>> 0;
}

function makeZip(file, entries) {
  const locals = [];
  const central = [];
  let offset = 0;
  for (const [name, content] of Object.entries(entries)) {
    const nameBuf = Buffer.from(name, 'utf8');
    const data = Buffer.from(content, 'utf8');
    const crc = crc32(data);

    const lh = Buffer.alloc(30);
    lh.writeUInt32LE(0x04034b50, 0);
    lh.writeUInt16LE(20, 4);          // version needed
    lh.writeUInt16LE(0, 6);           // flags
    lh.writeUInt16LE(0, 8);           // method: stored
    lh.writeUInt32LE(crc, 14);
    lh.writeUInt32LE(data.length, 18);
    lh.writeUInt32LE(data.length, 22);
    lh.writeUInt16LE(nameBuf.length, 26);
    locals.push(lh, nameBuf, data);

    const ch = Buffer.alloc(46);
    ch.writeUInt32LE(0x02014b50, 0);
    ch.writeUInt16LE(20, 4);
    ch.writeUInt16LE(20, 6);
    ch.writeUInt16LE(0, 8);
    ch.writeUInt16LE(0, 10);
    ch.writeUInt32LE(crc, 16);
    ch.writeUInt32LE(data.length, 20);
    ch.writeUInt32LE(data.length, 24);
    ch.writeUInt16LE(nameBuf.length, 28);
    ch.writeUInt32LE(offset, 42);
    central.push(ch, nameBuf);

    offset += lh.length + nameBuf.length + data.length;
  }
  const cd = Buffer.concat(central);
  const eocd = Buffer.alloc(22);
  eocd.writeUInt32LE(0x06054b50, 0);
  eocd.writeUInt16LE(Object.keys(entries).length, 8);
  eocd.writeUInt16LE(Object.keys(entries).length, 10);
  eocd.writeUInt32LE(cd.length, 12);
  eocd.writeUInt32LE(offset, 16);
  fs.writeFileSync(file, Buffer.concat([...locals, cd, eocd]));
  return file;
}

function tmpdir() {
  return fs.mkdtempSync(path.join(os.tmpdir(), 'ccmail-test-'));
}

// --- the MIME part walk ------------------------------------------------------

const MESSAGE = {
  payload: {
    mimeType: 'multipart/mixed',
    headers: [
      { name: 'Subject', value: 'Machinery valuations' },
      { name: 'From', value: 'a sender' },
    ],
    parts: [
      { partId: '0', mimeType: 'text/plain', filename: '', body: { size: 400, data: 'aGk=' } },
      { partId: '1', mimeType: 'text/html', filename: '', body: { size: 900, data: 'aGk=' } },
      { partId: '2', mimeType: 'application/pdf', filename: 'Dozer Valuation.pdf', body: { size: 120000, attachmentId: 'A1' } },
      { partId: '3', mimeType: 'image/jpeg', filename: '', body: { size: 4000, attachmentId: 'A2' } },
    ],
  },
};

test('attachmentsOf keeps files and drops the message body', () => {
  const got = cc.attachmentsOf(MESSAGE);
  assert.equal(got.length, 2);
  assert.equal(got[0].filename, 'Dozer Valuation.pdf');
  assert.equal(got[0].attachmentId, 'A1');
});

test('attachmentsOf keeps an unnamed inline image rather than dropping it', () => {
  const got = cc.attachmentsOf(MESSAGE);
  const unnamed = got.find((a) => a.filename === null);
  assert.ok(unnamed, 'the unnamed image/jpeg part should survive');
  assert.equal(unnamed.attachmentId, 'A2');
});

test('attachmentsOf descends into nested multiparts', () => {
  const nested = {
    payload: {
      mimeType: 'multipart/mixed',
      parts: [{
        mimeType: 'multipart/alternative',
        parts: [
          { mimeType: 'text/plain', filename: '', body: { size: 1 } },
          { mimeType: 'application/pdf', filename: 'deep.pdf', body: { size: 2, attachmentId: 'D' } },
        ],
      }],
    },
  };
  const got = cc.attachmentsOf(nested);
  assert.deepEqual(got.map((a) => a.filename), ['deep.pdf']);
});

test('header reads case-insensitively and misses cleanly', () => {
  assert.equal(cc.header(MESSAGE, 'subject'), 'Machinery valuations');
  assert.equal(cc.header(MESSAGE, 'Reply-To'), '');
});

// --- the selector grammar ----------------------------------------------------

const ITEMS = [
  { filename: 'Dozer Valuation.pdf' },
  { filename: 'Hino Valuation.pdf' },
  { filename: 'notes.txt' },
  { filename: null },
];

test('select defaults to everything', () => {
  assert.equal(cc.select(ITEMS, 'all').length, 4);
  assert.equal(cc.select(ITEMS, null).length, 4);
});

test('select takes a 1-based index', () => {
  assert.deepEqual(cc.select(ITEMS, '2').map((a) => a.filename), ['Hino Valuation.pdf']);
});

test('select matches a substring case-blind', () => {
  assert.deepEqual(cc.select(ITEMS, 'hino').map((a) => a.filename), ['Hino Valuation.pdf']);
  assert.equal(cc.select(ITEMS, 'valuation').length, 2);
});

test('select globs on the filename', () => {
  assert.deepEqual(cc.select(ITEMS, '*.txt').map((a) => a.filename), ['notes.txt']);
});

test('select mixes forms and never repeats a hit', () => {
  const got = cc.select(ITEMS, '1,dozer,notes');
  assert.deepEqual(got.map((a) => a.filename), ['Dozer Valuation.pdf', 'notes.txt']);
});

test('select returns nothing rather than guessing on a miss', () => {
  assert.equal(cc.select(ITEMS, 'invoice').length, 0);
});

// --- filename safety ---------------------------------------------------------

test('safeName strips path separators so an attachment cannot escape its dir', () => {
  // Separators become underscores, and the leading dots go too — so the result
  // is neither a traversal nor a hidden file the operator would not see in ls.
  const got = cc.safeName('../../etc/passwd', 0, 'text/plain');
  assert.equal(got, '_.._etc_passwd');
  assert.ok(!got.includes('/'));
  assert.ok(!got.startsWith('.'));
  assert.ok(!cc.safeName('a/b/c.pdf', 0, 'application/pdf').includes('/'));
  assert.ok(!cc.safeName('..\\..\\win.ini', 0, 'text/plain').includes('\\'));
});

test('safeName invents a name when the sender left none', () => {
  assert.equal(cc.safeName(null, 2, 'application/pdf'), 'attachment-3.pdf');
  assert.equal(cc.safeName('', 0, 'image/jpeg'), 'attachment-1.jpg');
  assert.equal(cc.safeName('', 0, 'application/x-weird'), 'attachment-1.bin');
});

test('safeName truncates a very long name but keeps its extension', () => {
  const long = 'x'.repeat(400) + '.pdf';
  const got = cc.safeName(long, 0, 'application/pdf');
  assert.ok(got.length <= 180);
  assert.ok(got.endsWith('.pdf'));
});

// --- the repo guard ----------------------------------------------------------

test('insideGitWorkTree finds the enclosing repo, and nothing outside one', () => {
  const root = tmpdir();
  const deep = path.join(root, 'a', 'b');
  fs.mkdirSync(deep, { recursive: true });
  assert.equal(cc.insideGitWorkTree(deep), null);
  fs.mkdirSync(path.join(root, '.git'));
  // Compared with the resolved root: on macOS the temp dir is itself reached
  // through a symlink, and the guard answers in resolved terms.
  assert.equal(cc.insideGitWorkTree(deep), fs.realpathSync(root));
});

test('insideGitWorkTree resolves symlinks, so a --dest reached through one is caught', () => {
  // Review CC5b: the guard compared the string it was given, so a link outside
  // the repo that points into it walked straight past.
  const base = tmpdir();
  const repo = path.join(base, 'repo');
  fs.mkdirSync(path.join(repo, '.git'), { recursive: true });
  fs.mkdirSync(path.join(repo, 'inner'));
  const link = path.join(base, 'innocent-looking');
  fs.symlinkSync(path.join(repo, 'inner'), link);
  assert.equal(cc.insideGitWorkTree(link), fs.realpathSync(repo));
  // A not-yet-created child of the link resolves through it too.
  assert.equal(cc.insideGitWorkTree(path.join(link, 'new', 'deeper')), fs.realpathSync(repo));
});

// --- XML text recovery -------------------------------------------------------

test('xmlText turns block tags into line breaks before stripping the rest', () => {
  const xml = '<w:p><w:r><w:t>one</w:t></w:r></w:p><w:p><w:r><w:t>two</w:t></w:r></w:p>';
  assert.equal(cc.xmlText(xml, ['w:p']), 'one\ntwo');
});

test('xmlText decodes entities, and ampersand last so it cannot double-decode', () => {
  assert.equal(cc.xmlText('<t>a &amp;lt; b</t>', []), 'a &lt; b');
  assert.equal(cc.xmlText('<t>Tom &amp; Jerry &quot;x&quot;</t>', []), 'Tom & Jerry "x"');
});

// --- Office extraction, against real ZIP containers --------------------------

test('extractOffice reads a .docx body', { skip: !HAVE_UNZIP && 'unzip not on PATH' }, () => {
  const f = makeZip(path.join(tmpdir(), 'letter.docx'), {
    '[Content_Types].xml': '<Types/>',
    'word/document.xml':
      '<w:document><w:body>' +
      '<w:p><w:r><w:t>Dear Ryan</w:t></w:r></w:p>' +
      '<w:p><w:r><w:t>The valuation is $68,400.</w:t></w:r></w:p>' +
      '</w:body></w:document>',
  });
  const r = cc.extractOffice(f, 'docx');
  assert.ok(r.ok, r.why);
  assert.match(r.text, /Dear Ryan/);
  assert.match(r.text, /\$68,400\./);
  assert.equal(r.text.split('\n').filter(Boolean).length, 2);
});

test('extractOffice reads .xlsx cells through the shared string table', { skip: !HAVE_UNZIP && 'unzip not on PATH' }, () => {
  const f = makeZip(path.join(tmpdir(), 'book.xlsx'), {
    'xl/workbook.xml': '<workbook><sheets><sheet name="Valuations" sheetId="1"/></sheets></workbook>',
    'xl/sharedStrings.xml':
      '<sst><si><t>Item</t></si><si><t>Value</t></si><si><t>Dual Dozer</t></si></sst>',
    'xl/worksheets/sheet1.xml':
      '<worksheet><sheetData>' +
      '<row r="1"><c r="A1" t="s"><v>0</v></c><c r="B1" t="s"><v>1</v></c></row>' +
      '<row r="2"><c r="A2" t="s"><v>2</v></c><c r="B2"><v>28500</v></c></row>' +
      '</sheetData></worksheet>',
  });
  const r = cc.extractOffice(f, 'xlsx');
  assert.ok(r.ok, r.why);
  assert.match(r.text, /--- sheet: Valuations ---/);
  assert.match(r.text, /Item\tValue/);
  assert.match(r.text, /Dual Dozer\t28500/);
});

test('extractOffice reads .pptx slides in numeric, not lexical, order', { skip: !HAVE_UNZIP && 'unzip not on PATH' }, () => {
  const slide = (s) => `<p:sld><p:cSld><a:p><a:r><a:t>${s}</a:t></a:r></a:p></p:cSld></p:sld>`;
  const entries = { 'ppt/slides/slide1.xml': slide('first'), 'ppt/slides/slide2.xml': slide('second') };
  for (let i = 3; i <= 11; i++) entries[`ppt/slides/slide${i}.xml`] = slide(`n${i}`);
  const f = makeZip(path.join(tmpdir(), 'deck.pptx'), entries);
  const r = cc.extractOffice(f, 'pptx');
  assert.ok(r.ok, r.why);
  assert.ok(r.text.indexOf('first') < r.text.indexOf('second'));
  // slide10 must not sort between slide1 and slide2.
  assert.ok(r.text.indexOf('second') < r.text.indexOf('n10'));
});

test('extractOffice says why rather than returning empty text', { skip: !HAVE_UNZIP && 'unzip not on PATH' }, () => {
  const f = makeZip(path.join(tmpdir(), 'empty.docx'), { 'other.xml': '<x/>' });
  const r = cc.extractOffice(f, 'docx');
  assert.equal(r.ok, false);
  assert.match(r.why, /no readable document body/);
});

test('officeKind reads the MIME type first and the extension second', () => {
  assert.equal(cc.officeKind('x.bin',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'), 'xlsx');
  assert.equal(cc.officeKind('report.DOCX', 'application/octet-stream'), 'docx');
  assert.equal(cc.officeKind('scan.pdf', 'application/pdf'), null);
});

// --- query building ----------------------------------------------------------

test('buildUrl repeats a list parameter instead of comma-joining it', () => {
  // Gmail wants metadataHeaders=Subject&metadataHeaders=From. A comma-joined
  // single value asks for one header literally named "Subject,From" and comes
  // back with no headers at all rather than an error — a silent empty subject.
  const u = cc.buildUrl('/messages/abc', {
    format: 'metadata',
    metadataHeaders: ['Subject', 'From', 'Date'],
  });
  assert.deepEqual(u.searchParams.getAll('metadataHeaders'), ['Subject', 'From', 'Date']);
  assert.equal(u.searchParams.get('format'), 'metadata');
  assert.ok(!u.search.includes('Subject%2CFrom'));
});

test('buildUrl drops absent parameters rather than sending empty ones', () => {
  const u = cc.buildUrl('/messages', { q: 'has:attachment', maxResults: undefined, pageToken: null });
  assert.equal(u.searchParams.get('q'), 'has:attachment');
  assert.equal(u.searchParams.has('maxResults'), false);
  assert.equal(u.searchParams.has('pageToken'), false);
});

test('buildUrl escapes a query rather than splicing it into the URL', () => {
  const u = cc.buildUrl('/messages', { q: 'from:a b OR subject:"x&y"' });
  assert.equal(u.searchParams.get('q'), 'from:a b OR subject:"x&y"');
});

// --- formatting --------------------------------------------------------------

test('human keeps whole bytes exact and scales the rest', () => {
  assert.equal(cc.human(0), '0 B');
  assert.equal(cc.human(512), '512 B');
  assert.equal(cc.human(2048), '2.0 KB');
  assert.equal(cc.human(2 * 1024 * 1024), '2.0 MB');
});

// --- config and route selection ----------------------------------------------

test('loadConfig tolerates a missing file and a malformed one', () => {
  const dir = tmpdir();
  const missing = path.join(dir, 'nope.json');
  process.env.CCMAIL_CONFIG = missing;
  assert.deepEqual(cc.loadConfig(), {});

  const bad = path.join(dir, 'bad.json');
  fs.writeFileSync(bad, '{not json');
  process.env.CCMAIL_CONFIG = bad;
  // Malformed config must not be fatal: it would otherwise take away a working
  // fallback route over a typo in an optional file.
  assert.deepEqual(cc.loadConfig(), {});

  const good = path.join(dir, 'good.json');
  fs.writeFileSync(good, JSON.stringify({ delegate: { serviceAccount: 'a', subject: 'b' } }));
  process.env.CCMAIL_CONFIG = good;
  assert.equal(cc.loadConfig().delegate.subject, 'b');
  delete process.env.CCMAIL_CONFIG;
});

test('delegationConfigured needs both the service account and the subject', () => {
  assert.equal(cc.delegationConfigured({}), false);
  assert.equal(cc.delegationConfigured({ delegate: { serviceAccount: 'test-service-account' } }), false);
  assert.equal(cc.delegationConfigured({ delegate: { subject: 'test-mailbox' } }), false);
  assert.equal(cc.delegationConfigured({ delegate: { serviceAccount: 'test-service-account', subject: 'test-mailbox' } }), true);
});

test('an empty keychain never sends a delegation operator to --auth', () => {
  const d = cc.keychainAbsentDetail(true, true);
  assert.doesNotMatch(d, /--auth/);
  assert.match(d, /not needed/);
});

test('an empty keychain still offers --auth where there is no delegation', () => {
  assert.match(cc.keychainAbsentDetail(false, true), /fix: ccmail --auth/);
  assert.equal(cc.keychainAbsentDetail(false, false), 'unavailable off macOS');
  assert.equal(cc.keychainAbsentDetail(true, false), 'unavailable off macOS');
});

test('--auth with delegation configured asks for nothing and points at gcloud', () => {
  // A delegation config with no gcloud on PATH: the route fails, and --auth
  // must stop with the gcloud advice instead of prompting for a client ID.
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ccmail-auth-'));
  const cfg = path.join(dir, 'ccmail.json');
  fs.writeFileSync(cfg, JSON.stringify({ delegate: { serviceAccount: 'test-service-account', subject: 'test-mailbox' } }));
  const r = spawnSync(process.execPath, [path.join(__dirname, 'ccmail'), '--auth'], {
    encoding: 'utf8',
    input: '',
    env: { ...process.env, HOME: dir, CCMAIL_CONFIG: cfg, CCMAIL_GCLOUD: path.join(dir, 'no-gcloud'), PATH: '/nonexistent' },
  });
  assert.notEqual(r.status, 0);
  assert.match(r.stderr, /gcloud auth login/);
  assert.doesNotMatch(r.stdout + r.stderr, /Client ID/);
});

// ===========================================================================
// Review CC2/CC5/CC6/CC7/CC8/CC11 — the cache, the write path, the parser
// ===========================================================================

const DAY = 24 * 60 * 60 * 1000;
const TOOL = path.join(__dirname, 'ccmail');

// Set a path's atime/mtime without following a link, `days` days before now.
function age(p, days) {
  const t = new Date(Date.now() - days * DAY);
  fs.lutimesSync(p, t, t);
}

// A message folder in a cache root, with one file, at the given modes and age.
function seedFolder(root, id, { days = 0, dirMode = 0o755, fileMode = 0o644, name = 'a.pdf' } = {}) {
  const dir = path.join(root, id);
  fs.mkdirSync(dir, { recursive: true });
  const f = path.join(dir, name);
  fs.writeFileSync(f, 'mail');
  fs.chmodSync(f, fileMode);
  fs.chmodSync(dir, dirMode);
  age(f, days);
  age(dir, days);
  return { dir, file: f };
}

const mode = (p) => fs.lstatSync(p).mode & 0o777;

function cacheRoot() {
  const root = path.join(fs.realpathSync(tmpdir()), 'ccmail');
  fs.mkdirSync(root, { mode: 0o755 });
  fs.chmodSync(root, 0o755);
  return root;
}

// --- CC2: private cache ------------------------------------------------------

test('cacheHygiene makes a world-readable cache private, root and contents', () => {
  const root = cacheRoot();
  const a = seedFolder(root, 'aaaa1111');
  const rep = cc.cacheHygiene(root);
  assert.equal(mode(root), 0o700);
  assert.equal(mode(a.dir), 0o700);
  assert.equal(mode(a.file), 0o600);
  assert.equal(rep.tightened, 3);
  assert.match(cc.hygieneLine(rep), /made 3 path\(s\) private/);
  // A second run has nothing to do, and says nothing.
  assert.equal(cc.hygieneLine(cc.cacheHygiene(root)), '');
});

test('cacheHygiene deletes message folders older than 30 days and keeps the rest', () => {
  const root = cacheRoot();
  const old = seedFolder(root, 'dead0001', { days: 31 });
  const fresh = seedFolder(root, 'f00d0002', { days: 29 });
  // A folder whose directory is old but which holds a recently written file is
  // live: a re-fetch renews it.
  const renewed = seedFolder(root, 'cafe0003', { days: 40 });
  fs.writeFileSync(path.join(renewed.dir, 'new.pdf'), 'x');
  const rep = cc.cacheHygiene(root);
  assert.deepEqual(rep.removed, ['dead0001']);
  assert.ok(!fs.existsSync(old.dir));
  assert.ok(fs.existsSync(fresh.dir));
  assert.ok(fs.existsSync(renewed.dir));
  assert.match(cc.hygieneLine(rep), /removed 1 message folder\(s\) not touched for 30\+ days/);
});

test('cacheHygiene honours an injected clock and window', () => {
  const root = cacheRoot();
  const f = seedFolder(root, 'beef0004', { days: 2 });
  assert.deepEqual(cc.cacheHygiene(root, { days: 1 }).removed, ['beef0004']);
  assert.ok(!fs.existsSync(f.dir));
});

// --- the sweep deletes files: every limit on its reach is pinned -------------

test('the sweep never follows a symlink entry out of the cache', () => {
  const root = cacheRoot();
  const outside = tmpdir();
  fs.writeFileSync(path.join(outside, 'precious.txt'), 'keep');
  const link = path.join(root, 'dead0005');           // a hex name, old, a link
  fs.symlinkSync(outside, link);
  age(link, 90);
  const rep = cc.cacheHygiene(root);
  assert.ok(fs.existsSync(path.join(outside, 'precious.txt')), 'the target was deleted');
  assert.ok(fs.lstatSync(link).isSymbolicLink(), 'the link itself was removed');
  assert.deepEqual(rep.removed, []);
  assert.match(cc.hygieneLine(rep), /left alone: dead0005 \(a symlink\)/);
});

test('deleting an expired folder removes a symlink inside it, not what it points at', () => {
  const root = cacheRoot();
  const outside = tmpdir();
  fs.writeFileSync(path.join(outside, 'precious.txt'), 'keep');
  const old = seedFolder(root, 'dead0006', { days: 60 });
  const inner = path.join(old.dir, 'looks-like-an-attachment');
  fs.symlinkSync(outside, inner);
  age(inner, 60);
  age(old.dir, 60);              // adding the link touched the directory
  const rep = cc.cacheHygiene(root);
  assert.deepEqual(rep.removed, ['dead0006']);
  assert.ok(!fs.existsSync(old.dir));
  assert.equal(fs.readFileSync(path.join(outside, 'precious.txt'), 'utf8'), 'keep');
});

test('tightening never chmods through a symlink to something outside the cache', () => {
  const root = cacheRoot();
  const outside = tmpdir();
  const victim = path.join(outside, 'victim.txt');
  fs.writeFileSync(victim, 'x');
  fs.chmodSync(victim, 0o644);
  const a = seedFolder(root, 'aaaa0007');
  fs.symlinkSync(victim, path.join(a.dir, 'link'));
  cc.cacheHygiene(root);
  assert.equal(mode(victim), 0o644);
});

test('the sweep only touches message-id folders, never a stray name or a loose file', () => {
  const root = cacheRoot();
  const stray = seedFolder(root, 'Documents', { days: 400 });     // not hex: not ours
  const loose = path.join(root, 'dead0008');                      // hex but a file
  fs.writeFileSync(loose, 'x');
  age(loose, 400);
  const traversal = seedFolder(root, 'dead00-09', { days: 400 }); // hex-ish, not hex
  const rep = cc.cacheHygiene(root);
  assert.deepEqual(rep.removed, []);
  assert.ok(fs.existsSync(stray.dir) && fs.existsSync(loose) && fs.existsSync(traversal.dir));
  // ... and a stray folder keeps its modes: only ccmail's own are tightened.
  assert.equal(mode(stray.dir), 0o755);
});

test('the sweep refuses a cache root that is a symlink, and deletes nothing through it', () => {
  const real = cacheRoot();
  const old = seedFolder(real, 'dead000a', { days: 90 });
  const link = path.join(fs.realpathSync(tmpdir()), 'ccmail-link');
  fs.symlinkSync(real, link);
  const rep = cc.cacheHygiene(link);
  assert.match(rep.refused, /symlink/);
  assert.ok(fs.existsSync(old.dir));
  assert.match(cc.hygieneLine(rep), /not tidied/);
});

test('the sweep refuses the home directory and a git work tree as a cache root', () => {
  const home = fs.realpathSync(tmpdir());
  const saved = process.env.HOME;
  process.env.HOME = home;
  try {
    const old = seedFolder(home, 'dead000b', { days: 90 });
    assert.match(cc.cacheHygiene(home).refused, /home directory/);
    assert.ok(fs.existsSync(old.dir));
  } finally {
    process.env.HOME = saved;
  }
  const repo = fs.realpathSync(tmpdir());
  fs.mkdirSync(path.join(repo, '.git'));
  const inRepo = path.join(repo, 'cache');
  fs.mkdirSync(inRepo);
  const old2 = seedFolder(inRepo, 'dead000c', { days: 90 });
  assert.match(cc.cacheHygiene(inRepo).refused, /git work tree/);
  assert.ok(fs.existsSync(old2.dir));
});

test('a missing cache is not an error and creates nothing', () => {
  const missing = path.join(tmpdir(), 'never-made');
  const rep = cc.cacheHygiene(missing);
  assert.equal(rep.refused, null);
  assert.equal(cc.hygieneLine(rep), '');
  assert.ok(!fs.existsSync(missing));
});

test('every working run tidies the real default cache path, and reports it once', () => {
  // The whole tool, in a scratch HOME: an old folder goes, a loose one is
  // tightened, and the run then stops at the door (no route) with the cache
  // line already printed. PATH is empty so nothing reaches a real Keychain.
  const home = fs.realpathSync(tmpdir());
  const root = path.join(home, '.cache', 'ccmail');
  fs.mkdirSync(root, { recursive: true });
  const old = seedFolder(root, 'dead000d', { days: 45 });
  const live = seedFolder(root, 'f00d000e', { days: 1 });
  const env = { ...process.env, HOME: home, PATH: '/nonexistent', CCMAIL_CONFIG: path.join(home, 'none.json') };
  delete env.XDG_CACHE_HOME;
  delete env.CCMAIL_DEST;
  const r = spawnSync(process.execPath, [TOOL, 'f00d000e'], { encoding: 'utf8', env });
  assert.equal(r.status, 1);
  assert.match(r.stderr, /cache {2}made \d+ path\(s\) private; removed 1 message folder/);
  assert.match(r.stderr, /no way in to the mailbox/);
  assert.ok(!fs.existsSync(old.dir));
  assert.equal(mode(live.dir), 0o700);
  assert.equal(mode(live.file), 0o600);
});

// --- CC2/CC5/CC6: the write path ---------------------------------------------

function withUmask(m, fn) {
  const saved = process.umask(m);
  try { return fn(); } finally { process.umask(saved); }
}

const b64 = (s) => Buffer.from(s).toString('base64url');
const part = (filename, extra = {}) => ({
  filename, mimeType: 'application/pdf', size: 1, attachmentId: 'A', inlineData: null, ...extra,
});

async function put(dest, items, data, opts = {}) {
  const fetchData = async (a) => data.get(a);
  return cc.writeAttachments(dest, items, items, fetchData, opts);
}

test('new attachment files are 0600 and new directories 0700, whatever the umask', async () => {
  const dest = path.join(fs.realpathSync(tmpdir()), 'a', 'b', 'msg');
  const a = part('x.pdf');
  await withUmask(0o000, async () => {
    const { written } = await put(dest, [a], new Map([[a, b64('pdf')]]));
    assert.equal(mode(written[0].file), 0o600);
  });
  assert.equal(mode(dest), 0o700);
  assert.equal(mode(path.dirname(dest)), 0o700);
});

test('an existing --dest keeps its own mode', async () => {
  const dest = fs.realpathSync(tmpdir());
  fs.chmodSync(dest, 0o755);
  const a = part('x.pdf');
  await put(dest, [a], new Map([[a, b64('pdf')]]));
  assert.equal(mode(dest), 0o755);
});

test('the .txt sidecar is private too', { skip: !HAVE_UNZIP && 'unzip not on PATH' }, async () => {
  const dir = tmpdir();
  const docx = makeZip(path.join(dir, 'src.docx'), {
    'word/document.xml': '<w:document><w:p><w:t>hello</w:t></w:p></w:document>',
  });
  const a = part('letter.docx', { mimeType: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' });
  const dest = path.join(dir, 'out');
  const { written } = await put(dest, [a], new Map([[a, fs.readFileSync(docx).toString('base64url')]]), { text: true });
  assert.ok(written[0].text, 'no sidecar written');
  assert.equal(mode(written[0].text), 0o600);
});

test('two attachments with one name become two files, not one overwritten', async () => {
  const dest = path.join(tmpdir(), 'msg');
  const a = part('image.png');
  const b = part('image.png');
  const { written } = await put(dest, [a, b], new Map([[a, b64('first')], [b, b64('second')]]));
  assert.equal(written.length, 2);
  assert.notEqual(written[0].file, written[1].file);
  assert.equal(fs.readFileSync(written[0].file, 'utf8'), 'first');
  assert.equal(fs.readFileSync(written[1].file, 'utf8'), 'second');
});

test('names that sanitise to one another do not collide either', async () => {
  const dest = path.join(tmpdir(), 'msg');
  const a = part('a/b.pdf');
  const b = part('a\\b.pdf');
  const { written } = await put(dest, [a, b], new Map([[a, b64('1')], [b, b64('2')]]));
  assert.notEqual(written[0].file, written[1].file);
});

test('re-running a fetch reuses identical files and suffixes different ones', async () => {
  const dest = path.join(tmpdir(), 'msg');
  const a = part('x.pdf');
  const first = await put(dest, [a], new Map([[a, b64('same')]]));
  const again = await put(dest, [a], new Map([[a, b64('same')]]));
  assert.equal(again.written[0].file, first.written[0].file);
  assert.equal(fs.readdirSync(dest).length, 1);
  const changed = await put(dest, [a], new Map([[a, b64('different')]]));
  assert.notEqual(changed.written[0].file, first.written[0].file);
  assert.equal(fs.readFileSync(first.written[0].file, 'utf8'), 'same');
});

test('a symlink planted at the destination name is not written through', async () => {
  // Review CC5a: in a shared directory such as /tmp the classic attack is a
  // pre-placed link named like the attachment.
  const dest = path.join(tmpdir(), 'msg');
  fs.mkdirSync(dest);
  const victim = path.join(tmpdir(), 'victim.txt');
  fs.writeFileSync(victim, 'untouched');
  fs.symlinkSync(victim, path.join(dest, 'x.pdf'));
  fs.symlinkSync(path.join(dest, 'nowhere'), path.join(dest, 'y.pdf'));   // dangling
  const a = part('x.pdf');
  const b = part('y.pdf');
  const { written } = await put(dest, [a, b], new Map([[a, b64('payload')], [b, b64('payload2')]]));
  assert.equal(fs.readFileSync(victim, 'utf8'), 'untouched');
  assert.ok(!fs.existsSync(path.join(dest, 'nowhere')));
  assert.equal(written.length, 2);
  for (const w of written) assert.ok(!fs.lstatSync(w.file).isSymbolicLink());
});

test('one failing attachment is reported and the rest are still written', async () => {
  const dest = path.join(tmpdir(), 'msg');
  const a = part('one.pdf');
  const b = part('two.pdf');
  const c = part('three.pdf');
  const fetchData = async (x) => {
    if (x === b) throw new Error('Gmail API error: boom');
    return b64(x.filename);
  };
  const { written, failed } = await cc.writeAttachments(dest, [a, b, c], [a, b, c], fetchData);
  assert.deepEqual(written.map((w) => path.basename(w.file)), ['one.pdf', 'three.pdf']);
  assert.equal(failed.length, 1);
  assert.match(failed[0].why, /boom/);
});

test('a part with neither an id nor data is skipped, never fetched as "null"', async () => {
  // Review CC11 (probe H): cmdGet used to ask for /attachments/null and die.
  const dest = path.join(tmpdir(), 'msg');
  const a = part('ghost.pdf', { attachmentId: null, inlineData: null });
  let asked = 0;
  const { written, failed } = await cc.writeAttachments(dest, [a], [a], async (x) => {
    asked++;
    return x.inlineData || (x.attachmentId ? 'AAAA' : null);
  });
  assert.equal(asked, 1);
  assert.equal(written.length, 0);
  assert.equal(failed[0].why, 'no data');
});

test('an extension longer than the name limit no longer aborts the batch', async () => {
  // Review CC6 (probe C): ENAMETOOLONG on the extension, mid-batch.
  const dest = path.join(tmpdir(), 'msg');
  const a = part('report.' + 'x'.repeat(300));
  const b = part('😀'.repeat(150) + '.pdf');                      // 600 bytes of name
  const c = part('plain.pdf');
  const { written, failed } = await put(dest, [a, b, c], new Map([[a, b64('1')], [b, b64('2')], [c, b64('3')]]));
  assert.equal(failed.length, 0, JSON.stringify(failed));
  assert.equal(written.length, 3);
  for (const w of written) assert.ok(Buffer.byteLength(path.basename(w.file)) <= 255);
});

// --- CC6/CC11: names ---------------------------------------------------------

test('safeName removes bidirectional overrides and control characters', () => {
  const got = cc.safeName('invoice‮gpj.exe', 0, 'image/jpeg');
  assert.doesNotMatch(got, /[‪-‮⁦-⁩‎‏]/);
  assert.doesNotMatch(cc.safeName('a\u001b[2Jb.pdf', 0, 'application/pdf'), /[\x00-\x1f]/);
  assert.doesNotMatch(cc.printable('x‮y\u001b[31m'), /[‮\x1b]/);
});

test('safeName caps bytes as well as characters, and caps the extension', () => {
  const emoji = cc.safeName('😀'.repeat(150) + '.pdf', 0, 'application/pdf');
  assert.ok(Buffer.byteLength(emoji) <= 200, `${Buffer.byteLength(emoji)} bytes`);
  assert.ok(emoji.endsWith('.pdf'));
  const longExt = cc.safeName('a.' + 'x'.repeat(400), 0, 'application/pdf');
  assert.ok(Buffer.byteLength(longExt) <= 200);
});

// --- CC5c: the message id ----------------------------------------------------

test('a message id that is not hex is refused before any network call or path join', () => {
  const home = fs.realpathSync(tmpdir());
  const env = { ...process.env, HOME: home, PATH: '/nonexistent', CCMAIL_CONFIG: path.join(home, 'none.json') };
  for (const bad of ['../../escape', 'A1B2', 'abc/def', '..']) {
    for (const args of [[bad, '--get', 'all'], [bad]]) {
      const r = spawnSync(process.execPath, [TOOL, ...args], { encoding: 'utf8', env });
      assert.equal(r.status, 1, `${args.join(' ')}`);
      assert.match(r.stderr, /is not a Gmail message id/, args.join(' '));
      assert.doesNotMatch(r.stderr, /no way in/, 'it got as far as the resolver');
    }
  }
});

// --- CC7: the argument parser and the selector -------------------------------

test('--get never swallows the next flag as its selector', () => {
  const home = fs.realpathSync(tmpdir());
  const env = { ...process.env, HOME: home, PATH: '/nonexistent', CCMAIL_CONFIG: path.join(home, 'none.json') };
  for (const args of [['abc123', '--get'], ['abc123', '--get', '--text']]) {
    const r = spawnSync(process.execPath, [TOOL, ...args], { encoding: 'utf8', env });
    assert.equal(r.status, 1);
    assert.match(r.stderr, /--get needs a value/);
  }
});

test('selectDetailed names the tokens that matched nothing, so a partial miss is not silent', () => {
  const items = [{ filename: 'a.pdf' }, { filename: 'b.xlsx' }];
  assert.deepEqual(cc.selectDetailed(items, '1,99').missed, ['99']);
  assert.equal(cc.selectDetailed(items, '1,99').chosen.length, 1);
  assert.deepEqual(cc.selectDetailed(items, '*.pdf,nothing').missed, ['nothing']);
  assert.deepEqual(cc.selectDetailed(items, 'all').missed, []);
  // A token that hits something already chosen is a hit, not a miss.
  assert.deepEqual(cc.selectDetailed(items, '1,a').missed, []);
});

// --- CC8: the consent URL and callback ---------------------------------------

test('the consent URL carries state and an S256 PKCE challenge', () => {
  const { verifier, challenge } = cc.pkcePair();
  const u = cc.buildConsentUrl('client-id', 'http://127.0.0.1:1234', 'st4te', challenge);
  assert.equal(u.searchParams.get('state'), 'st4te');
  assert.equal(u.searchParams.get('code_challenge'), challenge);
  assert.equal(u.searchParams.get('code_challenge_method'), 'S256');
  assert.equal(u.searchParams.get('scope'), 'https://www.googleapis.com/auth/gmail.readonly');
  // The challenge is the verifier's SHA-256, base64url, unpadded — what Google checks.
  assert.equal(challenge, require('node:crypto').createHash('sha256').update(verifier).digest('base64url'));
  assert.ok(verifier.length >= 43 && verifier.length <= 128);
  assert.notEqual(cc.pkcePair().verifier, verifier);
});

test('a callback without our state is ignored, and one with it is accepted', () => {
  assert.equal(cc.consentCallback('/?code=evil', 'st4te').ignore, true);
  assert.equal(cc.consentCallback('/?code=evil&state=other', 'st4te').ignore, true);
  assert.equal(cc.consentCallback('/favicon.ico', 'st4te').ignore, true);
  const ok = cc.consentCallback('/?code=good&state=st4te', 'st4te');
  assert.equal(ok.ignore, false);
  assert.equal(ok.code, 'good');
  assert.equal(cc.consentCallback('/?error=access_denied&state=st4te', 'st4te').err, 'access_denied');
});

// --- CC11: smaller gaps ------------------------------------------------------

test('xmlText decodes hex character references and leaves a hostile one as written', () => {
  assert.equal(cc.xmlText('<a>caf&#xE9; &#233; &#x1F600;</a>', []), 'café é 😀');
  assert.equal(cc.xmlText('<a>&#x110000; &#xD800;</a>', []), '&#x110000; &#xD800;');
});

test('a Keychain read that fails is an error, only "no such item" is absence', () => {
  assert.deepEqual(cc.classifyKeychainRead({ status: 44, stdout: '', stderr: '' }), { creds: null, error: null });
  assert.match(cc.classifyKeychainRead({ status: 36, stdout: '', stderr: 'user interaction is not allowed' }).error, /exited 36/);
  assert.match(cc.classifyKeychainRead({ status: null, error: new Error('ENOENT') }).error, /could not run security/);
  assert.match(cc.classifyKeychainRead({ status: 0, stdout: '{nope', stderr: '' }).error, /not valid JSON/);
  assert.deepEqual(cc.classifyKeychainRead({ status: 0, stdout: '{"account":"x"}\n', stderr: '' }),
    { creds: { account: 'x' }, error: null });
});

test('the cache retention is 30 days', () => {
  assert.equal(cc.CACHE_DAYS, 30);
});
