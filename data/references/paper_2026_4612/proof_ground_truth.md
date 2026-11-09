# Reference Proof

## Proof Obligations

The theorem-critical obligations are: (1) a coordinate-consistent trace contraction with the exact normalization; (2) the Kronecker log-determinant formula; (3) equality of the block objectives up to a finite additive constant and a positive multiplier; (4) convexity on the stated domain; and (5) identification of sequential exact block updates wherever those updates exist. All five obligations are derived below. The optional mode-product computation appearing in the original reference is also derived explicitly. No ADMM convergence theorem or universal attainment claim is used.

## Complete Proof

### 1. Coordinates and the trace contraction

Fix \(m\), hold all other factors fixed, and abbreviate \(q=D_{\ne m}\). Let \(Q_m\) be the permutation matrix that sends the coordinate tuple \((i_1,\ldots,i_M)\) to the ordered tuple consisting first of \(i_m\) and then of the remaining indices in their specified order. Thus \(Q_m\operatorname{vec}(X_{t,n})\) consists of the rows of \(B_{t,n}^{(m)}\) stacked consecutively. The entrywise definition of a Kronecker product gives
\[
\widetilde P_t:=Q_mP_tQ_m^\top=\Omega_t^{(m)}\otimes H_t^{(m)}.
\]
This is a simultaneous change of coordinates, not an assertion that differently ordered Kronecker factors are literally equal. Set \(\widetilde C_t=Q_m\widehat C_tQ_m^\top\). Since \(Q_m^\top Q_m=I\), cyclicity of the trace gives
\[
\operatorname{tr}(\widehat C_tP_t)=\operatorname{tr}(\widetilde C_t\widetilde P_t).
\]

Write \(b_{t,n,j}\in\mathbb R^q\) for the transpose of row \(j\) of \(B_{t,n}^{(m)}\). The \((j,k)\) block of \(\widetilde C_t\), with blocks of size \(q\times q\), is
\[
(\widetilde C_t)_{jk}=\frac1{n_t}\sum_{n=1}^{n_t}b_{t,n,j}b_{t,n,k}^\top.
\]
Every factor is symmetric, so \(H_t^{(m)}\) is symmetric. Consequently,
\[
\operatorname{tr}\bigl((\widetilde C_t)_{jk}H_t^{(m)}\bigr)
=\frac1{n_t}\sum_n b_{t,n,k}^\top H_t^{(m)}b_{t,n,j}
=q(C_t^{(m)})_{jk}.
\]
Expanding the diagonal blocks of the product now yields
\[
\begin{aligned}
\operatorname{tr}(\widehat C_tP_t)
&=\sum_{j,k}(\Omega_t^{(m)})_{kj}\operatorname{tr}\bigl((\widetilde C_t)_{jk}H_t^{(m)}\bigr)\\
&=q\sum_{j,k}(\Omega_t^{(m)})_{kj}(C_t^{(m)})_{jk}\\
&=q\operatorname{tr}(C_t^{(m)}\Omega_t^{(m)}).
\end{aligned}
\]
The factor \(q\) comes from the definition of \(C_t^{(m)}\); the factor \(1/n_t\) remains exactly the empirical-covariance normalization in the task.

The Kronecker product of positive-definite factors is positive definite: tensor products of their eigenvectors form a basis with positive product eigenvalues. Hence, for every \(u\in\mathbb R^{d_m}\),
\[
u^\top C_t^{(m)}u
=\frac1{n_tq}\sum_n (B_{t,n}^{(m)\top}u)^\top H_t^{(m)}(B_{t,n}^{(m)\top}u)\ge0.
\]
Thus \(C_t^{(m)}\) is a symmetric positive-semidefinite covariance-type matrix, although it need not be positive definite.

### 2. Optional equivalent mode-product computation

For completeness, define the mode-\(r\) product by
\[
(X\times_r A)_{i_1,\ldots,i_M}
=\sum_{j_r}A_{i_rj_r}X_{i_1,\ldots,i_{r-1},j_r,i_{r+1},\ldots,i_M}.
\]
Let \(Y_{t,n}^{(m)}\) be the mode-\(m\) unfolding after multiplying \(X_{t,n}\) in every other mode \(r\) by \(\Omega_t^{(r)}\). If \(a\) and \(b\) denote tuples of the remaining indices, its entries satisfy
\[
(Y_{t,n}^{(m)})_{j,a}
=\sum_b(B_{t,n}^{(m)})_{j,b}\prod_{r\ne m}(\Omega_t^{(r)})_{a_rb_r}
=(B_{t,n}^{(m)}H_t^{(m)\top})_{j,a}.
\]
Symmetry of \(H_t^{(m)}\) therefore gives \(Y_{t,n}^{(m)}=B_{t,n}^{(m)}H_t^{(m)}\), and hence
\[
B_{t,n}^{(m)}H_t^{(m)}B_{t,n}^{(m)\top}
=Y_{t,n}^{(m)}B_{t,n}^{(m)\top}.
\]
This verifies the optional efficient expression without relying on an unstated tensor identity. It is not needed to prove the public objective equivalence.

