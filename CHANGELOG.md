# Changelog

All notable changes to this skill are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Each release records the statute versions reflected in the content. When a statute amends, a new minor or patch release is cut. Pin to a specific tag in a submodule if you want to control upgrade timing.

## Unreleased

— No unreleased changes.

## [0.3.0] — 2026-05-04

Adds **Malaysia PDPA 2010 (with the 2024 Amendments — Act A1727)** as the fourth populated jurisdiction. Reflects the staged commencement of Act A1727 under P.U.(B) 522/2024 (1 January 2025, 1 April 2025, **1 June 2025**) and the operative JPDP guidelines on DPO appointment and data breach notification (issued 25 February 2025, effective 1 June 2025). Templates and checklists rewired to support the MY breach lane and processor regime; top-level divergence table extended with two new engineering-affecting rows (B2B SaaS processor; high-risk processing / DPIA); existing TH and ID obligation files trimmed to align with the engineering-first framing rule that the MY draft was written to. Philippines DPA and Vietnam PDPD now deferred to v0.4.

### Added — Malaysia jurisdiction content

- New jurisdiction directory [`skills/personal-data-protection/jurisdictions/my-pdpa/`](skills/personal-data-protection/jurisdictions/my-pdpa/) with:
  - `README.md` — statute metadata, critical thresholds, application / territorial reach (s2–s3), mental model
  - `statute-map.md` — reverse lookup from section number → obligation file → universal layer
  - 7 obligation files mirroring the SG / TH / ID structure: `01-accountability.md` (s12A DPO + s23–29 codes of practice + vendor flow-down), `02-consent.md` (General Principle s6, withdrawal s38, sensitive PD s40, direct marketing s43), `03-purpose.md` (Notice & Choice s7 incl. **bilingual BM/EN** requirement, Disclosure s8, s39, s41), `04-access-correction.md` (s30–37 access/correction, s42 prevention, **s43A data portability — new 2024**), `05-care.md` (Security s9 incl. processor direct duty, Retention s10, Data Integrity s11, Record s44, **Cross-border s129 post-whitelist removal**), `06-breach-notification.md` (s12B + JPDP Guideline 25 Feb 2025: 72h Commissioner / 7d subject), `07-offences.md` (penalty matrix incl. **s133 directors' deeming liability**)

### Added — divergence-table rows (engineering-affecting)

The top-level [README divergence table](README.md#how-the-four-statutes-diverge--developer-view) gained two new rows in addition to the new Malaysia column:

- **"Is a B2B SaaS / processes personal data on behalf of other businesses"** — captures MY's new processor direct duty under s5(1A) (Security Principle, 1 April 2025) and s12A(2) (DPO appointment, 1 June 2025), against TH s40, ID Pasal 51–52, and SG's narrower data-intermediary regime.
- **"Ships a new feature involving high-risk processing"** — captures ID's mandatory Pasal 34 DPIA as a pre-launch engineering gate (the only one of the four jurisdictions with a statutory DPIA requirement).

### Changed — cross-jurisdiction docs

- [`SKILL.md`](skills/personal-data-protection/SKILL.md) — frontmatter description and jurisdiction table updated to include Malaysia; "Critical thresholds" table grew a fourth column.
- [`skills/personal-data-protection/jurisdictions/_index.md`](skills/personal-data-protection/jurisdictions/_index.md) — cross-jurisdiction comparison grew a fourth column; status table marks `my-pdpa` populated; PH/VN now flagged for v0.4.
- [`README.md`](README.md) — divergence table extended (see above); Sources section gained a Malaysia subsection (Act 709 PDF, Act A1727 PDF, JPDP guidelines, JPDP regulator); "Planned" section moved from v0.3 to v0.4 with PH and VN as the remaining items; existing rows tightened — row 2 (sensitive data) ID column lists biometric / health / genetic / criminal / children's / financial categories explicitly; row 3 (notification toggles) makes the consent-withdrawal SLA comparison explicit across all four columns; row 1 (signup consent) ID column now also captures Pasal 25 accessibility / alternative consent channels for persons with disabilities (unique to ID); audience line broadened to "any app or service" with headless API in the stack list.
- [`AGENTS.md`](AGENTS.md) — Codex / Cursor / Copilot entry point mirrored: jurisdiction table includes MY (populated), critical-thresholds table grew a fourth column, "all four jurisdictions" wording aligned with SKILL.md.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — JPDP added to the regulator list for statute-update PRs; v0.4 milestone now lists PH and VN only.

### Changed — templates and checklists (engineer-facing artefacts)

- [`templates/INCIDENT_RESPONSE.md.template`](skills/personal-data-protection/templates/INCIDENT_RESPONSE.md.template) — statutory-clocks table grew a Subject-notification column and a Malaysia row (72h Commissioner from discovery / 7d subject post-Commissioner per JPDP Guideline); the "Indonesia / Thailand" assessment + filing sections now also cover Malaysia; quick-reference table grew a Malaysia column; penalty-summary footer gained the MY entry (s12B(3) RM 250k / 2y for notification failure; s5(2) RM 1M / 3y for underlying Security Principle breach; s133 director-deeming).
- [`checklists/breach-response.md`](skills/personal-data-protection/checklists/breach-response.md) — critical-timer table replaced "(planned coverage)" placeholders with the live MY 72h+7d row and a Subject-notification column.
- [`checklists/new-vendor.md`](skills/personal-data-protection/checklists/new-vendor.md) — DPA breach-flow-down clause tightened to reference all four jurisdictions' clocks (≤24h vendor flow-down so controller hits the strictest 72h or 3d window); cross-border-basis section split into per-jurisdiction items including MY s129(3)(f) due diligence post-whitelist; jurisdiction-notes table grew a MY row (processor s12A(2) DPO appointment now an evidence item, not just a contractual term).
- [`checklists/new-feature.md`](skills/personal-data-protection/checklists/new-feature.md) — jurisdiction-specific section expanded from "(if active) — once populated" stubs into fully drafted TH / ID / MY sub-blocks pointing engineers at the specific obligations to verify per feature (TH s26 sensitive data, s32 portability, s34 restrict, s37 breach; ID Pasal 22 form-of-consent, Pasal 25 accessibility, Pasal 34 DPIA trigger check, Pasal 31 RoPA, Pasal 40/41 72h SLAs, Pasal 46 dual notification; MY s7(3) bilingual notice, s4 biometric in sensitive data, s9/s5(1A) processor direct duty, s12B 72h+7d breach, s43A portability).
- [`checklists/new-data-field.md`](skills/personal-data-protection/checklists/new-data-field.md) — jurisdiction check items split per jurisdiction with concrete TH s24/s26, ID Pasal 20/Pasal 4/Pasal 34/Pasal 31, and MY s6/s6(3)/s4/s40(1)(a)/s44 references (replacing the previous "(when populated)" stub).

### Changed — TH and ID obligation files (engineering-first audit)

The MY draft was written to a stricter "engineering-first" rule than the SG/TH/ID files predated. A focused audit identified governance over-emphasis in 6 of 14 TH/ID obligation files; the following targeted trims bring them in line with the same bar (no content was removed that an engineer needs — full DPO duties, role-design language, and corporate-liability narrative are all retained in the corresponding non-technical layer / offences file):

- [`th-pdpa/obligations/01-accountability.md`](skills/personal-data-protection/jurisdictions/th-pdpa/obligations/01-accountability.md) — s41/s42 DPO designation + duties (~30 lines of governance prose) collapsed into a 3-bullet engineering-surface section (published contact email, audit-log access, exec-reporting touch-point).
- [`th-pdpa/obligations/05-care.md`](skills/personal-data-protection/jurisdictions/th-pdpa/obligations/05-care.md) — adequacy-decision narrative trimmed; processor cross-reference trimmed to a single forward-pointer.
- [`th-pdpa/obligations/06-breach-notification.md`](skills/personal-data-protection/jurisdictions/th-pdpa/obligations/06-breach-notification.md) — risk-to-rights-and-freedoms section flipped from PDPC-guidance-prose framing to engineer-checklist-first format (high-risk indicators lead, factors follow as a sentence).
- [`id-pdp/obligations/01-accountability.md`](skills/personal-data-protection/jurisdictions/id-pdp/obligations/01-accountability.md) — same DPO trim pattern as TH; Pasal 53/54 governance prose collapsed into 3-bullet engineering surface (contact channel, RoPA + audit-log read access, DPIA sign-off ownership).
- [`id-pdp/obligations/05-care.md`](skills/personal-data-protection/jurisdictions/id-pdp/obligations/05-care.md) — Pasal 37 supervision section reframed to lead with the engineering control (vendor register + technical scoping + audit cadence) rather than the governance principle.
- [`id-pdp/obligations/07-offences.md`](skills/personal-data-protection/jurisdictions/id-pdp/obligations/07-offences.md) — Pasal 70 corporate-criminal multi-paragraph governance narrative collapsed into one tight paragraph + an engineering-relevance line; mental-model bullet 2 reframed to focus on the audit-trail engineering input rather than dissolution-as-enforcement-tool framing.

### Fixed

- [`my-pdpa/obligations/04-access-correction.md`](skills/personal-data-protection/jurisdictions/my-pdpa/obligations/04-access-correction.md) — corrected a broken relative link to `jurisdictions/_index.md` (was `../_index.md`, should have been `../../_index.md`).
- [`id-pdp/obligations/02-consent.md`](skills/personal-data-protection/jurisdictions/id-pdp/obligations/02-consent.md) — "unique to Indonesia among the three jurisdictions covered" updated to "four" now that MY is populated.
- [`README.md`](README.md) status line — Malaysia entry de-bolded and the redundant "(with 2024 Amendments — Act A1727)" parenthetical removed for parity with the other three jurisdictions; "Philippines / Vietnam planned for v0.3" corrected to v0.4.

### Changed — disclaimer

- [`DISCLAIMER.md`](DISCLAIMER.md) — "What this skill is" and "Not licensed to practise law" sentences now name Malaysia explicitly. "Authoritative sources" gained a Malaysia entry (JPDP regulator + Federal Legislation portal). **The "Copyright in source materials" section now flags Malaysia separately** because the PNMB-published Act 709 / Act A1727 PDFs carry a notably restrictive publisher's copyright notice ("No part of this publication may be reproduced... without the prior permission of Percetakan Nasional Malaysia Berhad") that goes beyond the SSO / PDPC Thailand / peraturan.go.id terms. Reusers planning redistribution should treat MY source-copyright posture as the strictest of the four. Section 3 (redistribution permission) also now expressly mentions PNMB / JPDP as the relevant Malaysian permission-grantors.
- **Top-level disclaimer banner mirrored to entry-point files** — [`README.md`](README.md), [`skills/personal-data-protection/SKILL.md`](skills/personal-data-protection/SKILL.md), and [`AGENTS.md`](AGENTS.md) now each carry a short "Source-text posture" line: this skill **does not reproduce or republish** any underlying statute; it provides engineer-facing interpretation and short attributed quotations under fair-dealing, with the MY PNMB notice flagged as the strictest of the four for redistribution purposes. SKILL.md also updated to name Malaysia in the "not licensed to practise law" sentence (was missing) and in the layered-reference paragraph that previously said "Singapore, Indonesia, and Thailand".

### Plugin manifest

- [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) — `version` 0.2.2 → **0.3.0**; description and keywords expanded to include Malaysia.
- [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) — plugin description expanded to include Malaysia.

### Statute coverage matrix

| Jurisdiction | Statute version | Last verified |
|---|---|---|
| Singapore PDPA 2012 | Current as at 1 May 2026 (reflects 2020 Amendments) | 2026-05-02 |
| Thailand PDPA B.E. 2562 (2019) | Original 2019 text (PDPC Thailand English translation) | 2026-05-03 |
| Indonesia UU PDP No. 27/2022 | Original 2022 text (in force from 17 Oct 2024) | 2026-05-03 |
| Malaysia PDPA 2010 (Act 709) | Act 709 as amended by Act A1727 (all provisions in force as at 1 June 2025) | 2026-05-04 |

### Where to look for the engineering-level divergences

For the application-level divergences engineers need on a feature PR (consent UX, sensitive-data scope incl. biometric, retention/destroy, export + s43A portability, cross-border post-whitelist, 72h+7d breach lane, B2B-SaaS processor direct duty, mandatory DPIA in ID, accessibility-alternative consent in ID), see the developer-view divergence table in the top-level [`README.md`](README.md#how-the-four-statutes-diverge--developer-view).

## [0.2.2] — 2026-05-03

Fixes the marketplace `source` field so `claude plugin install` actually works. v0.2.1's `"source": "."` was rejected by the CLI as "source type your Claude Code version does not support."

### Changed

- [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json): replaced `"source": "."` with the official `{ "source": "url", "url": "..." }` object form used by the Anthropic-curated marketplace. Same effect (clones this repo and treats the whole repo as the plugin), but matches the documented schema the CLI accepts.
- Added `category: "compliance"` and `homepage` fields for marketplace listing.

## [0.2.1] — 2026-05-03

Adds a marketplace manifest so the plugin is installable via `claude plugin marketplace add` + `claude plugin install` without waiting for the official Anthropic marketplace approval.

### Added

- [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) — single-plugin marketplace manifest naming this repo as the `altbyte-plugins` marketplace and exposing `personal-data-protection` as its sole plugin.

### Install (once the marketplace is added)

```bash
claude plugin marketplace add AltByteSG/personal-data-protection-skill
claude plugin install personal-data-protection@altbyte-plugins
```

This is the working install path before the official Anthropic marketplace lists the plugin. Once the official marketplace lists it, `claude plugin install personal-data-protection@claude-plugins-official` will also work — both paths can coexist.

## [0.2.0] — 2026-05-03

Repo restructured as a Claude Code plugin to enable distribution via the official Anthropic plugin marketplace ([platform.claude.com/plugins](https://platform.claude.com/plugins)). No content changes — same SG / TH / ID jurisdictions, same layers, same checklists, same templates as v0.1.0.

### Changed

- **Layout:** all skill content (`SKILL.md`, `layers/`, `jurisdictions/`, `checklists/`, `templates/`) moved from the repo root into `skills/personal-data-protection/`. Required by the plugin loader, which only auto-discovers skills in a `skills/<name>/` subdirectory at the plugin root.
- **Plugin manifest:** added [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) declaring the plugin name, version, author, repository, license, and keywords. Required by the plugin loader.
- **Relative-path links:** the 41 markdown / template files inside the skill folder had their links to root-level meta files (`DISCLAIMER.md`, `LICENSE`, `CHANGELOG.md`, etc.) repointed by 2 additional `../` hops. No content was edited.
- **Root files:** `README.md`, `LICENSE`, `DISCLAIMER.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, `AGENTS.md`, and `.gitignore` remain at the repo root. `AGENTS.md`'s internal links updated to point into the new `skills/personal-data-protection/` subdirectory so Codex CLI / Cursor / Copilot still work.
- **README install section:** rewritten around three install paths — Claude Code via `/plugin install`, Claude Code via direct clone, and Codex / Cursor / Copilot via clone-and-reference.

### Migration notes for v0.1.0 users

- The bare-clone-into-`.claude/skills/` install pattern from v0.1.0 no longer works. Use the new install paths in [`README.md`](README.md#install).
- If you cloned v0.1.0 manually, either re-clone or pin to the `v0.1.0` tag — the v0.1.0 layout is preserved at that tag.
- All content (statute citations, layer guidance, checklists) is byte-for-byte identical to v0.1.0.

### Statute coverage matrix (unchanged from v0.1.0)

| Jurisdiction | Statute version | Last verified |
|---|---|---|
| Singapore PDPA 2012 | Current as at 1 May 2026 (reflects 2020 Amendments) | 2026-05-03 |
| Thailand PDPA B.E. 2562 (2019) | Original 2019 text (PDPC Thailand English translation) | 2026-05-03 |
| Indonesia UU PDP No. 27/2022 | Original 2022 enactment (Bahasa Indonesia binding text) | 2026-05-03 |

### Planned for v0.3 — additional SEA jurisdictions

| Jurisdiction | Code | Statute | Regulator |
|---|---|---|---|
| Malaysia | `my-pdpa` | Personal Data Protection Act 2010, with the Personal Data Protection (Amendment) Act 2024 (mandatory DPO, mandatory breach notification, data portability, raised penalties) | JPDP — Jabatan Perlindungan Data Peribadi |
| Philippines | `ph-dpa` | Data Privacy Act 2012 (Republic Act 10173) + NPC Circulars (incl. Circular 16-03 on breach notification) | NPC — National Privacy Commission |
| Vietnam | `vn-pdpd` | Personal Data Protection Decree 13/2023/ND-CP (in force 1 July 2023). The full Personal Data Protection **Law** is drafted and will replace the decree once enacted — track and re-cut on enactment. | A05 (Department of Cybersecurity and High-Tech Crime Prevention), Ministry of Public Security |

Each will follow the same shape as the existing v0.1 jurisdictions: `README.md` (statute version metadata, critical thresholds), `statute-map.md` (reverse lookup), and 7 obligation files mapping the statute to the universal layers.

## [0.1.0] — 2026-05-03

Initial release.

### Added
- Singapore PDPA content (statute version: current as of 1 May 2026, reflecting the Personal Data Protection (Amendment) Act 2020):
  - 7 obligation files (Parts 3, 4, 5, 6, 6A, 9B + penalties)
  - Statute-map for reverse lookup
- Thailand PDPA content (statute version: original 2019 text per PDPC Thailand-published English translation):
  - 7 obligation files (Chapter II Parts I–III, Chapter III, s37 / s39 / s41–42, Chapter VII penalties)
  - Statute-map for reverse lookup
- Indonesia UU PDP content (statute version: original 2022 enactment, UU No. 27 Tahun 2022):
  - 7 obligation files (BAB IV–VIII, BAB XIII–XIV)
  - Statute-map for reverse lookup
  - Translation caveat documented (binding text is Bahasa Indonesia)
- Universal (tech-agnostic) layer files:
  - 01 Non-technical (DPO, AUP, complaints)
  - 02 Architecture (least-privilege, encryption, isolation, defence-in-depth)
  - 03 Data model (consent records, audit records, retention markers, deletion conventions)
  - 04 Controls and processes (access control, retention sweeps, log hygiene, breach detection)
  - 05 Feature / UX (signup consent, settings, deletion, export, primer dialogs, EXIF strip)
  - 06 Disclosure (privacy policy, T&C, permission strings, contextual notices)
  - 07 Operational (incident response pointer, retention sweeps, log retention, backups, vendor reviews)
- 4 entry-point checklists: new-feature, new-data-field, new-vendor, breach-response
- 2 templates: incident response runbook, harness nudge hook
- Cross-jurisdiction comparison index covering all three jurisdictions

### Statute coverage matrix

| Jurisdiction | Statute version | Last verified |
|---|---|---|
| Singapore PDPA 2012 | Current as at 1 May 2026 (reflects 2020 Amendments) | 2026-05-03 |
| Thailand PDPA B.E. 2562 (2019) | Original 2019 text (PDPC Thailand English translation) | 2026-05-03 |
| Indonesia UU PDP No. 27/2022 | Original 2022 enactment (Bahasa Indonesia binding text) | 2026-05-03 |

[Unreleased]: https://github.com/AltByteSG/personal-data-protection-skill/compare/v0.2.2...HEAD
[0.2.2]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.2.2
[0.2.1]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.2.1
[0.2.0]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.2.0
[0.1.0]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.1.0
