# Problem

## Setup

Let \(d\) be a positive integer and \(0\leq\gamma<1\). Let \(\mathcal X\) be a measurable state space, let \(\pi\) be a probability measure on it, and let \(P(x,dr,dx')\) be a probability kernel from \(\mathcal X\) to \(\mathbb R\times\mathcal X\). Its state-transition marginal has invariant distribution \(\pi\). A sample \((X,X',R)\) is obtained by drawing \(X\sim\pi\) and then \((R,X')\) from \(P(X,\cdot)\). At successive iterations, independent identically distributed copies \((X_j,X'_j,R_j)\) are observed. Assume
\[
 \sup_{x\in\mathcal X}\int r^2\,P(x,dr,dx')<\infty.
\]

Let \(\phi:\mathcal X\to\mathbb R^d\) be measurable, satisfy \(\|\phi(x)\|\leq1\), and have coordinates that are linearly independent in \(L^2(\pi)\). Here \(\|\cdot\|\) denotes the Euclidean norm, \(\|\cdot\|_{\rm op}\) its induced matrix norm, and
\[
 \|f\|_\pi^2=\int_{\mathcal X}|f(x)|^2\,\pi(dx).
\]
Define
\[
 \Sigma=\mathbb E[\phi(X)\phi(X)^\top],\qquad
 C=\mathbb E[\phi(X)\phi(X')^\top],\qquad
 \omega=\lambda_{\min}(\Sigma).
\]
Assume
\[
 \|\Sigma^{-1/2}C\Sigma^{-1/2}\|_{\rm op}\leq1.
\]
Let \(\theta^*\in\mathbb R^d\) be the unique solution of
\[
 (\Sigma-\gamma C)\theta^*=\mathbb E[R\phi(X)].
\]
Let \(0\leq\sigma<\infty\) satisfy, almost surely in \(X\),
\[
 \mathbb E\left[\left(R+\gamma\phi(X')^\top\theta^*-\phi(X)^\top\theta^*\right)^2\middle|X\right]\leq\sigma^2.
\]

Starting from deterministic \(\theta_0\in\mathbb R^d\), use a constant step size \(\alpha\) within each run and define
\[
 \theta_j=\theta_{j-1}+\alpha\phi(X_j)
 \left(R_j+\gamma\phi(X'_j)^\top\theta_{j-1}-\phi(X_j)^\top\theta_{j-1}\right),\qquad
 \bar\theta_k=\frac1k\sum_{j=0}^{k-1}\theta_j.
\]
Write \(V_\theta(x)=\phi(x)^\top\theta\). Expectations of errors of these iterates are over the observed samples; the norm \(\|\cdot\|_\pi\) integrates the state variable. Set
\[
 a_0=\frac{2(1-\gamma)}{(1+\gamma)^2},\qquad
 a_1=\frac{2}{1+\gamma},
\]
\[
 \varepsilon_{k,\gamma}=
 \frac{4}{k(1-\gamma)}+3(1-\gamma)+\frac{10}{k}
 +\frac{1}{k\left(1-(1+\gamma)\alpha/2\right)}.
\]
The constant \(e\) denotes \(\exp(1)\).

## Task

Prove the following integrated claim.

For every \(0<\alpha<a_0\) and every integer \(k\geq1\),
\[
 \mathbb E\|V_{\bar\theta_k}-V_{\theta^*}\|_\pi^2
 \leq \frac{1}{(1-\gamma)^2k}
 \left(
 \sqrt{\frac{\|\theta_0-\theta^*\|^2}
 {2(1-\alpha/a_1)\alpha/(1-\gamma)}}
 +\sqrt{\frac{de\,\sigma^2(1+\varepsilon_{k,\gamma})}{1-\alpha/a_0}}
 \right)^2. \tag{1}
\]
In particular, the displayed bound has no explicit dependence on \(\omega\).

This rate is sharp up to a factor of \(11\). More precisely, for every positive integer \(d\), every \(0<\omega\leq1/d\), every \(\sigma>0\), and every deterministic \(\theta_0\in\mathbb R^d\), there is an instance whose sample law and feature map are fixed as \(\gamma\) varies, satisfying the setup for every \(0\leq\gamma<1\) with \(\Sigma=\omega I_d\), such that the following holds. For each fixed \(\lambda\in(0,1/2]\), set \(\alpha=\lambda a_0\). Along every joint limit
\[
 k\to\infty,\qquad \gamma\uparrow1,\qquad
 k(1-\gamma)\alpha\omega\to5.5,
\]
with \(d,\omega,\sigma,\theta_0,\lambda\) held fixed,
\[
 \liminf
 \frac{\mathbb E\|V_{\bar\theta_k}-V_{\theta^*}\|_\pi^2}{E_{k,\gamma}}
 \geq\frac1{11},
\]
where \(\theta^*\) is evaluated at the current value of \(\gamma\), and
\[
 E_{k,\gamma}=
 \left(
 \sqrt{\frac{\|\theta_0-\theta^*\|^2}{2\alpha(1-\gamma)k}}
 +\sqrt{\frac{ed\,\sigma^2}{(1-\lambda)(1-\gamma)^2k}}
 \right)^2.
\]
