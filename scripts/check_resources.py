#!/usr/bin/env python3
"""Verify resource integrity and SVG/PNG coverage without dependencies."""

import hashlib
import json
from pathlib import Path
import struct


def check(root):
    manifest = json.loads((root / "manifest.json").read_text())
    entries = manifest["files"]
    paths = {entry["path"] for entry in entries}
    assert len(paths) == len(entries), "Duplicate manifest paths"
    actual = {
        path.relative_to(root).as_posix()
        for directory in ("sources", "archive", "logos")
        for path in (root / directory).rglob("*")
        if path.is_file()
    }
    assert actual == paths, f"Unrecorded or missing resources: {sorted(actual ^ paths)}"
    pngs = 0
    svgs = 0
    for entry in entries:
        path = root / entry["path"]
        data = path.read_bytes()
        assert hashlib.sha256(data).hexdigest() == entry["sha256"], f"Hash mismatch: {path}"
        if path.suffix.lower() == ".svg":
            svgs += 1
            companion = path.with_suffix(".png").relative_to(root).as_posix()
            assert companion in paths, f"Missing PNG companion: {path}"
        if path.suffix.lower() == ".png":
            pngs += 1
            assert data[:8] == b"\x89PNG\r\n\x1a\n", f"Invalid PNG signature: {path}"
            assert data[8:16] == b"\x00\x00\x00\rIHDR", f"Invalid PNG header: {path}"
            width, height = struct.unpack(">II", data[16:24])
            assert width > 0 and height > 0, f"Empty PNG: {path}"
        if entry["kind"] == "generated-png":
            assert entry["svg"] in paths, f"Missing source SVG: {path}"
            assert Path(entry["svg"]).with_suffix(".png").as_posix() == entry["path"]
    print(f"OK: {len(entries)} resources, {svgs} SVGs with PNG companions, {pngs} PNGs")


if __name__ == "__main__":
    check(Path(__file__).resolve().parents[1])
