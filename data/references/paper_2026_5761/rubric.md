# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Covariance correction and subspace recovery (3 points).** Establish unbiasedness and a valid second-moment/variance bound for the corrected covariance. Apply matrix concentration to all offered samples, with the correct completed-round indexing and a simultaneous failure allocation. Convert covariance error into projector control and sufficiently sharp aligned-basis control, including the early/trivial regime, and verify the burn-in guarantee. An alternative valid variance argument is acceptable; the reference proof's exact second-moment identity is not mandatory.
2. **Uniform imputation under masking (2 points).** Establish simultaneous conditioning of the true observed subspace from incoherence and independent masks. Transfer it to the estimated subspace, justify basis alignment and rotation invariance, and derive uniform imputation error. Explain why the singular-matrix completion is irrelevant on the success event.
3. **Frozen surrogate confidence (2 points).** Derive the fixed-coordinate surrogate approximation, control aggregate misspecification without an unnecessary dimension loss, and combine regularization with a valid self-normalized noise argument to recover the algorithm's specified inflated radius. Verify both feature predictability and noise adaptedness for the same filtration. One valid route is to multiply the noise by the pre-reward indicator that the true observed Gram of the selected arm is invertible, prove post-reward measurability by reconstruction with fixed U, verify the conditional moment bound, and show equality with the original noise on the existing conditioning event. Construct the resulting noise events under the original law and intersect them with representation events; do not assume that conditioning on a global future-dependent representation event preserves the noise bound.
4. **Optimism, potential, and global regret (3 points).** Derive the leverage/potential inequalities, convert surrogate optimism into true regret, bound each epoch including both misspecification contributions, and sum the doubling epochs. Account for the actual burn-in rounds and the ceiling in t_b. Absorb the ceiling's additive SB_X contribution into an existing target term rather than incorrectly assigning it to the first term alone. Derive all three terms with the stated logarithmic dependence and probability, including the case of no post-burn-in epochs.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require incidental reference-proof constants, notation, or presentation choices. The explicit public confidence radius is an algorithm definition, not an assumed confidence guarantee; its validity must be proved. The covariance samples are all offered arms, not only selected arms, and regression uses only observations from the current epoch.

Merely naming matrix concentration, perturbation, imputation, or optimistic linear-bandit arguments without checking hypotheses and obtaining the required bounds does not earn the corresponding step. A stated standard independent theorem may be used when its applicable hypotheses are verified. The recovery-to-imputation-to-frozen-surrogate-to-regret chain must be materially established; theorem-critical gaps are major.

Do not require the source's unsupported conditional-probability assertion given the global representation event. Separate noise events, constructed with verified adaptedness, and a union bound suffice. Do not penalize a solver for noting or correcting the filtration issue. In particular, a reward minus an unobserved ideal mean need not be measurable from the learner's observed post-reward history. Feature predictability alone is not a complete verification, and adjoining hidden past actions or noises does not automatically preserve the public conditional moment bound. The task does not assume independence of reward noise from the entire sequence of future contexts and masks.

The localized-noise construction is proof-only: using fixed unknown U and theta* to exhibit measurability does not reveal them to the algorithm. On the already established true-mask conditioning event the localized and original noises agree, so the original design, confidence radius, and algorithm remain unchanged. Any alternative argument that rigorously closes the same filtration obligation is acceptable.

The assumptions allow S=0 or R=0, and the dimensions and horizon are positive integers. Empty epochs, m=d, and the burn-in ceiling should be handled without introducing undefined quantities. Brief direct treatment of trivial cases suffices. No separate analysis of rank adaptivity, lower bounds, or full-history replay is required.
