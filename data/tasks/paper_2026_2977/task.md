# Problem

## Setup

Let \(T_1,\ldots,T_n,\widetilde T\) be real-valued calibration and test scores on a common probability space. Write \(T_{(1)}\le\cdots\le T_{(n)}\) for the calibration order statistics and let \(\mathcal C_n=\sigma(T_1,\ldots,T_n)\). For \(1\le k\le n\), define
\[
D_{n,k}=\Pr(\widetilde T\le T_{(k)}\mid\mathcal C_n),\qquad \nu_{n,k}=\operatorname{Law}(D_{n,k}).
\]
Let \(\beta_{n,k}=\operatorname{Beta}(k,n+1-k)\) be the law on [0,1] of the kth order statistic of n iid Uniform(0,1) variables. For probability laws on [0,1] and \(p\ge1\), let \(W_p\) denote p-Wasserstein distance and define
\[
\mathcal B_p(\beta_{n,k},\rho)=\{\nu:W_p(\nu,\beta_{n,k})\le\rho\},\qquad \rho\ge0.
\]
Assume \(\nu_{n,k}\in\mathcal B_p(\beta_{n,k},\rho)\) for every \(1\le k\le n\). Let \(F_{\beta_{n,k}}\) be the beta CDF, extended by 1 for arguments at least 1, and define \(\operatorname{Cov}(k)=\Pr(\widetilde T\le T_{(k)})\). For \(\gamma\in(0,1)\) satisfying \(k_\gamma=\lceil(n+1)\gamma\rceil\le n\), use the corresponding \(D_{n,k_\gamma}\) and \(\operatorname{Cov}(k_\gamma)\).

## Task

Prove the following integrated theorem. For every \(1\le k\le n\),
\[
\left|\operatorname{Cov}(k)-\frac{k}{n+1}\right|\le W_1(\nu_{n,k},\beta_{n,k})\le W_p(\nu_{n,k},\beta_{n,k})\le\rho.
\]
Consequently, for every admissible \(\gamma\),
\[
\left|\operatorname{Cov}(k_\gamma)-\gamma\right|\le\rho+\frac1{n+1}.
\]
Moreover, if \(B\sim\beta_{n,k}\), \(F_{\nu_{n,k}}\) is the CDF of \(\nu_{n,k}\), and \(T=F_{\nu_{n,k}}^{-1}\circ F_{\beta_{n,k}}\) is the monotone transport map, then for every \(t\in[0,1]\) and \(\varepsilon>0\),
\[
\Pr(D_{n,k}\le t)\le F_{\beta_{n,k}}(t+\varepsilon)+\left(\frac{\rho}{\varepsilon}\right)^p.
\]
If additionally \(|T(B)-B|\le\rho\) almost surely, then
\[
\Pr(D_{n,k}\le t)\le F_{\beta_{n,k}}(t+\rho)
\]
for every \(t\in[0,1]\).
