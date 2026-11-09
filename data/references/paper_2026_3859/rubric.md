# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly parameterizes affine combinations through \(\beta=\Theta^Tr\), verifies the mass-one constraint, and uses no-cancellation and marginal linear independence to force \(\beta=e_i\). Uses square invertibility to obtain the unique vector \(r_i\), verifies its feasibility, and justifies the applicability of characteristic-kernel injectivity to the signed measures, yielding exactly the stated population zeros.
- **3 points:** Derives the stated high-probability uniform PM-MMD deviation bound, with valid dependence on \(K,\bar r,L,\delta\), and \(\sum_l n_l^{-1/2}\). Controls ordinary and product empirical embeddings, including dependence and bias from the diagonal terms when both marginal factors come from the same sample. Uses a valid simultaneous event and coefficient bounds to obtain the constant 10 or a stronger bound implying it.
- **3 points:** Uses positive-definite tangent Hessians and continuity to choose separated convex neighborhoods with a uniform local Hessian lower bound and quadratic growth. Combines the exact zero characterization with compactness to obtain a positive gap away from the targets, and establishes the population low-level-set decomposition. Treats an empty target set or a singleton domain directly when applicable.
- **2 points:** Validly transfers the decomposition to the defined empirical criterion. In the reference route, derives that both squared criteria have degree at most four and proves that uniform approximation on the fixed full-dimensional affine search domain controls tangent Hessians within this finite-dimensional polynomial space. Then chooses deterministic smallness constants, excludes points outside the neighborhoods, includes every target, proves each local empirical sublevel set connected, and establishes that these are exactly the connected components.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's notation, neighborhood choices, numerical values of \(\varepsilon_0,c_0\), or incidental presentation. The numerical concentration bound must be established, but any valid stronger bound suffices.

The empirical criterion is specifically the squared RKHS distance using the product of the two empirical marginals, including all diagonal terms. Replacing it with an unbiased statistic, an independently resampled product estimator, or an arbitrary smooth perturbation changes the problem unless equivalence is proved.

Uniform function approximation alone does not imply Hessian approximation or preserve strong convexity. An unsupported assertion that sufficiently small uniform error preserves convexity leaves a theorem-critical gap. The polynomial structure is available from the definitions and must be derived or replaced by another valid structural argument; it must not be imposed as a new hypothesis. In particular, a proof requiring an additional assumed Hessian-error bound does not prove the stated theorem.

A complete proof must cover the stated parameter ranges. It may handle \(R_{12}=\varnothing\), \(L=1\), and \(\varepsilon=c=0\) in short direct cases. Target containment only requires \(\widehat d(r_i)\leq\varepsilon\leq c\), not a strict inequality. Do not require positive-dimensional curvature arguments in the singleton case.

Standard concentration inequalities may be invoked in a correct form with their hypotheses checked. Omitting a theorem-critical concentration calculation, the zero characterization, or the structural justification for connectedness prevents full credit. No unresolved private reference-proof obligation remains.
