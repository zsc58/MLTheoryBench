# Reference Proof

## Proof Structure

Pass to Euclidean coordinates for the weighted inner product. First bound the error of projection onto the exact bottom spectral subspace using the Poisson equation and the inverse of the symmetrized transition operator. Then convert the learned features' objective excess into a projector bound across the cutoff eigengap. Finally, apply the triangle inequality between the two projections.

## Complete Proof

Write \(D=I-P\), \(R=(P+P^\dagger)/2\), and \(T=W^{1/2}\). Thus \(H=I-R=\operatorname{sym}_W(D)\), and
\[
 A:=THT^{-1}
\]
is symmetric positive semidefinite. The map \(T\) is an isometry from the \(W\)-norm to the Euclidean norm.

Let \(V=\{f:\pi^T f=0\}\). Since \(\pi^T g=0\), both \(g\) and \(v\) belong to \(V\). The restrictions of \(D\) and \(H\) to \(V\) are invertible. Indeed, stationarity makes \(V\) invariant. The only fixed vectors of the irreducible finite chain are constants, so \(D\) has trivial kernel on \(V\). Also, the additive reversiblization has the same constant nullspace for its Laplacian, so \(H\) is positive definite on \(V\). In particular, \(\lambda_2>0\), and \(Tv\) is orthogonal to \(\ker A\).

Let \(U=\operatorname{span}\{q_1,\ldots,q_k\}\), and put \(v_k=\Pi_U^W v\). In Euclidean coordinates, \(Tv_k\) is the orthogonal projection of \(Tv\) onto the first \(k\) eigenvectors of \(A\). The spectral expansion therefore gives
\[
 \|v-v_k\|_W^2
 \le \frac{\langle v,Hv\rangle_W}{\lambda_{k+1}}.
\]
The Poisson equation \(Dv=g\) and \(H=\operatorname{sym}_W(D)\) imply
\[
 \langle v,Hv\rangle_W=\langle v,Dv\rangle_W=\langle v,g\rangle_W.
\]
On \(V\), write \(v=D^{-1}g\). Taking the symmetric part inside this scalar quadratic form yields
\[
 \langle v,g\rangle_W
 =\langle g,\operatorname{sym}_W(D^{-1})g\rangle_W.
\]
After conjugation by \(T\), the symmetric part of \(D\) is positive definite. The standard inverse symmetric-part inequality consequently gives
\[
 \operatorname{sym}_W(D^{-1})\preceq H^{-1}\quad\text{on }V.
\]
Since the smallest eigenvalue of \(H\) on \(V\) is \(\lambda_2\),
\[
 \langle v,Hv\rangle_W
 \le \langle g,H^{-1}g\rangle_W
 \le \frac{\|g\|_W^2}{\lambda_2}.
\]
Combining the last two displays gives
\[
 \|v-v_k\|_W\le \frac{\|g\|_W}{\sqrt{\lambda_2\lambda_{k+1}}}. \tag{1}
\]

It remains to control the learned subspace. Let \(Q\) have as columns the Euclidean eigenvectors \(Tq_1,\ldots,Tq_k\), and let \(Y\) have columns \(T\widehat q_1,\ldots,T\widehat q_k\). Both matrices have orthonormal columns. Put \(\delta=\lambda_{k+1}-\lambda_k>0\). Diagonalizing \(A\) in the basis extending \(Q\), the variational energy excess satisfies
\[
 \operatorname{tr}(Y^TAY)-\sum_{i=1}^k\lambda_i
 \ge \delta\,\|(I-QQ^T)Y\|_F^2.
\]
The assumed feature inequality thus gives
\[
 \|(I-QQ^T)Y\|_F^2<\frac{\epsilon}{\delta}.
\]
For equal-dimensional Euclidean subspaces, the standard projector-angle identities imply
\[
 \|QQ^T-YY^T\|_2
 \le \|QQ^T-YY^T\|_F
 =\sqrt{2}\,\|(I-QQ^T)Y\|_F
 <\sqrt{\frac{2\epsilon}{\delta}}. \tag{2}
\]
Conjugating the two Euclidean projectors by \(T^{-1}\) identifies them with \(\Pi_U^W\) and \(\Pi_{\widehat U}^W\), respectively, and preserves their operator norm in the corresponding weighted norm. Hence
\[
 \|\Pi_U^W-\Pi_{\widehat U}^W\|_{W\to W}
 <\sqrt{\frac{2\epsilon}{\lambda_{k+1}-\lambda_k}}. \tag{3}
\]

Finally, \(\widehat v=\Pi_{\widehat U}^Wv\), whereas \(v_k=\Pi_U^Wv\). Therefore, by (1) and (3),
\[
\begin{aligned}
 \|v-\widehat v\|_W
 &\le \|v-v_k\|_W+\|(\Pi_U^W-\Pi_{\widehat U}^W)v\|_W\\
 &\le \frac{\|g\|_W}{\sqrt{\lambda_2\lambda_{k+1}}}
 +\|v\|_W\sqrt{\frac{2\epsilon}{\lambda_{k+1}-\lambda_k}}.
\end{aligned}
\]
This is the claimed bound.
