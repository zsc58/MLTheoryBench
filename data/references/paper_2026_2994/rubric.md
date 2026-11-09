# Scoring Guide

- 0: No correct idea or relevant valid method.
- 1-2: Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- 3-7: Some correct core steps or conclusions, but important steps are missing.
- 8-9: Complete and essentially correct, with only readily repairable errors or omitted cases.
- 10: Fully correct.

# Core Steps

- 2 points: Correctly derives the finite-difference/inclusion-exclusion expansion of the direct imputed-gradient bias, verifies the finiteness of every coefficient used, and obtains a linear term with an O(||pi||_1^2) remainder for each fixed w. Correctly handles fixed intensities and conditional mask/imputation independence. An equivalent direct finite-pattern expansion is acceptable.
- 3 points: Proves the higher-scale mask law and correctly analyzes restoration. Distinguishes H={j}, J={j} from H={j}, J=emptyset, or gives an equivalent correct calculation. Verifies integrability of the hybrid terms using the actual linked-gradient moment assumption, establishes an O(||pi||_1^2) discrepancy from direct lower-scale imputation, and proves first-order Richardson cancellation. A valid alternative argument earns full credit.
- 3 points: Uses the stated pi-uniform conditional centered-variance and trajectory-bias bounds for the actual update estimator, derives the strongly-convex smooth biased-SGD recursion with the prescribed step sizes, and solves it with the initialization contribution controlled uniformly in pi. Obtains O(b(pi)^2)+O(1/n). The elementary component variance inequality may be shown, but is not a substitute for verifying the variance hypothesis used in the recursion.
- 2 points: Substitutes the plain and Richardson bias orders to obtain O(||pi||_1^2)+O(1/n) and O(||pi||_1^4)+O(1/n), respectively, for iterates and expected excess population loss. Preserves the fixed-w population quantifier, the separate trajectory-uniform SGD hypotheses, normalized sMAR probabilities, pi-independent constants, and zero-probability cases.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A solution that merely names Richardson extrapolation, thinning, inclusion-exclusion, or standard SGD without deriving the cancellation and recursion does not earn the corresponding step. Propagate a dependency failure only when the downstream conclusion is genuinely unsupported.

Do not accept an exact identification of the restored lower estimator with direct lower-scale imputation for an arbitrary pattern-dependent rule. Do not accept the assertion that H={j} always gives Gamma_{ {j} }: it gives g when J=emptyset. A rare multi-coordinate event alone does not bound its gradient contribution; the relevant integrability must be verified. Do not infer a uniform linked variance bound from pointwise direct-gradient moments, or a trajectory-uniform bias bound from a pointwise expansion. The task separately assumes the latter conditional bounds. Initialization-dependent constants must respect the stated pi-uniform initialization condition.
