# Problem

## Setup

An environment specifies an exogenous sequence of states \(Y_t\in\{0,1\}\), where 0 denotes a null and 1 an alternative. The states are not observed by the procedure. Conditional on the entire state sequence, the p-values \(p_t\in[0,1]\) are independent, with distribution \(\mathrm{Unif}[0,1]\) when \(Y_t=0\) and CDF \(G\) when \(Y_t=1\).

Fix a deterministic procedure, consisting of one measurable decision rule for each round. At round \(t\), it chooses a threshold \(\lambda_t\in[0,1]\) using only its observed past, before observing \(p_t\), and rejects exactly when \(p_t\le\lambda_t\). Write
\[
\delta_t=\mathbf 1\{p_t\le\lambda_t\},\qquad
\mathcal F_t=\sigma((p_s,\lambda_s,\delta_s):1\le s\le t),
\]
with \(\mathcal F_0\) trivial, and require \(\lambda_t\) to be \(\mathcal F_{t-1}\)-measurable.

The CDF \(G:[0,1]\to[0,1]\) is continuous and strictly increasing, with \(G(0)=0\), \(G(1)=1\). There is a finite constant \(L\ge1\) such that
\[
|G(x)-G(y)|\le L|x-y|\qquad(x,y\in[0,1]),
\]
and there exist \(\mu>0\) and \(x_0\in(0,1]\) such that \(G(x)\ge\mu x\) for all \(x\in[0,x_0]\).

Fix \(a,b>0\) and \(\beta\in(0,1)\), and write \(\lambda_\beta=G^{-1}(\beta)\). Define
\[
V_T=\sum_{t=1}^T\mathbf 1\{Y_t=0,\ p_t\le\lambda_t\},\qquad
M_T=\sum_{t=1}^T\mathbf 1\{Y_t=1,\ p_t>\lambda_t\},\qquad
\operatorname{Regret}_T=aV_T+bM_T.
\]
For the fixed procedure, let \(\widetilde\lambda_t\) be the supremum of its threshold at time \(t\) over all observable histories consistent with its decision rules and having no previous rejection. If there is no such history, set this supremum to zero. Write \((x)_+=\max\{x,0\}\).

## Task

Prove the following integrated claim.

(i) In the stationary environment with iid states satisfying \(\Pr(Y_t=0)=\pi\in(0,1)\), if \(\lambda_t\ge\lambda_\beta\) almost surely for every \(t\), then, for every integer \(T\ge1\),
\[
\mathbb E[\operatorname{Regret}_T]\ge a\pi\lambda_\beta T,
\]
and
\[
\liminf_{T\to\infty}\frac{\operatorname{Regret}_T}{T}\ge a\pi\lambda_\beta
\quad\text{almost surely}.
\]

(ii) If \(\sum_{t\ge1}\widetilde\lambda_t\le C<1\), then for every integer \(n\ge1\), in the environment consisting of nulls in rounds \(1,\ldots,n\) and alternatives in rounds \(n+1,\ldots,2n\),
\[
\mathbb E[\operatorname{Regret}_{2n}]\ge b\,n(1-C)
\prod_{t=n+1}^{2n}(1-L\widetilde\lambda_t)_+.
\]
For the fixed procedure and constants, this lower bound has linear order in \(n\) for all sufficiently large \(n\).

Finally, prove that no deterministic procedure with the specified information can guarantee both \(\mathbb E V_T=o(T)\) and \(\mathbb E M_T=o(T)\) uniformly over environments in this model. More precisely, for every such procedure there is an environment in which its expected weighted regret is \(\Omega(T)\), meaning that it is bounded below by \(cT\) for some \(c>0\) and all sufficiently large integers \(T\).
