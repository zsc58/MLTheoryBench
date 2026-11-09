# Reference Proof

## Proof Structure

First restrict the skew generator to the query-key column space and expand its exponential in an orthonormal basis. Then analyze the finite normalized matrix: expand its orthogonality defect, use a full rectangular SVD, and explicitly factor the exponential increment to isolate the singular-value error factor.

## Complete Proof

### 1. Exact subspace reduction

Let \(U=\operatorname{span}(\operatorname{col}Q,\operatorname{col}K)\) and \(r=\dim U\). Since \(U\) is spanned by the \(2d_v\) columns of \([Q,K]\), \(r\le\min(N,2d_v)\). The displayed formula for \(S\) shows that \(S^\top=-S\), that its range is contained in \(U\), and that \(Sx=0\) for every \(x\in U^\perp\): indeed, both \(Q^\top x\) and \(K^\top x\) vanish.

For an orthonormal basis matrix \(C\) of \(U\), the matrix \(CC^\top\) is its orthogonal projector. Consequently
\[
S=CC^\top S CC^\top=C(C^\top SC)C^\top.
\]
Writing \(H_C=C^\top SC\), induction using \(C^\top C=I_r\) gives
\[
S^n=CH_C^nC^\top\qquad(n\ge1).
\]
The matrix exponential series converges absolutely in operator norm, so
\[
e^S=I_N+\sum_{n=1}^\infty\frac{CH_C^nC^\top}{n!}
=I_N+C(e^{H_C}-I_r)C^\top.
\]
If \(r=0\), the query and key matrices are zero, hence \(S=0\), and the same formula holds with the stated empty-matrix convention. There is no need for \(\operatorname{rank}(S)=r\).

### 2. Finite-iterate singular values

Set \(m=2d_v\) and \(p=\min(N,m)\). The positive \(\epsilon\) makes \(M_0=M/(\|M\|_F+\epsilon)\) defined even when \(M=0\). The singular values of \(M_0\) satisfy
\[
0\le\sigma_i(M_0)\le\frac{\|M\|_F}{\|M\|_F+\epsilon}<1.
\]
To verify that the construction meets the public singular-value assumption, substitute a full rectangular SVD \(M_k=P_k\Sigma_k V_k^\top\) into the update. This gives
\[
M_{k+1}=P_k\,\frac12\Sigma_k(3I_m-\Sigma_k^\top\Sigma_k)V_k^\top.
\]
Thus a singular value \(t\in[0,1]\) becomes \(f(t)=t(3-t^2)/2\). On this interval \(f(t)\ge0\), and
\[
1-f(t)=\frac{(1-t)^2(t+2)}2\ge0.
\]
Every finite iterate therefore has singular values in \([0,1]\), including zero singular values. In particular \(\|B\|_2\le1\). No polar convergence theorem or full-rank assumption is required. For the requested inequalities this fact may also be invoked directly from the explicit public assumption.

### 3. Orthogonality-defect identity

Put
\[
G=B^\top SB,\qquad \Delta=e^G-I_m,\qquad E=B^\top B-I_m.
\]
Since \(S\) is skew-symmetric, so is \(G\). The exponential series gives \((e^G)^\top=e^{-G}\), and multiplication of the absolutely convergent series gives \(e^{-G}e^G=I_m\). Hence
\[
\Delta+\Delta^\top+\Delta^\top\Delta=0.
\]
Expanding \(Y=I_N+B\Delta B^\top\) now yields
\[
\begin{aligned}
Y^\top Y-I_N
&=B\bigl(\Delta+\Delta^\top+\Delta^\top(B^\top B)\Delta\bigr)B^\top\\
&=B\Delta^\top E\Delta B^\top.
\end{aligned}
\]
All rightmost factors in this expansion are \(B^\top\).

### 4. Explicit compressed-series factorization

Take a full rectangular SVD
\[
B=P\Sigma V^\top,
\]
where \(P\in\mathbb R^{N\times N}\) and \(V\in\mathbb R^{m\times m}\) are orthogonal and \(\Sigma\in\mathbb R^{N\times m}\) is rectangular diagonal. Define
\[
H=P^\top SP,\qquad D=\Sigma\Sigma^\top,\qquad
\widehat E=\Sigma^\top\Sigma-I_m,
\qquad \widehat\Delta=e^{\Sigma^\top H\Sigma}-I_m.
\]
Orthogonal conjugation of the exponential series gives
\[
\Delta=V\widehat\Delta V^\top,\qquad E=V\widehat E V^\top.
\]
For every \(n\ge1\), direct multiplication gives
\[
(\Sigma^\top H\Sigma)^n
=\Sigma^\top(HD)^{n-1}H\Sigma.
\]
Define the \(N\)-by-\(N\) matrix
\[
\Psi=\sum_{n=1}^{\infty}\frac{(HD)^{n-1}H}{n!}.
\]
Here the zeroth matrix power is the identity. Since \(\|D\|_2=\|\Sigma\|_2^2\le1\) and \(\|H\|_2=\|S\|_2\), the terms satisfy
\[
\|(HD)^{n-1}H\|_2\le\|S\|_2^n.
\]
This includes \(n=1\), and if \(S=0\) every term is zero. The series is therefore absolutely convergent and
\[
\|\Psi\|_2\le\sum_{n=1}^{\infty}\frac{\|S\|_2^n}{n!}=e^{\|S\|_2}-1.
\]
Termwise substitution in the exponential series proves
\[
\widehat\Delta=\Sigma^\top\Psi\Sigma.
\]
This is a factorization, not a claim that the SVD diagonalizes \(\Delta\).

### 5. Spectral estimate and scalar maximum

Substituting the preceding identities into the defect gives
\[
\begin{aligned}
Y^\top Y-I_N
&=P\Sigma\widehat\Delta^\top\widehat E\widehat\Delta\Sigma^\top P^\top\\
&=P D\Psi^\top\Sigma\widehat E\Sigma^\top\Psi D P^\top.
\end{aligned}
\]
Orthogonal invariance and submultiplicativity of the operator norm imply
\[
\begin{aligned}
\|Y^\top Y-I_N\|_2
&\le\|\Sigma\|_2^4\|\Psi\|_2^2
\|\Sigma(\Sigma^\top\Sigma-I_m)\Sigma^\top\|_2\\
&\le(e^{\|S\|_2}-1)^2
\|\Sigma(\Sigma^\top\Sigma-I_m)\Sigma^\top\|_2.
\end{aligned}
\]
The final matrix is diagonal. Its first \(p\) diagonal entries are \(\sigma_i(B)^2(\sigma_i(B)^2-1)\); any remaining diagonal entries are zero. Therefore
\[
\|Y^\top Y-I_N\|_2
\le(e^{\|S\|_2}-1)^2
\max_{1\le i\le p}|\sigma_i(B)^2(\sigma_i(B)^2-1)|.
\]
For \(t\in[0,1]\),
\[
|t(t-1)|=t(1-t)=\frac14-(t-\tfrac12)^2\le\frac14.
\]
Apply this with \(t=\sigma_i(B)^2\) to obtain the second inequality.

The index set is nonempty because \(N\ge1\) and \(m=2d_v\ge2\). If \(M=0\), all iterates vanish and \(Y=I_N\). If \(S=0\), including when \(\alpha=0\) with nonzero query/key matrices, then \(G=0\) and again \(Y=I_N\). These cases are also covered by the displayed estimates. All theorem-critical obligations are closed.
