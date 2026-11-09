# Problem

## Setup

Let \(F:D\to\mathbb R\) and \(G_i:D\to\mathbb R\) \((i=1,\dots,m)\) be differentiable convex functions on the box
\[
D=\prod_{j=1}^n[\ell_j,u_j],\qquad \ell_j\le u_j.
\]
Consider the convex program
\[
\min_{x\in D}F(x)\quad\text{subject to}\quad G_i(x)\le b_i\quad(i=1,\dots,m).
\]
Let \(Q\) be a partition of the variable indices \(\{1,\dots,n\}\), and \(P\) a partition of the constraint indices \(\{1,\dots,m\}\). Assume the following equalities of the problem data:

- If \(j,k\in T\in Q\), then \(\ell_j=\ell_k\) and \(u_j=u_k\). Write \(\ell_T,u_T\) for these common bounds.
- If \(i,i'\in S\in P\), then \(b_i=b_{i'}\).

Assume further that the following conditions hold for every \(x\in D\) that is constant on each set \(T\in Q\):

1. For any \(j,k\in T\in Q\), \(\partial_jF(x)=\partial_kF(x)\).
2. For every constraint color \(S\in P\), with \(H_S(x)=\sum_{i\in S}G_i(x)\), and any \(j,k\in T\in Q\), \(\partial_jH_S(x)=\partial_kH_S(x)\).
3. If \(i,i'\in S\in P\), then \(G_i(x)=G_{i'}(x)\).

For \(x\in D\), define the color average \(A_Qx\) by \((A_Qx)_T=|T|^{-1}\sum_{j\in T}x_j\). For a reduced vector \(y=(y_T)_{T\in Q}\), define its lift \(L_Qy\in\mathbb R^n\) by \((L_Qy)_j=y_T\) for \(j\in T\). Choose one representative \(i_S\in S\) for each \(S\in P\). The reduced program is
\[
\min_y F(L_Qy)\quad\text{subject to}\quad G_{i_S}(L_Qy)\le b_{i_S}\ (S\in P),\qquad \ell_T\le y_T\le u_T\ (T\in Q).
\]

## Task

Prove that the reduced objective and all reduced constraint functions are convex, and that optimal solutions correspond exactly in both directions: if \(x^*\) is optimal for the original program, then \(A_Qx^*\) is optimal for the reduced program; conversely, if \(y^*\) is optimal for the reduced program, then \(L_Qy^*\) is optimal for the original program.
