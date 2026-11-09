# Reference Proof

## Proof Structure

1. Define posterior responsibilities and derive a variational upper bound tangent to the negative observed log-likelihood.
2. Derive the uniform baseline-softmax covariance bound, including the one-dimensional case.
3. Lift the bound to coefficient space and construct the explicit separable tangent quadratic majorizer, retaining all response-statistic linear terms.
4. Derive and solve the block normal equations, prove consistency when singular, and specify a valid centered-ridge alternative.
5. Apply majorization, tangency, and exact minimization to prove likelihood ascent.

## Complete Proof

All statements below hold for each realized batch. Independence of observations is part of the ambient sampling setup but is not needed for the deterministic MM inequalities. Write \(\phi_n=\phi(x_n)\in\mathbb R^Q\), where \(Q=P(D+1)\). Stack free coefficients class-major as
\[
\alpha=(\alpha_1^{\mathsf T},\ldots,\alpha_{K-1}^{\mathsf T})^{\mathsf T},\qquad
\beta_k=(\beta_{k1}^{\mathsf T},\ldots,\beta_{k,M-1}^{\mathsf T})^{\mathsf T}.
\]
Every coefficient is finite. Consequently all gate and expert probabilities, their mixture probabilities, and posterior responsibilities are strictly positive, and the batch log-likelihood is finite.

### 1. Responsibilities and the variational bound

Fix the current parameter \(\theta^{(t)}\), and define
\[
r_{nk}^{(t)}=\frac{g_k^{(t)}(x_n)e_k^{(t)}(y_n\mid x_n)}{s_{\theta^{(t)}}(y_n\mid x_n)}.
\]
These weights sum to one. Put \(a_{nk}(\theta)=g_k(x_n)e_k(y_n\mid x_n)\). Concavity of the logarithm gives
\[
\log\sum_k a_{nk}(\theta)
=\log\sum_k r_{nk}^{(t)}\frac{a_{nk}(\theta)}{r_{nk}^{(t)}}
\ge\sum_k r_{nk}^{(t)}\log\frac{a_{nk}(\theta)}{r_{nk}^{(t)}}.
\]
At the current iterate every ratio inside this weighted average equals \(s_{\theta^{(t)}}(y_n\mid x_n)\), so equality holds. Summing the negative of this inequality gives a global variational upper bound \(V_t\) satisfying
\[
-L(\theta)\le V_t(\theta),\qquad V_t(\theta^{(t)})=-L(\theta^{(t)}).
\]

For \(q\ge1\), define
\[
F_q(z)=\log\left(1+\sum_{j=1}^q e^{z_j}\right).
\]
Let
\[
Z_{K,n}=I_{K-1}\otimes\phi_n^{\mathsf T},\quad
Z_{M,n}=I_{M-1}\otimes\phi_n^{\mathsf T},\quad
\eta_n=Z_{K,n}\alpha,\quad \xi_{nk}=Z_{M,n}\beta_k.
\]
Define \(r_n^{(t),-}=(r_{n1}^{(t)},\ldots,r_{n,K-1}^{(t)})^{\mathsf T}\), and let \(u_n\in\mathbb R^{M-1}\) have coordinate \((u_n)_m=\mathbf1\{y_n=m\}\). In particular \(u_n=0\) if \(y_n=M\). Expanding the negative log probabilities yields
\[
V_t(\theta)=\sum_{n,k}r_{nk}^{(t)}\log r_{nk}^{(t)}
+\sum_n\left[F_{K-1}(\eta_n)-(r_n^{(t),-})^{\mathsf T}\eta_n\right]
+\sum_{n,k}r_{nk}^{(t)}\left[F_{M-1}(\xi_{nk})-u_n^{\mathsf T}\xi_{nk}\right].
\]
The linear terms displayed here depend on the candidate parameter and must not be absorbed into a constant.

### 2. Uniform logit curvature

Differentiation gives \(\nabla F_q(z)=\widehat p\) and
\[
\nabla^2F_q(z)=\operatorname{diag}(\widehat p)-\widehat p\widehat p^{\mathsf T},
\]
where \(\widetilde p=(\widehat p^{\mathsf T},p_{q+1})^{\mathsf T}\) is the full baseline-softmax probability vector. Define
\[
W=\operatorname{diag}(\widetilde p)-\widetilde p\widetilde p^{\mathsf T},\qquad
A_q=\frac34 I_q-\frac1{2q}\mathbf1_q\mathbf1_q^{\mathsf T}.
\]
We prove the claimed bound rather than invoke it as an unproved paper-specific result.

