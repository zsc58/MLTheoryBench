# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Establish simultaneous high-probability near-uniformity of the normalized input pair probabilities. State the spherical concentration estimate used, verify its sampling hypotheses, choose a sufficiently small fixed exponential sample-size constant, perform the union bound with a positive remaining exponent, and correctly normalize the conditional rows and unordered-pair symmetrization.
2. **2 points:** Compare every global minimizer with the collapsed embedding and derive D(P||U), D(P||Q)=O(d^{-1+2delta})=o(r^6). Use Pinsker and the total-variation triangle inequality, or another valid argument, to obtain TV(U,Q)=o(r^3). A bound on TV(P,Q) alone does not establish this conclusion.
3. **3 points:** Prove the radius-r concentration conclusion quantitatively. For the reference route, justify a uniform planar annulus-counting bound, handle the finite pair-distance quantile and ties, and show that two pair sets of uniform mass at least r have Cauchy weights separated enough to force TV(U,Q)>=b r^3 when the quantile is at least r. Include the averaging argument and the open-ball conclusion when the quantile is less than r. Accept a complete valid alternative geometric argument.
4. **3 points:** Control every remaining point. Establish the normalization lower bound from the concentrated points and use the correctly differentiated unordered-pair objective. For the reference route, project stationarity at a maximum-norm point, justify the interior/exterior weighted-sum comparison, and derive x=O(sqrt(r)) in the bounded-norm case. Exclude the large-norm case by a valid objective comparison, controlling the common normalization and retaining multiplicative errors on an unbounded log(1+x^2). The source-grounded reference uses a finite move to the center; unsupported claims of monotonic descent along the whole segment are insufficient.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental constants, annulus-density threshold, notation, or presentation choices. The sample-size qualification and positive union-bound exponent, objective comparison, passage from P to U, quantitative planar concentration, and control of all outliers are theorem-critical. A paper-specific supporting lemma must be proved or replaced by an independently justified argument; merely naming it does not close the obligation. Standard Pinsker and spherical concentration may be used when their relevant statements and hypotheses are made clear. Numerical gradient prefactors that do not affect a correctly derived stationary equation should not by themselves cause a major deduction.

The reference proof has no unresolved theorem-critical obligation. Do not infer existence of a global minimizer as an additional target: the public claim concerns every configuration attaining the global minimum.
