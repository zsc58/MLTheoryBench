# Problem

## Setup

At a fixed model checkpoint, let \(v_1,\ldots,v_n\in\mathbb R^d\) be per-example gradient vectors. Partition their indices into a clean set \(C\) and a corrupted set \(N\), and define the global mean and the two globally centered scatter matrices by
\[
m=\frac1n\sum_{i=1}^n v_i,\qquad
A=\sum_{i\in C}(v_i-m)(v_i-m)^{\mathsf T},\qquad
B=\sum_{i\in N}(v_i-m)(v_i-m)^{\mathsf T}.
\]
Assume \(\operatorname{tr}(A)>0\), and for \(t\ge0\) set \(M_t=A+tB\). Let \(P\) be the orthogonal projector onto \(\operatorname{range}(A)\), and let \(Q=I-P\).

For any positive-semidefinite matrix \(M\) with positive trace and positive eigenvalues \(\gamma_1,\ldots,\gamma_s\), define
\[
q_j(M)=\frac{\gamma_j}{\operatorname{tr}(M)},\qquad
H(M)=-\sum_{j=1}^s q_j(M)\log q_j(M),\qquad
r_{\mathrm{eff}}(M)=e^{H(M)}.
\]
If the positive eigenvalues of \(A\) are simple, write
\[
A=\sum_{k=1}^r\lambda_k u_ku_k^{\mathsf T},\qquad
p_k=\frac{\lambda_k}{\operatorname{tr}(A)},
\]
and define
\[
b_k=-\frac{r_{\mathrm{eff}}(A)}{\operatorname{tr}(A)}\bigl(\log p_k+H(A)\bigr).
\]

## Task

Prove the following theorem. There exists \(t_0>0\) such that
\[
r_{\mathrm{eff}}(M_t)>r_{\mathrm{eff}}(A)\qquad\text{for every }t\in(0,t_0)
\]
under either one of these two alternatives:

1. \(\operatorname{tr}(QBQ)>0\).
2. The positive eigenvalues of \(A\) are simple, \(\operatorname{range}(B)\subseteq\operatorname{range}(A)\), and
\[
\sum_{k=1}^r b_k\,u_k^{\mathsf T}Bu_k>0.
\]
