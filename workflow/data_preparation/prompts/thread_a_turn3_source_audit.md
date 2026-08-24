# Theorem Source Audit And Target Gate Agent

## Mission

A correctness-blind ranking of flagship chains was frozen in the preceding turn. Recover the full source statements and proofs of the paper's theoretical results and audit their correctness so that the runner can choose the highest-ranked unblocked chain.

The chain definitions, scores, and ranking are frozen. Source correctness must not change or rescore them.

## 1. Turn Protocol

The complete source, triage analysis, theory inventory, and frozen flagship selection remain available in this thread. Do not call tools, inspect the filesystem, or write files.

Return only the JSON object required by the supplied response schema. Set the protocol field `status` to `audited`; the runner derives the target gate from the material records rather than from this field.

## 2. Recover The Theoretical Material

Recover and audit:

- every `theory_candidate` in the triage inventory; and
- every `internal_support` item needed by those candidates.

For each such result, return to the complete source and recover its full mathematical contract and source-grounded proof reconstruction before assigning any audit status. The triage summaries are locators and overviews, not substitutes for the source statement or proof.

Use the inventoried `definition` and `external` items when recovering assumptions, notation, and proof dependencies. Recover their exact task-relevant content and source spans. Classify each external result as genuinely standard independent background or as a nonstandard external dependency.

If the source reveals a necessary internal result, definition, or external dependency omitted from the triage inventory, record it as an added material item with a new stable identifier and explain why it is required.

## 3. Source Statement Audit

For each audited result, recover the intended theorem contract from the full source, including standing assumptions, definitions, scope conventions, inherited hypotheses, parameter regimes, and surrounding statements.

Do not diagnose a missing assumption merely because it is not repeated in the local theorem environment when the full source clearly makes it part of the theorem contract.

Record `statement_status` as `clean`, `minor_issue`, or `major_issue`.

- `clean`: the statement is mathematically well specified under the recovered full-source contract.

- `minor_issue`: the source contains a genuine local statement defect, but the repair is local, unambiguously source-grounded, claim-preserving in substantive mathematical content, and unique or nearly unique from the source context. The repair must not materially strengthen substantive assumptions, weaken the intended conclusion, restrict the intended regime, change the convergence mode, or redesign the theorem.

- `major_issue`: the statement cannot be made correct and precise without a substantive change to assumptions, conclusion, regime, quantifiers, convergence mode, or other mathematical content; the intended repair is materially ambiguous; or a valid counterexample applies under the recovered source assumptions.

### Source-local statement-error rescue

Some defects that would otherwise satisfy the `major_issue` criteria may arise only from an evident source-local notation mix-up, symbol misuse, transcription error, or similarly local statement mistake that makes the theorem literally false as written.

Before assigning `major_issue`, check whether the defect is instead an evident source-local statement error. Classify it as `minor_issue`, and continue the subsequent proof audit using the uniquely recovered correct interpretation of the theorem, only if all of the following hold:

1. **Source-grounded intended form.** The surrounding source already provides a unique or nearly unique corrected formulation, for example through preceding lemmas, intermediate bounds, the proof immediately before the defective step, or later uses of the theorem.
2. **No new mathematics.** The corrected statement follows from the existing proof under exactly the same substantive assumptions and proof architecture. No new lemma, estimate, structural assumption, case analysis, or theorem-specific idea is needed.
3. **Downstream consistency.** Subsequent results and applications are compatible with the corrected formulation without changing their assumptions or proof logic.

For every `minor_issue`, record the original source clause, the repaired statement, the source evidence, and why the repair preserves the claim.

## 4. Source Proof Audit

Audit each source proof under a deliberately permissive standard appropriate for research-paper writing.

The purpose is to determine whether the theorem-critical argument is substantively valid, not whether every intermediate step is written out.

Actively complete omitted derivations, compressed standard arguments, routine calculations, and analogous cases from the source assumptions, earlier results, and standard independent background.