### 3. Log determinant

For square matrices \(A\) and \(B\) of sizes \(a\) and \(b\), the Kronecker determinant identity is
\[
\det(A\otimes B)=(\det A)^b(\det B)^a.
\]
In the positive-definite case used here, this follows directly by diagonalizing the two symmetric matrices: the product eigenvalues are all \(\alpha_i\beta_j\). More generally, if \(\eta_{r,i}>0\) are the eigenvalues of \(\Omega_t^{(r)}\), the eigenvalues of \(P_t\) are \(\prod_r\eta_{r,i_r}\). Summing their logarithms gives
\[
\log\det P_t
=\sum_{i_1,\ldots,i_M}\sum_{r=1}^M\log\eta_{r,i_r}
=\sum_{r=1}^M D_{\ne r}\log\det\Omega_t^{(r)}.
\]
Each eigenvalue logarithm from mode \(r\) occurs exactly \(D_{\ne r}\) times. All logarithms are finite because the matrices are positive definite.

### 4. Exact block objective

Let \(G_m\) denote the displayed block objective in the public task. Substitution of the trace and log-determinant formulas into \(F\) gives
\[
F=qG_m+\kappa_m,
\]
where
\[
\kappa_m=\sum_{r\ne m}\left[
-D_{\ne r}\sum_{t=1}^T\log\det\Omega_t^{(r)}
+\lambda_r\sum_{t=1}^T\|\Omega_t^{(r)}\|_{1,\mathrm{od}}
+\rho_r\sum_{t=2}^T\psi(\Omega_t^{(r)}-\Omega_{t-1}^{(r)})
\right].
\]
All factors occurring in \(\kappa_m\) are fixed during the update. Their positive definiteness and the real-valued penalty ensure that \(\kappa_m\) is finite. Since \(q>0\), the two block optimization problems have identical minimizer sets, including when those sets are empty. Their infima obey \(\inf F=q\inf G_m+\kappa_m\), also when the infimum is \(-\infty\). This proves precisely the required penalty rescalings \(\lambda_m/q\) and \(\rho_m/q\).

### 5. Convexity

The domain \((\mathbb S_{++}^{d_m})^T\) is convex. Each trace term is linear. For a symmetric direction \(U\), the second directional derivative of \(-\log\det\Omega\) at \(\Omega\succ0\) is
\[
\operatorname{tr}(\Omega^{-1}U\Omega^{-1}U)
=\|\Omega^{-1/2}U\Omega^{-1/2}\|_F^2\ge0.
\]
Thus \(-\log\det\) is convex on this domain. The off-diagonal absolute-value sum is convex. The map \((\Omega_{t-1},\Omega_t)\mapsto\Omega_t-\Omega_{t-1}\) is linear, so composing it with the stated convex restriction of \(\psi\) gives a convex function. All penalty coefficients are nonnegative. Therefore \(G_m\) is convex and has the time-varying graphical-lasso form.

### 6. Alternating updates and scope

At a current feasible collection of factors, form \(H_t^{(m)}\) and \(C_t^{(m)}\) from the other modes' current values. If \(G_m\) has a minimizer, replacing the mode-\(m\) sequence by such a minimizer exactly minimizes \(F\) with all other sequences fixed, by the objective equality above. Continue to the next mode using the updated collection, and repeat the order \(1,\ldots,M\). These are sequential alternating block-minimization updates, not simultaneous updates based on stale factors.

This identifies the procedure; it does not establish that every permitted block problem attains its infimum or that the outer iterations converge. Convexity alone would not establish either claim. For example, take \(M=2\), \(d_1=3\), \(d_2=2\), \(T=n_1=1\), all regularization coefficients zero, and a Gaussian observation with true precision \(I_3\otimes I_2\). Fix the second optimization factor at \(I_2\). The unfolding \(B\in\mathbb R^{3\times2}\) has a unit vector \(v\in\ker(B^\top)\). Along \(\Omega^{(1)}=I_3+a vv^\top\),
\[
F=\|B\|_F^2-2\log(1+a)\longrightarrow-\infty.
\]
This explains why no unconditional attainment assertion is part of the reference or rubric. It does not impair the objective reduction.

For \(M=1\), the conventions give \(q=1\), \(H=[1]\), and a one-column unfolding, so every calculation remains valid. For \(T=1\), the temporal sums are empty. Dimensions equal to one, zero penalty coefficients, and singular empirical covariances require no additional assumptions. The proof is pointwise in the observed tensors and uses no unprovided independence assumption. Every theorem-critical obligation is closed.
