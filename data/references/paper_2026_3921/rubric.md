# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Justifies the risk calculation under the concrete compact-support model and obtains $d\mathcal E/dt=-2\zeta\mathcal I\le0$, or an equally sufficient valid alternative. Establishes finite risk, monotonicity, and a finite limiting risk. Differentiation and integration interchanges must be justified; an unspecified chain-rule assumption is not supplied by the task.
- **2 points:** Proves both directions of the requested stationary-measure characterization and its support formulation. In the stationary-to-zero-dissipation direction, uses a time interval with positive integrated learning rate or another valid argument that does not assume $\zeta(t)>0$ at every time. Justifies the continuity needed for the support formulation.
- **3 points:** Derives the continuity estimates needed to convert integrated dissipation into $\mathcal I(\rho_t)\to0$, rather than treating dissipation continuity or accumulated-time uniform continuity as given assumptions. A time-change argument must remain valid when the learning rate vanishes or has zero intervals. Justifies the nonnegative-integrable-uniformly-continuous implication, or supplies a valid alternative, and then proves every $W_1$ omega-limit point is stationary.
- **3 points:** Establishes nonempty compact connected omega-limit geometry under the stated precompactness and trajectory continuity, applies total disconnectedness of $\Omega\cap\mathsf{Stat}$ to obtain a singleton, and proves full $W_1$ convergence rather than only subsequential convergence.

# Evaluator Notes

Accept a complete valid alternative proof and allocate the corresponding points by mathematical content. Do not require the reference proof's constants, notation, order of presentation, or particular choice of fixed test functions. Standard independent results may be used when their relevant hypotheses and application are justified; merely naming a gradient-flow framework, Barbalat's lemma, or a LaSalle principle does not replace a theorem-critical argument.

The output matrix $W_{\rm out}$ is fixed and is not differentiated as a particle coordinate. All parameter measures have the same compact support domain; the concrete attention formula supplies bounded smooth derivatives on bounded parameter regions. A solver need not prove existence of the stipulated trajectory, prove a confinement mechanism, or derive the assumed precompactness.

The learning rate is allowed to vanish. Do not demand a strictly positive lower bound or accept division by $\zeta$ without addressing its zeros. The compact support need not have interior, and the weak equation uses ambient gradients rather than projected or reflected dynamics. Degenerate cases such as one class or a zero output projection require no extra nondegeneracy assumption.

The final conditional claim uses $\Omega\cap\mathsf{Stat}$, not an additionally assumed total-disconnectedness condition on the entire trajectory closure. Global optimality, convergence rates, finite-head approximation, and local stability are not part of the task.
