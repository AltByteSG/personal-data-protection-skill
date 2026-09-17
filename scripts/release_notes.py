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
import subprocess
import sys
from pathlib import Path

REPO = "AltByteSG/personal-data-protection-skill"
MANIFESTS = (".claude-plugin/plugin.json", ".codex-plugin/plugin.json")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def fail(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(1)


def read_at_ref(ref: str, rel: str) -> str:
    """Read a file as of a git ref, so an existing tag is checked against its own tree."""
    result = subprocess.run(["git", "show", f"{ref}:{rel}"],
                            capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        fail(f"cannot read {rel} at {ref}: {result.stderr.strip()}")
    return result.stdout


def check_manifests(root: Path, version: str, ref: str | None = None) -> None:
    for rel in MANIFESTS:
        if ref:
            declared = json.loads(read_at_ref(ref, rel)).get("version")
        else:
            path = root / rel
            if not path.exists():
                fail(f"{rel} not found")
            declared = json.loads(path.read_text(encoding="utf-8")).get("version")
        if declared != version:
            where = f"{rel} at {ref}" if ref else rel
            fail(
                f"{where} declares version {declared!r}, but {version!r} is being "
                f"released. The tag must not disagree with what the plugin reports."
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
    parser.add_argument("--manifest-ref", default=None,
                        help="Validate manifests as of this git ref instead of the "
                             "working tree. Use when releasing an existing tag, whose "
                             "manifests differ from the current branch.")
    args = parser.parse_args()

    version = args.version.lstrip("v")
    if not SEMVER.match(version):
        fail(f"{args.version!r} is not a MAJOR.MINOR.PATCH version")

    root = Path(__file__).resolve().parent.parent
    check_manifests(root, version, args.manifest_ref)
    notes = extract_notes((root / "CHANGELOG.md").read_text(encoding="utf-8"), version)

    if args.check_only:
        at = f" (manifests as of {args.manifest_ref})" if args.manifest_ref else ""
        print(f"ok: v{version} is consistent across manifests and CHANGELOG.md{at}")
    else:
        print(notes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
