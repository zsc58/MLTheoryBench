# Problem

## Setup

Let \(n,d\) be positive integers, let \(C>0\) and \(\gamma>0\) be real numbers, and let \(z_1,\ldots,z_n\in\mathbb R^d\). Norms and inner products are Euclidean. Define
\[
\phi_i(x)=\exp(-\gamma\|x-z_i\|^2),\qquad x\in\mathbb R^d.
\]
Suppose real coefficients satisfy \(0\le\alpha_i,\alpha_i^*\le C\), \(\sum_{i=1}^n(\alpha_i-\alpha_i^*)=0\), and \(\alpha_i\alpha_i^*=0\) for every \(i\). Put \(\Delta_i=\alpha_i-\alpha_i^*\), \(S_+=\{i\in\{1,\ldots,n\}:\Delta_i\ge0\}\), \(S_-=\{i\in\{1,\ldots,n\}:\Delta_i<0\}\), and
\[
C_\alpha=\sum_{i\in S_+}\alpha_i+\sum_{i\in S_-}\alpha_i^*.
\]
Assume \(C_\alpha>0\).

For a real parameter \(\rho>0\), let \(g(x)=\frac\rho2\|x\|^2\), \(h_i(x)=\frac\rho2\|x\|^2-\phi_i(x)\), and define
\[
G(x)=\sum_{i\in S_+}\alpha_i g(x)+\sum_{i\in S_-}\alpha_i^*h_i(x),\qquad
H(x)=\sum_{i\in S_+}\alpha_i h_i(x)+\sum_{i\in S_-}\alpha_i^*g(x).
\]
Let \(\widehat f=G-H\) be the predictor, with any additive constant bias omitted. Let \(\Omega\subset\mathbb R^d\) be nonempty, closed, bounded, and convex. From an arbitrary initial point \(x^{(0)}\in\Omega\), exact DCA iterates are defined, for integers \(t\ge0\), by choosing
\[
x^{(t+1)}\in\operatorname*{arg\,min}_{x\in\Omega}\{G(x)-\langle\nabla H(x^{(t)}),x\rangle\}.
\]

For a proper closed convex function \(\Phi:\mathbb R^d\to\mathbb R\cup\{+\infty\}\), write
\[
\sigma(\Phi)=\sup\{\eta\ge0:\Phi(x)-\tfrac\eta2\|x\|^2\text{ is convex}\}.
\]

## Task

Prove the following integrated theorem. Let \(\rho_{\min}=2\gamma e^{-3/2}\).

1. If \(\rho\ge\rho_{\min}\), every exact DCA subproblem above is convex.
2. If \(\rho>\rho_{\min}\), then both \(G\) and \(H\) are \(\mu\)-strongly convex on \(\mathbb R^d\), with
\[
\mu=C_\alpha(\rho-2\gamma e^{-3/2}),
\]
both have globally \(L\)-Lipschitz gradients on \(\mathbb R^d\), with
\[
L=C_\alpha(\rho+\gamma),
\]
and every exact iteration satisfies
\[
\widehat f(x^{(t+1)})\le\widehat f(x^{(t)})-\mu\|x^{(t+1)}-x^{(t)}\|^2.
\]
