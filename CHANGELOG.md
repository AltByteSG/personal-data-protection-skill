# Changelog

All notable changes to this skill are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Each release records the statute versions reflected in the content. When a statute amends, a new minor or patch release is cut. Pin to a specific tag in a submodule if you want to control upgrade timing.

## Unreleased

— No unreleased changes.

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

[Unreleased]: https://github.com/AltByteSG/personal-data-protection-skill/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.2.1
[0.2.0]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.2.0
[0.1.0]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.1.0
