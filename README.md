# personal-data-protection-skill

> ⚠ **Engineering reference material — not legal advice.** This skill summarises personal-data-protection obligations as they apply to building software. It is **not** authoritative legal guidance and **must not** be used as the sole basis for compliance decisions. Always verify against the official statute and consult a qualified DPO or lawyer. See [DISCLAIMER.md](DISCLAIMER.md).

A Claude Code [skill](https://docs.claude.com/en/docs/claude-code/skills) that helps engineers build and maintain personal-data-protection-compliant applications, organised by where in the stack each obligation lands rather than by statute section number.

**Status:** v0.1.0 — Singapore PDPA, Thailand PDPA, and Indonesia UU PDP all populated.

**Audience:** anyone building any app that handles personal data of users in Singapore, Thailand, or Indonesia. Tech-agnostic — works whether your stack is Supabase, Firebase, AWS, your own backend, native iOS/Android, Flutter, React Native, web, or anything else.

## Why this exists

Personal-data-protection statutes are written by lawyers, for lawyers. Engineers shipping features need answers like *"I'm adding a new column that stores user PII — what do I touch?"*, not section numbers. This skill bridges the two:

- **Layered guidance** by where in the stack the obligation lives (architecture, data model, controls, feature/UX, disclosure, operational) — universal across jurisdictions.
- **Jurisdiction-specific obligations** mapped to the relevant statute sections.
- **Entry-point checklists** for common tasks: new feature, new data field, new vendor, breach response.
- **Statute-map** for reverse lookup when you need to cite a section in a PR description, audit response, or breach notification.

## How the three statutes diverge — developer view

This table is **application code and UX only**. Each row starts with *"If your app does X..."* and the per-jurisdiction columns describe how the implementation actually differs — what UI element to add, what column to create, what flow to build, what template to ship.

Governance/legal items (DPO appointment, staff AUP wording, vendor DPA contracts, regulator notification portals, penalty-cap exposure) are **excluded** — those are real obligations but they don't change what your application does. See `skill/jurisdictions/<code>/obligations/` for those.

Areas where the three regimes are **equivalent** at the app level (consent capture, withdrawal symmetry, per-user data isolation, retention sweeps, EXIF strip, soft-prompt dialogs, backup retention) are also omitted — the same code satisfies all three.

| If your app... | Singapore PDPA | Thailand PDPA | Indonesia UU PDP |
|---|---|---|---|
| **Has a signup consent screen** | Single bundled "I agree to T&C + Privacy" checkbox is acceptable when all processing is transactional | Same screen works, **but** if you collect any sensitive-category data (see below), add a separate explicit-consent modal for those fields specifically | **Stricter form requirements** (Pasal 22): consent must be written/recorded, clearly distinguishable, in simple/clear language. Non-compliant consent is **null and void by law** (Pasal 22(5)) — no fallback |
| **Collects sensitive data** (anything that could fall into health, biometrics, religion, sexuality, ethnicity, political opinion, criminal record, trade union, genetic, location patterns over time) | Apply the narrow deemed-significant-harm list — usually no special UX | Broad s26 — almost certainly need a **separate explicit-consent dialog** before collection, plus stricter logging on those fields | "Specific" Personal Data category (Pasal 4) — requires explicit consent under Pasal 20(2)(a) AND **mandatory DPIA** (Pasal 34) when high-risk |
| **Has a Settings screen with notification toggles** | Single "Notifications on/off" works for transactional-only apps | Same — split into transactional vs marketing the moment marketing is added | Same — but Pasal 40 requires **stop within 72 hours** of consent withdrawal |
| **Lets users delete their account** | Hard-delete + "Deleted User" attribution for shared content (chat history etc.) | Same flow works, **plus** offer "Anonymize" as an alternative choice in the confirmation UI (s33 explicitly covers erase OR anonymize) | Pasal 8 + 43 + 44 — explicit **erasure AND destruction** obligations (the Act distinguishes the two; destruction is more permanent). Subject can request both |
| **Lets users export their data** | Any structured format (JSON, CSV, ZIP) | Same, **but** format must be **suitable for transfer to another controller** — JSON works, ad-hoc proprietary blobs don't (s31) | Pasal 13 — machine-readable format; right to send/transfer to another Controller where systems can communicate securely. Must respond in **72 hours** (Pasal 32) |
| **Lets users pause processing without deleting** their account | No such feature needed | **Build it** (s34) — schema: `processing_restricted_at` column on user record. UI: Settings toggle. Code: check on every mutation; reads still allowed | **Required (Pasal 11)** — same code mechanism as Thailand. PLUS **72-hour SLA** (Pasal 41) — must comply or document statutory exception |
| **Lets admins / support read individual user data** | Audit-log mutations (best practice; not strictly required) | Audit-log mutations + maintain a discoverable s39 record-of-processing-activities document for the regulator | Pasal 31 explicit Records of Processing Activities (RoPA) requirement for **all** processing — formalised inventory, regulator can request |
| **Stores user data with cloud providers in another country** | Privacy policy mention of "service providers" is sufficient if vendor DPAs are in place | If relying on s28(2) consent: signup screen must disclose destination + that protection status is inadequate. If relying on s28(3) contractual necessity: vendor DPAs sufficient (most realistic) | **3-tier hierarchy (Pasal 56)**: adequacy → adequate-and-binding safeguards → consent. No published adequacy list yet from the regulator — most realistic basis is Tier 2 (vendor DPAs with binding clauses) |
| **Has an incident response runbook** | Lane: 3 calendar days from breach-assessment-as-notifiable; PDPC SG portal | Lane: 72 hours from *awareness* (faster); PDPC Thailand portal | **72-hour lane (Pasal 46)** — but distinct: notify **BOTH** subject AND regulator; "certain circumstances" trigger public notification. Operationally heavier than SG/TH |

**How to use this table:** find the row matching what your app already does (or is about to do). Read across — if the per-jurisdiction columns are the same, you ship one implementation. If they differ, you either build the strictest version (covers all) or branch by user jurisdiction (more code, more nuanced UX).

For the section-by-section walkthrough, see [`jurisdictions/`](jurisdictions/) and [`jurisdictions/_index.md`](jurisdictions/_index.md).

## Install

Clone into the directory your agent expects:

```bash
git clone https://github.com/AltByteSG/personal-data-protection-skill.git <destination>
```

| Agent | `<destination>` | Discovery |
|---|---|---|
| Claude Code | `.claude/skills/personal-data-protection` | Auto-registers via [`SKILL.md`](SKILL.md). Verify with `claude /skills`. |
| Codex CLI | `.codex/skills/personal-data-protection` | Reference [`AGENTS.md`](AGENTS.md) from your project's top-level `AGENTS.md` (snippet below). |
| Cursor / Copilot | anywhere in the repo | Reference [`AGENTS.md`](AGENTS.md) from your `.cursorrules` or `.github/copilot-instructions.md` (same snippet). |

For Codex / Cursor / Copilot, add a single line to your existing project-instruction file:

```markdown
For personal-data-protection compliance, follow the guidance in
<destination>/AGENTS.md
```

To pin a specific upstream version after cloning:

```bash
cd <destination> && git checkout v0.1.0
```

## Adapt to your project

Two templates ship in [`templates/`](templates/). Setup instructions are in each file's header.

- **[`INCIDENT_RESPONSE.md.template`](templates/INCIDENT_RESPONSE.md.template)** — *works with any agent.* Solo / small-team breach runbook. Copy to your project's `docs/` folder and fill in the `{{PLACEHOLDERS}}` (DPO contact, vendor list, jurisdictions).
- **[`pdp-nudge.sh.template`](templates/pdp-nudge.sh.template)** — **Claude Code only.** Auto-nudges Claude into this skill on edits to PDP-sensitive paths via a `PostToolUse` hook. Codex CLI, Cursor, and Copilot do not have an equivalent hook system at time of writing, so this template is not portable — manual diligence on PDP-sensitive paths is the substitute on those agents.

## Versioning

Releases are tagged to track significant statute changes — see [CHANGELOG.md](CHANGELOG.md). Each jurisdiction's `README.md` records which version of the statute the content reflects and when it was last verified.

When PDPC (Singapore), MOCI (Indonesia), or PDPC (Thailand) publishes amendments or new guidance, the skill is updated and a new minor or patch version is released. You can pin to a specific tag in your submodule if you want to control the upgrade timing.

## Sources

This skill summarises and references the following statutes. Always defer to the official text — see [DISCLAIMER.md](DISCLAIMER.md).

### Singapore — Personal Data Protection Act 2012

- **Statute:** [sso.agc.gov.sg/Act/PDPA2012](https://sso.agc.gov.sg/Act/PDPA2012)
- **Regulator:** Personal Data Protection Commission — [www.pdpc.gov.sg](https://www.pdpc.gov.sg)
- **Subordinate regulations:**
  - Personal Data Protection (Notification of Data Breaches) Regulations 2021: [sso.agc.gov.sg/SL/PDPA2012-S64-2021](https://sso.agc.gov.sg/SL/PDPA2012-S64-2021)
- **Advisory guidelines:** [pdpc.gov.sg → Guidelines and Consultation](https://www.pdpc.gov.sg/guidelines-and-consultation)
- **Breach reporting portal:** [eservice.pdpc.gov.sg/case/db](https://eservice.pdpc.gov.sg/case/db)

### Indonesia — UU No. 27/2022 (Pelindungan Data Pribadi)

- **Statute (Bahasa Indonesia, official):** [peraturan.go.id](https://peraturan.go.id) — search *"UU 27 2022"*
- **Regulator:** Komdigi (Kementerian Komunikasi dan Digital, formerly Kominfo) — [www.komdigi.go.id](https://www.komdigi.go.id)
- **Note:** an official English translation may not exist. Rely on qualified Indonesian counsel for interpretation.

### Thailand — PDPA B.E. 2562 (2019)

- **Regulator:** Personal Data Protection Committee Thailand — [www.pdpc.or.th](https://www.pdpc.or.th)
- **English translation (PDPC-published):** see [pdpc.or.th](https://www.pdpc.or.th) under *Laws & Regulations*
- **Citation:** Government Gazette No. 136 Chapter 69 Gor (27 May 2019)
- **Note:** the binding text is the Thai original; English versions are reference only.

### Planned for v0.2 — additional SEA jurisdictions

The next minor release adds three more SEA jurisdictions. See [CHANGELOG.md](CHANGELOG.md) and [`jurisdictions/_index.md`](jurisdictions/_index.md). Until v0.2 ships, these regimes are listed here for awareness only and are **not yet covered** by this skill.

- **Malaysia — Personal Data Protection Act 2010 (with the 2024 Amendments).** Regulator: Jabatan Perlindungan Data Peribadi (JPDP). The 2024 amendments introduce mandatory DPO designation, mandatory breach notification, data portability, and significantly raised penalties.
- **Philippines — Data Privacy Act 2012 (Republic Act 10173).** Regulator: National Privacy Commission (NPC) — [privacy.gov.ph](https://privacy.gov.ph). NPC Circular 16-03 governs breach notification (72-hour window).
- **Vietnam — Personal Data Protection Decree 13/2023/ND-CP (PDPD).** Regulator: A05 (Department of Cybersecurity and High-Tech Crime Prevention), Ministry of Public Security. The full Personal Data Protection **Law** is drafted and will eventually replace the decree — track and re-cut on enactment.

## Disclaimer

See [DISCLAIMER.md](DISCLAIMER.md). **This skill is reference material, not legal advice.** Always verify against the official statute and consult a qualified Data Protection Officer (DPO) or lawyer before relying on it for compliance decisions.

## Contributing

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Particularly valued:

- Malaysia PDPA, Philippines DPA, and Vietnam PDPD jurisdiction content (v0.2 milestone)
- Stack-specific implementation examples for the layer files (without coupling the layer text itself to any stack)
- Real-world incident-response notes that generalise

## Licence

[MIT](LICENSE) — use freely, including in commercial products. Attribution appreciated but not required.
