# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Variational responsibility bound and tangency (2 points).** Defines current posterior responsibilities, verifies their normalization and well-definedness for finite coefficients, and derives a global variational upper bound for the negative observed log-likelihood with equality at the current iterate.
2. **Global curvature majorization (3 points).** Establishes an explicit uniform baseline-softmax Hessian bound, correctly lifts it through the coefficient score maps, and proves the global Taylor upper bound. The reference uses A_q=3I_q/4-1_q1_q^T/(2q), but a valid alternative explicit curvature bound is acceptable. A paper-specific covariance result cannot simply be asserted without derivation. The proof must cover the scalar logit cases. A direct congruence proof is acceptable in place of an explicit Kronecker lemma.
3. **Explicit separable surrogate and exact updates (3 points).** Gives the surrogate with an explicitly determined tangent constant, correct responsibility and response linear terms, and all gate and expert curvature matrices. Derives the block normal equations and closed-form updates. For singular systems, establishes that their right-hand sides lie in the curvature ranges and specifies exact minimum-norm increments or another valid exact minimizer. Expert curvature is aggregated once per observation with its responsibility weight. If ridge is used, the constructed surrogate must explicitly include centered nonnegative ridge terms; a ridge solve is not generally an exact minimizer of the unchanged unregularized surrogate. No full-rank assumption may be introduced.
4. **Monotone likelihood ascent (2 points).** Uses global majorization, tangency, and exact minimization of the surrogate actually constructed to prove L(theta^(t+1))>=L(theta^(t)) at every iteration for every realized batch. If a ridge-modified surrogate is used, its majorization and tangency must be verified for the original unpenalized likelihood.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular curvature matrix, or its choice of minimum-norm increments rather than another exact minimizer. An alternative explicit quadratic majorizer can receive full credit if all required inequalities and exact-minimization claims are established.

Do not accept omission of the parameter-dependent response-statistic linear terms, invocation of an unproved paper-specific curvature estimate, an unjustified pseudoinverse solve for a potentially inconsistent system, or a claim that an arbitrary positive ridge exactly minimizes the original surrogate. Do not demand stationary-point convergence, maximizer existence, population likelihood claims, or statistical assumptions beyond the public setup.
