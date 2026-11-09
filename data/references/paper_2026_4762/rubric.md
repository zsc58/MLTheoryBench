# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points — Well-defined likelihood and geometry.** Defines an integrable likelihood-ratio objective, or otherwise justifies all likelihood differences; proves its gap is KL from the true observation law to the candidate law; establishes convexity and the needed score formulas. A treatment of ideal singleton observations must use densities or an equivalent valid formulation, not their zero Gaussian masses. Finite cell encodings alone do not justify finite entropy.

- **2 points — Quantitative local growth.** Uses information preservation, Pinsker, and a valid equal-covariance Gaussian TV bound to derive a quadratic parameter-error bound on a specified objective sublevel. Maintains the true-to-candidate divergence orientation and handles the sublevel boundary or works with a strictly smaller threshold.

- **2 points — Stochastic gradients and localization.** Constructs gradients that are unbiased conditionally on the adaptive history using fresh coarse observations and conditional samples. Gives a uniform second-moment bound on the actual candidate domain. Establishes an origin-box refinement with radius accounting for D, dimension, total sample count, and confidence; proves retained information preservation and a transcript coupling. Does not treat conditioning all latent samples to the box as preserving their unconditioned law. For arbitrary R, the basic moment bound retains the additive d; choosing R>=1 is sufficient.

- **2 points — Optimization and amplification.** Provides a justified stochastic-optimization guarantee with its hypotheses verified and objective tolerance translated correctly into Euclidean accuracy. A named specialized local-growth method is not by itself a derivation. The reference proof supplies a direct restarted-SGD argument; another complete argument is acceptable. Explains confidence amplification without assuming likelihood evaluation, and includes its sample cost.

- **2 points — Two-stage rate and runtime.** Obtains a constant-distance estimate from the supplied coarse data rather than assuming one, then uses fresh data to obtain the desired accuracy. Establishes the additive D^2 and epsilon^{-2} dependence, rather than a D^2 epsilon^{-2} product. Every sampling query must be supported by the public oracle: a translated-box sampler cannot simply be presumed. Accounts for all failure events, fixes any sample-budget/localization circularity, and gives polynomial runtime under the assumed sampler and observed-cell operations. Handles D=0 or D<=epsilon directly, and uses valid logarithm and integer-rounding conventions.

# Evaluator Notes

Accept a complete valid alternative proof; do not require incidental presentation choices, the reference constants, or an optimal power of suppressed logarithms. The target uses tilde-O, so the sufficient explicit logarithmic bound derived in the reference proof is acceptable.

Do not require implementation of the conditional sampler through hit-and-run: that sampler is already a public assumption. If an answer chooses to implement it, approximate sampling is not exact unbiased sampling, and the answer must verify the implementation hypotheses and account for approximation error.

Do not award full optimization credit for an unproved paper-specific dependency merely because it appears in the source. Standard independent results may be used with their relevant hypotheses checked. Propagate an earlier error only when it leaves a later conclusion unsupported.

The source's auxiliary local-estimation proposition has a sharper explicit logarithmic display that is not established by the supplied argument. That display is not an evaluator requirement or an unproved premise of this reference proof. All obligations necessary for the frozen public target are closed by the replacement proof.
