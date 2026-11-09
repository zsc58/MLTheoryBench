# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Couples the filters on the same true-model observation history, establishes the conditional affine recursion with the correct alpha and c, and unrolls it from the common prior. The posterior-comparison ingredients must be derived or justified by a precisely stated applicable result; a bare specialized citation is insufficient.
- **2 points:** Establishes a valid high-probability time-average bound implying the stated epsilon_b, then applies the union bound over 2N trajectories. Accept the reference proof's fixed-parameter exponential argument or another valid concentration proof. Bounded martingale increments alone do not justify the original smaller Hoeffding-style expression, and substituting random predictable variance into a fixed-variance Freedman bound without justification does not close this step.
- **2 points:** Proves posterior-feature Lipschitzness and the per-comparison bound ||tilde phi_i-phi_i||_2<=4TB_r epsilon_b, together with the feature boundedness needed downstream.
- **3 points:** Establishes the constrained unpenalized Bradley-Terry MLE inequality through the Hessian lower bound rho tilde Sigma, clean-score self-normalized concentration with the correct N normalization, mismatch-gradient control, and covariance comparison. The statistical contribution must include both 2/rho and sqrt(c_zeta/(c_zeta-1)), unless a valid alternative argument proves a stronger bound. The covariance regularizer must not be treated as an objective penalty.
- **1 point:** Combines the confidence events and obtains the exact statistical, mismatch, and covariance-regularization terms, including positive-zeta handling when B_r epsilon_b=0 and the t=0 expectation case.

# Evaluator Notes

Accept any complete valid alternative proof. Omission of the conditional filter recursion, justified concentration, feature transfer, or covariance/gradient comparison is theorem-critical. The expectation statement holds for each prescribed action sequence and each fixed full learned parameter; do not silently grant observation-dependent parameter selection. Preference independence and mean-zero score conditions should be used in the clean-feature experiment, not asserted for misspecified perturbed residuals. No eigenvalue lower bound on the unregularized covariance is assumed. The corrected reference proof closes all required obligations and has no unresolved GT dependency.
