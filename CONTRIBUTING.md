# Contributing

Thanks for your interest. Contributions of any size are welcome — typo fixes, statute updates, jurisdiction additions, real-world examples.

## What's particularly valuable

In rough priority order:

1. **Statute updates.** When PDPC (Singapore), the appointed Indonesia DPA, or PDPC (Thailand) publishes an amendment or material new guidance, open a PR updating the relevant jurisdiction file plus the [CHANGELOG](CHANGELOG.md) entry. Cite the official source and link to the regulator's announcement.
2. **Malaysia PDPA, Philippines DPA, and Vietnam PDPD jurisdiction content.** Tagged for v0.3 — see [CHANGELOG.md](CHANGELOG.md). Each needs the same shape as the existing `skills/personal-data-protection/jurisdictions/sg-pdpa/`, `th-pdpa/`, and `id-pdp/` folders: a `README.md` with statute version metadata, an `obligations/` folder mapping the statute to the universal layers, and a `statute-map.md` reverse lookup.
3. **Stack-specific implementation examples.** The layer files are deliberately stack-agnostic. Examples that show *"in a Supabase project, this principle is implemented as RLS + SECURITY DEFINER"* or *"in a Rails app, as `before_action` + Pundit"* are welcome — but please add them as labelled examples within the existing layer files, not by coupling the core text to any single stack.
4. **Incident-response notes that generalise.** If you've responded to a data incident and there's a learned pattern that would help others, the runbook template is the right home.

## Out of scope

- **Non-SEA jurisdictions.** This repo is scoped to SEA personal-data-protection statutes: SG PDPA, TH PDPA, ID UU PDP today, with MY PDPA, PH DPA, and VN PDPD planned for v0.3. GDPR, UK GDPR, CCPA, etc. are intentionally excluded — they are significantly different statutes and would dilute the skill. A separate project per jurisdiction family is a better pattern.
- **Stack-specific skills.** A "Supabase + Flutter PDP" skill belongs in its own repo (or in your project's `.claude/skills/`) using this skill as a base.
- **Promotional content** about products or services.

## How to contribute

1. **For typos / small fixes:** open a PR directly against `main`.
2. **For statute updates or jurisdiction content:** open an issue first to discuss scope and to confirm the update reflects an official change rather than personal interpretation.
3. **For new layer-file content:** open an issue first to discuss whether the content is universal enough to belong in the core layer files, or is better as a labelled stack-specific example.

### PR checklist

- [ ] Content is consistent with [DISCLAIMER.md](DISCLAIMER.md) — reference material, not legal advice; the statute is authoritative.
- [ ] Statute citations link to the official source (Singapore Statutes Online, Indonesia state gazette, Thailand RID, PDPC website, etc.).
- [ ] If updating a jurisdiction file, the `Last verified` date is bumped.
- [ ] If the change is materially new content (not a typo fix), [CHANGELOG.md](CHANGELOG.md) has an entry under `[Unreleased]`.
- [ ] Markdown lints: section headings consistent with the existing style, tables render on GitHub.

## Style

- **Tech-agnostic in the layer files.** No assumption of any specific cloud, database, or framework.
- **Engineer-readable in the obligation files.** Quote operative statute language verbatim where it's load-bearing; otherwise plain English.
- **One-line cross-references.** Layer files link to checklists, checklists link to layers and jurisdictions. Avoid duplicating content — link instead.
- **No emojis** in skill files (the repo's general style; emojis are fine in PR descriptions and issues).

## Licence

By contributing, you agree your contribution is licensed under the [MIT licence](LICENSE) — same as the rest of the repo.

## Contributor warranties and liability

By submitting a contribution to this repository, you warrant that:

1. You have authored the content yourself, or you have obtained the right to license it under the MIT licence.
2. Your contribution does not infringe any third party's copyright, trademark, trade secret, or other intellectual-property right.
3. To the best of your knowledge, the content reflects the official statute / regulator guidance as at the date of contribution and cites authoritative sources where appropriate.

You make **no warranty** as to:

- The accuracy of your contribution
- The completeness of your contribution
- The fitness of your contribution for any particular purpose
- The compliance value of your contribution for any user of this skill

You acknowledge that:

- The maintainers may accept, modify, or reject your contribution at their discretion
- Acceptance of your contribution does not constitute the maintainers' endorsement of its accuracy or legal correctness
- Once merged, your contribution is governed by the same disclaimers in [DISCLAIMER.md](DISCLAIMER.md) that apply to the rest of the repository
- **Neither the maintainers nor any individual contributor (including you) accepts liability arising from contributed content** to any third party who relies on it

## Code of conduct

Be civil. Disagreements about interpretation are expected and welcome; ad hominem is not. Maintainers reserve the right to lock or remove discussions that derail.
