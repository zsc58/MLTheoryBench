# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses weighted mixed primal/dual norms and oracle optimality to establish the one-step descent inequality with momentum error. Uses the valid feasibility bound on the step norm; does not require a nonzero estimate or equality in the ball constraint. Derives the quadratic upper model from gradient Lipschitzness if needed.
- **3 points:** Correctly expands the momentum error into decayed initialization, geometrically weighted centered noise, and gradient drift. Bounds adjacent-gradient differences using mixed-norm Lipschitzness and the step constraint. An expansion using differences from the current gradient must retain the initial-gradient drift term.
- **3 points:** Establishes the dimension-free mixed-norm second-moment estimate. Justifies conditional mini-batch covariance scaling and temporal martingale orthogonality; proves the weighted Schatten trace inequality or gives an equally complete valid derivation; obtains the covariance-factor Schatten norm using the correct spectral power or another justified argument; aggregates blocks using Minkowski in L_{2/beta}; and obtains the summed error bound. Handles singular covariance factors and exponent endpoints without unsupported inverses or undefined powers. No independence between blocks is required.
- **2 points:** Telescopes descent and substitutes the prescribed parameters. Correctly uses sigma_{v,q,B}<=sqrt(Delta_f/K) when theta=1, includes zero noise and K=1, and derives the stated constants. A stronger bound implying the target is acceptable.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a particular comparison-matrix presentation. A paper-specific martingale result cannot simply be invoked without establishing its relevant content. Standard Holder, Jensen, and Minkowski inequalities may be used when their applicable exponents and moment conditions are clear.

Treat an unresolved mixed-norm martingale estimate or unjustified parameter optimization as a theorem-critical gap. The reference proof's former momentum identity, choice of a comparison matrix proportional to V_j V_j^T, and reversed theta=1 inequality are not valid proof steps. Assess an isolated readily repairable slip differently from reliance on a false step that leaves the main estimate unproved. Do not penalize the use of step norm <=eta rather than equality; this is necessary to cover zero oracle estimates.

All reference-proof obligations are closed in the replacement proof; there is no outstanding GT quality warning.
