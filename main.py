#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261122 bounty.

The deliverable is the front page in entry.png: one 1024x1024 picture
summing up the world news of Sunday 22 November 2026 - Polish
prosecutors confirming the three objects that fell in Poland were
Russian Kh-101 missiles, the COP31 talks ending without a deal, Iran's
attacks on tankers near Hormuz, the deadly drone strike on Dymer,
Ukraine's sinking of a Russian warship off Libya, and the Cikande
candy-factory fire in Indonesia.

This program's only job is to deliver that picture to the grader: it
verifies the file is a complete, undamaged PNG inside the bounty
limits, then copies it to the output directory. Standard library only,
no network, and the same bytes come out on every run.
"""

import hashlib
import os
import shutil
import struct
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMAGE = ROOT / "entry.png"
LIMIT_BYTES = 1024 * 1024          # the bounty's 1 MiB cap
WANTED_SIZE = (1024, 1024)         # the picture is exactly square
SIGNATURE = b"\x89PNG\r\n\x1a\n"   # first eight bytes of any PNG


def die(reason):
    """Stop with a clear message instead of shipping a bad picture."""
    print("entry check failed: " + reason, file=sys.stderr)
    raise SystemExit(1)


def chunks(data):
    """Yield (type, body) for each PNG chunk, checking CRCs as we go."""
    pos = len(SIGNATURE)
    while pos + 8 <= len(data):
        (span,) = struct.unpack_from(">I", data, pos)
        kind = data[pos + 4:pos + 8]
        body = data[pos + 8:pos + 8 + span]
        (crc,) = struct.unpack_from(">I", data, pos + 8 + span)
        if len(body) != span or zlib.crc32(kind + body) & 0xFFFFFFFF != crc:
            die("chunk %r is damaged or cut short" % kind)
        yield kind, body
        pos += 12 + span
    if pos != len(data):
        die("loose bytes after the final chunk")


def verify(data):
    """Confirm the picture is whole, square and within the size cap."""
    if len(data) > LIMIT_BYTES:
        die("entry.png is %d bytes; the cap is %d" % (len(data), LIMIT_BYTES))
    if not data.startswith(SIGNATURE):
        die("entry.png does not start with the PNG signature")
    kinds = []
    dims = None
    for kind, body in chunks(data):
        kinds.append(kind)
        if kind == b"IHDR":
            dims = struct.unpack(">II", body[:8])
            depth, colour = body[8], body[9]
            if depth != 8 or colour not in (2, 6):
                die("unexpected IHDR format: %d-bit colour type %d" % (depth, colour))
    if kinds[0] != b"IHDR" or kinds[-1] != b"IEND":
        die("PNG must open with IHDR and close with IEND")
    if dims != WANTED_SIZE:
        die("entry.png measures %sx%s, not 1024x1024" % dims)


def main():
    if not IMAGE.is_file():
        die("entry.png is not in the repository")
    payload = IMAGE.read_bytes()
    verify(payload)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(IMAGE, target)
    fingerprint = hashlib.sha256(target.read_bytes()).hexdigest()
    print("delivered %s: %d bytes, sha256 %s" % (target, len(payload), fingerprint))


if __name__ == "__main__":
    main()