For a scalar random variable \(T\in[a,b]\) with mean \(\mu\), taking expectations of \((T-a)(b-T)\ge0\) gives
\[
\operatorname{Var}(T)\le(b-\mu)(\mu-a)\le\frac{(b-a)^2}{4}.
\]
For a one-hot vector \(J\) with probabilities \(\widetilde p\),
\[
v^{\mathsf T}Wv=\operatorname{Var}(v^{\mathsf T}J).
\]
The range of \(v^{\mathsf T}J\) is at most \(\sqrt2\|v\|\), since
\[
|v_i-v_j|=|v^{\mathsf T}(e_i-e_j)|\le\sqrt2\|v\|.
\]
Thus \(W\preceq I_{q+1}/2\). Also \(W\mathbf1_{q+1}=0\). Applying the preceding bound to the orthogonal projection of any vector onto \(\mathbf1_{q+1}^{\perp}\) therefore yields
\[
W\preceq\frac12\left(I_{q+1}-\frac{\mathbf1_{q+1}\mathbf1_{q+1}^{\mathsf T}}{q+1}\right).
\]
Taking the top-left principal submatrix gives
\[
\nabla^2F_q(z)\preceq\frac12\left(I_q-\frac{\mathbf1_q\mathbf1_q^{\mathsf T}}{q+1}\right).
\]
The difference between \(A_q\) and this last bound is
\[
\frac14 I_q-\frac{\mathbf1_q\mathbf1_q^{\mathsf T}}{2q(q+1)}.
\]
Its eigenvalue along \(\mathbf1_q\) is \((q-1)/(4(q+1))\), and its eigenvalue on \(\mathbf1_q^{\perp}\) is \(1/4\). Both are nonnegative for every \(q\ge1\). Hence
\[
\nabla^2F_q(z)\preceq A_q\quad\text{for all }z\in\mathbb R^q.
\]
In particular \(A_1=1/4\). More generally \(A_q\) has eigenvalue \(1/4\) along \(\mathbf1_q\) and \(3/4\) on its orthogonal complement, so \(A_q\succeq I_q/4\).

### 3. Coefficient curvature and the quadratic surrogate

For symmetric \(B-A\succeq0\) and \(C\succeq0\),
\[
(B-A)\otimes C=
\big((B-A)^{1/2}\otimes C^{1/2}\big)^{\mathsf T}
\big((B-A)^{1/2}\otimes C^{1/2}\big)\succeq0.
\]
This proves the required Kronecker Loewner-order property, including singular \(C\). Consequently the per-datum coefficient curvatures are
\[
B_{g,n}=Z_{K,n}^{\mathsf T}A_{K-1}Z_{K,n}
=A_{K-1}\otimes(\phi_n\phi_n^{\mathsf T}),
\]
\[
B_{e,n}=Z_{M,n}^{\mathsf T}A_{M-1}Z_{M,n}
=A_{M-1}\otimes(\phi_n\phi_n^{\mathsf T}).
\]
They uniformly dominate the corresponding coefficient Hessians. The aggregated curvatures are
\[
H_g=\sum_n B_{g,n},\qquad
H_{e,k}=\sum_n r_{nk}^{(t)}B_{e,n}.
\]
Thus \(H_g=A_{K-1}\otimes\sum_n\phi_n\phi_n^{\mathsf T}\), and \(H_{e,k}=A_{M-1}\otimes\sum_n r_{nk}^{(t)}\phi_n\phi_n^{\mathsf T}\). Each observation's curvature is included once; expert weights remain inside its own sum.

The integral Taylor formula gives, for any \(z,z_0\),
\[
F_q(z)\le F_q(z_0)+\nabla F_q(z_0)^{\mathsf T}(z-z_0)
+\frac12(z-z_0)^{\mathsf T}A_q(z-z_0),
\]
because the integral of \(1-s\) over \([0,1]\) is \(1/2\). This bound holds globally and is equal to \(F_q\) at \(z=z_0\).

Write \(p_n^{(t)}=(g_1^{(t)}(x_n),\ldots,g_{K-1}^{(t)}(x_n))^{\mathsf T}\) and \(h_{nk}^{(t)}=(e_k^{(t)}(1\mid x_n),\ldots,e_k^{(t)}(M-1\mid x_n))^{\mathsf T}\). Let \(\delta\alpha=\alpha-\alpha^{(t)}\), \(\delta\beta_k=\beta_k-\beta_k^{(t)}\), \(\delta\eta_n=Z_{K,n}\delta\alpha\), and \(\delta\xi_{nk}=Z_{M,n}\delta\beta_k\). An explicit surrogate is
\[
\mathcal Q_t(\theta)=-L(\theta^{(t)})+S_g+\sum_k S_{e,k},
\]
where
\[
S_g=\sum_n\left[(p_n^{(t)}-r_n^{(t),-})^{\mathsf T}\delta\eta_n
+\frac12\delta\eta_n^{\mathsf T}A_{K-1}\delta\eta_n\right],
\]
\[
S_{e,k}=\sum_n r_{nk}^{(t)}\left[(h_{nk}^{(t)}-u_n)^{\mathsf T}\delta\xi_{nk}
+\frac12\delta\xi_{nk}^{\mathsf T}A_{M-1}\delta\xi_{nk}\right].
\]
Substitution into \(V_t\) proves
\[
-L(\theta)\le\mathcal Q_t(\theta),\qquad
\mathcal Q_t(\theta^{(t)})=-L(\theta^{(t)}).
\]
All added expressions vanish at the current iterate, so the constant is explicitly determined.

