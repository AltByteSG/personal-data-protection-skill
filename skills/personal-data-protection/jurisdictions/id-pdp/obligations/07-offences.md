# BAB VIII (Pasal 57) + BAB XIII–XIV (Pasal 65–73) — Administrative Sanctions, Prohibitions, Criminal Penalties

> ⚠ **Reference material only — not legal advice.** See [DISCLAIMER.md](../../../../../DISCLAIMER.md). Verify against the official statute and consult a qualified DPO / lawyer.

UU PDP splits enforcement into **administrative sanctions** (Pasal 57), **prohibitions** (Pasal 65–66), and **criminal penalties** (Pasal 67–73). Corporate criminal liability under Pasal 70 is significantly broader than Singapore or Thailand.

## BAB VIII — Administrative Sanctions (Pasal 57)

### Pasal 57(1) — Triggering provisions

Administrative sanctions apply for violations of any of the following Pasal:

> 20(1), 21, 24, 25(2), 26(3), 27, 28, 29, 30, 31, 32(1), 33, 34(1), 35, 36, 37, 38, 39(1), 40(1), 41(1)/(3), 42(1), 43(1), 44(1), 45, 46(1)/(3), 47, 48(1), 49, 51(1)/(5), 52, 53(1), 55(2), 56(2)–(4)

That covers virtually every substantive Controller and Processor obligation.

### Pasal 57(2) — Sanction types

The regulator may impose:

a. **Written warning** (peringatan tertulis)
b. **Temporary suspension** of Personal Data processing activities
c. **Deletion or destruction** of Personal Data
d. **Administrative fine**

These are not exclusive — multiple may apply for the same violation. Sanctions (b), (c), and (d) can be operationally devastating: a temporary suspension of processing means you cannot run your service.

### Pasal 57(3) — Fine ceiling

> *"Administrative sanctions in the form of administrative fines as referred to in paragraph (2) letter d are at most **2% (two percent) of annual revenue or annual receipts** against the variable of the violation."*

