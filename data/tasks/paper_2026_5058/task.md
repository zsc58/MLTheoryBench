# Problem

## Setup

Fix \(\delta\in(0,1/2)\) and a bandwidth \(\sigma>0\), independent of \(d,n\). For a fixed constant \(c>0\), let \(d\to\infty\) and set
\[
n=\left\lfloor\exp(c d^{2\delta})\right\rfloor.
\]
Let \(x_1,\ldots,x_n\) be independent uniform samples from the unit sphere \(S^{d-1}\subset\mathbb R^d\). For \(i\ne j\), define
\[
p_{j|i}=\frac{\exp(-\|x_i-x_j\|^2/(2\sigma^2))}{\sum_{k\ne i}\exp(-\|x_i-x_k\|^2/(2\sigma^2))},
\qquad
p_{ij}=\frac{p_{j|i}+p_{i|j}}{n},
\]
so that \(P=(p_{ij})_{i<j}\) is a probability distribution on unordered pairs. For an embedding \(Y=(y_1,\ldots,y_n)\in(\mathbb R^2)^n\), define
\[
q_{ij}(Y)=\frac{(1+\|y_i-y_j\|^2)^{-1}}{\sum_{a<b}(1+\|y_a-y_b\|^2)^{-1}},
\qquad
C(Y)=D(P\|Q(Y))=\sum_{i<j}p_{ij}\log\frac{p_{ij}}{q_{ij}(Y)}.
\]
Assume \(r=r(d)\to0\), \(r=\omega(d^{-1/6+\delta/3})\), and \(r=\Omega(1/n)\). A global minimizer means any \(Y\) attaining the minimum of \(C\) over \((\mathbb R^2)^n\).

## Task

Prove that there exists a constant \(c_*>0\) such that, for every fixed \(c\in(0,c_*)\) in the setup, the following holds for all sufficiently large \(d\): with probability at least \(1-\exp(-\Omega(d^{2\delta}))\) over the sampled sphere points, every global minimizer \(Y\) has an open Euclidean ball of radius \(r\) containing at least \((1-r)n\) embedded points, and all embedded points lie in some Euclidean ball of radius \(O(\sqrt r)\). The implicit constants may depend on \(\sigma\) and \(\delta\), but not on \(c\), \(d\), or \(n\).
