# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly differentiates the zero-nudge update through the perturbed equilibrium and proves the required orthogonality \(\langle\nabla_zE(z_0;\theta),y\rangle=0\) from constrained optimality and the retained input constraint, for both schemes. The argument must be consistent with the perturbed state at zero being the free minimizer.
- **4 points:** Derives \(\sum_i F_i'\partial_{\theta_i}\nabla_zE=\nabla_zE\) from separability and uses it with the update to prove \(dM/dt=0\), hence constancy on the specified intervals. Merely naming a conservation principle without this derivation is insufficient.
- **2 points:** Correctly specializes the argument to the conductance graph energy and obtains conservation of the positive squared conductance mass, accounting for constant normalization.
- **1 point:** Correctly handles the resistance specialization, including that the antiderivative is negative and that a constant rescaling of its conserved value yields the stated positive squared resistance mass.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its explicit regularity observation for the separable factors, or use of Lagrange multipliers rather than feasible directional derivatives.

Strict convexity alone does not imply a positive-definite Hessian. The public assumptions also do not require independent constraint columns. Accordingly, do not accept a proof that relies on the existence of a bordered-Hessian inverse without establishing the needed hypotheses or replacing that step by a valid argument. Neither such an inverse nor an explicit formula for the perturbation direction is required for full credit.

The task concerns trajectories within the stated parameter domain, with the stated equilibrium and differentiability assumptions. It does not require a proof of global ODE existence, positivity preservation, or continuation after circuit parameters reach a boundary. No private reference-proof obligation remains unresolved.
