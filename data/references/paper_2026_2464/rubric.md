# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly derives the normal equations and unique minimizer on the eventual positive-definite tail, and defines/uses the deterministic target there.
- **3 points:** Obtains the exact root-n decomposition as inverse penalized Hessian times the score.
- **2 points:** Verifies a multivariate triangular-array CLT for the score using the common error distribution's finite (2+eta)-moment and the no-dominant-row condition.
- **2 points:** Establishes inverse-Hessian convergence and applies Slutsky to obtain the stated Gaussian covariance.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. The error law must be treated as common across the array (or an explicitly equivalent uniform-integrability condition must be proved). The eventual-tail formulation makes finite initial singular indices irrelevant to the asymptotic claim.
