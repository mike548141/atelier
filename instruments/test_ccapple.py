"""Unit tests for instruments/ccapple.

Run:  python3 -m unittest discover -s instruments -p 'test_*.py' -v

Every store here is a SYNTHETIC SQLite file built in a temp dir, mirroring only
the columns the tool queries. Names, numbers and messages are obviously fake
(Alex Example, Sam Sample, UK drama-range 020 7946 numbers, example.invalid). No
real Apple data is read, and none belongs in this file. The tool is never pointed
at the machine's real stores: the one test that runs the script as a process
sets HOME to an empty temp dir first.

What the tests are for: the read-only guarantee (a write is refused and the
file is byte-identical afterwards), the "search, never dump" gate (no filter
means a usage error), the Messages quirks that matter (nanosecond dates, body
only in the attributedBody blob, handle matching across number formats), and
Calendar's all-day and recurring handling. Notes: the gzip + protobuf body is
built here by a tiny encoder, so the decoder is tested against bytes this file
makes, never a real note; a locked note is never read; trashed notes stay out
unless asked; a multi-byte UTF-8 body survives. Photos: a fake .photoslibrary
tree holds both databases and a few empty files; the UUID is packed into psi's
two integers the way Photos does (little-endian), a trashed asset stays out, a
missing original falls back to the largest derivative, and a search with no
filter is refused. Home: a fake HomeKit store with invented entity numbers (the
join tables must be found by column name, not by the real macOS numbers),
credential-shaped columns holding SENTINEL values that must never reach any
output, the hidden automation-owned scene kept out of the scene list, and the
write-ahead-log warning. Last, the `--help` digest must be a subset of the man
page (REPO-STANDARD: the two registers share the options list, so a flag added
to one and not the other is caught here)."""

import contextlib
import importlib.machinery
import importlib.util
import io
import json
import os
import re
import sqlite3
import struct
import subprocess
import sys
import tempfile
import unittest
import uuid
import zlib
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "ccapple")
MANPAGE = os.path.join(HERE, "man", "ccapple.1")


def _load():
    """The instrument has no .py suffix (it installs as a bare command, like its
    siblings), so import it by path. No bytecode is written next to it."""
    sys.dont_write_bytecode = True
    loader = importlib.machinery.SourceFileLoader("ccapple", SCRIPT)
    spec = importlib.util.spec_from_loader("ccapple", loader)
    module = importlib.util.module_from_spec(spec)
    sys.modules["ccapple"] = module
    loader.exec_module(module)
    return module


cc = _load()

APPLE_EPOCH = datetime(2001, 1, 1, tzinfo=timezone.utc)


def apple(dt):
    return (dt - APPLE_EPOCH).total_seconds()


def local_midnight(y, m, d):
    return datetime(y, m, d).astimezone()


def typedstream(text, form="short"):
    """A minimal attributedBody-shaped blob around `text`."""
    raw = text.encode("utf-8")
    if len(raw) < 0x80:
        ln = bytes([len(raw)])
    elif form == "u16":
        ln = b"\x81" + len(raw).to_bytes(2, "little")
    else:
        ln = b"\x82" + len(raw).to_bytes(4, "little")
    if form == "u16" and len(raw) < 0x80:
        ln = b"\x81" + len(raw).to_bytes(2, "little")
    return (b"\x04\x0bstreamtyped\x81\xe8\x03\x84\x01@\x84\x84\x84\x12NSAttributedString\x00\x84\x84\x08NSObject\x00"
            b"\x85\x92\x84\x84\x84\x08NSString\x01\x94\x84\x01+" + ln + raw + b"\x86\x84\x02iI\x01\x05\x92\x84\x84\x84\x0cNSDictionary\x00")


def read_bytes(path):
    with open(path, "rb") as fh:
        return fh.read()


def build(path, statements):
    con = sqlite3.connect(path)
    for s in statements:
        if isinstance(s, tuple):
            con.execute(*s)
        else:
            con.execute(s)
    con.commit()
    con.close()


class TmpCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = self._tmp.name
        self.addCleanup(self._tmp.cleanup)

    def path(self, name):
        return os.path.join(self.dir, name)


# ------------------------------------------------------------ fixtures ----

def make_contacts(path):
    build(path, [
        "CREATE TABLE ZABCDRECORD (Z_PK INTEGER PRIMARY KEY, ZFIRSTNAME TEXT, ZMIDDLENAME TEXT, ZLASTNAME TEXT, "
        "ZNICKNAME TEXT, ZORGANIZATION TEXT, ZJOBTITLE TEXT)",
        "CREATE TABLE ZABCDPHONENUMBER (Z_PK INTEGER PRIMARY KEY, ZOWNER INTEGER, ZFULLNUMBER TEXT, ZLABEL TEXT)",
        "CREATE TABLE ZABCDEMAILADDRESS (Z_PK INTEGER PRIMARY KEY, ZOWNER INTEGER, ZADDRESS TEXT, ZLABEL TEXT)",
        "INSERT INTO ZABCDRECORD VALUES (1,'Alex',NULL,'Example',NULL,NULL,'Tester')",
        "INSERT INTO ZABCDRECORD VALUES (2,'Sam',NULL,'Sample',NULL,'Sample Co',NULL)",
        "INSERT INTO ZABCDRECORD VALUES (3,'Māori',NULL,'Fixture',NULL,NULL,NULL)",
        "INSERT INTO ZABCDRECORD VALUES (4,NULL,NULL,NULL,NULL,NULL,NULL)",  # the unnamed "me"/group row
        "INSERT INTO ZABCDPHONENUMBER VALUES (1,1,'+44 20 7946 0101','_$!<Mobile>!$_')",
        "INSERT INTO ZABCDPHONENUMBER VALUES (2,2,'020 7946 0202','_$!<Home>!$_')",
        "INSERT INTO ZABCDEMAILADDRESS VALUES (1,1,'alex@example.invalid','_$!<Work>!$_')",  # leakscan:allow:email: fictional address in the reserved .invalid TLD (RFC 2606), a test fixture
        "INSERT INTO ZABCDEMAILADDRESS VALUES (2,2,'Sam@Example.Invalid',NULL)",  # leakscan:allow:email: fictional address in the reserved .invalid TLD (RFC 2606), a test fixture
    ])


def make_messages(path):
    ns = lambda dt: int(apple(dt) * 1e9)
    d1 = datetime(2026, 3, 1, 9, 0, tzinfo=timezone.utc)
    build(path, [
        "CREATE TABLE handle (ROWID INTEGER PRIMARY KEY, id TEXT)",
        "CREATE TABLE chat (ROWID INTEGER PRIMARY KEY, display_name TEXT, chat_identifier TEXT)",
        "CREATE TABLE chat_handle_join (chat_id INTEGER, handle_id INTEGER)",
        "CREATE TABLE chat_message_join (chat_id INTEGER, message_id INTEGER, message_date INTEGER)",
        "CREATE TABLE message (ROWID INTEGER PRIMARY KEY, date INTEGER, text TEXT, attributedBody BLOB, "
        "is_from_me INTEGER, handle_id INTEGER, service TEXT, cache_has_attachments INTEGER)",
        "INSERT INTO handle VALUES (1,'+442079460101')",
        "INSERT INTO handle VALUES (2,'+442079460202')",
        "INSERT INTO handle VALUES (3,'+442079460303')",
        # chat 1: 1:1 with Alex; chat 2: 1:1 with Sam; chat 3: group of Alex + Sam + a stranger
        "INSERT INTO chat VALUES (1,NULL,'+442079460101')",
        "INSERT INTO chat VALUES (2,NULL,'+442079460202')",
        "INSERT INTO chat VALUES (3,'Fixture Group','chat0000')",
        "INSERT INTO chat_handle_join VALUES (1,1)",
        "INSERT INTO chat_handle_join VALUES (2,2)",
        "INSERT INTO chat_handle_join VALUES (3,1)",
        "INSERT INTO chat_handle_join VALUES (3,2)",
        "INSERT INTO chat_handle_join VALUES (3,3)",
        # nanosecond dates, body in the blob only
        ("INSERT INTO message VALUES (1,?,NULL,?,0,1,'iMessage',0)", (ns(d1), typedstream("meet at the museum at nine"))),
        ("INSERT INTO message VALUES (2,?,'plain text reply',NULL,1,1,'iMessage',0)", (ns(d1 + timedelta(minutes=5)),)),
        # an old-style SECONDS date, SMS
        ("INSERT INTO message VALUES (3,?,'old sms about the bike',NULL,0,2,'SMS',0)", (int(apple(datetime(2015, 6, 1, tzinfo=timezone.utc))),)),
        # group message from the stranger, and from Alex
        ("INSERT INTO message VALUES (4,?,NULL,?,0,3,'iMessage',0)", (ns(d1 + timedelta(days=1)), typedstream("group chatter"))),
        ("INSERT INTO message VALUES (5,?,NULL,?,0,1,'iMessage',0)", (ns(d1 + timedelta(days=2)), typedstream("alex in the group"))),
        # attachment only
        ("INSERT INTO message VALUES (6,?,NULL,NULL,0,2,'iMessage',1)", (ns(d1 + timedelta(days=3)),)),
        "INSERT INTO chat_message_join VALUES (1,1,0)",
        "INSERT INTO chat_message_join VALUES (1,2,0)",
        "INSERT INTO chat_message_join VALUES (2,3,0)",
        "INSERT INTO chat_message_join VALUES (3,4,0)",
        "INSERT INTO chat_message_join VALUES (3,5,0)",
        "INSERT INTO chat_message_join VALUES (2,6,0)",
    ])


def make_calendar(path):
    day = lambda y, m, d, h=0: apple(datetime(y, m, d, h, tzinfo=timezone.utc))
    build(path, [
        "CREATE TABLE Calendar (ROWID INTEGER PRIMARY KEY, title TEXT)",
        "CREATE TABLE Location (ROWID INTEGER PRIMARY KEY, title TEXT)",
        "CREATE TABLE CalendarItem (ROWID INTEGER PRIMARY KEY, summary TEXT, description TEXT, location_id INTEGER, "
        "start_date REAL, end_date REAL, all_day INTEGER, calendar_id INTEGER, has_recurrences INTEGER, entity_type INTEGER)",
        "CREATE TABLE OccurrenceCache (day REAL, event_id INTEGER, calendar_id INTEGER, store_id INTEGER, "
        "occurrence_date REAL, occurrence_start_date REAL, occurrence_end_date REAL)",
        "INSERT INTO Calendar VALUES (1,'Personal')",
        "INSERT INTO Calendar VALUES (2,'Work')",
        "INSERT INTO Location VALUES (1,'Test Venue')",
        # one-off timed event, 2026-05-10 10:00-11:00 UTC
        ("INSERT INTO CalendarItem VALUES (1,'Review meeting','bring the agenda',1,?,?,0,2,0,2)", (day(2026, 5, 10, 10), day(2026, 5, 10, 11))),
        # all-day event at UTC midnight
        ("INSERT INTO CalendarItem VALUES (2,'Fixture day off',NULL,NULL,?,?,1,1,0,2)", (day(2026, 5, 12), day(2026, 5, 12))),
        # weekly series: master in 2025, two cached occurrences in 2026
        ("INSERT INTO CalendarItem VALUES (3,'Weekly fixture sync',NULL,NULL,?,?,0,2,1,2)", (day(2025, 1, 6, 8), day(2025, 1, 6, 9))),
        ("INSERT INTO OccurrenceCache VALUES (0,3,2,0,?,?,?)", (day(2026, 5, 11, 8), day(2026, 5, 11, 8), day(2026, 5, 11, 9))),
        ("INSERT INTO OccurrenceCache VALUES (0,3,2,0,?,?,?)", (day(2026, 5, 18, 8), day(2026, 5, 18, 8), day(2026, 5, 18, 9))),
        # a task row (entity_type 3) that must never come back as an event
        ("INSERT INTO CalendarItem VALUES (4,'A task not an event',NULL,NULL,?,?,0,1,0,3)", (day(2026, 5, 10, 10), day(2026, 5, 10, 11))),
    ])


