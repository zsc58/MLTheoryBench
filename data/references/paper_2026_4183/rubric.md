# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formulates feasible one-sided convex perturbations and derives the linearized state-sensitivity equation. Justifies the first variation using the explicit C1 assumptions and uniform bounds, rather than assuming differentiability of the control-to-state map without explanation.
- **4 points:** Differentiates the population terminal cross-entropy with the label fixed by the initial input; obtains the readout-transposed, token-normalized softmax-residual terminal condition; establishes sufficient integrability or uniform bounds; and performs the adjoint cancellation to obtain the derivative inequality with D_uF evaluated at u*. Uses convergence in the local-minimality topology to justify the nonnegative one-sided derivative.
- **2 points:** Justifies the finite needle expansion using the Hamiltonian based on F(S_t^*;a), with an o(h) remainder, and invokes strong L1 local minimality. Localizes using Lebesgue differentiation and obtains one exceptional null set for all a in Theta, for example by a countable dense subset and continuity.
- **2 points:** Derives interior stationarity, including the zeta factor and transpose pairing. A signed-variation proof must first localize to sets with a uniform positive boundary distance and then exhaust the interior times. A direct differentiation argument at the pointwise Hamiltonian minimum is equally acceptable. Divides by zeta only where zeta>0 and does not assume uniform interiority or nonempty interior.

# Evaluator Notes

Accept any correct alternative proof and any equivalent allocation of routine estimates within it. A correctly stated standard ODE variation result may replace an explicit remainder calculation if its hypotheses are checked. A named needle method without a relevant expansion or justification does not by itself close the finite-variation step.

Distinguish the derivative Hamiltonian at u* from the finite-control Hamiltonian used for needle replacements; conflating them for nonlinear F is a major error. Controls and comparison values are shared across the population, so a particlewise optimization statement is not a substitute for the averaged one.

Do not require explicit differentiation of every attention or feed-forward coordinate: the task supplies the necessary regularity of the field. Do not require a globally convex admissible class in the first part, since feasibility of each comparison interpolation is stated separately.

Pointwise interiority alone does not make every bounded signed perturbation feasible with one common positive amplitude. An omitted boundary-distance exhaustion is a readily repairable omission when the argument otherwise correctly localizes; imposing uniform interiority instead changes the hypotheses. Likewise, an omitted dense-subset argument is a local completion when continuity and the fixed-a inequalities have already been established, but proving only unrelated fixed-a statements is not a proof of the simultaneous quantifier without that completion.
