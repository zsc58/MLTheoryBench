# Problem

## Setup

Let \(V\) be a finite nonempty vocabulary, and let \((X_t)_{t\in[0,1]}\) be a time-inhomogeneous continuous-time Markov chain on \(V\), with \(X_0\sim p_0\). Its conditional kernels from time zero are column-stochastic matrices \(K_t\), with \(K_0=I\), and
\[
q_t(\cdot\mid x_0)=K_t(\cdot,x_0),\qquad q_t=K_t p_0.
\]
Assume the process is jointly measurable and the entries of \(K_t\) are measurable in \(t\). Sample \(T\sim\operatorname{Unif}[0,1]\) independently of the entire trajectory, and let \(X_T\) be its state at time \(T\). Thus, conditional on \(X_0\) and \(T\), the law of \(X_T\) is \(q_T(\cdot\mid X_0)\). Let \(S=(X_T,T)\). Let \(\Omega\) denote the full trajectory together with the sampled time, so that \(S\) is a measurable function of \(\Omega\).

Write \(\Delta(V)\) for the set of probability vectors on \(V\). For each \(\theta\) in a parameter set \(\Theta\), a snapshot predictor is a measurable map \(\mu_\theta:V\times[0,1]\to\Delta(V)\), and a path predictor is a measurable probability vector \(\rho_\theta(\Omega)\in\Delta(V)\). Define
\[
L_{\rm snap}(\theta)=\mathbb E[-\log\mu_\theta(S)_{X_0}],\qquad
L_{\rm path}(\theta)=\mathbb E[-\log\rho_\theta(\Omega)_{X_0}].
\]
These quantities may take the value \(+\infty\). All expectations are under the fixed forward process and independent sampled time.

Use natural logarithms and \(-\log0=+\infty\). For probability vectors \(r,p\), define
\[
\operatorname{KL}(r\|p)=\sum_{x:r_x>0}r_x\log\frac{r_x}{p_x},
\]
with value \(+\infty\) if \(p_x=0<r_x\) for any \(x\). For an observation \(U\), write \(r_U(x)=\mathbb P(X_0=x\mid U)\) and define
\[
H(X_0\mid U)=\mathbb E\left[-\sum_{x\in V}r_U(x)\log r_U(x)\right],
\]
where \(0\log0=0\). Conditional distributions are understood up to almost-sure equality.

## Task

Prove the following integrated theorem. There is a snapshot latent-variable model with latent space \(V\times[0,1]\), a latent law independent of \(\theta\), and conditional data distribution \(\mu_\theta(s)\) given its latent \(s\), whose data marginal \(p_\theta^{\rm snap}\) satisfies, for every \(\theta\in\Theta\),
\[
\mathbb E[\log p_\theta^{\rm snap}(X_0)]\ge -L_{\rm snap}(\theta)+C
\]
for a finite real constant \(C\) independent of \(\theta\).

Writing \(r_S(\cdot)=\mathbb P(X_0\in\cdot\mid S)\) and \(r_\Omega(\cdot)=\mathbb P(X_0\in\cdot\mid\Omega)\), prove the individual identities
\[
L_{\rm snap}=H(X_0\mid S)+\mathbb E_S\operatorname{KL}(r_S\|\mu_\theta(S)),
\]
\[
L_{\rm path}=H(X_0\mid\Omega)+\mathbb E_\Omega\operatorname{KL}(r_\Omega\|\rho_\theta(\Omega)).
\]
Whenever at least one of \(L_{\rm snap}(\theta)\) and \(L_{\rm path}(\theta)\) is finite, deduce
\[
L_{\rm snap}-L_{\rm path}
=H(X_0\mid S)-H(X_0\mid\Omega)
+\mathbb E_S\operatorname{KL}(r_S\|\mu_\theta(S))
-\mathbb E_\Omega\operatorname{KL}(r_\Omega\|\rho_\theta(\Omega)),
\]
and show \(H(X_0\mid S)-H(X_0\mid\Omega)\ge0\). Finally, whenever the snapshot predictor class can represent \(r_S\), meaning that some \(\theta_*\in\Theta\) satisfies \(\mu_{\theta_*}(S)=r_S\) almost surely, prove that every global minimizer of \(L_{\rm snap}\) over \(\Theta\) calibrates the snapshot posterior: \(\mu_\theta(S)=r_S\) almost surely.
