# Principles, Data Classification and Purpose — Điều 3, 11, 16, 18 + Decree Điều 3, 4

> ⚠ **Reference material only — not legal advice.** See [DISCLAIMER.md](../../../../../DISCLAIMER.md). Verify against the official statute and consult a qualified DPO / lawyer.

## Điều 3 — Protection principles

1. Comply with the Constitution, this Law and related law.
2. **Collect and process only within the correct scope and a specific, clear purpose.**
3. Ensure **accuracy**, correct/update/supplement when necessary; store for a period **appropriate to the processing purpose**, unless the law provides otherwise.
4. Apply institutional, technical and human measures **synchronously and effectively**.
5. Proactively prevent, detect, stop and handle violations promptly.
6. Tie data protection to national interests, socio-economic development, defence, security and foreign affairs; balance protection against the lawful rights of agencies, organisations and individuals.

Principles 2 and 3 are the ones with direct engineering consequences: purpose limitation at collection, and retention tied to purpose rather than to a fixed default.

**Implementation layer:** [03 Data model](../../../layers/03-data-model.md), [06 Disclosure](../../../layers/06-disclosure.md).

## Data classification — Decree 356/2025/NĐ-CP, Điều 3 and Điều 4

Law Điều 2(2) delegates the catalogue to Government decree. Decree 356/2025/NĐ-CP supplies both halves, and the structure matters: **sensitive is a closed list, basic is the residual**.

### Basic personal data — Decree Điều 3

1. Surname, middle name and birth name; other names
2. Date of birth; date of death or disappearance
3. Gender
4. Place of birth, birth registration, permanent residence, temporary residence, current residence, native place, contact address
5. Nationality
6. **Image of the individual**
7. Phone number, personal identification number, passport number, driving licence number, vehicle plate number
8. Marital status
9. Family relationship information (parents, children, spouse)
10. **Digital account information of the individual**
11. **Any other information tied to, or helping identify, a specific person that does not fall under Điều 4**

Item 11 makes this residual: if a field identifies a person and is not in the sensitive list, it is basic by default. There is no "not personal data" gap between the two catalogues.

### Sensitive personal data — Decree Điều 4(1)

- a) Racial or ethnic origin
- b) Political, religious or belief views
- c) **Private life, personal secrets, family secrets**
- d) Health status
- đ) **Biometric data, genetic characteristics**
- e) Sex life, sexual orientation
- g) Crime and law-violation data collected and stored by law-enforcement agencies
- h) **Location of the individual determined through positioning services**
- i) **Login name and password of an electronic identification account; images of the căn cước / căn cước công dân / chứng minh nhân dân ID cards**
- k) **Bank account login name and password; bank card information; bank account transaction history; financial and credit information; activity and transaction history in finance, securities and insurance** held at credit institutions, foreign bank branches, payment intermediaries, securities and insurance organisations
- l) **Behaviour-tracking data — use of telecommunications, social media, online communication and other cyberspace services**
- m) Other personal data that the law requires to be kept secret or strictly secured

**Four of these will catch engineers out**, because they are not sensitive in SG, TH, ID, MY or PH:

| Item | Why it surprises |
|---|---|
| **(h) location** | GPS or positioning-derived location is sensitive outright — not "sensitive when paired with identity" |
| **(i) credentials + ID images** | An identity-document upload flow is a sensitive-data pipeline |
| **(k) financial** | Transaction history and card data are sensitive, far broader than elsewhere |
| **(l) behaviour tracking** | **Ordinary product analytics** — event streams on how users use your service — is sensitive personal data in Vietnam |

Item (l) is the one to check first on any new feature. A standard analytics SDK recording screen views and taps is processing sensitive personal data under Vietnamese law.

### Decree Điều 4(2) — mandatory controls for sensitive data

When processing sensitive personal data, organisations **must establish access-limiting permission rules, processing procedures, and security measures**. This is a positive obligation, not a recommendation: RLS or equivalent, a documented processing procedure, and stated security measures.

**Implementation layer:** [03 Data model](../../../layers/03-data-model.md), [04 Controls](../../../layers/04-controls-and-processes.md).

## Điều 11, 16, 18 — Collection, publication, other processing

Điều 11 covers collection, analysis and aggregation; Điều 16 covers **publication** of personal data; Điều 18 covers other processing activities. Read Điều 16 before building any feature that makes a profile or user content publicly visible by default.

**Implementation layer:** [05 Feature/UX](../../../layers/05-feature-ux.md), [06 Disclosure](../../../layers/06-disclosure.md).
