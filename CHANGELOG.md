# Changelog

All notable changes to this skill are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Each release records the statute versions reflected in the content. When a statute amends, a new minor or patch release is cut. Pin to a specific tag in a submodule if you want to control upgrade timing.

## Unreleased

### Changed — operational guidance consolidated into layer 07

The sub-processor-breach procedure, post-incident record-keeping discipline, and runbook readiness checklist were carried in `id-pdp` and `th-pdpa`'s breach files and **absent from `sg-pdpa`, `my-pdpa` and `ph-dpa` entirely**. They are jurisdiction-neutral, so they now live once in `layers/07-operational.md` under `## Incident response`, and all five jurisdictions reach them through the layer-07 pointers their breach files already carry.

- `skills/personal-data-protection/layers/07-operational.md` — new `Sub-processor / vendor breaches`, `Post-incident records`, and `Runbook readiness checklist` subsections.
- `skills/personal-data-protection/jurisdictions/id-pdp/obligations/06-breach-notification.md` and `.../th-pdpa/...` — those three sections reduced to their statutory hook plus a pointer. Every citation is retained (ID: Pasal 51, 31, 47; TH: s40(2), s39(8)), as are the jurisdiction-specific readiness items (Bahasa Indonesia and Thai notification templates, Komdigi and PDPC submission specifics).

**Token effect is negative, and that was not the expectation.** The breach files shed ~285 tokens while layer 07 gained ~352, so at five active jurisdictions this nets about +67 tokens and more at fewer. The earlier ~1,287-token estimate counted `What's at stake` and `Penalty exposure` as jurisdiction-neutral; inspection showed both are heavily statutory (14 and 8 citations respectively) and they stayed put. What the change does buy is a single source for operational guidance — five copies drifting apart is how the Singapore breach-clock error survived in two files while a third stated the opposite — and operational coverage for the three jurisdictions that previously had none.

### Changed — checklist execution order

Both task checklists ran their jurisdiction review near the end, after the steps it should have shaped. An engineer following either linearly wrote the migration, then learned several steps later that the column needed encryption; or drafted privacy-policy copy before discovering MY s7(3) requires it bilingually and PH § 13 requires written consent captured before processing.

- `skills/personal-data-protection/checklists/new-feature.md` — the jurisdiction-specific review moves from step 8 to step 2, so every layer review below it is jurisdiction-aware. The layer 02–07 reviews stay contiguous, shifted to steps 3–8. Added a short rationale naming the three obligations that change what you build rather than what you check afterwards.
- `skills/personal-data-protection/checklists/new-data-field.md` — the jurisdiction check moves from step 9 to step 2. Step 10 ("Sensitive data extra steps") is dissolved into the steps that act on it: column-level encryption into the data-model step, access tightening into admin visibility, and the breach-assessment matrix entry into the jurisdiction step where notifiability thresholds are decided. Each keeps an explicit "If sensitive (step 1)" marker. The disclosure step gained a line tying it back to the jurisdiction-specific notice requirements. Now nine steps rather than ten; no checklist item was dropped.

Earlier CHANGELOG entries refer to these checklists by their previous step numbers, which were accurate at the time of those releases.

### Changed — scanner keyword precision

- `scripts/pdp-check-changed-files.py` — `address` and `notification` matched bare, firing on `ip_address`, `address_bar`, `macAddress`, and every push or toast notification in a codebase. Both now require a personal-data qualifier: `home_address`, `shipping_address`, `billing_address`, `mailing_address`, `postal_address`, `street_address`, `address_line1` and `notification_preferences`, `notification_consent`, `notification_opt_in`, `push_token` all match, while the plumbing spellings no longer do. `email_address` was already covered by `email`.
- `tests/test_pdp_check.py` — four new tests pin both directions of that change (22 total).

### Removed

- `skills/personal-data-protection/jurisdictions/sg-pdpa/obligations/06-breach-notification.md` — dropped a leftover reference to a specific project ("High-risk PaoPao-style categories") in favour of neutral phrasing. Skill content carries no project-specific names.

### Changed — token footprint

- `SKILL.md` — the jurisdiction status table duplicated the one in `jurisdictions/_index.md` row for row. Replaced with a one-line code list plus a pointer; `_index.md` is now the single source for status and the comparison grid. `SKILL.md` loads on every session, so this is paid every time.
- `layers/04-controls-and-processes.md` — the backwards-compatibility rules restated `layers/02-architecture.md`. Layer 02 is now canonical and layer 04 carries only its two additions; both files load on a new-feature checklist run.
- `jurisdictions/id-pdp/obligations/06-breach-notification.md` — the inline sample breach email near-duplicated section 5 of `templates/INCIDENT_RESPONSE.md.template`. Replaced with a pointer to the template plus the two ID-specific points (regulator naming, no harm threshold), so the wording cannot drift per jurisdiction.

