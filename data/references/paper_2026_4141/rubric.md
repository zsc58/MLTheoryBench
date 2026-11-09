# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Inverse-probability weighted consistency and rate (2 points).** Establish conditional unbiasedness and a valid Hilbert-space second-moment bound for both designs. Use the inverse-probability maximum and fourth moments to obtain the weighted LLN, and the O_P(s_n^{-1/2}) rate when s_n=O(n). Deduce consistency and the scaled estimator bound from convexity of the loss and positive ridge regularization. Recognize that the source assumptions ensure existence and uniqueness; an empty Poisson sample is not excluded.
2. **Multinomial conditional score CLT (3 points).** Represent the score noise by conditionally independent centered increments, or an equivalent valid array. Compute the covariance Q_n-(P_ng) tensor (P_ng) and show that it tends to Sigma_M^*(psi). Verify conditional Lindeberg, for example with the bound 8s_n^{-1}[a_n^3P_n||g||^4+||P_ng||^4], where a_n=max_i(n pi_{n,i})^{-1}. Justify conditional characteristic-function convergence and projection-tail control sufficient for an H-valued limit.
3. **Poisson conditional score CLT (3 points).** Use the independent centered Bernoulli increments with conditional means s_n pi_{n,i}. Derive covariance Q_n-(s_n/n)P_n(g tensor g), including the subtraction of cE[g tensor g]. Verify Lindeberg using both Bernoulli feasibility and the inverse-probability bound, and supply H-valued tightness or asymptotic finite-dimensionality. A shared projection-tail argument with Step 2 earns the relevant credit in both steps without needing repetition.
4. **Norm-valued linearization and covariance combination (2 points).** Justify differentiation of the population risk and control the integrated Hessian remainder in H norm. A valid route applies the weighted LLN to the rank-one Hessian integrand in Hilbert-Schmidt norm, handles the identity regularization term separately, and uses local Lipschitz continuity along the consistent estimator path. Combine the conditional score characteristic functions with the full-data Hilbert-space CLT at scale sqrt(s_n/n), and control sqrt(s_n)(lambda^*_{s_n}-lambda_0)h_0. Conclude both stated covariance sums.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or explicit martingale terminology when conditional independence is used correctly. Standard scalar LLNs, scalar CLTs, and a correctly stated Hilbert-space convergence criterion may be invoked with their hypotheses checked. Merely naming a specialized conditional CLT without checking its variance, Lindeberg, conditioning, and Hilbert-space tightness requirements does not close the main bottleneck.

Population strong convexity alone must not be substituted for convexity of each weighted sample objective. Positive regularization supplies sample strong convexity here because the loss is convex and the weights are nonnegative.

Entrywise covariance inequalities cannot be multiplied termwise by arbitrary signed inner products. Exact covariance calculations or positive-semidefinite quadratic-form bounds are acceptable. Convergence against each fixed test vector alone does not establish an H-norm Taylor remainder or H-valued weak convergence. Likewise, an O_P(1) operator error times an O_P(1) scaled estimator error is not necessarily negligible; the needed error must be o_P(1), or an equivalent valid argument must be supplied.

The scaled estimator error is required to be O_P(1), not o_P(1). When using an integrated Hessian, the first-order expansion is exact and has no additional unaccounted-for remainder. The full-data and sampling fluctuations need not be independent at finite n; the conditional characteristic-function argument justifies the covariance sum. Bounded convergence in probability of the characteristic-function errors suffices for their L1 convergence.

The proof must remain valid for c=0 and for zero or singular limiting covariance. Do not impose a positive-variance assumption absent from the task. A uniform argument that covers these cases is sufficient; a separate discussion is not mandatory. No proof of optimal importance sampling, pilot estimation, or plug-in extensions is requested.
