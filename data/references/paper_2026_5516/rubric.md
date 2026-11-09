# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omissions.
- **10:** Fully correct.

# Core Steps

1. **2 points — Boundary and time scaling.** Uses the nonzero sharpness gradient to identify the tangent space and derive the Euclidean projected slow velocity −∇F−(α/β)∇s. Correctly obtains the exit velocity −ρ∇F in the common baseline clock. Does not infer full-spectrum stability from A3.

2. **3 points — Slow loss comparison.** Applies the chain rule, obtains the exact fork coefficient (1−ρ)r_k+(a/b)q_k, and controls the slow derivative sufficiently for the claimed final error. A valid approach uses local Lipschitz bounds for the ordinary gradient inner products and continuity of α/β near its positive fork value, together with d²=2a/b. Do not require an O(u) expansion of the sharpness gradient or of α/β. An alternative stronger estimate earns full credit if it is actually justified from the assumptions.

3. **3 points — Averaging.** Uses the C² Taylor formula at the slow point, the O(d) phase sizes, and cancellation of the mean phase to derive an O_k(d²) error for each averaged loss. Retains this as a value-level error, or supplies a genuinely valid alternative argument. A bound on an error's values does not by itself bound its derivative.

4. **2 points — Integration and conclusion.** Integrates the slow difference from its common initial point, obtaining the linear coefficient and controlled O_k(u²)+O_k(d²u) error; then includes the value-level averaging errors and bounds d²u by U₀d². Obtains the stated conclusion with constants independent of u and identifies the two contributions.

# Evaluator Notes

Accept any complete valid alternative proof. The source's specialized self-stabilization result is not a theorem the solver must establish: the projected local description is explicitly assumed in A2. Nevertheless, merely naming projected dynamics without deriving the required projection coefficient does not close Step 1.

Do not require exact equality of the two averaged initial losses. The common fork gives exact equality of the slow initial losses; the phase averages may differ by O_k(d²), which the target permits. Do not accept an unproved derivative estimate for a phase-averaging remainder or an unsupported sharpness-gradient Taylor expansion. The public theorem is local and conditional; it does not require an approximation theorem for raw discrete iterates, a window uniform over oscillation amplitudes, or uniform constants across subsets.

No sign assumption on r_k or q_k is available. Do not require a mixed-sign corollary, a relation between q_k and top-eigenvector alignment statistics, or a global training claim.
