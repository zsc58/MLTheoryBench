# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formulates the scalar influence-function score statistic and identifies null centering, the finite positive population second moment, and the fixed-predictor/fixed-direction sampling contract. Recognizes the denominator as a second moment, not necessarily a variance under alternatives.
- **3 points:** Under the null, derives the asymptotic normal law for the normalized estimated score by comparing it with the iid population contributions using the assumed asymptotic linearity. Establishes empirical second-moment consistency using the k=2 assumption and the law of large numbers; finite second moments suffice and no fourth moment is required.
- **3 points:** Combines the null limits by Slutsky and continuous mapping to obtain the chi-square_1 limit. Handles the public zero-denominator completion, either through an explicit probability bound or by a measurable completed ratio continuous at every limiting point with positive denominator.
- **2 points:** Under a fixed alternative, identifies the mean as the nonzero inner product, establishes numerator and denominator convergence, proves T_n/n converges in probability to a fixed positive constant or an equivalent divergence result, and concludes rejection probability tends to one for every fixed finite real critical value.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental notation, organization, or its auxiliary function Q.

The alternative hypothesis is H_1:f_* != f_0. The hypothesized predictor f_* is fixed, not a data-generating function, a validation-adaptively selected function, or a sequence of local alternatives. The direction is likewise fixed and nonzero.

Estimated influence-function evaluations can share sample-dependent nuisance estimates. Do not require them to be iid, and do not accept an unqualified CLT applied directly to them without using the stated comparison with the true contributions. Numerator-denominator independence is not needed for Slutsky's theorem.

The statistic is already defined at zero empirical denominator. Do not require a new assumption that the empirical denominator is almost surely positive for every n. It is enough to justify continuity at the positive limiting denominator; separately displaying Pr(D_n=0) -> 0 is optional if the completed-ratio argument is valid.

Under alternatives, the denominator limit is E[varphi_0(h,f_*)^2], not Var(varphi_0(h,f_*)). Positive centered variance under the alternative is not required. A proof using an unjustified replacement of the denominator by the centered variance has not established the stated statistic's limit.

The scalar CLT, integrable law of large numbers, Slutsky's theorem, continuous mapping, Cauchy-Schwarz, and the characterization of chi-square_1 as the square of a standard normal may be cited without proof, provided their applicable hypotheses are checked. The Riesz identity is supplied as a public assumption. No derivation of application-specific influence functions, nuisance-estimation rates, multidirectional extensions, or sequential inference guarantees is required.
