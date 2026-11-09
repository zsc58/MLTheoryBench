# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Coupling and first-disagreement control (3 points).** Constructs a coupling with the correct marginal policy experiments and common latent function and contexts. Uses maximal coupling while histories agree, defines the first disagreement time tau, and proves P(tau<=t)<=sum_{s<=t}epsilon_s. Shared reward observations are permitted for equal actions; distinct-arm reward observations must not acquire an unjustified shared-noise dependence.
2. **Posterior conditioning and regret decomposition (2 points).** Justifies applying the assumed posterior expectation of absolute pairwise reward differences after disagreement. For the reference coupling, this requires recognizing the combined transcript as a finite arm-specific observation collection, counting shared observations once, and explaining why adaptive action randomization adds no latent-dependent likelihood factor. The disagreement event must be included in the conditioning argument. Uses cancellation of the common oracle term and equality before disagreement to obtain an expected penalty of at most 2B_R P(tau<=t), then sums to obtain the horizon weights. A bound merely on differences of posterior means is not a substitute for the stated assumption.
3. **Reduction of action TV to vector-law TV (2 points).** Uses the common measurable argmax rule, TV contraction under that rule, and the triangle inequality to separate the exact-posterior Gaussian approximation error rho_t from the discrepancy between the two product Gaussian laws. Keeps all laws at the same context and histories.
4. **Explicit Gaussian discrepancy bound (3 points).** Computes KL(G_t^{approx}||G_t^Pi) with the correct direction, common scale s_a, variance ratios, and scaled squared mean errors. Applies Pinsker with the correct factor to obtain one-half the square root of the indicated sum, and takes the required supremum. Does not infer uniform finiteness from pointwise positive variances; an infinite supremum makes this bound vacuous but valid.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its explicit finite-state construction of maximal coupling. A concise, correct explanation of posterior validity under the coupled experiment suffices; repeating the reward-range assumption without addressing the conditioning is not by itself a complete justification. Routine integrability and boundary cases may be handled briefly. No predictive CLT, variance-estimator consistency proof, information-ratio bound, or quantitative rate for rho_t is required.
