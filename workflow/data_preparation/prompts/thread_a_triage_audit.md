# Contribution Triage Audit Agent

## Mission

Independently audit the `filtered_out` triage decision returned in the preceding turn. Use the complete paper source, broad principal-contribution summary, theory inventory, and triage analysis already present in this thread.

The final result must remain a triage decision. Do not select a flagship benchmark target, do not formalize the paper, and do not perform the later theorem-by-theorem source-validity audit.

## 1. Turn Protocol

All paper source and request data remain available in this thread. Do not call tools, inspect the filesystem, or write files. The runner validates structured responses and writes repository files.

Return the complete triage self-audit and no task, reference proof, rubric, provenance, proof-reconstruction complexity assessment, benchmark suitability, or source audit.

Return only the JSON object required by the supplied response schema.

## 2. Audit The Triage Decision

Independently check that:

- the broad paper-level principal contribution was recovered faithfully from the complete source;
- the inventory distinguishes formal substantive theorem-level results from informal theoretical discussion, routine derivations, and nonmaterial results;
- the paper was classified from its actual contribution structure rather than from the existence of one attractive theorem chain;
- `paper_type`, `theory_auxiliary_subtype`, `triage_reasoning`, final `filtered_out` status, and `filter_reason` follow the Paper Triage standards supplied in the preceding turn.

For `theory_auxiliary`, check representativeness, structural closure, and genericity using the strongest coherent auxiliary theoretical component in the theory inventory.

Do not reject or rescue a paper by performing the later adversarial theorem-correctness audit. If an obvious source defect happens to be visible, it is not part of this triage-audit disposition unless it changes the structural triage classification itself.

Base the audit on mathematical content and the paper's own presentation, never on authors, institutions, venue, or solver performance.

## 3. Required Audit Record

Return `confirmed_filtered_out` when the original decision is sound. Return `corrected` when the principal-contribution summary, inventory, paper type, auxiliary subtype, status, or filter reason must change. In either case, return the complete effective triage record together with concise checks of the principal contribution, theory inventory, and classification.
