# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** State or correctly use the nonsingular Gaussian-density domain \(\sigma_k^2>0\) and \(\sigma_k^{*2}>0\), reduce equality of centered Gaussian laws to equality of covariance matrices, and identify each \(\sigma_k^2\) from the smallest eigenvalue using the rank-deficient signal covariance.
- **3 points:** Derive from the cross-block covariance equality that the joint loadings have invertible coordinate changes \(W_{J1}^*=W_{J1}T_1\), \(W_{J2}^*=W_{J2}T_2\), with \(T_2=(T_1^{-1})^{\mathsf T}\), using full column rank; explain that the observable cross-covariance has rank \(r_J\).
- **3 points:** Equate diagonal covariance blocks and derive both positive-semidefinite residual Gram-matrix identities for the transformed individual loadings; establish necessity rather than merely naming a factorization.
- **2 points:** Prove sufficiency by substituting the transformation and Gram identities into all covariance blocks, concluding equality of the Gaussian densities and the stated identifiability/nonuniqueness implications.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Award no substantial credit for simply asserting a known factor-analysis identifiability result without deriving the coupled transformation and PSD residual conditions. A proof that treats Gaussian densities at zero error variance without addressing the resulting singularity does not satisfy the density-domain obligation.
