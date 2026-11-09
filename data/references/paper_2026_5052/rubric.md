# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Uses the stated paired-observation model, clipped population coefficient, residual difficulty, continuous oracle and terminal allocation regret correctly. Respects the covariance/variance ratio's denominator s, the residual sample variance's denominator s-1, the zero-denominator convention, and the source-faithful stopping rule. Establishes the oracle identities needed later and chooses calibration constants before B and delta, with only the allowed dependence. Restating definitions alone does not earn all credit.

2. **(3 points)** Establishes a simultaneous high-probability event over all units and deterministic sample sizes. Controls empirical moments and the coefficient denominator, applies clipping, and obtains residual-standard-deviation concentration uniformly over the fitted coefficient's domain. When using a grid, includes its cardinality and interpolation error. States any invoked standard concentration theorem precisely enough to verify its hypotheses and normalization. Obtains both optimism and an upper confidence-envelope bound, and correctly explains why the event applies at adaptive counts. Valid alternatives, including a different complete route to the same event, receive full credit.

3. **(3 points)** Gives a quantitative allocation argument rather than merely naming UCB or a pigeonhole method. For a last-selected-unit proof, identifies an adaptively selected unit through the post-initialization budget, uses that every unit is feasible at its last selection, controls its pre-selection count, derives lower bounds on every terminal count, and obtains upper deviations from the budget constraint. Retains the initialization contribution K sum_q c_q and the bounded remainder. Establishes the O(sqrt(B log(QT_max/delta))) gap and linear lower count bounds in a regime where they justify the subsequent quadratic estimate, or supplies a complete alternative regret argument.

4. **(2 points)** Converts allocation control to the required expected regret and covers the entire stated confidence range. In a Taylor proof, the first-order term equals the nonnegative quantity Lambda^2 Rem/B^2; the second-order denominator must be bounded using an established linear count lower bound. Handles log(QT_max/delta) comparable to B without assuming it is o(B), for example by the deterministic initialization bound K>=constant times log(QT_max/delta). Uses P(E^c)<=delta and the deterministic V_max bound, preserves constants independent of B and delta, and proves feasibility and the stated rate for delta=B^-2.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the stated assumptions and target. The point allocations describe mathematical obligations, not mandatory proof techniques.

The objective in the task is an allocation-quality criterion. Do not require, or accept as an unsupported substitute, an identity equating A_q/n_{q,B} with the exact finite-sample conditional MSE of the fitted estimator at an adaptive sample size.

The standard bounded sample-standard-deviation inequality may be invoked without reproving it if its relevant statement and hypotheses are correctly given. Merely naming a concentration theorem, UCB argument, or Taylor method does not establish the corresponding obligation.

The constants may be existential or explicit, but they must be selected independently of B and delta. The public task does not assume log(1/delta)=o(B). A proof that only covers fixed delta or polynomially small delta is incomplete unless it also handles the remaining initialization-feasible confidence levels. Likewise, initialization is logarithmic, not an O(1) budget loss.

Do not change the specified policy by using residual variance with denominator s, continuing purchases below c_max, or substituting an uncalibrated radius. A solver may analyze such variants additionally, but must establish the requested bound for the stated policy.
