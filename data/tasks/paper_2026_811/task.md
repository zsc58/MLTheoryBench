# Problem

## Setup

Let \(d,N\) be positive integers with \(\lambda=d/N<1\), and let \(e_1\in\mathbb R^d\) be a fixed unit signal direction. Fix a signal magnitude \(\mu_f\ge0\), a signal-noise amplitude \(\sigma_f\ge0\), and a reference orthogonal-noise amplitude \(\sigma_n>0\).

Let \(y\in\{-1,+1\}\) have a fixed probability law. Independently of \(y\), let
\[
\xi_f\sim\mathcal N(0,1),\qquad
\xi_\perp\sim\mathcal N(0,I_d-e_1e_1^\top)
\]
be independent, where \(I_d\) is the identity matrix. Thus \(\xi_\perp\perp e_1\) almost surely. For each amplitude \(t>0\), define a test feature vector by
\[
x(t)=y\mu_f e_1+\sigma_f\xi_f e_1+t\xi_\perp.
\]

Take \(N\) independent copies \((y_i,\xi_{f,i},\xi_{\perp,i})\) of these base variables for training, and define
\[
x_i(t)=y_i\mu_f e_1+\sigma_f\xi_{f,i}e_1+t\xi_{\perp,i},
\qquad i=1,\ldots,N.
\]
When comparing amplitudes, use the same realized training labels and base noise variables. The test draw is independent of the entire training sample.

Fix \(0<\alpha<1\) and a convex even function \(f:\mathbb R\to\mathbb R\), neither depending on \(t\). For weights \(S\in\mathbb R^d\), use signed inputs \(\widetilde x_i(t)=y_i x_i(t)\), logits \(z_i^{(t)}(S)=S^\top\widetilde x_i(t)\), and empirical objective
\[
L_t(S)=\frac1N\sum_{i=1}^N
\left[(1-\alpha)\log(1+e^{-z_i^{(t)}(S)})+\alpha f(z_i^{(t)}(S))\right].
\]
Let
\[
\mathcal M_t=\operatorname*{argmin}_{S\in\mathbb R^d}L_t(S).
\]
Work with any fixed realization of the base training sample for which \(\mathcal M_{\sigma_n}\ne\varnothing\).

For a fixed weight vector define
\[
A_t(S)=\Pr\{yS^\top x(t)\ge0\},
\]
where probability is over the independent test draw only, with the realized training sample held fixed. Whenever \(\mathcal M_t\ne\varnothing\), define optimal generalization accuracy by
\[
\operatorname{Acc}^*(t)=\sup_{S\in\mathcal M_t}A_t(S).
\]

## Task

Prove that for every \(\beta>0\), the set \(\mathcal M_{\beta\sigma_n}\) is nonempty and
\[
\operatorname{Acc}^*(\beta\sigma_n)=\operatorname{Acc}^*(\sigma_n).
\]
Thus optimal generalization accuracy is independent of the positive orthogonal-noise amplitude, with all other parameters and base laws fixed.
