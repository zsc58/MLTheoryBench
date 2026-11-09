# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points: Spectral compression of the action norm.** Derives the inverse of the low-rank-plus-ridge matrix, identifies the \(K\times K\) Gram matrix, and proves the exact norm/eigenvalue identity, including positive semidefiniteness. Merely asserting that a low-rank identity or matrix formula applies is insufficient.
- **3 points: Constrained projection reduction.** Correctly obtains the optimality system, treats the feasible and active-constraint cases, derives the retained-space and orthogonal-complement coefficients, and proves existence and uniqueness of the positive scalar root by establishing the continuity, strict monotonicity, and endpoint behavior of the scalar function, denoted \(\phi\) in the reference proof. The spectral coefficients must act on the unconstrained vector.
- **2 points: Operation-level cost analysis.** Establishes the per-action costs \(O(Kdm)\), \(O(K^2m)\), and \(O(K^3)\), and shows that the projection and thin spectral updates fit within \(O(Kd(m+K)^2)\) under the stated numerical-accuracy convention. Counts expressed in the effective rank \(q\) must remain valid for \(q=0\); bounds using \(q+1\), a separate zero-rank case, or uniform bounds using \(m+K\) are all acceptable.
- **2 points: Aggregate time and space bounds.** Correctly counts maintained state and reusable working storage, handles thin factors of compatible dimensions, and combines the action and update costs to obtain both full stated bounds, including the condition under which the shorter time expression is valid.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, notation, particular root bracket, or a separate q=0 discussion when the submitted formulas and bounds already cover that case. The two spectral reductions are the central achievements and must be derived rather than named. Direct verification of optimality may replace a KKT-based argument.

Exactness concerns the algebraic identities and projection characterization. Numerical eigenvalue and scalar-root computations are evaluated under the task's explicitly suppressed numerical-accuracy convention. Do not require a finite exact-real numerical algorithm or an unsupported global Newton convergence rate. Bisection or another justified scalar method is acceptable.

Space is maintained state plus auxiliary working memory, not storage of the externally supplied action set or retained reported outputs. A faulty intermediate derivation need not erase credit for a later conclusion that is independently and correctly established. Missing the active projection case, uniqueness of its multiplier, or an entire term of the full complexity bound is theorem-critical.
