# Problem

## Setup

Let \(n,d\) be positive integers, let \(\mathcal L\) be a finite nonempty label set, and let
\[
x_1,\ldots,x_n\in\mathbb R^d.
\]
For each \(i\), let \(L_i\subseteq\mathcal L\) be nonempty, put \(k_i=|L_i|\ge1\), and assume every label occurs at least once. Define
\[
n_\ell=|\{i:\ell\in L_i\}|\ge1,\qquad
\mu=\frac1n\sum_{i=1}^n x_i,\qquad
\mu_\ell=\frac1{n_\ell}\sum_{i:\ell\in L_i}x_i.
\]
All sums over labels below are over \(\mathcal L\). Define
\[
 B=\sum_{\ell\in\mathcal L} n_\ell(\mu_\ell-\mu)(\mu_\ell-\mu)^\top,\qquad
 U=\sum_{i=1}^n\sum_{\ell\in L_i}(x_i-\mu_\ell)(x_i-\mu_\ell)^\top,
\]
\[
 T_{\rm ml}=B+U,\qquad
 T=\sum_{i=1}^n(x_i-\mu)(x_i-\mu)^\top.
\]
Assume \(U\succ0\). Let the target dimension satisfy
\[
1\le r<d,\qquad r\le\operatorname{rank}(B).
\]
For every full-column-rank \(W\in\mathbb R^{d\times r}\), define
\[
 {\rm TR}(W)=\frac{\operatorname{tr}(W^\top BW)}{\operatorname{tr}(W^\top UW)},\quad
 {\rm RT}(W)=\operatorname{tr}[(W^\top UW)^{-1}(W^\top BW)],
\]
\[
 {\rm DR}(W)=\frac{\det(W^\top BW)}{\det(W^\top UW)},\quad
 {\rm TD}(W)=\operatorname{tr}(W^\top(B-U)W).
\]
The Stiefel constraint is \(W^\top W=I_r\).

## Task

Prove the following integrated theorem.

If all \(k_i=k\), assume \(B\) and \(T\) commute. Let \(q_j\) be a common orthonormal eigenbasis, with \(Bq_j=b_jq_j\) and \(Tq_j=t_jq_j\), and put \(u_j=kt_j-b_j\). Suppose an index set \(I\) of size \(r\) simultaneously consists of the \(r\) largest values of \(2b_j-kt_j\) and \(b_j/u_j\), with the explicit strict boundary separations
\[
\min_{i\in I}(2b_i-kt_i)>\max_{j\notin I}(2b_j-kt_j),
\qquad
\min_{i\in I}\frac{b_i}{u_i}>\max_{j\notin I}\frac{b_j}{u_j}.
\]
Assume also that
\[
\frac{\sum_{i\in I}b_i}{\sum_{i\in I}u_i}
\ge\frac{\sum_{j\in J}b_j}{\sum_{j\in J}u_j}
\quad\text{for every }J\subseteq\{1,\ldots,d\},\ |J|=r.
\]
Then \(\operatorname{span}\{q_i:i\in I\}\) maximizes TR, RT, DR, and TD over \(W^\top W=I_r\).

For arbitrary cardinalities, let \(\mathcal E_{\rm ml}\) and \(\mathcal E_0\) denote the top-\(r\) eigenspaces of \(2B-T_{\rm ml}\) and \(2B-T\), respectively. If \(\gamma=\lambda_r(2B-T)-\lambda_{r+1}(2B-T)>0\) and \(\|T_{\rm ml}-T\|_2<\gamma\), prove that TD is maximized on \(\mathcal E_{\rm ml}\), that ratio-trace optimization need not have the same eigenspace, and that
\[
\|\sin\Theta(\mathcal E_{\rm ml},\mathcal E_0)\|_2\le\frac{\|T_{\rm ml}-T\|_2}{\gamma}.
\]
