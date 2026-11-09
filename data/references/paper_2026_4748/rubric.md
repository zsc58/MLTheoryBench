# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the online information structure, statistic-realizing sampling oracle, compact convex domain, bounded RKHS feature operator, and expected-gap definition. Distinguishes a hidden current outcome from one allowed to depend on the fresh forecast draw. Defines and uses the finite-feature/kernel computational model correctly, including its measurable primitive interfaces, and addresses zero-gap degeneracies.
- **3 points:** Constructs admissible finite-support forecast distributions and proves the squared-potential recursion. An efficient construction must have a quantitative certificate, not merely assert that an empty strict feasibility set makes an ellipsoid terminate. Establishes measurable dependence of the computed support points and weights on the available history, for example by a finite arithmetic implementation with measurable oracle calls and fixed tie rules. Controls the cross term with the correct factor two, bounds the increment, and obtains the claimed square-root potential bound. Scaling the operator by two or halving its tolerance are equivalent acceptable normalizations.
- **2 points:** Applies the reproducing identity and Cauchy-Schwarz with the correct ||h||_H dependence and expectation order. For adaptive nonanticipating histories, justifies measurability and the conditional averaging/tower-property step. Obtains the uniform conclusion for an RKHS-bounded class without moving a supremum inside an expectation.
- **1 point:** Proves the exact sufficient-statistic identity between each OI discrepancy and the RKHS residual, using E_{mu_p}s=p.
- **2 points:** Establishes the implementation cost rather than quoting it. Accounts for support sizes, operator evaluations, finite-mixture computation, and updates; obtains total nearly T^2 kernel cost and nearly rT finite-feature cost, or an equivalent valid implementation. Derives the minimum bound and substitutes a horizon of order epsilon^{-2} for unit-ball average statistical error. Distinguishes total computation from per-round computation and statistical error from positive numerical tolerance. Near-linear horizon dependence is asserted only in the finite-feature regime. Charges oracle implementation costs according to the task's model.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A sampled-residual argument is acceptable if its information structure, measurability, constants, and implementation cost are independently established; it is not automatically the source's mean-residual implementation.

Standard independent results such as compact convex finite-dimensional minimax, the central-cut ellipsoid volume theorem, and convex optimization with a first-order oracle may be used with their relevant statements and verified hypotheses. Merely naming defensive forecasting, an EVI algorithm, constructive minimax, or an ellipsoid method does not establish the specialized finite-support construction or its cost.

Do not require a continuity assumption on the forecast-dependent feature map, a separable RKHS, or a standard-Borel context space. Positive-tolerance finite-support construction suffices. Do not demand exact zero-tolerance EVI existence for a discontinuous operator. Joint measurability of the supplied evaluation interfaces is distinct from continuity and from measurability of every fixed RKHS function. A valid proof must use the former, or otherwise establish measurable forecasts; it cannot infer it from the latter. Finite algebraic residual sums and measurable scalar pairings suffice, so a proof need not invoke Hilbert-valued integration.

The public statistical accuracy epsilon concerns A_T, the expected OI gap per round on the RKHS unit ball. The displayed epsilon-complexity is total computation to that accuracy. A proof claiming that it is numerical-accuracy cost per round, or that an arbitrary kernel has nearly linear total cost in T, has not established the computational target.

The source's unnormalized EVI condition has a factor-two error. Do not penalize a solver for correcting it by using half the original tolerance. Conversely, the uncorrected recursion with only one tolerance contribution is not valid. Propagate a missing potential bound to the final guarantee only when the latter is not independently established.
