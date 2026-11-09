# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the blockwise performance identity or an equivalent directional-derivative representation, and correctly shows that the block occupancy differs from the initial distribution in total variation norm (the discrete \(\ell_1\) norm) by at most \(2\gamma^k\). If the derivative is obtained by passing to a limit of occupancy measures, justifies that passage by a finite-block mixture argument or an equivalent valid argument.
- **4 points:** Establishes the approximate gradient-dominance inequality
  \[
  \langle\nabla f(q),r-q\rangle\leq\frac{f(r)-f(q)}{1-\gamma^k}+\frac{6\gamma^k c_{\max}}{(1-\gamma^k)(1-\gamma)},
  \]
  or a stronger bound sufficient for the target, including both the occupancy replacement and the one-block continuation comparison. The cost scale \(c_{\max}\) and the factor \((1-\gamma^k)^{-1}\) must be retained in the error terms. Merely invoking a named principle is insufficient.
- **3 points:** Proves the Bregman three-point mirror-descent inequality and combines smoothness and strong convexity at \(\eta=\lambda/\beta\) to obtain descent and the telescoping averaged directional-derivative bound.
- **1 point:** Correctly converts the averaged bound to the last blockwise iterate and performs the final first-\(k\)-steps/tail comparison, obtaining the stated constant \(8\) and the stated \(T^{-1}\) term, or a stronger inequality implying the target.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices; assign equivalent credit to alternative arguments that close the same mathematical obligations.

The comparator is optimal among the deterministic policies, not necessarily among the blockwise mixtures. Do not accept a proof that assumes convexity of \(f\), nonnegative blockwise objective gaps, or strictly positive mixture weights without justification. Feasible one-sided derivatives suffice at boundary points under the task's differentiability assumptions.

The target is the finite-T last-iterate performance inequality. Convergence of the policy vectors is not required, and objective descent alone should not be credited as a proof of that stronger assertion.
