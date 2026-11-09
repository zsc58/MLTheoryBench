# Reference Proof

## Proof Structure

First dispose of the case in which the higher-rank space is zero. Establish positive semidefiniteness of the graded block operator from its adjacent-rank quadratic forms. Use that decomposition on the higher-order principal block to show that every vector in its kernel is annihilated by the vertex-to-higher-order coupling. Diagonalize the higher-order block, cancel its kernel contribution in the regularized inverse, and compare the remaining eigenvalue coefficients to obtain the error bound and limiting statements.

## Complete Proof

If $H=\{0\}$, then $X$ is the zero map from $H$ to the vertex space. The endomorphisms of $H$, including its identity, inverse identity, and Moore–Penrose inverse, are interpreted on the zero space. Both correction products therefore vanish, so $S_\epsilon=S^\dagger=A$ for every $\epsilon>0$. There are no positive eigenvalues of $C$, and all claimed conclusions follow. This includes $K=0$. Henceforth suppose $H\ne\{0\}$, so $K\ge1$.

For $x=(x_0,\ldots,x_K)$, direct expansion of the block-tridiagonal matrix gives
\[
x^\top L^*x=\sum_{k=0}^{K-1}Q_k(x_k,x_{k+1}),
\]
where
\[
Q_k=\beta_{k+1}\|B_{k+1}^\top x_k\|^2+\beta_{k+1}\|B_{k+1}x_{k+1}\|^2-2\gamma_kx_k^\top B_{k+1}x_{k+1}.
\]
Take an SVD $B_{k+1}=U\Sigma V^\top$, with $U,V$ orthogonal. In a positive singular direction $\sigma$, with coordinates $a,b$, the contribution is
\[
\sigma\begin{pmatrix}a&b\end{pmatrix}
\begin{pmatrix}\beta_{k+1}\sigma&-\gamma_k\\-\gamma_k&\beta_{k+1}\sigma\end{pmatrix}
\binom a b.
\]
The inner $2\times2$ matrix has eigenvalues $\beta_{k+1}\sigma-\gamma_k$ and $\beta_{k+1}\sigma+\gamma_k$. They are nonnegative under the stated condition, because every positive singular value is at least $\sigma_{\min}^+(B_{k+1})$. Null singular directions contribute zero. If $B_{k+1}=0$, the entire $Q_k$ is zero, regardless of $\gamma_k$. Consequently every $Q_k$ is nonnegative and $L^*\succeq0$.

For every $v\in H$,
\[
v^\top Cv=\binom0v^\top L^*\binom0v\ge0,
\]
so $C\succeq0$. In particular, for $\epsilon>0$ and nonzero $v$,
\[
v^\top(C+\epsilon I)v\ge\epsilon\|v\|^2>0.
\]
Thus the inverse in the definition of $S_\epsilon$ exists.

The full coupling matrix is
\[
X=[-\gamma_0B_1,\,0,\ldots,0],
\]
with the remaining blocks corresponding to ranks $2,\ldots,K$. Let $v=(v_1,\ldots,v_K)\in\ker C$. Setting the vertex component to zero in the preceding decomposition gives
\[
0=v^\top Cv=\beta_1\|B_1v_1\|^2+\sum_{k=1}^{K-1}Q_k(v_k,v_{k+1}),
\]
where every summand is nonnegative. If $\beta_1>0$, then $B_1v_1=0$. If $\beta_1=0$ and $B_1\ne0$, the weight condition forces $\gamma_0=0$. If $B_1=0$, the full coupling matrix $X$ is zero directly. Hence in every case
\[
Xv=-\gamma_0B_1v_1=0,
\qquad \ker C\subseteq\ker X.
\]

If $C$ has no positive eigenvalues, its symmetry and positive semidefiniteness give $C=0$. Its kernel is then all of $H$, so the kernel inclusion gives $X=0$. Therefore $S_\epsilon=S^\dagger=A$ for every $\epsilon>0$.

Otherwise, let $\lambda_i>0$ be the positive eigenvalues of $C$, with orthonormal eigenvectors $u_i$, and let $P_0$ be the orthogonal projector onto $\ker C$. The spectral decomposition gives
\[
(C+\epsilon I)^{-1}=\sum_i(\lambda_i+\epsilon)^{-1}u_iu_i^\top+\epsilon^{-1}P_0,
\qquad
C^\dagger=\sum_i\lambda_i^{-1}u_iu_i^\top.
\]
Since $XP_0=0$, the kernel term disappears after multiplication by $X$ and $X^\top$. Consequently
\[
S_\epsilon-S^\dagger
=X\left[\sum_i\frac{\epsilon}{\lambda_i(\lambda_i+\epsilon)}u_iu_i^\top\right]X^\top.
\]
The operator in brackets is diagonal in an orthonormal eigenbasis, with its displayed nonnegative coefficients on the positive eigenspace and zero on the kernel. Its operator norm is therefore the largest displayed coefficient. Since $\lambda_i\ge\lambda_+>0$,
\[
\frac{\epsilon}{\lambda_i(\lambda_i+\epsilon)}
\le\frac{\epsilon}{\lambda_+(\lambda_++\epsilon)}.
\]
Submultiplicativity and $\|X^\top\|_2=\|X\|_2$ now give
\[
\|S_\epsilon-S^\dagger\|_2\le
\frac{\epsilon\|X\|_2^2}{\lambda_+(\lambda_++\epsilon)}.
\]
For the fixed complex and weights, the right side tends to zero as $\epsilon\downarrow0$. Together with the zero-positive-spectrum case, this proves the asserted operator-norm convergence. Finally, when $C$ is nonsingular, its Moore–Penrose pseudoinverse equals its inverse, so the limit is $A-XC^{-1}X^\top$.
