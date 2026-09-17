#!/usr/bin/env python3
"""Flag changed files that probably need a PDP compliance review.

This is a deterministic tripwire, not legal advice and not a compliance
decision engine. It detects likely personal-data-protection touchpoints and
points the developer back to the personal-data-protection skill.

Requires Python 3.9+ (PEP 585 builtin generics in annotations).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

DEFAULT_CONFIG = ".pdp-compliance.json"
VALID_POLICIES = {"warn", "block-on-sensitive-change"}
VALID_JURISDICTIONS = {"sg-pdpa", "th-pdpa", "id-pdp", "my-pdpa", "ph-dpa"}
GIT_TIMEOUT_SECONDS = 30

PATH_RULES = [
    (
        re.compile(r"(^|/)(privacy|terms|tos|legal)(/|\.|$)", re.I),
        "06-disclosure",
        "public-facing privacy, terms, or legal text",
    ),
    (
        re.compile(r"(^|/)(auth|login|signup|register|onboarding)(/|\.|$)", re.I),
        "05-feature-ux",
        "auth, signup, or onboarding surface",
    ),
    (
        re.compile(r"(^|/)(settings|account|profile)(/|\.|$)", re.I),
        "05-feature-ux",
        "settings, account, or profile surface",
    ),
    (
        re.compile(r"(^|/)(admin|internal|support)(/|\.|$)", re.I),
        "04-controls-and-processes",
        "admin, support, or internal tooling",
    ),
    (
        re.compile(r"(^|/)(api|routes|controllers|functions|lambda|handlers)(/|\.|$)", re.I),
        "04-controls-and-processes",
        "server-side handler or route",
    ),
    (
        re.compile(r"(^|/)(migrations|db|schema|models)(/|\.|$)", re.I),
        "03-data-model",
        "data model, schema, or migration",
    ),
]

CONTENT_RULES = [
    (
        re.compile(
            r"\b(consent|withdraw|privacy|personal data|pii|email|phone|"
            # `address` and `notification` alone matched ip_address, address bar,
            # and every push/toast notification in the codebase. Both now need a
            # personal-data qualifier. `email` above already covers email_address.
            r"(home|shipping|billing|mailing|postal|street|delivery|residential)"
            r"[\s_-]?address|address[\s_-]?line[\s_-]?\d*|"
            r"notification[\s_-]?((preference|setting|consent|token)s?|"
            r"opt[\s_-]?(in|out))|push[\s_-]?tokens?|"
            r"birthdate|birthday|birth|dob|passport|nric|national[\s_-]?id|"
            r"biometric|face[\s_-]?embedding|fingerprint|location|latitude|"
            r"longitude|retention|delete[\s_-]?account|export[\s_-]?user|"
            r"data[\s_-]?export|audit[\s_-]?log|marketing|"
            r"processor|subprocessor|vendor|breach)\b",
            re.I,
        ),
        "personal-data keyword",
    )
]

# `_` is a word character and `-` sits flush against one, so `\bemail\b` never
# matches `email_address`, `emailAddress`, or `email-address` — i.e. both of the
# dominant field-naming conventions were silently skipped. Splitting the
# haystack on those boundaries once is cheaper and less error-prone than
# encoding every separator variant into every keyword.
_ACRONYM_BOUNDARY = re.compile(r"([A-Z]+)([A-Z][a-z])")
_CAMEL_BOUNDARY = re.compile(r"([a-z0-9])([A-Z])")
_WORD_SEPARATORS = re.compile(r"[_\-]+")


def split_identifiers(text: str) -> str:
    """Split snake_case, kebab-case, and camelCase so `\\b` matches field names."""
    text = _ACRONYM_BOUNDARY.sub(r"\1 \2", text)
    text = _CAMEL_BOUNDARY.sub(r"\1 \2", text)
    return _WORD_SEPARATORS.sub(" ", text)


def run_git(args: list[str]) -> str:
    command = "git " + " ".join(args)
    try:
        result = subprocess.run(
            ["git", *args],
            check=False,
            capture_output=True,
            text=True,
            timeout=GIT_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        raise SystemExit(
            f"{command} timed out after {GIT_TIMEOUT_SECONDS}s"
        ) from None
    if result.returncode != 0:
        raise SystemExit(
            f"{command} failed: {result.stderr.strip() or 'no stderr output'}"
        )
    return result.stdout


def repo_root() -> Path:
    return Path(run_git(["rev-parse", "--show-toplevel"]).strip())


def changed_files(args: argparse.Namespace) -> list[Path]:
    if args.base or args.head:
        if not (args.base and args.head):
            raise SystemExit("--base and --head must be supplied together")
        output = run_git(["diff", "--name-only", f"{args.base}...{args.head}"])
    elif args.staged:
        output = run_git(["diff", "--cached", "--name-only"])
    else:
        output = run_git(["diff", "--name-only"])

    return [Path(line) for line in output.splitlines() if line.strip()]


def load_config(root: Path, config_path: str) -> dict:
    path = Path(config_path)
    if not path.is_absolute():
        path = root / path
    if not path.exists():
        return {"personalDataProtection": {"jurisdictions": [], "reviewPolicy": "warn"}}
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{path}: invalid JSON ({exc})") from None
    except OSError as exc:
        raise SystemExit(f"{path}: cannot read config ({exc})") from None


def policy_from(args: argparse.Namespace, config: dict) -> str:
    configured = (
        config.get("personalDataProtection", {}).get("reviewPolicy", "warn")
    )
    policy = args.review_policy or configured
    if policy not in VALID_POLICIES:
        raise SystemExit(
            f"Unsupported review policy {policy!r}; expected one of: "
            f"{', '.join(sorted(VALID_POLICIES))}"
        )
    return policy


def jurisdictions_from(config: dict) -> list[str]:
    configured = config.get("personalDataProtection", {}).get("jurisdictions", [])
    if not isinstance(configured, list):
        raise SystemExit("personalDataProtection.jurisdictions must be a list")
    unknown = [code for code in configured if code not in VALID_JURISDICTIONS]
    if unknown:
        raise SystemExit(
            f"Unknown jurisdiction code(s): {', '.join(sorted(unknown))}; "
            f"expected one of: {', '.join(sorted(VALID_JURISDICTIONS))}"
        )
    return configured


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def classify(root: Path, rel_path: Path) -> list[tuple[str, str]]:
    rel = rel_path.as_posix()
    findings: list[tuple[str, str]] = []

    for pattern, layer, reason in PATH_RULES:
        if pattern.search(rel):
            findings.append((layer, reason))

    full_path = root / rel_path
    if full_path.is_file() and full_path.stat().st_size <= 500_000:
        text = split_identifiers(read_text(full_path))
        for pattern, reason in CONTENT_RULES:
            if pattern.search(text):
                findings.append(("content-scan", reason))

    return list(dict.fromkeys(findings))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Flag changed files that probably need PDP compliance review."
    )
    parser.add_argument("--config", default=DEFAULT_CONFIG)
    parser.add_argument("--staged", action="store_true")
    parser.add_argument("--base")
    parser.add_argument("--head")
    parser.add_argument(
        "--review-policy",
        choices=sorted(VALID_POLICIES),
        help="Override .pdp-compliance.json reviewPolicy.",
    )
    args = parser.parse_args()

    root = repo_root()
    config = load_config(root, args.config)
    jurisdictions = jurisdictions_from(config)
    policy = policy_from(args, config)

    sensitive = []
    for rel_path in changed_files(args):
        findings = classify(root, rel_path)
        if findings:
            sensitive.append((rel_path, findings))

    if not sensitive:
        print("[pdp-check] No PDP-sensitive changed files detected.")
        return 0

    jurisdiction_text = ", ".join(jurisdictions) if jurisdictions else "not configured"
    print("[pdp-check] PDP-sensitive changes detected.")
    print(f"[pdp-check] Jurisdictions: {jurisdiction_text}; policy: {policy}")
    print(
        "[pdp-check] Ask your coding agent to review these changes with the "
        "personal-data-protection skill."
    )

    for rel_path, findings in sensitive:
        reasons = "; ".join(f"{layer}: {reason}" for layer, reason in findings)
        print(f"  - {rel_path.as_posix()} ({reasons})")

    if not jurisdictions:
        print("[pdp-check] No .pdp-compliance.json jurisdictions configured yet.")
        print("[pdp-check] Set up jurisdictions before relying on this guardrail.")

    if policy == "block-on-sensitive-change":
        print("[pdp-check] Blocking because reviewPolicy is block-on-sensitive-change.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
