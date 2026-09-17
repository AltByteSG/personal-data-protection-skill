#!/usr/bin/env python3
"""Tests for scripts/release_notes.py.

Runnable with pytest or directly: `python3 tests/test_release_notes.py`.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load():
    spec = importlib.util.spec_from_file_location(
        "release_notes", ROOT / "scripts" / "release_notes.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


rn = _load()

CHANGELOG = """# Changelog

## Unreleased

- No unreleased changes.

## [1.2.3] — 2026-01-01

Intro line.

### Fixed

- A thing in [`some/file.md`](some/file.md).
- A link that is already [absolute](https://example.com/x).

## [1.2.2] — 2025-12-01

- Older.
"""


def _expect_exit(fn, needle):
    try:
        fn()
    except SystemExit as exc:
        assert str(exc) == "1", exc
        return
    raise AssertionError(f"expected SystemExit for {needle}")


def test_extracts_only_the_requested_section():
    notes = rn.extract_notes(CHANGELOG, "1.2.3")
    assert "Intro line." in notes
    assert "Older." not in notes
    assert "No unreleased changes." not in notes


def test_headings_promoted_one_level():
    # Release pages render outside the repo, where ### sits too deep.
    assert "\n## Fixed" in rn.extract_notes(CHANGELOG, "1.2.3")


def test_relative_links_are_pinned_to_the_tag():
    notes = rn.extract_notes(CHANGELOG, "1.2.3")
    assert f"https://github.com/{rn.REPO}/blob/v1.2.3/some/file.md" in notes


def test_absolute_links_are_left_alone():
    assert "(https://example.com/x)" in rn.extract_notes(CHANGELOG, "1.2.3")


def test_missing_section_fails():
    _expect_exit(lambda: rn.extract_notes(CHANGELOG, "9.9.9"), "missing section")


def test_manifest_mismatch_fails():
    # The repo manifests carry the real version; a different one must not release.
    _expect_exit(lambda: rn.check_manifests(ROOT, "0.0.1"), "manifest mismatch")


def test_manifests_agree_with_changelog_for_current_version():
    import json
    version = json.loads(
        (ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
    rn.check_manifests(ROOT, version)          # must not raise
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert rn.extract_notes(changelog, version).strip()


if __name__ == "__main__":
    passed = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            passed += 1
            print(f"  PASS {name}")
    print(f"\n{passed} passed")
