# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Forward-KL collapse and dynamics (3 points).** Establishes strict positivity away from beta=0, uniqueness of the minimizer, and strict increase on the full interval [0,1], with a valid treatment of endpoints. Proves that every finite initial logit gives a globally defined flow, that the logit and weight decrease strictly, and that beta(t) tends to zero. A valid convexity/density-ratio argument or an equivalent proof is acceptable; positivity of the loss alone does not establish strict monotonicity or the flow limit.
2. **Responsibility leakage (1 point).** Derives the logit identity and the forward expectation bound with the factor (1/2)sqrt(beta/(1-beta)) and the Gaussian exponent -||mu_o-mu_n||_{Sigma^{-1}}^2/8. Supplies a valid overlap calculation or justified use of that Gaussian integral. Naming an overlap method without establishing the required inequality is insufficient.
3. **Reverse-KL consistency (2 points).** Justifies parameter differentiation, accounts for the vanishing derivative of normalization, and derives both displayed gradient formulas. Shows that target matching gives zero gradients and zero loss, and uses nonnegativity to establish global minimality. Does not need to prove uniqueness of the full parameter minimizer or reverse-KL flow convergence.
4. **Old-component drift bound (4 points).** Derives the exact old-mean decomposition, with the correct sign and beta Sigma^{-1} factor. If using Stein or integration by parts, verifies applicability to the logarithmic density ratio; merely naming the identity does not replace the decomposition. Derives the operator-norm inequality and both leakage bounds with their distinct weight prefactors and distinct separations: the learner pair (mu_o,m_n) for epsilon_q and the target pair (mu_o,mu_n) for epsilon_p. Explains exponential decay with fixed weights and vanishing drift with fixed covariance when both separations tend to infinity.

# Evaluator Notes

Accept any complete valid alternative proof. The point allocation totals ten and is guidance for the overall correctness bands.

Do not import a disjoint-support assumption: the task uses positive, overlapping Gaussian densities. The source's special disjoint-support example is not part of this problem. Do not require learner means to be distinct, large separation for the pointwise identities, or weights bounded away from the endpoints by a universal constant. In particular, m_n=mu_o is allowed. Forward weight optimization includes beta=0 and beta=1, while responsibility estimates with weight ratios and reverse-KL derivatives are asserted only for interior weights.

An unspecified assertion that leakage is 'exponentially small' does not establish the two quantitative bounds. Omitting weight dependence, replacing the learner separation by the target separation without justification, or asserting uniform leakage decay as weights approach zero is an error. A correct bound may exceed one and need not be clipped. Routine analytic justifications can be brief when their valid Gaussian envelopes are clear. Omission of the exact old-mean decomposition is theorem-critical. No unresolved private proof obligation is being treated as a completed scoring step.
