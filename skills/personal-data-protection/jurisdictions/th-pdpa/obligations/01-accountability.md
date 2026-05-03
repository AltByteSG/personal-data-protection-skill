# Chapter I + Section 37, 39, 41–42 — Accountability, Controller / Processor Duties, DPO

> ⚠ **Reference material only — not legal advice.** See [DISCLAIMER.md](../../../../../DISCLAIMER.md). Verify against the official statute and consult a qualified DPO / lawyer.

## Section 37 — Data Controller duties

The Data Controller has five enumerated duties:

### (1) Security measures

**Rule:** *"provide appropriate security measures for preventing the unauthorized or unlawful loss, access to, use, alteration, correction or disclosure of Personal Data, and such measures must be reviewed when it is necessary, or when the technology has changed in order to efficiently maintain the appropriate security and safety. It shall also be in accordance with the minimum standard specified and announced by the Committee."*

**Implementation layer:** [02 Architecture](../../../layers/02-architecture.md), [04 Controls](../../../layers/04-controls-and-processes.md).

PDPC Thailand has issued subordinate notifications specifying the minimum security standard — verify the current text at [pdpc.or.th](https://www.pdpc.or.th) for the binding details.

### (2) Onward-disclosure protection

**Rule:** when Personal Data is provided to other persons, the Data Controller must take action to prevent unlawful or unauthorised use / disclosure by those recipients.

**Implementation layer:** [01 Non-technical](../../../layers/01-non-technical.md) (vendor contracts), [04 Controls](../../../layers/04-controls-and-processes.md) (sub-processor dispatch sanitisation).

### (3) Erasure / destruction system

**Rule:** put in place an examination system for erasure or destruction of Personal Data when:
- The retention period ends, OR
- The Personal Data is irrelevant or beyond the necessary purpose, OR
- The data subject requests erasure, OR
- The data subject withdraws consent (and there's no other lawful basis).

Exceptions: freedom of expression, archival/research under s24(1) or (4), public-health under s26(5)(a)/(b), legal claims, legal compliance.

**Implementation layer:** [04 Controls](../../../layers/04-controls-and-processes.md) (retention sweeps).

### (4) Breach notification — 72 hours

See [06-breach-notification.md](06-breach-notification.md).

### (5) Designate Thai representative (for non-Thai controllers)

**Rule:** controllers outside Thailand serving Thai users (per s5 paragraph 2) must designate **in writing** a representative in the Kingdom of Thailand, authorised to act on behalf of the Data Controller without limitation of liability.

**Implementation layer:** [01 Non-technical](../../../layers/01-non-technical.md).

Exception (s38): does not apply to public authorities or to small operations not handling sensitive data and not handling large-scale data per the s41(2) threshold.

## Section 39 — Records of Processing Activities

**Rule:** the Data Controller must maintain records (paper or electronic) covering at minimum:

1. The Personal Data collected
2. The purpose of collection per category
3. Details of the Data Controller
4. Retention period
5. Rights and methods for access; conditions of access
6. Use or disclosure under s27 paragraph 3
7. Records of rejected access / objection / accuracy requests (s30, s31, s32, s36)
8. Explanation of security measures under s37(1)

**Implementation layer:** [03 Data model](../../../layers/03-data-model.md), [04 Controls](../../../layers/04-controls-and-processes.md).

**Small organisation exception:** items (1), (2), (3), (4), (5), (6), and (8) may not apply to small organisations — UNLESS the processing is likely to result in a risk to rights and freedoms, OR the processing is non-occasional, OR the processing involves sensitive data (s26). Items (7) always apply.

The "small organisation" threshold is defined by PDPC notification — verify current text.

## Section 40 — Data Processor duties

The Data Processor has three enumerated duties:

1. **Process only on the Data Controller's instructions** (except where instruction is contrary to law / PDPA)
2. **Provide appropriate security measures** AND **notify the Data Controller of any breach**
3. **Maintain records of processing activities** per Committee rules

**Critical:** if the Data Processor fails to comply with (1) — i.e. processes data outside the Data Controller's instructions — **the Data Processor is regarded as the Data Controller** for that processing. This shifts liability significantly.

The Data Controller must prepare a written agreement with the Data Processor controlling the activities. **Implementation layer:** [01 Non-technical](../../../layers/01-non-technical.md) (DPAs).

## Section 41 — DPO designation

**Rule:** the Data Controller AND the Data Processor must designate a Data Protection Officer (DPO) in the following circumstances:

1. **Public authority** as prescribed and announced by the Committee
2. **Large-scale regular monitoring**: activities require regular monitoring of Personal Data or systems by reason of large volume (threshold prescribed by Committee)
3. **Core activity is sensitive data** (s26)

**Joint DPO:** affiliated businesses or groups under a s29 PDPC-certified Personal Data Protection Policy may share a single DPO, provided each establishment can easily contact them.

**Public disclosure:** the Data Controller and Data Processor must publish the DPO's contact information so that data subjects and the Office can reach them about collection / use / disclosure and the exercise of rights.

**Implementation layer:** [01 Non-technical](../../../layers/01-non-technical.md).

## Section 42 — DPO duties

The DPO must:

1. **Advise** the Data Controller / Processor (and their staff and service providers) on PDPA compliance
2. **Investigate** the Data Controller / Processor's compliance with the Act in the collection / use / disclosure of Personal Data
3. **Coordinate with the Office** when problems arise
4. **Keep confidentiality** of Personal Data acquired in the course of duty

**DPO protections:**
- The Data Controller / Processor **must not dismiss** the DPO by reason of performing duties under the Act
- The DPO must be able to **report directly to the chief executive** of the Data Controller / Processor
- The Data Controller / Processor must provide adequate tools and access for the DPO to perform duties

**Conflict of interest:** the DPO may have other duties, but the Data Controller / Processor must warrant to the Office that those duties don't conflict with PDPA performance.

The DPO may be an employee or a contracted external service provider.

## Chapter I — Personal Data Protection Committee (s8–18)

The PDPC is the regulator. Composition and powers are governance-level — not directly relevant to compliance implementation. Engineers should know:

- The PDPC has the power to issue notifications that bind Data Controllers and Processors (e.g. defining "small organisation," "large amount," sensitive-data sub-categories, security minimum standards, breach-notification rules)
- The Committee can prescribe forms and statements for consent
- Subordinate notifications continue to be issued — verify current text at [pdpc.or.th](https://www.pdpc.or.th)

## Penalty exposure (this Part)

| Failure | Maximum administrative fine | Source |
|---|---|---|
| Fails to notify per s37 (general) | THB 3M | s83 |
| Fails to notify per s37 involving sensitive data | THB 5M | s84 |
| Fails to maintain records under s39 | THB 1M | s82 |
| Fails to designate DPO under s41 | THB 1M | s82 (controller) / s85 (processor) |
| DPO performance failures under s42 paragraph 2/3 | THB 1M | s82 / s85 |
| Failure to designate Thai representative (s37(5)) | THB 3M | s86 (when applies to processor via s38) |

Plus s81 personal liability for directors / managers whose instructions or omissions led to the offence.
