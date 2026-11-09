# Reference Proof

## Proof Structure

Construct one partial-symmetric third-order tensor from each covariance pair. Coefficient diversity and invertibility give the relevant Kruskal ranks. Establish the exact signed-factor uniqueness consequence directly by an orthogonal-congruence argument, including the possibility of singular individual covariance slices. Comparing an arbitrary simultaneous solution with the true one then gives two signed orthogonal-basis representations; transversality forces both sign patterns to be one common global sign.

## Complete Proof

Write the columns of \(U\) and \(V\) as \(u_i\) and \(v_i\), respectively. Let \(G\) be any real matrix satisfying all four covariance equations.

For each index \(i\), the coefficient pair \((\alpha_{1,i},\alpha_{2,i})\) is nonzero. Indeed, if both entries vanished, choosing any \(j\ne i\), possible since \(N\ge2\), would contradict the first coefficient-diversity condition. Nonnegativity therefore gives
\[
\alpha_{1,i}+\alpha_{2,i}>0.
\]
The same reasoning gives \(\alpha_{3,i}+\alpha_{4,i}>0\). Consequently \(X_1+X_2\) and \(X_3+X_4\) are positive definite. Since \(H\) is invertible,
\[
Y_1+Y_2=H(X_1+X_2)H^T
\]
is positive definite. Its alternative representation \(G(X_1+X_2)G^T\) implies that \(G\) is invertible as well.

For the first pair, form the order-three tensor whose two frontal slices are \(Y_1,Y_2\). With \(Q=HU\), it has the partial-symmetric decomposition
\[
\mathcal T_U(:,:,r)=Y_r
=Q\operatorname{diag}(\alpha_r)Q^T
=\sum_{i=1}^N\alpha_{r,i}q_iq_i^T,
\qquad r=1,2.
\]
The coefficient matrix has columns \((\alpha_{1,i},\alpha_{2,i})^T\). Its Kruskal rank is \(2\): every two columns are linearly independent by the first coefficient-diversity condition. Here Kruskal rank means the largest number of columns such that every subset of that size is linearly independent. Since \(Q\) is invertible, its Kruskal rank is \(N\). Thus the usual three-factor uniqueness threshold is met:
\[
N+N+2=2N+2.
\]
The second tensor, with slices \(Y_3,Y_4\) and repeated factor \(P=HV\), has the same rank properties.

For completeness, the exact signed-factor uniqueness consequence needed here follows from the following elementary argument, so the proof does not depend on an unstated external tensor theorem.

Suppose \(a,b\in\mathbb R_{\ge0}^N\) satisfy \(a_i b_j\ne a_j b_i\) for all \(i\ne j\), \(Q\) is invertible, and
\[
Z\operatorname{diag}(a)Z^T=Q\operatorname{diag}(a)Q^T,
\qquad
Z\operatorname{diag}(b)Z^T=Q\operatorname{diag}(b)Q^T.
\]
Set \(d_i=a_i+b_i\), \(D=\operatorname{diag}(d)\), and \(R=Q^{-1}Z\). As above, every \(d_i\) is positive. Adding the two equations yields
\[
RDR^T=D.
\]
Therefore \(W=D^{-1/2}RD^{1/2}\) satisfies \(WW^T=I_N\), so it is orthogonal. The first equation also gives
\[
WEW^T=E,
\qquad
E=\operatorname{diag}\left(\frac{a_i}{a_i+b_i}\right)_{i=1}^N.
\]
The diagonal entries of \(E\) are pairwise distinct: equality of entries \(i,j\), after multiplying by their positive denominators, is equivalent to \(a_i b_j=a_j b_i\). Multiplying \(WEW^T=E\) by \(W\) on the right gives \(WE=EW\). Entrywise, distinctness forces every off-diagonal entry of \(W\) to vanish. Orthogonality then makes each diagonal entry either \(1\) or \(-1\). Since \(W\) and \(D\) are diagonal,
\[
R=D^{1/2}WD^{-1/2}=W.
\]
Hence \(Z=QW\), establishing uniqueness up to column signs with the coefficient labels already fixed. This argument resolves both the scaling and permutation ambiguities that arise in a general tensor factorization.

Apply this result with \(a=\alpha_1\), \(b=\alpha_2\), \(Q=HU\), and \(Z=GU\). There is a diagonal sign matrix \(D_s\) such that
\[
GU=HU D_s,
\qquad
G=HU D_sU^T. \tag{1}
\]
Apply it again with \(a=\alpha_3\), \(b=\alpha_4\), \(Q=HV\), and \(Z=GV\). There is a diagonal sign matrix \(D_t\) such that
\[
G=HV D_tV^T. \tag{2}
\]
Comparing (1) and (2) and cancelling invertible \(H\) yields
\[
U D_sU^T=V D_tV^T. \tag{3}
\]

Let \(I=\{i:(D_s)_{ii}=1\}\) and \(J=\{j:(D_t)_{jj}=1\}\). For a subspace \(E\), denote its orthogonal projector by \(P_E\), with \(P_{\{0\}}=0\). Then
\[
U D_sU^T=2P_{\operatorname{span}\{u_i:i\in I\}}-I_N,
\]
and analogously for \(V,D_t\). Equation (3) implies equality of these projectors and therefore
\[
\operatorname{span}\{u_i:i\in I\}
=\operatorname{span}\{v_j:j\in J\}.
\]
Because both sets consist of orthonormal columns, their span dimensions are \(|I|\) and \(|J|\), so \(|I|=|J|\). If their common size were between \(1\) and \(N-1\), the equality would contradict transversality. It is therefore either \(0\) or \(N\). Thus either \(D_s=D_t=-I_N\) or \(D_s=D_t=I_N\). Equation (1) gives \(G=-H\) or \(G=H\).

Both matrices indeed satisfy all four equations, since a global sign cancels in each covariance congruence. This proves identifiability exactly up to a global sign.