### Added — tooling

- `tests/test_pdp_check.py` — 18 tests over `scripts/pdp-check-changed-files.py`: field-name detection across snake_case, kebab-case, camelCase and acronym boundaries (the conventions the pre-0.4.1 scanner silently missed), negative controls, config loading and error paths, jurisdiction and policy validation, and path-rule classification. Runs under pytest or directly with `python3 tests/test_pdp_check.py`.
- `pyproject.toml` — ruff configuration (`target-version = "py39"`, line length, rule selection). Tool config only: the release version stays in the plugin manifests rather than being duplicated where it could drift.
- `.markdownlint.json` — disables MD013 (line length). The long lines are jurisdiction comparison tables and verbatim statute citations, where wrapping would hurt readability; MD032 and the rest stay enforced.

### Changed — skill description

- `skills/personal-data-protection/SKILL.md` — trimmed the frontmatter `description` from 557 to 429 characters (~32 tokens). Skill descriptions load into every session for routing whether or not the skill fires, so this is the one surface paid on every conversation. Dropped the statute version annotations (`27/2022`, `B.E. 2562 (2019)`, `2010 (with the 2024 Amendments)`) — nobody routes on them, and each jurisdiction README records the version authoritatively. Kept `RA 10173`, which is a genuine alias the Philippine law is cited by. Dropped the trailing sentence describing first-use behaviour, which is runtime workflow rather than a routing criterion and is already implemented by Step 1. Narrowed `admin access controls` to `admin access to personal-data stores` so the skill stops matching generic RBAC / IAM questions.
- `AGENTS.md` — mirrored the same narrowing in its agent trigger sentence, and added `breach response`, which `SKILL.md` listed but `AGENTS.md` had omitted despite `checklists/breach-response.md` being a core entry point.

### Fixed

- `SKILL.md` — added the missing blank line before the statute-version list (MD032).
- `scripts/pdp-check-changed-files.py` — import ordering, and `capture_output=True` in place of the separate `stdout`/`stderr` PIPE arguments (ruff I001, UP022).

## [0.4.1] — 2026-09-17

Correctness and coverage pass following an external skill review. No statute
version changes — the underlying statutes reflected are unchanged from 0.4.0.

### Fixed — factual corrections

- [`skills/personal-data-protection/jurisdictions/_index.md`](skills/personal-data-protection/jurisdictions/_index.md) and [`skills/personal-data-protection/jurisdictions/sg-pdpa/README.md`](skills/personal-data-protection/jurisdictions/sg-pdpa/README.md) — corrected the claim that Singapore's 3-calendar-day breach clock is the strictest. SG s26D(1) runs from **assessment**, while the MY / TH / ID / PH 72-hour clocks run from **awareness / discovery / knowledge**, so SG is operationally *looser* and does not control the multi-jurisdiction deadline. Both files previously contradicted the (correct) note already carried in `templates/INCIDENT_RESPONSE.md.template`.
- [`skills/personal-data-protection/layers/07-operational.md`](skills/personal-data-protection/layers/07-operational.md) and [`skills/personal-data-protection/checklists/breach-response.md`](skills/personal-data-protection/checklists/breach-response.md) — the "internal-only access is not notifiable" shortcut is now qualified per jurisdiction. It is an explicit SG carve-out (s26B(4)); TH has none (s37(1) — still a breach, notifiability per risk assessment), and ID / MY / PH carry no explicit carve-out either. Previously stated without qualifier, contradicting `th-pdpa/obligations/06-breach-notification.md`.

### Added — Philippines coverage completed

v0.4.0 added the `ph-dpa` obligation tree and extended the top-level surfaces, but the task checklists and the incident-response runbook template were missed. PH is now present in all of them:

