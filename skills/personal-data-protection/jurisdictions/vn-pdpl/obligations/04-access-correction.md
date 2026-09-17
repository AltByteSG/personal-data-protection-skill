# Data Subject Rights — Điều 4, 13, 14, 15, 17

> ⚠ **Reference material only — not legal advice.** See [DISCLAIMER.md](../../../../../DISCLAIMER.md). Verify against the official statute and consult a qualified DPO / lawyer.

Điều 4 enumerates the rights; Điều 13–17 give the operative mechanics for correction, deletion, provision and transfer.

## Điều 4(1) — Rights of the data subject

- a) To **know** about the processing of their personal data
- b) To **consent or refuse**, and to request **withdrawal** of consent
- c) To **view, correct, or request correction** of their personal data
- d) To request **provision**, **deletion**, or **restriction** of processing; and to submit an **objection** to processing
- đ) To **complain, denounce, sue**, and claim **compensation** under the law
- e) To require the competent authority, or parties involved in processing, to apply protection measures

**Note the shape:** viewing and correction sit together in (c), and provision, deletion, restriction and objection sit together in (d). The right to **object** is explicit — unlike SG and MY, where it is only implicit via consent withdrawal.

Điều 4(2) also imposes **duties on the subject** (protect their own data, respect others', provide accurate data, comply with the law) — unusual among the regimes in this skill, and Điều 4(3)(b) bars the subject from obstructing the controller's lawful performance. This does not reduce your obligations; it is context for disputes.

Điều 4(4) requires organisations to **facilitate** the exercise of rights and not obstruct it.

**Implementation layer:** [05 Feature/UX](../../../layers/05-feature-ux.md), [04 Controls](../../../layers/04-controls-and-processes.md).

## Điều 13 — Correction of personal data

The correction right in Điều 4(1)(c) is operationalised here. Build a self-service edit surface where the field allows it, and a documented channel where it does not.

## Điều 14 — Deletion, destruction, de-identification

Điều 14 is the longest of this group and covers all three disposal routes. Read with **Điều 2(1)**: once de-identified, the data is **no longer personal data**, which makes de-identification a genuine exit from scope rather than a risk-reduction measure.

**Operationalisation:** account deletion should decide, per table, between hard deletion, destruction, and de-identification — and de-identification must be irreversible, because **Điều 7 prohibits re-identification**.

**Implementation layer:** [03 Data model](../../../layers/03-data-model.md), [07 Operational](../../../layers/07-operational.md).

## Điều 15 — Provision of personal data

The access/export right in Điều 4(1)(d). The export must cover **all** personal data held about the subject — a new field added anywhere must reach the export path.

## Điều 17 — Transfer of personal data

Transfer between parties within Vietnam. Distinct from **Điều 20**, which governs transfer across the border — do not conflate them; only Điều 20 carries the 60-day filing duty.

**Implementation layer:** [02 Architecture](../../../layers/02-architecture.md).
