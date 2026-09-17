#!/usr/bin/env python3
"""Tests for scripts/pdp-check-changed-files.py.

Runnable either with pytest or directly: `python3 tests/test_pdp_check.py`.
The script name contains a dash, so it is loaded by path rather than imported.
"""

from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path


def _load():
    path = Path(__file__).resolve().parent.parent / "scripts" / "pdp-check-changed-files.py"
    spec = importlib.util.spec_from_file_location("pdp_check", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pdp = _load()
KEYWORDS = pdp.CONTENT_RULES[0][0]


def _matches(text: str) -> bool:
    return bool(KEYWORDS.search(pdp.split_identifiers(text)))


# --- content scan -----------------------------------------------------------
# Regression: `_` is a word character and `-` sits flush against one, so a bare
# `\bemail\b` matched none of the snake_case / kebab-case / camelCase spellings
# that dominate real schemas. Every case below silently escaped the scanner.

def test_snake_case_field_names_are_detected():
    for name in ("email_address", "phone_number", "passport_number", "user_email",
                 "nric_number", "national_id", "delete_account", "audit_log",
                 "face_embedding", "data_export"):
        assert _matches(name), name


def test_camel_case_field_names_are_detected():
    for name in ("emailAddress", "phoneNumber", "nationalId", "deleteAccount",
                 "auditLog", "dataExport", "personalData"):
        assert _matches(name), name


def test_acronym_boundaries_are_split():
    for name in ("userNRIC", "NRICNumber"):
        assert _matches(name), name


def test_kebab_case_field_names_are_detected():
    assert _matches("shipping-address")


def test_date_of_birth_variants_are_detected():
    for name in ("dob", "birthdate", "birthday", "birth_date", "date_of_birth"):
        assert _matches(name), name


def test_qualified_address_fields_are_detected():
    for name in ("home_address", "shippingAddress", "billing_address", "mailing_address",
                 "postal_address", "street_address", "email_address",
                 "address_line1", "address_line_2"):
        assert _matches(name), name


def test_unqualified_address_does_not_match():
    # Bare `address` matched ip_address, the address bar, and MAC addresses.
    for name in ("ip_address", "address_bar", "memory_address", "macAddress", "addressable"):
        assert not _matches(name), name


def test_personal_data_notification_fields_are_detected():
    for name in ("notification_preferences", "notificationSettings", "notification_consent",
                 "notification_opt_in", "notificationOptOut", "push_token", "push_tokens"):
        assert _matches(name), name


def test_plumbing_notifications_do_not_match():
    # Bare `notification` fired on every push/toast notification in a codebase.
    for name in ("push_notification", "toast_notification", "notification_service",
                 "sendNotification", "notification_queue", "notificationCenter"):
        assert not _matches(name), name


def test_unrelated_identifiers_do_not_match():
    for name in ("birthplace", "rebirth", "widget", "threadsafe",
                 "render_button", "http_client", "processing_time"):
        assert not _matches(name), name


# --- config loading ---------------------------------------------------------

def _write_config(root: Path, payload: str) -> None:
    (root / ".pdp-compliance.json").write_text(payload, encoding="utf-8")


def _expect_exit(fn, needle: str) -> None:
    try:
        fn()
    except SystemExit as exc:
        assert needle in str(exc), f"expected {needle!r} in {exc!r}"
        return
    raise AssertionError(f"expected SystemExit containing {needle!r}")


def test_missing_config_yields_safe_defaults():
    with tempfile.TemporaryDirectory() as tmp:
        config = pdp.load_config(Path(tmp), ".pdp-compliance.json")
        assert config["personalDataProtection"]["jurisdictions"] == []
        assert pdp.jurisdictions_from(config) == []


def test_malformed_config_reports_readable_error():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _write_config(root, "{ not json")
        _expect_exit(lambda: pdp.load_config(root, ".pdp-compliance.json"), "invalid JSON")


def test_unknown_jurisdiction_code_is_rejected():
    config = {"personalDataProtection": {"jurisdictions": ["sg-pdps"]}}
    _expect_exit(lambda: pdp.jurisdictions_from(config), "sg-pdps")


def test_known_jurisdiction_codes_round_trip():
    codes = sorted(pdp.VALID_JURISDICTIONS)
    config = {"personalDataProtection": {"jurisdictions": codes}}
    assert pdp.jurisdictions_from(config) == codes


def test_jurisdictions_must_be_a_list():
    config = {"personalDataProtection": {"jurisdictions": "sg-pdpa"}}
    _expect_exit(lambda: pdp.jurisdictions_from(config), "must be a list")


def test_example_config_is_valid():
    root = Path(__file__).resolve().parent.parent
    config = json.loads((root / ".pdp-compliance.example.json").read_text(encoding="utf-8"))
    assert pdp.jurisdictions_from(config)
    assert config["personalDataProtection"]["reviewPolicy"] in pdp.VALID_POLICIES


# --- policy resolution ------------------------------------------------------

class _Args:
    def __init__(self, review_policy=None):
        self.review_policy = review_policy


def test_policy_defaults_to_warn():
    assert pdp.policy_from(_Args(), {}) == "warn"


def test_cli_flag_overrides_configured_policy():
    config = {"personalDataProtection": {"reviewPolicy": "warn"}}
    got = pdp.policy_from(_Args("block-on-sensitive-change"), config)
    assert got == "block-on-sensitive-change"


def test_unsupported_policy_is_rejected():
    config = {"personalDataProtection": {"reviewPolicy": "explode"}}
    _expect_exit(lambda: pdp.policy_from(_Args(), config), "Unsupported review policy")


# --- classification ---------------------------------------------------------

def test_path_rules_map_to_layers():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        findings = pdp.classify(root, Path("app/migrations/0002_add_column.sql"))
        assert ("03-data-model", "data model, schema, or migration") in findings


def test_findings_are_deduplicated():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        target = root / "api" / "admin"
        target.mkdir(parents=True)
        (target / "handler.py").write_text("email_address = 1\n", encoding="utf-8")
        findings = pdp.classify(root, Path("api/admin/handler.py"))
        assert len(findings) == len(set(findings))


def test_clean_file_produces_no_findings():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "util.py").write_text("def add(a, b):\n    return a + b\n", encoding="utf-8")
        assert pdp.classify(root, Path("util.py")) == []


if __name__ == "__main__":
    passed = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            passed += 1
            print(f"  PASS {name}")
    print(f"\n{passed} passed")
