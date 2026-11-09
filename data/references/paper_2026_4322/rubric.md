# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly handles the importance weight and proves that the summand mean is independent of k by cancellation of the sampling density. Establishes or appropriately justifies the moments used. Identification of the mean through the one-dimensional CDF formula for squared Wasserstein distance is valid but is not necessary for full credit on the stated variance target.
2. **2 points:** Derives localization from the coupling definition or an adequately justified CDF characterization of W_infinity, together with projection contraction. Shows that the integrand vanishes beyond the normalized gap W_infinity(mu,nu)/(2R). Proving vanishing only for strictly larger gaps suffices if endpoint issues in the subsequent integral argument are handled correctly.
3. **4 points:** Derives the squared-integrand gap representation of the second moment with correct normalization; explicitly defines and proves monotonicity and boundedness of the localized profile H; justifies differentiation near gap zero; and establishes the integral sign for k sufficiently near 1 by integration by parts or another complete valid argument. The threshold must lie in (0,1), depend only on the normalized transport distance, and yield monotonicity on the closed interval ending at 1. The gap-density calculation is acceptable, but naming or separately proving a Beta distribution identity is not required.
4. **1 point:** Correctly transfers second-moment monotonicity to variance using the k-independent mean and independence of the L summands, including the factor 1/L and the same threshold for every positive integer L.
5. **1 point:** Handles W_infinity(mu,nu)=0, for example by showing that the discrepancy and estimator vanish, without adding a positive-distance assumption.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, the identification of the mean as a named distance, or use of Stieltjes notation if an equivalent rigorous integral argument is supplied. A response that merely names importance sampling, localization, or monotonicity without deriving the corresponding inequalities and integral sign argument should not receive credit for those steps.

For a gap-profile proof, the profile must involve the square of the CDF discrepancy and its shrinking integration domain must be accounted for. Compact support alone does not justify differentiating through the logarithmic singularity at zero; boundedness of H and an integrable bound such as a constant times 1+|log s| do. Ordinary almost-everywhere conventions for the sampling density on the diagonal are sufficient. Consistent positive rescalings of the second-moment functional or antiderivative are immaterial, but displayed identities must respect the chosen normalization.

The source's local antiderivative-description error and its omitted zero-distance case have been repaired in the reference proof. They are not additional assumptions or unresolved proof obligations.
