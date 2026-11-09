# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the Gaussian infinite-prompt operator and the quartic population risk, including a=mu^T Sigma mu and b=mu^T Sigma^2 mu.
- **3 points:** Solves the population critical-point equations without an invalid coordinate subtraction, proves completeness of the critical set, and correctly classifies zero, all eigendirection critical points, and the two global minima. Handles d=1, where there are no saddles. Coercivity and attainment, or an equivalent direct argument, justify global minimality.
- **3 points:** Establishes the finite-prompt transfer for the deterministic whole-prompt population risk with the query included in the prompt. Supplies compact-uniform convergence sufficient for C2 risk convergence, justifies differentiation and tail control, proves unique persistence and preservation of Hessian inertia, excludes additional critical points on the compact complement, and proves eventual forward invariance of the sufficiently large fixed balls with the stated quantifier order.
- **2 points:** Proves convergence to an individual critical point for bounded trajectories and applies a valid stable-manifold null-basin argument to obtain almost-everywhere convergence for the population and sufficiently large finite risks. Establishes convergence of the finite leading minima to the population leading pair.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, quantitative concentration exponents, exponential rates, or an analyticity-based convergence theorem. C2 regularity, energy dissipation, and a finite critical set suffice for the bounded-flow convergence argument.

The finite risk averages over X_1,...,X_L and reconstructs X_1 using a prompt containing X_1. A proof for a fixed empirical prompt with an independent query does not prove this task. There is no almost-sure qualifier on the deterministic risks or on their sufficiently-large-L threshold.

Pointwise almost-sure operator convergence alone does not establish compact-uniform C2 convergence of risks. Require justified control of derivatives through order two and the relevant expectations, or another complete mechanism proving the finite landscape. Do not accept an unexplained citation to a paper-specific concentration result as closure of this obligation.

For persistence, local Hessian invertibility alone is not a proof of uniqueness throughout a neighborhood. A sufficiently small fixed-center Hessian comparison, a contraction argument, or a correctly applied persistence theorem with checked hypotheses is acceptable. Exclusion of extra critical points requires a compact set separated from the limiting critical points.

A radius containing one trajectory is not automatically a forward-invariant ball for all initializations. The compact confinement and threshold must have the quantifiers in the public statement. Finite minima need only be strict local minima; no global finite-risk claim outside the ball is required.

Treat omission of the finite C2 transfer or equivalent landscape mechanism, compact confinement, convergence to a point, or generic saddle avoidance as a theorem-critical gap. The reference proof closes these obligations and carries no GT quality warning.
