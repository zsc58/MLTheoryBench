# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes that the stated symmetrized population objective is bounded above by mutual information, that the Gaussian log density ratio plus a constant is admissible and attains this bound, and that every maximizing critic agrees with this form almost everywhere. Derives the Gaussian quadratic-form expression up to an additive constant. A conditional relative-entropy argument or a correctly applied variational inequality with its equality conditions is sufficient.
- **3 points:** Performs whitening and canonical-correlation SVD reduction, accounts for the cancellation of uncorrelated residual coordinates, and obtains the coefficients `rho_i/(1-rho_i^2)` and `-rho_i^2/[2(1-rho_i^2)]` for the bilinear and self-quadratic terms.
- **3 points:** Gives and verifies explicit measurable separable encoders whose `K+2`-dimensional dot product equals the displayed optimal representative, accounting for both self-normalization terms.
- **2 points:** Gives and verifies a `K`-dimensional separable-augmented representation with appropriate symmetric quadratic coefficient matrices. Coefficients must be matched to the chosen encoder scaling; for encoders scaled by `sqrt(rho_i/(1-rho_i^2))`, diagonal entries `-rho_i/2` are correct.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of either self-quadratic term or failure to verify the stated coefficient matching as a major gap.

The objective has a logarithm inside each outer marginal expectation. Proving only the joint-versus-product DV bound does not by itself establish the required bound or equality conditions for this objective. Do not require finite-batch analysis or an estimator convergence argument.

The optimizer characterization is almost everywhere, whereas the requested encoder constructions reproduce the displayed polynomial pointwise. A proof using additive-constant equivalence is acceptable if the representative and the claimed equality are clear.

The case `K=0` is included. Empty-sum and empty-matrix constructions are sufficient; a separate discussion is not necessary if the proof manifestly covers them. An otherwise complete proof that merely omits a readily supplied rank-zero case belongs in the 8-9 range rather than receiving a major-gap penalty.

Do not require a lower bound on the necessary bottleneck width, uniqueness of the encoders, a claim that `K+2` is minimal, equal canonical correlations, or realization by a specified finite neural network.
