# Problem

## Setup

Let \(N\ge1\) and \(m_1,\ldots,m_N\ge1\) be integers, and put \(M=\sum_{i=1}^N m_i\ge2\). For each task \(i\), let \(\Omega_i\subset\mathbb R^{d_i}\) be a convex bounded input domain. An observation space \(\mathcal X_i\) is either \(\Omega_i\) or \(\Omega_i\times\mathbb R\), with the second coordinate representing an observed response in the latter case. Let \(D_i\) be a probability distribution on \(\mathcal X_i\), let \(S_i=(X_{i,1},\ldots,X_{i,m_i})\) consist of i.i.d. draws from \(D_i\), and assume the datasets \(S_i\) are mutually independent. Write \(S=(S_1,\ldots,S_N)\).

Let \((\Theta,\mathcal T)\) be a measurable parameter space and let \(\ell_i:\Theta\times\mathcal X_i\to\mathbb R\) be jointly measurable losses satisfying
\[
\mathbb E_{X\sim D_i}|\ell_i(\theta,X)|<\infty
\qquad\text{for every }i,\theta.
\]
The notation \(\nabla_x\ell_i\) denotes the gradient with respect to the input coordinates in \(\Omega_i\). For an observation \(x=(u,y)\), it means the gradient with respect to \(u\), holding \(y\) fixed, not differentiation with respect to the response. Assume these input gradients have fixed jointly measurable representatives with values in \(\mathbb R^{d_i}\). Define
\[
R_i(\theta)=\mathbb E_{X\sim D_i}\ell_i(\theta,X),\qquad
\widehat R_i(\theta,S_i)=\frac1{m_i}\sum_{j=1}^{m_i}\ell_i(\theta,X_{i,j}).
\]

Let \(\pi\) be a probability measure on \(\Theta\), independent of all samples. A posterior \(\rho\) is a probability measure on \(\Theta\) satisfying \(\rho\ll\pi\); it may depend on the samples. Define
\[
\operatorname{gen}(\rho,S)=\mathbb E_{\theta\sim\rho}\sum_{i=1}^N\frac{m_i}{M}\bigl(R_i(\theta)-\widehat R_i(\theta,S_i)\bigr)
\]
whenever this signed integral is defined, meaning that its positive and negative parts are not both infinite. The expectation is taken of the displayed difference, without requiring the separate posterior expectations of the two risks to be finite.

For \(\lambda>0\), let
\[
\Lambda_i(\theta,\lambda)=\log\mathbb E_{X\sim D_i}
\exp\{\lambda(R_i(\theta)-\ell_i(\theta,X))\}.
\]
Assume fixed finite constants \(C_i>0\) and \(L_i>0\) satisfy, for every \(i,\theta\) and every \(\lambda>0\),
\[
\Lambda_i(\theta,\lambda)\le\frac{C_i\lambda^2}{2}\,
\mathbb E_{X\sim D_i}\|\nabla_x\ell_i(\theta,X)\|_2^2,
\qquad
\|\nabla_x\ell_i(\theta,x)\|_2^2\le L_i\quad\text{for all }x\in\mathcal X_i.
\]
For \(p=d\rho/d\pi\), use
\[
\mathrm{KL}(\rho\|\pi)=\int p\log p\,d\pi\in[0,\infty],
\]
with \(0\log0=0\). Define
\[
\widehat G(\rho,S)=\sum_{i=1}^N C_i\,\mathbb E_{\theta\sim\rho}\sum_{j=1}^{m_i}\|\nabla_x\ell_i(\theta,X_{i,j})\|_2^2,
\]
\[
K(\rho,\pi,\delta)=\frac{M}{M-1}\left(\mathrm{KL}(\rho\|\pi)+\log\frac{2M}{\delta}\right),
\qquad
L=\sqrt{2\sum_{i=1}^N m_iC_i^2L_i^2}.
\]
All logarithms are natural. When \(\mathrm{KL}(\rho\|\pi)=\infty\), the right-hand side of the inequality below is interpreted as \(+\infty\).

## Task

Prove that for every \(\delta\in(0,1)\), with probability at least \(1-\delta\) over the independent samples, simultaneously for every posterior \(\rho\ll\pi\) for which \(\operatorname{gen}(\rho,S)\) is defined,
\[
\operatorname{gen}(\rho,S)\le\frac1M\sqrt{2\,\widehat G(\rho,S)\,K(\rho,\pi,\delta)+L\,K(\rho,\pi,\delta)^{3/2}}.
\]
