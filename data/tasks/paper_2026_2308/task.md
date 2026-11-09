# Problem

## Setup

Let \((X,\mathcal X)\) be a measurable parameter space, let \((Y,\mathcal Y,\nu)\) be an observation space with a \(\sigma\)-finite reference measure \(\nu\), and let \(\mu\) be a probability measure on \(X\). Let \(\ell,\widetilde\ell:Y\times X\to[0,\infty)\) be jointly measurable likelihood densities such that
\[
\int_Y\ell(y\mid x)\,\nu(dy)=\int_Y\widetilde\ell(y\mid x)\,\nu(dy)=1
\quad\text{for }\mu\text{-almost every }x.
\]
Define
\[
z(y)=\int_X\ell(y\mid x)\,\mu(dx),\qquad
\widetilde z(y)=\int_X\widetilde\ell(y\mid x)\,\mu(dx).
\]
Define the posterior probability measures by
\[
\mu^y(dx)=\frac{\ell(y\mid x)\mu(dx)}{z(y)}
\quad\text{when }0<z(y)<\infty,
\qquad
\widetilde\mu^y(dx)=\frac{\widetilde\ell(y\mid x)\mu(dx)}{\widetilde z(y)}
\quad\text{when }0<\widetilde z(y)<\infty.
\]
Set the corresponding posterior equal to \(\mu\) whenever its evidence is zero or infinite.

Let \(\mathcal F\) be a nonempty symmetric class of measurable real-valued functions on \(X\): if \(f\in\mathcal F\), then \(-f\in\mathcal F\). Define its probability-measure domain by
\[
\mathcal P_{\mathcal F}
=\left\{P:\ P\text{ is a probability measure on }(X,\mathcal X),\ 
\int_X|f|\,dP<\infty\text{ for every }f\in\mathcal F\right\}.
\]
For \(P,Q\in\mathcal P_{\mathcal F}\), set
\[
\gamma_{\mathcal F}(P,Q)
=\sup_{f\in\mathcal F}\left|\int_X f\,dP-\int_X f\,dQ\right|.
\]
Assume \(\mu\in\mathcal P_{\mathcal F}\) and that there is a measurable \(\nu\)-null set \(N\subseteq Y\) such that \(\mu^y,\widetilde\mu^y\in\mathcal P_{\mathcal F}\) for every \(y\notin N\). On \(N\), set both posterior measures equal to \(\mu\).

Define
\[
\omega(x)=\sup_{f\in\mathcal F}|f(x)|,
\qquad
\bar\omega=\int_X\omega(x)\,\mu(dx).
\]
Assume that \(\omega\) and the maps
\[
y\longmapsto\gamma_{\mathcal F}(\mu,\mu^y),
\qquad
y\longmapsto\gamma_{\mathcal F}(\mu,\widetilde\mu^y)
\]
are measurable. These functions and \(\bar\omega\) may take the value \(+\infty\). In products of nonnegative extended quantities, use \(0\cdot(+\infty)=(+\infty)\cdot0=0\).

For the two likelihoods define the expected IPM utilities
\[
U_{\mathcal F}=\int_Y\gamma_{\mathcal F}(\mu,\mu^y)z(y)\,\nu(dy),
\qquad
\widetilde U_{\mathcal F}=\int_Y\gamma_{\mathcal F}(\mu,\widetilde\mu^y)\widetilde z(y)\,\nu(dy).
\]
Assume that at least one of \(U_{\mathcal F}\) and \(\widetilde U_{\mathcal F}\) is finite, so their difference is defined. If exactly one is infinite, the absolute difference is \(+\infty\).

## Task

Prove, allowing the right-hand side to be \(+\infty\), that
\[
\left|U_{\mathcal F}-\widetilde U_{\mathcal F}\right|
\leq
\int_Y\int_X\bigl(\omega(x)+\bar\omega\bigr)
\left|\ell(y\mid x)-\widetilde\ell(y\mid x)\right|\,\mu(dx)\,\nu(dy).
\]