- [`skills/personal-data-protection/checklists/breach-response.md`](skills/personal-data-protection/checklists/breach-response.md) — PH row in the critical-timer table (72h from knowledge to **NPC and subjects in parallel**, annual Security Incident Report by 31 March, § 30 concealment offence).
- [`skills/personal-data-protection/templates/INCIDENT_RESPONSE.md.template`](skills/personal-data-protection/templates/INCIDENT_RESPONSE.md.template) — PH row in the statutory-clocks table, NPC portal, and PH added to the active-jurisdictions placeholder.
- [`skills/personal-data-protection/checklists/new-feature.md`](skills/personal-data-protection/checklists/new-feature.md) — PH block in the Step 8 jurisdiction review (§ 13 closed SPI list, § 16(b) objection to automated processing / profiling, § 16(e) erasure-or-blocking, § 20(f) parallel breach lane, § 34 / § 30 liability).
- [`skills/personal-data-protection/checklists/new-data-field.md`](skills/personal-data-protection/checklists/new-data-field.md) — PH bullet in the Step 9 jurisdiction check (§ 12 / § 13 lawful criteria, written or electronically signed SPI consent before processing, § 24 IRR registered processing-system description).
- [`skills/personal-data-protection/checklists/new-vendor.md`](skills/personal-data-protection/checklists/new-vendor.md) — PH row in the Step 10 jurisdiction notes (§ 21 PIC accountability with no whitelist or SCC regime, § 14 written outsourcing agreement, NPC Circular 2020-03).
- [`README.md`](README.md) — `ph-dpa` added to the jurisdiction-code list in the guardrail setup section, which had only listed four codes.

### Fixed — `scripts/pdp-check-changed-files.py`

- **Personal-data keyword scan missed the two dominant field-naming conventions.** `_` is a word character and `-` sits flush against one, so `\bemail\b` never matched `email_address`, `emailAddress`, or `email-address`. The scanner only fired on bare words and prose, silently skipping `phone_number`, `passport_number`, `nationalId`, `deleteAccount`, `auditLog` and similar. Identifiers are now split on snake_case, kebab-case, camelCase and acronym boundaries before matching.
- Date-of-birth variants `birthday`, `birth_date` and `date_of_birth` were missed by `birth(date)?`; now covered.
- `subprocess.run` had no `timeout` — a hung git process blocked the pre-commit hook indefinitely. Now bounded at 30s.
- A malformed `.pdp-compliance.json` raised a raw `JSONDecodeError` traceback; now reported as a readable config error. Unreadable config files are handled the same way.
- Jurisdiction codes from config were never validated, so a typo (`sg-pdps`) was silently accepted and yielded zero coverage. Unknown codes are now rejected, matching the existing `reviewPolicy` behaviour.
- Git failures now name the failing subcommand instead of emitting bare stderr.

### Changed — `scripts/pdp-check-changed-files.py`

- Dropped the unused `mode` read and its line in the output. The field stays valid in `.pdp-compliance.json` — it is agent-facing guidance on resolving conflicting obligations, and the script never resolved obligations. Documented as such in `README.md`.
- Output no longer hardcodes "Ask Codex"; the repo ships Claude Code, Codex, and Cursor / Copilot entry points.
- Removed an unused `sys` import (ruff F401), noted the 3.9+ requirement in the module docstring, and replaced the hand-rolled dedup loop with `dict.fromkeys`.

### Statute coverage matrix

No statute versions changed in this release; the matrix is restated in full because v0.4.0 omitted it.

| Jurisdiction | Statute version | Last verified |
|---|---|---|
| Singapore PDPA 2012 | Version in force as at 1 May 2026 (reflects 2020 Amendments) | 2026-05-02 |
| Thailand PDPA B.E. 2562 (2019) | Original 2019 Government Gazette text (PDPC Thailand English translation) | 2026-05-03 |
| Indonesia UU PDP No. 27/2022 | Original 2022 enactment (full enforcement from 17 Oct 2024) | 2026-05-03 |
| Malaysia PDPA 2010 (Act 709) | Act 709 as amended by Act A1727 (all provisions in force as at 1 June 2025) | 2026-05-04 |
| Philippines DPA 2012 (RA 10173) | RA 10173 read with the 2016 NPC IRR and operative NPC Circulars (16-03, 18-01, 2020-03, 2022-04) | 2026-05-14 |

## [0.4.0] — 2026-05-14

Adds **Philippines Data Privacy Act 2012 (RA 10173)** as the fifth populated jurisdiction. Reflects RA 10173 read with the 2016 NPC Implementing Rules and Regulations and the operative NPC Circulars (16-03 Personal Data Breach Management, 18-01 Right to Data Portability, 2020-03 Data Sharing Agreements in the Private Sector, 2022-04 Rules on the Exercise of Data Subject Rights). Vietnam PDPD now deferred to v0.5 (the full Personal Data Protection Law is in draft and is expected to replace Decree 13/2023; v0.5 will write VN content against the Law where possible rather than against a soon-superseded decree).

### Added — Philippines jurisdiction content

