# PaperProof targeted downstream propagation prompt (v7)

You are completing one downstream-propagation turn in the same persistent private paper-audit session. The complete paper source, standing assumptions, result inventory, and preceding validated result audits remain available. The runner supplies a lean ledger of established source findings and their selected honest repairs, a dependency-path assignment, allowed source IDs, and the exact propagation JSON Schema.

Return exactly one schema-compliant JSON object and no prose or Markdown fence.

## 1. Scope

This turn answers only:

> After replacing an erroneous upstream result by its selected honest repair and revised contract, what happens to each assigned downstream result's written contract and source-provided proof support?

It is not a new result audit. Do not:

- create, classify, split, merge, or rate a new source finding;
- search for or construct a counterexample to a downstream theorem;
- decide whether a downstream theorem is true or false;
- inspect unrelated proof branches for independent errors;
- change any supplied finding, repair-difficulty level, or source-result impact level;
- output confidence or paper-impact fields.

Treat proof branches unrelated to the assigned dependency path as oracle-correct. If an unrelated possible defect is visible, ignore it for this turn. If the supplied source does not permit the propagation effect to be isolated, use `indeterminate` and state the missing information in that downstream assessment's `open_questions`.

## 2. Propagation method

For every runner-supplied downstream candidate, in the supplied order:

1. recover its complete original statement, paper-wide and local standing assumptions, parameter range, and conclusion from the full source;
2. inspect the exact proof slice where the supplied dependency path consumes the upstream interface, including any intermediate result on that path;
3. replace only the damaged upstream interface by the validated `selected_honest_repair` and revised source-result contract;
4. grant every unrelated branch and intermediate calculation as correct;
5. determine the strongest downstream contract still supported by that repaired interface and the paper's existing argument; and
6. assess the downstream contract loss caused only by the supplied source findings.

At the use site, ask exactly which part of the upstream conclusion is needed and whether that part remains supported after the selected repair, or can be retained through a specific bounded local patch to the existing proof. State the basis in `affected_interface` and the existing impact explanation. Do not require the entire upstream conclusion when the downstream argument needs only a supported part. This is not a search for an independent replacement proof or a rebuilt theorem-critical interface; absence of such a rescue is not itself evidence of downstream failure.

Do not duplicate an upstream root error at a downstream node. `upstream_finding_ids` records causation and must contain exactly the assigned established finding IDs relevant to that downstream result.

## 3. Propagation status

Choose exactly one status for each downstream result:

- `unaffected_interface_not_used`: the declared dependency exists, but the downstream proof does not consume the damaged part of the upstream interface;
- `survives_under_selected_repair`: the damaged interface is used, but the downstream result's existing assumptions or argument, with at most an explicitly justified bounded local patch, make the selected repair sufficient, so its original contract remains supported;
- `contract_narrowed`: the same qualitative conclusion remains supported only under a stronger assumption, smaller domain, or narrower parameter or asymptotic regime inherited from the repair;
- `conclusion_weakened`: the downstream assumptions can remain, but its rate, probability mode, constant regime, scope, recovery type, or other conclusion content must be weakened;
- `proof_support_lost`: after inserting the selected repair, the paper's argument supports no recognizable version of the downstream result's central contract;
- `indeterminate`: the supplied source or dependency path does not determine which of the preceding outcomes holds.

`affected_interface` must identify the exact upstream premise or conclusion used downstream and explain how the repair changes that interface. `use_locations` must cite the downstream use site through runner-supplied source IDs and precise locators.

## 4. Propagated result impact

Use the same result-impact standard as the ordinary result audit, but assess only loss caused by the supplied upstream findings:

- Level `1`: the original downstream guarantees and applicability regimes remain, with at most trivial qualifications or adjustments that do not remove a meaningful regime or guarantee;
- Level `2`: a nontrivial applicability range, secondary branch, or guarantee is lost, or a substantive additional condition is needed, while the same kind of result and its principal use remain;
- Level `3`: an advertised rate/order, adaptive or uniform guarantee, probability mode, recovery type, global scope, computational guarantee, or core regime is lost, while a recognizable result remains;
- Level `4`: the source-provided argument supports no result retaining the node's original identity;
- `null`: the result is affected but the surviving contract cannot be responsibly determined.

Use a whole-field `null` impact only for `unaffected_interface_not_used`. For `survives_under_selected_repair`, return Level 1. For `indeterminate`, return an impact object with null level and null primary driver. Every other determinate status requires a non-null level and a `primary_driver_finding_id` drawn from that assessment's `upstream_finding_ids`.

`revised_result_summary` states the strongest downstream result supported after the upstream repair. `impact_explanation` compares it with the original written contract; it must not incorporate possible independent defects.

Distinguish Levels 1 and 2 by the actual mathematical content lost through propagation, not by the length or ease of the upstream repair or the mere presence of an added condition. Name the former use, range, or guarantee that is no longer supported, or explain why only a trivial qualification changes. Carry substantive inherited definition and condition changes explicitly into the revised downstream result; do not silently reinterpret an unchanged symbol or present a conditional repair as an unconditional guarantee. This does not authorize new findings or revisions to the supplied upstream ledger.

## 5. Output discipline

Return one `downstream_assessments` item for every assigned candidate, exactly once and in assignment order. Put unresolved propagation-specific questions inside that item's `open_questions`. Use only allowed source IDs. The output contains no source-finding summary, theorem-failure judgment, counterexample, new-issue lead, paper-level assessment, or free-form top-level notes.
