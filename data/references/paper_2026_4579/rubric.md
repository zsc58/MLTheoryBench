# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses realizability and the conditional Bellman equation to establish that theta-star is a policy-independent root, and correctly uses the assumed greedy root at theta-diamond. The positive-beta axis identity is a valid way to connect the second root to the second Bellman equation, but need not be reproved when the root assumption is used directly. Do not require or accept samplewise vanishing of the random Bellman residual.
- **3 points:** Exploits unique greedy actions to obtain local affine fields and proves that the greedy Jacobians are nonsingular Hurwitz. A direct stationary Cauchy-Schwarz argument giving v^T A v <= -(1-gamma)v^T R v suffices. Alternatively, an accurately stated on-policy TD result may be used with its hypotheses checked.
- **3 points:** Justifies quantitative local C^1 convergence of the actual tamed-Gibbs policy, including its theta-dependent normalization, and of the stationary mean fields. Uses this control in a quantitative implicit-function or contraction argument to obtain the second root with displacement O(epsilon+1/kappa), with a constant independent of epsilon and kappa in the asserted regime. Within this component, policy control, stationary-law/mean-field control, and quantitative root persistence each account for one point.
- **2 points:** Proves exploratory Jacobian control and transfers Hurwitzness and local asymptotic stability to both equilibria. Includes epsilon-greedy exploration with the same fixed pmf nu, displacement O(epsilon), and kappa=infinity.

# Evaluator Notes

Accept any correct alternative proof. The fixed exploration pmf need not be uniform or have full support; use the assumptions actually stated in the task.

Do not award the perturbation points for merely asserting continuity. Both the rate and derivative control needed for root persistence and stability must be justified. In particular, differentiation of the exploratory mean field must account for its parameter-dependent stationary law. The stationary-law argument must remain valid at deterministic greedy policies, where some state-action probabilities can vanish; no unprovided irreducibility or aperiodicity assumption on these greedy chains may be imposed.

A valid treatment of the parameter 1/kappa at zero or a direct small-C^1-perturbation argument is acceptable. Merely naming the Implicit Function Theorem without checking an applicable extension or providing quantitative perturbation control is incomplete.

The exploration-chain assumptions inherited from the source must remain part of the public contract, but a solver need not use every assumption. No proof of global drift, stochastic-iterate boundedness, general PBE existence, or stochastic-approximation convergence is requested. In particular, theory_005 and theory_012 are not black-box proof obligations for this local theorem.
