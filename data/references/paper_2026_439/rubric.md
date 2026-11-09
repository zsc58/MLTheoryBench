# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Score propagation and reverse Lyapunov control (2 points).** Establishes the needed initial tails and polynomial moments without inferring convexity from radial dissipativity. Derives propagated dissipativity and polynomial score/Jacobian bounds with the correct VE/VP scaling. Obtains conditional reverse-kernel polynomial moment estimates, including strict quadratic drift on positive-noise grid intervals. An equivalent valid argument is acceptable.

2. **Localized minorization and geometric forgetting (3 points).** Proves bounded-ball minorization using nondegenerate grid transitions, including a step ending at data time. Verifies drift and minorization hypotheses and obtains a single b>0 and a single contraction factor below one for all grid kernels. Merely naming Harris earns at most one point here. A valid common-weight construction chooses a weight in the common admissible range; asserting that individually valid weights can simply be enlarged is insufficient.

3. **Initialization and one-step learned-kernel error (2 points).** Proves the regime-specific initialization estimate with the task's corrected mixing constant. The unweighted part of rho_b is 2TV, so Pinsker contributes sqrt(2), not 1/sqrt(2). Establishes a local estimate with distinct Delta and sqrt(Delta) terms and integrates it using the stated chain moments. A Girsanov proof must verify its finite-energy/localization hypotheses, use the correct KL direction, and justify score evolution up to data time under a conditional reverse start. A correct alternative proof is equally acceptable. The VP entropy estimate may be obtained from a correctly stated standard OU entropy-contraction or Gaussian log-Sobolev result with its hypotheses checked; a bare reference to an unavailable paper-specific result is not a derivation.

4. **Final nonasymptotic bound (3 points).** Correctly compares the exact data law with the learned output, propagates initialization through all exact transitions, and propagates each local discrepancy through its remaining exact transitions. Obtains the factors bar-alpha^N and bar-alpha^{N-k} and the complete initialization/discretization/score-error decomposition. Telescoping is one valid method but is not mandatory if another complete argument proves the same bound.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the particular conditional-Gaussian presentation, the particular Harris coupling construction, or the displayed private choices of local constants. The constants must have the permitted dependencies, and the argument must genuinely justify the asserted local orders rather than conceal the total error inside arbitrary grid-dependent coefficients.

The explicit public mixing prefactor is part of the target and must be respected. Incidental constants in privately constructed discretization and network coefficients may differ. Preserve the finite-grid quantifier order; no grid-uniform contraction bounded away from one is requested.

Treat missing contraction hypotheses, an unjustified common metric, an unclosed local-error bound, or incorrect final geometric weights as theorem-critical gaps. Do not penalize a solver for avoiding the source's erroneous covariance identity or Gaussian bridge formulas. VE identities used in VP require the appropriate scaling factors. A schedule may have jumps or zero plateaus, although every full grid step has positive integrated noise; a proof must not silently assume a differentiable inverse clock.

The reference proof has no outstanding quality warning. Its external OU entropy estimate is independently reconstructed, and the standard weighted-Harris mechanism is explicitly verified. The optional TV and Wasserstein consequences are not a separate core requirement.
