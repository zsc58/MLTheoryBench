# Reference Proof

## Proof Structure

For each anchor, profile the weighted local regression by removing its intercept and solving the centered weighted least-squares problem. Express the minimized residual as a B-independent total energy minus a projection term, yielding F. Prove right-orthogonal invariance by conjugating the Gram matrix and establish smoothness on the Stiefel manifold and its quotient. Differentiate one summand using the inverse-matrix differential, verify tangency and horizontality, identify the gradients under the specified metrics, and sum over anchors.

## Complete Proof

### 1. Profiling the local regressions

Fix an anchor \(j\in\{1,\ldots,n\}\). Write \(z_i=x_i-\bar x_j\), \(y_i^c=y_i-\bar y_j\), \(G=G^{(j)}\), and \(\mu=\mu^{(j)}\). The normalization of the weights gives
\[
\sum_iw_{ij}z_i=0,\qquad \sum_iw_{ij}y_i^c=0.
\]
For any fixed slope \(b\), set
\[
a_*(b)=\bar y_j-b^TB^T(\bar x_j-x_j).
\]
Since \(x_i-x_j=z_i+(\bar x_j-x_j)\), the local objective decomposes as
\[
\sum_iw_{ij}\bigl(y_i-a-b^TB^T(x_i-x_j)\bigr)^2
=\sum_iw_{ij}(y_i^c-b^TB^Tz_i)^2+(a-a_*(b))^2.
\]
The cross term vanishes by the two centering identities. Therefore its minimum over the intercept is attained at \(a_*(b)\).

Let \(W=\operatorname{diag}(w_{1j},\ldots,w_{nj})\), let \(Z\) have rows \(z_i^T\), and let \(y^c\) be the vector of centered responses. Put
\[
M=B^TGB=(ZB)^TW(ZB),\qquad v=B^T\mu,\qquad c_j=(y^c)^TWy^c.
\]
Nonnegative weights imply that \(M\) is symmetric positive semidefinite. By the assumed invertibility it is positive definite. The centered objective equals
\[
c_j-2b^Tv+b^TMb.
\]
Its normal equation is \(Mb=v\), with unique solution \(u=M^{-1}v\). Completing the square gives
\[
c_j-2b^Tv+b^TMb
=c_j-v^TM^{-1}v+(b-u)^TM(b-u).
\]
Consequently the minimized local residual is
\[
c_j-\mu^{(j)T}B(B^TG^{(j)}B)^{-1}B^T\mu^{(j)}.
\]
Summing over anchors yields
\[
Q(B)=C-F(B),\qquad
C=\sum_{j=1}^n\sum_{i=1}^nw_{ij}(y_i-\bar y_j)^2.
\]
The finite constant \(C\) is independent of \(B\), because the data and weights are fixed. Hence the minimizers of \(Q\) are exactly the maximizers of \(F\).

### 2. Orthogonal invariance and smoothness

For \(R\in O(d)\), if \(M=B^TG^{(j)}B\), then
\[
(BR)^TG^{(j)}(BR)=R^TMR,
\qquad (R^TMR)^{-1}=R^TM^{-1}R.
\]
Thus
\[
\mu^{(j)T}BR(R^TMR)^{-1}R^TB^T\mu^{(j)}
=\mu^{(j)T}BM^{-1}B^T\mu^{(j)}.
\]
Every summand is invariant, so \(F(BR)=F(B)\).

To verify smoothness, define the ambient open set
\[
\mathcal U=\{A\in\mathbb R^{p\times d}:\det(A^TG^{(j)}A)\ne0\text{ for every }j\}.
\]
It contains \(\operatorname{St}(p,d)\) by assumption. Matrix inversion is smooth on invertible matrices, as is also seen from the adjugate divided by the nonzero determinant. Thus the same formula defines a smooth extension of \(F\) to \(\mathcal U\).

Invariance makes \(\widehat F(\operatorname{span}(B))=F(B)\) well-defined. Smoothness of this quotient function can be checked in local graph coordinates. Fix an orthonormal basis \([B_0\ C_0]\) of \(\mathbb R^p\), with \(B_0\) having \(d\) columns. Subspaces in the graph chart at \(\operatorname{span}(B_0)\) are represented by the columns of \(B_0+C_0K\), where \(K\in\mathbb R^{(p-d)\times d}\). Applying Gram-Schmidt in column order with positive normalization to this full-rank matrix gives a smooth orthonormal representative \(S(K)\): each successive normalization divides by a positive norm. Therefore the quotient function has the smooth coordinate expression \(F(S(K))\). These charts cover the Grassmannian. For \(d=p\), the Grassmannian consists of one point, so smoothness is immediate.

