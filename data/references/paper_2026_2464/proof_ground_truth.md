# Reference Proof

## Proof Structure

1. Derive the penalized normal equations on the eventual invertible tail.
2. Express the estimator around its deterministic finite-sample target, isolating the score term.
3. Prove the score's multivariate triangular-array Gaussian limit using the common error law and leverage condition.
4. Pass the convergent inverse Hessian through the score limit by Slutsky's theorem.

## Complete Proof

Write
\[
A_n=Q_n+\lambda_{1n}C_{\delta,n}+\lambda_{2n}I_p,
\qquad q_n=n^{-1}X_n^{\mathsf T}y_n.
\]
Because \(A_n\to A\) and \(A\) is positive definite, there is \(N\) such that \(A_n\) is positive definite for every \(n\ge N\). Thus, for \(n\ge N\), the objective is strictly convex and its unique minimizer satisfies
\[
A_n\widehat w_n=q_n,
\qquad \widehat w_n=A_n^{-1}q_n.
\]
Using \(y_n=X_nw_0+\varepsilon_n\),
\[
q_n=Q_nw_0+n^{-1}X_n^{\mathsf T}\varepsilon_n.
\]
For \(n\ge N\), define \(b_n=A_n^{-1}Q_nw_0\). Then
\[
\sqrt n(\widehat w_n-b_n)=A_n^{-1}n^{-1/2}X_n^{\mathsf T}\varepsilon_n. \tag{1}
\]

The errors have one common distribution over all rows and sample sizes, with mean zero, variance \(\sigma^2\), and finite \((2+\eta)\)-moment. For any fixed \(a\in\mathbb R^p\),
\[
a^{\mathsf T}n^{-1/2}X_n^{\mathsf T}\varepsilon_n
=\sum_{i=1}^n \frac{a^{\mathsf T}x_{i,n}}{\sqrt n}\,\varepsilon_{i,n}.
\]
Its variance is \(\sigma^2a^{\mathsf T}Q_na\to\sigma^2a^{\mathsf T}Qa\). Since the common \((2+\eta)\)-moment is finite and
\(\max_i\|x_{i,n}\|^2/n\to0\),
\[
\sum_{i=1}^n\mathbb E\left|\frac{a^{\mathsf T}x_{i,n}}{\sqrt n}\varepsilon_{i,n}\right|^{2+\eta}
\le \mathbb E|\varepsilon_{1,1}|^{2+\eta}\,n^{-(2+\eta)/2}\Big(\max_i|a^{\mathsf T}x_{i,n}|^\eta\Big)\sum_i|a^{\mathsf T}x_{i,n}|^2\to0.
\]
Thus Lyapunov's condition holds for every projection. The Cramer-Wold device gives
\[
n^{-1/2}X_n^{\mathsf T}\varepsilon_n\Rightarrow N(0,\sigma^2Q). \tag{2}
\]

Finally, \(A_n\to A\) implies \(A_n^{-1}\to A^{-1}\). Applying Slutsky's theorem to (1) and (2),
\[
\sqrt n(\widehat w_n-b_n)
\Rightarrow N\!\left(0,\sigma^2A^{-1}QA^{-1}\right),
\]
as claimed.
