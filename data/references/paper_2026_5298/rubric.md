# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps for the Drift-and-Projection Route

- **3 points:** Correctly derives the effective coordinatewise endpoint estimate for the marginal-endpoint bridge from exact posterior marginals and the coordinatewise OU bridge likelihood, identifying it with \(\mathbb E[X_{0,l}\mid X_{u_k},X_{u,l}]\). The argument must account for the observed path filtration: conditional on the grid-start state and current state, the already observed bridge segment gives no additional information about the latent endpoint. Product endpoint sampling and independent block likelihoods then reduce the estimate to the current block. Merely asserting that the sampler has more information, or computing only a one-time posterior without justifying the path drift, is insufficient.
- **3 points:** Validly obtains the true and sampler drifts and justifies the full-horizon KL identities with a common finite initialization term and coefficient \(c_u^2/\sigma_u^4\). The public assumptions are explicit full-path absolute continuity and finite initialization entropy; an answer may not simply invoke an additional unspecified global Novikov hypothesis. The endpoint-support argument in the reference proof verifies that the drift differences vanish in this setting and that the required change-of-measure conditions hold. A different complete justification is acceptable. Local arguments on \([0,T-\varepsilon]\) alone do not establish the closed-horizon identity.
- **4 points:** Correctly uses the OU Markov relation, tower property, and nested conditional-expectation projection to compare errors coordinatewise; sums and integrates with justified finiteness; and establishes the strict implication from the positive-measure condition. The condition concerns positive probability under the true forward law for a positive-Lebesgue-measure set of interior times. Subtracting two potentially infinite entropies or appealing only to a single exceptional time is not sufficient.

# Complete Alternative: Endpoint-Support Route

A complete proof using the actual full-horizon assumptions receives full credit without reproducing the drift-and-projection route. For this alternative, use the following allocation instead of the preceding allocation:

- **4 points:** Shows that if the clean support contains two distinct sequences, some token block has at least two possible tokens. Strict positivity of every supported endpoint's Gaussian likelihood implies that its posterior mean is not one-hot at any finite noisy state. Since the final mean bridge is pinned to that mean, its terminal law assigns zero probability to valid one-hot sequences, whereas the true terminal law assigns probability one. This contradicts the assumed full-path absolute continuity.
- **4 points:** Concludes that the clean law is a point mass; identifies the identical bridge dynamics of the two samplers; and proves the required weak inequality. For example, disintegration by the initial state shows both path entropies equal \(\mathrm{KL}(\lambda_T\|\pi_T)\). Equality of the two sampler path laws alone also suffices for the weak comparison.
- **2 points:** Observes that every conditional endpoint mean is then the same fixed block, so the strictness antecedent is impossible and its stated implication holds vacuously.

# Evaluator Notes

Accept any complete valid alternative proof; do not require the reference proof's incidental presentation choices. In particular, the endpoint-support proof is a valid resolution, not an objection to the theorem.

Do not accept a nonconstant one-hot example as a counterexample unless it satisfies the complete full-path absolute-continuity assumptions. In this setting it cannot. Conversely, do not claim that the strictness condition is realized by a nonconstant clean law while also claiming those full-horizon assumptions hold.

Do not replace the closed horizon by an early-stopped interval, smooth the terminal data, alter the final bridge endpoint, or compare only terminal or grid-point laws. Those modifications change the stated problem. The possible scientific vacuity of the strictness condition is not a solver error and must not be concealed by the evaluator.
