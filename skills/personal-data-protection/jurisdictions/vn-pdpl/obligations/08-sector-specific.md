# Sector and Technology-Specific Duties — Điều 24–32 + Decree Điều 8–12

> ⚠ **Reference material only — not legal advice.** See [DISCLAIMER.md](../../../../../DISCLAIMER.md). Verify against the official statute and consult a qualified DPO / lawyer.

Vietnam is the only jurisdiction in this skill that imposes duties **by sector and technology** rather than only by lifecycle stage. Nine Law articles and five Decree articles sit here. Check this file whenever a feature falls into one of the categories below — the general obligation files do not repeat these duties.

## Law Điều 24–32

| Điều | Covers | Typical engineering trigger |
|---|---|---|
| **24** | Children; persons lacking or with limited civil act capacity | Any product usable by minors; age gates; guardian consent flows |
| **25** | Recruitment, management and use of employees | HR systems, applicant tracking, workforce monitoring |
| **26** | Health information and related business activity | Health features, symptom logging, fitness data, insurance |
| **27** | Finance, banking, credit information | Payments, lending, credit scoring, transaction history |
| **28** | Advertising services | Ad targeting, audience building, marketing segments |
| **29** | Social media platforms and online communication services | Feeds, messaging, profiles, UGC |
| **30** | **Big data, artificial intelligence, blockchain, virtual worlds** | Model training, analytics at scale, on-chain identifiers |
| **31** | **Personal location data and biometric data** | GPS, geofencing, face or fingerprint authentication |
| **32** | Data obtained from **audio and video recording in public places** | CCTV, dashcams, in-venue cameras, voice capture |

## Decree Điều 8–12 — added detail

- **Điều 8** — finance, banking and credit information activity
- **Điều 9** — **big data**: processing that contains personal data at large scale
- **Điều 10** — **artificial intelligence systems and virtual worlds**: the conditions under which personal data may be used for research and development
- **Điều 11** — **blockchain technology**
- **Điều 12** — **cloud computing**: technical and organisational measures required of the parties involved

Điều 10 and 11 are worth reading before any model-training or on-chain design decision, and Điều 12 before choosing a cloud architecture — note that a cloud region outside Vietnam is *also* a cross-border transfer under Law Điều 20(1)(c), so the two obligations stack.

## Reading order

These articles **add to** the general obligations; they do not replace them. A feature in one of these categories still needs the Điều 9 consent mechanics, the Điều 21 impact assessment, and the Điều 23 notification path. Work the general files first, then come here for the sector overlay.

## Cross-references

- Location and biometric data are also **sensitive** under Decree Điều 4(1)(đ) and (h) — see [03-purpose](03-purpose.md).
- Behaviour-tracking data on social media and online communication services is **sensitive** under Decree Điều 4(1)(l), which interacts directly with Điều 29 and Điều 30.
- Financial and transaction data is **sensitive** under Decree Điều 4(1)(k), interacting with Điều 27 and Decree Điều 8.
