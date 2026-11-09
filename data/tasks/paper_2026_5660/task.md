# Problem

## Setup

Let \(x_0\ge 0\). Let \(\phi:[x_0,\infty)\to[0,\infty)\) be a known strictly increasing bijection with \(\phi(x_0)=0\) and \(\phi(x)\to\infty\), and let \(\psi=\phi^{-1}:[0,\infty)\to[x_0,\infty)\). For each rate \(\lambda>0\), define the distribution function
\[
F_\lambda(x)=\begin{cases}
0,&x<x_0,\\
1-e^{-\lambda\phi(x)},&x\ge x_0.
\end{cases}
\]
Let \(X_1,X_2,\ldots\) be independent identically distributed rewards with law \(F_\theta\), where the true parameter \(\theta>0\) is fixed and unknown.

For a horizon \(n\), an admissible stopping time \(\sigma\) takes values in \(\{1,\ldots,n+1\}\) and is adapted to the natural filtration of the sequentially observed rewards. Stopping at \(i\le n\) receives \(X_i\); choosing \(n+1\) receives zero. Define
\[
\mathrm{OPT}_n(\theta)=\mathbb E_\theta\!\left[\max_{1\le i\le n}X_i\right],\qquad
\mathrm{CR}_n(\sigma;\theta)=\frac{\mathbb E_\theta[X_\sigma\mathbf 1\{\sigma\le n\}]}{\mathrm{OPT}_n(\theta)}.
\]
Let \(\tau^*\) denote an optimal admissible stopping rule when \(\theta\) is known.

Assume that \(\psi\) is twice differentiable for all sufficiently large arguments, with \(\psi'(y)>0\) there, and that for some \(c,c'\in[0,\theta)\),
\[
\frac{\psi'(y)}{\psi(y)}\longrightarrow c,\qquad
\frac{\psi''(y)}{\psi'(y)}\longrightarrow c'
\qquad(y\to\infty).
\]

For \(\eta>0\) and finite \(a\ge x_0\), define
\[
r_\eta(a)=\int_a^\infty e^{-\eta\phi(t)}\,dt,
\qquad r_\eta(+\infty)=0.
\]
For each positive integer horizon \(h\), define
\[
V_{h+1}(\eta;h)=0,\qquad V_h(\eta;h)=\mathbb E_\eta[X_1],
\]
\[
V_i(\eta;h)=V_{i+1}(\eta;h)+r_\eta\bigl(V_{i+1}(\eta;h)\bigr),
\qquad i=h-1,\ldots,1.
\]
These nonnegative expectations, integrals, and values are allowed to equal \(+\infty\). An infinite threshold is never crossed by a finite reward.

Fix \(\delta\in(0,1)\). For \(n\ge2\), let \(m=m(n)\) be a deterministic integer with \(1\le m<n\), and put \(N=n-m\). The learning policy knows \(\phi,x_0,n,m,\delta\), but not \(\theta\), and has no samples other than the sequential rewards. It observes and rejects the first \(m\) rewards and defines, almost surely,
\[
\widehat\theta_m=\left(\frac1m\sum_{i=1}^m\phi(X_i)\right)^{-1},\qquad
\varepsilon_m=\sqrt{\frac{4\log(2/\delta)}m},\qquad
\eta=(1+\varepsilon_m)\widehat\theta_m.
\]
It then stops at the first post-exploration stage \(j\in\{1,\ldots,N-1\}\) for which
\[
X_{m+j}\ge V_{j+1}(\eta;N),
\]
and accepts \(X_n\) if it has not stopped earlier. Denote its stopping time by \(\tau\). Assume
\[
m=o(n),\qquad m=\omega\!\left(\log^2 n\,\log(1/\delta)\right).
\]

## Task

Prove that
\[
\mathrm{CR}_n(\tau^*;\theta)\longrightarrow
\rho(c,\theta):=
\frac{\left(\theta/(\theta-c)\right)^{c/\theta}}{\Gamma(1-c/\theta)},
\]
and that the learning policy satisfies
\[
\liminf_{n\to\infty}\mathrm{CR}_n(\tau;\theta)
\ge(1-\delta)\rho(c,\theta).
\]
Here \(\Gamma\) denotes the gamma function. Both limits are for the fixed family, fixed true parameter, and fixed confidence level specified above.
