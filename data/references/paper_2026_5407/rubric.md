# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Gibbs form and exact update.** Derives the normalized escort optimizer through a Gibbs variational identity, a fully justified KL variational/KKT argument, or an equivalent valid method. Establishes optimality against all feasible competitors, including dismissal of infinite-objective competitors, and handles both the interior active-constraint case and the target-feasible case, including equality of the radius and target KL. Merely naming KKT or exponential tilting without deriving and justifying the optimizer does not earn full credit.
- **3 points: Escort KL geometry.** Establishes the path endpoints, derives the log-moment expectation and variance derivatives and both KL expressions, or supplies equivalent arguments. Justifies the required differentiation and endpoint continuity from the stated assumptions, proves weak and conditional strict monotonicity, and obtains the unique interior temperature. Handles P=Pi without asserting temperature uniqueness in that case.
- **3 points: Residual variance representation.** Establishes finite residual-weight second moments, proves that normalized residual-weight variance equals chi-square divergence, and derives the moment representation 1+chi-square=M(tau)M(2-tau), or an equivalent fully justified representation sufficient for the remaining claim.
- **2 points: Variance monotonicity and strictness.** Uses the log-moment convexity structure, or an equivalent valid argument, to prove nonincrease and strict decrease when P differs from Pi. Justifies any derivatives used at interior moment parameters and handles both path endpoints, including strict comparisons involving an endpoint. Merely asserting that tempering reduces variance is insufficient.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the stated assumptions. The log-moment notation and the order of the steps are not mandatory. A direct Gibbs variational comparison can replace abstract KKT theory entirely. If KKT is used, its relevant applicability and the normalized minimizer must be justified rather than assumed.

Do not require finiteness of E_P[R²|log R|] or E_P[R²|log R|²], or a finite derivative of the log-moment function at parameter two: these are not assumptions of the problem. Interior differentiation followed by endpoint continuity, or an appropriate convexity argument, is sufficient. Strict monotonicity on a closed interval does not require a nonzero derivative at its endpoints.

A failed derivation of an intermediate identity should not erase credit for a later conclusion proved independently. Missing the exact-update identification or the variance monotonicity argument is theorem-critical. All listed proof obligations are closed in the reference proof; there is no unresolved external or paper-specific dependency to treat as a completed step without justification.
