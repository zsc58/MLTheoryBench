# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly diagonalizes the commuting matrices, derives the mean recursion with consistent momentum scaling, and obtains the exact mean critical step size. Necessity must apply to the stated zero-momentum initialization, not merely to arbitrary augmented states.
- **3 points:** Derives the closed weighted second-moment recursion from conditional Gaussian fourth moments, including the local variance term and rank-one global coupling. The covariance state and its momentum normalization must agree with the displayed update.
- **3 points:** Correctly establishes stability strictly below the scalar root and failure strictly above it. For the covariance-operator route, this includes the local resolvent domain, a justified coupled spectral argument covering steps outside that domain, separate treatment of zero-curvature coordinates under summable forcing, and transfer of supercritical growth to an admissible deterministic initialization with zero momentum. An unproved assertion of strict instability from local noncontractivity is insufficient. A rank-one injection matrix cannot be assumed to dominate an arbitrary PSD Perron eigenvector.
- **2 points:** Proves existence and uniqueness of the scalar root, identifies it as the mean-square critical step size defined by a supremum using both strict regimes, and derives both stated bounds.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular two-step domination argument if admissible initialization and instability are justified another way.

The assumptions allow singular nonzero H and beta=0. A proof using inverse local resolvents must restrict them to positive-curvature coordinates and justify boundedness of the remaining coordinates. A proof using arbitrary position-momentum initial states or their mixtures must additionally establish the needed conclusion for the actual experiment m0=0.

The theorem does not require a claim about mean-square stability exactly at the critical equality boundary. Award no separate points for optional endpoint analysis and do not deduct for omitting it. An unsupported endpoint assertion must not substitute for a required strict-regime argument. In particular, spectral radius one is not, by itself, a proof of either boundedness or unboundedness.

All reference-proof obligations are closed. There is no private GT quality warning.
