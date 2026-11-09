# Reference Proof

## Proof Structure

Construct a symmetric full-conformal version of the score on every augmented sample. Prove its coverage by an exchangeable-rank counting argument, including ties and the infinite-threshold case. Adding reference occurrences cannot increase the sum of the k smallest scores. This gives equality of the full and practical test scores and domination of the full calibration scores by the practical calibration scores. Quantile monotonicity then gives set inclusion and transfers coverage.

## Complete Proof

Write $Z_i=(X_i,Y_i)$ and $N=n+1$. All datasets below retain their indexed occurrences. For a candidate label $y$, put $Z_i^y=Z_i$ for $i\le n$ and $Z_N^y=(X_N,y)$. Define
\[
T_j^y=\Sigma_k\bigl(\{s_{Z_\ell^y}(Z_j^y):1\le\ell\le N,\ \ell\ne j\}\bigr),\qquad 1\le j\le N.
\]
The braces denote a multiset with one entry per indicated index. Thus this construction removes precisely the target occurrence's self-score. Every such multiset has $n\ge k$ finite entries. Let
\[
q_{\rm full}^y=\operatorname{Quantile}_\beta(T_1^y,\ldots,T_n^y),\qquad
C_{\rm full}(X_N)=\{y\in\mathcal Y:T_N^y\le q_{\rm full}^y\}.
\]
The quantile convention is exactly the convention in the public task, including $+\infty$ when $\beta>1$.

### 1. Symmetry and full-set coverage

Permuting the augmented observations permutes the target indices and, for each target, permutes the multiset of reference scores with its own index excluded. Since the score rule is fixed and $\Sigma_k$ depends only on the multiset, the full-score vector is permutation equivariant. At the true candidate $y=Y_N$, the augmented sample is the exchangeable vector $(Z_1,\ldots,Z_N)$. Therefore
\[
(U_1,\ldots,U_N):=(T_1^{Y_N},\ldots,T_N^{Y_N})
\]
is exchangeable. Joint measurability of the score rule and measurability of finite order statistics ensure these are real random variables.

Put
\[
r=\lceil N(1-\alpha)\rceil=\lceil n\beta\rceil.
\]
Since $0<\alpha<1$, we have $1\le r\le N$. If $r=N$, then $\beta>1$ and the full threshold is $+\infty$, so the true label belongs to the full set surely.

Suppose $r\le n$. For each $j$, let $Q_{-j}$ be the $r$-th smallest of the $N-1$ scores other than $U_j$. For every deterministic vector of $N$ real numbers,
\[
\#\{j:U_j>Q_{-j}\}\le N-r.
\]
Indeed, $U_j>Q_{-j}$ requires at least $r$ other entries strictly smaller than $U_j$. Any $r$ indices occupying the first $r$ positions in a nondecreasing ordering fail that requirement. This argument allows ties.

Exchangeability makes the probabilities of the events $\{U_j>Q_{-j}\}$ equal. Consequently,
\[
\Pr\{U_N>Q_{-N}\}
=\frac1N\mathbb E\sum_{j=1}^N\mathbf 1\{U_j>Q_{-j}\}
\le\frac{N-r}{N}\le\alpha.
\]
Here $Q_{-N}=q_{\rm full}^{Y_N}$ by the definition of the empirical quantile. Combining both cases gives
\[
\Pr\{Y_N\in C_{\rm full}(X_N)\}\ge1-\alpha.
\]

### 2. Monotonicity and score comparison

If a reference collection $D'$ contains every occurrence of $D$ and $|D|\ge k$, then $A_{D'}(z)$ contains every occurrence of $A_D(z)$. For each $1\le j\le k$, its $j$-th order statistic is no larger: the $j$ entries witnessing the $j$-th order statistic in the smaller collection are still present in the larger collection. Summing gives
\[
S_{D'}(z)\le S_D(z).
\]
No sign restriction on the scores is used.

Fix $y$. For the test target, the references in $T_N^y$ are exactly the $n$ original occurrences. Hence
\[
T_N^y=S_{D_n}(X_N,y).
\]
For each calibration target $i\le n$, the references in $T_i^y$ consist of $D_n^{-i}$ with the candidate test occurrence appended. The collection $D_n^{-i}$ has $n-1\ge k$ entries. Monotonicity therefore yields
\[
T_i^y\le S_{D_n^{-i}}(Z_i)=S_i.
\]
These conclusions remain valid when observations or score values coincide, because deletion and augmentation operate on occurrences.

### 3. Quantile comparison and inclusion

Empirical quantiles at the stated level are coordinatewise monotone. When $\beta\le1$, they are the $r$-th order statistic, and coordinatewise domination implies domination of that order statistic. When $\beta>1$, both quantiles are $+\infty$. Thus, for every $y$,
\[
q_{\rm full}^y\le q.
\]
If $y\in C_{\rm full}(X_N)$, then
\[
S_{D_n}(X_N,y)=T_N^y\le q_{\rm full}^y\le q,
\]
so $y\in C(X_N)$. We have established the samplewise inclusion
\[
C_{\rm full}(X_N)\subseteq C(X_N).
\]

### 4. Final marginal guarantee

Taking the events containing the true label and using the inclusion gives
\[
\Pr\{Y_{n+1}\in C(X_{n+1})\}
\ge\Pr\{Y_{n+1}\in C_{\rm full}(X_{n+1})\}
\ge1-\alpha.
\]
This is the claimed finite-sample marginal guarantee.

## Private Source-Repair Note

The original source's notation appendix caps an out-of-range empirical quantile at the maximum calibration score. That convention does not justify the asserted coverage when $\alpha<1/(n+1)$. The task uses the locally repaired $+\infty$ convention, explicitly recorded in the provenance. The proof above closes all theorem-critical obligations under that repair; no unresolved external dependency remains.
