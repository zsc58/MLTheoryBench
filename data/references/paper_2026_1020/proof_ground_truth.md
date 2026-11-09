# Reference Proof

## Proof Structure

1. Once the training split is fixed, the encoder, prototypes, and score function are fixed; set membership is exactly a comparison between the test score at its true label and the calibration quantile.
2. Exchangeability of the observations implies exchangeability of the resulting calibration scores and the test score, conditional on the fitted objects.
3. Apply the finite-sample order-statistic rank lemma to obtain the lower coverage bound and, when scores are almost surely distinct, the exact rank probability and the stated upper correction.

## Complete Proof

Let m = |D_cal| and let k = ceil((1-alpha)(m+1)). Condition on the training data and on the realized split. The fitted encoder and prototypes are then fixed, so s(x,y) is a fixed measurable function of (x,y). Write S_i = s(X_i,Y_i) for calibration observations and S_{m+1} = s(X_{m+1},Y_{m+1}) for the test observation (after relabeling the calibration points).

By construction, the prediction set contains the true test label exactly when S_{m+1} <= Q, where Q is the kth smallest calibration score if k <= m and Q = +infinity otherwise.

The calibration observations and the test observation are exchangeable after conditioning on the training fold: every permutation of these m+1 observations has the same conditional law, and applying the fixed score function preserves exchangeability. Therefore (S_1,...,S_m,S_{m+1}) is exchangeable.

If k > m, then Q = +infinity and the coverage event holds surely. This proves the lower bound, and the upper bound also holds because k > m implies (1-alpha)(m+1) > m, hence 1-alpha+1/(m+1) > 1.

Suppose now that k <= m. The standard finite-sample rank lemma for an exchangeable vector states that the probability that the last score is no larger than the kth order statistic of the first m scores is at least k/(m+1). (With ties, random tie-breaking or the corresponding weak-rank argument can only increase this event.) Since k = ceil((1-alpha)(m+1)), k/(m+1) >= 1-alpha. Thus P{Y_{m+1} in C_alpha(X_{m+1}) | training, split} >= 1-alpha. Averaging over the training data and split gives the asserted marginal lower bound.

If the m+1 scores are almost surely pairwise distinct, the rank of S_{m+1} among them is uniform on {1,...,m+1}. In that case the coverage event is exactly {rank(S_{m+1}) <= k}, so its conditional probability is k/(m+1). Since ceil(t) <= t+1,

k/(m+1) <= 1-alpha + 1/(m+1).

Averaging again yields the stated upper bound. The argument applies for every alpha in (0,1).
