# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Justifies the constrained inverses and weighted loss as needed, differentiates the free bordered KKT system, obtains the active-edge factorization of the residual Jacobian, and turns rank plus continuity into a uniform positive local coercivity bound. Continuity need only preserve a strictly smaller bound, not the exact pointwise constant.
- **3 points:** Derives the limiting fields and method-specific loss estimates: EP exponential loss decay; the CL negative update-dissipation term together with a proved cubic remainder bound and its absorption near the solution; and the AL gradient identity and uniform adjoint-loss coercivity. Allocate approximately one point to each method.
- **3 points:** Establishes uniform residual and velocity estimates for all three methods and a quantitative first-exit argument keeping trajectories in a compact subset of the positive-conductance neighborhood. Justifies global forward existence by local ODE existence and continuation. The source route uses an IFT chart and a residual-to-distance estimate; if using it, verify the theorem's hypotheses and justify invertibility of the averaged Jacobian by closeness to a fixed invertible block. A complete direct-ball confinement proof that does not need the chart is equally acceptable.
- **2 points:** Establishes integrable velocity, Cauchy convergence of the conductances, the requested exponential residual and weighted/adjoint-loss estimates, and membership of the limit in S for all three methods. For AL, supplies a quantitative comparison of the adjoint multiplier and free residual, not just equality of their zero sets.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the solver to identify source errors or use the reference proof's notation or constants. Do not award full credit for merely naming coercivity, an IFT, or a bootstrap without proving the needed estimates and convergence conclusions.

The CL cubic-remainder control is theorem-critical for the weighted-loss route. CL need not be gradient flow of its weighted loss. If beta is the derivative of its output multiplier with the displayed KKT sign convention, then beta=-Dr while its physical nudge response is RQDr.

For AL, the update must subtract the energy derivative at the fully constrained reference state, not at the free state. The source-grounded identity mu=Dr proves both equality of zero sets and local norm comparison; an equivalent derivation is acceptable. Its coercivity can be proved directly from the fully constrained KKT system or from the adjoint Jacobian at the solution.

A claim that individual Jacobian blocks have bounded inverses does not by itself show that their average is invertible. Uniform closeness to the fixed block at k_* supplies the elementary repair. Similarly, the pointwise active-edge constants need not remain unchanged throughout a neighborhood; smaller positive constants suffice.

The trajectory must stay strictly inside the admissible domain so that its finite-time continuation and limiting state are well-defined. Merely asserting that S is globally closed in R^M is not a substitute. Include stationary initial points on S. If zero-dimensional output spaces are allowed, that case has zero residual, zero losses, and zero fields; it is not an obstruction to the theorem.
