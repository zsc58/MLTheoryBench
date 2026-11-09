# Reference Proof

## Proof Structure

1. Verify that the fixed scoring definitions produce exchangeable calibration/test score vectors conditional on the reference sample.
2. Establish the finite-sample split-conformal rank bound, including ties and the rank-n+1 convention.
3. Use nesting of the neighbor-label sets to identify the rank-score event with membership in the thresholded k-NN set, including an infinite threshold.
4. Apply the same score bound to the contrastive set.
5. Bound failure of the intersection by the union bound and substitute the prescribed error allocation.

## Complete Proof

### Well-definedness and score exchangeability

The reference sample has N indexed observations, and both neighbor counts lie between 1 and N. Sorting by kernel similarity and breaking ties by reference index gives a measurable ordering and retains distinct observations even if their embeddings coincide. The symmetric positive-semidefinite matrix M and positive parameters L and xi make K_M a continuous, finite function with values in (0,1]. This remains true when M is singular or zero. Consequently d_M lies in [0,2], and the denominator in each contrastive loss is a finite, nonempty sum of strictly positive terms. Every neighbor loss is therefore finite. The two scores are measurable extended-real functions; a missing label has score infinity.

Condition on the reference sample. All parameters and the encoder are fixed independently of the calibration and test observations, and the same score function is applied separately to each observation. Conditional exchangeability of the observations therefore implies conditional exchangeability of the n+1 scores for each component. The two component score vectors need not be independent.

### The rank bound

We prove the precise standard split-conformal fact needed here. Let S_1,...,S_{n+1} be an exchangeable vector of extended-real scores. For a fixed a in [0,1), put r=ceil((1-a)(n+1)), and let q be the r-th order statistic of S_1,...,S_n,infinity. Then

\[
\Pr\{S_{n+1}\le q\}\ge \frac{r}{n+1}\ge 1-a.
\]

If r=n+1, q=infinity and the event holds surely, including when the test score is infinity.

Suppose r<=n. For each i, let T_i be the r-th order statistic of the other n scores. In any realization, arrange the n+1 scores in nondecreasing order, breaking ties arbitrarily for this counting argument. Each of the first r scores is at most its leave-one-out threshold T_i: deleting such a score cannot make the r-th remaining score smaller than it. Thus

\[
\sum_{i=1}^{n+1}\mathbf 1\{S_i\le T_i\}\ge r.
\]

Exchangeability makes the expectations of these n+1 indicators equal. Since T_{n+1} is the r-th calibration score and appending infinity does not change that order statistic for r<=n, taking expectations gives the asserted lower bound. If the scores are pairwise distinct, precisely the first r scores satisfy the inequality: every later score has at least r strictly smaller scores among the other observations. Hence, in that case,

\[
\Pr\{S_{n+1}\le q\}=\frac{r}{n+1}
\le 1-a+\frac1{n+1}.
\]

This proof also applies conditionally on the reference sample. Integrating the conditional probabilities gives the marginal assertions. It does not condition on an observed quantile or on a calibration-dependent selection event.

### k-NN coverage

Apply the rank bound with S_i=S_knn(Z_i,y_i) and a=alpha_knn. It gives

\[
\Pr\{S_{\rm knn}(Z_{n+1},y_{n+1})\le q_{\rm knn}\}\ge 1-\alpha_{\rm knn}.
\]

For every input, the neighbor sets are prefixes of one ordering, so their label sets satisfy

\[
L_1(Z)\subseteq\cdots\subseteq L_{m_{\rm knn}}(Z)\subseteq L_\infty(Z).
\]

For a finite integer q in {1,...,m_knn}, if y belongs to L_q(Z), its first occurrence has rank at most q. Conversely, if its first occurrence is at most q, nesting places y in L_q(Z). Thus

\[
S_{\rm knn}(Z,y)\le q\quad\Longleftrightarrow\quad y\in L_q(Z).
\]

At q=infinity the same equivalence holds because every extended-real rank score is at most infinity and L_infinity(Z)=Y. Every possible q_knn is either an integer in {1,...,m_knn} or infinity. Therefore the equivalence applies to the random threshold pointwise and yields

\[
\Pr\{y_{n+1}\in C_{\rm knn}(Z_{n+1})\}\ge 1-\alpha_{\rm knn}.
\]

For the optional upper bound, assume the n+1 rank scores are pairwise distinct almost surely and q_knn<=m_knn almost surely. Finiteness of the threshold excludes r_knn=n+1. The exact-rank calculation consequently gives

\[
\Pr\{y_{n+1}\in C_{\rm knn}(Z_{n+1})\}
=\frac{r_{\rm knn}}{n+1}
\le 1-\alpha_{\rm knn}+\frac1{n+1}.
\]

These are assumptions on the experiment, not instructions to condition on whichever calibration samples happen to have finite thresholds.

### Contrastive coverage

Apply the same rank bound to S_i=S_clr(Z_i,y_i) with a=alpha_clr. Conditional score exchangeability was verified above, and the extended threshold is defined for every allocation, so

\[
\Pr\{S_{\rm clr}(Z_{n+1},y_{n+1})\le q_{\rm clr}\}\ge 1-\alpha_{\rm clr}.
\]

By the definition of C_clr this is exactly

\[
\Pr\{y_{n+1}\in C_{\rm clr}(Z_{n+1})\}\ge 1-\alpha_{\rm clr}.
\]

No tie-free assumption is needed here. In particular, when r_clr=n+1, q_clr=infinity and the extended-real comparison includes every label, including those with score infinity.

### Intersection coverage

Since C_mix(Z)=C_knn(Z) intersect C_clr(Z),

\[
\{y_{n+1}\notin C_{\rm mix}(Z_{n+1})\}
=\{y_{n+1}\notin C_{\rm knn}(Z_{n+1})\}
\cup\{y_{n+1}\notin C_{\rm clr}(Z_{n+1})\}.
\]

Boole's inequality and the two lower coverage bounds give

\[
\Pr\{y_{n+1}\notin C_{\rm mix}(Z_{n+1})\}
\le\alpha_{\rm knn}+\alpha_{\rm clr}.
\]

Thus

\[
\Pr\{y_{n+1}\in C_{\rm mix}(Z_{n+1})\}
\ge 1-\alpha_{\rm knn}-\alpha_{\rm clr}
=1-\alpha,
\]

where the last equality uses alpha_knn=(1-lambda)alpha and alpha_clr=lambda alpha. Both endpoints lambda=0 and lambda=1 are covered by the threshold convention. The optional upper-bound assumptions are not needed for this conclusion.

## Obligation Closure

All theorem-critical obligations are derived above. The exchangeable-score lemma and Boole's inequality are standard-independent background, and the former is proved explicitly. No specialized external result, training guarantee, or unresolved private proof dependency is used.
