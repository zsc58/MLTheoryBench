# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly compose the affine iteration, state the Gaussian pushforward mean and covariance Sigma=G Sigma_0 G^T, and introduce a valid rank factorization of G.
2. **3 points:** Prove from positive definiteness and the rank factorization that ker(Sigma)=ker(G^T) and range(Sigma)=range(G), including the needed non-singularity on the rank-dimensional factor.
3. **2 points:** Use the universal fixed-point identity for the sampled exact truth to derive x_i-x^star=G(x_0-x^star) and hence the identically zero null-space error.
4. **3 points:** Under x^star~N(x_0,Sigma_0), derive the Gaussian law and covariance of the range-projected error and show that whitening by (R^T Sigma R)^(-1/2) gives N(0,I_r), completing strong calibration. Accept either an explicit r=0 boundary-case argument or the stated empty-space convention.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A missing or incorrect range/null-space argument or whitening-law derivation is theorem-critical; merely naming Gaussianity, rank factorization, or calibration without proving the corresponding claim earns no credit for that step. The fixed-point step must apply to the sampled exact truth, not merely to one separately specified solution. Treat the zero-dimensional boundary case using the convention stated in the public task or by a separate vacuity argument.