**Practical effect:**
- 2% of annual revenue is the absolute cap per violation
- "Variable of the violation" — the implementing PP refines what constitutes a single violation; multiple findings in one investigation can stack
- For a small organisation: 2% of small revenue is small in absolute terms but proportional
- For a large organisation: 2% of large revenue is a significant penalty (similar in spirit to GDPR's 4% / EUR 20M ceiling, though GDPR is higher)

### Pasal 57(4) — Imposed by the regulator (lembaga)

Administrative sanctions are imposed by the regulator (lembaga) — currently administered through Komdigi pending the establishment of the dedicated Personal Data Protection authority by Presidential Regulation.

## BAB XIII — Prohibitions (Pasal 65–66)

These prohibitions establish the conduct that becomes criminal under Pasal 67–68.

### Pasal 65 — Prohibitions on use of others' data

It is prohibited to:

(1) **Unlawfully obtain or collect** Personal Data not belonging to oneself, with intent to benefit oneself or another, **in a way that may cause loss to the Data Subject**

(2) **Unlawfully disclose** Personal Data not belonging to oneself

(3) **Unlawfully use** Personal Data not belonging to oneself

### Pasal 66 — Prohibition on falsification

It is prohibited to **make false Personal Data or falsify Personal Data**, with intent to benefit oneself or another, **in a way that may cause loss to others**.

**Implementation layers:** [01 Non-technical](../../../layers/01-non-technical.md) (staff AUP), [04 Controls](../../../layers/04-controls-and-processes.md) (admin audit log).

## BAB XIV — Criminal Penalties (Pasal 67–73)

### Pasal 67 — Three-tier criminal offences

Built on the Pasal 65 prohibitions:

| Pasal 67 paragraph | Conduct | Maximum penalty |
|---|---|---|
| (1) | Intentionally + unlawfully **obtaining or collecting** another's Personal Data with intent to benefit, causing loss | **5 years imprisonment** + IDR 5,000,000,000 fine (~USD 320k) |
| (2) | Intentionally + unlawfully **disclosing** another's Personal Data | **4 years imprisonment** + IDR 4,000,000,000 fine (~USD 256k) |
| (3) | Intentionally + unlawfully **using** another's Personal Data | **5 years imprisonment** + IDR 5,000,000,000 fine (~USD 320k) |

Each paragraph allows the court to impose imprisonment, fine, or both.

### Pasal 68 — Falsification

Intentional falsification of Personal Data (per Pasal 66) carries:
- **6 years imprisonment** + IDR 6,000,000,000 fine (~USD 384k)

### Pasal 69 — Additional penalties

In addition to Pasal 67–68 penalties, the court may also impose:
- **Confiscation of profits or assets** obtained from the criminal act
- **Compensation payment** to the victim

### Pasal 70 — Corporate criminal liability (broader than SG / TH)

**Rule:** when the offence under Pasal 67–68 is committed by a **Corporation**, the penalty may be imposed on:
- Management (pengurus)
- Controlling shareholders (pemegang kendali)
- Persons giving instructions (pemberi perintah)
- Beneficial owners (pemilik manfaat)
- AND/OR the Corporation itself

**For corporations**, only fines may be imposed (Pasal 70(2)), but:

- **Fine ceiling: up to 10× the maximum** for a natural person under Pasal 67–68 (Pasal 70(3))
- For Pasal 67(1) corporate version: up to **IDR 50,000,000,000** (~USD 3.2M)
- For Pasal 68 corporate version: up to **IDR 60,000,000,000** (~USD 3.8M)

**Plus additional penalties (Pasal 70(4)):**

a. Confiscation of profits / assets from the criminal act
b. **Suspension of all or part of the Corporation's business**
c. **Permanent ban** on conducting certain activities
d. **Closure of all or part of the Corporation's business locations**
e. Mandatory performance of neglected obligations
f. Compensation payment
g. **Licence revocation**
h. **Dissolution of the Corporation**

This is significantly broader than:
- Singapore PDPA (s48D/E/F): individual criminal liability + organisational financial penalty cap
- Thailand PDPA (s79–81): individual criminal + tiered administrative fines

Indonesia is the only one of the three where a court can **dissolve the corporation** for PDP offences.

### Pasal 71–73 — Enforcement procedures

Procedural — covers payment timelines (1 month from finalisation), asset seizure if unpaid, conversion of unpaid fines to imprisonment for natural persons, business suspension for corporations.

## Mental model

Three concepts to internalise:

1. **Administrative + criminal layers stack.** Pasal 57 (administrative) and Pasal 67–73 (criminal) can both apply to the same incident. A breach that involves unauthorised disclosure for personal benefit triggers both.

2. **Corporate criminal liability is broader than peer jurisdictions.** Beyond fines, courts can dissolve the corporation. This is the strongest enforcement tool in any of the three PDP-family jurisdictions covered.

3. **2% revenue ceiling is per-violation.** Multiple findings in one investigation can stack. A single root cause that triggers violations of multiple Pasal can produce a multi-tier fine.

## Penalty cap calculation in practice

**Compared across jurisdictions:**

| Aspect | Singapore PDPA | Thailand PDPA | Indonesia UU PDP |
|---|---|---|---|
| Administrative org penalty | SGD 1M, or 10% SG turnover above SGD 10M | THB 1M / 3M / 5M tiered | **2% of annual revenue per violation** |
| Personal criminal penalty | SGD 5,000 + 2 years (s48D/E/F) | THB 500k–1M + 6mo–1yr (s79–81) | IDR 4–6 billion (~USD 256k–384k) + 4–6 years (Pasal 67–68) |
| Corporate criminal additional measures | None | None | **Suspension, ban, licence revocation, dissolution** (Pasal 70(4)) |

Indonesia's penalty surface is the broadest in absolute terms once corporate criminal liability is in play.

## Cross-references

- [02-consent.md](02-consent.md) — sensitive ("specific") data and explicit consent
- [05-care.md](05-care.md) — security measures and cross-border transfer
- [01-accountability.md](01-accountability.md) — DPO, records of processing, controller / processor duties
- [01 Non-technical](../../../layers/01-non-technical.md) — staff AUP and director / manager responsibilities
