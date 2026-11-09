# Problem

## Setup

Let \(n,m\) be positive integers. For each positive integer \(r\), write
\[
\Delta_r=\left\{p\in\mathbb R_+^r:\sum_{i=1}^r p_i=1\right\},
\]
and let \(\mathbf 1_r\) denote the vector of \(r\) ones. For probability vectors \(\mu\in\Delta_n\) and \(\nu\in\Delta_m\), define
\[
\Gamma(\mu,\nu)=\{\gamma\in\mathbb R_+^{n\times m}:\sum_j\gamma_{ij}=\mu_i,\ \sum_i\gamma_{ij}=\nu_j\}.
\]
Let \(K\in\mathbb R^{n\times m\times n\times m}\). For \(A\in\mathbb R^{n\times m}\), define
\[
(K\otimes A)_{kl}=\sum_{i=1}^n\sum_{j=1}^m K_{ijkl}A_{ij},
\qquad
\langle K\otimes A,A\rangle=\sum_{i=1}^n\sum_{j=1}^m\sum_{k=1}^n\sum_{l=1}^m K_{ijkl}A_{ij}A_{kl}.
\]
Assume \(K\) is symmetric: \(K_{ijkl}=K_{klij}\). Define
\[
\mathsf{GW}(K,\mu,\nu)=\min_{\gamma\in\Gamma(\mu,\nu)}\langle K\otimes\gamma,\gamma\rangle.
\]
Assume further that, for every \(\gamma_1,\gamma_2\in\Gamma(\mu,\nu)\),
\[
\big\langle K\otimes(\gamma_1-\gamma_2),\gamma_1-\gamma_2\big\rangle\le0.
\]
For \(\gamma\in\Gamma(\mu,\nu)\), let \(\operatorname{supp}(\gamma)=\{(i,j):\gamma_{ij}>0\}\). When \(n=m\), let \(\mathsf{Perm}_n\) be the set of matrices \((1/n)P\), where \(P\) is an \(n\times n\) permutation matrix.

## Task

Prove the following integrated structural claim: a minimizer \(\gamma^*\in\Gamma(\mu,\nu)\) exists with
\[
|\operatorname{supp}(\gamma^*)|\le n+m-1.
\]
Moreover, if \(n=m\) and \(\mu=\nu=(1/n)\mathbf 1_n\), a minimizer can be chosen in \(\mathsf{Perm}_n\), and
\[
\mathsf{GW}(K,\mu,\nu)=\min_{\gamma\in\mathsf{Perm}_n}\langle K\otimes\gamma,\gamma\rangle.
\]
