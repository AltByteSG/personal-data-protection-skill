# Accountability and Governance — Điều 33–37 + Decree Điều 13–16

> ⚠ **Reference material only — not legal advice.** See [DISCLAIMER.md](../../../../../DISCLAIMER.md). Verify against the official statute and consult a qualified DPO / lawyer.

## Điều 33 — Personal data protection force

The protection force comprises (Điều 33(1)): the specialised authority under the **Ministry of Public Security**; the **unit or personnel** inside each agency or organisation; **service providers**; and mobilised parties.

**Điều 33(2) — the operative duty:** every agency and organisation must **designate a unit or personnel with adequate protection capability, or engage a service provider**.

**No threshold.** Unlike MY (JPDP guideline at 20,000 subjects) or TH (core-activity test), this applies to every organisation in scope. The only relief is the Điều 38 transition for small, startup, household and micro entities — and that falls away for anyone processing sensitive data or data of a large number of subjects.

Decree Điều 13 sets the **conditions** for that personnel, Điều 14 their **duties**, and Điều 15–16 the regime for individual and organisational **service providers**.

### Decree Điều 14 — what the unit is actually responsible for

- a) Building **policies, procedures, regulations and forms** for compliance
- b) Implementing **data subject rights** operationally
- c) **Periodic self-assessment** of the organisation's compliance, as a report measuring performance against statutory obligations, proposing improvements and risk controls
- d) Preparing the **cross-border transfer impact assessment** dossier

Point (c) is worth noting: a periodic written compliance self-assessment is expected, not optional. That is an artefact to schedule, alongside the Điều 22 six-month dossier review.

**Implementation layer:** [01 Non-technical](../../../layers/01-non-technical.md), [04 Controls](../../../layers/04-controls-and-processes.md).

## Điều 37 — Responsibilities of controller, processor, and controller-processor

Điều 37(1) sets the controller's duties. The engineering-relevant ones:

- a) **State each party's responsibilities, rights and obligations in the contract** covering processing
- b) Decide the **purpose and means** of processing in the documents and agreements with the subject
- c) Apply appropriate **management and technical measures**, and **review and update them when necessary**
- d) **Notify violations under Điều 23**
- đ) **Select an appropriate processor**
- e) **Ensure the data subject rights in Điều 4**
- g) **Be liable to the data subject for damage caused by processing**
- h) **Prevent unauthorised collection of personal data from its own systems, equipment and services**
- i) Coordinate with the Ministry of Public Security and competent state agencies

Limb (h) is unusual and specific: you are responsible for stopping *others* scraping or harvesting personal data out of your product. Rate limiting, bot defence and enumeration protection on endpoints exposing personal data become compliance measures here, not just abuse controls.

Limb (đ) makes processor selection a named statutory duty — vendor due diligence is evidence, not hygiene.

**Implementation layer:** [02 Architecture](../../../layers/02-architecture.md), [04 Controls](../../../layers/04-controls-and-processes.md).

## Điều 34, 35, 36 — Standards, inspection, state management

Điều 34 covers technical standards and regulations; Điều 35 covers **inspection** of protection activities; Điều 36 covers state management responsibility. Decree Điều 31 details inspection. Engineering surface is limited — the relevant point is that inspection is a live possibility, and the artefacts it asks for are the ones named above: the filed dossiers, the policies, the self-assessment, the incident records.
