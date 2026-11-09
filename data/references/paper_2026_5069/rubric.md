# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points — Oracle validity and cross-fitting.** Establish oracle-score centering using MAR and the target moment; verify finite second moments. Derive the three-term nuisance expansion with correct conditional centering, bound the first two conditional variances using L² errors and the product's first moment by the L²-error product, and aggregate over the fixed folds to obtain an o_p(n^−1/2) remainder. A quantitative sup-norm propensity rate is not available or needed.
2. **3 points — GAI consistency and normality.** Establish local population identification and nonsingular J; justify local empirical convergence and convex localization on the open, potentially unbounded parameter set. Obtain a valid Taylor expansion, first establish the root-n rate, and then derive asymptotic linearity and the stated CLT. An integrated empirical-Hessian argument is fully acceptable instead of Donsker theory. If stochastic equicontinuity is used, it must concern the centered process √n(P_n−P), not an uncentered empirical-score increment.
3. **3 points — Unified family.** Verify the corrected criterion-score relationship, nonnegative Hessian weights including λ=0 and λ=1, the common population target and Jacobian, and finite score second moments for each fixed admissible member. Prove consistency and asymptotic normality for these members, rather than merely asserting that the GAI proof repeats. Derive the binary-label covariance expression.
4. **1 point — Covariance minimization.** Use conditional mean zero of the label residual to eliminate the mixed terms and obtain the displayed positive-semidefinite gap. State directional strictness using vᵀJ^−1Xᵀr; do not infer positive-definite improvement merely from a nonzero vector residual.
5. **1 point — Members and feasible transfer.** Identify GAI, primary-only, PPI and PPI++; check the prediction component's membership and existence of a population trace-minimizing λ_*. Show that known-propensity feasible GAI has the oracle limit under foldwise L² consistency alone, without imposing the general product-rate condition.

# Evaluator Notes

Accept complete valid alternative proofs. The public approximate-score rate is an estimator condition, not something a solver must derive from o_p(1) criterion excess alone. Exact roots need exist only with probability tending to one; no finite-sample almost-sure existence claim is required. Measurable assignments on vanishing-probability exceptional events do not affect the asymptotic conclusions.

The proof must respect fixed-fold training independence; individual observation exclusion does not justify the conditional variance bound for an aggregate of arbitrary leave-one-out fits. No uniform CLT over f, data-adaptive tuning theorem, growing-fold result, or nonsingular limiting covariance is required.

A missing conditional-residual covariance argument is theorem-critical. Merely naming orthogonality, convex M-estimation, Donsker theory, or a concentration theorem without stating the relevant consequence and verifying its hypotheses does not close the corresponding step. The optimal covariance is unique, but the minimizing pair (λ,f) need not be.
