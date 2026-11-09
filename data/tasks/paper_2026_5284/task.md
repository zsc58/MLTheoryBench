# Problem

## Setup

Let \(m,d\) be positive integers. Equip real matrix spaces and their linear subspaces with the Frobenius inner product
\[
\langle A,B\rangle_F=\operatorname{tr}(A^TB),\qquad
\|A\|_F^2=\langle A,A\rangle_F.
\]
Let \(W_0\in\mathbb{R}^{m\times d}\), and let \(L:\mathbb{R}^{m\times d}\to\mathbb{R}\) be differentiable at \(W_0\), with \(G=\nabla L(W_0)\). Define
\[
O(k)=\{U\in\mathbb{R}^{k\times k}:U^TU=I_k\},\qquad
\operatorname{Skew}(k)=\{A\in\mathbb{R}^{k\times k}:A^T=-A\},
\]
and, for a square matrix \(A\), define \(\operatorname{skew}(A)=\tfrac12(A-A^T)\). Set
\[
F=\operatorname{skew}(W_0^TG)\in\operatorname{Skew}(d).
\]

Fix an integer \(1\le r\le d\) and a row-orthonormal matrix \(P\in\mathbb{R}^{r\times d}\) satisfying \(PP^T=I_r\). For each \(E\in\operatorname{Skew}(r)\), let \(t\mapsto Q(tE)\in O(r)\) be a smooth path near \(t=0\), with
\[
Q(0)=I_r,\qquad \frac{d}{dt}Q(tE)\Big|_{t=0}=E.
\]
For this direction \(E\), define the supported update
\[
W(t)=W_0\bigl[I_d+P^T(Q(tE)-I_r)P\bigr].
\]
The initialization gradient on \(\operatorname{Skew}(r)\) means the Frobenius representative of the first variation: a matrix \(H\in\operatorname{Skew}(r)\) such that
\[
\frac{d}{dt}L(W(t))\Big|_{t=0}=\langle H,E\rangle_F
\quad\text{for every }E\in\operatorname{Skew}(r).
\]

Let \(q\) be the number of nonzero conjugate eigenvalue pairs of \(F\), counted with multiplicity. Write their positive magnitudes as
\[
\mu_1\ge\mu_2\ge\cdots\ge\mu_q>0,
\]
so the nonzero pairs are \(\pm i\mu_j\), and set \(\mu_j=0\) for \(q<j\le\lfloor d/2\rfloor\). The positive list is empty when \(q=0\), and empty sums are understood to be zero.

## Task

Prove that, for every \(E\in\operatorname{Skew}(r)\),
\[
\frac{d}{dt}L(W(t))\Big|_{t=0}=\langle PFP^T,E\rangle_F,
\]
so the initialization gradient on \(\operatorname{Skew}(r)\) is \(PFP^T\). Moreover, prove the sharp support bound
\[
\|PFP^T\|_F^2\le 2\sum_{j=1}^{\lfloor r/2\rfloor}\mu_j^2.
\]
Prove that equality is attained by choosing the row space of \(P\) to contain a direct sum of mutually orthogonal real two-dimensional invariant subspaces associated with the leading \(\min\{q,\lfloor r/2\rfloor\}\) nonzero eigenvalue pairs, counted with multiplicity, and completing that subspace to dimension \(r\) with orthogonal directions as necessary. Choices among tied pair magnitudes are permitted. This assertion includes both odd \(r\) and the case in which fewer than \(\lfloor r/2\rfloor\) nonzero pairs exist.
