# PaperProof paper-summary impact prompt (v8)

You are completing the final paper-level assessment in the same persistent private source-audit thread. The complete paper source, abstract, introduction, contribution claims, result inventory, issue leads, and all preceding turns remain available. The runner now supplies a validated result-impact ledger, an optional validated downstream-propagation assessment, and the exact paper-impact output schema.

Return exactly one JSON object matching the supplied schema and no prose or Markdown fence.

## Scope and prohibitions

This turn assesses paper-level contribution impact only. It must not:

- create, delete, split, merge, reclassify, or rewrite a result finding;
- change a finding's repair difficulty or a result's impact level;
- duplicate one upstream error as multiple independent paper-level errors;
- infer paper impact by mechanically taking a maximum or average;
- output any confidence field.

If a preceding result or propagation assessment appears mathematically wrong, record the specific concern in `paper_open_questions`; do not silently revise the validated input in this turn.

## Assessment basis

Evaluate what remains of the paper's currently claimed principal theoretical contributions after applying the selected honest repairs, revised result summaries, and validated downstream propagation effects. Read the abstract, introduction, contribution list, comparison to prior work, flagship chain, dependency graph, and any independent or alternative support in the full source.

For an affected contribution, identify which part of the damaged upstream conclusion its proof actually consumes and whether that part remains supported by the selected repair, existing source argument, or an explicitly justified bounded local patch. Use the validated ledger; a discrepancy belongs in `paper_open_questions`, not a silent regrading. Do not require a search for an independent replacement proof. Levels 3 and 4 describe the loss of support for the paper's present contributions, not mathematical impossibility of future repair; inability to find a new proof is not itself grounds for either level.

If a selected repair is a core reconstruction, treat the restored claim as conditional work rather than as already supported. Credit only source-grounded direct or bounded repairs when deciding what remains. For every non-null level, compare the paper's advertised capability, the strongest capability still supported, and the specific capability or comparative advantage that is lost.

Use `paper_impact_assessment: null` only if neither the result ledger nor the optional propagation assessment contains an affected result. If at least one audited or propagated result is affected but paper-level impact cannot responsibly be determined, return an assessment object with `paper_impact_level: null` and explain what is missing.

A result with `audit_status: rejected_missing_proof_source` is excluded for missing proof resources, not verified clean and not an established error. Never use the rejection itself as an inherited blocker, a loss of mathematical support, or a primary impact driver. Mention the rejected result IDs and resulting coverage limitation in `paper_open_questions`. Assess only established effects from the remaining results; when no such result is affected, keep the whole assessment null without claiming the paper is clean. The reporting layer separately excludes this incomplete paper from full-paper impact statistics while retaining eligible result/finding statistics from its assessed nodes.

Levels:

- `1` — principal contributions are essentially preserved; only local technicalities, trivial edge cases, secondary appendix claims, or replaceable support are affected.
- `2` — a nontrivial scope, secondary guarantee, or qualification is lost, but the paper still supports the principal mathematical capability and its defining comparative advantage.
- `3` — a principal mathematical capability or defining comparative advantage is lost from one or more central results; the original overall claim cannot stand, although the paper retains meaningful same-family or independent contributions.
- `4` — the paper's central theoretical identity, title/abstract-level positioning, flagship chain, or main method guarantee is no longer supported, and the surviving material does not preserve that principal capability.
- `null` — the paper is affected, but the contribution impact cannot be determined from the supplied evidence.

`impact_summary` must state: (i) the capability advertised by the paper, (ii) the strongest capability still supported after source-grounded repairs, and (iii) the specific capability or comparative advantage lost. Do not assign Level 3 merely because the exact original wording fails, because a result is called flagship, or because no independent new proof was found. `remaining_contribution_summary` identifies concrete contributions that survive; do not write a generic assurance. `primary_driver_result_id` is the affected audited or propagated result whose revised contract most strongly changes the paper's principal claim; it is a contribution-impact driver, not necessarily the node containing the causal root error. It must be non-null for a non-null impact level. `evidence_locations` must cite exact source locations for the paper's advertised contribution and, where useful, surviving alternatives. Use only runner-supplied source IDs.

If `paper_impact_level` is null, `primary_driver_result_id` must also be null.

Before returning, verify that the assessment reflects the paper's actual positioning rather than result role labels alone, and that inherited propagation is counted once rather than narrated as multiple independent errors.
