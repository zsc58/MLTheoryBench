# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly maps the projected-gradient update to the hidden coordinates, obtains the hidden supporting gradient with a valid norm bound, localizes both updates, and derives their common local quadratic model using the Hessian compatibility condition. The updates and hindsight comparator must be well defined.
- **4 points:** Establishes an order-eta-squared one-step discrepancy by bounding both Taylor-remainder gradients and directly comparing the two first-order optimality conditions, including a valid constrained comparison such as normal-cone monotonicity. Merely asserting a coupling or naming a method is insufficient. The transformed projected-gradient objective need not be convex, but the necessary first-order inequalities must be justified on the convex feasible set.
- **3 points:** Derives a valid perturbed mirror-descent regret inequality, telescopes the Bregman terms at the actual hidden iterates, verifies the convexity reduction to external regret, and chooses a positive step size of order `T^{-1/2}` with constants depending only on `L,M,B`.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The final rate alone does not compensate for an unsupported coupling or perturbed mirror-descent reduction.

The hidden-gradient estimate supplied by the assumptions is `||a_t||_2<=L M`. Consequently a Euclidean mirror-descent bound using that estimate has gradient-cost term at most `eta L^2 M^2 T/2`. A bound using only `eta L^2 T/2` requires a separate valid justification and must not be accepted merely because an inherited lemma is cited. The private source-repair ledger corrects the supplied paper's normalization; it does not authorize an extra hypothesis such as `M<=1`.

The mirror step used for the one-step comparison is centered at the actual current hidden iterate. Do not accept an independent, persistent mirror trajectory in its place without proving the additional comparison that such a proof would require.

For the Taylor estimates, either explicit differentiation of the exact remainders or another fully justified derivation is sufficient. No fourth derivative of `Psi`, third derivative of `phi^{-1}`, or smoothness assumption on the losses beyond the public setup may be imposed without justification.

The task does not require optimizing the leading constant. For example, a proved estimate `Reg_T<=B/eta+A eta T` with `A` depending only on the displayed parameters permits `eta=T^{-1/2}` and already gives full credit for the final rate. If the optimizing step size `sqrt(B/(AT))` is used, its positivity and any required upper bound must be checked using `B>0`, `A>0`, and a suitable threshold `T_0`.

Do not require nonempty interior or exclude singleton domains. Boundary-constrained minimizers are allowed. The proof must hold for arbitrary admissible online loss sequences; it must not add an oblivious-adversary restriction. A specialized external perturbed-mirror-descent citation alone does not close a missing derivation in this self-contained task.
