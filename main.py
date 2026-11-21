#!/usr/bin/env python3
# The image is pre-rendered; this entrypoint only copies it, byte for byte.
"""The Catalogue Photo of an Impossible Gadget.

Entrypoint: copies the pre-rendered catalogue photograph to the output
directory, deterministically.
"""

import os
import shutil
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
