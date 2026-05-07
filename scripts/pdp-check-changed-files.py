#!/usr/bin/env python3
"""Flag changed files that probably need a PDP compliance review.

This is a deterministic tripwire, not legal advice and not a compliance
decision engine. It detects likely personal-data-protection touchpoints and
points the developer back to the personal-data-protection skill.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


DEFAULT_CONFIG = ".pdp-compliance.json"
VALID_POLICIES = {"warn", "block-on-sensitive-change"}

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
            r"\b(consent|withdraw|privacy|personal data|pii|email|phone|address|"
            r"birth(date)?|dob|passport|nric|national[_-]?id|biometric|face[_-]?"
            r"embedding|fingerprint|location|latitude|longitude|retention|delete[_-]?"
            r"account|export[_-]?user|data[_-]?export|audit[_-]?log|marketing|"
            r"notification|processor|subprocessor|vendor|breach)\b",
            re.I,
        ),
        "personal-data keyword",
    )
]


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or "git command failed")
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
        return {
            "personalDataProtection": {
                "jurisdictions": [],
                "mode": "strictest-wins",
                "reviewPolicy": "warn",
            }
        }
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


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
        text = read_text(full_path)
        for pattern, reason in CONTENT_RULES:
            if pattern.search(text):
                findings.append(("content-scan", reason))

    seen = set()
    unique = []
    for finding in findings:
        if finding not in seen:
            seen.add(finding)
            unique.append(finding)
    return unique


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
    pdp_config = config.get("personalDataProtection", {})
    jurisdictions = pdp_config.get("jurisdictions", [])
    mode = pdp_config.get("mode", "strictest-wins")
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
    print(f"[pdp-check] Jurisdictions: {jurisdiction_text}; mode: {mode}; policy: {policy}")
    print("[pdp-check] Ask Codex to review these changes with the personal-data-protection skill.")

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
