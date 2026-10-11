#!/usr/bin/env python3
"""Validate all Jupyter notebooks in the repository (JSON + nbformat schema)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    notebooks = sorted(ROOT.glob("**/*.ipynb"))
    failed = False
    for path in notebooks:
        if ".git" in path.parts:
            continue
        try:
            with path.open(encoding="utf-8") as f:
                json.load(f)
            nb = nbformat.read(path, as_version=4)
            nbformat.validate(nb)
            print(f"OK  {path.relative_to(ROOT)}")
        except Exception as exc:  # noqa: BLE001 — report all validation errors
            failed = True
            print(f"FAIL {path.relative_to(ROOT)}: {exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
