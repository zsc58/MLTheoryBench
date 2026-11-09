# Reference Proof

## Source Contract and Scope

The source uses one fixed process-noise covariance and one fixed observation-noise covariance. Its expansion path rescales supplied local Jacobians while holding these covariances, the observation matrix, and the incoming covariance fixed. The one-step filtered derivative is therefore a local derivative with its incoming filtered covariance fixed, not the total derivative obtained by rerunning all earlier filtering steps. The covariance recursion is the local-linearization model being analyzed; no claim of exact nonlinear predictive covariance is required.

The no-transport comparison carries covariance forward additively without applying the scaled Jacobians. Its source definition appears at L000072 and L000634. The claims concern the log-determinant part of the Gaussian score and same-step covariance reduction. They do not assert monotonicity of the full Gaussian negative log likelihood, strict reduction at every assimilation, or monotone decrease of posterior covariance across different times.

## Theorem-Critical Obligations

1. Derive the open-loop covariance expansion with fixed positive-semidefinite coefficient matrices and verify observation-covariance positive definiteness.
2. Derive the log-determinant derivative, establish its sign and strictness, and handle both vanishing transported contributions and the separately defined no-transport comparison.
3. Derive the one-step filtered covariance-volume derivative under its fixed-input contract.
4. Prove the same-step Loewner contraction. Verify privately that the posterior remains positive semidefinite so that the covariance update can be applied repeatedly.

All four obligations are closed below. No Lyapunov-spectrum or entropy result is used. The filtering formulas needed for the claim are supplied definitions, and the relevant covariance identities are verified algebraically rather than deferred to an external filtering theorem.

## Complete Proof

### 1. Open-loop expansion and well-definedness

For integers $0\le a<b\le h$, define
\[
\Phi_{b:a}=J_{b-1}\cdots J_a,
\qquad \Phi_{a:a}=I_d.
\]
The products are independent of $s$. We claim that for $0\le i\le h$,
\[
P_i(s)=e^{2is}\Phi_{i:0}\Sigma_t\Phi_{i:0}^T
 +\sum_{r=0}^{i-1}e^{2(i-1-r)s}\Phi_{i:r+1}G\Phi_{i:r+1}^T.
\]
For $i=0$, the sum is empty and the identity is $P_0(s)=\Sigma_t$. If the formula holds at $i$, multiplying by $e^{2s}J_i$ on the left and $J_i^T$ on the right appends $J_i$ to each product and increases each exponent by $2s$. Adding $G$ gives the new summand with $r=i$ and empty transport product. This proves the formula by induction.

For any positive-semidefinite matrix $C$ and any real matrix $M$ of compatible size, $MCM^T$ is positive semidefinite because
\[
v^TMCM^Tv=(M^Tv)^TC(M^Tv)\ge0.
\]
In particular, every covariance term in the expansion is positive semidefinite. Define
\[
A_h=B\Phi_{h:0}\Sigma_t\Phi_{h:0}^TB^T,
\]
and, for $0\le\ell\le h-1$, define
\[
A_\ell=B\Phi_{h:h-\ell}G\Phi_{h:h-\ell}^TB^T.
\]
These are fixed $m\times m$ positive-semidefinite matrices. Reindexing the process-noise sum using $\ell=h-1-r$ gives
\[
\Omega_{\rm open}(s)=\Lambda+\sum_{\ell=0}^{h}e^{2\ell s}A_\ell.
\]
Since $\Lambda\succ0$, this covariance is positive definite for every finite real $s$. Its inverse and real log determinant are therefore well defined. No invertibility of any latent covariance, Jacobian, or observation matrix is used.

### 2. Volume derivative, strictness, and zero-pressure cases

