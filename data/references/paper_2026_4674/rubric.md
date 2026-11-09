# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps: Tensor-Operator Route

1. **2 points:** Formulate the displacement dynamics, identify the batch Jacobians, and prove the uniform Euclidean contraction of their linear parts from symmetry, positive definiteness, the positive strict step-size condition, and finiteness of the batch family. Obtain a common analytic expansion and justify a sufficiently small invariant neighborhood before applying it along the trajectories.
2. **3 points:** Derive the independent-batch upper-triangular recurrence for all tensor moments, justify expectation/series interchange, and construct the rho-scaled operator with blocks rho^{p-k} Psi_{k,p}. Verify that the actual scaled moment vectors belong to the direct-sum ell_2 space.
3. **3 points:** Supply quantitative analytic coefficient estimates giving summable geometric block-row bounds. Prove boundedness using the block row/column estimate and compactness using operator-norm convergence of finite truncations. Bound diagonal-block spectra by gamma^k and correctly apply compact spectral approximation to obtain spectral radius less than one.
4. **2 points:** Use decay of operator powers and the deterministic initial displacement to show convergence of each scaled tensor moment. Apply a correct even-degree tensor functional, or equivalent finite-dimensional norm comparisons, to obtain the requested Euclidean moments for every even k with a single common rho.

# Equally Valid Direct Route

A proof need not use tensor moments, infinite-dimensional operators, analyticity beyond the regularity needed for a local estimate, or spectral approximation. Award full credit to a complete direct proof. For partial-credit calibration, use the following allocation instead of the operator-route allocation:

1. **2 points:** Prove gamma=max_S ||I-alpha H_S||_2<1, using the symmetry and positive definiteness of the batch Hessians.
2. **3 points:** Obtain one neighborhood and one contraction factor theta<1 valid for every batch, by continuity of the finitely many Jacobians and a segment-integral estimate, or by a uniform Taylor remainder estimate.
3. **3 points:** Prove that the neighborhood is invariant and that every batch sequence satisfies ||z_t-z^star||_2<=theta^t||z_0-z^star||_2. This also establishes well-definedness and finiteness of all required moments.
4. **2 points:** Take kth powers and expectations, preserving the normalization and proving the limit for every even k using the same rho.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its longer operator architecture. Do not penalize a proof for showing the stronger pathwise contraction that follows from the stated assumptions.

A radius chosen separately for each moment order does not establish the requested quantifier order. A formal Taylor recurrence without checking that trajectories remain in its domain is incomplete. Uniformly bounded row and column sums alone do not prove compactness; an operator proof must supply a genuine truncation or equivalent compactness argument. Diagonal spectral bounds alone are likewise insufficient for an arbitrary infinite upper-triangular operator without the relevant additional argument.

Allow gamma=0, repeated Hessian eigenvalues, n=b=1, b=n, and initialization at z^star. Do not require strict inequality between the smallest and largest Hessian eigenvalues. Do not require uniform convergence as k tends to infinity.

The source's ell_k-norm moment conclusion is equivalent to the public Euclidean kth-moment conclusion in fixed finite dimension. A proof using that comparison is valid. No unresolved reference-proof obligation is being treated as a completed scoring step.
