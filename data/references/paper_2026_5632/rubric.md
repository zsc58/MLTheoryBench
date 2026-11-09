# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Constructs valid data-dependent conditional-mean intervals and proves both simultaneous coverage and the mass-squared radius budget. Defines the radius for unobserved points, handles single observations and non-atoms, justifies the conditional finite union bound, and proves the binomial expectation estimate before applying Markov's inequality.
- **3 points:** Derives a randomized multicalibrated predictor from the interval information. Defines randomized residuals, establishes the finite signed-test minimax and exponential-weights bounds, and performs the population online-to-batch transfer with the entire predictive map fixed before each fresh observation. Verifies the hypotheses of the standard results used and preserves allowed support.
- **4 points:** Establishes deterministic cell-wise rounding. Defines a complete finite measurable partition, including any required tails and cutpoint singletons; handles ties and unseen atoms in the squared-mass estimate; and proves a uniform signed-residual concentration bound using independent cell randomness, correct pointwise marginals, and the atom-sensitive and cell-sensitive ranges. Controls the grid discrepancy pathwise. A cell-wise pair consisting of a uniform online index and an independent uniform seed is valid once these same properties are verified.
- **1 point:** Combines probabilities and universal parameter choices to obtain the stated sample bound and epsilon guarantee, including the polynomial-group specialization, and establishes the implicit representation and polynomial training and query costs in the public computational model. The implementation must include confidence-table and partition lookup, compact online states or another efficient representation, and a query procedure genuinely meeting the logarithmic dependence on sample size.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, numerical constants, or particular allocation of failure probabilities. The frozen target is the deterministic population-calibration upper bound and its implementation claim, not a lower bound or another prediction objective.

Merely asserting that randomized predictions can be rounded, or invoking generic concentration without the atom-sensitive and cell-sensitive control, does not earn the rounding points. Population expectations must hold the trained predictor fixed; calibration averaged over training randomness is not a substitute for the required high-probability guarantee.

Direct inverse-CDF rounding of the averaged predictor is a valid statistical construction, but it does not by itself justify reconstructing only one online state at query time. To close the computational requirement, establish a suitable implementation, such as the source-grounded cell-wise mixture sampler, or prove an alternative query bound. Equality of pointwise sampling marginals does not mean that two shared-seed samplers define the same random function; explain why the chosen sampler satisfies the rounding argument's hypotheses.

Use the public unit-cost group-evaluation and real-operation model. Do not demand that arbitrary measurable group functions have efficient finite programs or require an unstated finite-bit encoding theorem. Conversely, simply calling an unspecified linear program polynomial-time does not establish an encoding-independent bit bound; an explicit real-operation implementation or an appropriately stated applicable result suffices here.

Null sampling endpoints, empty partition cells, zero-mass observed singletons, singleton group families, and zero variance may be handled by explicit conventions or valid probability-one arguments. There are no unresolved reference-proof obligations to waive or award automatically.
