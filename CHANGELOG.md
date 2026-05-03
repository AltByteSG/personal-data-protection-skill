# Changelog

All notable changes to this skill are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Each release records the statute versions reflected in the content. When a statute amends, a new minor or patch release is cut. Pin to a specific tag in a submodule if you want to control upgrade timing.

## Unreleased

### Planned for v0.2 — additional SEA jurisdictions

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

[Unreleased]: https://github.com/AltByteSG/personal-data-protection-skill/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.1.0
