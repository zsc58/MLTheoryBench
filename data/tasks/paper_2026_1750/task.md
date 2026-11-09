# Problem

## Setup

Let \(M\) be a real symmetric \(n\times n\) matrix with distinct ordered eigenvalues
\[
\lambda_1<\lambda_2<\cdots<\lambda_n
\]
and an orthonormal eigenbasis \(e_1,\ldots,e_n\). Define
\[
f:S^{n-1}\to\mathbb R,\qquad f(x)=x^{\mathsf T}Mx,
\]
and its sublevel filtration \(X_c=\{x\in S^{n-1}:f(x)\le c\}\). Consider the persistent homology of this filtration over a fixed field, with intervals written \([b,d)\) and \([b,\infty)\). The total finite persistence is the sum of the lengths of all finite intervals, counted with multiplicity.

## Task

Prove that the persistence diagram of \(\{X_c\}_{c\in\mathbb R}\) consists exactly of
\[
[\lambda_k,\lambda_{k+1})\text{ in degree }k-1,\qquad k=1,\ldots,n-1,
\]
together with one infinite interval \([\lambda_1,\infty)\) in degree zero and one infinite interval \([\lambda_n,\infty)\) in degree \(n-1\). In particular, prove that the total finite persistence equals \(\lambda_n-\lambda_1\).
