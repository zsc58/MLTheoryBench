# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **3 points:** Derive the uniform empirical transition-matrix concentration bound by controlling all pair and departure frequencies on a common event, applying a union bound, and handling denominators on that event. Use the n_s-1 observed transitions with the matching normalization, justify absorbing n_s-1 into constants multiplying n_s for n_s>=2, and cover n_s=1 by a trivial bound after a permissible enlargement of C_0. Include the regularized-matrix version.
2. **2 points:** Prove the stationary-distribution perturbation estimate ||pi_Q-pi_P||_1 <= rho^{-1}||Q-P||_{row,1} <= (N/rho)||Q-P||_max using contraction on zero-sum vectors, or an equally complete valid argument. The empirical fallback rows must be stochastic, and all stationary vectors used must be probability vectors.
3. **3 points:** Establish the embedding's L1 isometry and combine concentration, the perturbation estimate, regularization bias, the explicit partition-density identification, partition approximation, and noise bias to prove the noiseless-density radius in each window. Keep vectors and functions correctly typed by applying E_N before comparing a stationary vector with a density.
4. **2 points:** Apply triangle and reverse-triangle inequalities to the two density-error events and use a union bound to prove both the false-alarm bound and the separated-density detection guarantee at threshold r_0+r_t. Preserve strict threshold crossing under the strict separation condition and do not assume independence of the windows.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The numerical values C_0=max{2C_*,exp(c_*/32)} and c_0=c_*/32 are one admissible choice, not required answers. Any valid positive constants with the stated dependencies are acceptable. The same constants must work for both regimes and must not be selected separately for each epsilon, sample size, or rho. Dependence through the given concentration constants is permitted; no additional uniformity across partitions or regime classes is demanded.

The matrix-error event alone does not imply that all departure counts are positive. A valid ratio argument obtains positivity on a joint frequency-concentration event and uses its inclusion in the matrix-error event, or otherwise handles the denominators correctly.

The embedding identity is not supplied as a public hypothesis and should be justified, though its one-line integral calculation is sufficient. A vector-minus-density expression should be interpreted only when the embedding is explicit or unambiguously established by notation.

The concentration inequality, partition approximation, and noise stability are assumed. Do not require a solver to derive them from geometric ergodicity or an operator-theoretic perturbation result. The source's fixed-N regularization-bias limit follows from uniqueness, but proving that ancillary limit is not required for the finite-sample targets. Likewise, do not require multiple-window or asymptotic results outside the frozen task.
