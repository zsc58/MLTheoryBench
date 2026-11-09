# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Constructs one smooth learned field independent of grid resolution and proves the uniform forward-marginal squared score error is at most the prescribed tolerance. For the reference construction, the cutoff must vanish near zero so nonintegral powers cause no loss of smoothness, and a uniform Gaussian tail envelope must justify the error bound.
- **2 points:** Establishes unique nonexplosive strong learned dynamics and uniform finite-horizon moments of every positive integer order, together with the asserted path-law total-variation bound. The reference route verifies local strong solvability for both learned and exact drifts, uses a coercive estimate and stopped Lyapunov bounds, and couples the processes through a common initial value and Brownian motion until the exact path exits the region where the drifts agree. A valid alternative route is equally acceptable.
- **2 points:** Proves convergence in probability on the specified geometric time grids under the common initial draw and Brownian-increment coupling. The reference route verifies the globally Lipschitz truncated Euler theorem's hypotheses and transfers convergence using a buffered no-exit event. An unsupported assertion of grid-uniform raw Euler moment bounds is not a substitute for this localization argument.
- **4 points:** Proves rare-event amplification and all distributional conclusions: 1 point for geometric step bounds, a terminal shell, and the independent bounded-noise event with a justified probability lower bound; 1 point for a correct lower recursion and iteration that keeps the trajectory in the active tail; 1 point for showing amplification dominates the rare-event cost for every fixed positive moment order; and 1 point for finite moments at every finite grid, weak convergence, and the fixed-law Wasserstein lower bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

Standard local strong-solvability theory may be invoked without reproving it, provided the invoked version is clear enough to verify applicability: a deterministic jointly continuous drift locally Lipschitz in space uniformly on compact time-space cylinders, unit additive Brownian noise, and an almost surely finite initial value independent of Brownian motion give a pathwise unique maximal adapted strong solution, with failure of continuation only through explosion. The initial value need not be bounded. The learned and exact drifts satisfy these hypotheses by compact smoothness, and their nonexplosion still requires the Lyapunov or another valid argument. The reference supplies a truncation/Picard construction, but solvers are not required to reproduce that construction.

The public experiment uses geometric time levels t_k=delta exp((k/K)log(T/delta)), not uniform time levels. A proof for another mesh must also justify the stated experiment.

In the reference rare-event argument the raw-state lower bound contains the factor 1/K. The K-independent power recursion is for the normalized state |Y_j|/K^{1/alpha}, not for |Y_j| itself. Equivalent rescalings or exact iterations retaining the factor 1/K are acceptable. Dropping that factor without justification is not a correct amplification step.

Independence of terminal initialization from Brownian increments is part of the experiment. Independence across different grid resolutions is neither assumed nor required.

The learned field, radius and associated proof constants must be fixed as the grid resolution tends to infinity. Constants may depend on the fixed source parameters and initial law, but the iteration and event-probability comparisons require constants independent of K. The statement does not require them to be uniform over all initial laws or all parameter choices.

The private construction, its coercivity estimate, and the normalized cascade are proof methods, not additional public hypotheses. No specialized Euler-divergence theorem or unresolved paper-specific dependency is a completed rubric step.
