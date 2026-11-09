# Problem

## Setup

Let \((X,\mathcal X)\) be a measurable input space and let Y be a nonempty finite label set equipped with its discrete sigma-algebra. Let P_x be a probability measure on X and let \(\eta^*(\cdot\mid x)\) be a measurable probability kernel on Y. Set \(P(dx,dy)=P_x(dx)\eta^*(dy\mid x)\).

Fix a model classifier h and an expert classifier e, with measurable real-valued losses \(\ell_h,\ell_e:X\times Y\to\mathbb R\). Fix \(\gamma>0\), and for \(a\in\{h,e\}\) define

\[
L_a(x)=\sum_{y\in Y}\eta^*(y\mid x)\ell_a(x,y).
\]

For probability measures U absolutely continuous with respect to V, use

\[
\mathrm{KL}(U\|V)=\int\log\left(\frac{dU}{dV}\right)\,dU.
\]

Define the marginal KL ideal \(Q_m^a\) as a minimizer over probability measures \(Q\ll P_x\) of

\[
\mathbb E_Q L_a(X)+\gamma\,\mathrm{KL}(Q\|P_x).
\]

Define the joint KL ideal \(R_j^a\) as a minimizer over probability measures \(R\ll P\) of

\[
\mathbb E_R\ell_a(X,Y)+\gamma\,\mathrm{KL}(R\|P),
\]

and let \(Q_j^a\) denote its X-marginal. In these minimizations, competitors with an undefined objective are excluded; defined extended-real objective values are allowed. Assume that all four minima are attained and that the chosen minimizers satisfy, for each \(a\in\{h,e\}\),

\[
\int|L_a|\,dQ_m^a<\infty,
\qquad \mathrm{KL}(Q_m^a\|P_x)<\infty,
\]

\[
\int|\ell_a|\,dR_j^a<\infty,
\qquad \mathrm{KL}(R_j^a\|P)<\infty.
\]

Choose measurable versions of the Radon–Nikodym ratios

\[
\rho_i=\frac{dQ_i^h}{dQ_i^e},\qquad i\in\{m,j\},
\]

and, for positive thresholds \(\tau_i\), define \(r_i(x)=\mathbf 1\{\rho_i(x)\le\tau_i\}\). Finally set

\[
\widetilde\eta_\gamma(y\mid x)=
\frac{\eta^*(y\mid x)e^{-\ell_e(x,y)/\gamma}}
{\mathbb E_{Y'\sim\eta^*(\cdot\mid x)}e^{-\ell_e(x,Y')/\gamma}}.
\]

## Task

Prove that for every real loss-difference cutoff \(c\in\mathbb R\), there are positive thresholds \(\tau_m,\tau_j\), constant in x, such that the following statements hold \(P_x\)-almost surely:

1. \(r_m(x)=\mathbf 1\{\mathbb E_{\eta^*(\cdot\mid x)}[\ell_e(x,Y)-\ell_h(x,Y)]\le c\}\).
2. \(r_j(x)=1\) implies
\[
\mathbb E_{Y\sim\widetilde\eta_\gamma(\cdot\mid x)}[\ell_e(x,Y)-\ell_h(x,Y)]\le c.
\]
