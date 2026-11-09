# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Projection and truncation comparison (2 points).** Defines the truncated additive target including its intercept, verifies its feasibility in the full coefficient ball, and proves the full-error comparison using the closed-convex projection inequality and orthogonality of the discarded tail. Establishes a squared tail bound of order J_t^{-2s}. Distinguishes projection onto the coefficient-constrained convex set from orthogonal projection onto the retained linear span.
2. **Nonlinear pinball cross-term (3 points).** Conditions on the preceding history and derives the conditional-CDF difference by integrating the density, or uses another argument valid under absolute continuity of the conditional distribution. Uses the positive density bounds to obtain contraction while controlling the retained/discarded mixed term. Keeps conditional and unconditional expectations consistent. A point-value mean-value formula requires additional justification and cannot be assumed from absolute continuity alone.
3. **Mini-batch second moment and recursion (3 points).** Uses conditional independence, bounded scores, the full orthonormal system including the intercept, and Bessel's inequality or an equivalent estimate to control both the diagonal and off-diagonal terms. Obtains a bound of the form C J_t/n_t+C' e_{t-1} for the averaged score's second moment, then a contraction-plus-bias-plus-variance recursion after absorbing the quadratic step-size term. Correctly handles n_t=1 and sufficiently early iterations without requiring a small initial step.
4. **Unrolling and rate calculation (2 points).** Correctly iterates the eventual nonnegative scalar recursion and shows that gamma_t=A n_t/N_t and J_t=ceil(N_t^{1/(2s+1)}) yield the required rate for every fixed positive-integer batch sequence with n_t/N_t tending to zero. Supplies a valid product bound and weighted-sum calculation, or a complete equivalent induction argument. Accounts for the finite initial segment and does not assume additional regularity or boundedness of the batch sizes.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, exact constants, or a particular recursion-solving method. A sufficiently large fixed A may be chosen using the density lower bounds; the eventual starting index and implicit rate constant need not be uniform over batch schedules.

Theorem-critical omissions in the cross-term, conditional second moment, or schedule-dependent summation are major gaps. Missing an intercept in an intermediate display, omitting a fixed constant's square, or using an unjustified point-value mean-value expression is not automatically fatal if the surrounding argument admits the immediate corrections described above and otherwise closes the proof. Do not require continuity of the conditional density, finite moments of Y, or residual orthogonality for projection onto the l1 ball. No unresolved reference-proof step is treated as an established result.
