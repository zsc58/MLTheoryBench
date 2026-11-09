# Problem

## Setup

Let \(n,p,d\) be positive integers with \(1\le d\le p\). Let \(x_i\in\mathbb R^p\) and \(y_i\in\mathbb R\), \(i=1,\ldots,n\), be fixed data. For each anchor \(j\in\{1,\ldots,n\}\), let \(w_{ij}\ge0\) and \(\sum_{i=1}^n w_{ij}=1\). The weights are fixed and do not vary with the optimization variable \(B\). Define
\[
\bar x_j=\sum_{i=1}^n w_{ij}x_i,\qquad \bar y_j=\sum_{i=1}^n w_{ij}y_i,\qquad z_i^{(j)}=x_i-\bar x_j,
\]
\[
\tilde y_i^{(j)}=y_i-\bar y_j,\qquad G^{(j)}=\sum_{i=1}^n w_{ij}z_i^{(j)}z_i^{(j)T},\qquad \mu^{(j)}=\sum_{i=1}^n w_{ij}z_i^{(j)}\tilde y_i^{(j)}.
\]
Let
\[
\operatorname{St}(p,d)=\{B\in\mathbb R^{p\times d}:B^TB=I_d\},\qquad
O(d)=\{R\in\mathbb R^{d\times d}:R^TR=I_d\}.
\]
Identify \(B\) and \(BR\), for \(R\in O(d)\), as the same element of \(\operatorname{Gr}(p,d)\), the manifold of \(d\)-dimensional linear subspaces of \(\mathbb R^p\). Equip \(\operatorname{St}(p,d)\) with the embedded Frobenius metric
\[
\langle\xi,\eta\rangle_B=\operatorname{tr}(\xi^T\eta)
\]
on its tangent spaces, and equip \(\operatorname{Gr}(p,d)\) with the induced quotient metric.

Define
\[
Q(B)=\sum_{j=1}^n\min_{a_j\in\mathbb R,\,b_j\in\mathbb R^d}\sum_{i=1}^n w_{ij}\bigl(y_i-a_j-b_j^TB^T(x_i-x_j)\bigr)^2.
\]
Assume \(B^TG^{(j)}B\) is invertible for every anchor \(j\) and every \(B\in\operatorname{St}(p,d)\).

## Task

Prove the following integrated theorem. Define
\[
F(B)=\sum_{j=1}^n\mu^{(j)T}B\bigl(B^TG^{(j)}B\bigr)^{-1}B^T\mu^{(j)}.
\]
Then minimizing \(Q\) over \(\operatorname{St}(p,d)\) is equivalent to maximizing \(F\); for every \(R\in O(d)\), \(F(BR)=F(B)\), so \(F\) is a well-defined smooth objective on \(\operatorname{Gr}(p,d)\); and the Riemannian gradient of \(F\) on \(\operatorname{St}(p,d)\) is
\[
\operatorname{grad}F(B)=2\sum_{j=1}^n\bigl(\mu^{(j)}-G^{(j)}B u^{(j)}\bigr)u^{(j)T},
\qquad u^{(j)}=\bigl(B^TG^{(j)}B\bigr)^{-1}B^T\mu^{(j)}.
\]
This matrix is also the horizontal lift at \(B\) of the gradient of the descended Grassmannian objective for the specified quotient metric.
