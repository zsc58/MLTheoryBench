# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly derive the Gaussian positivity probability and the Bernoulli law and moments for the standard hard score. Use independence of the batch indicators to obtain the normalized-binomial law, mean, and variance for Multi-TCAV.
2. **3 points:** Correctly identify the smooth score as logit-normal and apply the adopted moment prescriptions with Gaussian mean mu and variance sigma^2/N, using tau_1 and tau_2 as specified. Distinguish the approximate mean m_alpha from the exact expectation. The sigmoid–probit relation and the moment formulas are approximation prescriptions provided by the task, not accuracy theorems to be proved.
3. **3 points:** Verify that alpha-star=sigma^{-1}sqrt(n/[tau_1(1-1/s)]) gives the stated approximate mean matching for s>1. A derivation by argument matching is valid for mu != 0. Handle mu=0 by direct substitution or symmetry; the displayed value remains a valid choice, but mean matching does not uniquely determine alpha in this case. Direct verification of the displayed parameter for all mu is equally acceptable.
4. **2 points:** Use the adopted mean-matching replacement in the variance prefactor, substitute alpha-star, obtain r(s)=s[1-(1+(tau_2/tau_1)/(s-1))^{-1/2}], and prove that this expression tends to tau_2/(2tau_1), approximately 0.4558. Correctly interpret this as about 45.6% variance retained, or about 54.4% reduction, within the approximation.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its private upstream-support discussion, or a particular limit method; Taylor expansion with a controlled remainder and rationalization are both valid.

The exact distributional statements hold under the Gaussian model. The smooth-moment formulas and the finite-s ratio comparison are approximation calculations. Do not demand a proof of a uniform approximation bound, a derivation of the fitted constant tau_2, or convergence of the exact variance ratio. Conversely, unsupported claims that the approximations are exact or that their errors vanish as s grows are not valid conclusions.

The large-s limit concerns the number of batches; for example, n can be fixed while N=sn grows. It is not a limit with infinitely many positive-size batches at a fixed finite N. All variance denominators are positive for the stated finite real mu and sigma>0.

Do not require uniqueness of alpha-star when mu=0. An argument that divides by mu without addressing zero has an omitted case, normally a readily repairable error if the remaining proof is correct.

A missing limiting interpolation statement should not reduce credit if the distributions, matching parameter, and variance-ratio calculation requested in the public task are fully established. No additional branch concerning random-input scores, Bayesian calibration, practical sigma estimation, or ridge regression is required.
