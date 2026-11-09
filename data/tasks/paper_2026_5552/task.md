# Problem

## Setup

Let \(T\geq 1\) and \(d\geq 1\) be integers. Let \((\mathcal Z,d_{\mathcal Z})\) be a nonempty metric data space and let \(\mathcal X\subset\mathbb R^d\) be nonempty, convex, and compact. All norms on the parameter space are Euclidean. All probability measures below are Borel probability measures. Write \(\mathcal P_1(\mathcal Z)\) for the probability measures with finite first moment, meaning \(\int d_{\mathcal Z}(z,z_0)\,\nu(dz)<\infty\) for one, equivalently every, \(z_0\in\mathcal Z\). Let \(W_1\) denote Wasserstein-1 distance for the ground metric \(d_{\mathcal Z}\).

Fix finite constants \(\mu>0\) and \(\epsilon,\beta,L\geq 0\). Fix a sequence of coefficients \(\rho_t\in[0,1]\) and exogenous probability distributions \(Q_t\) on \(\mathcal Z\), for \(t=1,\ldots,T\); these distributions do not depend on the deployed model. Let \(\mathsf M:\mathcal X\to\mathcal P_1(\mathcal Z)\) be an endogenous distribution map and define
\[
\mathsf P_t(x)=(1-\rho_t)\mathsf M(x)+\rho_t Q_t.
\]
Assume \(\mathsf M\) is \(\epsilon\)-sensitive:
\[
W_1(\mathsf M(x),\mathsf M(y))\leq\epsilon\|x-y\|\qquad(x,y\in\mathcal X).
\]

Let \(\ell:\mathcal Z\times\mathcal X\to\mathbb R\) be continuously differentiable in its second argument, with \(z\mapsto\ell(z,x)\) Borel measurable for each \(x\). For every \(z\), assume \(\ell(z,\cdot)\) is \(\mu\)-strongly convex, with the convention
\[
\ell(z,y)\geq\ell(z,x)+\langle\nabla_x\ell(z,x),y-x\rangle+\frac{\mu}{2}\|y-x\|^2
\qquad(x,y\in\mathcal X).
\]
Assume also
\[
\|\nabla_x\ell(z,x)-\nabla_x\ell(z',x)\|
\leq\beta d_{\mathcal Z}(z,z')
\qquad(x\in\mathcal X,\ z,z'\in\mathcal Z).
\]
The expected risks below are finite real-valued integrals: explicitly, assume
\[
\int |\ell(z,x)|\,\mathsf P_t(y)(dz)<\infty
\qquad(t=1,\ldots,T,\ x,y\in\mathcal X).
\]
Define
\[
R_t(x)=\mathbb E_{Z\sim\mathsf P_t(x)}[\ell(Z,x)],
\qquad
\bar R_t(x,y)=\mathbb E_{Z\sim\mathsf P_t(y)}[\ell(Z,x)].
\]
Assume each \(\bar R_t(\cdot,y)\) attains its minimum on \(\mathcal X\), and that the deployed risk is uniformly \(L\)-Lipschitz:
\[
|R_t(x)-R_t(y)|\leq L\|x-y\|
\qquad(x,y\in\mathcal X,\ t=1,\ldots,T).
\]

Let \(s_t\in\arg\min_{x\in\mathcal X}\bar R_t(x,s_t)\) be the performatively stable comparator. Initialize at any fixed \(x_1\in\mathcal X\) and, for \(t=1,\ldots,T-1\), update by exact population risk minimization,
\[
x_{t+1}\in\arg\min_{x\in\mathcal X}\bar R_t(x,x_t).
\]
Set
\[
\rho_{\min}=\min_{1\leq t\leq T}\rho_t,
\qquad
\gamma=\frac{(1-\rho_{\min})\epsilon\beta}{\mu},
\]
and assume \(\gamma<1\). For \(1\leq t<T\), define \(\delta_t=\|s_{t+1}-s_t\|\). Define
\[
\operatorname{Reg}^{\mathrm{stab}}_T
=\sum_{t=1}^{T}\left(\mathbb E[R_t(x_t)]-R_t(s_t)\right),
\]
where the expectation is over algorithmic randomness and is redundant for the deterministic population update with fixed initialization. Empty sums are zero.

## Task

Prove that
\[
\operatorname{Reg}^{\mathrm{stab}}_T
\leq
\frac{L}{1-\gamma}
\left(\|x_1-s_1\|+\sum_{t=1}^{T-1}\delta_t\right).
\]
