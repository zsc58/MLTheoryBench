# Problem

## Setup

Let \(K,d\geq1\) and \(\varepsilon>0\). Let \(Y\) be uniform on \(\{1,\ldots,K\}\). Conditional on \(Y=a\), let
\[
X\sim\nu_a:=\mathcal N(m_a,C),
\]
where \(m_a\in\mathbb R^d\) and \(C\in\mathbb R^{d\times d}\) is a shared symmetric positive-semidefinite matrix.

For \(a,b\in\{1,\ldots,K\}\), define
\[
q_{ab}:=\frac14(m_a-m_b)^\top(\varepsilon I+C)^{-1}(m_a-m_b).
\]
For independent \(X_a\sim\nu_a\) and \(X_b\sim\nu_b\), define the class affinity
\[
A_{ab}:=\mathbb E\left[\exp\left(-\frac{\|X_a-X_b\|^2}{4\varepsilon}\right)\right],
\]
and define the mean-field class transition matrix by
\[
T_{ab}:=\frac{A_{ab}}{\sum_{r=1}^K A_{ar}}.
\]

## Task

Prove that, for all \(a,b\),
\[
A_{ab}=\det(I+C/\varepsilon)^{-1/2}e^{-q_{ab}}.
\]
Consequently,
\[
T_{ab}=\frac{e^{-q_{ab}}}{\sum_{r=1}^K e^{-q_{ar}}}.
\]
In particular, the class affinities up to their common prefactor, and the mean-field transition matrix exactly, are determined by the regularized pairwise separation matrix \((q_{ab})_{a,b=1}^K\).
