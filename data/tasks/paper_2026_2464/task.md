# Problem

## Setup

Fix a parameter dimension \(p\). For each \(n\), let the deterministic matrices \(X_n\in\mathbb R^{n\times p}\) and \(R_n\in\mathbb R^{n\times p}\) have rows \(x_{i,n}^{\mathsf T}\) and \(r_{i,n}^{\mathsf T}\), respectively, and observe
\[
y_n=X_nw_0+\varepsilon_n,
\]
where \(w_0\in\mathbb R^p\). Assume:

- \(Q_n=n^{-1}X_n^{\mathsf T}X_n\to Q\), with \(Q\) positive definite;
- \(C_n=n^{-1}R_n^{\mathsf T}R_n\to C\), where \(C\) is positive semidefinite;
- for fixed \(\delta>0\), \(C_{\delta,n}:=C_n+\delta I_p\to C_\delta:=C+\delta I_p\);
- \(\max_{1\le i\le n}\|x_{i,n}\|_2^2/n\to0\);
- the collection \(\{\varepsilon_{i,n}:n\ge1,1\le i\le n\}\) is iid with common mean zero, variance \(\sigma^2\in(0,\infty)\), and finite \((2+\eta)\)-moment for some \(\eta>0\);
- \(\lambda_{1n},\lambda_{2n}\ge0\), \(\lambda_{1n}\to\lambda_1\), \(\lambda_{2n}\to\lambda_2\), and \(A:=Q+\lambda_1C_\delta+\lambda_2I_p\) is positive definite.

For each \(n\), let \(\widehat w_n\) minimize
\[
\frac{1}{2n}\|y_n-X_nw\|_2^2
+\frac{\lambda_{1n}}2w^{\mathsf T}C_{\delta,n}w
+\frac{\lambda_{2n}}2\|w\|_2^2.
\]
Since \(A_n:=Q_n+\lambda_{1n}C_{\delta,n}+\lambda_{2n}I_p\to A\), choose \(N\) so that \(A_n\) is positive definite for all \(n\ge N\), and for such \(n\) define
\[
b_n:=A_n^{-1}Q_nw_0.
\]

## Task

Prove that, as \(n\to\infty\),
\[
\sqrt n\,(\widehat w_n-b_n)
\Rightarrow
N\!\left(0,\,\sigma^2A^{-1}QA^{-1}\right).
\]
