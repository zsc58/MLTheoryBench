# Problem

## Setup

Let d≥1 and let G be a known directed acyclic graph on {1,…,d}. Write pa(i) for the parents of i in this graph, Pa(i)=pa(i)∪{i}, and an(i) for the proper ancestors of i. Thus a component depending on x_{Pa(i)} may depend on its own coordinate. All directed paths and topological orders below refer to G without self-loops.

Let p be a bounded positive probability density on R^d, and let X_1,…,X_n be iid with density p, where n≥3. Let D:R^d→R^{d×d} be a known bounded measurable symmetric positive-definite diffusivity, and let b*:R^d→R^d be an unknown bounded measurable drift. Assume b_i* depends only on x_{Pa(i)} and

\[
\int (b^*)^T\nabla\phi\,dp
=\frac12\int\langle D,\nabla^2\phi\rangle_F\,dp,
\qquad \phi\in C_c^\infty(\mathbb R^d),
\]

where \(\langle A,B\rangle_F=\sum_{a,b}A_{ab}B_{ab}\).

For each i, fix a bounded continuous symmetric positive-definite kernel k_i on R^{|Pa(i)|}, with RKHS H_i. Regard its functions as functions on R^d by projection onto Pa(i), and abbreviate the lifted kernel by k_i(x,y). Fix known functions K_{i,y}(x) depending only on (x_{Pa(i)},y_{Pa(i)}) such that

\[
\partial_{x_i}K_{i,y}(x)=k_i(x,y).
\]

Assume K and all its x-derivatives through order two are jointly continuous in (x,y) and satisfy

\[
\max_{i\le d}\max_{|\alpha|\le2}
\sup_{x,y\in\mathbb R^d}
|\partial_x^\alpha K_{i,y}(x)|<\infty.
\]

Let J_i:H_i→L²(p) be inclusion, let

\[
(J_i^*f)(y)=\int k_i(x,y)f(x)\,dp(x),
\qquad L_i=J_i^*J_i,
\]

and, for λ>0, define

\[
b_{i,\lambda}
=\operatorname*{argmin}_{h\in H_i}
\bigl(\|h-b_i^*\|_{L^2(p)}^2+\lambda\|h\|_{H_i}^2\bigr),
\qquad
T_i(\lambda)=\|b_{i,\lambda}-b_i^*\|_{L^2(p)}.
\]

Fix deterministic positive regularization sequences λ_i(n). Using the same n observations at every vertex, define estimates in a topological order as follows:

\[
\widehat z_i(x,y)
=\sum_{j\in\mathrm{pa}(i)}\widehat b_j(x)\,
\partial_{x_j}K_{i,y}(x)
-\frac12\sum_{a,b\in\mathrm{Pa}(i)}
D_{ab}(x)\,\partial_{x_a}\partial_{x_b}K_{i,y}(x),
\qquad
\widehat\zeta_i(y)=\frac1n\sum_{a=1}^n\widehat z_i(X_a,y).
\]

An empty sum is zero. Set

\[
\mathbf G_i=(k_i(X_a,X_b))_{a,b=1}^n,
\quad
\mathbf k_{i,y}=(k_i(y,X_a))_{a=1}^n,
\quad
\widehat{\boldsymbol\zeta}_i=(\widehat\zeta_i(X_a))_{a=1}^n,
\]

and define the estimator by

\[
\widehat b_i(y)
=\frac1{\lambda_i(n)}\mathbf k_{i,y}^{T}
(\mathbf G_i+n\lambda_i(n)I_n)^{-1}
\widehat{\boldsymbol\zeta}_i
-\frac1{\lambda_i(n)}\widehat\zeta_i(y).
\]

The empirical covariance operator on H_i is

\[
\widehat L_i h=\frac1n\sum_{a=1}^n h(X_a)k_i(X_a,\cdot).
\]

For j∈an(i), let d_{ji} be the longest directed-path length from j to i. Put d_{ii}=0,

\[
d_i=\max\bigl(\{0\}\cup\{d_{ji}:j\in\mathrm{an}(i)\}\bigr),
\qquad r_i=6\cdot3^{d_i}.
\]

## Task

Suppose that, for every vertex i and n≥3,

\[
\lambda_i(n)\ge n^{-2/r_i},
\qquad
\lambda_i(n)\ge
T_j(\lambda_j(n))^{2/3^{d_{ji}}}
\quad\text{for every }j\in\mathrm{an}(i).
\]

Prove that there are finite constants C_i, depending only on the fixed graph, dimension, and stated uniform bounds, and not on n or the admissible regularization values, such that

\[
\mathbb E\|\widehat b_i-b_i^*\|_{L^2(p)}
\le C_i\left[
(\log n)n^{-1/r_i}
+T_i(\lambda_i(n))
+\sum_{j\in\mathrm{an}(i)}
T_j(\lambda_j(n))^{1/3^{d_{ji}}}
\right].
\]

The expectation is over the training sample; the L²(p) norm is the population norm.

If each H_i is dense in L²(p_{Pa(i)}), where p_{Pa(i)} is the corresponding marginal density, prove that deterministic admissible schedules with λ_i(n)→0 exist, and that every such choice gives

\[
\mathbb E\|\widehat b_i-b_i^*\|_{L^2(p)}\longrightarrow0.
\]

Finally, suppose for each j that

\[
T_j(\lambda)=O\!\left(\sqrt\lambda\,
\log^{\alpha_j}(1/\lambda)\right)
\quad\text{as }\lambda\downarrow0,
\qquad \alpha_j\ge0.
\]

For any ε∈(0,1/(2d)), set ε_i=d_iε and

\[
\lambda_i(n)=n^{-2(1-\varepsilon_i)/r_i}.
\]

Show that these schedules satisfy the regularization lower bounds for all sufficiently large n, and derive

\[
\mathbb E\|\widehat b_i-b_i^*\|_{L^2(p)}
=O\!\left(n^{-(1-2\varepsilon_i)/r_i}
(\log n)^{q_i}\right)
\]

for some finite q_i≥0. Constants in this final rate may also depend on ε and the approximation-rate constants and exponents.
