# Problem

## Setup

Let \(\mathcal X\) be a Borel subset of \(\mathbb R^p\). On an underlying probability space, let \(X\in\mathcal X\), \(A\in\{-1,1\}\), and let \(R(a),R^*(a)\in[0,1]\) be potential proxy and target rewards for each action \(a\). The factual proxy reward \(R\in[0,1]\) and factual latent target reward \(R^*\in[0,1]\) satisfy consistency:
\[
R=R(a),\qquad R^*=R^*(a)\quad\text{almost surely on }\{A=a\}.
\]
Assume
\[
\{R(1),R(-1),R^*(1),R^*(-1)\}\perp A\mid X.
\]
Let \(\pi(a\mid x)=\Pr(A=a\mid X=x)\) be measurable versions of the true propensities, with
\[
\pi(a\mid x)\ge\epsilon\quad\text{for every }(x,a),\qquad \epsilon\in(0,1/2].
\]

Fix a measurable function \(u:\mathcal X\times\{-1,1\}\times[0,1]\to[0,1]\), specified independently of the learning sample. Write \(U=u(X,A,R)\), and assume
\[
R^*\ge R-U\quad\text{almost surely}.
\]
Set \(R_\ell=(R-U)_+\), where \(t_+=\max\{t,0\}\). For a positive integer \(n\), the learning sample consists of the observed coordinates \(Z_i=(X_i,A_i,R_i,U_i)\) of \(n\) independent copies of \((X,A,R,U,R^*)\); the target rewards \(R_i^*\) are not observed. Write \(Z=(X,A,R,U)\) for a generic observation.

For every measurable policy \(d:\mathcal X\to\{-1,1\}\), define
\[
V^*(d)=\mathbb E[R^*(d(X))],\qquad
V_\ell(d)=\mathbb E\!\left[\frac{R_\ell\mathbf 1\{A=d(X)\}}{\pi(A\mid X)}\right].
\]
Let \(\mu_a(x)=\mathbb E[R_\ell\mid X=x,A=a]\), using measurable versions; almost-everywhere statements about \(x\) refer to the marginal law \(P_X\).

Fix a measurable policy-parameter space \((\mathcal B,\mathcal G)\) and a jointly measurable score \(f:\mathcal X\times\mathcal B\to\mathbb R\). Define \(d_\beta(x)=\operatorname{sgn}(f(x,\beta))\), with \(\operatorname{sgn}(0)=1\). Fix a measurable nuisance-parameter space \((\mathcal A,\mathcal H)\) and jointly measurable functions \(\nu_a:\mathcal X\times\mathcal A\to[0,1]\); write \(\nu_{a,\alpha}(x)=\nu_a(x,\alpha)\). Equip \(\Theta=\mathcal B\times\mathcal A\) with \(\mathcal G\otimes\mathcal H\), and let \(\Pi_0\) be a prior probability measure on this space, specified independently of the sample.

For \(a\in\{-1,1\}\), define
\[
\Gamma_a^\alpha(Z)=\nu_{a,\alpha}(X)+\frac{\mathbf 1\{A=a\}}{\pi(A\mid X)}(R_\ell-\nu_{a,\alpha}(X)),
\qquad
\Gamma_d^\alpha(Z)=\sum_{a\in\{-1,1\}}\mathbf 1\{d(X)=a\}\Gamma_a^\alpha(Z).
\]
Let
\[
D_\alpha=\Gamma_1^\alpha-\Gamma_{-1}^\alpha,\qquad
Y_\alpha=\operatorname{sgn}(D_\alpha),\qquad W_\alpha=|D_\alpha|,
\]
\[
R_{01}^\alpha(d)=\mathbb E[W_\alpha\mathbf 1\{d(X)\ne Y_\alpha\}],\qquad
C_\alpha^\sharp=\mathbb E\left[\frac{\Gamma_1^\alpha+\Gamma_{-1}^\alpha+W_\alpha}{2}\right].
\]

For \(\theta=(\beta,\alpha)\), write \(d_\theta=d_\beta\) and define the parameter-indexed empirical certified value by
\[
\widehat V_{\ell,n}(d_\theta)=\frac1n\sum_{i=1}^n\Gamma_{d_\beta}^\alpha(Z_i).
\]
For any probability measure \(Q\ll\Pi_0\), the randomized policy \(d_Q\) draws \(\theta=(\beta,\alpha)\sim Q\) and deploys \(d_\beta\), with the draw independent of a fresh population unit. Define
\[
V^*(d_Q)=\int_\Theta V^*(d_\beta)\,Q(d\theta),\qquad
\widehat V_{\ell,n}(d_Q)=\int_\Theta\widehat V_{\ell,n}(d_\theta)\,Q(d\theta).
\]
When \(Q\) is selected using the learning sample, these quantities are evaluated at its realized value; the population value does not average over the learning sample. With \(q=dQ/d\Pi_0\), use
\[
\mathrm{KL}(Q\Vert\Pi_0)=\int_\Theta q\log q\,d\Pi_0\in[0,\infty],\qquad 0\log0=0.
\]

## Task

Prove the following integrated theorem.

First, for every measurable \(d\) and every nuisance parameter \(\alpha\),
\[
V_\ell(d)=C_\alpha^\sharp-R_{01}^\alpha(d).
\]
Consequently, for each fixed \(\alpha\), maximizing certified value over measurable policies is exactly equivalent to minimizing the weighted 0-1 risk, and Bayes-optimal policies choose an action maximizing \(\mu_a(x)\) almost everywhere.

Second, for each fixed \(\delta\in(0,1)\), \(\eta>0\), and positive integer \(n\), show that with probability at least \(1-\delta\) over the learning sample, simultaneously for every probability measure \(Q\ll\Pi_0\),
\[
V^*(d_Q)\ge \widehat V_{\ell,n}(d_Q)-K_\epsilon\left[\frac{\mathrm{KL}(Q\Vert\Pi_0)+\log(1/\delta)}{\eta n}+\frac{\eta}{8}\right],
\qquad K_\epsilon=2\epsilon^{-1}-1.
\]
The right-hand side is interpreted as \(-\infty\) when the KL divergence is infinite. The probability event may depend on \(\delta,\eta,n\).

Finally, for fixed \(\eta>0\) and a realized sample, prove that the unique maximizing probability measure for
\[
Q\longmapsto \widehat V_{\ell,n}(d_Q)-\frac{K_\epsilon}{\eta n}\mathrm{KL}(Q\Vert\Pi_0),\qquad Q\ll\Pi_0,
\]
is \(\widehat Q_\eta\), with density, up to \(\Pi_0\)-null sets,
\[
\frac{d\widehat Q_\eta}{d\Pi_0}(\theta)=
\frac{\exp\{(\eta n/K_\epsilon)\widehat V_{\ell,n}(d_\theta)\}}
{\int_\Theta \exp\{(\eta n/K_\epsilon)\widehat V_{\ell,n}(d_\vartheta)\}\,\Pi_0(d\vartheta)}.
\]
Show also that this density is equivalently proportional to \(\exp\{-\eta\sum_{i=1}^n\ell_{\rm val}(\theta;Z_i)\}\), where
\[
\ell_{\rm val}(\theta;Z)=\frac{\epsilon^{-1}-\Gamma_{d_\beta}^\alpha(Z)}{2\epsilon^{-1}-1}.
\]
