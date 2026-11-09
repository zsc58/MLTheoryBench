# Problem

## Setup

Let \(L\geq2\) be an integer, let \(B\geq L+2\), and let \(d_0,d_L\) be positive integers. Consider depth-\(L\) networks with input dimension \(d_0\), output dimension \(d_L\), and a common positive integer hidden width \(d\), which may vary from network to network. Thus \(d_1=\cdots=d_{L-1}=d\).

For an input \(x\in[0,1]^{d_0}\), set \(h^{(0)}=x\) and define
\[
 a_i^{(\ell)}=\frac{1}{L+2}\left(
 \frac{1}{d_{\ell-1}}\sum_{j=1}^{d_{\ell-1}}
 W_{ij}^{(\ell)}h_j^{(\ell-1)}+b_i^{(\ell)}
 \right),\qquad 1\leq\ell\leq L.
\]
Set \(h_i^{(\ell)}=\max\{0,a_i^{(\ell)}\}\) for \(1\leq\ell<L\), and set \(h_i^{(L)}=a_i^{(L)}\). The network output is \(N(x)=h^{(L)}\).

The network is **\(B\)-strongly dense** if every weight and bias entry has absolute value at most \(B\). Let \(\mathcal N_{B,L,d_0,d_L}\) denote the class of all such networks, allowing every positive common hidden width. For a fixed architecture, let \(W\) denote its total number of scalar weights and biases.

Write \(\operatorname{Lip}(d_0,d_L)\) for the functions \(f:[0,1]^{d_0}\to[-1,1]^{d_L}\) satisfying
\[
 \|f(x)-f(y)\|_\infty\leq\|x-y\|_\infty
 \quad\text{for all }x,y\in[0,1]^{d_0},
\]
where both vector norms are coordinatewise maximum norms. For functions on the cube, use
\[
 \|f-g\|_\infty=\sup_{x\in[0,1]^{d_0}}
 \max_{1\leq i\leq d_L}|f_i(x)-g_i(x)|.
\]
The class \(\mathcal N_{B,L,d_0,d_L}\) is universal for this Lipschitz class if for every \(f\in\operatorname{Lip}(d_0,d_L)\) and every \(\varepsilon>0\) there is \(N\in\mathcal N_{B,L,d_0,d_L}\) with \(\|f-N\|_\infty<\varepsilon\).

Let \(c>0\) be a universal constant for which the VC dimension of the class obtained by thresholding a scalar output of any fixed ReLU architecture with \(W\) scalar weights and biases is at most \(cW^2\), allowing unrestricted parameters. Define
\[
 \widetilde W=d_0^2d_L^4L^3(L+2)^2(2B)^{2L}\,
 2^{\,2^{14}(L+2)^2d_L^2(2B)^{2L}+18}.
\]
Assume additionally that \(d_0>1800\) and
\[
 \log_2(c^{1/2}\widetilde W)
 <\frac{d_0}{2}\log_2(4/3).
\]

## Task

Prove that \(\mathcal N_{B,L,d_0,d_L}\) is not a universal approximator of \(\operatorname{Lip}(d_0,d_L)\).
