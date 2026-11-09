# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes the minimizer-map contraction \(\|G_t(u)-G_t(v)\|\leq(1-\rho_t)\epsilon\beta\|u-v\|/\mu\) from strong convexity, the \(\beta\)-Lipschitz gradient in the data variable, Wasserstein sensitivity, and cancellation or a valid transport bound for the common exogenous component. The map must be well-defined; existence is assumed and uniqueness follows from strong convexity. Accept either the finite objective-contrast argument or a properly justified constrained-gradient argument. Merely naming contraction or a transport theorem without deriving the bound earns at most 1 point.
- **2 points:** Uses the contraction together with the moving comparator definition to derive \(e_{t+1}\leq\gamma e_t+\delta_t\), with the correct indexing and path-length displacement.
- **2 points:** Correctly telescopes or sums the recursion to obtain \(\sum_{t=1}^T e_t\leq(e_1+\sum_{t<T}\delta_t)/(1-\gamma)\) under \(\gamma<1\), with the terminal term handled in the correct direction.
- **3 points:** Converts tracking error to deployed-risk regret using the assumed uniform \(L\)-Lipschitz property and states the complete bound with the correct comparator, initialization term, path length, contraction constant, and expectation scope.

# Evaluator Notes

Accept a complete valid alternative proof, including a correct constrained-optimization or subgradient treatment. Do not require the reference proof's incidental presentation choices. Deduct for theorem-critical gaps in the contraction derivation, recursion summation, or final regret conversion even if the overall architecture is plausible.

The public task does not assume a first moment for \(Q_t\), integrability of all ambient loss gradients under \(Q_t\), or permission to interchange differentiation and expectation. A proof using such quantities must justify them or avoid them; it may not add these assumptions. The finite loss-contrast route is one valid way to avoid these issues. Do not require Kantorovich--Rubinstein duality specifically when a direct coupling argument establishes the needed estimate.

The Lipschitz property of \(R_t\) is a primitive assumption. Do not require the solver to derive it from additional Lipschitz conditions on the loss. Parameter-gradient Lipschitzness, stochastic-gradient variance bounds, and assumptions from other algorithmic branches are not part of this task.

The comparator is specified by its fixed-point relation, so a separate existence proof is not an additional scoring requirement. If a solver supplies one, the contraction on the closed parameter domain justifies it. The fixed initialization and unique exact minimizers make the iterates deterministic; arbitrary randomized initialization is not an additional version of the requested claim.

The argument must be compatible with boundary minimizers, \(T=1\), singleton domains, \(\gamma=0\), and \(L=0\). These cases need not be discussed separately when the displayed reasoning already covers them. An omitted trivial case that is immediately repairable should not be treated as a theorem-critical failure. Stability regret need not be nonnegative.
