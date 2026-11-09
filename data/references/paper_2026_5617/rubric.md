# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly standardizes the clean and noisy variables and identifies their coordinatewise joint Gaussian correlations as \(\sqrt{\rho_j}\).
- **4 points:** Derives, rather than merely asserts, the conditional Hermite attenuation \(\mathbb E[h_\alpha(U)\mid V]=\prod_j\rho_j^{\alpha_j/2}h_\alpha(V)\), and validly extends it from modes or finite sums to the \(L^2\) expansion of the Bayes predictor. Within these points, assess both the modewise/product calculation and the passage to the full expansion. The identification with the Bayes predictor must account for the label noise's zero conditional mean.
- **2 points:** Identifies affine functions of the noisy covariates with the degree-at-most-one Hermite subspace and justifies that the best affine predictor is the corresponding orthogonal projection.
- **2 points:** Uses the conditional-expectation risk decomposition and Parseval correctly to obtain the exact displayed excess-risk sum.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that only cites a Hermite conditional-expectation formula without establishing or adequately justifying it does not earn the central 4 points. A missing \(L^2\) limiting argument or an unsupported projection/risk-decomposition step is theorem-critical when it prevents the exact identity from being established. Award partial credit within each item for the components actually established.

The multi-indices include zero in every coordinate; the constant mode and the coordinate unit modes must therefore be included in the affine comparison. Square integrability of predictors is under the observed Gaussian law, not Lebesgue measure. The expansion is required in \(L^2\), not pointwise everywhere.

The stated independence assumptions imply independence of \(\epsilon\) from \(\widetilde X\): use \(\epsilon=Y-f(X)\), independence of \(\eta\) from \((X,Y)\), and independence of \(\epsilon\) from \(X\). Accept a concise correct invocation of this implication; do not require a stronger joint independence assumption to be added to the task.

Standard Gaussian calculations, conditional Jensen, Hermite orthonormality, and the L2 norm identity may be justified in any mathematically adequate way. The reference proof explicitly verifies their applications. Do not impose a particular generating-function presentation on a valid alternative derivation.

The task restores the source's strictly positive measurement variances. Do not require a zero-measurement-noise extension, a large-noise asymptotic rate, a classification result, or a finite-sample learning claim. Constant and affine regression functions and zero label noise remain admissible; their vanishing nonlinear energy is covered by the same identity.
