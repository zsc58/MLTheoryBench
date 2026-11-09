# Problem

## Setup

Let \(\mathbb S^2\) be the unit sphere in \(\mathbb R^3\), and let
\[
\mathcal Y=\bigsqcup_{m\geq1}(\mathbb S^2)^m/S_m
\]
be the space of finite unordered point clouds, where \(S_m\) acts by permuting coordinates. Equip this space with its disjoint-union quotient Borel structure. A cloud is a multiset, and its empirical probability measure is
\[
\mu_y=|y|^{-1}\sum_{u\in y}\delta_u,
\]
with multiplicities included in the sum. Write \(\mathcal P(\mathbb S^2)\) for the Borel probability measures on the sphere, equipped with the Borel structure of weak convergence.

Use the following fixed spherical sliced discrepancy. Let \(\mathbb S^1\) be the unit circle, with geodesic distance \(r(a,b)=\arccos(a^\top b)\). For probability measures \(\eta,\zeta\) on \(\mathbb S^1\), define
\[
W_{2,\mathbb S^1}(\eta,\zeta)^2
=\inf_{\pi\in\Pi(\eta,\zeta)}
\int r(a,b)^2\,\pi(da,db),
\]
where \(\Pi(\eta,\zeta)\) is the set of probability measures with marginals \(\eta\) and \(\zeta\).

Let \(V=\{U\in\mathbb R^{3\times2}:U^\top U=I_2\}\). In circle coordinates, the great-circle projection associated with \(U\in V\) is
\[
P^U(u)=
\begin{cases}
U^\top u/\|U^\top u\|_2,&U^\top u\ne0,\\
(1,0),&U^\top u=0.
\end{cases}
\]
Fix either the uniform probability measure \(\rho\) on \(V\), or \(\rho=L^{-1}\sum_{\ell=1}^L\delta_{U_\ell}\) for a fixed positive integer \(L\) and fixed frames \(U_1,\ldots,U_L\in V\). Use this same fixed choice in every evaluation. For \(\mu,\nu\in\mathcal P(\mathbb S^2)\), define
\[
d(\mu,\nu)=
\left(\int_V W_{2,\mathbb S^1}\bigl(P^U_\#\mu,P^U_\#\nu\bigr)^2\,\rho(dU)\right)^{1/2},
\]
where \(P^U_\#\mu\) is the distribution of \(P^U(u)\) when \(u\) has law \(\mu\). Use the same notation for clouds: \(d(y,y')=d(\mu_y,\mu_{y'})\).

Let \(\mathcal X\) be a measurable covariate space and let \(f:\mathcal X\to\mathcal P(\mathbb S^2)\) be a fixed measurable predictor. Define
\[
S(y,f(x))=d(\mu_y,f(x)).
\]
Let \(n,n_0\) be positive integers. Suppose \((X_i,Y_i)_{i=1}^{n+1}\) are exchangeable \(\mathcal X\times\mathcal Y\)-valued random pairs. For \(\alpha\in(0,1)\), put \(S_i=S(Y_i,f(X_i))\) and \(k=\lceil(n+1)(1-\alpha)\rceil\). If \(k\leq n\), let \(\tau_\alpha\) be the \(k\)-th smallest of \(S_1,\ldots,S_n\), counting multiplicities; otherwise let \(\tau_\alpha=+\infty\). Define
\[
C_\alpha^{\rm amb}(x)=\{y\in\mathcal Y:S(y,f(x))\leq\tau_\alpha\}.
\]

Assume \(Y_1^0,\ldots,Y_{n_0}^0,Y_{n+1}\) are iid with common law \(Q\), supported on a bounded measurable manifold \(M\subset\mathcal Y\). Assume the training vector \((Y_1^0,\ldots,Y_{n_0}^0)\) is independent of the calibration sample \((X_i,Y_i)_{i=1}^n\).

Fix \(\varepsilon>0\) and a finite measurable cover \(A_1,\ldots,A_{N_\varepsilon}\) of \(M\), where \(N_\varepsilon\geq1\), such that
\[
\sup_{y,y'\in A_j}d(y,y')\leq\varepsilon
\quad\text{for every }j.
\]
Define
\[
\beta_\varepsilon=\min_{1\leq j\leq N_\varepsilon}Q(A_j).
\]
From \(D_0=\{Y_i^0\}_{i=1}^{n_0}\), define
\[
d_M(y)=\min_{1\leq i\leq n_0}d(y,Y_i^0),\qquad
C_\alpha(x)=\{y\in\mathcal Y:S(y,f(x))\leq\tau_\alpha\text{ and }d_M(y)\leq\varepsilon\}.
\]

## Task

Prove that
\[
\Pr\bigl(Y_{n+1}\in C_\alpha(X_{n+1})\bigr)
\geq1-\alpha-N_\varepsilon(1-\beta_\varepsilon)^{n_0}.
\]
