# Problem

## Setup

Let \(d,M\) be positive integers, let \(\sigma>0\) and \(\lambda>0\), and let \(\mu\) be a finite nonnegative Borel measure on \(\mathbb R^d\). Define the squared-exponential kernel
\[
k(x,y)=\exp\!\left(-\frac{\|x-y\|^2}{2\sigma^2}\right).
\]
For finite signed Borel measures \(\alpha,\beta\) of finite total variation on \(\mathbb R^d\), define
\[
\operatorname{MMD}_k^2(\alpha,\beta)
=\iint k(x,x')\,d\alpha(x)d\alpha(x')-2\iint k(x,y)\,d\alpha(x)d\beta(y)+\iint k(y,y')\,d\beta(y)d\beta(y').
\]
For a particle configuration \(Z=(z_1,\ldots,z_M)^T\in(\mathbb R^d)^M\), set \(K_{ij}=k(z_i,z_j)\),
\[
(m_0)_i=\int k(x,z_i)\,d\mu(x),\qquad (m_1)_i=\int x\,k(x,z_i)\,d\mu(x),
\]
where the rows of \(m_1\) are vectors in \(\mathbb R^d\). For weights \(a\in\mathbb R^M\), let \(q_{a,Z}=\sum_{i=1}^M a_i\delta_{z_i}\), and define
\[
\mathcal E_\mu(a,Z)=\tfrac12\operatorname{MMD}_k^2(\mu,q_{a,Z}),
\qquad
\mathcal E_{\mu,\lambda}(a,Z)=\mathcal E_\mu(a,Z)+\tfrac\lambda2\|a\|^2,
\]
with reduced objective \(\mathcal E_{\mu,\lambda}^{\rm red}(Z)=\inf_{a\in\mathbb R^M}\mathcal E_{\mu,\lambda}(a,Z)\). Put
\[
G_\lambda(Z)=K(Z)+\lambda I_M,\quad a_\lambda(Z)=G_\lambda(Z)^{-1}m_0(Z),\quad D_\lambda(Z)=\operatorname{diag}(a_\lambda(Z)),
\]
and, whenever all entries of \(a_\lambda(Z)\) are nonzero, define
\[
\Phi_{\mu,\lambda}(Z)=D_\lambda(Z)^{-1}G_\lambda(Z)^{-1}m_1(Z),\qquad
P_\lambda(Z)=\sigma^{-2}D_\lambda(Z)G_\lambda(Z)D_\lambda(Z).
\]

## Task

Prove the following integrated theorem. For every configuration \(Z\),
\[
\nabla_Z\mathcal E_{\mu,\lambda}^{\rm red}(Z)=\sigma^{-2}D_\lambda(Z)\bigl(G_\lambda(Z)D_\lambda(Z)Z-m_1(Z)\bigr).
\]
Consequently, on the domain where the diagonal entries of \(D_\lambda(Z)\) are nonzero, the update
\[
Z^+=Z-\eta P_\lambda(Z)^{-1}\nabla_Z\mathcal E_{\mu,\lambda}^{\rm red}(Z)
=(1-\eta)Z+\eta\Phi_{\mu,\lambda}(Z)
\]
is preconditioned gradient descent for every step size \(\eta>0\). Moreover, for every \(C>0\), if \(\mu_C=C\mu\), then on the common domain of definition,
\[
\Phi_{\mu_C,\lambda}(Z)=\Phi_{\mu,\lambda}(Z).
\]
