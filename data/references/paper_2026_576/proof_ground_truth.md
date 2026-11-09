# Reference Proof

## Proof Structure

Solve the linear reverse ODE explicitly, decompose the initial matrix into its constant projector and orthogonal component, then diagonalize the Laplacian. The zero row and column sums eliminate all modes involving the zero eigenvalue, so every remaining mode is amplified by at least the spectral-gap factor. Frobenius orthogonality to the projector gives the stated bound for the full terminal state.

## Complete Proof

Let \(X(t)=e^{tTL}X_0e^{tTL}\). Since \(L\) commutes with its exponential,
\[
\frac{d}{dt}X(t)=T(LX(t)+X(t)L),\qquad X(0)=X_0,
\]
so \(X_1=X(1)=e^{TL}X_0e^{TL}\).

Write \(X_0=\Pi+X_\perp\), where \(\mathbf 1^TX_\perp=0\) and \(X_\perp\mathbf 1=0\). Because \(L\mathbf 1=0\) and \(\Pi=\mathbf 1\mathbf 1^T/n\), \(e^{TL}\Pi e^{TL}=\Pi\). Hence
\[
X_1=\Pi+Z,\qquad Z=e^{TL}X_\perp e^{TL}.
\]
Moreover, \(Z\mathbf 1=0\) and \(\mathbf 1^TZ=0\), so \(Z\) is Frobenius-orthogonal to \(\Pi\). Therefore
\[
\|X_1\|_F^2=\|\Pi\|_F^2+\|Z\|_F^2\geq \|Z\|_F^2.
\]

By the real spectral theorem, choose an orthogonal \(U\) with first column \(\mathbf 1/\sqrt n\) and
\[
L=U\,\operatorname{diag}(\lambda_1,\ldots,\lambda_n)\,U^T,
\qquad 0=\lambda_1<\lambda_2\leq\cdots\leq\lambda_n.
\]
Set \(B=U^TX_\perp U\). The zero row and column sums imply \(B_{1j}=B_{i1}=0\) for all \(i,j\). Thus
\[
\|Z\|_F^2
=\sum_{i,j}e^{2T(\lambda_i+\lambda_j)}|B_{ij}|^2
=\sum_{i,j\geq2}e^{2T(\lambda_i+\lambda_j)}|B_{ij}|^2.
\]
For \(i,j\geq2\), \(\lambda_i+\lambda_j\geq2\lambda_2\), and therefore
\[
\|Z\|_F^2\geq e^{4T\lambda_2}\sum_{i,j\geq2}|B_{ij}|^2
=e^{4T\lambda_2}\|X_\perp\|_F^2.
\]
Taking square roots and combining with the preceding inequality yields
\[
\boxed{\|X_1\|_F\geq e^{2T\lambda_2}\|X_\perp\|_F}.
\]
This proves the claim.