If a missing derivation can be completed without changing the theorem or introducing a new paper-specific mechanism, treat the source proof as `clean`.

Paper-internal earlier results that carry a material part of the proof closure must themselves be checked; only genuinely standard independent background may be treated as a black box.

Record `proof_status` as `clean`, `minor_error`, or `major_gap`.

- `clean`: the theorem-critical proof closes after allowing normal research-paper compression and completing omitted but derivable steps.

- `minor_error`: a stated proof step is locally incorrect, but a local source-grounded repair establishes the same required conclusion without changing the theorem, adding a substantive assumption, or changing the principal proof architecture.

- `major_gap`: a specific theorem-critical step cannot be established from the source assumptions and proof closure after a serious completion attempt, and repairing it would require a new substantive paper-specific argument or leaves the truth of the result materially unresolved.

Inability to reconstruct a proof immediately is not itself evidence of a `major_gap`. A `major_gap` requires a concrete theorem-critical failure or unresolved bridge. However, if the source supplies, inherits, or identifies no recoverable proof closure for an audited result, record `major_gap`.

If an audited result depends on another result whose statement has `major_issue` or whose effective proof status is `major_gap`, the dependent result's effective proof status is also `major_gap`. If the source instead provides an independent valid proof route, correct the `depends_on` relation before applying this rule and record the source evidence for that correction.

For every `minor_error`, record the incorrect source step, the local repair, the source evidence, and why the repair preserves the conclusion and proof architecture.

Record source issues for all candidates. An issue blocks only the ranked chains whose selected candidates or proof-dependency closures contain that issue.

## 5. Ranked-Target Blocking Gate

Each ranked flagship chain is blocked when:

- a selected `theory_candidate` has `statement_status = major_issue` or effective `proof_status = major_gap`; or
- any `theory_candidate` or `internal_support` item in its transitive proof-dependency closure has a blocking statement or proof defect that prevents the selected conclusion from closing.

Minor source issues do not block the target when their local source-grounded repairs satisfy the criteria above.

The runner considers every chain with `CF_total >= 8` in the frozen order and selects the first unblocked chain. A blocked higher-ranked chain is recorded but does not prevent a lower-ranked eligible chain from proceeding. When every ranked chain is blocked, the runner maps the confirmed source result to pipeline status `stopped` with reason `paper_issue`.

## 6. Required Source-Audit Record

Return one material record for every inventoried or newly added item.

For each `theory_candidate` and `internal_support` item, record:

- its complete recovered statement;
- its source-grounded proof reconstruction;
- `statement_status` and `proof_status`;
- concrete statement and proof findings;
- separate statement and proof repairs when applicable;
- updated human-readable source spans;
- exact inclusive line ranges for the original statement and its proof in the supplied line-numbered source.

Use `statement_source_locations` for the theorem statement and inherited local assumptions. Use `proof_source_locations` for the displayed proof, appendix proof, proof sketch, or the source line that explicitly omits or delegates the proof. These locations are operational: a later correction turn may receive only the cited lines, so make every range accurate and sufficiently complete. For `definition` and `external` items, record statement locations and leave proof locations empty. A paper-internal proved result needed by a selected chain must instead be represented as `internal_support`.

For each `definition` and `external` item, record its exact task-relevant content and updated source spans. For an external item, also record whether it is `standard_independent` or `nonstandard_dependency`.

The `theory_candidate` classification is frozen after target selection. You may correct the role of a non-candidate supporting item when the full source shows that the shallow triage classification was wrong.

Before returning, verify that each ranked chain has a complete recursive proof closure. Its candidate records must link every statement-essential definition, primitive assumption, paper-internal supporting result, and nonstandard external dependency used by the recovered proof. Add omitted material and repair missing or incorrect `depends_on` links now; the source-blind compiler cannot recover them later.

Do not repeat the principal-contribution analysis, target-selection reasoning, fidelity assessments, or other fields already recorded in the preceding turns. The runner combines the turn outputs by stable material identifier.
