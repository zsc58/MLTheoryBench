# Problem

## Setup

All vector norms are Euclidean, and the norm used for Jacobians is the induced operator norm. Write \(\sigma_{\max}\) for the largest singular value.

Let \(h:\mathbb R^n\to\mathbb R^p\) be twice differentiable and convex componentwise. Let \(L\ge0\) be finite and suppose
\[
\|J_h(y)-J_h(z)\|_{\mathrm{op}}\le L\|y-z\|\qquad\text{for all }y,z\in\mathbb R^n.
\]
Let \(A\in\mathbb R^{m\times n}\), and let \(\ell_A,u_A\in\mathbb R^m\) satisfy \(\ell_A\le u_A\) componentwise. Define
\[
C=\{y\in\mathbb R^n:h(y)\le0,\ \ell_A\le Ay\le u_A\},
\]
and assume \(C\ne\varnothing\). Let \(P_{[\ell_A,u_A]}\) be coordinatewise projection onto the box \([\ell_A,u_A]\), and let \([v]_+\) denote coordinatewise positive part. Define
\[
F(y)=\frac12\|[h(y)]_+\|^2+\frac12\|Ay-P_{[\ell_A,u_A]}(Ay)\|^2.
\]
For an initial point \(y^0\in\mathbb R^n\), let \(S=\{y:F(y)\le F(y^0)\}\) and assume
\[
R:=\sup_{y\in S}\inf_{y^*\in C}\|y-y^*\|<\infty.
\]
Set \(g(y)=(h(y),Ay)\), with combined bounds \(\ell=(-\infty,\ell_A)\) and \(u=(0,u_A)\), and let \(J_g\) be its Jacobian. Let \(\sigma\ge0\) be finite and assume on \(S\) that
\[
\sigma_{\max}^2(J_h(y))+\sigma_{\max}^2(A)\le\sigma^2.
\]
Choose a fixed \(\lambda>0\) satisfying
\[
\lambda^2-\sqrt{2F(y^0)}\,L\lambda-\frac{L^2F(y^0)}{16}\ge0.
\]
Define
\[
y^{k+1}=y^k-\bigl(J_g(y^k)^TJ_g(y^k)+\lambda I\bigr)^{-1}\nabla F(y^k),\qquad k=0,1,2,\ldots,
\]
where \(I\) is the \(n\times n\) identity matrix.

## Task

Prove that every iterate is well defined, remains in \(S\), and, for every \(k\ge0\),
\[
F(y^k)\le\frac{F(y^0)}{1+F(y^0)k/[2R^2(\sigma^2+\lambda)]}.
\]
When \(F(y^0)=0\), interpret the conclusion directly as \(y^0\in C\) and \(F(y^k)=0\); otherwise the displayed bound applies with \(R>0\). In all cases \(F(y^k)\to0\), so the iterations converge to feasibility of \(C\).
