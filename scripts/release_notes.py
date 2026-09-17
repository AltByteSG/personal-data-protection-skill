#!/usr/bin/env python3
"""Validate a release and emit its notes from CHANGELOG.md.

Used by .github/workflows/release.yml, and runnable locally to preview what a
release would publish:

    python3 scripts/release_notes.py 0.4.1
    python3 scripts/release_notes.py 0.4.1 --check-only

Validation fails the release rather than publishing something inconsistent:
both plugin manifests must already carry the version being released, and
CHANGELOG.md must have a dated section for it.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = "AltByteSG/personal-data-protection-skill"
MANIFESTS = (".claude-plugin/plugin.json", ".codex-plugin/plugin.json")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def fail(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(1)


def check_manifests(root: Path, version: str) -> None:
    for rel in MANIFESTS:
        path = root / rel
        if not path.exists():
            fail(f"{rel} not found")
        declared = json.loads(path.read_text(encoding="utf-8")).get("version")
        if declared != version:
            fail(
                f"{rel} declares version {declared!r}, but {version!r} is being "
                f"released. Bump the manifests first — the tag must not disagree "
                f"with what the plugin reports."
            )


def extract_notes(changelog: str, version: str) -> str:
    start = re.search(rf"^## \[{re.escape(version)}\] — .+$", changelog, re.M)
    if not start:
        fail(f"CHANGELOG.md has no dated '## [{version}] — <date>' section")
    nxt = re.search(r"^## (\[|Unreleased)", changelog[start.end():], re.M)
    body = changelog[start.end():start.end() + nxt.start()] if nxt else changelog[start.end():]
    body = body.strip()
    if not body:
        fail(f"CHANGELOG.md section for {version} is empty")
    # Release pages are not rendered inside the repo tree: promote headings one
    # level and pin relative links to the tag so they resolve.
    body = re.sub(r"^###", "##", body, flags=re.M)
    body = re.sub(
        r"\]\((?!https?://|#)([^)]+)\)",
        rf"](https://github.com/{REPO}/blob/v{version}/\1)",
        body,
    )
    return body


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="Version being released, without the leading v.")
    parser.add_argument("--check-only", action="store_true",
                        help="Validate without printing the notes.")
    args = parser.parse_args()

    version = args.version.lstrip("v")
    if not SEMVER.match(version):
        fail(f"{args.version!r} is not a MAJOR.MINOR.PATCH version")

    root = Path(__file__).resolve().parent.parent
    check_manifests(root, version)
    notes = extract_notes((root / "CHANGELOG.md").read_text(encoding="utf-8"), version)

    if args.check_only:
        print(f"ok: v{version} is consistent across manifests and CHANGELOG.md")
    else:
        print(notes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
