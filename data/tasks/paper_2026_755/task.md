# Problem

## Setup

Let \(n,d\) be positive integers, and fix \(q>1\). Draw two independent centers \(\theta_1,\theta_2\sim N(0,I_d)\). Fix nonempty true label classes \(T_1,T_2\) partitioning \([n]=\{1,\ldots,n\}\), and draw independent noises \(\epsilon_i\sim N(0,\sigma^2 I_d)\), independent of the centers and labels. Set
\[
y_i=\theta_{z_i^\star}+\epsilon_i,
\]
where \(z_i^\star=\ell\) iff \(i\in T_\ell\).

A current partition is a bipartition \(A_1\sqcup A_2=[n]\) with both parts nonempty. Its empirical centroids are \(\bar y_j=|A_j|^{-1}\sum_{i\in A_j}y_i\). It is \(q\)-approximately balanced if both sizes exceed \(2\), and
\[
\bigl||A_j|-n/2\bigr|<q\sqrt n/2\qquad(j=1,2).
\]
One Lloyd update assigns each \(y_i\) to the current centroid with smaller squared Euclidean distance (ties have probability zero); a partition is a Lloyd fixed point if this update leaves every assignment unchanged.

Fix \(\beta>1\), put
\[
\sigma=\frac{\beta\,(n+q\sqrt n-2)}{\sqrt{2}\,\sqrt{n+q\sqrt n}},
\]
and define
\[
\rho_q=1-\left(\frac{(1+\frac{2}{n+q\sqrt n})\sigma^2-\left[2(1-\frac{2}{n+q\sqrt n})^2+(1-\frac{2}{n+q\sqrt n})\sigma^2\right]}{(1+\frac{2}{n+q\sqrt n})\sigma^2+\left[2(1-\frac{2}{n+q\sqrt n})^2+(1-\frac{2}{n+q\sqrt n})\sigma^2\right]}\right)^2.
\]
Under the stated regime, \(0<\rho_q<1\).

## Task

Prove that, with probability at least
\[
1-2^n n\,\rho_q^{d/4},
\]
every \(q\)-approximately balanced partition of \([n]\) is a fixed point of the Lloyd update.
