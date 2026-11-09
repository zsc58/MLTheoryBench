# Problem

## Setup

Fix an integer d≥1 and a real number s>d/2+2. Write H^s=H^s(ℝ^d;ℝ^d), with its usual inhomogeneous Sobolev norm, and define
\[
\mathcal D^s=\{\Phi:\mathbb R^d\to\mathbb R^d:\ \Phi\text{ is a }C^1\text{ diffeomorphism and }\Phi-\mathrm{id}\in H^s\}.
\]
Let \(\mathcal D_0^s\) be the identity component, consisting of endpoints of flows
\[
\dot X_t(x)=U_t(X_t(x)),\qquad X_0(x)=x,
\]
with \(U\in L^1([0,1];H^s)\). For \(\Phi\in\mathcal D_0^s\), define
\[
A_s(\Phi)=\inf\left\{\int_0^1\|U_t\|_{H^s}^2\,dt:\ U\in L^2([0,1];H^s),\ X_1=\Phi\right\},
\]
where the infimum of an empty set is +∞.

Fix a bounded Lebesgue-measurable set \(\Omega\subset\mathbb R^d\) and finite positive bounds B and L. Let \(\rho:\mathbb R^d\to[0,\infty)\) be a compactly supported probability density satisfying
\[
\operatorname{supp}\rho\subset\Omega,\qquad \|\rho\|_{L^\infty}\le B,\qquad |\rho(x)-\rho(y)|\le L|x-y|\quad(x,y\in\mathbb R^d),
\]
and write \(\mu=\rho\,dx\).

For \(\sigma(r)=\max\{r,0\}\), a width-one piecewise-constant ReLU control has velocity
\[
V_t(x)=w_t\sigma(a_t\cdot x+b_t),\qquad w_t,a_t\in\mathbb R^d,\quad b_t\in\mathbb R,
\]
where \((w_t,a_t,b_t)\) is constant on each interval of a finite partition of [0,1]. A switch is a jump of this parameter triple at an interior partition point. Its terminal flow map is denoted by \(\Psi\).

For finite measures ν and λ, use the normalization
\[
\operatorname{TV}(\nu,\lambda)=\sup_{f\text{ Borel},\ |f|\le1}\left|\int f\,d(\nu-\lambda)\right|.
\]
For a Borel map F, its pushforward is \(F_\#\mu(E)=\mu(F^{-1}(E))\) for Borel sets E. The norm \(L^2(\Omega)\) below uses Lebesgue measure and the Euclidean norm of the map difference.

## Task

Prove that there is a constant C depending only on d,s,Ω,B,L such that, for every ε∈(0,1), every \(\Phi\in\mathcal D_0^s\) with finite \(A_s(\Phi)\), and every density ρ satisfying the conditions above, one can choose a width-one piecewise-constant ReLU flow \(\Psi_N\) with at most
\[
N\le C\exp\!\bigl(C\sqrt{A_s(\Phi)}\bigr)\bigl(1+A_s(\Phi)\bigr)\varepsilon^{-2}
\]
switches and satisfying simultaneously
\[
\|\Psi_N-\Phi\|_{L^2(\Omega)}\le\varepsilon,
\qquad
\operatorname{TV}\bigl((\Psi_N)_\#\mu,\Phi_\#\mu\bigr)\le\varepsilon.
\]
