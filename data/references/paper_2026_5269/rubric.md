# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Setup, policy, and concentration decomposition (2 points).** Correctly handles the bounded offline/online model, empirical means, fresh independent Gaussian draws, zero-sample conventions, and median index. Establishes an O(Delta_i^-2) contribution from concentration failures. Concentration at adaptive counts must be justified, for example by fixed-prefix counting; conditioning on the event that an adaptive count equals s does not by itself preserve an i.i.d. sample law. The good event for arm i must not inadvertently include the optimal arm's accurate-anchor event.

2. **Suboptimal-arm median intersection (3 points).** Shows that an index above y_i, with the suboptimal online anchor below x_i<y_i, requires both posterior samples to exceed y_i. Gives a valid online tail residual and hybrid concentration/bias threshold, counts selected prefixes, and derives the reduction N_i(1-3omega_i/Delta_i)_+ inside the required positive part. Handles the boundary 3omega_i=Delta_i and the vanishing-discount case. A Gaussian threshold makes exceedances rare, not impossible.

3. **Optimal-arm transfer and accurate-anchor branch (3 points).** Proves a valid conditional comparison with the factor (1-p)/p and an optimal-arm selection probability, or an equivalent rigorous waiting-time argument. Justifies summation by optimal-arm prefixes without assuming unobserved stopping times are defined. On an accurate optimal online anchor, uses the union of posterior successes and explicitly establishes the necessary inverse-tail estimates, including the hybrid N_1 benefit. Derives the N_1 subtraction with logarithmic constants placed correctly inside the positive part. A direct inverse-tail moment and concentration proof is acceptable in place of a geometric hitting-time construction.

4. **Poor-anchor branch and regret summation (2 points).** On the complementary optimal-anchor event, uses the simultaneous-success probability and supplies a valid uniform inverse-tail moment of order strictly greater than one, or another complete bound yielding O(Delta_i^-2). Correctly handles the dependence between the online and hybrid empirical means. Applies bounded-reward concentration and Holder, or a valid alternative, includes the initial prefix, and combines per-arm pull bounds into the stated regret guarantee with universal constants.

# Evaluator Notes

Accept any complete valid alternative proof under the public assumptions. Do not require the reference proof's notation, particular thresholds, exponent 5/4, numerical coefficient 72, or geometric construction. The universal constants may change, but the dependence on Delta_i, N_i, N_1, and omega_i and the stated positive-part structure must be established. A rigorously proved stronger bound also receives full credit if it implies the requested bound.

A named concentration or Thompson-sampling method does not close a specialized inverse-tail obligation without its relevant statement and verified hypotheses or an explicit derivation. The supplied reference proof derives all required specialized controls; no unresolved private lemma is being treated as a completed scoring step.

Do not accept the assertion that failure to obtain a simultaneous online/hybrid success implies failure of at least one component to succeed anywhere in the trial sequence. Component successes can occur in different trials. Also do not accept independence of the online and hybrid empirical means, or a universal pointwise ordering of their posterior success probabilities. Conditional independence of fresh posterior draws is different from independence of the empirical means.

The refined logarithm must be justified uniformly in small gaps and short horizons. Replacing log T by log(T Delta_i^2+e^6), or bounding the source's time-dependent confidence radius by a constant multiple of that quantity, without a valid argument is insufficient. Minor integer endpoint allowances can be absorbed into O(Delta_i^-2).

The final online-only conclusion is a comparison of upper-bound orders, not a requirement to prove monotonicity of actual regret in the offline sample size or a particular leading-constant improvement.