For a differentiable positive-definite matrix function $\Omega(s)$, determinant multiplicativity and the first-order determinant expansion give
\[
\det\Omega(s+\varepsilon)
=\det\Omega(s)\det\!\left(I_m+\varepsilon\Omega(s)^{-1}\Omega'(s)+o(\varepsilon)\right).
\]
By multilinearity of the determinant, $\det(I_m+\varepsilon H+o(\varepsilon))=1+\varepsilon\operatorname{tr}(H)+o(\varepsilon)$. Taking the logarithmic derivative therefore yields
\[
\frac{d}{ds}\log\det\Omega(s)=\operatorname{tr}\!\left(\Omega(s)^{-1}\Omega'(s)\right).
\]
The finite covariance expansion is differentiable, and its derivative is
\[
\Omega_{\rm open}'(s)=\sum_{\ell=1}^h2\ell e^{2\ell s}A_\ell.
\]
Thus
\[
\frac{d}{ds}\frac12\log\det\Omega_{\rm open}(s)
=\sum_{\ell=1}^h\ell e^{2\ell s}\operatorname{tr}\!\left(\Omega_{\rm open}(s)^{-1}A_\ell\right).
\]
For $Q\succ0$ and $A\succeq0$, cyclicity of the trace gives
\[
\operatorname{tr}(Q^{-1}A)=\operatorname{tr}(Q^{-1/2}AQ^{-1/2}).
\]
The matrix on the right is positive semidefinite, so its eigenvalues and their sum are nonnegative. Since $Q^{-1/2}$ is invertible, this matrix is nonzero exactly when $A$ is nonzero. A nonzero positive-semidefinite matrix has at least one positive eigenvalue and hence positive trace. It follows that every summand in the derivative is nonnegative and that any nonzero $A_\ell$ with $\ell\ge1$ makes the derivative strictly positive at every finite real $s$. If $A_1=\cdots=A_h=0$, the derivative vanishes identically.

For the separately defined no-transport recursion, induction gives
\[
\widetilde P_i(s)=\Sigma_t+iG.
\]
Consequently $\widetilde\Omega_{\rm open}(s)=B(\Sigma_t+hG)B^T+\Lambda$ is positive definite and independent of $s$, so its log-determinant derivative is zero. This comparison does not replace the Jacobians by identities and then scale those identities: its covariance recursion contains no Jacobian-scaling factor.

These are statements about the covariance-volume component $\frac12\log\det\Omega$. No sign for the derivative of the Mahalanobis component or the full Gaussian score is inferred.

### 3. One-step filtered volume derivative

The incoming covariance $\Sigma_{t-1|t-1}$ and all supplied matrices are fixed with respect to $s$. Hence $P^-(s)\succeq0$ and $\Omega_t(s)\succ0$, and
\[
\Omega_t'(s)=2e^{2s}BJ_{\rm f}\Sigma_{t-1|t-1}J_{\rm f}^TB^T.
\]
Applying the logarithmic derivative identity gives
\[
\frac{d}{ds}\frac12\log\det\Omega_t(s)
=e^{2s}\operatorname{tr}\!\left(\Omega_t(s)^{-1}BJ_{\rm f}\Sigma_{t-1|t-1}J_{\rm f}^TB^T\right).
\]
The matrix $BJ_{\rm f}\Sigma_{t-1|t-1}J_{\rm f}^TB^T$ is positive semidefinite by the congruence argument above. The same trace argument therefore proves nonnegativity, including when this matrix is zero.

### 4. Assimilation contraction and repeated applicability

Fix $s$ and abbreviate $P=P^-(s)$, $\Omega=BPB^T+\Lambda$, and $K=PB^T\Omega^{-1}$. Substitution into the specified update gives
\[
P^+(s)=P-PB^T\Omega^{-1}BP.
\]
Since $P$ is symmetric,
\[
PB^T\Omega^{-1}BP
=(\Omega^{-1/2}BP)^T(\Omega^{-1/2}BP)\succeq0.
\]
Therefore $P^+(s)\preceq P^-(s)$, with equality allowed.

For completeness of the repeated-covariance interpretation, the posterior is also positive semidefinite. Expanding the Joseph expression gives
\[
\begin{aligned}
&(I_d-KB)P(I_d-KB)^T+K\Lambda K^T\\
&\quad=P-KBP-PB^TK^T+K(BPB^T+\Lambda)K^T.
\end{aligned}
\]
Here $K\Omega=PB^T$, and $KBP=PB^T\Omega^{-1}BP$ is symmetric. The expression therefore equals $P-KBP=P^+(s)$. Both terms in the Joseph expression are positive semidefinite, proving $P^+(s)\succeq0$ even when $P$ is singular. Subsequent prediction by a Jacobian congruence and addition of $G\succeq0$ preserves positive semidefiniteness. Thus the same non-strict posterior-versus-prior contraction applies at each assimilation step. Prediction between updates can increase covariance; no cross-time monotonicity is asserted.

The proof covers $h=1$, zero initial or process covariance, and zero or rank-deficient $B$ without additional assumptions.
