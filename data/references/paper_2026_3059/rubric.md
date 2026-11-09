# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the parameter and Gaussian-random-effect transformations corresponding to the standardized representation induced by an allowed raw-coordinate rescaling, and proves invariance of the actual conditional predictor and integrated marginal likelihood. The intercept coordinate must remain fixed. A valid Gaussian pushforward or expectation argument is sufficient and covers singular covariance matrices; a density/Jacobian argument is acceptable wherever densities exist.
- **2 points:** Shows that empirical centering and positive unit-variance normalization reduce the allowed raw-coordinate rescalings to coordinatewise sign flips, using the same empirical normalization sample and convention.
- **3 points:** Proves invariance of absolute population effects, random-effect standard deviations, and normalized population and heterogeneity shares for coordinates 1 through K. Addresses positive-denominator domains and does not assign shares to zero-denominator cases.
- **2 points:** Establishes representation-independent posterior ordering probabilities for defined shares under consistently transported conditional posteriors, and demonstrates non-identifiability of the raw sign of every nonzero population coefficient among coordinates 1 through K.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. In particular, a direct proof using the induced sign transformation earns full credit without the auxiliary general coordinate-reparameterization calculation.

Do not apply the inverse raw-scale transformation to standardized-coordinate parameters after restandardizing the raw outputs. Positive raw rescalings leave standardized coordinates unchanged. Any auxiliary unstandardized or unnormalized model must be distinguished from the supplied standardized model.

Do not require a positive-definite covariance assumption or a Lebesgue density for a degenerate Gaussian law. Do not require full statistical identifiability beyond invariance within the stated coordinate-rescaling ambiguity. The share sums exclude the intercept coordinate.

Naming a reparameterization or invariance method without deriving the theorem-critical consequences earns no credit for the corresponding step.
