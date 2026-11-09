# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly applies or proves the empirical energy representation of CRPS to each leave-one-out empirical CDF, with the correct denominators. For an empirical CDF on indexed real values \(z_1,\dots,z_r\), the relevant identity is \(\operatorname{CRPS}(G,y)=r^{-1}\sum_i|z_i-y|-(2r^2)^{-1}\sum_{i,j}|z_i-z_j|\), valid for every integer \(r\ge1\). Its application here uses \(r=m-1\).
- **2 points:** Derives the held-out score formula using \(d_k\) and the deletion identity that the retained ordered pairwise sum is \(D-2d_k\).
- **3 points:** Sums over all observations and correctly establishes \(\sum_k d_k=D\) and the resulting algebraic simplification to \(mD/[2(m-1)^2]\).
- **2 points:** Converts the ordered sum to the unordered sum \(D=2W\) and states the exact target \(\operatorname{Cost}(B)=mW/(m-1)^2\) for every \(m\ge2\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The reference proof closes the empirical energy identity directly: expand the squared differences between empirical indicator functions and integrate, using that the integral of a squared difference of two threshold indicators is the absolute distance between their thresholds. A solver may instead correctly invoke the standard empirical energy identity in its precise applicable form; reproducing the reference derivation is not mandatory. If the general expectation form is used, its two draws must be independent draws from the predictive distribution, whose finite first absolute moment is automatic for the empirical CDFs here. This does not impose independence or any sampling-law assumption on the observed responses.

Observations are indexed and may have repeated values. Leaving out an observation removes one index, not every occurrence of its response value. The proof must cover \(m=2\), where the retained off-diagonal sum is empty, and zero dispersion. Separate case discussions are unnecessary when the argument already covers these cases. Do not require distinct responses, positive dispersion, sorted responses, or probabilistic assumptions beyond the stated definitions.
