# Reference Proof

## Proof Structure

Expand the quadratic objective, identify its minimizer from positive definiteness, compare that minimizer with the weighted average by completing the square, and identify the resulting displacement with the correlation vector.

## Complete Proof

Let
\[
b=\sum_{i=1}^n\lambda_i A_i u_i,
\qquad
C=\sum_{i=1}^n\lambda_i u_i^\top A_i u_i.
\]
Since the matrices \(A_i\) are symmetric,
\[
F(z)=z^\top\bar A z-2z^\top b+C.
\]
Completing the square gives
\[
F(z)=(z-u_H)^\top\bar A(z-u_H)+C-b^\top\bar A^{-1}b,
\]
because \(u_H=\bar A^{-1}b\). Since \(\bar A\) is positive definite, this also shows that \(u_H\) is the unique minimizer of \(F\).

Evaluating the preceding expansion at \(u_I=\bar u\) and at \(u_H\) yields
\[
\begin{aligned}
F(u_I)-F(u_H)
&=\bar u^\top\bar A\bar u-2\bar u^\top b+b^\top\bar A^{-1}b\\
&=(\bar A\bar u-b)^\top\bar A^{-1}(\bar A\bar u-b).
\end{aligned}
\]

It remains to identify the vector in this quadratic form. Using \(\sum_i\lambda_i=1\), \(\sum_i\lambda_i A_i=\bar A\), and \(\sum_i\lambda_i u_i=\bar u\),
\[
\begin{aligned}
c
&=\sum_i\lambda_i(A_i-\bar A)(u_i-\bar u)\\
&=\sum_i\lambda_i A_i u_i
 -\Bigl(\sum_i\lambda_i A_i\Bigr)\bar u
 -\bar A\Bigl(\sum_i\lambda_i u_i\Bigr)
 +\bar A\bar u\\
&=b-\bar A\bar u.
\end{aligned}
\]
Thus \(\bar A\bar u-b=-c\), and hence
\[
F(u_I)-F(u_H)=c^\top\bar A^{-1}c.
\]
Because \(\bar A^{-1}\) is positive definite, this quantity is nonnegative and is zero if and only if \(c=0\). This proves all claims.
