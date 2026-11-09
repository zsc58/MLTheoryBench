# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly identifies the query-key subspace, proves that the skew generator has range in it and acts trivially on its orthogonal complement, and derives the exact reduced-exponential identity. Uses the correct basis size r=dim(U), with r<=2d_v, without assuming rank(S)=r.
2. **4 points:** Derives the finite-matrix orthogonality-defect identity and carries out a valid SVD/compressed-series factorization, or an alternative argument proving the same singular-value-sensitive estimate. Merely naming low-rank reduction or Newton-Schulz receives no credit for this step. A factor introduced for the exponential increment must be explicitly defined and its factorization justified; the SVD does not generally diagonalize that increment.
3. **2 points:** Justifies the norm estimates yielding the factor (exp(||S||_2)-1)^2. May invoke the public assumption that all singular values of B lie in [0,1], or establish it from the normalized iteration. Does not need to prove polar convergence. For a series-based proof, supplies a valid termwise estimate rather than merely naming an unspecified exponential-series factor.
4. **2 points:** Computes the singular-value error factor, proves its maximum is at most 1/4 on [0,1], and states both final inequalities with correct dimensions and indexing.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Propagate a failed dependency only when the corresponding downstream conclusion is unsupported; theorem-critical gaps remain major.

Distinguish the r-column exact orthonormal basis C from the m=2d_v-column finite matrix B. A full rectangular SVD or a correctly handled reduced SVD is acceptable, including when N<m or B is rank deficient. No full-rank assumption, nonzero alpha assumption, or initialization distribution may be imposed to bypass the stated cases.

The proof must cover r=0, zero singular values, and S=0, but an argument valid under the public conventions need not discuss each case separately. The public singular-value assumption may be used directly; independently verifying it is not an additional scoring requirement. There are no unresolved reference-proof obligations.
