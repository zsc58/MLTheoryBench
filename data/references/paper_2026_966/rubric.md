# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Translate the monotonicity family into linear constraints (3 points).** Correctly represents each conjunction of pairwise increment events by fixed 0/1 indicators and derives the lower/upper linear inequalities for all w. The essential justification is that the indicator-weighted sum is exactly the probability of the conjunction. Merely observing that the displayed inequalities are linear does not establish this equivalence.
2. **Construct the complete feasible LP system (2 points).** Includes the probability simplex, the applicable experimental and/or observational marginals under consistency, and any stated exogeneity equations. Correctly verifies that optional exogeneity is independence of each Y_k from X: observational data fix q_l, whereas experimental-only data fix a_{kj} and leave the treatment marginal variable. The imposed equations must be equivalent to these law restrictions, not to independence of the entire potential-outcome vector.
3. **Establish LP attainment (2 points).** Shows the feasible set is a nonempty compact polytope and the linear objective therefore has both minimum and maximum, or gives an equivalent valid argument establishing attainment. No full-dimensionality, strict positivity, LP duality, or particular optimization algorithm is required.
4. **Prove sharpness and the target bounds (3 points).** Shows every admissible law maps into the feasible set and every feasible vector is realizable as an admissible finite joint distribution, so the attained extrema are valid and cannot be tightened. The constructed observed outcome must satisfy Y=Y_X, and all applicable data, event, and exogeneity restrictions must hold.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its explicit structural-causal-model representation; the public target is stated over joint laws.

A concise finite-state probability calculation can establish several equivalences at once. Do not require separate repetition of every displayed marginal equation.

Do not accept substitution of full-vector independence for coordinatewise exogeneity, or introduction of a fixed treatment distribution in the experimental-only regime. These change the feasible class.

The conventional empty product and empty intersection cover d_X=1. Zero cells, zero treatment probabilities, d_Y=1, constant objectives, and lower-dimensional feasible sets are allowed. A proof that applies uniformly to these cases does not need separate case discussions. Do not require positivity or conditional probabilities.

All reference-proof obligations are closed; there is no private ground-truth quality exception.
