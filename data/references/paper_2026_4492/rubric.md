# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **3 points:** Correctly conditions on the input-independent matrix M, identifies the common Gaussian support and covariance, and derives the likelihood-ratio distribution with squared Mahalanobis parameter ||P_M(V-V')||_F^2/sigma_G^2. Specifies the ratio orientation and sampling law consistently and justifies the matching conditional event inequality using the Gaussian tail.
2. **3 points:** Establishes the random-subspace projection bound: rotational invariance, the Beta(r/2,(d-r)/2) marginal projection law, the SVD weighted-energy identity, and a union bound over at most s=min(d,n) directions. Does not assume independence between different singular-direction projection fractions. The reference proof derives the Beta law through a Gaussian squared-norm ratio.
3. **3 points:** Justifies the tail comparison on the good event, including monotonicity of T or an alternative valid comparison, and integrates conditional event inequalities over the common law of M. Adds the bad-event probability and handles the reversed neighboring direction. Keeps the additive privacy parameter pair-dependent unless a uniform bound over neighbors is established.
4. **1 point:** Uses all definitions and parameter restrictions consistently: integer dimensions, 1<=r<d, sigma_G>0, independent randomization, fixed input pair, 0<alpha<1, epsilon>0, and s=min(d,n). Handles a zero input difference or zero conditional projected difference without division by zero. Bounds exceeding 1 may be capped at 1 or handled by the trivial event inequality.

# Evaluator Notes

Accept a complete valid alternative proof; do not require incidental presentation choices. Either likelihood-ratio sign convention is valid when the ratio orientation, sampling law, mean, and event bound agree. T is a sufficient two-sided privacy-loss bound, not a claim about the exact optimal DP profile.

The conditional Gaussian calculation, projection-energy bound, and removal of conditioning are theorem-critical. Merely naming a paper-specific lemma or specialized method does not establish them. A precisely stated standard probability fact may be used with its hypotheses verified; an unexplained reference to Haar/Beta concentration without identifying its relevant distributional consequence and application is insufficient. An elementary derivation of the Beta law, as in the reference proof, fully closes that step.

A claim of global DP on an unrestricted domain with a parameter calibrated only to one pair is not a correct conclusion. No unit-column assumption, alignment restriction, bounded sensitivity assumption, large-r result, or asymptotic comparison is required. Minor omissions of a readily repairable zero case or an elementary monotonicity verification can merit 8-9 when the remainder is complete, but must not be counted as fully justified steps for a score of 10.
