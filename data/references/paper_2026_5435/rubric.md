# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly computes the conditional mean and variance of a general leave-one-out linear estimator, using conditional independence to eliminate covariance terms.
- **2 points:** Identifies the unbiasedness constraint \(\sum_{j\ne i}a_{ij}\mu_j=\mu_i\) and shows that conditional MSE reduces under this constraint to \(\sum_{j\ne i}a_{ij}^2\tau_j^2\).
- **4 points:** Solves the heteroskedastic constrained quadratic minimization and derives
  \[
  a_{ij}^{\star}=\frac{\mu_i\mu_j/\tau_j^2}{\sum_{k\ne i}\mu_k^2/\tau_k^2}.
  \]
  Merely naming a least-squares or BLUE principle without deriving the coefficients does not earn full credit for this step.
- **2 points:** Verifies feasibility/unbiasedness of the displayed coefficients and proves global optimality and uniqueness from positivity of the variances and strict convexity (or an equivalent equality-case argument).

# Evaluator Notes

Accept a complete valid alternative proof, including one based on Cauchy-Schwarz. Do not require the reference proof's incidental presentation choices. If the optimization is not justified but the correct coefficients are merely asserted, award credit for any independently correct moment and feasibility calculations, but not full credit for the central minimization step.
