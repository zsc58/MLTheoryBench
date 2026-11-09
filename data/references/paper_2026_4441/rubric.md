# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly handles the iid dropout variables, establishes unbiasedness of the single-level sample variance, and establishes or correctly invokes its finite-fourth-moment variance formula with the hypotheses verified. The corresponding sample-mean identities may be used as supporting facts but are not separate required conclusions.
- **3 points:** Correctly handles the dependence created by prefix reuse. In a covariance-based proof, derives the overlapping-sample covariance through a justified pooled-variance decomposition and fourth-moment calculation, or an equivalent argument. A direct derivation of the correction variance that accounts for the same shared-sample dependence earns the same credit without separately stating a covariance identity.
- **3 points:** Obtains the explicit variance of each multilevel correction, including both the \(\mu_4-3\mu_2^2\) and \(\mu_2^2\) terms. The derivation must be justified rather than merely asserting the paper-specific correction formula.
- **2 points:** Proves unbiasedness of the coupled MLMC estimator, uses unbiasedness of each within-level empirical variance and linearity of expectation to obtain the displayed formula for \(\mathbb E[S_V^2]\), and obtains the zero-excess-kurtosis specialization.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or an explicit covariance calculation when a valid direct calculation proves the same correction-variance identity. Standard independent sample-variance identities may be invoked with their statements and hypotheses made clear; an unsupported specialized overlap or correction identity is insufficient.

Outer replicates are iid within each level. Independence between different levels is not assumed and is not needed for either requested expectation identity. A proof must not rely on cross-level independence or identify \(\mathbb E[S_V^2]\) with \(\operatorname{Var}(\mathcal V)\) without an additional valid argument applicable to the stated sampling contract.

No Gaussianity or positive predictive variance is assumed. The condition \(\mu_4=3\mu_2^2\) is only a moment relation. A proof valid algebraically when \(\mu_2=0\), at the minimum sample sizes, and with an empty correction sum need not discuss those cases separately.