- [`skills/personal-data-protection/jurisdictions/ph-dpa/README.md`](skills/personal-data-protection/jurisdictions/ph-dpa/README.md) — statute version (RA 10173 + IRR + operative Circulars), critical-thresholds block (72-hour breach lane to **both** NPC and affected subjects, 31 March annual incident report, ₱5M / 6 years criminal cap for combination offences), application + extraterritorial reach notes (§ 6), engineering-view "what makes PH distinctive" mental model (§ 34 personal officer liability, § 30 concealment offence, § 35 ≥100 person aggravation, government identifiers as SPI under § 3(l)), and `What's intentionally not covered` block keeping DPO appointment / NPC registration / DPIA in scope as paperwork rather than engineering surface.
- [`skills/personal-data-protection/jurisdictions/ph-dpa/statute-map.md`](skills/personal-data-protection/jurisdictions/ph-dpa/statute-map.md) — reverse lookup keyed to RA 10173 sections, IRR sections, and NPC Circulars.
- Seven obligation files under [`skills/personal-data-protection/jurisdictions/ph-dpa/obligations/`](skills/personal-data-protection/jurisdictions/ph-dpa/obligations/) covering accountability, consent + lawful bases (§§ 12, 13), general principles + notice (§ 11 + § 18 IRR), eight data subject rights (§ 16 + NPC Circular 2022-04 + NPC Circular 18-01), security + retention + cross-border accountability (§§ 20, 21 + IRR §§ 25–29 + § 50 IRR), breach notification (§ 38 IRR + NPC Circular 16-03), and offences (§§ 25–37 with § 34 personal officer liability and § 30 concealment).

### Changed — cross-jurisdiction surfaces

- [`skills/personal-data-protection/SKILL.md`](skills/personal-data-protection/SKILL.md) — frontmatter description, jurisdiction-listing prompt, status table, and critical-thresholds table all extended to include Philippines; "all four jurisdictions" wording generalised to "all populated jurisdictions"; v0.4 milestone closed; Vietnam moved to v0.5.
- [`AGENTS.md`](AGENTS.md) — Codex / Cursor / Copilot entry point mirrored: same set of changes as `SKILL.md`.
- [`skills/personal-data-protection/jurisdictions/_index.md`](skills/personal-data-protection/jurisdictions/_index.md) — cross-jurisdiction comparison grid extended to a fifth column (lawful bases, breach window, sensitive data, penalty cap, DPO requirement, individual criminal liability, restrict-processing, object-to-ADM, portability, cross-border mechanism, operational SLAs, children's data threshold, mandatory DPIA all populated for PH); status table flips PH to ✅ populated; closing strictest-rule paragraph extended to flag PH as the highest-stakes criminal regime among the populated jurisdictions.
- [`README.md`](README.md) — "Coverage — Southeast Asia focus" table flips PH to ✅ populated and pushes VN to v0.5; "How the four statutes diverge" → "How the five statutes diverge" with all 11 rows extended to a fifth column (signup consent, sensitive data, high-risk processing / DPIA, notification toggles, account deletion, data export, pause-processing, admin reads of user data, B2B SaaS / processor, cross-border cloud storage, incident response runbook); Sources section gained a Philippines subsection (RA 10173, IRR, regulator, key Circulars, incident reporting portal); "Planned for v0.4" replaced with "Planned for v0.5 — Vietnam"; audience and status lines updated.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — NPC added to the regulator list for statute-update PRs; v0.5 milestone now lists Vietnam PDPD only.
- [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) and [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) — version bumped to **0.4.0**; descriptions extended to mention Philippines DPA.

## [0.3.1] — 2026-05-07

Adds Codex packaging and local guardrails without changing the underlying statute coverage.

### Added

- [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) — Codex plugin manifest pointing to the existing `skills/` directory.
- [`.pdp-compliance.example.json`](.pdp-compliance.example.json) — project-level jurisdiction config example for Codex / local guardrails.
- [`scripts/pdp-check-changed-files.py`](scripts/pdp-check-changed-files.py) — dependency-free changed-file tripwire for pre-commit and CI. It flags likely PDP-sensitive changes and points developers back to the skill; it does not make legal-compliance decisions.

### Changed

- [`README.md`](README.md) — Codex install notes, `.pdp-compliance.json` setup, pre-commit example, and GitHub Actions example added.
- [`skills/personal-data-protection/SKILL.md`](skills/personal-data-protection/SKILL.md) and [`AGENTS.md`](AGENTS.md) — first check `.pdp-compliance.json`; ask for jurisdictions only when project config is absent.
- [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) and [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) — version bumped to **0.3.1**.

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

[Unreleased]: https://github.com/AltByteSG/personal-data-protection-skill/compare/v0.4.1...HEAD
[0.4.1]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.4.1
[0.4.0]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.4.0
[0.3.1]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.3.1
[0.3.0]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.3.0
[0.2.2]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.2.2
[0.2.1]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.2.1
[0.2.0]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.2.0
[0.1.0]: https://github.com/AltByteSG/personal-data-protection-skill/releases/tag/v0.1.0
