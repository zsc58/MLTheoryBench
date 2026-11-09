# Problem

## Setup

Let \(d\) be a positive integer and let \(0\leq T<\infty\). Work on \(\mathbb R^d\). Let \(A\in\mathbb R^{d\times d}\) be symmetric positive definite, \(V\in\mathbb R^{d\times d}\) symmetric, and let \(\alpha:(0,T]\to[0,\infty)\) be a damping function. No value of \(\alpha\) at zero is required.

For smooth positive probability densities and smooth potentials for which the integral exists absolutely, define the operator denoted by \(G_\rho^{-1}\) by
\[
(G_\rho^{-1}[\Phi])(x)=-\nabla\!\cdot\!\left(\rho(x)\int_{\mathbb R^d} y^\top A x\,\nabla\Phi(y)\rho(y)\,dy\right).
\]
The energy, on probability densities with finite second moment, is
\[
F(\rho)=-\frac12\int_{\mathbb R^d} y^\top Vy\,\rho(y)\,dy,
\]
with first-variation representative \(-\tfrac12x^\top Vx\).

Here \(\mathcal E(m,\Sigma,g)\) denotes the elliptically contoured probability density
\[
\mathcal E(m,\Sigma,g)(x)=\det(\Sigma)^{-1/2}g\!\left((x-m)^\top\Sigma^{-1}(x-m)\right),
\]
where \(m\in\mathbb R^d\), \(\Sigma\succ0\) is symmetric, and \(g:[0,\infty)\to(0,\infty)\) is smooth and satisfies
\[
\int_{\mathbb R^d}g(\|z\|^2)\,dz=1,
\qquad
\int_{\mathbb R^d}\|z\|^2g(\|z\|^2)\,dz<\infty.
\]
Define \(\kappa_g>0\) by
\[
\int_{\mathbb R^d}zz^\top g(\|z\|^2)\,dz=\kappa_g I_d.
\]

Fix \(m_0\in\mathbb R^d\) and symmetric \(\Sigma_0\succ0\). Consider a solution \((\rho_t,\Phi_t)_{0\leq t\leq T}\), with \(\rho_t\) a smooth strictly positive probability density. Assume that \(\rho\) and \(\Phi\) are continuous on \([0,T]\times\mathbb R^d\), smooth in space, and continuously differentiable in time for \(t>0\). The vector-valued integral displayed in the first equation below is assumed absolutely convergent and continuous in \((t,x)\) on \([0,T]\times\mathbb R^d\). For \(0<t\leq T\), the equations hold pointwise:
\[
\partial_t\rho_t(x)+\nabla\!\cdot\!\left(\rho_t(x)\int_{\mathbb R^d} y^\top A x\,\nabla\Phi_t(y)\rho_t(y)\,dy\right)=0,
\]
\[
\partial_t\Phi_t(x)+\alpha_t\Phi_t(x)+\int_{\mathbb R^d}\langle\nabla\Phi_t(x),\nabla\Phi_t(y)\rangle\,y^\top A x\,\rho_t(y)\,dy-\frac12x^\top Vx=0.
\]
The initial values are
\[
\rho_0=\mathcal E(m_0,\Sigma_0,g),\qquad \Phi_0\equiv0.
\]

## Task

Prove that there exist continuous parameter curves \(m_t\in\mathbb R^d\), symmetric \(\Sigma_t\succ0\), symmetric \(P_t\), and matrices \(C_t\), with \(m_t,\Sigma_t,P_t\) differentiable for \(t>0\), such that for every \(t\in[0,T]\),
\[
\rho_t=\mathcal E(m_t,\Sigma_t,g),\qquad \Phi_t(x)=\frac12x^\top P_tx.
\]
Moreover, the parameters satisfy
\[
\dot m_t=C_tm_t,\qquad
\dot\Sigma_t=C_t\Sigma_t+\Sigma_tC_t^\top,
\]
\[
C_t=P_t(\kappa_g\Sigma_t+m_tm_t^\top)A,
\qquad
\dot P_t=-\alpha_tP_t-(C_t^\top P_t+P_tC_t)+V.
\]
The differential equations are required for \(0<t\leq T\), the formula for \(C_t\) holds throughout \([0,T]\), and the initial values are the prescribed \(m_0,\Sigma_0\) and \(P_0=0\).
