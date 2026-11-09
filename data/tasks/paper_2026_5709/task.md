# Problem

## Setup

Let \(n,p\geq 1\) be integers, let \(x_1,\ldots,x_n\in\mathbb R^p\), and let \(Q,R,S\) be linear maps from \(\mathbb R^p\) to \(\mathbb R^p\). Let \(\phi:\mathbb R\to\mathbb R\) act coordinatewise on vectors.

Fix a displacement kernel \(\kappa:\mathbb R\to\mathbb R^p\) parameterized by a finite sinusoidal network. Thus, for some integers \(r\geq 0\) and \(m\geq 1\), and positive real frequencies \(\omega_0,\omega_h\),
\[
h_0(t)=\sin(\omega_0 W_0t+b_0),\qquad
h_\ell(t)=\sin(\omega_hW_\ell h_{\ell-1}(t))\quad(1\leq \ell\leq r),
\qquad
\kappa(t)=W_{\mathrm{out}}h_r(t),
\]
where
\[
W_0\in\mathbb R^{m\times 1},\qquad
b_0\in\mathbb R^m,\qquad
W_\ell\in\mathbb R^{m\times m}\quad(1\leq\ell\leq r),\qquad
W_{\mathrm{out}}\in\mathbb R^{p\times m},
\]
and sine is coordinatewise.

Define the gated mixer by
\[
z_j=(Qx_j)\odot\phi(Rx_j),
\qquad
y_i=\left(\sum_{j=1}^n
\kappa\!\left(\frac{i-j}{n}\right)\odot z_j\right)
\odot\phi(Sx_i),
\quad 1\leq i\leq n,
\]
where \(\odot\) denotes coordinatewise multiplication.

Call an \(n\times n\) matrix separable if it has the form \(D_{\mathrm{out}}TD_{\mathrm{in}}\), where the two outer factors are diagonal and \(T\) is Toeplitz, meaning \(T_{ij}=t_{i-j}\).

## Task

Prove that, independently for every channel \(h\in\{1,\ldots,p\}\), the matrix of scalar summands induced by the gated mixer is separable. More precisely, set
\[
a_j^{(h)}=(Qx_j)^{(h)}\phi(Rx_j)^{(h)},
\qquad
b_i^{(h)}=\phi(Sx_i)^{(h)},
\]
and let \(M^{(h)}\) be the matrix satisfying
\[
y_i^{(h)}=\sum_{j=1}^n M_{ij}^{(h)}
\]
with \(M_{ij}^{(h)}\) equal to the corresponding \(j\)-th summand in the mixer formula. Prove the exact factorization
\[
M^{(h)}=D_{\mathrm{out}}^{(h)}T^{(h)}D_{\mathrm{in}}^{(h)},
\]
where
\[
T_{ij}^{(h)}=\kappa^{(h)}\!\left(\frac{i-j}{n}\right),
\quad
D_{\mathrm{out}}^{(h)}=\operatorname{diag}(b_1^{(h)},\ldots,b_n^{(h)}),
\quad
D_{\mathrm{in}}^{(h)}=\operatorname{diag}(a_1^{(h)},\ldots,a_n^{(h)}),
\]
and establish that \(T^{(h)}\) is Toeplitz.
