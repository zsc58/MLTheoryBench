# Problem

## Setup

All distributions below are on \(\mathbb R^d\) and have finite second moments. For such a distribution \(R\), let \(C_R\) denote its covariance matrix. Write \(R_j\) for its \(j\)-th coordinate marginal and define
\[
\delta(P,Q):=\|C_P-C_Q\|_F.
\]

For a centered bivariate distribution \(R\) of \((X,Y)\) with \(\operatorname{Var}_R(X)>0\), define its population least-squares slope by
\[
\beta_R:=\frac{\operatorname{Cov}_R(X,Y)}{\operatorname{Var}_R(X)}.
\]

For distributions with continuous coordinate marginals, write \(\operatorname{Cop}(R)\) for the associated copula measure. A kernel \(k\) on \([0,1]^d\) is called characteristic when its maximum mean discrepancy satisfies \(\operatorname{MMD}_k(\mu,\nu)=0\) only if \(\mu=\nu\).

For a symmetric matrix \(A\), write its eigenvalues in nonincreasing order as \(\lambda_1(A)\ge\cdots\ge\lambda_d(A)\). If \(U_P,U_Q\) are orthonormal bases for two \(r\)-dimensional subspaces, \(\|\sin\Theta(U_P,U_Q)\|_2\) denotes the largest sine of their principal angles.

## Task

Prove the following integrated claim.

1. For every \(d\ge2\) and every \(M>0\), there exist distributions \(P,Q\) with continuous coordinate marginals such that \(P_j=Q_j\) for every \(j\), while \(\operatorname{Cop}(P)\ne\operatorname{Cop}(Q)\),
\[
\operatorname{MMD}_k(\operatorname{Cop}(P),\operatorname{Cop}(Q))>0
\]
for every characteristic kernel \(k\), and \(\delta(P,Q)>M\).

2. If \(P,Q\) are centered bivariate distributions satisfying
\[
\operatorname{Var}_P(X)=\operatorname{Var}_Q(X)=\sigma_X^2>0,
\qquad
\operatorname{Var}_P(Y)=\operatorname{Var}_Q(Y)=\sigma_Y^2>0,
\]
then
\[
|\beta_P-\beta_Q|=\frac{\delta(P,Q)}{\sqrt{2}\,\sigma_X^2}.
\]
Moreover, distributions satisfying these assumptions can have \(\beta_P\) and \(\beta_Q\) of opposite signs.

3. Let \(P,Q\) be zero-mean distributions on \(\mathbb R^d\). Then, for every \(k=1,\ldots,d\),
\[
|\lambda_k(C_P)-\lambda_k(C_Q)|\le\delta(P,Q).
\]
Further, fix \(1\le r<d\), let \(U_P,U_Q\) span the top-\(r\) eigenspaces of \(C_P,C_Q\), and suppose
\[
\gamma:=\lambda_r(C_P)-\lambda_{r+1}(C_P)>0,
\qquad
\delta(P,Q)<\gamma.
\]
Then
\[
\|\sin\Theta(U_P,U_Q)\|_2\le\frac{2\delta(P,Q)}{\gamma}.
\]
