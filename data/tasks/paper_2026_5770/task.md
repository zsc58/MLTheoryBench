# Problem

## Setup

Fix integers \(d\ge1\) and \(m\ge0\). Let \(\mathcal D_d\) be the finite linear differential operators with real-valued functional coefficients on \(\mathbb R^d\), and let \(\mathcal M_d=\mathcal D_d\times\mathbb R^d\). Only marks whose operators have order at most \(m\) are considered below. Such an operator is written
\[
A=\sum_{|\alpha|\le m}a_\alpha(z)\partial^\alpha,
\]
where \(\alpha\in\mathbb Z_{\ge0}^d\), \(|\alpha|=\sum_{k=1}^d\alpha_k\), and \(\partial^\alpha=\partial_{z_1}^{\alpha_1}\cdots\partial_{z_d}^{\alpha_d}\). The mark \(x^A\) means evaluation of \(Af\) at \(x\). Operators act on the input variable before evaluation and act componentwise on vector-valued functions.

Fix a non-learnable bias scale \(\gamma>0\). For depth \(L\ge2\), input width \(n_0=d\), fixed finite output width \(n_L\ge1\), and hidden widths \(n_1,\ldots,n_{L-1}\), consider
\[
h^{(1)}(x)=W^{(1)}x+\gamma b^{(1)},\qquad
h^{(\ell+1)}(x)=n_\ell^{-1/2}W^{(\ell+1)}\sigma(h^{(\ell)}(x))+\gamma b^{(\ell+1)},
\quad 1\le\ell<L.
\]
Here \(W^{(\ell)}\in\mathbb R^{n_\ell\times n_{\ell-1}}\), \(b^{(\ell)}\in\mathbb R^{n_\ell}\), the activation acts componentwise, and all weight and bias entries are independent standard Gaussian random variables at initialization. Let \(\theta\) consist of all these weight and bias entries, excluding \(\gamma\).

Assume that \(\sigma:\mathbb R\to\mathbb R\) is differentiable through order \(m\), that \(\sigma^{(m)}\) is piecewise continuously differentiable, and that there exist constants \(C,s>0\) such that
\[
|\sigma^{(k)}(t)|\le C(1+|t|^s)
\quad\text{for almost every }t\in\mathbb R,
\qquad 0\le k\le m+1.
\]
Here \(\sigma^{(0)}=\sigma\), and the derivative of order \(m+1\) is understood wherever it exists. The activation belongs to either of these classes:

- \(\sigma\) is \(C^\infty\) and is not a polynomial;
- \(\sigma(t)=(t_+)^q\), where \(t_+=\max\{t,0\}\) and \(q\) is an integer satisfying \(q\ge m+1\).

Fix one output coordinate \(\mu\in\{1,\ldots,n_L\}\). At initialization, define the tangent kernel, almost surely, by
\[
\Theta^{(L)}(x^A,y^B)
=\left\langle\nabla_\theta A h^{(L)}_\mu(x),\nabla_\theta B h^{(L)}_\mu(y)\right\rangle.
\]
Use the sequential infinite-width limits, first \(n_1\to\infty\), then \(n_2\to\infty\), and so on through \(n_{L-1}\to\infty\), with the later widths fixed at each stage. Output evaluations converge jointly in distribution on every fixed finite marked collection of operator order at most \(m\), and each tangent-kernel entry converges in probability to a deterministic limit for every fixed pair of such marked inputs. For a finite marked set \(X=\{x_i^{A_i}\}_{i=1}^N\), let \(\Sigma_L(X)\) be the covariance matrix of the limiting output vector \((A_i h^{(L)}_\mu(x_i))_{i=1}^N\), and let \(\Theta_L(X)\) be the matrix of these limiting tangent-kernel entries.

Assume that the locations \(x_i\) are pairwise distinct and that, for every \(i\), at least one coefficient of \(A_i\) is nonzero at \(x_i\).

## Task

Prove that for every depth \(L\ge2\), every finite marked set \(X\) satisfying these assumptions, and either permitted activation class, both \(\Sigma_L(X)\) and \(\Theta_L(X)\) are positive definite. Equivalently, for every nonzero vector \(c\in\mathbb R^N\),
\[
c^\top\Sigma_L(X)c>0\quad\text{and}\quad c^\top\Theta_L(X)c>0.
\]
