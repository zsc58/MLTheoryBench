# Reference Proof

## Proof Structure and Obligations

The proof closes six obligations: the exact small-matrix representation; its operation count; existence and uniqueness of the metric projection; the active-case scalar equation and its unique positive root; the projection and thin-decomposition costs, including zero-rank factors; and the aggregate working-space and time bounds. The reductions are deterministic and conditional on the supplied factors. They require no confidence, regret, sampling, or specialized external result.

## Complete Proof

### 1. Exact spectral compression

Write the columns of \(U_t\) as \(u_1,\ldots,u_m\), with block decomposition \(u_j=(u_{j1}^\top,\ldots,u_{jK}^\top)^\top\). Orthonormality implies \(m\le n\). Complete these columns to an orthonormal basis of \(\mathbb R^n\), solely for this mathematical argument. In this basis, \(H_t\) has eigenvalue \(\lambda+\mu_j\) along \(u_j\) and eigenvalue \(\lambda\) on \(\operatorname{col}(U_t)^\perp\). All these eigenvalues are positive. Therefore
\[
H_t^{-1}=\lambda^{-1}I_n+\sum_{j=1}^m\left((\lambda+\mu_j)^{-1}-\lambda^{-1}\right)u_ju_j^\top.
\]

For an action \(x\), let
\[
B_x=H_t^{-1/2}(I_K\otimes x),
\qquad
A_t(x)=B_x^\top B_x=(I_K\otimes x)^\top H_t^{-1}(I_K\otimes x).
\]
For every \(z\in\mathbb R^K\), \(z^\top A_t(x)z=\|B_xz\|_2^2\ge0\); hence \(A_t(x)\) is positive semidefinite. Moreover,
\[
\|B_x\|_2^2=\max_{\|z\|_2=1}z^\top A_t(x)z=\lambda_{\max}(A_t(x)).
\]
Using the displayed inverse gives
\[
A_t(x)_{i\ell}=\frac{\|x\|_2^2}{\lambda}\delta_{i\ell}
+\sum_{j=1}^m\left(\frac1{\lambda+\mu_j}-\frac1\lambda\right)
\langle x,u_{ji}\rangle\langle x,u_{j\ell}\rangle.
\]
Thus the original quantity is exactly the largest eigenvalue of a positive-semidefinite \(K\times K\) matrix. Neither an \(n\times n\) inverse square root nor a completed orthonormal basis needs to be formed computationally.

For a fixed action, the \(Km\) inner products cost \(O(Kdm)\), assembling the matrix costs \(O(K^2m)\), and its dense symmetric eigenvalue calculation costs \(O(K^3)\), under the stated numerical-accuracy convention. Computing \(\|x\|_2^2\) costs \(O(d)\), already included because \(K,m\ge1\). The total per-action cost is
\[
O(Kdm+K^2m+K^3).
\]
These statements also cover \(x=0\), zero retained eigenvalues, and a full retained eigenspace.

### 2. Projection and scalar characterization

