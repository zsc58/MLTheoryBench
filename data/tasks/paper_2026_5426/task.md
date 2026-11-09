# Problem

## Setup

Let \(n\geq 1\), let \(\lambda_i\geq 0\) satisfy \(\sum_{i=1}^n\lambda_i=1\), and let \(u_i\in\mathbb R^p\) and real symmetric positive-semidefinite matrices \(A_i\in\mathbb R^{p\times p}\) be given. Define
\[
\bar A=\sum_{i=1}^n\lambda_i A_i,
\qquad
\bar u=\sum_{i=1}^n\lambda_i u_i,
\]
and suppose that \(\bar A\) is positive definite. For \(z\in\mathbb R^p\), define
\[
F(z)=\sum_{i=1}^n\lambda_i(z-u_i)^\top A_i(z-u_i).
\]
Set
\[
u_I=\bar u,
\qquad
u_H=\bar A^{-1}\sum_{i=1}^n\lambda_i A_i u_i,
\]
and define
\[
c=\sum_{i=1}^n\lambda_i(A_i-\bar A)(u_i-\bar u).
\]

## Task

Prove that
\[
F(u_I)-F(u_H)=c^\top\bar A^{-1}c\geq 0.
\]
Moreover, prove that equality holds if and only if \(c=0\).
