# Reference Proof

## Proof Structure

1. Use the data identity and rank condition to show that every feedback gain has an integrated-data representation and that the represented dynamics are exactly the corresponding closed loop.
2. Show that data Lyapunov evaluation equals model-based policy evaluation.
3. Reduce the constrained data Hamiltonian minimization to model-based minimization, identify its unique induced gain, and account for nonuniqueness of the representation matrix.
4. Identify the resulting gain and Lyapunov sequences with Kleinman's iteration and conclude stability, monotonicity, optimality, and convergence.

## Complete Proof

Let S=[\\tilde U;\\tilde X]. The data identity is \\bar X=A\\tilde X+B\\tilde U, and S has full row rank. Hence, for every K\\in\\mathbb R^{m\\times n}, the equation SG=[-K;I_n] has a solution G\\in\\mathbb R^{T\\times n}. For every such solution,
\\[
\\tilde XG=I_n,\\qquad \\bar XG=A\\tilde XG+B\\tilde UG=A-BK,
\\]
and K=-\\tilde UG. Conversely, any G with \\tilde XG=I_n induces K=-\\tilde UG and satisfies \\bar XG=A-BK. Thus \\bar XG is Hurwitz exactly when the induced gain is stabilizing.

For a stabilizing G, put A_G=\\bar XG and K_G=-\\tilde UG. The data evaluation equation is
\\[
A_G^TP_G+P_GA_G+Q+K_G^TRK_G=0.
\\]
Since A_G is Hurwitz, it has a unique symmetric solution. By the identities above this is precisely the model Lyapunov equation for the gain K_G, so P_G is the model value matrix.

Fix a symmetric positive semidefinite matrix P. The improvement objective is
\\[
J_P(G)=\\operatorname{tr}\\!\\left(Q+G^T\\tilde U^TR\\tilde UG+P\\bar XG+G^T\\bar X^TP\\right)
\\]
subject to \\tilde XG=I_n. For a feasible G, writing K=-\\tilde UG and using \\bar XG=A-BK gives
\\[
J_P(G)=\\operatorname{tr}\\!\\left(Q+K^TRK+P(A-BK)+(A-BK)^TP\\right).
\\]
The full-row-rank property makes every K attainable, so minimizing over feasible G is equivalent to minimizing this expression over K. Completing the square (or differentiating) yields the unique minimizer
\\[
K^+=R^{-1}B^TP.
\\]
Therefore every minimizing representation has induced gain -\\tilde UG=K^+. Choose the minimum-Frobenius-norm feasible minimizer. Since S has full row rank, it is G=S^\\dagger[-K^+;I_n]; all other solutions differ by a matrix in \\ker S, and hence induce the same gain.

Start with G_0 such that \\tilde XG_0=I_n and A_{G_0} is Hurwitz. At iteration k, solve the data Lyapunov equation for P_k, then choose the minimum-norm minimizer for J_{P_k}, obtaining G_{k+1}. By the preceding reduction, the induced gains satisfy
\\[
K_{k+1}=R^{-1}B^TP_k,
\\]
while P_k is the Lyapunov solution for K_k. Thus (K_k,P_k) is exactly the model-based Kleinman iteration. Under the stated stabilizability and detectability assumptions, its standard convergence result gives that every A-BK_k is Hurwitz, P^*\\preceq P_{k+1}\\preceq P_k, and K_k\\to K^*, P_k\\to P^*. Here P^* is the unique positive-semidefinite stabilizing solution of the CARE. Consequently every G_k remains feasible and stabilizing. Finally, the minimum-norm representation is the continuous affine map K\\mapsto S^\\dagger[-K;I_n], so G_k\\to G^*=S^\\dagger[-K^*;I_n], which is a feasible optimal representation and induces K^*.
