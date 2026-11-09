# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct core argument.
- **3–7:** Some correct core steps or conclusions, with important obligations unresolved.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

## Proof expectations

The repaired reference now proves both the expectation and the leading variance for the public Gaussian experiment. Its former centered-covariance gap is closed by an explicit calculation; it must not be closed merely by citing the source's uncentered deterministic equivalents.

Accept a complete valid alternative proof and do not require the reference's incidental presentation or its particular error rate. An audited standard-independent result may be used with its relevant statement and verified hypotheses. A nonstandard dependency requires an actual derivation or an already audited proof of the needed statement; a name, citation, or proposed conclusion alone is insufficient.

The public task does not assume its target expectation or covariance identities. Uniform integrability and tightness control integration but do not identify a covariance kernel. A valid proof must establish the latter separately.

## Core Steps

1. **2 points — Statistical experiment and terminal map.** Use the centered Gaussian covariance with normalization 1/n and fixed denoiser location mu, without conditioning on a random empirical-mean equality. Obtain the fixed-dimension infinite-initial-noise limit mu+widehat Sigma^(1/2)xbar. Do not replace the stated sequential limit with an unspecified joint rate.

2. **4 points — Mean and modewise shrinkage.** Establish a positive-square-root representation valid for singular matrices, justify the anisotropic expectation approximation, and pass through the improper integral with adequate integrability. The reference's Gaussian sign-symmetry, coordinate-deletion, concentration, and self-consistency argument is one acceptable approach. Prove the specified bounded deterministic bilinear conclusion. Compare the deterministic coefficient with sqrt(s), including equality at s=0 and strict finite-dimensional shrinkage at positive s. Do not assert a pathwise matrix ordering or a uniformly positive limiting gap.

3. **3 points — Leading variance.** Establish the exact centered covariance integral and a sufficiently precise centered two-point approximation. Obtain the factorized kernel with coefficient 4/pi^2, denominator n-df_2, and both directional factors. Identify and control the actual alignment contribution under the public J_n condition. The reference derives C_n=H_n+J_n+R_n with |R_n|<=o(1)H_n on compact positive rectangles; any estimate strong enough for the asserted integrated relative limit is acceptable. Control errors without losing the variance scale when population quadratic forms vanish with n. Apply the public integration conditions only after kernel identification. Dataset independence, Euclidean orthogonality, formal first-moment cancellation, or uncentered o(1) error alone does not suffice.

4. **1 point — Domains, scales, and boundary cases.** Keep gamma_n=d/n in finite-dimensional equations. Verify uniqueness and positivity of kappa and positivity of the mixed denominator for positive arguments. Treat improper endpoints, singular covariances, zero vectors, and population-nullspace vectors. Distinguish additive mean convergence from relative variance convergence. When V_n=0, prove the variance is exactly zero; the projected output is the constant v^T mu and need not itself be zero.

## Evaluator Notes

Do not award the variance points for formal cancellation or uniform-integrability assumptions without a valid centered approximation. The exact error identity C_n-H_n=epsilon_{u,w}-m_u delta_w-m_w delta_u-delta_u delta_w explains why separate low-accuracy moment equivalents are insufficient.

Do not require the reference's coordinate-entry decomposition if an alternative proof supplies equally strong centered and alignment estimates. Likewise, its O(n^(-1/4)) compact-rectangle relative remainder is sufficient but not a required rate.

Do not demand a uniform lower bound on positive population eigenvalues, exclude the critical aspect ratio, or demand operator-norm concentration of the random covariance function. The reference's operator-norm one-point estimate concerns an expected matrix. Its weighted covariance error estimates preserve small variance scales without additional public assumptions.

The public tightness assumptions suffice for the final integration in the reference because it proves local L1 convergence directly. A proof need not separately use every part of a stronger stated uniformity assumption if the required passage is otherwise justified.

The reviewer correctly identified a gap in the preceding reference revision. That historical finding must not be reinterpreted as a counterexample to the public theorem or dismissed as mathematically unfounded; the present reference repairs it by supplying the missing calculation.
