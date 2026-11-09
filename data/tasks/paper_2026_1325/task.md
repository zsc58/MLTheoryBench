# Problem

## Setup

Work in Euclidean spaces. Fix \(x\in\mathbb R^d\), \(W\in\mathbb R^{n\times n}\), \(U\in\mathbb R^{n\times d}\), and \(b\in\mathbb R^n\). Let \(G:\mathbb R^n\to\mathbb R^n\) be a locally Lipschitz monotone map. Define

\[
F(z)=(I-W)z-(Ux+b).
\]

Assume \(F\) is \(m\)-strongly monotone for some \(m>0\), and set \(L=\|I-W\|_2\). A quantized weight matrix is \(W_q=W+\Delta W\) with \(\|\Delta W\|_2\le\epsilon\). For symmetric uniform \(b\)-bit quantization on \([-1,1]\), one may take \(\epsilon=n2^{1-b}/2\). Define

\[
F_q(z)=(I-W_q)z-(Ux+b),\qquad
m_q=\lambda_{\min}(\operatorname{sym}(I-W_q)),\qquad
L_q=\|I-W_q\|_2,
\]

\[
J_{\alpha G}=(I+\alpha G)^{-1},\qquad
\Phi_q(z)=J_{\alpha G}(z-\alpha F_q(z)).
\]

Let \(\theta=(W,U,b)\). At a parameter point where \(W_q(\theta)\) and the quantized equilibrium \(z_q^*(\theta)\) are differentiable, set \(p=D_\theta z_q^*\) columnwise and

\[
r=(D_\theta W_q)z_q^*+(D_\theta U)x+D_\theta b.
\]

Let \(G_b\) be a matrix in the Clarke generalized Jacobian of \(G\) at \(z_q^*\) whose symmetric part is positive semidefinite and which is compatible with the columnwise chain rule:

\[
D_\theta\bigl[G(z_q^*(\theta))\bigr]=G_bp.
\]

Let \(G_b\) act columnwise and define

\[
\Psi_{q,b}(P)=J_{\alpha G_b}\bigl(P-\alpha[(I-W_q)P-r]\bigr).
\]

## Task

Prove that if \(\epsilon<m\), then

\[
m_q\ge m-\epsilon>0
\quad\text{and}\quad
|L-\epsilon|\le L_q\le L+\epsilon.
\]

For every \(0<\alpha<2m_q/L_q^2\), prove that \(\Phi_q\) is a contraction with modulus

\[
\rho=\sqrt{1-2\alpha m_q+\alpha^2L_q^2};
\]

consequently, the quantized equilibrium equation \(0\in F_q(z)+G(z)\) has a unique solution and its forward iteration converges linearly. Moreover, for every \(G_b\) satisfying the setup's compatibility condition, prove that the sensitivity \(p\) is the unique solution of

\[
0=(I-W_q)p-r+G_bp,
\]

and that the iteration \(P_{k+1}=\Psi_{q,b}(P_k)\) converges linearly to \(p\) with the same \(\rho\) and stepsize condition.
