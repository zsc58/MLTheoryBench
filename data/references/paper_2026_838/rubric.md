# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Poisson KL derivation and residual factorization (4 points):** Establishes the coordinatewise Poisson posterior-to-prior KL and obtains \(R_P=\sum_i\lambda_{0i}f(\delta_i)\) for independent coordinates on the stated positive-rate domain. A direct log-mass-ratio calculation is sufficient. An applicable standard KL result, correctly stated and applied with its hypotheses verified, is also acceptable.
2. **Gaussian KL derivation (3 points):** Establishes the diagonal-Gaussian KL and expresses it in displacement/variance-ratio form. A direct expected log-density-ratio calculation using Gaussian second moments is sufficient. An applicable standard multivariate Gaussian KL formula, correctly stated and specialized to the positive diagonal covariance matrices, is also acceptable.
3. **Structural contrast and interpretation (3 points):** Proves scaling by every \(c>0\) when the Poisson residual is fixed and both prior and posterior rates scale together. Proves invariance of the Gaussian rate when both means are translated together with displacement and variances unchanged. Explains the resulting coupling between the defined Poisson coding rate and baseline firing activity, interpreted as the metabolic proxy, and its absence under the specified Gaussian translation comparison.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The public domain has strictly positive Poisson rates and Gaussian standard deviations. Zero-rate or degenerate-Gaussian extensions are not required. If an answer discusses zero Poisson rates, distinguish the fixed-positive-baseline extension from the fixed-residual zero-baseline extension; do not require or accept unrestricted joint continuity at two zero rates.

The identity residual \(\delta=(1,\ldots,1)\) is included: its Poisson coding rate is zero for every baseline, and the homogeneity statement still holds. Do not demand strict positivity or strict activity penalization in that case. Conversely, a claim that KL is strictly increasing with baseline scaling for every residual is an error.

Coding rate is the posterior-to-prior KL defined in the task. No stimulus distribution, mutual-information equality, axiomatic uniqueness theorem, Fisher-metric derivation, decoder analysis, or training prediction is required. The metabolic conclusion concerns baseline spike activity in the specified comparison; it is not an equality between KL and physical energy or a uniqueness claim over all latent distribution families. Do not require logarithmic-unit conversion unless the answer makes an incorrect numerical assertion about bits versus nats.
