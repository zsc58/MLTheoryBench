# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly conditions on \(\sigma(S)\) to derive \(\mathbb E[\ell(S,Y)]=\mathbb E[d_\ell(S,C)]+\mathbb E[E_\ell(C)]\).
- **4 points:** Correctly derives the feature-level decomposition of \(\mathbb E[E_\ell(C)]\), including the conditional-law tower identity \(C=\mathbb E[Q\mid\sigma(S)]\), and combines the identities into the stated three-term formula.
- **3 points:** Under strict propriety, proves both directions of the equivalence between zero expected grouping loss, \(C=Q\) almost surely, and existence of a \(\sigma(S)\)-measurable version of \(Q\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that merely asserts the chain identity or the sufficiency equivalence without deriving its required conditional-expectation and strict-propriety steps does not earn the corresponding core-step credit.

The task does not assume finite expected score loss. In assessing the first two core steps, verify that conditioning and expectation splitting are justified for the stated domain and do not use undefined infinity-minus-infinity expressions. A finite lower shift of the loss and boundedness of generalized entropy provide one valid justification: propriety at point-mass truths bounds the loss below, and comparison with any fixed prediction bounds generalized entropy above. Accept other valid justifications, including appropriately justified localization or truncation. Do not require the reference proof's particular constants or the separate presentation of these estimates. A proof that adds a finite-risk assumption without treating the remaining case does not establish the full task; assess a readily repairable omitted domain justification under the 8-9 guidance rather than treating it as a new theorem requirement.

Measurability of s ensures \(\sigma(S)\subseteq\sigma(X)\). Conditional label laws may be handled coordinatewise using conditional expectations of bounded label indicators. It is not necessary to construct a regular conditional distribution on the feature space or to reprove elementary conditional-expectation facts. Equalities of conditional laws and their versions are almost-sure equalities.

Do not impose positivity of label probabilities, interior-valued predictions, continuity or differentiability of the loss, nonnegative loss values, calibration of S, or a nonconstant score. The real-valued loss domain is the entire probability simplex. The proof must remain valid in degenerate cases allowed by this setup. Strict propriety is needed for the zero-grouping characterization, not for the decomposition.
