# Problem

## Setup

Let \(k,d,p\) be positive integers with \(d\ge k\). Let \(\mathcal U\subseteq\mathbb R^k\), \(\mathcal W\subseteq\mathbb R^d\), \(\mathcal X\subseteq\mathbb R^p\), and \(\mathcal Y\subseteq\mathbb R\) be nonempty Borel sets. An unobserved confounder \(U\), proxy \(W\), treatment \(X\), and outcome \(Y\), taking values in these respective sets, arise from measurable structural equations
\[
U\leftarrow N_U,\qquad W\leftarrow f_W(U,E),\qquad X\leftarrow f_X(U,N_X),\qquad Y\leftarrow f_Y(U,X,N_Y),
\]
where the exogenous noises are mutually independent. The observational law is well defined and has a density with respect to a sigma-finite product measure \(\mu_U\otimes\mu_W\otimes\mu_X\otimes\mu_Y\), positive exactly on \(\mathcal U\times\mathcal W\times\mathcal X\times\mathcal Y\). The interventional law under \(\mathrm{do}(X=x)\) exists for every \(x\in\mathcal X\). Assume common support:
\[
p_{X\mid U}(x\mid u)>0
\quad\text{for every }x\in\mathcal X\text{ and for }P_U\text{-almost every }u,
\]
where treatment densities are with respect to \(\mu_X\).

For fixed treatment values, use the conditional outcome kernels specified by the structural equations. Explicitly, the kernel given \(U=u,X=x\) is
\[
B\longmapsto \mathbb P\{f_Y(u,x,N_Y)\in B\},\qquad B\subseteq\mathbb R\text{ Borel}.
\]
After a one-to-one change of confounder coordinates, use this same kernel expressed in the new coordinates. This convention also applies at treatment values of observational probability zero; conditional outcome expectations in the task do not refer to arbitrary versions modified at those values.

Assume, for every \(x\in\mathcal X\), that
\[
\mathbb E^{\mathrm{do}(X=x)}|Y|<\infty,
\]
and that \(u\mapsto\mathbb E[|Y|\mid U=u,X=x]\), with the specified kernel convention, is finite \(P_U\)-almost everywhere and \(P_U\)-integrable. Define
\[
\theta(x)=\mathbb E^{\mathrm{do}(X=x)}[Y].
\]

The proxy conditional mechanism is known and is additive:
\[
W=AU+E,
\]
where \(A\in\mathbb R^{d\times k}\) has full column rank and \(E\) has known Lebesgue density \(p_E\). Assume
\[
\widehat p_E(t)=(2\pi)^{-d/2}\int_{\mathbb R^d}p_E(e)e^{-it^\top e}\,de\ne0
\quad\text{for every }t\in\mathbb R^d.
\]

Fix a positive integer \(m\) and a nonempty parameter set \(\Gamma\). For each \(\gamma\in\Gamma\), let \(H_\gamma:\mathcal X\times\mathcal Y\times\mathbb R^m\to\mathbb R^d\) be Borel measurable and define
\[
V_\gamma(x,y,\varepsilon,e)=H_\gamma(x,y,\varepsilon)+e.
\]
Here \(\varepsilon\sim N(0,I_m)\) and \(e\sim P_E\) are independent of each other and of the observational variables. The primed pair \((\varepsilon',e')\) is an independent copy. Whenever noise is subtracted from \(V_\gamma\), it is the same draw \(e\) used in that output, not a fresh draw. Write
\[
Q_{\gamma,x,y}=\mathcal L(V_\gamma(x,y,\varepsilon,e)).
\]

For a probability law \(Q\) on \(\mathbb R^d\) with finite first moment, define the energy score using independent \(V,V'\sim Q\) by
\[
\operatorname{ES}(Q,w)=\mathbb E\|V-w\|_2-\tfrac12\mathbb E\|V-V'\|_2.
\]
For each \(\gamma\), assume that \(Q_{\gamma,x,y}\) has a finite first moment for \(P_{X,Y}\)-almost every \((x,y)\) and that the population objective
\[
R(\gamma)=\mathbb E\bigl[\operatorname{ES}(Q_{\gamma,X,Y},W)\bigr]
\]
is finite. Conditional laws on exceptional null sets may be assigned arbitrary versions wherever they do not enter these integrals.

Fix versions of \(P_{W\mid X=x,Y=y}\) on \(\mathcal X\times\mathcal Y\). Assume correct specification: there is one \(\gamma_0\in\Gamma\) such that
\[
Q_{\gamma_0,x,y}=P_{W\mid X=x,Y=y}
\quad\text{for every }(x,y)\in\mathcal X\times\mathcal Y.
\]
Let \(\gamma^*\) be any population minimizer of \(R\).

## Task

Prove that:

1. There exists a full-column-rank matrix \(\widetilde A\in\mathbb R^{d\times k}\) such that, for \(P_{X,Y}\)-almost every \((x,y)\),
\[
\mathcal L(V_{\gamma^*}(x,y,\varepsilon,e))=P_{W\mid X=x,Y=y}
\]
and
\[
\mathcal L(H_{\gamma^*}(x,y,\varepsilon))
=\mathcal L(\widetilde A U\mid X=x,Y=y).
\]
Here \(H_{\gamma^*}(x,y,\varepsilon)=V_{\gamma^*}(x,y,\varepsilon,e)-e\).

2. With \(Z=\widetilde A U\), adjustment for \(Z\) gives the same causal function as adjustment for \(U\):
\[
\theta(x)=\mathbb E\!\left[\mathbb E[Y\mid Z,X=x]\right]
\quad\text{for every }x\in\mathcal X,
\]
using the fixed-treatment kernel convention specified above. The outer expectation is with respect to the marginal law of \(Z\).