Let
\[
F(w)=\frac12(w-w')^\top G_t(w-w').
\]
The feasible ball is nonempty and compact, so continuity gives a minimizer. Since \(G_t\) is positive definite, \(F\) is strictly convex, so that minimizer is unique. If \(\|w'\|_2\le S\), the vector \(w'\) is feasible and attains objective zero; it is therefore the minimizer, including the boundary case \(\|w'\|_2=S\).

Suppose \(\|w'\|_2>S\). Use the constraint \((\|w\|_2^2-S^2)/2\le0\). Its strictly feasible point \(w=0\) exists because \(S>0\). For this differentiable convex problem, the KKT conditions are necessary and sufficient: primal feasibility, a multiplier \(\nu\ge0\), complementary slackness, and
\[
G_t(w-w')+\nu w=0,
\qquad
(G_t+\nu I_n)w=G_tw'.
\]
The multiplier cannot be zero, since stationarity would then force \(w=w'\), which is infeasible. Hence \(\nu>0\), and complementary slackness gives \(\|w\|_2=S\).

Put
\[
a=Q_t^\top w',
\qquad
b=w'-Q_ta=(I_n-Q_tQ_t^\top)w'.
\]
Then \(b\in\operatorname{col}(Q_t)^\perp=\ker(Q_t^\top)\) and
\[
\|w'\|_2^2=\|a\|_2^2+\|b\|_2^2.
\]
Along the \(j\)-th column of \(Q_t\), the operator \((G_t+\nu I_n)^{-1}G_t\) has eigenvalue \((\lambda+\alpha_j)/(\lambda+\alpha_j+\nu)\). On the orthogonal complement, its eigenvalue is \(\lambda/(\lambda+\nu)\). Consequently,
\[
w(\nu)=Q_t\operatorname{diag}\!\left(\frac{\lambda+\alpha_j}{\lambda+\alpha_j+\nu}\right)a
+\frac{\lambda}{\lambda+\nu}b.
\]
Equivalently,
\[
w(\nu)=\left[\frac{\lambda}{\lambda+\nu}I_n
+\frac{\nu}{\lambda+\nu}Q_t\Gamma_t((\lambda+\nu)I_q+\Gamma_t)^{-1}Q_t^\top\right]w'.
\]
The coefficients in these formulas multiply the unconstrained vector \(w'\), not the projected vector.

By orthogonality, the active constraint is precisely
\[
\phi(\nu):=\sum_{j=1}^q\left(\frac{\lambda+\alpha_j}{\lambda+\alpha_j+\nu}\right)^2a_j^2
+\left(\frac{\lambda}{\lambda+\nu}\right)^2\|b\|_2^2=S^2.
\]
Each nonzero summand is continuous and strictly decreasing for \(\nu\ge0\). At least one summand is nonzero because \(\|w'\|_2>S>0\). Thus \(\phi\) is continuous and strictly decreasing, with
\[
\phi(0)=\|w'\|_2^2>S^2,
\qquad
\lim_{\nu\to\infty}\phi(\nu)=0<S^2.
\]
The intermediate value theorem and strict monotonicity give exactly one positive root \(\nu_*\).

The vector \(w_*=w(\nu_*)\) satisfies the displayed stationarity equation and \(\|w_*\|_2=S\). Optimality can also be checked directly, without leaving any reliance on an unstated sufficiency argument. For any feasible \(z\),
\[
F(z)-F(w_*)
=\frac12(z-w_*)^\top G_t(z-w_*)-\nu_*w_*^\top(z-w_*).
\]
Cauchy-Schwarz gives \(w_*^\top z\le\|w_*\|_2\|z\|_2\le S^2=w_*^\top w_*\), so both terms on the right are nonnegative. The first is strictly positive when \(z\ne w_*\). Hence \(w_*\) is the unique projection.

Empty update factors are allowed: if \(q=0\), take \(a\) to be empty and \(b=w'\). Then \(G_t=\lambda I_n\), and in the active case
\[
\nu_*=\lambda\left(\frac{\|w'\|_2}{S}-1\right),
\qquad
w_*=\frac{S}{\|w'\|_2}w'.
\]
Zero eigenvalues and a zero-dimensional orthogonal complement likewise cause no difficulty; the same formulas apply with the corresponding terms zero or absent.

### 3. Numerical evaluation and projection cost

Computing the feasibility norm, \(a\), and \(\|b\|_2^2=\|w'\|_2^2-\|a\|_2^2\) costs \(O(n(q+1))\). An explicit vector \(b\), when needed for reconstruction, can be formed within the same bound. Each evaluation of \(\phi\) costs \(O(q+1)\), and reconstruction of \(w(\nu)\) costs \(O(n(q+1))\). The added ones account for the norm, orthogonal-complement contribution, and output vector even when \(q=0\).

A finite bisection bracket is available from the stored numbers. Define
\[
\gamma_{\max}=\lambda+\max\bigl(\{0\}\cup\{\alpha_j:1\le j\le q\}\bigr),
\qquad
u_{\mathrm{hi}}=\gamma_{\max}\left(\frac{\|w'\|_2}{S}-1\right)>0.
\]
Every shrinkage coefficient is at most \(\gamma_{\max}/(\gamma_{\max}+\nu)\), so
\[
\phi(\nu_{\mathrm{hi}})
\le\left(\frac{\gamma_{\max}}{\gamma_{\max}+\nu_{\mathrm{hi}}}\right)^2\|w'\|_2^2=S^2.
\]
Thus \([0,\nu_{\mathrm{hi}}]\) contains the root. Bisection converges, halving the bracket at every iteration; an endpoint giving equality may be accepted immediately. With \(N\) scalar evaluations, the projection work is explicitly
\[
O\bigl(n(q+1)+(q+1)N\bigr).
\]
The displayed dimension-wise costs suppress numerical-accuracy factors as stipulated in the task. This convention does not assert that arbitrary real roots or eigenvalues are obtained exactly by finitely many arithmetic operations, and no unqualified global quadratic-convergence assertion for Newton's method is used. The projection formula and root characterization themselves are exact.

### 4. Thin updates, storage, and aggregation

Set \(p=m+K\). A retained factor augmented by at most \(K\) columns has at most \(p\) columns. A dense thin spectral decomposition of an \(n\times p\) factor can be implemented in \(O(np\min\{n,p\})\) arithmetic, hence in \(O(np^2)\). Its thin factors and workspace require \(O(np)\) storage: writing \(r=\min\{n,p\}\), their sizes are bounded by \(nr+pr+r^2=O(np)\). Thus this bound also covers the case \(p>n\); no nonexistent collection of more than \(n\) orthonormal columns is required. A fixed number of these updates has the same asymptotic bounds.

The supplied orthonormal update factor satisfies \(q\le\min\{n,p\}\). Therefore \(q+1\le p+1\le2p\), so, under the stipulated numerical-accuracy convention, the projection costs are dominated by \(O(np^2)\), including \(q=0\).

The maintained factors, augmented factors, and thin-decomposition workspace use \(O(np)\) space. The diagonal spectra and length-\(n\) vectors fit within this bound. The action calculation uses \(O(Km+K^2+d)\) additional storage. Since \(K\le n\), \(p\ge K,m\), and \(d\le n\), this is also \(O(np)\). Action work arrays can be reused between actions; retaining all action inputs or reported outputs is outside the stated working-space convention. Consequently the total working space is
\[
O(np)=O(Kd(m+K)).
\]

Evaluating all actions costs
\[
O\!\left(|\mathcal X_t|(Kdm+K^2m+K^3)\right).
\]
Adding the projection and thin spectral updates gives
\[
O\!\left(|\mathcal X_t|(Kdm+K^2m+K^3)+Kd(m+K)^2\right).
\]
An empty action set simply contributes zero action-evaluation work to this algebraic task.

Finally, with \(p=m+K\) and \(n=Kd\), each of \(Kdm\), \(K^2m\), and \(K^3\) is \(O(np^2)\): use respectively \(m\le p^2\), \(K\le n\) and \(m\le p^2\), and \(K\le n\) and \(K^2\le p^2\). Thus a constant number of actions is absorbed into the update bound. The same conclusion holds whenever the complete action-evaluation term is non-dominating. The shorter dependence is then \(O(Kd(m+K)^2)\), linear in \(d\) for fixed \(K,m\).

## Private Source-Repair Note

The source's projection proof at L000625 omits the prime on the vector inside its spectral coefficients; L000624 and L000628 fix the intended expression uniquely. Its complement-space description at L000619 means the orthogonal complement of the column space, and the inconsistent eigenvalue names at L000626 and L000637 mean the previously defined eigenvalues. The final Newton iteration estimate at L000640 is not used as a global guarantee. The bracketed implementation above is already permitted by L000140 and retains the same scalar-root proof architecture. These local source repairs are recorded under theory_004. The q=0 cost correction is separately a repair to the previous formalized reference proof. No unresolved proof obligation remains.
