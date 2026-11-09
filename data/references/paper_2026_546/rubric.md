# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly handles the fixed centered feature map, finite-moment covariance definitions, and the intermediate empirical covariance of the latent embeddings; derives the triangle decomposition without treating latent measures as observed data.
- **3 points:** Proves the R^{1/2}n^{-1/2} inter-measure bound by independence and Hilbert-Schmidt second-moment calculations, and proves the 2R^{1/4}r_m(Phi) replacement bound by a valid rank-one identity and moment inequalities.
- **3 points:** Constructs admissible alternatives in the actual data experiment; verifies their population fourth moments for all three embeddings at the stated R thresholds; derives the full marginal observation laws and a KL bound uniform in m. For the reference construction the A/B moments are tau_k^2 d(d+2), the C moment is (1+2/d)tau_k^2+2tau_k+1, and KL(Q_1||Q_0)<=d/4.
- **2 points:** Computes covariance separation in the specified Hilbert spaces and completes a measurable two-point testing reduction, producing an explicit positive constant independent of n and m. The reference separations are sqrt(d)n^{-1/2} for A/B and n^{-1/2}/sqrt(d) for C; the displayed reference constants or any justified smaller positive constants are acceptable.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, KL orientation, or optimal constants. Standard Gaussian, operator, and testing results may be used when their relevant statements and hypotheses are clear; naming an internal proposition or claiming that calculations were previously audited does not supply the missing calculation.

The upper bound uses the given fixed centered map, not an estimator that secretly receives an unknown population mean. The minimax class bounds the population fourth moment of the specified uncentered map, while its target is the centered covariance. In particular, the deterministic standard-normal quantile component contributes to the C class-membership calculation but not to covariance separation in the reference subfamily.

Do not require the lower-bound alternatives to satisfy the upper theorem's empirical fourth-moment assumption at the same R. Do not add a dense-regime restriction on m: the lower bound is for every positive integer m. Verify boundary cases through the estimates rather than excluding n=1, m=1, d=1, or equality at the R thresholds.

Treat omission of either the upper bound or the minimax converse as a major gap. Unjustified class membership, covariance separation, or observed-data KL is likewise a substantive proof omission. A nearest-parameter test must be justified by error under the true hypothesis; an estimator need not, and generally cannot, lie within half the separation of both parameters.
