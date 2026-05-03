# Jurisdictions Index

> ⚠ **Reference material only — not legal advice.** See [DISCLAIMER.md](../DISCLAIMER.md). Verify against the official statute and consult a qualified DPO / lawyer.

This skill covers Singapore PDPA, Thailand PDPA, and Indonesia UU PDP today, with Malaysia PDPA, Philippines DPA, and Vietnam PDPD planned for v0.2.

| Jurisdiction | Code | Status |
|---|---|---|
| Singapore PDPA 2012 (post-2020 Amendments) | [`sg-pdpa`](sg-pdpa/) | ✅ Populated |
| Thailand PDPA B.E. 2562 (2019) | [`th-pdpa`](th-pdpa/) | ✅ Populated |
| Indonesia UU PDP No. 27/2022 | [`id-pdp`](id-pdp/) | ✅ Populated |
| Malaysia PDPA 2010 (with 2024 Amendments) | `my-pdpa` | 🚧 Planned for v0.2 |
| Philippines Data Privacy Act 2012 (RA 10173) | `ph-dpa` | 🚧 Planned for v0.2 |
| Vietnam PDP Decree 13/2023/ND-CP | `vn-pdpd` | 🚧 Planned for v0.2 |

## Cross-jurisdiction comparison

| | Singapore PDPA | Thailand PDPA | Indonesia UU PDP |
|---|---|---|---|
| **In force since** | 2014 (orig); 2020 Amendments commenced 2021 / 2022 | 1 Jun 2022 (delayed twice from 2019 enactment) | 17 Oct 2024 (2-year transition from 17 Oct 2022 enactment) |
| **Lawful bases** | Consent + 1st/2nd Sch enumerated cases | 6 GDPR-style bases (s24) | 6 GDPR-style bases (Pasal 20(2)) |
| **Breach notification window** | **3 calendar days** to PDPC after assessment (s26D(1)) | **72 hours** to PDPC from awareness (s37(4)) | **72 hours** from awareness — to **both** subject AND regulator (Pasal 46(1)) |
| **Sensitive data** | Deemed-significant-harm categories per PDP NDB Regulations 2021 | Broad list (s26): racial, ethnic, political, religious, sexual behavior, criminal, health, disability, trade union, genetic, biometric | "Specific" Personal Data category (Pasal 4) — scope refined by implementing PP; typically health, biometric, genetic, criminal records, children's data, financial |
| **Penalty cap (org)** | SGD 1M / 10% SG turnover (s48J(3)) | THB 1M / 3M / 5M tiered (s82–84); plus criminal up to THB 1M / 1 year (s79) | **2% of annual revenue per violation** (Pasal 57(3)); plus corporate criminal — fines up to 10× of natural-person max + suspension / **dissolution** (Pasal 70) |
| **DPO requirement** | Always (s11) | For (1) public authorities, (2) large-scale regular monitoring, (3) core sensitive-data activity (s41) | For (1) public-interest processing, (2) large-scale regular monitoring, (3) core sensitive-data or criminal-records processing (Pasal 53) — same shape as TH |
| **Individual criminal liability** | Yes — s48D/E/F (knowing/reckless disclosure, misuse, re-identification) — SGD 5,000 / 2 years | Yes — s79 (sensitive-data misuse), s80 (duty-holder disclosure), **s81 (director / manager omission)** broader than SG | Yes — Pasal 67 (4–5 years + IDR 4–5B), Pasal 68 (6 years + IDR 6B); corporate criminal liability (Pasal 70) extends to dissolution |
| **Right to restrict processing** | Not in PDPA | Yes (s34) | Yes (Pasal 11) — 72-hour SLA |
| **Right to object to automated decision-making** | Not explicit | Implicit via consent withdrawal | Yes — explicit standalone right (Pasal 10) |
| **Within-affiliate transfer mechanism** | Sub-processor DPA / contractual binding clauses | s29 PDPC-certified Personal Data Protection Policy (BCR-equivalent) | Pasal 56 3-tier hierarchy: adequacy → adequate-and-binding safeguards → consent |
| **Operational SLAs (correction / access / withdrawal / restrict)** | "As soon as reasonably possible" (PDPC guidance: 30 days for access) | Generally per request | **3 × 24 hours (72h)** for correction (Pasal 30), access (Pasal 32), stop on consent withdrawal (Pasal 40), suspend / restrict (Pasal 41) — most aggressive of the three |
| **Children's data threshold** | 13 (under-13 cannot give valid consent); applications often gate at 16 | s20 — under 10 requires parental consent; 10+ minors handled per Civil and Commercial Code | Pasal 25 — children's processing requires parental / guardian consent (age threshold per other Indonesian law) |
| **Mandatory DPIA** | Not statutory; PDPC guidance recommends | Not statutory | Yes — Pasal 34 with 7 enumerated triggers (similar to GDPR Art. 35) |

When operating in multiple jurisdictions, **the strictest rule applies in each dimension**. Singapore's 3 calendar days for breach notification beats Thailand's and Indonesia's 72 hours from awareness; Indonesia requires notifying the Data Subject in **all** breaches (vs Singapore's significant-harm and Thailand's high-risk thresholds); Indonesia's 72-hour SLAs for routine subject-rights requests is the most aggressive operational pressure of the three.

## Choosing your active jurisdiction(s)

Active jurisdiction is determined by **where the application's users are located**, not where the company is registered. Many applications need to comply with multiple regimes simultaneously:

- App operated by a Singapore company, used by users in Singapore only → SG PDPA
- App operated by a Singapore company, used by users in SG + ID + TH → all three
- App operated by an Indonesian company, used only by Indonesian users → ID PDP

When in doubt, treat all jurisdictions where you actively market or accept users as in-scope.