def _pb_varint(n):
    out = bytearray()
    while True:
        b = n & 0x7F
        n >>= 7
        out.append(b | (0x80 if n else 0))
        if not n:
            return bytes(out)


def pb_field(number, value):
    """One protobuf field: int -> varint, bytes -> length-delimited."""
    if isinstance(value, int):
        return _pb_varint(number << 3) + _pb_varint(value)
    return _pb_varint(number << 3 | 2) + _pb_varint(len(value)) + value


def note_blob(text, runs=2, gz=True):
    """ZDATA as Notes writes it: gzip( root{1:0, 2: doc{1:0, 2:0, 3: note{2: text, 3*: run}}} )."""
    note = pb_field(2, text.encode("utf-8")) + b"".join(pb_field(3, pb_field(1, len(text) // runs + 1)) for _ in range(runs))
    doc = pb_field(1, 0) + pb_field(2, 0) + pb_field(3, note)
    raw = pb_field(1, 0) + pb_field(2, doc)
    if not gz:
        return raw
    co = zlib.compressobj(wbits=31)
    return co.compress(raw) + co.flush()


def make_notes(path):
    """Entities as on a real store: looked up through Z_PRIMARYKEY, not hard-coded.
    Folders: 10 Work (type 0), 11 Sub (child of Work), 12 Recently Deleted (type 1),
    13 a smart folder. Notes: 1 plain, 2 Māori body, 3 locked, 4 trashed, 5 old, 6 no body."""
    d = lambda y, m, dd: apple(datetime(y, m, dd, 12).astimezone())  # local noon: day filters are local
    ins = "INSERT INTO ZICCLOUDSYNCINGOBJECT (Z_PK, Z_ENT, ZTITLE1, ZTITLE2, ZMODIFICATIONDATE1, ZFOLDER, ZNOTEDATA, " \
          "ZISPASSWORDPROTECTED, ZMARKEDFORDELETION, ZFOLDERTYPE, ZPARENT, ZSMARTFOLDERQUERYJSON) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
    build(path, [
        "CREATE TABLE Z_PRIMARYKEY (Z_ENT INTEGER PRIMARY KEY, Z_NAME VARCHAR, Z_SUPER INTEGER, Z_MAX INTEGER)",
        "CREATE TABLE ZICCLOUDSYNCINGOBJECT (Z_PK INTEGER PRIMARY KEY, Z_ENT INTEGER, ZTITLE1 VARCHAR, ZTITLE2 VARCHAR, "
        "ZMODIFICATIONDATE1 TIMESTAMP, ZFOLDER INTEGER, ZNOTEDATA INTEGER, ZISPASSWORDPROTECTED INTEGER, "
        "ZMARKEDFORDELETION INTEGER, ZFOLDERTYPE INTEGER, ZPARENT INTEGER, ZSMARTFOLDERQUERYJSON VARCHAR)",
        "CREATE TABLE ZICNOTEDATA (Z_PK INTEGER PRIMARY KEY, ZNOTE INTEGER, ZDATA BLOB)",
        "INSERT INTO Z_PRIMARYKEY VALUES (12,'ICNote',1,0)",
        "INSERT INTO Z_PRIMARYKEY VALUES (15,'ICFolder',1,0)",
        "INSERT INTO Z_PRIMARYKEY VALUES (14,'ICAccount',1,0)",
        (ins, (10, 15, None, "Work", None, None, None, None, None, 0, None, None)),
        (ins, (11, 15, None, "Sub", None, None, None, None, None, 0, 10, None)),
        (ins, (12, 15, None, "Recently Deleted", None, None, None, None, None, 1, None, None)),
        (ins, (13, 15, None, "Smart", None, None, None, None, None, 2, None, "{}")),
        (ins, (1, 12, "Packing checklist", None, d(2026, 5, 10), 10, 1, 0, 0, None, None, None)),
        (ins, (2, 12, "Kōrero notes", None, d(2026, 6, 1), 11, 2, 0, 0, None, None, None)),
        (ins, (3, 12, "Locked thing", None, d(2026, 6, 2), 10, 3, 1, 0, None, None, None)),
        (ins, (4, 12, "Binned note", None, d(2026, 6, 3), 12, 4, 0, 0, None, None, None)),
        (ins, (5, 12, "Old list", None, d(2024, 1, 5), 10, 5, 0, 0, None, None, None)),
        (ins, (6, 12, "Bodyless", None, d(2026, 6, 4), 10, 6, 0, 0, None, None, None)),
        ("INSERT INTO ZICNOTEDATA VALUES (1,1,?)", (note_blob("Packing checklist\nbring the spare batteries and the torch for tent nine\n" + "filler words go here " * 30 + "\nNEEDLE-ONE"),)),
        ("INSERT INTO ZICNOTEDATA VALUES (2,2,?)", (note_blob("Kōrero notes\nMāori words need macrons: whānau, tēnā koe \ufffc end"),)),
        ("INSERT INTO ZICNOTEDATA VALUES (3,3,?)", (b"\x00ENCRYPTED-NOT-GZIP-NOT-READ",)),
        ("INSERT INTO ZICNOTEDATA VALUES (4,4,?)", (note_blob("Binned note\ntrash-only-word"),)),
        ("INSERT INTO ZICNOTEDATA VALUES (5,5,?)", (note_blob("Old list\nancient pins"),)),
        "INSERT INTO ZICNOTEDATA VALUES (6,6,NULL)",
    ])


def make_reminders(path, rows=True):
    stmts = [
        "CREATE TABLE ZREMCDBASELIST (Z_PK INTEGER PRIMARY KEY, ZNAME TEXT, ZSMARTLISTTYPE TEXT, ZISGROUP INTEGER, ZMARKEDFORDELETION INTEGER)",
        "CREATE TABLE ZREMCDREMINDER (Z_PK INTEGER PRIMARY KEY, ZTITLE TEXT, ZNOTES TEXT, ZCOMPLETED INTEGER, "
        "ZCOMPLETIONDATE REAL, ZDUEDATE REAL, ZALLDAY INTEGER, ZPRIORITY INTEGER, ZFLAGGED INTEGER, ZLIST INTEGER, ZMARKEDFORDELETION INTEGER)",
        "INSERT INTO ZREMCDBASELIST VALUES (1,'Groceries',NULL,0,0)",
        "INSERT INTO ZREMCDBASELIST VALUES (2,'Errands',NULL,0,0)",
        "INSERT INTO ZREMCDBASELIST VALUES (3,NULL,'today',0,0)",
    ]
    if rows:
        due = apple(datetime(2026, 6, 1, tzinfo=timezone.utc))
        stmts += [
            ("INSERT INTO ZREMCDREMINDER VALUES (1,'Buy fixture milk','the blue top one',0,NULL,?,1,0,0,1,0)", (due,)),
            ("INSERT INTO ZREMCDREMINDER VALUES (2,'Book the dentist',NULL,0,NULL,NULL,0,1,1,2,0)", ()),
            ("INSERT INTO ZREMCDREMINDER VALUES (3,'Old milk run',NULL,1,?,NULL,0,0,0,1,0)", (due,)),
            "INSERT INTO ZREMCDREMINDER VALUES (4,'Deleted milk',NULL,0,NULL,NULL,0,0,0,1,1)",
        ]
    build(path, stmts)


# ---------------------------------------------------------------- tests ----
# ---- photos: a synthetic .photoslibrary (everything here is invented) ----

PH_A1 = "AAAAAAAA-1111-4111-8111-000000000001"  # original on disk, GPS at the reference point, album "Holiday Shelf"
PH_B2 = "BBBBBBBB-2222-4222-8222-000000000002"  # original missing, derivatives only, no GPS
PH_C3 = "CCCCCCCC-3333-4333-8333-000000000003"  # trashed
PH_D4 = "DDDDDDDD-4444-4444-8444-000000000004"  # shared-scope directory, no files at all
PH_E5 = "EEEEEEEE-5555-4555-8555-000000000005"  # GPS far away (about 400 km), nothing recognised
PH_ASSET_ENT, PH_ALBUM_ENT = 3, 40  # deliberately not the real macOS numbers: the tool must read them by name


def psi_halves(u):
    return struct.unpack("<qq", uuid.UUID(u).bytes)


def make_photos(root):
    """Returns the Photos.sqlite path inside <root>/Test.photoslibrary."""
    lib = os.path.join(root, "Test.photoslibrary")
    for d in ("database/search", "originals/A", "resources/derivatives/B", "resources/derivatives/masters/B"):
        os.makedirs(os.path.join(lib, d))
    def touch(rel, size):
        with open(os.path.join(lib, rel), "wb") as fh:
            fh.write(b"x" * size)
    touch("originals/A/%s.heic" % PH_A1, 10)
    touch("resources/derivatives/B/%s_1_105_c.jpeg" % PH_B2, 200)
    touch("resources/derivatives/B/%s_1_102_o.jpeg" % PH_B2, 500)          # the largest image: wins
    touch("resources/derivatives/B/%s.THM" % PH_B2, 9000)                   # larger but not an image: ignored
    touch("resources/derivatives/masters/B/%s_4_5005_c.jpeg" % PH_B2, 50)
    day = lambda y, m, d: apple(local_midnight(y, m, d) + timedelta(hours=12))
    asset_rows = [
        (1, PH_A1, day(2026, 3, 10), "A", PH_A1 + ".heic", -10.0, 20.0, 0, "IMG_0001.HEIC"),
        (2, PH_B2, day(2026, 3, 11), "B", PH_B2 + ".heic", -180.0, -180.0, 0, "IMG_0002.HEIC"),
        (3, PH_C3, day(2026, 3, 12), "C", PH_C3 + ".heic", -10.0, 20.0, 1, "IMG_0003.HEIC"),
        (4, PH_D4, day(2026, 3, 13), "1234/" + PH_D4, PH_D4 + ".heic", None, None, 0, None),
        (5, PH_E5, day(2026, 4, 1), "E", PH_E5 + ".heic", -13.0, 22.0, 0, "IMG_0005.HEIC"),
    ]
    st = [
        "CREATE TABLE Z_PRIMARYKEY (Z_ENT INTEGER PRIMARY KEY, Z_NAME VARCHAR, Z_SUPER INTEGER, Z_MAX INTEGER)",
        ("INSERT INTO Z_PRIMARYKEY (Z_ENT, Z_NAME) VALUES (?,?)", (PH_ASSET_ENT, "Asset")),
        ("INSERT INTO Z_PRIMARYKEY (Z_ENT, Z_NAME) VALUES (?,?)", (PH_ALBUM_ENT, "Album")),
        "CREATE TABLE ZASSET (Z_PK INTEGER PRIMARY KEY, Z_ENT INTEGER, ZUUID VARCHAR, ZDATECREATED TIMESTAMP, ZDIRECTORY VARCHAR, "
        "ZFILENAME VARCHAR, ZLATITUDE FLOAT, ZLONGITUDE FLOAT, ZTRASHEDSTATE INTEGER)",
        "CREATE TABLE ZADDITIONALASSETATTRIBUTES (Z_PK INTEGER PRIMARY KEY, ZASSET INTEGER, ZORIGINALFILENAME VARCHAR)",
        "CREATE TABLE ZGENERICALBUM (Z_PK INTEGER PRIMARY KEY, Z_ENT INTEGER, ZTITLE VARCHAR, ZTRASHEDSTATE INTEGER)",
        "CREATE TABLE Z_%dASSETS (Z_%dALBUMS INTEGER, Z_%dASSETS INTEGER)" % (PH_ALBUM_ENT, PH_ALBUM_ENT, PH_ASSET_ENT),
        "CREATE TABLE ZMEDIAANALYSISASSETATTRIBUTES (Z_PK INTEGER PRIMARY KEY, ZASSET INTEGER)",
        "CREATE TABLE ZCHARACTERRECOGNITIONATTRIBUTES (Z_PK INTEGER PRIMARY KEY, ZMEDIAANALYSISASSETATTRIBUTES INTEGER, "
        "ZCHARACTERRECOGNITIONDATA BLOB)",
    ]
    for pk, u, created, d, f, lat, lon, trashed, orig in asset_rows:
        st.append(("INSERT INTO ZASSET VALUES (?,?,?,?,?,?,?,?,?)", (pk, PH_ASSET_ENT, u, created, d, f, lat, lon, trashed)))
        st.append(("INSERT INTO ZADDITIONALASSETATTRIBUTES (ZASSET, ZORIGINALFILENAME) VALUES (?,?)", (pk, orig)))
    st += [
        ("INSERT INTO ZGENERICALBUM VALUES (?,?,?,?)", (1, PH_ALBUM_ENT, "Holiday Shelf", 0)),
        ("INSERT INTO ZGENERICALBUM VALUES (?,?,?,?)", (2, PH_ALBUM_ENT, "Holiday Old", 1)),  # trashed album
        ("INSERT INTO ZGENERICALBUM VALUES (?,?,?,?)", (3, 99, "Holiday Folder", 0)),          # not an Album entity
        ("INSERT INTO Z_%dASSETS VALUES (1, 1)" % PH_ALBUM_ENT),
        ("INSERT INTO Z_%dASSETS VALUES (2, 2)" % PH_ALBUM_ENT),
        ("INSERT INTO Z_%dASSETS VALUES (3, 5)" % PH_ALBUM_ENT),
    ]
    # recognised text: A1, B2 and the trashed C3 carry data; D4 has an analysis row with NULL data
    for pk, asset in ((1, 1), (2, 2), (3, 3), (4, 4)):
        st.append(("INSERT INTO ZMEDIAANALYSISASSETATTRIBUTES VALUES (?,?)", (pk, asset)))
    for pk, data in ((1, b"x"), (2, b"x"), (3, b"x"), (4, None)):
        st.append(("INSERT INTO ZCHARACTERRECOGNITIONATTRIBUTES VALUES (?,?,?)", (pk, pk, data)))
    db = os.path.join(lib, "database", "Photos.sqlite")
    build(db, st)

    # psi.sqlite. Strings are NUL-terminated, as Photos writes them (measured).
    groups = [  # (rowid, category, normalized_string, [asset rowids])
        (1, 1203, "x9000", [1, 2, 3]),
        (2, 1203, "serial", [1]),
        (3, 1202, "blue bike", [2]),
        (4, 1203, "plate", [4]),
        (5, 1100, "x9000", [5]),        # same word in a place category: must NOT match
        (6, 1203, "x9000b", [4]),       # substring of a longer token: matches "x9000"
        (7, 1203, "cafe", [1]),         # psi stores folded text; a query typed with an accent must still find it
    ]
    ps = [
        "CREATE TABLE groups (category INT2, owning_groupid INT, normalized_string TEXT)",
        "CREATE TABLE assets (uuid_0 INT, uuid_1 INT, creationDate INT, UNIQUE(uuid_0, uuid_1))",
        "CREATE TABLE ga (groupid INT, assetid INT, PRIMARY KEY(groupid, assetid))",
    ]
    for i, u in enumerate((PH_A1, PH_B2, PH_C3, PH_D4, PH_E5), start=1):
        a, b = psi_halves(u)
        ps.append(("INSERT INTO assets (rowid, uuid_0, uuid_1, creationDate) VALUES (?,?,?,0)", (i, a, b)))
    for rid, cat, norm, assets in groups:
        ps.append(("INSERT INTO groups (rowid, category, owning_groupid, normalized_string) VALUES (?,?,0,?)", (rid, cat, norm + "\x00")))
        for a in assets:
            ps.append(("INSERT INTO ga VALUES (?,?)", (rid, a)))
    build(os.path.join(lib, "database", "search", "psi.sqlite"), ps)
    return db


class OpenReadOnly(TmpCase):
    def test_write_is_refused_and_file_unchanged(self):
        p = self.path("c.sqlite")
        make_contacts(p)
        before = read_bytes(p)
        con = cc.open_ro(p)
        with self.assertRaises(sqlite3.OperationalError):
            con.execute("INSERT INTO ZABCDRECORD (Z_PK, ZFIRSTNAME) VALUES (99,'No')")
        with self.assertRaises(sqlite3.OperationalError):
            con.execute("DROP TABLE ZABCDRECORD")
        con.close()
        self.assertEqual(read_bytes(p), before)
        self.assertEqual(sorted(os.listdir(self.dir)), ["c.sqlite"], "no -wal/-shm/-journal litter")

    def test_path_with_spaces_and_odd_characters_opens(self):
        d = os.path.join(self.dir, "Group Containers", "a b#c")
        os.makedirs(d)
        p = os.path.join(d, "x.sqlite")
        make_contacts(p)
        self.assertEqual(len(cc.search_contacts([p], name="alex")), 1)

    def test_uri_asks_for_ro_and_immutable(self):
        seen = []
        real = sqlite3.connect
        sqlite3.connect = lambda target, **kw: (seen.append((target, kw)), real(":memory:"))[1]  # records, then opens a harmless in-memory db
        try:
            cc.open_ro("/x/y z.sqlite")
        finally:
            sqlite3.connect = real
        uri, kw = seen[0]
        self.assertIn("mode=ro", uri)
        self.assertIn("immutable=1", uri)
        self.assertTrue(kw.get("uri"))
        self.assertIn("y%20z", uri)


class Times(unittest.TestCase):
    def test_seconds_and_nanoseconds_agree(self):
        dt = datetime(2026, 3, 1, 9, 0, tzinfo=timezone.utc)
        self.assertEqual(cc.ts_to_datetime(apple(dt)), dt)
        self.assertEqual(cc.ts_to_datetime(int(apple(dt) * 1e9)), dt)

    def test_none_and_zero(self):
        self.assertIsNone(cc.ts_to_datetime(None))
        self.assertEqual(cc.ts_to_datetime(0), APPLE_EPOCH)

    def test_parse_day_until_is_inclusive_and_bad_date_is_usage(self):
        a = cc.parse_day("2026-05-10")
        b = cc.parse_day("2026-05-10", end_of_day=True)
        self.assertEqual(b - a, timedelta(days=1))
        with self.assertRaises(cc.UsageError):
            cc.parse_day("10/05/2026")

    def test_compact_yyyymmdd_means_the_same_day(self):
        self.assertEqual(cc.parse_day("20260510"), cc.parse_day("2026-05-10"))
        self.assertEqual(cc.parse_day("20260510", end_of_day=True), cc.parse_day("2026-05-10", end_of_day=True))
        for bad in ("2026051", "202605100", "20261301", "2026-5-1x"):
            with self.assertRaises(cc.UsageError, msg=bad):
                cc.parse_day(bad)


class AttributedBody(unittest.TestCase):
    def test_short_length(self):
        self.assertEqual(cc.decode_attributed_body(typedstream("hello there")), "hello there")

    def test_u16_length_and_unicode(self):
        text = "Kia ora — " + "tēnā koe " * 40
        self.assertGreater(len(text.encode()), 255)
        self.assertEqual(cc.decode_attributed_body(typedstream(text, "u32")), text)
        self.assertEqual(cc.decode_attributed_body(typedstream("x" * 200, "u16")), "x" * 200)

    def test_garbage_and_truncation_return_none_not_junk(self):
        self.assertIsNone(cc.decode_attributed_body(None))
        self.assertIsNone(cc.decode_attributed_body(b""))
        self.assertIsNone(cc.decode_attributed_body(b"no marker here"))
        blob = typedstream("a longer message than the cut")
        self.assertIsNone(cc.decode_attributed_body(blob[:blob.index(b"a longer") + 4]))


class Handles(unittest.TestCase):
    def test_phone_formats_agree_and_email_lowercases(self):
        self.assertEqual(cc.handle_key("+44 20 7946 0101"), cc.handle_key("020-7946-0101"))
        self.assertEqual(cc.handle_key("Sam@Example.Invalid"), "sam@example.invalid")  # leakscan:allow:email: fictional address in the reserved .invalid TLD (RFC 2606), a test fixture
        self.assertEqual(cc.handle_key(None), "")

    def test_looks_like_handle(self):
        for v in ("+442079460101", "020 7946 0101", "a@b.invalid"):  # leakscan:allow:email: fictional address in the reserved .invalid TLD (RFC 2606), a test fixture
            self.assertTrue(cc.looks_like_handle(v), v)
        for v in ("Alex", "Alex 2", "5"):
            self.assertFalse(cc.looks_like_handle(v), v)


class Contacts(TmpCase):
    def setUp(self):
        super().setUp()
        self.p = self.path("book.abcddb")
        make_contacts(self.p)

    def test_requires_a_filter(self):
        with self.assertRaises(cc.UsageError):
            cc.search_contacts([self.p])

    def test_name_is_case_and_accent_insensitive_and_multiword(self):
        self.assertEqual([r["name"] for r in cc.search_contacts([self.p], name="maori")], ["Māori Fixture"])
        self.assertEqual([r["name"] for r in cc.search_contacts([self.p], name="example alex")], ["Alex Example"])
        self.assertEqual(cc.search_contacts([self.p], name="nobody"), [])

    def test_phone_matches_across_formats(self):
        got = cc.search_contacts([self.p], phone="02079460101")
        self.assertEqual([r["name"] for r in got], ["Alex Example"])
        got = cc.search_contacts([self.p], phone="+44 20 7946 0202")
        self.assertEqual([r["name"] for r in got], ["Sam Sample"])
        with self.assertRaises(cc.UsageError):
            cc.search_contacts([self.p], phone="abc")

    def test_email_org_and_labels_cleaned(self):
        got = cc.search_contacts([self.p], email="ALEX@example")
        self.assertEqual(got[0]["phones"][0]["label"], "Mobile")
        self.assertEqual(got[0]["emails"][0]["label"], "Work")
        self.assertEqual([r["name"] for r in cc.search_contacts([self.p], org="sample co")], ["Sam Sample"])

    def test_unnamed_rows_never_listed_and_limit_caps(self):
        self.assertEqual(len(cc.search_contacts([self.p], name="a")), 3)  # Alex, Sam (Sample), Māori; not the unnamed row
        self.assertEqual(len(cc.search_contacts([self.p], name="a", limit=2)), 2)

    def test_searches_every_source(self):
        q = self.path("second.abcddb")
        make_contacts(q)
        build(q, ["UPDATE ZABCDRECORD SET ZFIRSTNAME='Pat' WHERE Z_PK=1"])
        names = [r["name"] for r in cc.search_contacts([self.p, q], name="example")]
        self.assertEqual(sorted(names), ["Alex Example", "Pat Example"])

    def test_empty_source_without_tables_is_skipped(self):
        e = self.path("empty.abcddb")
        build(e, ["CREATE TABLE other (x)"])
        self.assertEqual(len(cc.search_contacts([e, self.p], name="alex")), 1)


class Messages(TmpCase):
    def setUp(self):
        super().setUp()
        self.db = self.path("chat.db")
        self.book = self.path("book.abcddb")
        make_messages(self.db)
        make_contacts(self.book)

    def search(self, **kw):
        return cc.search_messages(self.db, [self.book], **kw)

    def test_requires_a_filter(self):
        with self.assertRaises(cc.UsageError):
            self.search()

    def test_person_by_name_returns_one_to_one_thread_and_their_group_posts_only(self):
        got = self.search(person="alex")
        self.assertEqual([m["id"] for m in got], [1, 2, 5])  # not the stranger's group message (4)
        self.assertEqual(got[0]["text"], "meet at the museum at nine")  # body came from the blob
        self.assertEqual(got[0]["from"], "Alex Example")  # handle resolved to a name
        self.assertEqual(got[1]["from"], "me")
        self.assertEqual(got[2]["chat"], "Fixture Group")

    def test_person_by_handle_in_another_format(self):
        self.assertEqual([m["id"] for m in self.search(person="020 7946 0202")], [3, 6])

    def test_unknown_name_is_usage_not_silence(self):
        with self.assertRaises(cc.UsageError):
            self.search(person="nobody at all")

    def test_text_search_finds_blob_only_bodies_case_and_accent_insensitive(self):
        got = self.search(text="MUSEUM")
        self.assertEqual([m["id"] for m in got], [1])
        self.assertEqual([m["id"] for m in self.search(text="bike")], [3])  # old seconds-dated row

    def test_date_window_handles_seconds_and_nanoseconds(self):
        self.assertEqual([m["id"] for m in self.search(since="2015-01-01", until="2015-12-31")], [3])
        ids = [m["id"] for m in self.search(since="2026-01-01")]
        self.assertEqual(ids, [1, 2, 4, 5, 6])
        # --until is inclusive of the day: 2 Mar 2026 09:00 UTC is on or before 3 Mar local in any NZ/UTC zone
        self.assertNotIn(5, [m["id"] for m in self.search(since="2026-01-01", until="2026-03-01")])

    def test_limit_keeps_newest_and_shows_oldest_first(self):
        got = self.search(since="2026-01-01", limit=2)
        self.assertEqual([m["id"] for m in got], [5, 6])

    def test_attachment_only_message_flagged(self):
        got = self.search(since="2026-03-04")
        self.assertEqual(got[0]["id"], 6)
        self.assertTrue(got[0]["attachments"])
        self.assertIsNone(got[0]["text"])

    def test_works_without_contacts(self):
        got = cc.search_messages(self.db, [], person="+442079460101")
        self.assertEqual([m["id"] for m in got], [1, 2, 5])
        self.assertEqual(got[0]["from"], "+442079460101")

    def test_read_only_no_litter(self):
        before = read_bytes(self.db)
        self.search(text="museum")
        self.assertEqual(read_bytes(self.db), before)
        self.assertFalse([f for f in os.listdir(self.dir) if f.endswith(("-wal", "-shm", "-journal"))])


class Calendar(TmpCase):
    def setUp(self):
        super().setUp()
        self.db = self.path("Calendar.sqlitedb")
        make_calendar(self.db)

    def test_requires_a_filter(self):
        with self.assertRaises(cc.UsageError):
            cc.search_calendar(self.db)

    def test_window_returns_oneoffs_allday_and_cached_occurrences_not_tasks(self):
        got = cc.search_calendar(self.db, since="2026-05-09", until="2026-05-19")
        titles = [(e["title"], e["start"][:10]) for e in got]
        self.assertEqual(titles, sorted(titles, key=lambda t: t[1]), "sorted by start")
        self.assertEqual(sorted(titles), sorted([("Review meeting", "2026-05-10"), ("Fixture day off", "2026-05-12"),
                                                 ("Weekly fixture sync", "2026-05-11"), ("Weekly fixture sync", "2026-05-18")]))
        self.assertNotIn("A task not an event", [e["title"] for e in got])

    def test_all_day_shown_as_plain_date_and_location_joined(self):
        by = {e["title"]: e for e in cc.search_calendar(self.db, since="2026-05-09", until="2026-05-13")}
        self.assertEqual(by["Fixture day off"]["start"], "2026-05-12")
        self.assertTrue(by["Fixture day off"]["all_day"])
        self.assertEqual(by["Review meeting"]["location"], "Test Venue")
        self.assertEqual(by["Review meeting"]["notes"], "bring the agenda")
        self.assertTrue(by["Weekly fixture sync"]["repeats"])

    def test_recurring_outside_cache_window_absent_and_master_shown_without_dates(self):
        self.assertEqual(cc.search_calendar(self.db, since="2026-07-01", until="2026-07-31"), [])
        got = cc.search_calendar(self.db, text="weekly")
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0]["start"][:10], "2025-01-06")  # the series master, once
        self.assertTrue(got[0]["repeats"])

    def test_calendar_name_and_text_filters(self):
        got = cc.search_calendar(self.db, since="2026-05-09", until="2026-05-19", calendar="personal")
        self.assertEqual([e["title"] for e in got], ["Fixture day off"])
        got = cc.search_calendar(self.db, since="2026-05-09", until="2026-05-19", text="VENUE")  # via location
        self.assertEqual([e["title"] for e in got], ["Review meeting"])
        self.assertEqual(cc.search_calendar(self.db, calendar="%"), [])  # LIKE wildcards are escaped

    def test_limit(self):
        self.assertEqual(len(cc.search_calendar(self.db, since="2026-05-09", until="2026-05-19", limit=2)), 2)


class Reminders(TmpCase):
    def setUp(self):
        super().setUp()
        self.p = self.path("Data-A.sqlite")
        self.empty = self.path("Data-B.sqlite")
        make_reminders(self.p)
        make_reminders(self.empty, rows=False)

    def test_requires_a_filter(self):
        with self.assertRaises(cc.UsageError):
            cc.search_reminders([self.p])

    def test_open_only_skips_done_and_deleted_and_reads_all_stores(self):
        got = cc.search_reminders([self.empty, self.p], open_only=True)
        self.assertEqual([r["title"] for r in got], ["Buy fixture milk", "Book the dentist"])  # dated first, undated last

    def test_list_and_text_filters(self):
        self.assertEqual([r["title"] for r in cc.search_reminders([self.p], list_name="errands")], ["Book the dentist"])
        got = cc.search_reminders([self.p], text="MILK")
        self.assertEqual([r["title"] for r in got], ["Buy fixture milk", "Old milk run"])  # open before done, no deleted
        self.assertEqual([r["title"] for r in cc.search_reminders([self.p], text="blue top")], ["Buy fixture milk"])

    def test_fields(self):
        r = {x["title"]: x for x in cc.search_reminders([self.p], open_only=True)}
        self.assertEqual(r["Buy fixture milk"]["due"], "2026-06-01")  # all-day shown as a date
        self.assertEqual(r["Buy fixture milk"]["list"], "Groceries")
        self.assertTrue(r["Book the dentist"]["flagged"])
        self.assertEqual(r["Book the dentist"]["priority"], 1)
        self.assertIsNone(r["Book the dentist"]["due"])

    def test_limit(self):
        self.assertEqual(len(cc.search_reminders([self.p], open_only=True, limit=1)), 1)


class NoteBody(unittest.TestCase):
    def test_round_trip_ascii_and_multibyte(self):
        for text in ("plain text", "Māori — tēnā koe \U0001F33F", "x" * 5000):
            self.assertEqual(cc.decode_note_body(note_blob(text)), text)

    def test_attachment_marker_replaced(self):
        self.assertEqual(cc.decode_note_body(note_blob("a\ufffcb")), "a[attachment]b")

    def test_not_decodable_is_none_never_a_guess(self):
        self.assertIsNone(cc.decode_note_body(None))
        self.assertIsNone(cc.decode_note_body(b""))
        self.assertIsNone(cc.decode_note_body(b"not gzip at all"))
        self.assertIsNone(cc.decode_note_body(note_blob("t", gz=False)))  # protobuf but not gzipped
        gz = note_blob("some body text here")
        self.assertIsNone(cc.decode_note_body(gz[: len(gz) // 2]))          # truncated stream
        no_text = zlib.compressobj(wbits=31)
        blob = no_text.compress(pb_field(1, 0) + pb_field(2, pb_field(3, pb_field(7, 1)))) + no_text.flush()
        self.assertIsNone(cc.decode_note_body(blob))                        # path absent

    def test_protobuf_reader_handles_all_wire_types_and_rejects_bad_ones(self):
        msg = pb_field(1, 300) + pb_field(2, b"ab") + b"\x29" + b"\x00" * 8 + b"\x35" + b"\x00" * 4
        self.assertEqual([(f, w) for f, w, _ in cc._proto_fields(msg)], [(1, 0), (2, 2), (5, 1), (6, 5)])
        self.assertEqual(next(cc._proto_fields(pb_field(1, 300)))[2], 300)
        for bad in (b"\x12\x05ab", b"\x0b", b"\x80", b"\x00\x01"):  # truncated, group, bad varint, field 0
            with self.assertRaises(cc.ProtoError):
                list(cc._proto_fields(bad))

    def test_gunzip_is_capped(self):
        saved = cc.MAX_NOTE_BYTES
        cc.MAX_NOTE_BYTES = 100
        try:
            self.assertIsNone(cc.decode_note_body(note_blob("y" * 5000)))
        finally:
            cc.MAX_NOTE_BYTES = saved


class Notes(TmpCase):
    def setUp(self):
        super().setUp()
        self.p = self.path("NoteStore.sqlite")
        make_notes(self.p)

    def titles(self, **kw):
        return [r["title"] for r in cc.search_notes(self.p, **kw)]

    def test_no_filter_refused(self):
        with self.assertRaises(cc.UsageError):
            cc.search_notes(self.p)
        with self.assertRaises(cc.UsageError):
            cc.search_notes(self.p, include_deleted=True, full=True)  # switches are not filters

    def test_title_text_folder_and_date_filters(self):
        self.assertEqual(self.titles(title="packing"), ["Packing checklist"])
        self.assertEqual(self.titles(text="spare batteries"), ["Packing checklist"])
        self.assertEqual(self.titles(folder="work"), ["Bodyless", "Locked thing", "Kōrero notes", "Packing checklist", "Old list"])
        self.assertEqual(self.titles(folder="work/sub"), ["Kōrero notes"])
        self.assertEqual(self.titles(since="2026-05-01", until="2026-05-31"), ["Packing checklist"])
        self.assertEqual(self.titles(until="2024-12-31"), ["Old list"])
        self.assertEqual(self.titles(title="packing", text="tent"), ["Packing checklist"])
        self.assertEqual(self.titles(title="packing", text="no such words"), [])

    def test_folder_includes_parent_path_and_modified_date(self):
        r = cc.search_notes(self.p, title="korero")[0]
        self.assertEqual((r["folder"], r["modified"][:7]), ("Work/Sub", "2026-06"))

    def test_multibyte_and_accent_insensitive(self):
        self.assertEqual(self.titles(text="maori"), ["Kōrero notes"])
        self.assertEqual(self.titles(text="TENA KOE"), ["Kōrero notes"])
        self.assertEqual(self.titles(title="korero"), ["Kōrero notes"])
        snip = cc.search_notes(self.p, text="whanau")[0]["snippet"]
        self.assertIn("whānau, tēnā koe [attachment] end", snip)

    def test_snippet_is_around_the_match_not_the_note(self):
        body = "start " + "filler " * 60 + "THE-NEEDLE" + " filler" * 60 + " finish"
        p2 = self.path("long.sqlite")
        make_notes(p2)
        con = sqlite3.connect(p2)
        con.execute("UPDATE ZICNOTEDATA SET ZDATA=? WHERE Z_PK=1", (note_blob(body),))
        con.commit(); con.close()
        r = cc.search_notes(p2, text="the-needle")[0]
        self.assertIn("THE-NEEDLE", r["snippet"])
        self.assertLess(len(r["snippet"]), 2 * cc.SNIPPET_CONTEXT + 40)
        self.assertTrue(r["snippet"].startswith("…") and r["snippet"].endswith("…"))
        self.assertNotIn("text", r)

    def test_title_only_match_shows_body_opening_without_repeating_title(self):
        r = cc.search_notes(self.p, title="packing")[0]
        self.assertTrue(r["snippet"].startswith("bring the spare batteries"))

    def test_locked_note_listed_flagged_never_read(self):
        rows = {r["title"]: r for r in cc.search_notes(self.p, since="2026-06-01")}
        locked = rows["Locked thing"]
        self.assertTrue(locked["locked"])
        self.assertIsNone(locked["snippet"])
        self.assertTrue(locked["decoded"])  # nothing was attempted, so nothing failed
        # --text cannot see inside a locked note: it is left out, not listed as a hit
        self.assertEqual(self.titles(text="encrypted"), [])
        self.assertEqual(cc.locked_count(self.p), 1)
        # and the encrypted bytes are never passed to the decoder
        calls = []
        real = cc.decode_note_body
        cc.decode_note_body = lambda z: (calls.append(z), real(z))[1]
        try:
            cc.search_notes(self.p, since="2000-01-01")
        finally:
            cc.decode_note_body = real
        self.assertNotIn(b"\x00ENCRYPTED-NOT-GZIP-NOT-READ", calls)

    def test_locked_note_refuses_full(self):
        with self.assertRaises(cc.UsageError) as cm:
            cc.search_notes(self.p, note_id=3, full=True)
        self.assertIn("locked", str(cm.exception))

    def test_trashed_hidden_unless_asked(self):
        self.assertEqual(self.titles(title="binned"), [])
        self.assertEqual(self.titles(text="trash-only-word"), [])
        r = cc.search_notes(self.p, text="trash-only-word", include_deleted=True)
        self.assertEqual([(x["title"], x["deleted"]) for x in r], [("Binned note", True)])

    def test_note_with_no_body_is_flagged_not_dropped(self):
        r = cc.search_notes(self.p, title="bodyless")[0]
        self.assertFalse(r["decoded"])
        self.assertIsNone(r["snippet"])
        self.assertEqual(self.titles(title="bodyless", text="x"), [])

    def test_full_needs_exactly_one_match(self):
        with self.assertRaises(cc.UsageError) as cm:
            cc.search_notes(self.p, since="2000-01-01", full=True)
        self.assertIn("matched", str(cm.exception))
        with self.assertRaises(cc.UsageError):
            cc.search_notes(self.p, title="zzz", full=True)  # zero matches is not one
        r = cc.search_notes(self.p, text="spare batteries", full=True)
        self.assertEqual(len(r), 1)
        self.assertIn("NEEDLE-ONE", r[0]["text"])
        self.assertNotIn("snippet", r[0])
        r = cc.search_notes(self.p, note_id=2, full=True)
        self.assertIn("Māori words", r[0]["text"])

    def test_limit_caps_results_newest_first(self):
        r = cc.search_notes(self.p, since="2000-01-01", limit=2)
        self.assertEqual([x["title"] for x in r], ["Bodyless", "Locked thing"])

    def test_store_is_untouched(self):
        before = read_bytes(self.p)
        cc.search_notes(self.p, since="2000-01-01", include_deleted=True)
        self.assertEqual(read_bytes(self.p), before)
        self.assertEqual(sorted(os.listdir(self.dir)), ["NoteStore.sqlite"])

    def test_not_a_notes_store_is_a_store_error(self):
        other = self.path("c")
        make_contacts(other)
        with self.assertRaises(sqlite3.Error):
            cc.search_notes(other, title="x")


class Photos(TmpCase):
    def setUp(self):
        super().setUp()
        self.db = make_photos(self.dir)
        self.lib = os.path.dirname(os.path.dirname(self.db))

    def uuids(self, **kw):
        return [r["uuid"] for r in cc.search_photos(self.db, **kw)]

    def test_uuid_is_packed_little_endian(self):
        a, b = psi_halves(PH_A1)
        self.assertEqual(cc.psi_uuid(a, b), PH_A1)
        self.assertNotEqual(cc.psi_uuid(*struct.unpack(">qq", uuid.UUID(PH_A1).bytes)), PH_A1)
        self.assertEqual(cc.psi_uuid(-1, -1), "FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF")  # signed halves are fine

    def test_no_filter_is_refused(self):
        with self.assertRaises(cc.UsageError):
            cc.search_photos(self.db)

    def test_text_finds_recognised_text_and_captions_not_other_categories(self):
        # newest first; C3 is trashed, E5 only has "x9000" in a place category, D4 has the longer token x9000b
        self.assertEqual(self.uuids(text="x9000"), [PH_D4, PH_B2, PH_A1])
        self.assertEqual(self.uuids(text="BLUE"), [PH_B2])      # a caption, case-insensitive

    def test_text_needs_every_word(self):
        self.assertEqual(self.uuids(text="x9000 serial"), [PH_A1])
        self.assertEqual(self.uuids(text="serial blue"), [])

    def test_text_query_is_accent_folded_and_wildcards_are_literal(self):
        self.assertEqual(self.uuids(text="Café"), [PH_A1])
        self.assertEqual(self.uuids(text="x9%"), [])
        self.assertEqual(self.uuids(text="x_000"), [])

    def test_trashed_assets_are_skipped_unless_asked(self):
        self.assertNotIn(PH_C3, self.uuids(text="x9000"))
        rows = cc.search_photos(self.db, text="x9000", include_deleted=True)
        self.assertIn(PH_C3, [r["uuid"] for r in rows])
        self.assertTrue([r for r in rows if r["uuid"] == PH_C3][0]["deleted"])

    def test_original_on_disk_is_the_viewable_path(self):
        r = cc.search_photos(self.db, uuid=PH_A1)[0]
        self.assertTrue(r["original_on_disk"])
        self.assertEqual(r["viewable_kind"], "original")
        self.assertEqual(r["viewable_path"], os.path.join(self.lib, "originals", "A", PH_A1 + ".heic"))
        self.assertEqual(r["filename"], "IMG_0001.HEIC")

    def test_missing_original_falls_back_to_largest_derivative_image(self):
        r = cc.search_photos(self.db, uuid=PH_B2)[0]
        self.assertFalse(r["original_on_disk"])
        self.assertEqual(r["viewable_kind"], "derivative")
        self.assertTrue(r["viewable_path"].endswith(PH_B2 + "_1_102_o.jpeg"), r["viewable_path"])  # not the bigger .THM
        self.assertTrue(os.path.isfile(r["viewable_path"]))

    def test_no_files_at_all_reports_none_not_a_guess(self):
        r = cc.search_photos(self.db, uuid=PH_D4)[0]
        self.assertFalse(r["original_on_disk"])
        self.assertIsNone(r["viewable_path"])
        self.assertIsNone(r["viewable_kind"])
        self.assertEqual(r["filename"], PH_D4 + ".heic")  # no camera-roll name recorded: the stored name

    def test_masters_and_cvt_folders_are_considered(self):
        os.makedirs(os.path.join(self.lib, "resources", "derivatives", "cvt", "D", PH_D4))
        with open(os.path.join(self.lib, "resources", "derivatives", "cvt", "D", PH_D4, PH_D4 + "_cvt_t0000.jpeg"), "wb") as fh:
            fh.write(b"x" * 5)
        r = cc.search_photos(self.db, uuid=PH_D4)[0]
        self.assertTrue(r["viewable_path"].endswith("_cvt_t0000.jpeg"))

    def test_gps_present_absent_and_minus_180_sentinel(self):
        by = {r["uuid"]: r for r in cc.search_photos(self.db, since="2026-01-01")}
        self.assertEqual(by[PH_A1]["gps"], {"lat": -10.0, "lon": 20.0})
        self.assertIsNone(by[PH_B2]["gps"])   # -180 means "none"
        self.assertIsNone(by[PH_D4]["gps"])   # NULL

    def test_near_uses_distance_and_ignores_assets_without_gps(self):
        rows = cc.search_photos(self.db, near="-10.0,20.0")
        self.assertEqual([r["uuid"] for r in rows], [PH_A1])
        self.assertEqual(rows[0]["distance_km"], 0.0)
        self.assertEqual(self.uuids(near="-10.0,20.0,5000"), [PH_E5, PH_A1])   # the second point is ~400 km away
        self.assertEqual(self.uuids(near="-10.0,20.0,100"), [PH_A1])
        # roughly 0.8 km north: outside the 0.5 km default window, inside 1 km
        self.assertEqual(self.uuids(near="-9.993,20.0,0.5"), [])
        self.assertEqual(self.uuids(near="-9.993,20.0"), [PH_A1])

    def test_bad_near_is_a_usage_error(self):
        for bad in ("x", "1", "1,2,3,4", "95,0", "0,200", "0,0,0", "0,0,-3"):
            with self.assertRaises(cc.UsageError, msg=bad):
                cc.search_photos(self.db, near=bad)

    def test_since_until_inclusive_of_the_day(self):
        self.assertEqual(self.uuids(since="2026-03-11", until="2026-03-13"), [PH_D4, PH_B2])  # C3 trashed
        self.assertEqual(self.uuids(until="2026-03-10"), [PH_A1])
        with self.assertRaises(cc.UsageError):
            cc.search_photos(self.db, since="March")

    def test_uuid_accepts_lowercase_and_braces(self):
        self.assertEqual(self.uuids(uuid="{" + PH_E5.lower() + "}"), [PH_E5])
        self.assertEqual(self.uuids(uuid="00000000-0000-4000-8000-000000000000"), [])

    def test_album_by_name_reads_entity_numbers_and_skips_trashed_albums_and_non_albums(self):
        self.assertEqual(self.uuids(album="holiday"), [PH_A1])   # B2 sits in the trashed album, E5 in a non-Album row
        self.assertEqual(self.uuids(album="shelf"), [PH_A1])
        self.assertEqual(self.uuids(album="old"), [])       # trashed album
        self.assertEqual(self.uuids(album="folder"), [])    # a different entity
        self.assertEqual(self.uuids(album="nonesuch"), [])

    def test_filters_combine(self):
        self.assertEqual(self.uuids(text="x9000", since="2026-03-11"), [PH_D4, PH_B2])
        self.assertEqual(self.uuids(text="x9000", near="-10.0,20.0"), [PH_A1])
        self.assertEqual(self.uuids(text="x9000", album="shelf"), [PH_A1])

    def test_limit(self):
        self.assertEqual(len(cc.search_photos(self.db, since="2000-01-01", limit=2)), 2)

    def test_search_writes_nothing(self):
        psi = os.path.join(self.lib, "database", "search", "psi.sqlite")
        before = (read_bytes(self.db), read_bytes(psi))
        listing = sorted(os.listdir(os.path.join(self.lib, "database")))
        cc.search_photos(self.db, text="x9000", album="shelf", near="-10.0,20.0,100", since="2000-01-01")
        self.assertEqual((read_bytes(self.db), read_bytes(psi)), before)
        self.assertEqual(sorted(os.listdir(os.path.join(self.lib, "database"))), listing)
        with self.assertRaises(sqlite3.OperationalError):
            cc.open_ro(psi).execute("DELETE FROM ga")

    def test_missing_search_index_is_a_store_error(self):
        os.remove(os.path.join(self.lib, "database", "search", "psi.sqlite"))
        with self.assertRaises(sqlite3.Error):
            cc.search_photos(self.db, text="x9000")
        self.assertEqual(self.uuids(since="2026-03-10", until="2026-03-10"), [PH_A1])  # non-text searches do not need it

    def test_status_counts(self):
        report = cc.status({"photos": [self.db]})
        e = [x for x in report if x["app"] == "photos"][0]
        self.assertTrue(e["opens_read_only"])
        # not trashed: A1, B2, D4, E5. Recognised text (non-NULL data, not trashed): A1, B2.
        self.assertEqual(e["counts"], {"assets": 4, "with_recognised_text": 2, "originals_on_disk": 1, "indexed_assets": 5})
        blob = json.dumps(e) + cc.render_status([e])
        for secret in (PH_A1, "IMG_0001", "x9000", "serial"):
            self.assertNotIn(secret, blob)

# ---- home: a synthetic HomeKit core.sqlite (everything here is invented) ----

HM_ROOM, HM_ZONE, HM_SET, HM_TRIG = 11, 12, 7, 8  # deliberately not the real macOS entity numbers
HM_SECRETS = ("SENTINEL-PASSWORD", "SENTINEL-PSK", "SENTINEL-KEY", "SENTINEL-SSID", "SENTINEL-PAIRING", "SENTINEL-AUTH")


def make_home(path):
    """Home 1 'Test House' (owned) with a blank default room, Hall, Lounge and a macron room;
    home 2 'Sample Cabin' (shared) with only its blank default room. Zone 'Downstairs' holds
    Hall and Lounge; 'Empty Zone' holds nothing. Accessories: a lamp, a hub, a sensor bridged
    behind the hub, and a TV in the cabin. Scenes: wake-up, a user-defined one, a hidden
    automation-owned one, a departure in the cabin. Automations: an event trigger (runs the
    hidden scene) and an inactive timer (runs the user-defined scene)."""
    uid = lambda short: bytes.fromhex("%08x" % short) + bytes.fromhex("0000100080000026bb765291")
    custom = bytes(range(16))
    ts = apple(datetime(2026, 5, 1, 12, tzinfo=timezone.utc))
    acc = ("INSERT INTO ZMKFACCESSORY (Z_PK, Z_ENT, ZCONFIGUREDNAME, ZPROVIDEDNAME, ZMANUFACTURER, ZMODEL, ZSERIALNUMBER, "
           "ZFIRMWAREVERSION, ZACCESSORYCATEGORY, ZROOM, ZHOME, ZHOSTACCESSORY, ZPASSWORD, ZPUBLICKEY, ZWIFIUNIQUEPRESHAREDKEY, "
           "ZPAIRINGIDENTITY) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
    svc = "INSERT INTO ZMKFSERVICE (Z_PK, ZACCESSORY, ZNAME, ZPROVIDEDNAME, ZSERVICETYPE) VALUES (?,?,?,?,?)"
    secret = ("SENTINEL-PASSWORD", b"SENTINEL-KEY", "SENTINEL-PSK", b"SENTINEL-PAIRING")
    build(path, [
        "CREATE TABLE Z_PRIMARYKEY (Z_ENT INTEGER PRIMARY KEY, Z_NAME VARCHAR, Z_SUPER INTEGER, Z_MAX INTEGER)",
        "INSERT INTO Z_PRIMARYKEY VALUES (20,'MKFHAPAccessory',0,0),(21,'MKFAppleMediaAccessory',0,0),"
        "(11,'MKFRoom',0,0),(12,'MKFZone',0,0),(7,'MKFActionSet',0,0),(8,'MKFTrigger',0,0),"
        "(30,'MKFEventTrigger',8,0),(31,'MKFTimerTrigger',8,0),(9,'MKFUser',0,0)",
        "CREATE TABLE ZMKFHOME (Z_PK INTEGER PRIMARY KEY, ZNAME VARCHAR, ZOWNED INTEGER, ZDEFAULTROOM INTEGER, ZCREATIONDATE TIMESTAMP, "
        "ZPRIMARYWIFISSID VARCHAR, ZOWNERPUBLICKEY BLOB)",
        ("INSERT INTO ZMKFHOME VALUES (1,'Test House',1,1,?,'SENTINEL-SSID',x'53454e54494e454c2d4b4559')", (ts,)),
        "INSERT INTO ZMKFHOME VALUES (2,'Sample Cabin',0,5,NULL,NULL,NULL)",
        "CREATE TABLE ZMKFROOM (Z_PK INTEGER PRIMARY KEY, ZNAME VARCHAR, ZHOME INTEGER)",
        "INSERT INTO ZMKFROOM VALUES (1,NULL,1),(2,'Hall',1),(3,'Lounge',1),(4,'Whare Wānanga',1),(5,'',2)",
        "CREATE TABLE ZMKFZONE (Z_PK INTEGER PRIMARY KEY, ZNAME VARCHAR, ZHOME INTEGER)",
        "INSERT INTO ZMKFZONE VALUES (1,'Downstairs',1),(2,'Empty Zone',1)",
        "CREATE TABLE Z_11ZONES_ (Z_11ROOMS_ INTEGER, Z_12ZONES_ INTEGER)",   # room <-> zone, named by entity numbers
        "INSERT INTO Z_11ZONES_ VALUES (2,1),(3,1)",
        "CREATE TABLE Z_9USERS_ (Z_9PAIRED INTEGER, Z_11OTHER INTEGER)",     # a decoy two-column join that must not be taken
        "CREATE TABLE ZMKFACCESSORY (Z_PK INTEGER PRIMARY KEY, Z_ENT INTEGER, ZCONFIGUREDNAME VARCHAR, ZPROVIDEDNAME VARCHAR, "
        "ZMANUFACTURER VARCHAR, ZMODEL VARCHAR, ZSERIALNUMBER VARCHAR, ZFIRMWAREVERSION VARCHAR, ZACCESSORYCATEGORY INTEGER, "
        "ZROOM INTEGER, ZHOME INTEGER, ZHOSTACCESSORY INTEGER, ZPASSWORD VARCHAR, ZPUBLICKEY BLOB, ZWIFIUNIQUEPRESHAREDKEY VARCHAR, "
        "ZPAIRINGIDENTITY BLOB)",
        (acc, (1, 20, "Test Lamp", "Lamp", "Acme Fixture", "L-1", "SN-TEST-0001", "1.2.3", 5, 2, 1, None) + secret),
        (acc, (2, 20, None, "Hub Bridge", "Acme Fixture", "B-1", "SN-TEST-0002", None, 2, 1, 1, None) + secret),
        (acc, (3, 20, None, "Bridged Sensor", "Acme Fixture", "S-1", "SN-TEST-0003", "0.9", 10, 3, 1, 2) + secret),
        (acc, (4, 21, "Sample TV", None, "Example Corp", "TV-9", "SN-TEST-0004", None, 31, 5, 2, None) + secret),
        "CREATE TABLE ZMKFSERVICE (Z_PK INTEGER PRIMARY KEY, ZACCESSORY INTEGER, ZNAME VARCHAR, ZPROVIDEDNAME VARCHAR, ZSERVICETYPE BLOB)",
        (svc, (1, 1, None, None, uid(0x3E))), (svc, (2, 1, "Lamp", "Lamp", uid(0x43))),
        (svc, (3, 3, "Temp", None, uid(0x8A))), (svc, (4, 3, None, "Vendor thing", custom)),
        (svc, (5, 4, "Sample TV", None, uid(0xD8))), (svc, (6, 4, "HDMI 1", None, uid(0xD9))),
        (svc, (7, 4, "HDMI 2", None, uid(0xD9))), (svc, (8, 4, None, None, uid(0x777))),
        "CREATE TABLE ZMKFACTIONSET (Z_PK INTEGER PRIMARY KEY, ZNAME VARCHAR, ZTYPE VARCHAR, ZHOME INTEGER, ZLASTEXECUTIONDATE TIMESTAMP)",
        ("INSERT INTO ZMKFACTIONSET VALUES (1,'Wake Up','HMActionSetTypeWakeUp',1,?)", (ts,)),
        "INSERT INTO ZMKFACTIONSET VALUES (2,'Movie Night','HMActionSetTypeUserDefined',1,NULL)",
        "INSERT INTO ZMKFACTIONSET VALUES (3,'Hidden Auto Scene','HMActionSetTypeTriggerOwned',1,NULL)",
        "INSERT INTO ZMKFACTIONSET VALUES (4,'Leave','HMActionSetTypeHomeDeparture',2,NULL)",
        "CREATE TABLE ZMKFTRIGGER (Z_PK INTEGER PRIMARY KEY, Z_ENT INTEGER, ZNAME VARCHAR, ZACTIVE INTEGER, ZHOME INTEGER, "
        "ZFIREDATE TIMESTAMP, ZMOSTRECENTFIREDATE TIMESTAMP)",
        ("INSERT INTO ZMKFTRIGGER VALUES (1,30,'Porch at dusk',1,1,NULL,?)", (ts,)),
        ("INSERT INTO ZMKFTRIGGER VALUES (2,31,'Nightly',0,1,?,NULL)", (ts,)),
        "CREATE TABLE Z_7TRIGGERS_ (Z_7ACTIONSETS_ INTEGER, Z_8TRIGGERS_ INTEGER)",
        "INSERT INTO Z_7TRIGGERS_ VALUES (3,1),(2,2)",
        # a credential-shaped column on a table the tool does read, and a table it never reads
        "CREATE TABLE ZMKFCHARACTERISTIC (Z_PK INTEGER PRIMARY KEY, ZAUTHORIZATIONDATA BLOB)",
        "INSERT INTO ZMKFCHARACTERISTIC VALUES (1, x'53454e54494e454c2d41555448')",
    ])


class Home(TmpCase):
    def setUp(self):
        super().setUp()
        self.db = self.path("core.sqlite")
        make_home(self.db)

    def rows(self, mode, **kw):
        return cc.search_home(self.db, mode, **kw)

    def test_homes_counts_and_shared_flag(self):
        by = {r["name"]: r for r in self.rows("homes")}
        h, c = by["Test House"], by["Sample Cabin"]
        self.assertTrue(h["owned"])
        self.assertFalse(c["owned"])
        self.assertEqual((h["rooms"], h["zones"], h["accessories"], h["scenes"], h["automations"]), (4, 2, 3, 2, 2))
        self.assertEqual((c["rooms"], c["zones"], c["accessories"], c["scenes"], c["automations"]), (1, 0, 1, 1, 0))
        self.assertEqual([r["name"] for r in self.rows("homes", home="cabin")], ["Sample Cabin"])

    def test_rooms_default_room_zones_and_accessory_counts(self):
        by = {(r["home"], r["name"]): r for r in self.rows("rooms")}
        self.assertEqual(len(by), 5)
        self.assertEqual(by[("Test House", "Default Room")]["accessories"], 1)   # blank name on the home's default room
        self.assertEqual(by[("Sample Cabin", "Default Room")]["accessories"], 1)  # '' is blank too
        self.assertEqual(by[("Test House", "Hall")]["zones"], ["Downstairs"])
        self.assertEqual(by[("Test House", "Whare Wānanga")]["zones"], [])
        self.assertEqual([r["name"] for r in self.rows("rooms", room="whare wananga")], ["Whare Wānanga"])  # accent-folded

    def test_zones_list_member_rooms(self):
        by = {r["name"]: r for r in self.rows("zones")}
        self.assertEqual(by["Downstairs"]["rooms"], ["Hall", "Lounge"])
        self.assertEqual(by["Empty Zone"]["rooms"], [])
        self.assertEqual([r["name"] for r in self.rows("zones", room="lounge")], ["Downstairs"])

    def test_accessories_fields_names_bridge_and_services(self):
        by = {r["name"]: r for r in self.rows("accessories")}
        self.assertEqual(set(by), {"Test Lamp", "Hub Bridge", "Bridged Sensor", "Sample TV"})   # configured name beats provided
        lamp = by["Test Lamp"]
        self.assertEqual((lamp["manufacturer"], lamp["model"], lamp["serial"], lamp["firmware"]),
                         ("Acme Fixture", "L-1", "SN-TEST-0001", "1.2.3"))
        self.assertEqual((lamp["kind"], lamp["category"], lamp["category_name"], lamp["room"], lamp["home"]),
                         ("HAP", 5, "Lightbulb", "Hall", "Test House"))
        self.assertEqual([s["type"] for s in lamp["services"]], ["AccessoryInformation", "Lightbulb"])
        self.assertEqual(by["Hub Bridge"]["room"], "Default Room")
        self.assertIsNone(by["Hub Bridge"]["firmware"])
        self.assertIsNone(by["Hub Bridge"]["bridged_by"])
        self.assertEqual(by["Bridged Sensor"]["bridged_by"], "Hub Bridge")
        self.assertEqual([s["type"] for s in by["Bridged Sensor"]["services"]], ["TemperatureSensor", "custom"])
        tv = by["Sample TV"]
        self.assertEqual((tv["kind"], tv["category_name"], tv["home"]), ("AppleMedia", "Television", "Sample Cabin"))
        self.assertEqual([s["type"] for s in tv["services"]], ["Television", "InputSource", "InputSource", "0x777"])

    def test_accessory_filters(self):
        names = lambda **kw: sorted(r["name"] for r in self.rows("accessories", **kw))
        self.assertEqual(names(room="hall"), ["Test Lamp"])
        self.assertEqual(names(home="cabin"), ["Sample TV"])
        self.assertEqual(names(text="sn-test-0003"), ["Bridged Sensor"])    # serial
        self.assertEqual(names(text="example corp"), ["Sample TV"])         # manufacturer
        self.assertEqual(names(text="lounge"), ["Bridged Sensor"])          # room
        self.assertEqual(names(text="nothing here"), [])
        self.assertEqual(len(self.rows("accessories", limit=2)), 2)

    def test_scenes_hide_the_automations_own_scene(self):
        by = {r["name"]: r for r in self.rows("scenes")}
        self.assertEqual(set(by), {"Wake Up", "Movie Night", "Leave"})
        self.assertEqual(by["Wake Up"]["type"], "WakeUp")
        self.assertEqual(by["Wake Up"]["last_run"][:4], "2026")
        self.assertIsNone(by["Movie Night"]["last_run"])
        self.assertEqual(by["Movie Night"]["automations"], ["Nightly"])
        self.assertEqual([r["name"] for r in self.rows("scenes", home="cabin")], ["Leave"])

    def test_automations_kind_state_and_scenes(self):
        by = {r["name"]: r for r in self.rows("automations")}
        self.assertEqual((by["Porch at dusk"]["kind"], by["Porch at dusk"]["active"]), ("Event", True))
        self.assertEqual(by["Porch at dusk"]["scenes"], ["Hidden Auto Scene"])
        self.assertEqual((by["Nightly"]["kind"], by["Nightly"]["active"]), ("Timer", False))
        self.assertIsNone(by["Nightly"]["last_fired"])
        self.assertEqual(by["Nightly"]["next_fire"][:4], "2026")
        self.assertEqual(by["Nightly"]["scenes"], ["Movie Night"])

    def test_credential_shaped_columns_never_reach_any_output(self):
        blob = ""
        for mode in cc.HOME_MODES:
            rows = self.rows(mode)
            blob += json.dumps(rows, ensure_ascii=False) + cc.render_text("home", rows)
        for secret in HM_SECRETS:
            self.assertNotIn(secret, blob)
        self.assertIn("SN-TEST-0001", blob)    # the allowlisted serial does appear

    def test_no_query_selects_a_wildcard_or_a_credential_column(self):
        import inspect
        src = inspect.getsource(cc.search_home) + inspect.getsource(cc._home_names) + inspect.getsource(cc._room_names)
        self.assertNotIn("SELECT *", src)
        for col in ("ZPASSWORD", "ZPUBLICKEY", "ZWIFIUNIQUEPRESHAREDKEY", "ZPAIRINGIDENTITY", "ZBROADCASTKEY", "ZMATCRED",
                    "ZOWNERPUBLICKEY", "ZNFCREADERKEY", "ZTHREADOPERATIONALDATASET", "ZPRIMARYWIFISSID", "ZAUTHORIZATIONDATA"):
            self.assertNotIn(col, src)

    def test_read_only_the_store_is_unchanged(self):
        with open(self.db, "rb") as fh:
            before = fh.read()
        for mode in cc.HOME_MODES:
            self.rows(mode)
        with open(self.db, "rb") as fh:
            self.assertEqual(fh.read(), before)
        self.assertEqual(sorted(os.listdir(self.dir)), ["core.sqlite"])    # no -wal/-shm or copy appeared

    def test_unknown_mode_is_a_usage_error(self):
        with self.assertRaises(cc.UsageError):
            self.rows("lights")

    def test_a_store_without_the_join_tables_still_lists_rooms(self):
        con = sqlite3.connect(self.db)
        con.execute("DROP TABLE Z_11ZONES_")
        con.commit(); con.close()
        self.assertTrue(all(r["zones"] == [] for r in self.rows("rooms")))

    def test_status_counts_only(self):
        e = [x for x in cc.status({"home": [self.db]}) if x["app"] == "home"][0]
        self.assertTrue(e["opens_read_only"])
        self.assertEqual(e["counts"], {"homes": 2, "rooms": 5, "zones": 2, "accessories": 4, "services": 8, "scenes": 3, "automations": 2})
        blob = json.dumps(e) + cc.render_status([e])
        for leak in ("Test House", "Hall", "SN-TEST", "Acme"):
            self.assertNotIn(leak, blob)


class Status(TmpCase):
    def test_counts_only_no_content(self):
        c, m, cal, r, n = (self.path(x) for x in ("c", "m", "cal", "r", "n"))
        make_contacts(c); make_messages(m); make_calendar(cal); make_reminders(r); make_notes(n)
        ph = make_photos(self.dir)
        hm = self.path("core.sqlite")
        make_home(hm)
        report = cc.status({"contacts": [c], "messages": [m], "calendar": [cal], "reminders": [r], "notes": [n], "photos": [ph],
                            "home": [hm]})
        self.assertTrue(all(e["opens_read_only"] for e in report))
        counts = {e["app"]: e["counts"] for e in report}
        self.assertEqual(counts["contacts"], {"contacts": 3, "phone_numbers": 2, "emails": 2})
        self.assertEqual(counts["messages"], {"messages": 6, "chats": 3, "handles": 3})
        self.assertEqual(counts["calendar"], {"calendars": 2, "events": 3})
        self.assertEqual(counts["reminders"], {"reminders": 3, "open": 2, "lists": 2})
        self.assertEqual(counts["notes"], {"notes": 5, "recently_deleted": 1, "locked": 1, "folders": 2})
        self.assertEqual(counts["home"]["accessories"], 4)
        blob = json.dumps(report) + cc.render_status(report)
        for secret in ("Alex", "Example", "museum", "milk", "7946", "Packing", "batteries", "Māori", "Locked thing", "Test House", "SN-TEST"):
            self.assertNotIn(secret, blob)

    def test_missing_and_unreadable_stores_are_reported_not_raised(self):
        junk = self.path("junk.sqlite")
        with open(junk, "wb") as fh:
            fh.write(b"this is not a database at all, just text" * 10)
        report = cc.status({"contacts": [self.path("nope.abcddb")], "messages": [junk], "photos": [self.path("nope.sqlite")]})
        by = {e["app"]: e for e in report}
        self.assertFalse(by["contacts"]["opens_read_only"])
        self.assertFalse(by["messages"]["opens_read_only"])
        self.assertIn("error", by["messages"])


class Cli(TmpCase):
    def run_cli(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stderr(err):
            rc = cc.main(list(argv), out=out)
        return rc, out.getvalue(), err.getvalue()

    def test_no_filter_exits_2_for_every_search(self):
        for app, db in (("contacts", "c"), ("messages", "m"), ("calendar", "cal"), ("reminders", "r"), ("notes", "n")):
            p = self.path(db)
            {"c": make_contacts, "m": make_messages, "cal": make_calendar, "r": make_reminders, "n": make_notes}[db](p)
            rc, out, err = self.run_cli(app, "--db", p)
            self.assertEqual(rc, 2, app)
            self.assertEqual(out, "")
            self.assertIn("at least one", err)

    def test_contacts_text_and_json(self):
        p = self.path("c")
        make_contacts(p)
        rc, out, _ = self.run_cli("contacts", "--db", p, "--name", "alex")
        self.assertEqual(rc, 0)
        self.assertIn("Alex Example", out)
        self.assertIn("[Mobile]", out)
        rc, out, _ = self.run_cli("contacts", "--db", p, "--name", "alex", "--json")
        self.assertEqual(json.loads(out)[0]["name"], "Alex Example")

    def test_messages_cli_with_contacts_override(self):
        m, c = self.path("m"), self.path("c")
        make_messages(m); make_contacts(c)
        rc, out, _ = self.run_cli("messages", "--db", m, "--contacts-db", c, "--person", "alex", "--text", "museum")
        self.assertEqual(rc, 0)
        self.assertIn("Alex Example", out)
        self.assertIn("meet at the museum", out)

    def test_notes_cli_snippet_json_and_full(self):
        n = self.path("n")
        make_notes(n)
        rc, out, err = self.run_cli("notes", "--db", n, "--text", "batteries")
        self.assertEqual(rc, 0)
        self.assertIn("1 locked note(s) cannot be searched", err)
        self.assertIn("Packing checklist", out)
        self.assertIn("(Work)", out)
        self.assertIn("spare batteries", out)
        self.assertNotIn("NEEDLE-ONE", out)  # a snippet, not the note
        rc, out, _ = self.run_cli("notes", "--db", n, "--since", "2026-06-01", "--until", "2026-06-02", "--json")
        rows = json.loads(out)
        self.assertEqual([r["title"] for r in rows], ["Locked thing", "Kōrero notes"])
        self.assertTrue(rows[0]["locked"])
        rc, out, _ = self.run_cli("notes", "--db", n, "--text", "batteries", "--full")
        self.assertEqual(rc, 0)
        self.assertIn("NEEDLE-ONE", out)
        rc, out, _ = self.run_cli("notes", "--db", n, "--since", "2000-01-01")
        self.assertIn("[locked]", out)
        self.assertIn("[body not decoded]", out)
        self.assertNotIn("[deleted]", out)
        rc, out, _ = self.run_cli("notes", "--db", n, "--title", "binned", "--include-deleted")
        self.assertIn("[deleted]", out)

    def test_notes_full_with_many_matches_exits_2(self):
        n = self.path("n")
        make_notes(n)
        rc, out, err = self.run_cli("notes", "--db", n, "--since", "2000-01-01", "--full")
        self.assertEqual((rc, out), (2, ""))
        self.assertIn("matched", err)

    def test_bad_date_and_bad_limit_exit_2(self):
        cal = self.path("cal")
        make_calendar(cal)
        self.assertEqual(self.run_cli("calendar", "--db", cal, "--since", "yesterday")[0], 2)
        self.assertEqual(self.run_cli("calendar", "--db", cal, "--text", "x", "--limit", "0")[0], 2)

    def test_unreadable_store_exits_1(self):
        junk = self.path("junk")
        with open(junk, "wb") as fh:
            fh.write(b"not sqlite" * 50)
        rc, _, err = self.run_cli("calendar", "--db", junk, "--text", "x")
        self.assertEqual(rc, 1)
        self.assertIn("cannot read store", err)

    def test_no_matches_message(self):
        r = self.path("r")
        make_reminders(r)
        rc, out, _ = self.run_cli("reminders", "--db", r, "--text", "zzz")
        self.assertEqual((rc, out.strip()), (0, "(no matches)"))

    def test_text_output_for_calendar_and_reminders(self):
        cal, r = self.path("cal"), self.path("r")
        make_calendar(cal); make_reminders(r)
        rc, out, _ = self.run_cli("calendar", "--db", cal, "--since", "2026-05-09", "--until", "2026-05-19", "--text", "review")
        self.assertIn("Review meeting", out)
        self.assertIn("@ Test Venue", out)
        rc, out, _ = self.run_cli("reminders", "--db", r, "--open-only")
        self.assertIn("[ ] Book the dentist  (Errands)  !", out)

    def test_photos_cli_text_json_and_negative_near(self):
        db = make_photos(self.dir)
        rc, out, _ = self.run_cli("photos", "--db", db, "--text", "serial")
        self.assertEqual(rc, 0)
        self.assertIn("IMG_0001.HEIC  " + PH_A1, out)
        self.assertIn("original: on disk", out)
        self.assertIn("gps:      -10.0, 20.0", out)
        rc, out, _ = self.run_cli("photos", "--db", db, "--uuid", PH_B2)
        self.assertIn("original: not on disk", out)
        self.assertIn("[derivative]", out)
        rc, out, _ = self.run_cli("photos", "--db", db, "--uuid", PH_D4)
        self.assertIn("(no file on disk)", out)
        rc, out, _ = self.run_cli("photos", "--db", db, "--near", "-10.0,20.0,1", "--json")   # a leading minus must not be read as a flag
        rows = json.loads(out)
        self.assertEqual([r["uuid"] for r in rows], [PH_A1])
        self.assertEqual(rows[0]["distance_km"], 0.0)
        rc, out, _ = self.run_cli("photos", "--db", db, "--text", "zzz")
        self.assertEqual(out.strip(), "(no matches)")

    def test_photos_cli_errors(self):
        db = make_photos(self.dir)
        rc, out, err = self.run_cli("photos", "--db", db)
        self.assertEqual((rc, out), (2, ""))
        self.assertIn("at least one", err)
        rc, _, err = self.run_cli("photos", "--db", db, "--near", "nowhere")
        self.assertEqual(rc, 2)
        os.remove(os.path.join(os.path.dirname(db), "search", "psi.sqlite"))
        rc, _, err = self.run_cli("photos", "--db", db, "--text", "serial")
        self.assertEqual(rc, 1)
        self.assertIn("cannot read store", err)

    def test_home_cli_needs_exactly_one_mode(self):
        db = self.path("core.sqlite")
        make_home(db)
        rc, out, err = self.run_cli("home", "--db", db)
        self.assertEqual((rc, out), (2, ""))
        self.assertIn("at least one", err)
        rc, out, err = self.run_cli("home", "--db", db, "--rooms", "--zones")
        self.assertEqual((rc, out), (2, ""))
        self.assertIn("exactly one", err)

    def test_home_cli_text_and_json(self):
        db = self.path("core.sqlite")
        make_home(db)
        rc, out, _ = self.run_cli("home", "--db", db, "--homes")
        self.assertIn("Test House  rooms=4 zones=2 accessories=3 scenes=2 automations=2", out)
        self.assertIn("Sample Cabin [shared]", out)
        rc, out, _ = self.run_cli("home", "--db", db, "--accessories", "--room", "hall")
        self.assertIn("Test Lamp  (Hall)  Acme Fixture L-1  Lightbulb", out)
        self.assertIn("serial: SN-TEST-0001", out)
        self.assertIn("services: AccessoryInformation, Lightbulb", out)
        rc, out, _ = self.run_cli("home", "--db", db, "--accessories", "--home", "cabin")
        self.assertIn("InputSource x2", out)
        rc, out, _ = self.run_cli("home", "--db", db, "--accessories", "--text", "sensor", "--json")
        rows = json.loads(out)
        self.assertEqual([r["name"] for r in rows], ["Bridged Sensor"])
        self.assertEqual(rows[0]["bridged_by"], "Hub Bridge")
        rc, out, _ = self.run_cli("home", "--db", db, "--rooms", "--room", "hall")
        self.assertIn("Hall  (Test House)  accessories=1  zones: Downstairs", out)
        rc, out, _ = self.run_cli("home", "--db", db, "--zones")
        self.assertIn("Downstairs  (Test House)  rooms: Hall, Lounge", out)
        rc, out, _ = self.run_cli("home", "--db", db, "--scenes")
        self.assertIn("Movie Night  [UserDefined]  (Test House)  automations: Nightly", out)
        self.assertNotIn("Hidden Auto Scene", out)
        rc, out, _ = self.run_cli("home", "--db", db, "--automations")
        self.assertIn("Porch at dusk  [Event, on]", out)
        self.assertIn("Nightly  [Timer, off]", out)
        rc, out, _ = self.run_cli("home", "--db", db, "--rooms", "--text", "zzz")
        self.assertEqual(out.strip(), "(no matches)")
        rc, out, _ = self.run_cli("home", "--db", db, "--scenes", "--limit", "1", "--json")
        self.assertEqual(len(json.loads(out)), 1)

    def test_home_cli_warns_about_an_unread_write_ahead_log(self):
        db = self.path("core.sqlite")
        make_home(db)
        rc, _, err = self.run_cli("home", "--db", db, "--homes")
        self.assertEqual((rc, err), (0, ""))
        with open(db + "-wal", "wb") as fh:
            fh.write(b"x" * 4096)
        rc, out, err = self.run_cli("home", "--db", db, "--homes")
        self.assertEqual(rc, 0)
        self.assertIn("write-ahead log", err)
        self.assertIn("4 KB", err)
        self.assertNotIn("write-ahead", out)    # stdout stays clean for --json callers

    def test_home_cli_unreadable_store_exits_1(self):
        junk = self.path("junk")
        with open(junk, "wb") as fh:
            fh.write(b"not sqlite" * 50)
        rc, _, err = self.run_cli("home", "--db", junk, "--homes")
        self.assertEqual(rc, 1)
        self.assertIn("cannot read store", err)

    def test_status_cli_runs_against_defaults_without_crashing(self):
        # Hermetic: point the default globs at an empty dir so no real store is touched.
        saved = dict(cc.DEFAULT_PATTERNS)
        cc.DEFAULT_PATTERNS.update({k: [os.path.join(self.dir, "none-*")] for k in saved})
        try:
            rc, out, _ = self.run_cli("status")
        finally:
            cc.DEFAULT_PATTERNS.update(saved)
        self.assertEqual(rc, 1)
        self.assertIn("CANNOT OPEN", out)


class ReadOnlyPragma(TmpCase):
    def test_open_ro_sets_query_only(self):
        p = self.path("c.sqlite")
        make_contacts(p)
        con = cc.open_ro(p)
        try:
            self.assertEqual(con.execute("PRAGMA query_only").fetchone()[0], 1)
        finally:
            con.close()


class AsAProcess(TmpCase):
    """Run the script itself, with HOME pointed at an empty temp dir so that no
    real store on the machine running the tests can be found, let alone read."""

    def run_script(self, *argv):
        env = dict(os.environ, HOME=self.dir)
        done = subprocess.run([sys.executable, SCRIPT, *argv], capture_output=True, text=True, env=env, timeout=60)
        return done.returncode, done.stdout, done.stderr

    def test_it_is_executable_with_a_python_shebang(self):
        self.assertTrue(os.access(SCRIPT, os.X_OK))
        with open(SCRIPT, "rb") as fh:
            self.assertEqual(fh.readline().strip(), b"#!/usr/bin/env python3")

    def test_status_with_no_stores_reports_each_missing_and_exits_1(self):
        rc, out, _ = self.run_script("status")
        self.assertEqual(rc, 1)
        self.assertEqual(out.count("CANNOT OPEN (store not found)"), 7)

    def test_search_with_no_filter_exits_2_and_prints_nothing(self):
        db = self.path("Data-A.sqlite")
        make_reminders(db)
        rc, out, err = self.run_script("reminders", "--db", db)
        self.assertEqual((rc, out), (2, ""))
        self.assertIn("ccapple: reminders needs at least one of", err)

    def test_no_filter_is_exit_2_naming_the_filter_even_with_no_store(self):
        """The filter is checked before any store is looked for: under an empty
        HOME, every search subcommand given no filter exits 2 and says which
        filter is missing, never that a store is."""
        wanted = {
            "contacts": "--name, --phone, --email, --org",
            "messages": "--person, --since, --until, --text",
            "calendar": "--since, --until, --calendar, --text",
            "reminders": "--list, --text, --open-only",
            "notes": "--title, --text, --folder, --since, --until, --id",
            "photos": "--text, --since, --until, --near, --album, --uuid",
            "home": "exactly one of --homes, --rooms, --zones, --accessories, --scenes, --automations",
        }
        for cmd, flags in wanted.items():
            with self.subTest(cmd=cmd):
                rc, out, err = self.run_script(cmd)
                self.assertEqual((rc, out), (2, ""))
                self.assertIn("ccapple: %s needs " % cmd, err)
                self.assertIn(flags, err)
                self.assertNotIn("store", err)
                self.assertNotIn("Traceback", err)

    def test_a_filter_with_no_store_is_still_exit_1(self):
        for cmd, flag in (("messages", "--text"), ("notes", "--text"), ("photos", "--text"), ("home", "--rooms")):
            with self.subTest(cmd=cmd):
                rc, out, err = self.run_script(cmd, flag, *(["x"] if cmd != "home" else []))
                self.assertEqual((rc, out), (1, ""))
                self.assertIn("cannot read store", err)

    def test_missing_store_is_exit_1_not_a_traceback(self):
        rc, out, err = self.run_script("calendar", "--text", "x")
        self.assertEqual((rc, out), (1, ""))
        self.assertIn("ccapple: cannot read store", err)
        self.assertNotIn("Traceback", err)


class HelpAndManual(unittest.TestCase):
    """REPO-STANDARD: `--help` is the digest, the man page the superset. Every
    flag any `--help` prints must appear in the page."""

    SUBCOMMANDS = ("status", "contacts", "messages", "calendar", "reminders", "notes", "photos", "home")

    def help_text(self, *argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            with self.assertRaises(SystemExit) as cm:
                cc.build_parser().parse_args(list(argv) + ["--help"])
        self.assertEqual(cm.exception.code, 0)
        return out.getvalue()

    def test_top_level_help_points_at_the_manual_and_lists_every_subcommand(self):
        text = self.help_text()
        self.assertIn("man ccapple", text)
        for sub in self.SUBCOMMANDS:
            self.assertIn(sub, text)

    def test_the_man_page_exists_and_covers_every_flag_help_prints(self):
        with open(MANPAGE, encoding="utf-8") as fh:
            page = fh.read().replace("\\-", "-")  # roff writes a literal hyphen as \-
        flags = set()
        for sub in self.SUBCOMMANDS:
            flags.update(re.findall(r"--[a-z][a-z-]*", self.help_text(sub)))
        self.assertIn("--include-deleted", flags)  # the harvest worked
        missing = sorted(f for f in flags if f not in page)
        self.assertEqual(missing, [], "flags in --help but absent from man/ccapple.1")

    def test_the_man_page_has_a_section_for_every_subcommand(self):
        with open(MANPAGE, encoding="utf-8") as fh:
            page = fh.read()
        for sub in self.SUBCOMMANDS:
            self.assertIn("\n.SS " + sub + "\n", page, sub)


if __name__ == "__main__":
    unittest.main()
