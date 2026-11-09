# Reference Proof

## Proof Structure

First show that the PSD probe values and the matrix summary determine one another. Then show that the trace-scaled matrices are positive definite and use the log-spectrum distance to obtain a Loewner-order sandwich. Finally, test that sandwich against every PSD probe and rewrite its constants using the similarity score.

## Complete Proof

For any representation map \(u\), the matrix
\[
K_u=\mathbb E_{s\sim\nu}\left[P^T J_{u\circ\psi}(s)^T\Sigma^{-1}J_{u\circ\psi}(s)P\right]
\]
is symmetric positive semidefinite: each integrand has the form \(X^T\Sigma^{-1}X\), hence is PSD. By the definition of \(T_C\), \(K_u\) determines every task value, since \(T_C(u)=\operatorname{Tr}(CK_u)\).

Conversely, suppose \(T_C(f)=T_C(g)\) for every \(C\succeq0\). Put \(D=K_f-K_g\). Then \(D\) is symmetric and
\[
\operatorname{Tr}(CD)=0\quad\text{for every }C\succeq0.
\]
For every \(v\in\mathbb R^k\), the rank-one matrix \(C=vv^T\) is PSD, so
\[
v^TDv=\operatorname{Tr}(vv^TD)=0.
\]
A symmetric matrix whose quadratic form vanishes on every vector is zero (for example, apply the identity to the standard basis and to \(e_i+e_j\)). Thus \(D=0\), or \(K_f=K_g\). This proves the asserted completeness and minimality in the stated sense.

Because \(K_f\) and \(K_g\) are nonzero PSD matrices, their traces are positive. Hence
\[
H_u=K_u+\lambda\frac{\operatorname{Tr}(K_u)}{k}I_k
\]
is SPD for \(u=f,g\). Let
\[
d=d(H_f,H_g),\qquad M=H_f^{-1/2}H_gH_f^{-1/2}.
\]
The matrix \(M\) is SPD. If its eigenvalues are \(\mu_1,\ldots,\mu_k\), then
\[
d^2=\sum_{i=1}^k(\log\mu_i)^2.
\]
Therefore \(|\log\mu_i|\le d\) for every \(i\), and consequently
\[
e^{-d}\le\mu_i\le e^d.
\]
The spectral theorem gives \(e^{-d}I_k\preceq M\preceq e^dI_k\). Congruencing by \(H_f^{1/2}\) yields
\[
e^{-d}H_f\preceq H_g\preceq e^dH_f.\tag{1}
\]

Let \(C\succeq0\). Congruencing (1) by \(C^{1/2}\) preserves the Loewner inequalities, and taking traces preserves them because the trace of a PSD matrix is nonnegative. Thus
\[
e^{-d}\operatorname{Tr}(CH_f)
\le \operatorname{Tr}(CH_g)
\le e^d\operatorname{Tr}(CH_f).
\]
Equivalently,
\[
e^{-d}U_C(f)\le U_C(g)\le e^dU_C(f).\tag{2}
\]
Finally, \(\delta=d/\sqrt{k}\) and \(R=e^{-\delta}\), so \(e^{-d}=R^{\sqrt{k}}\) and \(e^d=R^{-\sqrt{k}}\). Substitution into (2) proves the required uniform certificate for every PSD \(C\).
