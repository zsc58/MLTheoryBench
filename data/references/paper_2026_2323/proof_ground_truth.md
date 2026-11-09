# Reference Proof

## Proof Structure

Let the ensemble miscoverage event be reduced to a weighted vote. The majority threshold and Markov's inequality give the universal bound under finite-sample base validity. Under asymptotic base validity, the same reduction incurs only an $o(1)$ error. For a coalition whose limiting optimal weight is strictly larger than one-half, weight set-consistency makes its estimated weight exceed one-half with probability tending to one; outside the coalition's collective miscoverage event, the ensemble must then include the response.

## Complete Proof

Write
\[
p_{n,k}=\Pr\{Y\notin C_k(X;D_n)\mid D_n\},
\qquad
M_n=\{Y\notin C_{\rm ens}(X;D_n)\}.
\]
By the weighted-majority definition, on $M_n$ the weighted inclusion sum is at most $1/2$, and therefore
\[
V_n:=\sum_{k=1}^K\widehat w_{n,k}{\bf1}\{Y\notin C_k(X;D_n)\}\ge\tfrac12.
\]
Since $0\le V_n\le1$, Markov's inequality and conditioning on $D_n$ give
\[
\Pr(M_n)\le 2\,\mathbb E[V_n]
 =2\,\mathbb E\!\left[\sum_k\widehat w_{n,k}p_{n,k}\right].
\]
Under finite-sample validity, $p_{n,k}\le\alpha$ almost surely for every $k$, so the last display is at most $2\alpha$. Hence $\Pr\{Y\in C_{\rm ens}(X;D_n)\}\ge1-2\alpha$ for every $n$.

Under asymptotic validity, put $\delta_n=\sup_k|p_{n,k}-\alpha|$. Then
\[
\sum_k\widehat w_{n,k}p_{n,k}\le\alpha+\delta_n.
\]
Here $0\le\delta_n\le1$ and $\delta_n=o_p(1)$, hence $\mathbb E\delta_n=o(1)$ (bounded convergence in probability). The preceding argument yields $\Pr(M_n)\le2\alpha+o(1)$ and therefore the liminf coverage is at least $1-2\alpha$.

Now let $K^*\subseteq\{1,\ldots,K\}$ satisfy
\[
\inf_{w\in W^*}\sum_{k\in K^*}w_k>\tfrac12.
\]
Set $S_n=\sum_{k\in K^*}\widehat w_{n,k}$. The map $w\mapsto\sum_{k\in K^*}w_k$ is continuous, and the strict margin together with $\operatorname{dist}(\widehat w_n,W^*)\to_p0$ implies $\Pr(S_n\le1/2)\to0$. On the event $S_n>1/2$ and $Y\in C_k(X;D_n)$ for every $k\in K^*$, the weighted inclusion sum exceeds $1/2$, so $Y\in C_{\rm ens}(X;D_n)$. Consequently,
\[
\Pr\{Y\in C_{\rm ens}(X;D_n)\}\ge
1-\Pr(S_n\le1/2)-\Pr\Bigl(\bigcup_{k\in K^*}\{Y\notin C_k(X;D_n)\}\Bigr).
\]
If the coalition's collective miscoverage probability has limsup at most $\alpha$, taking liminf gives ensemble coverage at least $1-\alpha$. This argument uses only weight consistency and thus applies in both the finite-sample-valid and asymptotically-valid regimes. A dominant learner is the special case $K^*=\{k^*\}$, for which the condition is $\inf_{w\in W^*}w_{k^*}>1/2$ and the collective event is that learner's miscoverage event.
