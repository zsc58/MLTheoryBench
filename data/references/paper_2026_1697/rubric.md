# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Projected one-step progress inequality (2 points).** Applies smoothness on update segments, the orthogonal-projector identities, conditional unbiasedness, and the conditional variance bound. Obtains the conditional gain with coefficient at least eta_t/2 and error L eta_t^2 sigma_g^2/2. The projected second moment must be bounded using the centered-noise decomposition, not by incorrectly replacing an ambient gradient norm with its projected norm.
2. **Telescoping, convergence, and finite-time rate (3 points).** Derives expected weighted summability, almost-sure weighted summability, and almost-sure convergence of objective values for the infinite-horizon schedule. A correctly stated and checked almost-supermartingale theorem, or the nonnegative-supermartingale tail correction, is acceptable. Separately obtains the exact finite-horizon bound for eta_t=eta/sqrt(T), with the displayed constants and parameter dependence.
3. **Euclidean-to-natural stationarity comparison (2 points).** Establishes the pointwise two-sided spectral comparison, its expectation form with random inverse eigenvalues inside expectation, and the deterministic-factor comparison when m_T>0. Recognizes that an SPD random matrix need not have a positive deterministic lower spectral bound. Handles the expectations as extended nonnegative integrals when necessary.
4. **Kantorovich alignment bottleneck (3 points).** Proves the actual-cosine bound 2 sqrt(kappa)/(kappa+1) for every nonzero direction. Either derives the relevant matrix inequality or states its precise standard form and verifies its application, including the square-root substitution or an equivalent argument. Merely naming Kantorovich without the relevant inequality and application is insufficient. Handles positive definiteness, positivity when taking square roots, and the nonzero-direction restriction.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The estimator is sampled after the pre-update history; do not require it to be measurable with respect to that history. The initialization and step sizes are deterministic. The infinite-horizon and finite-horizon schedules are alternatives, not simultaneous requirements.

The boundedness assumption does not modify the displayed linear-subspace recursion. Do not insert an additional radius-projection update and apply the same proof without justification.

Do not demand an unweighted gradient limit. The source's additional assertion is a liminf, which follows from weighted summability and divergent total step length; it was previously misread in the material record. The frozen target requires the stated weighted summability, objective convergence, and finite-horizon rate.

Do not accept extracting a random minimum eigenvalue from an unconditional expectation. No independence of the metric and the iterates is assumed. If m_T=0, the task does not assert a finite deterministic-factor bound.

The action policy is Gaussian-generated with explicitly clipped exploration, not an unmodified Gaussian supported on a compact set. No Gaussian score or Fisher identity is required. Smoothness and the estimator properties are given hypotheses; deriving them from the MDP is outside this task.

An arbitrary lower-bound witness for a cosine need not exceed the sharp universal guarantee. The target concerns the actual cosine alpha_t. In an endpoint-weight proof of Kantorovich, the maximizing weight is 1/2 for distinct endpoints, not M/(m+M).
