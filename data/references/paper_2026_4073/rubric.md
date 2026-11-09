# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly formulate the finite Gaussian posterior evaluation laws and use the multivariate Gaussian Rényi decomposition with K_alpha=alpha K'+(1-alpha)K. The covariance term is -log(det(K_alpha)/(det(K)^(1-alpha)det(K')^alpha))/(2(alpha-1)). Verify the positivity and common-affine-support conditions, including that the mean difference lies in the common covariance range when matrices are singular.
2. **3 points:** Derive the common-core covariance sandwich, establish positivity of the interpolated covariance in the stated alpha range, and exploit the rank-at-most-two covariance perturbation to obtain the covariance contribution bounded by 2 psi_alpha. Justify the eigenvalue interval and endpoint maximum, or provide an equivalent valid argument.
3. **3 points:** Show that the posterior-mean difference lies in the common-core RKHS and rigorously bound the interpolated-covariance quadratic form by Delta_n(r)^2 with the factor (V_n(r)+r^2)/(r^2-(alpha-1)V_n(r)). Handle support-restricted inversion and justify the finite-section RKHS inequality.
4. **2 points:** Combine the two terms, retain uniformity over neighboring datasets and finite test sequences, and correctly lift the bound to the function-valued posterior sample-path mechanism. Account for the zero-variance case and empty core, either explicitly or through conventions and an argument valid in those cases.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Standard Gaussian integration, RKHS projection facts, and a correctly stated general Rényi finite-evaluation or increasing-sigma-algebra theorem may be used without reproducing the reference proof's derivations, provided their hypotheses are checked.

An approximate-DP finite-evaluation characterization alone does not prove a path-valued Rényi-divergence bound. The lifting step requires a valid Rényi argument, such as a cylinder-algebra approximation, a suitable variational characterization, or an applicable measure-theoretic continuity theorem.

A theorem-critical omission of either the covariance or mean contribution is a major gap; merely naming a Gaussian-divergence method without deriving the required bounds earns no credit for that step. A genuinely incorrect determinant formula is not a valid Gaussian decomposition. An isolated transcription error may be treated as readily repairable only when the subsequent calculation unambiguously uses the correct formula.

Do not demand a bounded-response model, a strictly positive-definite kernel, distinct evaluation points, a unit kernel diagonal, or additional sampling assumptions. The task assumes finite V_n and Delta_n and permits singular covariance matrices. Do not require any optional added-noise mechanism, composition result, or kernel-specific sensitivity bound.
