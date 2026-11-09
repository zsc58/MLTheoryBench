# Reference Proof

## Proof Structure

1. Establish the mean-squared error of the per-sample clipped estimator under the finite p-th moment assumption by separately controlling clipping bias and sampling variance.
2. Apply L-smoothness to one update and use polarization to obtain a descent inequality involving the true gradient and estimator error.
3. Condition on each iterate, use the fresh batch error bound, telescope over the updates, and divide by the total step-size weight.

## Complete Proof

Write $g_t=\nabla F(x_t)$ and let $Y_{t,k}=\nabla f(x_t,z_{t,k})$. For fixed $x_t$, set $\mu=\mathbb E[Y_{t,k}]=\nabla F(x_t)$ and
\[
 c_{t,k}=\min\left\{1,\frac{\sigma k^{1/p}}{\|Y_{t,k}\|}\right\},\qquad Z_{t,k}=Y_{t,k}c_{t,k}.
\]
The batch estimator is $\widehat g_t=n^{-1}\sum_{k=1}^n Z_{t,k}$. We first prove, conditionally on $x_t$, that
\[
\mathbb E\left[\|\widehat g_t-\nabla F(x_t)\|^2\mid x_t\right]\le 8\sigma^2 n^{-2(p-1)/p}.
\]

More generally, let $Y_k$ be independent copies of a vector $Y$ with $\mathbb E\|Y\|^p\le \sigma^p$, let $r_k=\alpha k^{1/p}$ with $\alpha\ge\sigma$, and let $c_k=\min\{1,r_k/\|Y_k\|\}$. Put $\mu=\mathbb E Y$ and $\mu_k=\mathbb E[Y_kc_k]$. Since $c_k-1$ vanishes when $\|Y_k\|\le r_k$,
\[
\|\mu_k-\mu\|\le \mathbb E[\|Y_k\|\mathbf 1_{\{\|Y_k\|>r_k\}}]
\le r_k^{1-p}\mathbb E\|Y_k\|^p
\le \sigma^p\alpha^{1-p}k^{(1-p)/p}.
\]
Using $\sum_{k=1}^n k^{-(p-1)/p}\le 2n^{1/p}$ and $\sigma\le\alpha$ gives
\[
\left\|\frac1n\sum_{k=1}^n\mu_k-\mu\right\|^2
\le 4\alpha^2n^{-2(p-1)/p}.
\]
Also, for every vector $y$ and $r>0$,
\[
\|y\|^2\min\{1,r^2/\|y\|^2\}\le r^{2-p}\|y\|^p.
\]
Therefore
\[
\mathbb E\|Y_kc_k\|^2\le \alpha^{2-p}k^{(2-p)/p}\sigma^p.
\]
Independence yields
\[
\mathbb E\left\|\frac1n\sum_{k=1}^n(Z_k-\mu_k)\right\|^2
=\frac1{n^2}\sum_{k=1}^n\mathbb E\|Z_k-\mu_k\|^2
\le\frac1{n^2}\sum_{k=1}^n\mathbb E\|Z_k\|^2.
\]
Since $\sum_{k=1}^n k^{(2-p)/p}\le 2n^{2/p}$ and $\sigma\le\alpha$, the last display is at most $4\alpha^2n^{-2(p-1)/p}$. Combining variance and squared bias gives
\[
\mathbb E\left\|\frac1n\sum_{k=1}^nY_kc_k-\mu\right\|^2
\le 8\alpha^2n^{-2(p-1)/p}.
\]
Taking $\alpha=\sigma$ proves the claimed conditional estimator bound.

Now use L-smoothness for the update $x_{t+1}=x_t-\eta_t\widehat g_t$:
\[
F(x_{t+1})\le F(x_t)-\eta_t\langle g_t,\widehat g_t\rangle+\frac{L\eta_t^2}{2}\|\widehat g_t\|^2.
\]
With $e_t=g_t-\widehat g_t$, polarization gives
\[
-\langle g_t,\widehat g_t\rangle
=-\tfrac12\|g_t\|^2-\tfrac12\|\widehat g_t\|^2+\tfrac12\|e_t\|^2.
\]
Hence
\[
F(x_{t+1})\le F(x_t)-\frac{\eta_t}{2}\|g_t\|^2+\frac{\eta_t}{2}\|e_t\|^2-\frac{\eta_t(1-L\eta_t)}2\|\widehat g_t\|^2.
\]
Because $\eta_t<1/L$, the final term is nonpositive, so
\[
\eta_t\|g_t\|^2\le 2(F(x_t)-F(x_{t+1}))+\eta_t\|e_t\|^2.
\]
Summing over $t=1,\ldots,T$ and using $F(x_{T+1})\ge F^*$ gives
\[
\sum_{t=1}^T\eta_t\|\nabla F(x_t)\|^2
\le 2\Delta_1+\sum_{t=1}^T\eta_t\|\widehat g_t-\nabla F(x_t)\|^2.
\]
Take expectations. The conditional estimator bound and the tower property imply
\[
\mathbb E\|\widehat g_t-\nabla F(x_t)\|^2\le 8\sigma^2n^{-2(p-1)/p}.
\]
Therefore
\[
\sum_{t=1}^T\eta_t\mathbb E\|\nabla F(x_t)\|^2
\le 2\Delta_1+8\sigma^2n^{-2(p-1)/p}\sum_{t=1}^T\eta_t.
\]
Dividing by $\sum_{t=1}^T\eta_t>0$ proves the stated bound.
