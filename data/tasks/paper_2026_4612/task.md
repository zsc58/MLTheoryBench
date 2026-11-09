# Problem

## Setup

Let \(M,T,d_1,\ldots,d_M\) be positive integers, and put \(D=\prod_{r=1}^M d_r\). For each \(t=1,\ldots,T\), let \(n_t\) be a positive integer and observe tensors \(X_{t,n}\in\mathbb R^{d_1\times\cdots\times d_M}\), \(n=1,\ldots,n_t\).

Use the following coordinate convention. The entries of \(\operatorname{vec}(X)\) are indexed by the tuples \((i_1,\ldots,i_M)\) in lexicographic order, with the last index varying fastest. Every Kronecker product of mode-indexed factors lists those factors in increasing mode order. For mode \(m\), \(\operatorname{unfold}_m(X)\) is the \(d_m\times D_{\ne m}\) matrix whose row index is \(i_m\), whose column index is the tuple of remaining indices in increasing mode order and lexicographic order, and whose corresponding entry is \(X_{i_1,\ldots,i_M}\), where
\[
D_{\ne m}=\prod_{r\ne m}d_r.
\]
An empty ordinary product is \(1\), an empty Kronecker product is the \(1\times1\) matrix \([1]\), and an empty sum is zero.

Write \(\mathbb S^d\) for the real symmetric \(d\times d\) matrices and \(\mathbb S_{++}^d\) for their positive-definite cone. Assume
\[
\operatorname{vec}(X_{t,n})\sim\mathcal N(0,P_t^{-1}),\qquad P_t=\bigotimes_{r=1}^M\Omega_t^{(r)},
\]
where each \(\Omega_t^{(r)}\in\mathbb S_{++}^{d_r}\). Define
\[
\widehat C_t=\frac1{n_t}\sum_{n=1}^{n_t}\operatorname{vec}(X_{t,n})\operatorname{vec}(X_{t,n})^\top,
\qquad \|A\|_{1,\mathrm{od}}=\sum_{i\ne j}|A_{ij}|.
\]
For each mode choose \(\lambda_m,\rho_m\ge0\). Let \(\psi\) be a dimension-compatible real-valued penalty: for each matrix size occurring among \(d_1,\ldots,d_M\), its restriction \(\psi:\mathbb S^d\to\mathbb R\) is convex. Consider
\[
F=\sum_{t=1}^T\bigl[\operatorname{tr}(\widehat C_tP_t)-\log\det P_t\bigr]
+\sum_{m=1}^M\lambda_m\sum_{t=1}^T\|\Omega_t^{(m)}\|_{1,\mathrm{od}}
+\sum_{m=1}^M\rho_m\sum_{t=2}^T\psi\!\left(\Omega_t^{(m)}-\Omega_{t-1}^{(m)}\right).
\]
For a fixed mode \(m\), set
\[
H_t^{(m)}=\bigotimes_{r\ne m}\Omega_t^{(r)},\qquad B_{t,n}^{(m)}=\operatorname{unfold}_m(X_{t,n}),
\]
and define
\[
C_t^{(m)}=\frac1{n_tD_{\ne m}}\sum_{n=1}^{n_t}B_{t,n}^{(m)}H_t^{(m)}B_{t,n}^{(m)\top}.
\]

## Task

Prove that, with all modes \(r\ne m\) fixed, minimizing \(F\) over \(\Omega_1^{(m)},\ldots,\Omega_T^{(m)}\in\mathbb S_{++}^{d_m}\) is equivalent, up to an additive constant independent of these variables and multiplication by the positive scalar \(D_{\ne m}\), to
\[
\min_{\Omega_{1:T}^{(m)}\in(\mathbb S_{++}^{d_m})^T}
\sum_{t=1}^T\left[\operatorname{tr}(C_t^{(m)}\Omega_t^{(m)})-\log\det\Omega_t^{(m)}+\frac{\lambda_m}{D_{\ne m}}\|\Omega_t^{(m)}\|_{1,\mathrm{od}}\right]
+\frac{\rho_m}{D_{\ne m}}\sum_{t=2}^T\psi\!\left(\Omega_t^{(m)}-\Omega_{t-1}^{(m)}\right).
\]
Show moreover that this is a convex time-varying graphical-lasso subproblem. Explain how cycling through the modes \(m=1,\ldots,M\), choosing an exact block minimizer at each step for which the displayed block problem has a minimizer, gives an alternating block-minimization procedure for \(F\).
