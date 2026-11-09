# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Prediction-versus-ideal decomposition (2 points).** Derives the learned-versus-ideal fixed-schedule log-ratio identity and averages it to identify the public epsilon_pred term. Prediction error must be evaluated on data-law contexts, not generated contexts. A proof using the public revealed-batch definition need not discuss the source's alternative normalization. If it uses that normalization, it must justify equality by conditional uniform-subset averaging, not by time sampling alone.
2. **Recursive ideal-sampler identity (2 points).** Defines expected fixed-schedule ideal KL, conditions on the first random batch, applies the KL chain rule, and identifies its contribution as conditional total correlation. The residual context is averaged under the true conditional first-batch law, not the ideal product-marginal sampling law.
3. **TC telescoping induction (4 points).** Uses induction with the prescribed w_tc/Psi_tc recurrence, explicit entropy expansion, and uniform-subset double counting to cancel intermediate subset entropies and prove the exact coefficient f_tc(K,L')TC. It must account for the lower endpoint, the vanishing upper endpoint f_tc(K-1,K-1)=0, and both surviving entropy coefficients. The unnormalized double-counting sum uses H(X_T) for its newly introduced subset T; an equivalent averaged-subset-entropy calculation is fully acceptable. It must also justify that the recursive coefficients give nonnegative finite weights and a positive normalizer. Merely naming telescoping or a schedule receives little credit.
4. **Coefficient bound and final averaging (2 points).** Proves the harmonic bound on f_tc through an explicit valid calculation, including K=2 and L'=K, then combines it with the prediction decomposition and convexity/Jensen to obtain both KL inequalities and the stated constant for all 2<=K<=L.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or notation. A minor indexing or boundary-case omission may reduce the relevant step, but an unsupported telescoping argument or missing harmonic bound is theorem-critical. The coefficient denominator is positive even at K=L=2; no endpoint convention is necessary. True conditional kernels may be chosen arbitrarily on zero-data-probability contexts, and their choices do not affect the data-law KL calculations. Learned kernels need not be strictly positive: a correct proof must accommodate infinite prediction error and learned KL, or explicitly explain why that case is immediate before treating finite error. Do not require a solver to impose stronger support assumptions. Zero TC and diagonal schedules are included in the claim.
