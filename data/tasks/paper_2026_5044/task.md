# Problem

## Setup

Let \(d,N,K\) be positive integers, let \(x_1,\ldots,x_N\in\mathbb R^d\), and let \(\widehat P_N=N^{-1}\sum_{n=1}^N\delta_{x_n}\). Write \(\mathcal P_2(\mathbb R^d)\) for probability measures with finite second moment and \(W_2\) for Wasserstein-2 distance. Fix \(r>0\) and set
\[
\mathcal B_r(\widehat P_N)=\{P\in\mathcal P_2(\mathbb R^d):W_2(P,\widehat P_N)\le r\}.
\]

For centers \(M=(\mu_1,\ldots,\mu_K)\in(\mathbb R^d)^K\) and a measurable partition \(\Phi=(C_1,\ldots,C_K)\) of \(\mathbb R^d\), let \(Q_{M,\Phi}(x)=\mu_k\) on \(C_k\) and, for \(P\in\mathcal P_2(\mathbb R^d)\), define
\[
\operatorname{Risk}(M,\Phi,P)=\mathbb E_P\|X-Q_{M,\Phi}(X)\|^2.
\]
Define
\[
\operatorname{WC}(M)=\sup_{P\in\mathcal B_r(\widehat P_N)}\mathbb E_P\min_{1\le k\le K}\|X-\mu_k\|^2.
\]
Let
\[
\Delta_K=\left\{\pi\in[0,\infty)^K:\sum_{k=1}^K\pi_k=1\right\},
\]
let \(\Pi=(\pi_1,\ldots,\pi_N)\) with \(\pi_n\in\Delta_K\), and write \(M\pi_n=\sum_{k=1}^K\pi_{kn}\mu_k\). For \(\gamma>1\), define
\[
J(M,\Pi,\gamma)=\gamma r^2+\frac1N\sum_{n=1}^N\left[\sum_{k=1}^K\pi_{kn}\|x_n-\mu_k\|^2+\frac{1}{\gamma-1}\|x_n-M\pi_n\|^2\right].
\]

## Task

Prove the following integrated theorem. For every fixed \(M\),
\[
\operatorname{WC}(M)=\inf_{\gamma>1}\left\{\gamma r^2+\frac1N\sum_{n=1}^N e_n(\gamma,M)\right\},
\qquad
 e_n(\gamma,M)=\sup_{x\in\mathbb R^d}\left[\min_{1\le k\le K}\|x-\mu_k\|^2-\gamma\|x-x_n\|^2\right],
\]
and, for every \(\gamma>1\) and every \(n\in\{1,\ldots,N\}\),
\[
e_n(\gamma,M)=\min_{\pi\in\Delta_K}\left\{\sum_{k=1}^K\pi_k\|x_n-\mu_k\|^2+\frac{1}{\gamma-1}\|x_n-M\pi\|^2\right\}.
\]
Moreover, suppose \((M^*,\Pi^*,\gamma^*)\) is a local minimizer of \(J\) over
\[
(\mathbb R^d)^K\times\Delta_K^N\times(1,\infty),
\]
where local minimality is relative to this feasible set. Suppose each \(\pi_n^*\) attains the displayed simplex minimum for \((M^*,\gamma^*)\), and define
\[
x_n^*=x_n+\frac{x_n-M^*\pi_n^*}{\gamma^*-1}.
\]
Then every nonempty cluster, meaning every \(k\) with \(s_k^*:=\sum_{n=1}^N\pi_{kn}^*>0\), satisfies
\[
\mu_k^*=\frac{\sum_{n=1}^N\pi_{kn}^*x_n^*}{\sum_{n=1}^N\pi_{kn}^*},
\]
and
\[
\gamma^*=1+\frac1r\sqrt{\frac1N\sum_{n=1}^N\|x_n-M^*\pi_n^*\|^2}.
\]
