# Problem

## Setup

Let \(n\ge2\) be an integer, and let the index set be \(\{0,\ldots,n-1\}\). For a nonnegative \(n\times n\) row-stochastic matrix \(A\), form the weighted undirected bipartite graph \(G(A)\) with left vertices \(L_0,\ldots,L_{n-1}\), right vertices \(R_0,\ldots,R_{n-1}\), and edge weight \(A_{ij}\) between \(L_i\) and \(R_j\). For a vertex set \(U\), let \(U^c\) denote its complement in the vertex set of \(G(A)\), let \(w_G(U,U^c)\) be its crossing edge weight, and let \(\operatorname{vol}(U)\) be the sum of weighted degrees of its vertices. When both \(\operatorname{vol}(U)\) and \(\operatorname{vol}(U^c)\) are positive, define
\[
\phi_G(U)=\frac{w_G(U,U^c)}{\min\{\operatorname{vol}(U),\operatorname{vol}(U^c)\}}.
\]

For an integer \(t\) with \(0<t<n\), define the temporal cut
\[
T_t=\{L_0,\ldots,L_{t-1}\}\cup\{R_0,\ldots,R_{t-1}\}.
\]
For \(c\in(0,1/2]\), call \(T_t\) \(c\)-balanced when \(\min\{t,n-t\}\ge cn\).

Fix a positive integer \(w\). Consider the following two causal row-stochastic matrices:
\[
A^{(w)}_{ij}=\frac{\mathbf{1}\{\max(0,i-w+1)\le j\le i\}}{\min(w,i+1)},
\qquad
A^{(u)}_{ij}=\frac{\mathbf{1}\{j\le i\}}{i+1}.
\]

## Task

Prove the following temporal-cut separation.

For every integer \(t\) with \(0<t<n\),
\[
\phi_{G(A^{(w)})}(T_t)\le\frac{w}{\min\{t,n-t\}},
\qquad
\phi_{G(A^{(u)})}(T_t)\ge\frac15.
\]
In particular, if \(n-t\le t\), then \(\phi_{G(A^{(w)})}(T_t)\le w/(n-t)\). For every fixed \(c\in(0,1/2]\), every \(c\)-balanced temporal cut satisfies \(\phi_{G(A^{(w)})}(T_t)\le w/(cn)\), whereas \(\phi_{G(A^{(u)})}(T_t)\ge1/5\).
