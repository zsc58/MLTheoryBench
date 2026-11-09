# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Proves that every even function has zero Shapley value, using complement pairing and the symmetry of the Shapley weights or an equivalent valid argument; concludes \(\phi_i(f)=\phi_i(f_{\rm odd})\). If coalition coefficients are used, their indices must be valid at the empty and full coalitions.
- **2 points:** Establishes the odd/even decomposition of admissible functions and proves, in both directions, that the two boundary matching constraints are equivalent to independent odd and even boundary constraints.
- **3 points:** Demonstrates cancellation of all odd-even cross terms under complementary sampling with equal multiplicities and symmetric weights, yielding the sum of the odd and even objectives. A verified orthogonality or reindexing argument is equivalent to expanding the paired squares.
- **2 points:** Uses the independent feasible-set structure and separated objective to establish equality of the complete argmin sets, not merely a relation between selected minimizers. The reasoning must remain valid for empty feasible classes and nonunique solutions, and it identifies the odd fitted component as carrying the fitted Shapley values.

# Evaluator Notes

Accept any complete valid alternative proof. Do not award the central separation points for merely naming orthogonality or paired sampling without justifying the cancellation and constraint arguments. Propagate a missing decomposition or cancellation step to the final argmin conclusion when it leaves that conclusion unsupported.

Do not require a particular proof format for degenerate cases: a general set-membership argument that covers them is sufficient. Do not impose nonempty sampling, feasibility, uniqueness, full rank, or a particular sampling distribution as additional assumptions. A separate proof of minimizer existence is unnecessary when both inclusions of the argmin-set identity are established without presupposing existence. Empty samples, zero-dimensional component spaces, and \(d=1\) are permitted by the public task.

The conclusion concerns the Shapley values of the odd component of each fit. It does not assert exact recovery of the original function's Shapley values from an arbitrary paired sample, and a solver must not be required to prove that stronger claim. Neither Fourier-basis machinery nor an external regression-recovery theorem is required.
