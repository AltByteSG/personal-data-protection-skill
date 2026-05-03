# AGENTS.md — Personal Data Protection Compliance Skill

> ⚠ **Reference material only — not legal advice.** See [DISCLAIMER.md](DISCLAIMER.md). Verify against the official statute and consult a qualified DPO / lawyer.

This file is the **Codex CLI / Cursor / Copilot-friendly entry point** to the same content surfaced to Claude Code via [`SKILL.md`](SKILL.md). The two files mirror each other; if you edit one, mirror the change to the other.

If you are an agent and the user is working on code that touches personal data — signup, auth, consent, profile fields, notifications, friends, chat, media uploads, location, account deletion, data export, admin tooling, retention/cron, third-party processors, or privacy/T&C documents — follow the steps below.

## Step 1 — Identify the active jurisdiction(s)

**On first use in a project, ask the user which jurisdiction(s) apply.** The answer depends on where the application's *users* are located, not where the company is registered.

> *"Which personal-data-protection regimes does this application need to comply with? Pick all that apply: Singapore (PDPA 2012), Thailand (PDPA B.E. 2562), Indonesia (UU PDP 27/2022). If users span multiple jurisdictions, pick all relevant — the strictest rule will usually win."*

Once the user has chosen, persist that choice somewhere project-specific (a comment in the project's `AGENTS.md`, `CLAUDE.md`, or equivalent project-instruction file) so subsequent sessions don't need to re-ask. Then load only the relevant `jurisdictions/<code>/README.md` files for the rest of the session.

| Code | Jurisdiction | Status |
|---|---|---|
| `sg-pdpa` | Singapore PDPA 2012 (post-2020 Amendments) | ✅ populated |
| `th-pdpa` | Thailand PDPA B.E. 2562 (2019) | ✅ populated |
| `id-pdp` | Indonesia UU PDP No. 27/2022 | ✅ populated |
| `my-pdpa` | Malaysia PDPA 2010 (with 2024 Amendments) | 🚧 planned for v0.2 |
| `ph-dpa` | Philippines Data Privacy Act 2012 (RA 10173) | 🚧 planned for v0.2 |
| `vn-pdpd` | Vietnam PDP Decree 13/2023/ND-CP | 🚧 planned for v0.2 |

Cross-jurisdiction comparison lives in [`jurisdictions/_index.md`](jurisdictions/_index.md).

## Step 2 — Pick the right entry point

**You're starting work on something.** Open the matching checklist:

| Task | Checklist |
|---|---|
| Adding or modifying a feature that touches personal data | [`checklists/new-feature.md`](checklists/new-feature.md) |
| Adding a column / field that holds personal data | [`checklists/new-data-field.md`](checklists/new-data-field.md) |
| Adding a third-party SDK or vendor that will process personal data | [`checklists/new-vendor.md`](checklists/new-vendor.md) |
| Responding to a security incident | [`checklists/breach-response.md`](checklists/breach-response.md) |

**You want depth on a specific layer.** Open the matching layer file:

| Layer | What it covers |
|---|---|
| [01 Non-technical](layers/01-non-technical.md) | DPO, staff acceptable-use, vendor contracts, complaint handling |
| [02 Architecture](layers/02-architecture.md) | Data residency, isolation, encryption, secret handling, defence-in-depth |
| [03 Data model](layers/03-data-model.md) | Consent records, audit records, retention markers, deletion conventions, PII inventory |
| [04 Controls and processes](layers/04-controls-and-processes.md) | Access control, retention sweeps, log hygiene, breach detection signals |
| [05 Feature / UX](layers/05-feature-ux.md) | Signup consent, settings, account deletion, data export, primer dialogs, EXIF strip |
| [06 Disclosure](layers/06-disclosure.md) | Privacy policy, T&C, OS permission strings, contextual notices |
| [07 Operational](layers/07-operational.md) | Incident response, retention sweeps, backups, vendor reviews, monitoring |

Layer files are **universal across all three jurisdictions** — implementation patterns are shared. Jurisdiction-specific obligations live in `jurisdictions/<code>/obligations/`.

## Critical thresholds (load-bearing on every PDP question)

These vary by jurisdiction — only the active one(s) apply.

| | Singapore PDPA | Thailand PDPA | Indonesia UU PDP |
|---|---|---|---|
| Breach notification window to authority | **3 calendar days** after assessing as notifiable (s26D(1)) | **72 hours** from awareness (s37(4)) | **72 hours** from awareness — to **both** subject AND regulator (Pasal 46(1)) |
| Significant-scale / risk threshold | ≥ 500 affected individuals | "Risk to rights and freedoms"; "high risk" triggers individual notification | Always notify subject; "certain circumstances" trigger public notification (Pasal 46(3)) |
| Maximum financial penalty cap | SGD 1M / 10% SG turnover (s48J(3)) | THB 1M / 3M / 5M tiered (s82–84); plus criminal up to 1 year + THB 1M (s79) | **2% of annual revenue per violation** (Pasal 57(3)); plus corporate criminal — fines up to 10× + suspension / **dissolution** (Pasal 70) |
| Individual criminal liability | Yes (s48D/E/F) — SGD 5,000 / 2 years | Yes (s79–81); s81 catches director / manager **omissions**, broader than SG | Yes (Pasal 67–68): up to 6 years + IDR 6B; corporate liability extends to dissolution (Pasal 70(4)) |

## How to use the layer ↔ obligation split

The pattern is **implement once, check against multiple jurisdictions**:

1. Identify what personal data the feature touches.
2. Walk the universal `layers/` to plan the implementation (data model, access controls, UX, disclosure, operational).
3. For each active jurisdiction, walk `jurisdictions/<code>/obligations/` to verify the implementation satisfies the statute-level obligations. Note where multiple jurisdictions disagree — usually the strictest rule controls.
4. Update the project's privacy policy / consent records / runbook as needed.

## Differences from the Claude Code version

The content (`layers/`, `jurisdictions/`, `checklists/`, `templates/`) is identical between agents. The only Claude-specific element is the `templates/pdp-nudge.sh.template` PostToolUse hook — Codex CLI does not have an equivalent hook system at time of writing, so that template is Claude-only. If you are using Codex, manual diligence on PDP-sensitive paths replaces the hook.

## Statute version + verification dates

Each jurisdiction's `README.md` records:
- Which version of the statute the obligation files reflect
- When the content was last verified against official sources
- Pending amendments to watch for

When statutes amend, this skill is updated and tagged. See [CHANGELOG.md](CHANGELOG.md) and pin to a specific tag if you need stability.
