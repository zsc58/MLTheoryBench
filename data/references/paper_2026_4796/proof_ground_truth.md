# Reference Proof

## Proof Structure

Separate the selected calibration scores into exchangeable safe scores and arbitrary contaminated scores. Compare the contaminated threshold with a safe-score order statistic, derive a tie-safe rank bound from exchangeability, and simplify the resulting coverage bound. Finally, use monotonicity and interval containment to establish the level correction, including a possibly random valid upper bound.

## Complete Proof

### 1. Setup and deterministic order-statistic comparison

Let $b=n-m$, and let $G_{(1)}\le\cdots\le G_{(m)}$ be the order statistics of the selected safe calibration scores. Set
\[
k=\left\lceil(n+1)(1-\alpha)\right\rceil,
\qquad r=k-b.
\]
Because $0<\alpha<1$, we have $1\le k\le n+1$ and hence $r\le m+1$.

Suppose first that $1\le r\le m$. At most $r-1$ safe calibration scores are strictly below $G_{(r)}$, and at most $b$ contaminated scores are strictly below it. Thus at most $r-1+b=k-1$ entries of the augmented calibration list are strictly below $G_{(r)}$. Consequently,
\[
q_\alpha\ge G_{(r)}.
\]
This comparison is pointwise and requires no distributional or independence assumption on contaminated scores.

If $r\le0$, probability nonnegativity gives $\mathbb P(R^*\le q_\alpha)\ge0\ge r/(m+1)$. If $r=m+1$, then $k=n+1$, so the appended infinity is the selected order statistic and coverage is one. These cases include every possibility when $m=0$.

### 2. Exchangeable rank bound, including ties

Enumerate the unsorted selected safe scores and the test score as $V_1,\ldots,V_{m+1}$, with $V_{m+1}=R^*$. They are exchangeable by the public assumption. For $1\le r\le m$, let
\[
H_j=\mathbf 1\{V_j\le \text{the $r$-th order statistic of }(V_\ell)_{\ell\ne j}\}.
\]
For any realization, choose an ordering of the coordinates by increasing value, breaking ties arbitrarily. Each of the first $r$ coordinates satisfies the inequality defining $H_j$: after removing that coordinate, the $r$-th remaining value is at least its value. Therefore
\[
\sum_{j=1}^{m+1}H_j\ge r.
\]
Exchangeability makes the expectations of all $H_j$ equal. It follows that
\[
\mathbb P\{R^*\le G_{(r)}\}
=\mathbb E H_{m+1}
=\frac{1}{m+1}\mathbb E\!\left[\sum_{j=1}^{m+1}H_j\right]
\ge\frac{r}{m+1}.
\]
This proves the standard rank inequality directly and does not assume distinct scores.

Combining this result with the deterministic comparison and the boundary cases gives, in every case,
\[
\mathbb P\{R^*\le q_\alpha\}
\ge\frac{k-b}{m+1}.
\]

### 3. Coverage bound and residual interpretation

Using the ceiling inequality,
\[
\frac{k-b}{m+1}
\ge\frac{(n+1)(1-\alpha)-b}{m+1}
=1-\frac{(n+1)\alpha}{m+1}.
\]
Since $n+1=m+1+b$,
\[
1-\frac{(n+1)\alpha}{m+1}
=1-\alpha-\frac{\alpha b}{m+1}
\ge1-\alpha-\frac{b}{m+1}.
\]
The last inequality uses $b\ge0$ and $0<\alpha<1$. With $\delta=b/n$,
\[
\frac{b}{m+1}=\frac{\delta n}{(1-\delta)n+1}=g(\delta,n).
\]
Thus
\[
\mathbb P\{R^*\le q_\alpha\}\ge1-\alpha-g(\delta,n).
\]
Because the outcome and fitted prediction are real and $q_\alpha\ge0$, the event $R^*\le q_\alpha$ is precisely the claimed interval-coverage event. If $q_\alpha=+\infty$, that interval is the whole real line. This establishes the first claim for every joint distribution of contaminated scores consistent with the selected-safe exchangeability assumption.

### 4. Corrected level

On $[0,1]$, the denominator in $g$ is positive and
\[
\frac{\partial}{\partial d}g(d,n)
=\frac{n(n+1)}{((1-d)n+1)^2}>0.
\]
Let $\bar\delta\in[0,1]$ be a valid upper bound on $\delta$, almost surely if it is random. Define
\[
\alpha_0=\alpha-g(\delta,n),
\qquad
\alpha_c=\alpha-g(\bar\delta,n).
\]
The number $\alpha_0$ is fixed because $n,m$, and hence $\delta$, are fixed in this experiment. Monotonicity gives $\alpha_c\le\alpha_0$ almost surely.

If $\alpha_0\le0$, then $\alpha_c\le0$ almost surely and the corrected interval is the whole real line. Otherwise $0<\alpha_0\le\alpha<1$. Applying the first claim at this fixed level gives
\[
\mathbb P\{R^*\le q_{\alpha_0}\}
\ge1-\alpha_0-g(\delta,n)
=1-\alpha.
\]
For each realization with $\alpha_c>0$, the inequality $\alpha_c\le\alpha_0$ implies
\[
\left\lceil(n+1)(1-\alpha_c)\right\rceil
\ge
\left\lceil(n+1)(1-\alpha_0)\right\rceil,
\]
so $q_{\alpha_c}\ge q_{\alpha_0}$. When $\alpha_c\le0$, the corrected interval is the whole line and also contains the interval at level $\alpha_0$. Thus the corrected interval contains the fixed-level interval at $\alpha_0$ almost surely and has coverage at least $1-\alpha$.

For a deterministic upper bound this also follows directly from $1-\alpha_c-g(\delta,n)\ge1-\alpha$. The containment argument establishes the result for a random valid upper bound without conditioning on that bound or assuming it independent of the scores.
