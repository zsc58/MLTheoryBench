# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Shifted-logit representation and linear maps (2 points):** Correctly uses the pivoted matrices and shows that each shifted logit discrepancy equals L_{i,J}^T(f-A_{i,J}f'), with A_{i,J}=L_{i,J}^{-T}L'_{i,J}^T.
2. **Combinatorial/logit averaging identity (2 points):** Derives the subset and pivot averages and uses centering to obtain average_{i,J} E||L_{i,J}^T(f-A_{i,J}f')||^2 = (2m/(k-1)) d_logit^2. The count remains valid for m=k-1.
3. **Singular-value bottleneck (4 points):** Applies the SVD or equivalent extremal singular-value inequalities to every shifted matrix, with correct orientation and use of general-position invertibility, and averages the resulting weighted residual bounds. Uses the unprimed matrices for the extrema and justifies that the extrema are positive and finite because the family is finite and nonempty.
4. **Final two-sided comparison (2 points):** Combines the identities, uses the global sigma_min and sigma_max, takes square roots correctly, and states both bounds with C=sqrt(2m/(k-1)). The argument must remain valid for zero and infinite distances.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or an explicit SVD when equivalent singular-value norm bounds are correctly justified. Deduct for treating the representation bound as an assumption, omitting either inequality, or failing to justify the averaging factor or singular-value conditioning.

No finite-second-moment or probability-lower-bound assumption is available. A proof using nonnegative integration and positive finite constants already covers infinite distances; do not require a redundant separate case split. A proof that only establishes the finite-distance case and does not extend to infinite values has an omitted case. Do not require use of the embedding-span assumptions or primed invertibility in every argument: they remain part of the source contract even though the direct quantitative proof needs less. No Aitchison identity or exact-identifiability theorem must be invoked.
