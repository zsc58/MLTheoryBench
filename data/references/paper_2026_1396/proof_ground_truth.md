# Reference Proof

## Proof Structure

First factor the loss through the Gramian, so its composite with the triangularization operator is smooth even when the factor is nonunique. Differentiate the two Gramian identities and show that any surrogate tangent satisfying the resulting identity gives the exact directional derivative. Finally verify the stated surrogate tangent by splitting it into column-space and null-space components.

## Complete Proof

Let \(\Sigma=LL^T=MM^T\). By the Gramian-dependence assumption there is a \(C^1\) function \(\widetilde\ell\) such that \(\ell(Z)=\widetilde\ell(ZZ^T)\) for the triangularization outputs under consideration. Hence
\[
 \ell(T(M))=\widetilde\ell(MM^T),
\]
and the right-hand side is smooth in \(M\), since \(M\mapsto MM^T\) is polynomial. Therefore, for any direction \(\dot M\),
\[
 D(\ell\circ T)(M)[\dot M]
 =D\widetilde\ell(\Sigma)[\dot M M^T+M\dot M^T].
\]

Suppose \(\dot L\) satisfies
\[
 \dot L L^T+L\dot L^T=\dot M M^T+M\dot M^T. \tag{1}
\]
The chain rule applied to \(\widetilde\ell(LL^T)\) gives
\[
 D\widetilde\ell(\Sigma)[\dot L L^T+L\dot L^T]
 =D\widetilde\ell(\Sigma)[\dot M M^T+M\dot M^T],
\]
so propagating \(\dot L\) through the Gramian-dependent loss yields the exact JVP.

It remains to verify the explicit construction. Let \(P=LL^\dagger\) and \(P^\perp=I-P\), and choose \(Q\) with \(Q^TQ=I\) and \(M=LQ^T\). The standard Moore--Penrose identities give \(P^T=P\), so \(P\) is the orthogonal projector onto \(\operatorname{col}(L)\). Set
\[
 K=L^\dagger\dot M Q,\qquad
 A=\operatorname{tril}(K+K^T)-\operatorname{diag}(K),
\]
\[
 \dot L_{\rm col}=LA,\qquad \dot L_{\rm null}=P^\perp\dot M Q,
 \qquad \dot L=\dot L_{\rm col}+\dot L_{\rm null}.
\]
Because \(A+A^T=K+K^T\),
\[
\begin{aligned}
 \dot L_{\rm col}L^T+L\dot L_{\rm col}^T
 &=L(K+K^T)L^T\\
 &=P\dot M M^T+M\dot M^T P.
\end{aligned}
\]
Here \(LKL^T=LL^\dagger\dot M QL^T=P\dot M M^T\), using \(M^T=QL^T\), and the transpose term uses \(P^T=P\). Also,
\[
 \dot L_{\rm null}L^T+L\dot L_{\rm null}^T
 =P^\perp\dot M M^T+M\dot M^T P^\perp,
\]
again using \(M^T=QL^T\) and \(Q^T L^T=M\). Adding these two equalities and using \(P+P^\perp=I\) proves (1). The preceding argument therefore proves exactness of the surrogate JVP at every rank. If \(L\) is invertible, then \(P=I\), \(P^\perp=0\), and the null-space term vanishes, leaving the usual full-rank triangular/QR differential rule.
