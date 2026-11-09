# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the necessary convex-smooth estimates at the current and perturbed points, including a valid lower bound for the scheduler numerator and an upper bound for the perturbed-gradient norm. Correctly handles or justifies the zero-gradient case.
- **3 points:** Expands the squared-distance recursion, uses convexity at the perturbed point and the adaptive step size, and proves the deterministic one-step decrease \(\|x_{t+1}-x^*\|^2\le\|x_t-x^*\|^2-(1-Lr)^2(f(x_t)-f^*)/(2L)\). This is the central required step.
- **3 points:** Uses strong-convexity quadratic growth in the one-step decrease and correctly unrolls the resulting recurrence with factor \(1-m(1-Lr)^2/(4L)\).
- **2 points:** Telescopes the same decrease in the convex case and applies Jensen's inequality to obtain the Cesaro bound, including the factor \(1/T\) and the dependence on \((1-Lr)^2\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A solution that only asserts a perturbed-gradient descent lemma, or names a standard method without deriving the required inequality under this update and scheduler, does not earn the central-step credit. At \(r=1/L\), the strong-convexity factor equals one and the convex weighted bound is noninformative; do not require strict contraction or division by \((1-Lr)^2\) at that endpoint.
