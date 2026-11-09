# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly establishes that the shifted Gaussian expectations are finite and derives the Gaussian score representation of the smoothed gradient under the stated nominal square-integrability hypothesis. Provides a valid differentiation justification or invokes an explicitly stated applicable standard result. Proves both necessity and sufficiency of C>=sigma^2||G||_2^2 and the affine equality case, understood almost surely and including G=0.
- **4 points:** Solves the fixed-perturbation variational problem under the exact gradient and variance constraints. Identifies or equivalently handles the likelihood-ratio residual, derives its squared norm D(r), proves a globally valid sharp bound, and verifies that the displayed signed extremizer has the required moments and attains the maximum. Handles the zero-residual-variance case without dividing by k_delta and treats delta=0 separately.
- **2 points:** Correctly handles the absolute objective while preserving the exact gradient constraint and maximizes over directions. Proves that the positive gradient-aligned perturbation can attain the sphere optimum when G is nonzero and that the value is direction-independent when G=0. Does not assert uniqueness of the positive direction for the absolute objective.
- **2 points:** Obtains the exact Phi(R) expression, justifies maximization over the ball at radius R, and proves the uniform certified-radius criterion and its extended-real endpoint. Includes R=0, epsilon=0, and C=G=0, where all finite radii are certified and the supremum is +infinity. Justifies attainment when the endpoint is finite.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular orthogonal-decomposition notation.

Single-point integrability of f times the Gaussian score is not alone a justification for differentiating under the integral; accept a locally uniform domination argument, an L^2 differentiation argument, or an applicable standard Gaussian-convolution theorem with its hypotheses checked.

Do not accept functional stationarity alone as proof of a global maximum without a sufficiency argument or independently applicable optimization theorem.

At fixed G, replacing f by -f generally changes the constraint. Accept the two residual signs or another valid argument that preserves G.

The arbitrary constant m is allowed; no mean constraint or pointwise output bound is imposed. The task uses exact population quantities, not finite-sample estimates or confidence intervals.

Do not penalize a solver for stating that the negative aligned direction is also optimal for the absolute objective. The public claim asks only that the positive aligned direction may be chosen.

The certified radius is uniform over the specified admissible class. It need not be the largest robust radius of a particular individual function. No finite computational search cap is part of the task.

All reference-proof obligations are closed; no unresolved specialized result should be treated as a completed step merely because it is named or cited.
