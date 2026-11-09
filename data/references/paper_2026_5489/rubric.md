# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Forward reduction on the sparse manifold (2 points).** Computes the unchanged data tokens and normalized query update, proves the normalized \((I+\rho XX^{\mathsf T})^L\) formula through all shared loops, and identifies the restricted objective with \(R_L(\rho)\). Respects full-token normalization and does not assume that a lower query block has unit norm at arbitrary parameters.
2. **Gradient invariance and symmetry reduction (3 points).** Proves vanishing of all inactive full-parameter gradients through the entire shared-loop computation. A valid first-variation argument tracks the top data-token variation and bottom query variation; it need not make the whole trajectory variation vanish. Justifies differentiation under expectation by a uniform local lower bound on normalization denominators and a dominating derivative bound. Establishes rotational equivariance, obtains scalar identity active gradients by a valid commutant argument, and derives the exact coefficients \((v/d)R_L'(wv)\) and \((w/d)R_L'(wv)\). Closes the full-GD invariance induction from \(w_0=0,v_0=1\).
3. **Scalar dynamics (3 points).** Establishes strict negativity and continuity of \(R_L'\), together with a derivative bound sufficient for the given step size. Handles the zero initial product and proves nonnegativity, monotonicity, and \(\rho_t\to\infty\). Gives a rigorous balancing argument, for example the exact bounded-difference-of-squares recursion, and proves \(w_t/v_t\to1\). Derives the product increment asymptotic, justifies telescoping of squared-product increments, and obtains \(\rho_t\sim(4\eta\Upsilon_1t/d)^{1/2}\) and quarter-power growth of both factors.
4. **Asymptotic constant, loss, and power-method limit (2 points).** Proves existence and strict positivity of \(\Upsilon_1\) and the inverse-square derivative asymptotic, with an explicit integrable domination justified by the inverse-smallest-eigenvalue assumption. Establishes the defined limiting risk by dominated convergence and proves it is strictly positive. Integrates the derivative asymptotic to obtain the stated parameter-scaled loss bound and \(O(t^{-1/2})\) rate. Proves the pointwise normalized power-iterate limit for every fixed unit-column, positive-definite input and unit query.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or award the same calculation twice merely because it supports two core steps.

The multiplicity is \(r(X)\), not a constant across samples. A solution must not add a constant-multiplicity assumption, a deterministic spectral lower bound, independent data columns, a higher inverse-eigenvalue moment, or a uniform positive spectral-gap bound. The stipulated initialization is \(w_0=0,v_0=1\); an argument that only starts from two positive coordinates must justify the first step.

Differentiating the two-scalar restricted objective alone does not establish invariance under full-matrix gradient descent. Likewise, naming dominated convergence without identifying a sufficient dominating bound does not close a theorem-critical limit exchange.

The needed symmetry result concerns the defining rotation action in dimension at least three. Accept a correct standard statement or an elementary coordinate-rotation proof. Do not require or accept as a sufficient justification the false general claim that every irreducible real representation has only scalar commuting operators.

All asymptotics concern fixed model parameters and a fixed data law. No uniformity over data distributions is required. The fixed-input conclusion does not require the query to have a nonzero principal projection when the input covariance is positive definite.

The repaired reference proof is complete; there are no unresolved ground-truth obligations.
