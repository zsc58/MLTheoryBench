# Problem

## Setup

Let \(m\ge n\) and let \(M\in\mathbb R^{n\times m}\) have rank \(r\). A rank-aware triangularization operator returns \(L=T(M)\in\mathbb R^{n\times n}\) such that
\[
LL^T=MM^T,
\qquad
L=\begin{bmatrix}L_1&0\\L_2&0\end{bmatrix},
\]
where \(L_1\in\mathbb R^{r\times r}\) is lower triangular with nonnegative diagonal and \(L_2\) is arbitrary. Choose any \(Q\in\mathbb R^{m\times n}\) with \(Q^TQ=I_n\) and \(M=LQ^T\).

Let \(\ell\) be a smooth scalar loss that depends on a triangularization output only through its Gramian: there is a smooth \(\widetilde\ell\) with \(\ell(Z)=\widetilde\ell(ZZ^T)\). For a perturbation \(\dot M\), define the Moore--Penrose inverse \(L^\dagger\), projectors \(P=LL^\dagger\), \(P^\perp=I-P\),
\[
K=L^\dagger\dot M Q,
\qquad
A=\operatorname{tril}(K+K^T)-\operatorname{diag}(K),
\]
where \(\operatorname{tril}\) retains the diagonal, and set
\[
\dot L= L A+P^\perp\dot M Q.
\]

## Task

Prove that, for every rank \(r\) and every perturbation \(\dot M\), the surrogate tangent satisfies
\[
\dot L L^T+L\dot L^T=\dot M M^T+M\dot M^T,
\]
and consequently computes the exact forward-mode JVP of the composite loss:
\[
D(\ell\circ T)(M)[\dot M]
 =D\widetilde\ell(MM^T)[\dot M M^T+M\dot M^T]
 =D\widetilde\ell(LL^T)[\dot L L^T+L\dot L^T].
\]
Finally, show that when \(L\) is invertible the null-space correction vanishes and the construction reduces to the classical full-rank rule.
