# personal-data-protection-skill

> ⚠ **Engineering reference material — not legal advice.** This skill summarises personal-data-protection obligations as they apply to building software. It is **not** authoritative legal guidance and **must not** be used as the sole basis for compliance decisions. Always verify against the official statute and consult a qualified DPO or lawyer. See [DISCLAIMER.md](DISCLAIMER.md).
>
> **Source-text posture:** this skill **does not reproduce or republish any of the underlying statutes**. It provides engineer-facing interpretation, layered patterns, and short attributed quotations of operative phrases under fair-dealing principles, with links to the official sources. Anyone planning to package or redistribute this content beyond similar engineering-reference use should read [DISCLAIMER.md § Copyright in source materials](DISCLAIMER.md#copyright-in-source-materials) — Malaysia's PNMB-published Act 709 / Act A1727 carry the strictest publisher's notice of the four jurisdictions and may require prior permission.

A Claude Code [skill](https://docs.claude.com/en/docs/claude-code/skills) that helps engineers build and maintain personal-data-protection-compliant applications, organised by where in the stack each obligation lands rather than by statute section number.

**Status:** Singapore PDPA, Thailand PDPA, Indonesia UU PDP, and Malaysia PDPA all populated. Repo is packaged as a Claude Code plugin (skill content under `skills/personal-data-protection/`); installable via `/plugin install` or direct clone. Philippines / Vietnam planned for v0.4.

**Audience:** anyone building any app or service that handles personal data of users in Singapore, Thailand, Indonesia, or Malaysia. Tech-agnostic — works whether your stack is Supabase, Firebase, AWS, your own backend, native iOS/Android, Flutter, React Native, web, a headless API, or anything else.

## Why this exists

Personal-data-protection statutes are written by lawyers, for lawyers. Engineers shipping features need answers like *"I'm adding a new column that stores user PII — what do I touch?"*, not section numbers. This skill bridges the two:

- **Layered guidance** by where in the stack the obligation lives (architecture, data model, controls, feature/UX, disclosure, operational) — universal across jurisdictions.
- **Jurisdiction-specific obligations** mapped to the relevant statute sections.
- **Entry-point checklists** for common tasks: new feature, new data field, new vendor, breach response.
- **Statute-map** for reverse lookup when you need to cite a section in a PR description, audit response, or breach notification.

## How the four statutes diverge — developer view

This table is **application code and UX only**. Each row starts with *"If your app does X..."* and the per-jurisdiction columns describe how the implementation actually differs — what UI element to add, what column to create, what flow to build, what template to ship.

Governance/legal items (DPO appointment, staff AUP wording, vendor DPA contracts, regulator notification portals, penalty-cap exposure) are **excluded** — those are real obligations but they don't change what your application does. See `skills/personal-data-protection/jurisdictions/<code>/obligations/` for those.

Areas where the four regimes are **equivalent** at the app level (consent capture, withdrawal symmetry, per-user data isolation, retention sweeps, EXIF strip, soft-prompt dialogs, backup retention) are also omitted — the same code satisfies all four.

| If your app... | Singapore PDPA | Thailand PDPA | Indonesia UU PDP | Malaysia PDPA |
|---|---|---|---|---|
| **Has a signup consent screen** | Single bundled "I agree to T&C + Privacy" checkbox is acceptable when all processing is transactional | Same screen works, **but** if you collect any sensitive-category data (see below), add a separate explicit-consent modal for those fields specifically | **Stricter form requirements** (Pasal 22): consent must be written/recorded, clearly distinguishable, in simple/clear language. Non-compliant consent is **null and void by law** (Pasal 22(5)) — no fallback. **Pasal 25** also requires accessible alternative consent channels for persons with disabilities (screen-reader-compatible flows, alternative formats; consent obtainable from the person and/or their guardian) — unique to ID among the four | Bundled checkbox works, **but the privacy notice (s7) must be in BOTH Bahasa Malaysia AND English** (s7(3)). Maintain both versions in your release pipeline |
| **Collects sensitive data** (anything that could fall into health, biometrics, religion, sexuality, ethnicity, political opinion, criminal record, trade union, genetic, location patterns over time) | Apply the narrow deemed-significant-harm list — usually no special UX | Broad s26 — almost certainly need a **separate explicit-consent dialog** before collection, plus stricter logging on those fields | "Specific" Personal Data category (Pasal 4) — typically health, **biometric (face embeddings, fingerprints, voice prints, gait, iris)**, genetic, criminal records, children's data, financial. Requires explicit consent under Pasal 20(2)(a) | s4 list now includes **biometric data** (added 2024) — separate **explicit-consent dialog** under s40(1)(a). Face embeddings, fingerprint hashes, voice prints all in scope |
| **Ships a new feature involving high-risk processing** (sensitive data, large-scale profiling, automated decisions, novel tech, public-area monitoring, data matching, rights-restrictive processing) | No statutory DPIA; PDPC guidance recommends one — best-practice artefact, no launch gate | No statutory DPIA; common best practice for sensitive-data features | **Pasal 34 — mandatory DPIA before launch** when any of 7 enumerated triggers fires (automation, sensitive PD, large-scale, regular systematic monitoring, data matching, novel technology, rights-restrictive processing). Skipping renders processing non-compliant; have the artefact (purpose, categories, risk, mitigation) on file before deployment | No statutory DPIA; JPDP guidance encourages |
| **Has a Settings screen with notification toggles** | Single "Notifications on/off" works for transactional-only apps; consent withdrawal handled "as soon as reasonably possible" (no statutory SLA) | Same — split into transactional vs marketing the moment marketing is added; no statutory SLA on withdrawal | Same — but **Pasal 40 requires processing to stop within 72 hours** of consent withdrawal. Encode this as a per-jurisdiction SLA constant in the consent-withdrawal handler | Same — split transactional vs marketing; honour s43 direct-marketing opt-out per channel; "reasonable period" under s38 (operationally treat as next send-batch) |
| **Lets users delete their account** | Hard-delete + "Deleted User" attribution for shared content (chat history etc.) | Same flow works, **plus** offer "Anonymize" as an alternative choice in the confirmation UI (s33 explicitly covers erase OR anonymize) | Pasal 8 + 43 + 44 — explicit **erasure AND destruction** obligations (the Act distinguishes the two; destruction is more permanent). Subject can request both | s10 Retention Principle: must **destroy or permanently delete** when the purpose ends — soft-delete alone isn't compliant; pair with a sweep job |
| **Lets users export their data** | Any structured format (JSON, CSV, ZIP) | Same, **but** format must be **suitable for transfer to another controller** — JSON works, ad-hoc proprietary blobs don't (s31) | Pasal 13 — machine-readable format; right to send/transfer to another Controller where systems can communicate securely. Must respond in **72 hours** (Pasal 32) | s30 access (21 days) + **s43A data portability (new 2024)** — direct transmission to another controller subject to technical-feasibility / format-compatibility caveat |
| **Lets users pause processing without deleting** their account | No such feature needed | **Build it** (s34) — schema: `processing_restricted_at` column on user record. UI: Settings toggle. Code: check on every mutation; reads still allowed | **Required (Pasal 11)** — same code mechanism as Thailand. PLUS **72-hour SLA** (Pasal 41) — must comply or document statutory exception | s42 — same `processing_restricted_at` mechanism; trigger is "substantial damage or distress", not at-will |
| **Lets admins / support read individual user data** | Audit-log mutations (best practice; not strictly required) | Audit-log mutations + maintain a discoverable s39 record-of-processing-activities document for the regulator | Pasal 31 explicit Records of Processing Activities (RoPA) requirement for **all** processing — formalised inventory, regulator can request | s44 record obligation — list of disclosures + categories of recipients, produced on Commissioner's request. s9(1)(d) personnel-reliability requirement; audit reads of sensitive columns |
| **Is a B2B SaaS / processes personal data on behalf of other businesses** (i.e., you are a "data processor" / "data intermediary") | Narrow direct duties: s24 (protection) and s25 (retention) bind on data intermediaries (s4(2) + s11(2)). Otherwise controller-driven; flow obligations via DPA | s40 — processor must comply with s37 security standards, process only per controller's instructions, notify controller of breach without delay | Pasal 51–52 — processor obligations parallel controller; sub-processor controls; instructions-based processing | **New direct duty post-A1727 (1 Apr 2025): s5(1A) makes the processor directly bound by the Security Principle (s9), and s12A(2) requires the processor to appoint its own DPO** — independent statutory floor on top of the customer DPA. Plan your breach-notification flow-down so customers can still hit their 72h s12B(1) clock |
| **Stores user data with cloud providers in another country** | Privacy policy mention of "service providers" is sufficient if vendor DPAs are in place | If relying on s28(2) consent: signup screen must disclose destination + that protection status is inadequate. If relying on s28(3) contractual necessity: vendor DPAs sufficient (most realistic) | **3-tier hierarchy (Pasal 56)**: adequacy → adequate-and-binding safeguards → consent. No published adequacy list yet from the regulator — most realistic basis is Tier 2 (vendor DPAs with binding clauses) | **s129 post-A1727 (1 Apr 2025) — whitelist regime deleted.** Realistic basis is **s129(3)(f) due diligence**: vendor DPA + cert audits (ISO 27001 / SOC 2) + documented assessment. Burden on the controller |
| **Has an incident response runbook** | Lane: 3 calendar days from breach-assessment-as-notifiable; PDPC SG portal | Lane: 72 hours from *awareness* (faster); PDPC Thailand portal | **72-hour lane (Pasal 46)** — but distinct: notify **BOTH** subject AND regulator; "certain circumstances" trigger public notification. Operationally heavier than SG/TH | **72-hour Commissioner notification + 7-day subject notification** (s12B + JPDP Guideline 25 Feb 2025); JPDP Personal Data Protection System portal |

**How to use this table:** find the row matching what your app already does (or is about to do). Read across — if the per-jurisdiction columns are the same, you ship one implementation. If they differ, you either build the strictest version (covers all) or branch by user jurisdiction (more code, more nuanced UX).

For the section-by-section walkthrough, see [`skills/personal-data-protection/jurisdictions/`](skills/personal-data-protection/jurisdictions/) and [`skills/personal-data-protection/jurisdictions/_index.md`](skills/personal-data-protection/jurisdictions/_index.md).

## Install

The repo is laid out as a Claude Code **plugin** — skill content lives under [`skills/personal-data-protection/`](skills/personal-data-protection/). Three install paths depending on your tool:

### Claude Code / Claude Cowork — via this repo's marketplace (works today)

```bash
claude plugin marketplace add AltByteSG/personal-data-protection-skill
claude plugin install personal-data-protection@altbyte-plugins
```

The repo carries a [`marketplace.json`](.claude-plugin/marketplace.json) so it works as a single-plugin marketplace. Verify with `claude plugin list`.

### Claude Code / Claude Cowork — via the official Anthropic marketplace (once approved)

```
/plugin install personal-data-protection@claude-plugins-official
```

Pending Anthropic review of the submission. Both install paths can coexist — pick one.

### Codex CLI / Cursor / Copilot

```bash
git clone https://github.com/AltByteSG/personal-data-protection-skill.git ~/.tools/personal-data-protection-skill
```

Then add a single line to your project's existing `AGENTS.md` / `.cursorrules` / `.github/copilot-instructions.md`:

```markdown
For personal-data-protection compliance, follow
~/.tools/personal-data-protection-skill/AGENTS.md
```

The root [`AGENTS.md`](AGENTS.md) routes the agent into the skill content under `skills/personal-data-protection/`.

### Pin a specific upstream version

```bash
cd <clone-path> && git checkout v0.2.0
```

## Adapt to your project

Two templates ship in [`skills/personal-data-protection/templates/`](skills/personal-data-protection/templates/). Setup instructions are in each file's header.

- **[`INCIDENT_RESPONSE.md.template`](skills/personal-data-protection/templates/INCIDENT_RESPONSE.md.template)** — *works with any agent.* Solo / small-team breach runbook. Copy to your project's `docs/` folder and fill in the `{{PLACEHOLDERS}}` (DPO contact, vendor list, jurisdictions).
- **[`pdp-nudge.sh.template`](skills/personal-data-protection/templates/pdp-nudge.sh.template)** — **Claude Code only.** Auto-nudges Claude into this skill on edits to PDP-sensitive paths via a `PostToolUse` hook. Codex CLI, Cursor, and Copilot do not have an equivalent hook system at time of writing, so this template is not portable — manual diligence on PDP-sensitive paths is the substitute on those agents.

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

### Malaysia — Personal Data Protection Act 2010 (with the 2024 Amendments)

- **Statute (Act 709, consolidated bilingual):** JPDP-published PDF — [pdp.gov.my Act 709 EN/BM](https://www.pdp.gov.my/ppdpv1/wp-content/uploads/2024/07/UNDANG-UNDANG-MALAYSIA_AKTA_PERLINDUNGAN_DATA_PERIBADI_2010_709_MALAY_AND-ENG_V2022.pdf)
- **Amendment Act 2024 (Act A1727):** [pdp.gov.my Act A1727](https://www.pdp.gov.my/ppdpv1/wp-content/uploads/2024/11/Act-A1727.pdf) — Royal Assent 9 October 2024; staged commencement under P.U.(B) 522/2024 (1 January 2025, 1 April 2025, **1 June 2025**).
- **Regulator:** Department of Personal Data Protection (Jabatan Perlindungan Data Peribadi, JPDP) under the Ministry of Digital — [www.pdp.gov.my](https://www.pdp.gov.my)
- **Operative JPDP guidelines (issued 25 February 2025; effective 1 June 2025):** Personal Data Protection Guideline on the Appointment of Data Protection Officer; Personal Data Protection Guideline on Data Breach Notification.
- **Federal Legislation portal (alternative source):** [lom.agc.gov.my](https://lom.agc.gov.my) — search *"Act 709"* / *"Act A1727"*.

### Planned for v0.4 — additional SEA jurisdictions

A future minor release (v0.4) will add the remaining SEA jurisdictions. See [CHANGELOG.md](CHANGELOG.md) and [`skills/personal-data-protection/jurisdictions/_index.md`](skills/personal-data-protection/jurisdictions/_index.md). Until v0.4 ships, these regimes are listed here for awareness only and are **not yet covered** by this skill.

- **Philippines — Data Privacy Act 2012 (Republic Act 10173).** Regulator: National Privacy Commission (NPC) — [privacy.gov.ph](https://privacy.gov.ph). NPC Circular 16-03 governs breach notification (72-hour window).
- **Vietnam — Personal Data Protection Decree 13/2023/ND-CP (PDPD).** Regulator: A05 (Department of Cybersecurity and High-Tech Crime Prevention), Ministry of Public Security. The full Personal Data Protection **Law** is drafted and will eventually replace the decree — track and re-cut on enactment.

## Disclaimer

See [DISCLAIMER.md](DISCLAIMER.md). **This skill is reference material, not legal advice.** Always verify against the official statute and consult a qualified Data Protection Officer (DPO) or lawyer before relying on it for compliance decisions.

## Privacy

See [PRIVACY.md](PRIVACY.md). **This skill collects no data.** It is documentation, not running software — no telemetry, no source-code transmission, no usage tracking by the maintainers.

## Contributing

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Particularly valued:

- Philippines DPA and Vietnam PDPD jurisdiction content (v0.4 milestone)
- Stack-specific implementation examples for the layer files (without coupling the layer text itself to any stack)
- Real-world incident-response notes that generalise

## Licence

[MIT](LICENSE) — use freely, including in commercial products. Attribution appreciated but not required.
