#!/usr/bin/env python3
"""Sum up Friday 20 November 2026's world news in one image.

The entry image is entry.png beside this file: a newspaper front page
("The World in One Day") drawn by assets/generate.py from the day's
reported news -- GTA VI's record launch day, the Trump-Xi-Putin summit
in Shenzhen, the Houthi strike on Riyadh's PIF Tower, Cyclone Akvan,
and the ICJ's Myanmar ruling, plus a ticker of the day's other stories.

This program only copies that image to the output directory, so grading
needs no fonts and no network, and two runs write identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Self-check: the copy must be byte-identical to the source image,
    # so a truncated or corrupted write fails loudly instead of entering
    # a broken file.
    if sha256(src) != sha256(dst):
        raise SystemExit("entry.png copy failed verification")
    size = os.path.getsize(dst)
    print(f"wrote entry.png: {size} bytes, sha256 {sha256(dst)[:16]}...")
    if size > 1_048_576:
        raise SystemExit("entry.png is over the 1 MiB cap")


if __name__ == "__main__":
    main()
