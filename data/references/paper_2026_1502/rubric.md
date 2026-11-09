# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Duality and support localization (2 points).** Establish an optimal dual vector for each existing primal minimizer and the pairing equality \(\int K_*p\,d\mu=\|\mu\|_{\rm TV}\), together with dual feasibility. Deduce support in \(\{|K_*p|=1\}\). For regularization, use the residual relation with the correct factor of \(\lambda\). Do not require or assert uniqueness of an interpolation dual optimizer.
2. **Piecewise-linear stratum formula (3 points).** Derive the ReLU formula using binary activation indicators \(\pi_i\in\{0,1\}\). On a stratum and its relative closure, identify the coefficient as the orthogonal projection onto \(L_J\). Handle boundary strata without assuming independent normals or replacing their actual dimensions by the number of equality constraints.
3. **Extremizer characterization and finite representation (3 points).** Justify that relative-interior saturation forces the projected vector to be parallel to the saturation point and of norm one. A tangent-curve or equivalent local-optimality argument is sufficient. Then obtain the signed normalized-projection formula and exclude a second saturation point in the same stratum. Treat zero measures by an empty sum and do not divide by a zero projected vector.
4. **Geometric cardinality bound and consequences (2 points).** Give a valid proof of the exact requested bound \(N\le B(n,d)\), followed by \(B(n,d)\le3^n\) and the fixed-dimensional \(O(n^d)\) estimate. The reference proof counts positive and negative saturation points on the corresponding coefficient-sign subarrangements and proves the stronger intermediate bound \(|\{|\eta|=1\}|\le\Xi(n,d)\). Any complete valid alternative establishing the requested bound is acceptable.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its coefficient-sign partition, or a separate proof of uniqueness of the regularized dual optimizer.

The following are theorem-critical errors, not acceptable counting shortcuts:

- Inferring equality in Cauchy-Schwarz merely from \(|\langle z,w\rangle|=1\), \(\|w\|=1\), and \(\|z\|\ge1\).
- Applying a fixed activation-pattern formula outside the associated stratum closure.
- Replacing a sum over possible stratum dimensions by the maximum of the individual layer counts without a valid additional argument.
- Assuming codimension equals the number of equality indices for arbitrary data.
- Claiming that the zero certificate has finitely many absolute-maximum points. Its unit level set, which is the relevant set, is empty.

Standard finite-dimensional convex or arrangement facts may be used when stated precisely and applied with verified hypotheses. The regularized dual objective in the task is scaled: equality of optimal values is between the primal value and \(\lambda\) times the displayed dual value. This normalization does not change the dual optimizer.

Interpolation infeasibility makes the assertion about its minimizers vacuous; it does not require a new feasibility hypothesis. Constants in the fixed-dimensional bound may depend on \(d\), but not on the data, labels, or \(\lambda\).
