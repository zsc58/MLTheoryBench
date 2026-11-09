# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **RKHS representer identification (2 points).** Correctly uses the reproducing property and the kernel integral operator to express the expected score functional as \(\langle f,S_{q_\phi,k}(s_p-s_{q_\phi})\rangle_{\mathcal H}\). Justifies that the representer is an RKHS element using the stated operator domain and integrability assumptions, rather than treating pointwise integrability as sufficient.
2. **Exact lower-level optimization (3 points).** Solves the Hilbert-space quadratic maximization, establishes uniqueness, derives the representer-form optimizer, and derives the optimum's equality with squared KSD from the unit-ball definition. Handles the zero-representer case without dividing by zero.
3. **Conditional-score projection (3 points).** Derives, rather than merely names, the replacement of the marginal-score representation by the joint conditional-score representation using differentiation of the mixture and the conditional score formula. Justifies integration using the stated first-moment condition. A proof working directly with score differences is valid and avoids unnecessary separate integrability assumptions on the two scores.
4. **Tractable pairwise form and final equivalence (2 points).** Expands the squared RKHS norm with independent conditional pairs and justifies absolute integrability to obtain the displayed kernel-score expectation. Correctly concludes equality of the outer optimization objectives and explains Monte Carlo estimability using the stated sampling and evaluation access. Does not assume an outer minimum is attained or claim a variance guarantee without additional hypotheses.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A claimed use of a score-projection or representer theorem without the corresponding derivation does not earn the associated step's substantial credit. Propagate a missing representer or projection dependency only insofar as later conclusions are unsupported; independently correct later algebra should receive its earned credit.

A concise, correct justification of Hilbert-valued integration is sufficient; do not require a separate reproduction of the reference proof's separability argument. The kernel need not be strictly positive definite, and zero kernels and zero discrepancies remain admissible. Do not require Stein integration by parts, kernel derivatives, Gaussian conditionals, optimization convergence results, finite Monte Carlo variance, or an existence proof for an outer minimizer. All theorem-critical reference-proof obligations are closed; there is no unresolved private dependency.
