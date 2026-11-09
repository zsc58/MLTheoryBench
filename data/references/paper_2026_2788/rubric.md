# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the correctly normalized similarity-time equation, compact confinement, and a uniform drift bound, giving local uniform compactness of forward time shifts. Establishes the posterior concentration or equivalent gradient asymptotics needed to identify the limiting field. Value asymptotics may be established by finite Gaussian-sum bounds or the lower-mass estimates; a separate value-convergence calculation is not mandatory in a valid proof that directly establishes all requested conclusions.
- **3 points:** Identifies every subsequential time-shift limit, not merely one selected limit. A weak-* approach must verify measurability and boundedness of the convex constraints and justify their preservation, for example with support functions and countable directions. Establishes genuine Clarke equality in 0<=lambda<=1 by the applicable finite-maximum/minimum structure, and retains the outer-Clarke field for lambda>1. Includes the forward-time integral equation and almost-everywhere solution interpretation.
- **2 points:** Proves autonomous dissipation, including at interfaces, and convergence of every autonomous solution. In the reference route, density-point tangency and common tangential gradients yield the energy identity; coercivity yields boundedness; a uniform energy-drop argument excludes noncritical omega-limit points; and finite-stratum rigidity plus connectedness yields a single limiting critical point. Standard existence results may be used with their upper-semicontinuity, compact-convex-value, and growth hypotheses verified.
- **2 points:** Establishes local-minimizer trapping in both parameter regimes, including nonsmooth CFG minimizers, and transfers convergence to the original rescaled curve. In the reference route, finite criticality and local minimality give a strict surrounding energy barrier; unbounded bad intervals contradict autonomous convergence and the omega-limit exclusion; bounded intervals and endpoint time shifts exclude repeated excursions. Uses finiteness and connectedness to obtain one minimizer and translates convergence back to physical time.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not award credit for merely naming Laplace asymptotics, nonsmooth analysis, or trapping without establishing the corresponding claims. The inclusion-identification and conditional-transfer arguments are theorem-critical obligations.

The lower-mass condition is automatic for finite positive atomic measures and need not be used separately. No generic-position condition, support nesting, or smoothness assumption on CFG minimizers may be imposed. The endpoint cases lambda=0 and lambda=1 must be covered, with inactive terms omitted when necessary. Singleton supports and lower-dimensional strata are permitted.

Do not accept the false inequality ||nabla F_lambda(x,t)||<=2 dist(x,K) from membership in 2(x-K). The valid estimate uses 2 sup_{k in K}||x-k||, or directly 2(||x||+sup_{k in K}||k||). A proof using the correct terminal bound need not discuss the source typo.

A general Clarke sum rule supplies an inclusion, not automatically equality. Likewise, a generic nonsmooth chain-rule citation alone does not establish the exact dissipation identity for the outer inclusion. The relevant finite-support geometry must be justified or replaced by a valid alternative argument.

A quadratic-well argument restricted to the convex-mixture regime does not establish CFG trapping. The energy-barrier proof works without smoothness and must include why the minimizer is strict locally. In transferring autonomous limits, justify that each limiting curve lies in omega(Y) and that its limiting critical point remains in this closed set.

No unresolved ground-truth proof obligation is being treated as an established rubric step.
