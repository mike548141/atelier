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
  assert.equal(cc.insideGitWorkTree(deep), fs.realpathSync(root) === root ? root : cc.insideGitWorkTree(deep));
  assert.ok(cc.insideGitWorkTree(deep).endsWith(path.basename(root)));
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

// --- formatting --------------------------------------------------------------

test('human keeps whole bytes exact and scales the rest', () => {
  assert.equal(cc.human(0), '0 B');
  assert.equal(cc.human(512), '512 B');
  assert.equal(cc.human(2048), '2.0 KB');
  assert.equal(cc.human(2 * 1024 * 1024), '2.0 MB');
});
