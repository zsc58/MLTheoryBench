# Problem

## Setup

Let \(f,g:\mathbb R^d\to\mathbb R^m\) be differentiable representation maps. Fix a smooth coordinate map \(\psi:\Omega\subset\mathbb R^q\to\mathbb R^d\), a probability measure \(\nu\) on \(\Omega\), an integer \(1\le k\le q\), and a matrix \(P\in\mathbb R^{q\times k}\) with orthonormal columns. Fix \(\Sigma\in\mathbb S_{++}^m\), and assume that all expectations below exist.

For \(u\in\{f,g\}\), write \(h_u=u\circ\psi\) and define
\[
K_u:=\mathbb E_{s\sim\nu}\left[P^T J_{h_u}(s)^T\Sigma^{-1}J_{h_u}(s)P\right]\in\mathbb S_+^k.
\]
For each \(C\in\mathbb S_+^k\), define the corresponding second-moment task value by
\[
T_C(u):=\operatorname{Tr}(CK_u).
\]

Assume \(K_f\ne0\) and \(K_g\ne0\). Fix \(\lambda>0\), and define the lifted matrices and lifted task values
\[
H_u:=K_u+\lambda\frac{\operatorname{Tr}(K_u)}{k}I_k,
\qquad
U_C(u):=\operatorname{Tr}(CH_u).
\]
Thus \(H_f,H_g\in\mathbb S_{++}^k\). For SPD matrices \(A,B\), set
\[
d(A,B):=\left\|\log\left(A^{-1/2}BA^{-1/2}\right)\right\|_F.
\]
Finally, let
\[
\delta:=\frac{d(H_f,H_g)}{\sqrt{k}},
\qquad R:=e^{-\delta}.
\]

## Task

Prove the following integrated claim.

The matrix \(K_u\) is a minimal complete summary of the task family \(\{T_C(u):C\in\mathbb S_+^k\}\) in the following sense: it determines every task value, and if \(T_C(f)=T_C(g)\) for every \(C\in\mathbb S_+^k\), then \(K_f=K_g\). Moreover, the lifted summaries satisfy, simultaneously for every \(C\in\mathbb S_+^k\),
\[
R^{\sqrt{k}}U_C(f)\ \le\ U_C(g)\ \le\ R^{-\sqrt{k}}U_C(f).
\]
