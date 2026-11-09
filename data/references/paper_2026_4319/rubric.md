# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes strong Lagrange duality for the stated conditional-kernel problem, rather than only weak duality. A convex-analytic proof must retain source and destination coordinates, justify the relevant compactness or closure, and verify the hypotheses of its duality theorem. The reference route explicitly computes the conjugate and verifies continuity for Fenchel duality. A complete alternative separation, value-function, or minimax argument earns the same credit. The argument must cover a zero budget without an unjustified strict-feasibility assumption.
- **3 points:** Correctly exploits the fibers fixing x to obtain the stated potential and the exact supremum/integral identity. Establishes both inequalities and justifies measurable choices, either by a precisely stated applicable selection result or by an explicit measurable approximate-selection construction. Checks measurability or continuity and integrability of the potential. Distinguishes the unrestricted penalized kernel supremum from the original budget-constrained supremum.
- **3 points:** Proves the pointwise-in-G risk bound with the factor L_G, not sqrt(1+L_G^2). The reference route uses the Lipschitz inequality, quadratic maximization for lambda>L_G^2, and scalar optimization. A complete direct L2 triangle-inequality argument under each feasible joint plan is equally acceptable. Handles epsilon=0, R_G=0, and L_G=0, either explicitly or by an argument valid in all those cases. Does not assume an interior minimizing multiplier exists in a degenerate case.
- **1 point:** Takes the infimum over the same reconstruction class to obtain the stated final inequality, with no assumption of an attained minimizing reconstruction or a common Lipschitz constant. Correctly retains the fidelity integral and the L_G sqrt(epsilon) term.

# Evaluator Notes

Accept every complete valid alternative proof. Do not require use of an auxiliary continuous potential h, a named conjugate, Fenchel duality, exact measurable maximizers, or scalar optimization when another rigorous argument establishes the same obligations. A Tikhonov interpretation is not required by the public task and carries no separate scoring requirement.

Theorem-critical omissions in strong duality, the conditional supremum/integral reduction, or the risk estimate are major gaps. Merely naming a theorem without stating its relevant content and verifying its hypotheses does not close the corresponding obligation. In particular, weak duality alone does not prove the first target, and the compactness of the set of induced second marginals alone does not retain transportation costs.

The adversarial kernel may depend measurably on both x and y. Do not impose a shared conditional law independent of y. Almost-everywhere versions of kernels are sufficient. Approximate Dirac selectors used after dualization need not themselves meet the cost budget.

A solver may use standard compactness, disintegration, separation, and convex-duality facts with their applicable hypotheses checked. Do not require a proof of those standard independent results. Missing an easily supplied zero-case limit may be a minor omission when the proof otherwise covers the stated regime; an essential reliance on strict feasibility at epsilon=0 is a strong-duality gap.
