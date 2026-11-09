# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly expands the two Gaussian likelihoods, uses the stated invertibility condition to obtain the positive-definite covariance \(S\), and completes the square to produce the measurement-dependent pivot \(w\) and factorization.
- **2 points:** Obtains the conditional-density factorization with positive finite normalizers and differentiates both its normalizing factor and its smoothed-density factor with the correct chain rule. Supplies a valid justification for the required differentiation under the integral, such as an integrable Gaussian-derivative bound.
- **3 points:** Derives the anisotropic Gaussian-smoothing score identity from the defining integral and applies it so that the pivot terms cancel, establishing the stated posterior-score formula.
- **2 points:** Correctly identifies the normalized latent conditional density and proves the posterior-mean identity \(M_S(w)=\mathbb E[U\mid Z=z,R=r]\), including finiteness of the conditional means and the pointwise density-ratio interpretation, while respecting the stated time and invertibility domain.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. In particular, a proof that differentiates the joint likelihood integral directly and separately identifies the conditional latent density may receive full credit without introducing the reference proof's intermediate normalizer or separately naming a smoothing identity. Allocate the points by the mathematical obligations established, rather than by a mandatory sequence of displayed equations.

The prior is an arbitrary probability density. Do not require an unconditional first or second moment, bounded support, or differentiability of the prior. The conditional means in the task are integrals against the specified density-ratio conditional laws. Positive-definite Gaussian weighting makes their first absolute moments finite at every required conditioning value. A proof that adds an unconditional moment assumption proves only a restricted case unless it removes that assumption.

The claims are pointwise for every \(z,r\), not merely almost surely for unspecified conditional versions. A proof using the prescribed positive density ratios addresses this requirement. It need not discuss pathological alternative versions.

The stated domain permits \(a_t=0\) if \(Q\) is invertible. Do not accept an unqualified division by \(a_t\) that leaves this case untreated. Conversely, a proof whose formulas remain valid at \(a_t=0\) needs no separate case split. Rank-deficient and zero \(H\) must not be excluded when \(Q\) is invertible. Neither \(b_t>0\) alone nor a claim about typical schedules is a substitute for the actual invertibility condition.

All theorem-critical obligations are closed in the reference proof. There is no unresolved private proof dependency to be treated as an assumed scoring step.
