# Solution

## Proof Framework

Give a concise dependency-level framework. Identify theorem-critical proof obligations rather than merely repeating final conclusions.

If several conclusions share an argument, first write:

- **Shared framework:** [common mathematical mechanism and the conclusions that depend on it].

Then describe each principal obligation in this form:

- **Core obligation A:** Establish [precise intermediate statement] by [mathematical method or standard result], then use it to derive [dependent target conclusion].

A method or result means a mathematical technique, theorem, inequality, decomposition, coupling, or representation, not an external tool. Naming a method does not complete an obligation. Expand every such item in the Full Proof by deriving the required representation and verifying all hypotheses.

This section is an outline and does not replace any derivation.

## Full Proof

Give the proof in clearly numbered steps organized by mathematical dependency. Prove shared preliminary arguments once. Every target in the public task must then be derived explicitly or identified as unproved.

For every nontrivial claim, do exactly one of the following:

1. prove it;
2. invoke a non-elementary standard background theorem, state its relevant version, map the present objects to it, and verify all task-relevant hypotheses;
3. label it as a gap and do not use it as though established.

Elementary inequalities and foundational facts may be used without restating their full theorem statements.

Do not replace a paper-specific reduction with a theorem name or an assertion that a standard framework applies. Derive the model-specific objects and verify applicability. Prioritize theorem-critical bridges over routine preliminary facts.

If the proof is incomplete, retain all valid intermediate results, label conditional conclusions, and state each unresolved claim and its downstream effects.

Use `$...$` for inline mathematics and `$$...$$` for display mathematics. Do not use `\(...\)` or `\[...\]`. Keep each prose paragraph on one physical line, with blank lines only between paragraphs, headings, lists, and display equations.

## Self-Assessment

- **Claimed score:** `0-10`
- **Possible errors or uncertain points:** Identify every theorem invocation, estimate, limit passage, regularity argument, or reduction whose justification may be incomplete; otherwise write `None`.
- **Proof components completed:** List only components whose conclusions were rigorously established.
- **Remaining gaps:** List every theorem-critical claim that remains unproved and state which final conclusions depend on it; write `None` only when every target has been proved.

The self-assessment is recorded separately and is not part of the mathematical proof.
