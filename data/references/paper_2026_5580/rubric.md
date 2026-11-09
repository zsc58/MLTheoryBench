# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Capacity scheduler and reduction.** Constructs a causal, capacity-feasible randomized retention rule with probability comparable to \(\min\{1,m/(b+1)\}\), proves exponentially small saturation, and correctly reduces ordinary regret to weighted regret. For the reference route, distinguishes the exact conditional mean \(\mathbb E[w_t\mid\text{pre-draw history}]=1-J_t\) from the unconditional first, second, and distinct-index moments. Does not assume a conditional pairwise bound by one. Recognizes that zero backlog makes saturation impossible.
- **3 points: Delayed bandit learner bound.** Defines an implementable delayed update and correctly distinguishes uniform-ball smoothing from the sphere-sampled estimator. Establishes conditional unbiasedness, feasible perturbations, contraction and smoothing error, the fictitious-iterate FTRL inequality, and delayed-iterate stability. Justifies weighted martingale orthogonality by conditioning on the direction-independent scheduler randomization, or by another valid argument. Handles empty pending sets. Merely naming FTRL, smoothing, or a specialized delayed-feedback bound does not establish this step.
- **2 points: Joint moment and backlog control.** Propagates diagonal and distinct-index weight moments through all three terms of the delayed bandit estimate. In particular, controls \(\mathbb E[w_t\sqrt{\sum_{s\in A_t}w_s^2}]\) jointly, rather than separating dependent factors without justification. Obtains the aggregate convex and logarithmically weighted strongly convex estimates with the stated dependence on \(b/m\).
- **3 points: Optimization and both final regimes.** Uses admissible smoothing and learning-rate schedules and establishes both target rates. Treats clipped smoothing by a valid case split or an equivalent bound. In the strong case, bounds the curvature residual supported on saturation instead of dropping it because it is nonnegative. Uses the actual diameter bound \(\operatorname{diam}(\mathcal X)\le2G/\lambda\), not an unjustified inequality for a loose supplied \(D\). Handles saturation uniformly, including zero backlog and arbitrarily small positive \(\rho\), and retains a valid \(T=1\) guarantee. Both clauses are required for full credit.

# Evaluator Notes

Accept a complete valid alternative proof and equivalent parameter schedules. Do not require the reference proof's incidental constants, intermediate notation, or presentation choices. A genuinely different valid proof need not reproduce machinery that it does not use.

For the reference route, the scheduler guarantee, delayed weighted bandit estimate, joint weight-backlog estimate, and curvature calculation are contribution-specific obligations; simply assuming them omits a core step. Standard background may be used when its relevant statement is clear and its hypotheses are satisfied. In particular, the fixed-weight bandit theorem must not be applied to scheduler-dependent weights without explaining why conditioning or another argument validates the application.

The smoothing estimate must not assume \(R\le D/2\), and the proof must not infer \(D\le2G/\lambda\) from the fact that \(D\) is merely an upper bound on the diameter. Either use the actual diameter or explicitly replace the working upper bound by a valid sharper one.

Do not accept deletion of the nonnegative expected curvature residual. Its correct value is a saturation-supported expectation, which is small but need not vanish. Do not accept unclipped parameter substitutions when the radius is capped unless the capped case is separately covered.

No lower bound on \(\rho\) or \(\rho n\) is assumed. An unexplained additive \(GD\) or \(G^2/\lambda\) cannot always be absorbed when \(b=0\); the reference proof avoids that issue because the corresponding saturation terms are then exactly zero. The target uses \(\log(eT)\), so the one-round case is included.

Failure of an upstream estimate should affect a final rate only when that rate is not otherwise established. Local presentational omissions should be distinguished from invalid conditioning, missing core estimates, or an unproved final regime.
