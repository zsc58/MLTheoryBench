# Problem

## Setup

There are \(n\ge1\) agents, with \(x\in\mathbb R^{d_x}\) and \(y,\theta\in\mathbb R^{d_y}\). Agent \(i\) has continuously differentiable functions \(f_i(x,y)\) and \(g_i(x,y)\), and
\[
F(x,y)=\frac1n\sum_{i=1}^n f_i(x,y),\qquad G(x,y)=\frac1n\sum_{i=1}^n g_i(x,y).
\]
Assume \(F\ge F_*\), with \(F_*\) finite. The full gradients of \(f_i\) and \(g_i\) are globally Lipschitz in the joint variables, with positive constants \(L_1\) and \(L_2\), respectively. No gradient-heterogeneity or local-to-global dissimilarity bound is assumed.

At iteration \(k\), each agent draws an upper-level sample \(\xi_{f,i}^k\) and a lower-level sample \(\xi_{g,i}^k\). Conditional on the history before these samples are drawn, they are fresh and independent across agents; upper- and lower-level samples are independent. At every queried point, the corresponding stochastic full gradients are conditionally unbiased and have conditional mean-square errors at most \(\delta_f^2\) and \(\delta_g^2\), respectively. The same local sample is reused for the several evaluations explicitly carrying its label below. No Lipschitz condition on individual sample-gradient maps is assumed.

Let \(W=(w_{ij})\) be nonnegative, symmetric, and doubly stochastic, with
\[
\left\|W-\frac1n\mathbf1\mathbf1^\top\right\|_2=\rho<1.
\]
Fix \(\gamma\in(0,1/(2L_2))\), and define
\[
V_\gamma(x,y)=\min_\theta\left\{G(x,\theta)+\frac1{2\gamma}\|\theta-y\|^2\right\},\qquad
\Psi_\mu(x,y)=\mu F(x,y)+G(x,y)-V_\gamma(x,y).
\]
Let \(\theta_\gamma^*(x,y)\) denote the unique minimizer. Take \(\mu_0>0\) and
\[
\mu_k=\mu_0(k+1)^{-p},\qquad 0<p<1/4.
\]

Start from arbitrary fixed finite local variables \((x_i^0,y_i^0,\theta_i^0)\). At their iteration-\(k\) values define the exact directions
\[
D_{\theta,i}^k=\nabla_y g_i(x_i^k,\theta_i^k)+\gamma^{-1}(\theta_i^k-y_i^k),
\]
\[
D_{x,i}^k=\mu_k\nabla_x f_i(x_i^k,y_i^k)+\nabla_x g_i(x_i^k,y_i^k)-\nabla_x g_i(x_i^k,\theta_i^k),
\]
\[
D_{y,i}^k=\mu_k\nabla_y f_i(x_i^k,y_i^k)+\nabla_y g_i(x_i^k,y_i^k)-\gamma^{-1}(y_i^k-\theta_i^k).
\]
Their stochastic versions are
\[
\widehat D_{\theta,i}^k=\nabla_y g_i(x_i^k,\theta_i^k;\xi_{g,i}^k)+\gamma^{-1}(\theta_i^k-y_i^k),
\]
\[
\widehat D_{x,i}^k=\mu_k\nabla_x f_i(x_i^k,y_i^k;\xi_{f,i}^k)+\nabla_x g_i(x_i^k,y_i^k;\xi_{g,i}^k)-\nabla_x g_i(x_i^k,\theta_i^k;\xi_{g,i}^k),
\]
\[
\widehat D_{y,i}^k=\mu_k\nabla_y f_i(x_i^k,y_i^k;\xi_{f,i}^k)+\nabla_y g_i(x_i^k,y_i^k;\xi_{g,i}^k)-\gamma^{-1}(y_i^k-\theta_i^k).
\]
Write \(\widehat D_i^k\) and \(S_i^k\) for the corresponding three-component vectors. Compute the initial stochastic directions and set
\[
S_i^0=\sum_jw_{ij}\widehat D_j^0.
\]
For \(k=0,\ldots,K-1\), first update the variables using the already available tracker:
\[
(x_i^{k+1},y_i^{k+1},\theta_i^{k+1})
=\sum_jw_{ij}\bigl(x_j^k-\lambda_xS_{x,j}^k,\ y_j^k-\lambda_yS_{y,j}^k,\ \theta_j^k-\lambda_\theta S_{\theta,j}^k\bigr).
\]
If another iteration is to be performed, sample at the new variables, compute \(\widehat D^{k+1}\), and set
\[
S_i^{k+1}=\sum_jw_{ij}\bigl(S_j^k+\widehat D_j^{k+1}-\widehat D_j^k\bigr).
\]
The old stochastic direction in this difference is the stored value, not a new evaluation.

For averages \(\bar z^k=n^{-1}\sum_i z_i^k\), define
\[
\Delta^k=\frac1n\sum_i\mathbb E\bigl[\|x_i^k-\bar x^k\|^2+\|y_i^k-\bar y^k\|^2+\|\theta_i^k-\bar\theta^k\|^2\bigr].
\]

## Task

Prove that there are positive constants \(a,b\), depending only on \(L_1,L_2,\gamma,\mu_0\), such that the following holds. Fix positive step prefactors \(c_\theta,c_\lambda\) with \(c_\lambda\le a\). For every positive integer horizon \(K\) satisfying
\[
c_\theta\sqrt{n/K}\le b(1-\rho)^4,
\]
choose constant steps
\[
\lambda_\theta=c_\theta\sqrt{n/K},\qquad \lambda_x=\lambda_y=c_\lambda\lambda_\theta.
\]
Then
\[
\frac1K\sum_{k=0}^{K-1}\mathbb E\|\nabla\Psi_{\mu_k}(\bar x^k,\bar y^k)\|^2
=O\!\left(\frac1{\sqrt{nK}}+\frac{n(\delta_f^2+\delta_g^2)}{(1-\rho)^4K}\right),
\]
and
\[
\frac1K\sum_{k=0}^{K-1}\Delta^k
=O\!\left(\frac1{\sqrt K}+\frac{n^{3/2}(\delta_f^2+\delta_g^2)}{(1-\rho)^4K}\right).
\]
The hidden constants are independent of \(n,K\), and \(1-\rho\). They may depend on the smoothness parameters, \(\gamma\), \(\mu_0\), the fixed step prefactors, oracle variances, and finite initialization quantities such as initial objective gaps, mean-square starting-variable values, and initial tracker second moments. When comparing a family of agent counts or networks, this initialization dependence is held uniformly bounded.

In particular, the leading stationarity term has asymptotic linear speedup in the number of agents when it dominates the lower-order term, and the result requires no gradient-heterogeneity assumption.
