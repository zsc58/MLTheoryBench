# Problem

## Setup

Let \(N\) be a connected, complete, finite-dimensional Riemannian manifold with geodesic distance \(d\), and fix \(o\in N\). Write \(\mathcal P_2(N)\) for the Borel probability measures \(\rho\) on \(N\) satisfying
\[
\int_N d(o,y)^2\,\rho(dy)<\infty.
\]
For Borel probability measures \(\mu,\nu\), let \(\Pi(\mu,\nu)\) denote the Borel probability measures on \(N\times N\) with first marginal \(\mu\) and second marginal \(\nu\).

Let \(\mu,\nu\in\mathcal P_2(N)\), and let \(\gamma\in\Pi(\mu,\nu)\). Fix a Borel probability kernel \(x\mapsto\kappa_x\) giving a disintegration
\[
\gamma(dx,dy)=\mu(dx)\kappa_x(dy).
\]
Here each \(\kappa_x\) is a Borel probability measure on \(N\), and \(x\mapsto\kappa_x(E)\) is Borel for every Borel set \(E\subseteq N\).

Let
\[
X_0:=\left\{x\in N:\int_N d(o,y)^2\,\kappa_x(dy)<\infty\right\}.
\]
Then \(X_0\) has full \(\mu\)-measure. For \(x\in X_0\), define
\[
\phi_x(z):=\frac12\int_N d(z,y)^2\,\kappa_x(dy),\qquad
A(x):=\operatorname*{argmin}_{z\in N}\phi_x(z),\qquad
v(x):=\inf_{z\in N}\phi_x(z).
\]
Set
\[
D(\gamma):=\int_{X_0}v(x)\,\mu(dx).
\]
For a Borel map \(T:N\to N\), define its deterministic squared-distance loss by
\[
L_\gamma(T):=\frac12\int_{N\times N}d(T(x),y)^2\,\gamma(dx,dy),
\]
allowing the value \(+\infty\).

Write \(\delta_z\) for the probability measure concentrated at \(z\), \(\mathrm{id}\) for the identity map on \(N\), and \(F_\#\rho\) for the pushforward of a measure \(\rho\) under a Borel map \(F\), defined by \((F_\#\rho)(E)=\rho(F^{-1}(E))\) for Borel sets \(E\) in its codomain.

## Task

Prove the following integrated claim.

The infimum
\[
\inf_{T\ \mathrm{Borel}}L_\gamma(T)
\]
is attained and equals \(D(\gamma)\). Moreover, a Borel map \(T\) attains this infimum if and only if \(T(x)\in A(x)\) for \(\mu\)-almost every \(x\). Finally, the following are equivalent:
\[
D(\gamma)=0;
\qquad v(x)=0\ \text{for \(\mu\)-almost every }x;
\qquad \kappa_x=\delta_{T(x)}\ \text{for \(\mu\)-almost every }x\ \text{for some Borel }T;
\qquad \gamma=(\mathrm{id},T)_\#\mu\ \text{for some Borel }T.
\]

Also prove that the definition of \(X_0\) is independent of the chosen reference point \(o\) up to a \(\mu\)-null set.
