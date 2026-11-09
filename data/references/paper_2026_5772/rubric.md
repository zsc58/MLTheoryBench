# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Moment factorization and shared row space (2 points).** Derives both observable factorizations from the conditional independences and identifies the observed conditional outcome means with potential-outcome means. Uses positivity plus full-rank assumptions to show rank k, identify the common row space, justify the existence of V, and obtain an invertible change-of-basis matrix R with B^T=RV^T. The expectations must be justified by the stated first-moment assumptions and conditional independence; no boundedness or higher marginal moments may be assumed.
2. **Common-similarity spectral identification (3 points).** Uses justified full-rank pseudoinverse algebra, or an equivalent direct argument, on the compressed moments to prove K_t=R^{-1}G_tR and L=R^{-1}diag(theta)R. Concludes that the eigenvalues are exactly the latent treatment effects, with multiplicities. This is the characteristic bottleneck and requires an actual derivation of the common similarity, not merely the name of a spectral method. A Moore-Penrose verification or the full-column-rank inverse formula can justify the product identity.
3. **Eigenvector lifting, anchor normalization, and proportion recovery (3 points).** Uses distinct effects to characterize left eigendirections, lifts them through V^T, and removes diagonal scaling using the first coordinate of every row of B^T. Correctly identifies the all-ones anchor as the first column of B^T, equivalently the first row of B. Establishes nonzero normalization denominators and solves Bp=E[X] uniquely using full column rank. Tracks the same permutation through effects, feature columns, and probability coordinates.
4. **Complete moment and resolvent identity (2 points).** Establishes a^T L^ell c=E[theta_C^ell] for every integer ell>=0 and derives the convergent resolvent/generating-series formula for every complex z with |z| ||L||_2<1. Justifies the matrix series convergence and multiplication by the anchor vectors. Includes the zeroth moment and does not exclude zero treatment effects or L=0.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Apply the common integer score guide. Do not award the spectral-identification points for merely naming a diagonalization or a spectral method without verifying the factorizations and the relevant pseudoinverse or equivalent cancellation step. Propagate a missing shared-row-space argument to downstream conclusions when the required similarity representation remains unsupported. The one-class case is allowed and spectral separation is then vacuous. The condition |z| ||L||_2<1 does not require division by ||L||_2 and therefore includes L=0. The task concerns population identification only; finite-sample concentration, rank selection, and perturbation bounds are not proof obligations.
