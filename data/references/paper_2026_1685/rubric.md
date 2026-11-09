# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Lift and geometric properties (2 points).** Establish convexity and closedness of the convex-gradient constraint using Brenier correspondence and a valid stability or optimal-plan argument. Distinguish the unconstrained lift F from F+I_K. Transfer lower semicontinuity and lambda-convexity, and justify the lift's gradient formula. A correct statement of the Wasserstein-to-Hilbert differentiability theorem with verified hypotheses is acceptable; alternatively derive it using smooth-gradient approximation and coupling estimates. Brenier uniqueness alone is not a proof of stability.

2. **Global flow existence (2 points).** Apply a correctly stated Hilbert semiconvex subgradient-flow theorem, or give a valid minimizing-movement construction. Check properness, the inherited lower bound, strong lower semicontinuity, lambda-convexity, and finite initial energy. Identify the least-norm constrained subgradient with minus the projected vector field. Obtain H^1 regularity up to time zero on every finite horizon. If using weak compactness for the proximal step, apply weak lower semicontinuity to the convex proximal objective; do not infer it for an arbitrary negatively semiconvex lift. Address compatible finite-horizon solutions when discussing infinite time.

3. **Projection inequalities and dissipation (3 points).** Derive the tangent-cone projection identities, justify an absolutely continuous energy and its dissipation identity, and obtain the endpoint comparison with the correct inequality direction. The normal residual need not have zero pairing with T_*-T_t. A subgradient chain rule with its hypotheses verified is sufficient; merely naming a projected flow or a Lyapunov argument is insufficient.

4. **Rates and map convergence (3 points).** Integrate the comparison to prove the 1/(2t) gap estimate without imposing metrizability. Under the conditional metrizability assumption, use the topology that includes second moments and a valid optimal-map stability argument to prove strong H convergence. Derive the polynomial map estimate using only power growth along the selected flow, with constants independent of time. For positive endpoint convexity, derive the projected Polyak--Lojasiewicz estimate, exponential gap decay, and the stated 4/kappa map bound from endpoint convexity and minimality. Explain extension from a.e. inequalities to the stated all-time bounds. Missing a theorem-critical regime or estimate loses the corresponding credit.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular proof of a standard independent theorem. A theorem invocation must state enough of its hypotheses and conclusion to verify applicability; a paper-specific assertion or specialized method name alone does not discharge an obligation.

Award downstream rate credit when its prerequisites and derivation are independently correct, even if an earlier auxiliary argument is presented differently. Do not demand power growth on all of P_2, metrizability for the bare energy-gap bound, or a separate metrizability hypothesis for the quantitative power-growth estimate. Narrow convergence without second-moment control does not justify strong map convergence. A proof that establishes stronger constants may receive full credit if it also implies every requested bound.

All required proof obligations have a completed justification in the replacement reference proof; there is no unresolved GT exception.
