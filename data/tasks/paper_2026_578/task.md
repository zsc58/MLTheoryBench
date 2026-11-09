# Problem

## Setup

Let \(\mathcal V\) be a token vocabulary containing a distinguished outcome token \(\omega\). Conditional on a fixed initial context, a model samples a finite random timeline sequentially from next-token conditional probabilities. For notation, extend each completed timeline by a fixed symbol \(\dagger\notin\mathcal V\), and write the resulting sequence as \(Z=(Z_1,Z_2,\ldots)\). Let \(\mathcal F_t=\sigma(Z_1,\ldots,Z_t)\), with \(\mathcal F_0\) trivial.

Let \(\tau_\omega\) be the first index at which \(\omega\) appears, or \(\infty\) if it never appears. Let \(\tau_E\) be the endpoint or window-exceeding index. It is a positive, almost surely finite stopping time: \(\{\tau_E\le t\}\in\mathcal F_t\) for every integer \(t\ge0\). Assume \(\tau_E\ne\tau_\omega\) almost surely. When the outcome occurs before the endpoint, use the convention \(\tau_E=\tau_\omega+1\).

Define
\[
\mu=\Pr(\tau_\omega<\tau_E),\qquad K=\min(\tau_\omega,\tau_E),\qquad
r_t=\Pr(Z_t=\omega\mid\mathcal F_{t-1}).
\]
For \(n\) iid timelines generated under the same model and stopping rule, define
\[
U_i=\sum_{t=1}^{K_i}r_{i,t},\qquad
\widehat\mu_{\rm SCOPE}=\frac1n\sum_{i=1}^n U_i,
\]
where the upper limit is inclusive. Assume \(\mathbb E[U_1^2]<\infty\). Define the ordinary Monte Carlo estimator
\[
\widehat\mu_{\rm MC}=\frac1n\sum_{i=1}^n\mathbf 1\{\tau_{\omega,i}<\tau_{E,i}\}.
\]

## Task

Prove the following integrated theorem for every integer sample size \(n\ge1\):

1. \(\widehat\mu_{\rm SCOPE}\) is unbiased for \(\mu\).
2. The exact variance comparison is
\[
\operatorname{Var}(\widehat\mu_{\rm SCOPE})-\operatorname{Var}(\widehat\mu_{\rm MC})
=\frac{\mathbb E[U_1(U_1-1)]}{n},
\]
so SCOPE has strictly smaller variance exactly when \(\mathbb E[U_1(U_1-1)]<0\).
3. Over the class of all models in this setup, allowing the vocabulary and stopping rule to vary, there is no constant \(M>0\) such that every model with \(0<\mu<M\) necessarily satisfies \(\operatorname{Var}(\widehat\mu_{\rm SCOPE})<\operatorname{Var}(\widehat\mu_{\rm MC})\).
