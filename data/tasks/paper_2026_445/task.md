# Problem

## Setup

Let the parameter space be \(\mathbb R^{d_\theta}\) and the state space be \(\mathbb R^{d_x}\), with Euclidean norms. For each parameter \(\theta\), let \(V_\theta:\mathbb R^{d_x}\to\mathbb R\) be measurable and define
\[
\rho_\theta(x)=e^{-V_\theta(x)},\qquad
Z_\theta=\int_{\mathbb R^{d_x}}\rho_\theta(x)\,dx,
\qquad
p_\theta(x)=\frac{\rho_\theta(x)}{Z_\theta}.
\]
Assume \(Z_\theta<\infty\) for every \(\theta\). Let \(F:\mathbb R^{d_\theta}\to\mathbb R\) be differentiable. For every \(\theta\), suppose \(h_\theta:\mathbb R^{d_x}\to\mathbb R^{d_\theta}\) is measurable,
\[
\mathbb E_{X\sim p_\theta}[\|h_\theta(X)\|]<\infty,
\qquad
\nabla F(\theta)=\mathbb E_{X\sim p_\theta}[h_\theta(X)].
\]

Fix \(\theta_0\), a constant step size \(\eta>0\), forward Markov transition densities \(M_k(x,y)\), and backward Markov transition densities \(B_{k-1}(y,x)\). Each is measurable and nonnegative, with
\[
\int M_k(x,y)\,dy=1\quad\text{for every }x,
\qquad
\int B_{k-1}(y,x)\,dx=1\quad\text{for every }y.
\]
The kernels are arbitrary subject to the following support condition: for every \(k\ge1\),
\[
B_{k-1}(y,x)=0
\quad\text{for Lebesgue-almost every }(x,y)
\text{ such that }M_k(x,y)=0.
\]

Consider the following idealized recursion. Initialize
\[
X_0\sim p_{\theta_0},\qquad \omega_0=1.
\]
For \(k\ge1\), set
\[
\theta_k=\theta_{k-1}-\eta\,
\frac{\mathbb E[h_{\theta_{k-1}}(X_{k-1})\omega_{k-1}]}
{\mathbb E[\omega_{k-1}]},
\]
then draw \(X_k\mid X_{0:k-1}\sim M_k(X_{k-1},\cdot)\) and define
\[
\omega_k=\omega_{k-1}
\frac{\rho_{\theta_k}(X_k)B_{k-1}(X_k,X_{k-1})}
{\rho_{\theta_{k-1}}(X_{k-1})M_k(X_{k-1},X_k)}.
\]
All expectations are unconditional expectations with respect to the forward path law generated from \(X_0\) and the transitions \(M_1,M_2,\ldots\). Weight ratios are evaluated almost surely under this law; their values on forward-null sets may be assigned arbitrarily.

Assume that for some \(\mu,L>0\), for all \(\theta,\theta'\),
\[
F(\theta)-\inf_uF(u)
\le\frac{\|\nabla F(\theta)\|^2}{2\mu},
\qquad
\|\nabla F(\theta)-\nabla F(\theta')\|
\le L\|\theta-\theta'\|.
\]

## Task

Prove that if \(0<\eta\le1/L\), then for every integer \(k\ge0\),
\[
F(\theta_k)-\inf_\theta F(\theta)
\le(1-\eta\mu)^k
\left(F(\theta_0)-\inf_\theta F(\theta)\right).
\]
The zeroth power is interpreted as one.
