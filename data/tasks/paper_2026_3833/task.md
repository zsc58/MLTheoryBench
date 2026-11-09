# Problem

## Setup

Fix a field \(\mathbb F\) and a finite ordered vertex set \(V=\{1,\ldots,n\}\), where \(n\geq 0\). Let \(w,\widetilde w\in[0,\infty)^{n\times n}\) be symmetric matrices with zero diagonal, indexed by \(V\).

For a symmetric matrix \(C\) with entries in \([0,\infty]\) and zero diagonal, and a finite scale \(\alpha\geq0\), let \(R_\alpha(C)\) be the simplicial complex consisting of the vertex subsets \(\sigma\) such that \(C_{rs}\leq\alpha\) for every pair of distinct vertices \(r,s\in\sigma\).

Set
\[
 A_\wedge=\min(w,\widetilde w),\qquad A_\vee=\max(w,\widetilde w),
\]
entrywise.

For a symmetric nonnegative \(n\times n\) matrix \(A\) with zero diagonal, define
\[
 (A^+)_{rs}=\begin{cases}\infty,&r<s,\\A_{rs},&r\geq s.\end{cases}
\]
For two such matrices \(A,B\), define
\[
 T(A,B)=
 \begin{bmatrix}
 A&(A^+)^\top&0\\
 A^+&B&\infty\\
 0&\infty&0
 \end{bmatrix}.
\]
The blocks correspond to two copies of \(V\) and one additional vertex; \(0\) and \(\infty\) denote constant blocks of the indicated sizes.

There are two indexed orientations \((a,b)=(w,\widetilde w)\) and \((a,b)=(\widetilde w,w)\). Every sum over orientations below contains both indexed terms, including when \(w=\widetilde w\). Define
\[
 M_{\mathrm{sym}}=T(A_\vee,A_\wedge),\qquad
 M_{\min}(a,b)=T(a,A_\wedge),\qquad
 M_{\max}(a,b)=T(A_\vee,a).
\]

For each auxiliary filtration \(K_\alpha=R_\alpha(M)\) defined by one of these matrices, let
\[
 \overline\beta_i(K_\alpha)=
 \begin{cases}
 \dim_{\mathbb F}\widetilde H_0(K_\alpha;\mathbb F),&i=0,\\
 \dim_{\mathbb F}H_i(K_\alpha;\mathbb F),&i>0,
 \end{cases}
\]
and define its finite persistence by
\[
 \operatorname{Pers}_i(K)=\int_0^\infty\overline\beta_i(K_\alpha)\,d\alpha.
\]
For these auxiliary filtrations this is equivalently the sum of the finite interval lengths in the degree-\(i\) persistence barcode. Set
\[
 \mathcal D_{\mathrm{sym},i}=\operatorname{Pers}_i(R_\bullet(M_{\mathrm{sym}})),
\]
\[
 \mathcal D_{\min,i}=\tfrac12\sum_{(a,b)}\operatorname{Pers}_i(R_\bullet(M_{\min}(a,b))),\qquad
 \mathcal D_{\max,i}=\tfrac12\sum_{(a,b)}\operatorname{Pers}_i(R_\bullet(M_{\max}(a,b))),
\]
where both sums are over the two indexed orientations.

For each \(\alpha\geq0\), put
\[
 I_\alpha=R_\alpha(A_\vee),\qquad
 U_\alpha=R_\alpha(A_\wedge),\qquad
 X^a_\alpha=R_\alpha(a).
\]
For each orientation, let
\[
 \gamma_i^a(\alpha):H_i(X^a_\alpha,I_\alpha;\mathbb F)
 \longrightarrow H_i(U_\alpha,I_\alpha;\mathbb F)
\]
be the relative-homology map induced by inclusion of pairs. Set \(\gamma_{-1}^a(\alpha):0\to0\), so its kernel has dimension zero.

## Task

Prove that, for every homological dimension \(i\geq0\),
\[
\mathcal D_{\max,i}+\mathcal D_{\min,i}-\mathcal D_{\mathrm{sym},i}
=
\frac12\sum_{(a,b)}
\int_0^\infty
\left(
\dim\ker\gamma_i^a(\alpha)+
\dim\ker\gamma_{i-1}^a(\alpha)
\right)d\alpha,
\]
where the sum is over the two indexed orientations.