The Stiefel manifold is closed and bounded in finite-dimensional Euclidean space, hence compact. The smooth function \(F\) therefore attains its maximum, and \(Q=C-F\) attains its minimum. The optimization equivalence is consequently an equality of attained optimizer sets.

### 3. Differentiation

For one summand, write
\[
f(B)=\mu^TBM^{-1}B^T\mu,\qquad
M=B^TGB,\qquad v=B^T\mu,\qquad u=M^{-1}v.
\]
Differentiate its ambient extension on \(\mathcal U\). For a perturbation \(\Delta\in\mathbb R^{p\times d}\),
\[
dv[\Delta]=\Delta^T\mu,
\qquad dM[\Delta]=\Delta^TGB+B^TG\Delta.
\]
Differentiating \(MM^{-1}=I\) gives
\[
d(M^{-1})[\Delta]=-M^{-1}dM[\Delta]M^{-1}.
\]
Since \(G\) and \(M\) are symmetric,
\[
\begin{aligned}
df(B)[\Delta]
&=2\mu^T\Delta u-u^T(\Delta^TGB+B^TG\Delta)u\\
&=2(\mu-GBu)^T\Delta u\\
&=\operatorname{tr}\bigl([2(\mu-GBu)u^T]^T\Delta\bigr).
\end{aligned}
\]
Thus the Euclidean gradient of this extension is
\[
H=\nabla f(B)=2(\mu-GBu)u^T.
\]

### 4. Riemannian and quotient gradients

The tangent space to the Stiefel manifold is
\[
T_B\operatorname{St}(p,d)=\{\xi:B^T\xi+\xi^TB=0\}.
\]
Necessity follows by differentiating the orthonormality constraint. Conversely, for such a \(\xi\), orthonormalizing \(B+t\xi\) gives a curve with derivative \(\xi\) at zero, since its Gram matrix is \(I+t^2\xi^T\xi\). This verifies the tangent-space characterization.

By \(Mu=v\),
\[
B^TH=2(B^T\mu-B^TGBu)u^T=0.
\]
In particular, \(H\) is tangent. For every tangent \(\xi\), the differential calculation gives
\[
df(B)[\xi]=\operatorname{tr}(H^T\xi)=\langle H,\xi\rangle_B.
\]
This is precisely the defining property of the Riemannian gradient for the embedded Frobenius metric, so \(\operatorname{grad}f(B)=H\).

The vertical tangent vectors of the quotient map \(\pi(B)=\operatorname{span}(B)\) are \(B\Omega\), where \(\Omega^T=-\Omega\), obtained by differentiating the right action of \(O(d)\). Since \(B^TH=0\),
\[
\langle H,B\Omega\rangle_B=\operatorname{tr}(H^TB\Omega)=0.
\]
Thus \(H\) is horizontal. Let \(\widehat f\) denote the smooth descended function defined by \(\widehat f(\operatorname{span}(B))=f(B)\); the single-summand invariance and the smoothness argument in Section 2 establish that this is well-defined and smooth. For the induced quotient metric, the differential of \(\pi\) preserves inner products of horizontal lifts. If \(\eta\) is a Grassmannian tangent vector and \(\xi\) its horizontal lift, the chain rule gives
\[
d\widehat f[\eta]=df[\xi]=\langle H,\xi\rangle_B
=\langle d\pi_B(H),\eta\rangle_{\operatorname{Gr}}.
\]
Hence \(H\) is the horizontal representative of the Grassmannian gradient.

Summing the differentials and horizontal gradients over anchors gives
\[
\operatorname{grad}F(B)=2\sum_{j=1}^n\bigl(\mu^{(j)}-G^{(j)}Bu^{(j)}\bigr)u^{(j)T},
\qquad u^{(j)}=(B^TG^{(j)}B)^{-1}B^T\mu^{(j)}.
\]
Under \(B\mapsto BR\), one has \(u^{(j)}\mapsto R^Tu^{(j)}\), so the displayed gradient transforms as \(\operatorname{grad}F(BR)=\operatorname{grad}F(B)R\), consistently representing a quotient tangent vector.

All arguments allow zero individual weights and zero moment vectors. When \(d=p\), \(B\) is square orthogonal and \(B^T\operatorname{grad}F(B)=0\) implies \(\operatorname{grad}F(B)=0\), as required on a one-point Grassmannian.

## Source Audit Note

The source's invariance display at L001463 has a missing transpose on its first factor. The scalar quadratic form used in Section 2 above is the unique correction specified in the theory_008 proof-repair record. No theorem statement or assumption is changed. All theorem-critical obligations are proved above; no unresolved external or paper-specific dependency remains.
