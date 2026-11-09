# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derive the forward KL objective as \(A(\lambda)-A(\lambda_0)-\phi(\lambda_0)^\top(\lambda-\lambda_0)\), using \(\nabla A(\lambda)=\sum_yP_\lambda(y)\gamma_y\), and obtain the appropriate first-order stationarity equations at an existing constrained minimizer. A null-space parameterization, feasible directional derivatives, or another valid method is acceptable.
- **3 points:** Deduce that \(\phi(\hat\lambda)-\phi(\lambda_0)\) is orthogonal to \(\ker(\beta_W^\top)\) and therefore equals \(t\beta_W\) for some real \(t\). The argument must remain valid for a zero probe and a zero-dimensional tangent space, either uniformly or through a local case split.
- **3 points:** Derive the complete factorized KL decomposition into the binary-concept KL weighted by the initial total pair mass and the off-target KL. Include neutral outputs and use normalization of the binary factor. The derivation must not substitute an unweighted binary KL when neutral outputs are present.
- **1 point:** Use the identification \(P_\lambda(W=w)=P_\lambda^W(w)\) and the exact logistic probe to show that the weighted concept term is constant on the constraint. Conclude that every full-KL constrained minimizer minimizes off-target KL, and state the conditional target-probability change.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Strict convexity, uniqueness of the minimizer, an inverse dual-coordinate map, and an external projection theorem are not prerequisites. A proof must not silently impose them as additional assumptions.

All output probabilities are positive. Under factorization, summing over the two members of a pair identifies its off-target probability as the pair's total mass; a neutral off-target probability is its output probability. These observations justify positivity and uniqueness of the off-target factor. A concise proof may leave these immediate well-definedness observations implicit if all logarithmic operations are valid.

The empty neutral set and the empty pair collection are covered by ordinary empty-sum conventions; do not require separate discussions when the formulas already cover them. A zero probe is permitted when the affine constraint is nonempty, in which case the constraint is the full parameter space and the dual displacement is zero. Do not require a positive or unique steering coefficient, zero off-target divergence, or unconditional target-probability change.

Deduct for treating the factorized KL decomposition or the parallel-displacement conclusion as assumptions rather than deriving them; propagate a missing stationarity or decomposition argument to the corresponding conclusion.