### 4. Exact updates, singular systems, and ridge

Define
\[
b_g=\sum_n Z_{K,n}^{\mathsf T}(r_n^{(t),-}-p_n^{(t)}),\qquad
b_{e,k}=\sum_n r_{nk}^{(t)}Z_{M,n}^{\mathsf T}(u_n-h_{nk}^{(t)}).
\]
The coefficient blocks are \(-b_g^{\mathsf T}\delta\alpha+(1/2)\delta\alpha^{\mathsf T}H_g\delta\alpha\) and \(-b_{e,k}^{\mathsf T}\delta\beta_k+(1/2)\delta\beta_k^{\mathsf T}H_{e,k}\delta\beta_k\). Their normal equations are
\[
H_g\delta\alpha=b_g,\qquad H_{e,k}\delta\beta_k=b_{e,k}.
\]

To verify consistency, consider any block with curvature \(H=\sum_n w_n Z_n^{\mathsf T}A_qZ_n\), where the weights are nonnegative, and its right-hand side \(b=\sum_n w_n Z_n^{\mathsf T}d_n\). If \(v\in\ker H\), then
\[
0=v^{\mathsf T}Hv\ge\frac14\sum_n w_n\|Z_nv\|^2.
\]
Thus \(Z_nv=0\) for every positive weight, and \(v^{\mathsf T}b=0\). For a real symmetric matrix, \(\operatorname{range}(H)=(\ker H)^{\perp}\), so \(b\in\operatorname{range}(H)\). This applies to the gate with \(w_n=1\) and to expert \(k\) with \(w_n=r_{nk}^{(t)}\). It requires no full-rank design assumption.

The explicit minimum-norm increments and updates are therefore
\[
\alpha^{(t+1)}=\alpha^{(t)}+H_g^{\dagger}b_g,\qquad
\beta_k^{(t+1)}=\beta_k^{(t)}+H_{e,k}^{\dagger}b_{e,k}.
\]
The minimum-norm convention concerns the increment. Adding any vector in the appropriate curvature nullspace gives another exact minimizer. To verify minimization directly, for a solution \(\delta_*\) of \(H\delta_*=b\),
\[
\left[-b^{\mathsf T}\delta+\frac12\delta^{\mathsf T}H\delta\right]
-\left[-b^{\mathsf T}\delta_*+\frac12\delta_*^{\mathsf T}H\delta_*\right]
=\frac12(\delta-\delta_*)^{\mathsf T}H(\delta-\delta_*)\ge0.
\]
This also covers a zero curvature block, for which consistency gives \(b=0\). Duplicate constant features, dependent feature columns, and rank-deficient batches are consequently harmless. The scalar logit cases \(K=2\) or \(M=2\) were covered by \(q=1\).

For a valid ridge alternative, choose finite \(\lambda_g,\lambda_{e,k}\ge0\) and construct the surrogate
\[
\mathcal Q_{t,\lambda}(\theta)=\mathcal Q_t(\theta)
+\frac{\lambda_g}{2}\|\delta\alpha\|^2
+\sum_k\frac{\lambda_{e,k}}2\|\delta\beta_k\|^2.
\]
These additions are nonnegative and vanish at the current iterate, preserving majorization and tangency. The curvatures become \(H_g+\lambda_g I\) and \(H_{e,k}+\lambda_{e,k}I\). For a positive ridge use the ordinary inverse of the corresponding modified curvature; for zero ridge use the pseudoinverse as above. Explicitly,
\[
\delta\alpha=(H_g+\lambda_g I)^{\dagger}b_g,\qquad
\delta\beta_k=(H_{e,k}+\lambda_{e,k}I)^{\dagger}b_{e,k}.
\]
These exactly minimize \(\mathcal Q_{t,\lambda}\). A positive-ridge solve does not generally exactly minimize the original \(\mathcal Q_t\); no such assertion is needed or made. This centered ridge modifies the surrogate, not the likelihood being proved monotone.

### 5. Monotonicity

Let \(\mathcal R_t\) denote either \(\mathcal Q_t\) or the explicitly constructed \(\mathcal Q_{t,\lambda}\). Separability and the block minimization proof imply that the concatenated update exactly minimizes \(\mathcal R_t\). Hence
\[
-L(\theta^{(t+1)})\le\mathcal R_t(\theta^{(t+1)})
\le\mathcal R_t(\theta^{(t)})=-L(\theta^{(t)}).
\]
Equivalently, \(L(\theta^{(t+1)})\ge L(\theta^{(t)})\) at every iteration. The matrices and right-hand sides are finite and the stated solves produce finite vectors, so this argument can be repeated from every finite iterate. No maximizer-existence, full-rank, or statistical-convergence assumption is used.
