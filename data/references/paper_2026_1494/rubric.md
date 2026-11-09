# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Retraction--exponential control (2 points).** Derives the quadratic deviation bound from the radial second-derivative assumption using Taylor's integral formula, and applies it to admissible update inputs. A full Hessian bound is not an assumption and must not be silently substituted.
2. **Deterministic descent and nonconvex rate (2 points).** Establishes the smoothness-based one-step inequality along a minimizing geodesic, controls the retraction error, absorbs the fourth-order term under the stated step-size regime, and telescopes to the fixed-step O(1/T) average squared-gradient bound.
3. **Deterministic geodesically convex rate (2 points).** Uses the geodesic first-order inequality and diameter control in a valid argument for the final-iterate O(1/(eta T)) gap. For the reference route, explicitly derives the weighted objective-potential increment, completes the square, bounds each increment, and sums it. Merely asserting that displacement terms telescope does not establish this step. Dependence on the fixed deterministic step size is permitted.
4. **Stochastic one-step analysis (2 points).** Correctly handles fresh-sample conditional unbiasedness, variance, bounded moments, and the retraction error. Obtains conditional expected descent with a gradient coefficient bounded below by a positive constant times eta and an O(eta^2 sigma^2) noise contribution, uniformly over admissible stochastic step sizes. Does not lose a factor of two in the second-moment or absorption calculation.
5. **Stochastic rates and step-size specializations (2 points).** Telescopes the stochastic nonconvex descent and proves the convex final-iterate bound O(1/(eta T)+eta^2 T sigma^2), including the weighted noise accumulation if following the reference route. Verifies that constant-within-run choices proportional to T^{-1/2} and T^{-2/3}, with fixed sufficiently small proportionality constants, are admissible and give the stated rates with constants independent of T.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular weights, or a particular choice of minimizing geodesic. No curvature comparison theorem or unique logarithm from each iterate to the minimizer is required. The scalar bound on the convex gap obtained from the diameter may be used to avoid measurable geodesic selections in the stochastic argument.

The regularity assumption controls derivatives along the update ray; a proof must work under that stated assumption. All iterates needed for telescoping, including x_{T+1}, lie in A. The deterministic rates concern a fixed admissible step size. The stochastic constants must remain controlled when the step size is chosen as a function of the horizon.

A minor algebraic or indexing error may receive substantial credit when the corresponding achievement is otherwise established. Failure to control the retraction error, to justify the stochastic noise terms, or to derive a theorem-critical convex increment is not an incidental omission. The reference proof contains no unresolved proof obligation. Zero variance, zero diameter, zero initial gap, and T=1 must not invalidate the argument; a readily repairable omission of one of these cases is a minor issue rather than a failure of the main proof.
