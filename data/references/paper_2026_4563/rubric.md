# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Derives the population-minimum expected-Hessian identity and covariance-weighted fluctuation expression with consistent Jacobian dimensions. Uses independent zero-mean noise correctly and accounts for the fixed iid batch factor 1/m. Obtains the layerwise trace and fluctuation expressions, or equivalent identities sufficient for the remaining proof.
2. **2 points:** Proves that each selected limit is a population minimizer and minimizes fluctuation on the population minimum manifold. Uses the eta/4 comparison correctly. Under the stated second moments, handles possibly infinite off-manifold fluctuation using lower semicontinuity/Fatou or another valid argument, rather than assuming a finite polynomial without justification. Does not assume coercivity of the factorized population loss or existence of a limit not stipulated by the task.
3. **3 points:** Establishes the minimum-fluctuation bound and attainment and derives sufficient equality conditions for every fluctuation minimizer. Effective prefix/suffix product characterizations are sufficient; a universal canonical factorization of all raw weights is neither required nor generally true. Computes the selected Hessian trace with the exact exponents, covariance traces, and final-layer contribution.
4. **2 points:** Proves the sharpness lower bound over all population minima, verifies attainment by appropriately scaled SVD-aligned factors, and obtains the exact formula for T_min. AM-GM and the Frobenius/nuclear-norm inequality are one valid route. The attaining factors must satisfy the product constraint and achieve equality in the bound.
5. **1 point:** Establishes orthogonal similarity of the expected Hessians for all selected limits. It suffices to show that orthogonal maps between the effective cut isometries intertwine the first-variation operators. A proof restricted to canonical representatives is incomplete unless it also covers arbitrary selected parameters with unused hidden components.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission or misstatement of either closed-form formula, the minimum claim, or the spectrum-invariance claim as theorem-critical.

The Hessian in the task is the expected population-loss Hessian, not an individual sample Hessian or the Hessian of F_eta. The architecture is fixed when comparing spectra.

The proof must cover D=2 and V=0. When V=0, all-zero weights attain zero trace and fluctuation, and positive-definite noise covariance forces the expected Hessian of every selected limit to be zero. A short independently justified treatment is sufficient. Penalize an omitted elementary endpoint proportionately, but do not accept a substantive restriction to a nonzero or full-rank teacher as proving the entire task.

Do not require or reward an unsupported invocation of a specialized deep-linear minimizer theorem. The characterization used must be derived, or supplied through an independently justified result with verified hypotheses. In particular, citing the prior-work factorization without addressing unused hidden directions does not close Steps 3 and 5.

There are no unresolved reference-proof obligations and no GT quality warning.
