# Reference Proof

## Proof Structure

1. Show that the calibration and test score variables are exchangeable for every fixed agent parameter and every black-box output kernel.
2. Relate membership in the test prediction set to comparison of the test score with the calibrated order-statistic threshold.
3. Prove the exchangeable rank-counting bound, including ties and infinite scores, and obtain the no-tie equality and ceiling.
4. Since the argument is pointwise in the parameter and output law, conclude uniform bias immunity.

## Complete Proof

Fix an arbitrary parameter \(\theta\), an arbitrary conditional output kernel \(Q_\theta(\cdot\mid x)\), an exchangeable law for \((X_i,Y_i)_{i=1}^{n+1}\), and a fixed \(\alpha\in(0,1)\). Write \(N=n+1\).

### 1. Exchangeability of the scores

For each example index \(i\), let \(B_i\) comprise its batch of agent responses and its frequency-tie-breaking randomness. Conditional on the entire example vector, these auxiliary variables are independent, and the conditional law of \(B_i\) is the same prescribed law depending on \(X_i\) at every index: the responses have law \(Q_\theta(\cdot\mid X_i)^{\otimes m}\), followed by independent uniform frequency-tie breaking. Consequently, permuting the examples and their auxiliary variables together merely permutes the factors in this conditional product law. Since the example vector itself is exchangeable, the augmented vector \(((X_i,Y_i),B_i)_{i=1}^N\) is exchangeable.

Apply the same canonicalization, ranking, and score construction to every augmented example. Writing \(R_i\) for the ranked list obtained at occurrence \(i\), define
\[
T_i=s_{R_i}(X_i,Y_i),\qquad i=1,\ldots,N.
\]
The resulting scores are exchangeable and take values in \(\{1,\ldots,m\}\cup\{+\infty\}\). Repeated inputs still receive the independently generated batches prescribed by the setup.

### 2. Prediction-set membership

For a finite integer \(M\ge1\), a canonical true class belongs to the top-\(M\) set exactly when its position in the sampled list is at most \(M\). An absent class has score \(+\infty\) and belongs to no finite-threshold set. For \(M=+\infty\), the prediction set is the full canonical universe and every score is at most \(+\infty\), including an absent-answer score. Thus, for the random calibrated threshold as well,
\[
c_{X_N}(Y_N)\in S_{M^*}(X_N)
\quad\Longleftrightarrow\quad T_N\le M^*.
\]
This also covers a finite threshold exceeding the number of observed test classes: the prediction set then contains all observed classes, but no absent class.

### 3. Coverage with ties and infinite scores

Let \(k=\lceil N(1-\alpha)\rceil\), so \(1\le k\le N\). If \(k=N\), the prescribed threshold is \(+\infty\), and the membership event is certain. Hence coverage is one in this case.

Now suppose \(k\le n\), and let \(T_{(k)}\) denote the k-th order statistic of the calibration scores. For each \(i\in\{1,\ldots,N\}\), define
\[
L_i=1+\#\{j\in\{1,\ldots,N\}:T_j<T_i\}.
\]
These are lower ranks, so ties may give several indices the same lower rank. In particular, they are not asserted to be uniformly distributed.

The event \(T_N\le T_{(k)}\) occurs exactly when fewer than \(k\) calibration scores are strictly smaller than \(T_N\). Since the test score is not strictly smaller than itself, this gives
\[
\{T_N\le T_{(k)}\}=\{L_N\le k\}.
\]
The equivalence uses only the total ordering of the scores and remains valid when one or more scores equal \(+\infty\).

For every realized vector of \(N\) scores, choose any ordering of its indices that is nondecreasing in score. Each of the first \(k\) indices in this ordering has at most \(k-1\) strictly smaller scores. Therefore, deterministically,
\[
\sum_{i=1}^N\mathbf 1\{L_i\le k\}\ge k.
\]
The lower-rank construction is permutation-equivariant. Exchangeability therefore makes the probabilities \(\Pr(L_i\le k)\) equal for all indices, giving
\[
\Pr(T_N\le T_{(k)})
=\Pr(L_N\le k)
=\frac1N\mathbb E\!\left[\sum_{i=1}^N\mathbf 1\{L_i\le k\}\right]
\ge\frac{k}{N}\ge1-\alpha.
\]
This directly handles all tied-score cases, including the case in which every score is infinite. No comparison with an unspecified tie-free distribution is required.

### 4. No-tie equality and uniformity over agents

If the \(N\) scores are almost surely pairwise distinct, their lower ranks are exactly \(1,\ldots,N\), each occurring once. Hence the sum of indicators in the preceding display is exactly \(k\), and, for \(k\le n\),
\[
\Pr\{c_{X_N}(Y_N)\in S_{M^*}(X_N)\}
=\frac{k}{N}
=\frac{\lceil N(1-\alpha)\rceil}{N}
\le1-\alpha+\frac1N.
\]
The lower bound follows from the other ceiling inequality. Distinctness is the additional condition for this equality; uniform tie breaking of empirical frequencies does not itself imply distinct example-level scores.

Every probability above is marginal over the examples, agent samples, and frequency-tie-breaking randomness. No conditioning on a realized calibration set or on a particular test query is asserted. The argument holds for each fixed \(\theta\), each output kernel, and each exchangeable example law in the setup, with the same lower bound. Taking an infimum of these coverage probabilities therefore preserves the bound \(1-\alpha\). In particular, no restriction on systematic bias or on the probability that the agent generates the true class is needed.
