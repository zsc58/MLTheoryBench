# Reference Proof

## Ambient Contract and Proof Obligations

This is a population, finite-dimensional statement. The domain covariances, dimensions, and chosen domain principal projectors remain fixed as the penalty tends to infinity. No local covariance eigengap, sampling model, fourth-moment assumption, or block-diagonality assumption is required. The covariance operator on the intersection means compression to that subspace, not an assumption that the pooled covariance preserves it. Both optimization criteria depend on a basis only through its projector.

The five obligations are: (step_001) establish the spectral geometry and the optimization formulation; (step_002) prove hard-subspace inclusion and justify the representative basis; (step_003) establish spectral separation and projector convergence; (step_004) control the complement coordinates using the correct shifted equation; and (step_005) identify the ordered eigenvalue limits and, under simplicity, the sign-adjusted vector limits.

Set
\[
A=\overline\Sigma,\qquad Q=\overline\Pi,\qquad P_*=\Pi_{S_*},\qquad t=2E\lambda,\qquad a=\|A\|_{\mathrm{op}}.
\]
All constants below may depend on the fixed problem instance, but not on \(\lambda\) or on the permitted choices of eigenvectors.

## step_001: Spectral Geometry and Optimization

For every vector \(v\), the projector identities give
\[
v^\top(I-Q)v=\frac1E\sum_{e=1}^E\|(I-\Pi_k^{(e)})v\|_2^2.
\]
Thus \(0\preceq Q\preceq I\), and equality \(v^\top(I-Q)v=0\) holds precisely when every domain projector fixes \(v\). Consequently
\[
\ker(I-Q)=S_*.
\]
Because \(Q\) is symmetric, it preserves \(S_*^\perp\). Its eigenvalues on that complement belong to \([0,1)\). Since \(m<p\) and the dimension is finite, define
\[
\beta=\|Q|_{S_*^\perp}\|_{\mathrm{op}}<1,\qquad g=1-\beta>0.
\]

For \(W\in\operatorname{St}(p,k)\), both \(\Pi_W\) and each \(\Pi_k^{(e)}\) are rank-\(k\) orthogonal projectors. Hence
\[
\sum_{e=1}^E\|\Pi_W-\Pi_k^{(e)}\|_F^2
=2Ek-2E\operatorname{Tr}(W^\top QW).
\]
The soft objective therefore equals
\[
\operatorname{Tr}(W^\top(A+tQ)W)-2Ek\lambda.
\]

For completeness, the trace-maximization fact needed here can be verified directly. Let a symmetric matrix \(H\) have orthonormal eigenvectors \(z_j\) and ordered eigenvalues \(h_1\geq\cdots\geq h_p\). For a rank-\(k\) orthogonal projector \(P\), set \(b_j=z_j^\top Pz_j\). Then \(0\leq b_j\leq1\), \(\sum_jb_j=k\), and
\[
\sum_{j=1}^kh_j-\operatorname{Tr}(HP)
=\sum_{j\leq k}(h_j-h_k)(1-b_j)
+\sum_{j>k}(h_k-h_j)b_j\geq0.
\]
Equality requires full inclusion of every eigendirection with eigenvalue strictly above \(h_k\), exclusion of every eigendirection with eigenvalue strictly below \(h_k\), and selection of the remaining dimension inside the cutoff eigenspace. Conversely, those conditions give equality.

It follows that soft solution subspaces are exactly the maximizing top-\(k\) spectral subspaces of \(M_\lambda=A+tQ\). They admit ordered top-\(k\) eigenvector representatives. An arbitrary orthonormal basis of such a subspace is still a soft optimizer, but its individual columns need not be eigenvectors or be ordered. The public task has separately specified the ordered eigenvectors used in its limits.

The optimizer sets are nonempty: the Stiefel manifold is compact, the objectives are continuous, and the primary hard maximizer set is a nonempty compact set on which the secondary objective attains its maximum.

## step_002: Hard Inclusion and the Representative Basis

Apply the preceding trace characterization to \(H=Q\). Its first \(m\) eigenvalues are one and every remaining eigenvalue is at most \(\beta<1\).

If \(m<k\), the cutoff eigenvalue is strictly below one, so every agreement-maximizing rank-\(k\) subspace contains all of \(S_*\). If \(m=k\), equality forces exclusion of all eigendirections with eigenvalue below one, so the maximizing subspace is exactly \(S_*\). Every hard optimizer is a primary agreement maximizer, and therefore
\[
S_*\subseteq\operatorname{Im}(W_\infty).
\]

The compression \(A_*v=P_*Av\) is a self-adjoint operator on \(S_*\): for \(u,v\in S_*\), \(\langle u,A_*v\rangle=\langle u,Av\rangle=\langle A_*u,v\rangle\). Its fixed ordered orthonormal eigenbasis \(s_1,\ldots,s_m\) can be extended to an orthonormal basis of any hard solution subspace. This is a change of representative basis, not merely a permutation of arbitrary optimizer columns. The change preserves the projector and both optimization criteria. When \(m=k\), there are no additional basis vectors. Under a simple compressed spectrum, the ordered eigenvectors on \(S_*\) are unique up to sign.

## step_003: Spectral Separation and Projector Convergence

We first justify the eigenvalue perturbation bound used below. For a symmetric \(H\), the finite-dimensional variational formula is
\[
\lambda_j(H)=\max_{\dim L=j}\ \min_{\substack{x\in L\\\|x\|_2=1}}x^\top Hx.
\]
Indeed, the span of its first \(j\) eigenvectors attains the displayed value, and any \(j\)-dimensional subspace intersects the span of eigenvectors numbered \(j,\ldots,p\) nontrivially, giving the reverse inequality. If \(D\) is symmetric, every unit-vector Rayleigh quotient changes by at most \(\|D\|_{\mathrm{op}}\). Applying the formula therefore gives
\[
|\lambda_j(H+D)-\lambda_j(H)|\leq\|D\|_{\mathrm{op}}.
\]

Let
\[
H_t=t^{-1}M_\lambda=Q+t^{-1}A,\qquad \epsilon_t=a/t.
\]
The perturbation bound gives
\[
\lambda_m(H_t)\geq1-\epsilon_t,\qquad
\lambda_{m+1}(H_t)\leq\beta+\epsilon_t.
\]
For all sufficiently large \(t\), their difference is at least \(g/2>0\). Thus the leading rank-\(m\) projector is unique eventually, regardless of eigenvector choices at smaller penalties or ties within the selected block.

The standard independent perturbation input is the following top-block instance of the Davis–Kahan theorem recorded in theory_016. For symmetric \(H,\widehat H\), let \(V,\widehat V\) span their leading \(d\) eigenspaces. If
\[
\Delta=\lambda_d(H)-\lambda_{d+1}(\widehat H)>0,
\]
then
\[
\|\sin\Theta(\widehat V,V)\|_{\mathrm{op}}
\leq\|\widehat H-H\|_{\mathrm{op}}/\Delta.
\]
Here the principal-angle cosines are the singular values of \(V^\top\widehat V\). For equal-dimensional subspaces, their projector difference has norm equal to this sine norm, as recorded in theory_015. To see the identity, take singular-vector bases for \(V^\top\widehat V\): on each nontrivial principal plane the projector difference has eigenvalues \(\pm\sqrt{1-\sigma_j^2}\), and it is zero on common directions and on the complement of the two subspaces. Taking the largest absolute eigenvalue yields the identity, including the zero-angle and right-angle cases.

Apply the stated theorem with \(H=Q\), \(\widehat H=H_t\), and \(d=m\). Both matrices are real symmetric, \(1\leq m<p\), both selected spaces have dimension \(m\), and the population selected spectrum is the single value one. The required separation satisfies
\[
\Delta_t=1-\lambda_{m+1}(H_t)\geq g-\epsilon_t>0
\]
for large \(t\). The perturbation norm is \(\epsilon_t\). Consequently
\[
\|P_\lambda-P_*\|_{\mathrm{op}}
\leq\frac{\epsilon_t}{g-\epsilon_t}\longrightarrow0.
\]
This supplies the perturbation theorem's relevant statement and verifies all its application hypotheses. No statistical lemma or empirical rate is being invoked.

## step_004: Correct Complement Equation and Its Bound

Let \(S=[s_1\ \cdots\ s_m]\), and complete it to an orthogonal matrix \((S,Z)\), with \(Z\) spanning \(S_*^\perp\). In these coordinates,
\[
(S,Z)^\top Q(S,Z)=\begin{pmatrix}I_m&0\\0&B\end{pmatrix},\qquad
(S,Z)^\top A(S,Z)=\begin{pmatrix}A_{11}&A_{12}\\A_{21}&A_{22}\end{pmatrix},
\]
where \(A_{11}=\operatorname{diag}(\mu_1,\ldots,\mu_m)\), \(A_{21}=A_{12}^\top\), \(0\preceq B\preceq\beta I\), and each covariance block has operator norm at most \(a\). In particular, no off-diagonal covariance block is assumed to vanish.

For \(i\leq m\), write
\[
w_i^\lambda=Su_i^\lambda+Zv_i^\lambda,\qquad
\delta_i(\lambda)=\lambda_i(M_\lambda)-t.
\]
The eigenvalue perturbation bound applied to \(tQ+A\) and \(tQ\) gives \(|\delta_i(\lambda)|\leq a\), since \(\lambda_i(tQ)=t\) for these indices.

The two block equations are
\[
A_{11}u_i^\lambda+A_{12}v_i^\lambda=\delta_i(\lambda)u_i^\lambda,
\]
\[
L_i(\lambda)v_i^\lambda=A_{21}u_i^\lambda,\qquad
L_i(\lambda)=t(I-B)+\delta_i(\lambda)I-A_{22}.
\]
The term \(tI\) in the second equation is essential: it comes from substituting \(\lambda_i(M_\lambda)=t+\delta_i(\lambda)\) into the complement equation. This is the operator appearing in the original source at L000501-L000512.

For every complement vector, the preceding bounds give
\[
L_i(\lambda)\succeq(tg-2a)I.
\]
For sufficiently large \(t\), it is positive definite and
\[
\|L_i(\lambda)^{-1}\|_{\mathrm{op}}
\leq\frac1{tg-2a}=O(t^{-1}).
\]
Since \(\|u_i^\lambda\|_2\leq1\),
\[
\|v_i^\lambda\|_2\leq\frac{a}{tg-2a}=O(t^{-1})=O(\lambda^{-1}),\qquad
\|u_i^\lambda\|_2\longrightarrow1.
\]
Substitution into the first equation also gives
\[
\bigl(A_{11}+A_{12}L_i(\lambda)^{-1}A_{21}\bigr)u_i^\lambda
=\delta_i(\lambda)u_i^\lambda,
\]
with
\[
\|A_{12}L_i(\lambda)^{-1}A_{21}\|_{\mathrm{op}}
\leq\frac{a^2}{tg-2a}\longrightarrow0.
\]

## step_005: Ordered Limits and Signs

Fix an arbitrary sequence \(\lambda_n\to\infty\). The \(m\) shifted eigenvalues are bounded and the \(m\) coordinate vectors \(u_i^{\lambda_n}\) lie in a compact ball. Passing to a common subsequence, write their limits as \(d_i\) and \(u_i^*\). The complement coordinates tend to zero. Orthonormality of the original eigenvectors implies
\[
\langle u_i^{\lambda_n},u_j^{\lambda_n}\rangle
=\mathbf1_{i=j}-\langle v_i^{\lambda_n},v_j^{\lambda_n}\rangle
\longrightarrow\mathbf1_{i=j}.
\]
Thus \(u_1^*,\ldots,u_m^*\) form an orthonormal basis of \(\mathbb R^m\). Passing to the limit in the reduced equation yields
\[
A_{11}u_i^*=d_i u_i^*.
\]
Therefore the multiset \(\{d_1,\ldots,d_m\}\), including multiplicities, is the full spectrum of \(A_{11}\). Moreover, \(\delta_1(\lambda)\geq\cdots\geq\delta_m(\lambda)\), so \(d_1\geq\cdots\geq d_m\). It follows that \(d_i=\mu_i\) for every \(i\). Because the initial sequence was arbitrary, a contradiction-subsequence argument gives the full limits
\[
\lambda_i(M_\lambda)-2E\lambda\longrightarrow\mu_i.
\]
This eigenvalue conclusion is valid even with multiplicities, although the public task requests it only under simplicity.

Now assume \(\mu_1>\cdots>\mu_m\). The preceding argument shows that every subsequential limit of \(u_i^\lambda\) is \(+e_i\) or \(-e_i\). Choose the sign of each \(w_i^\lambda\) so that its inner product with the fixed vector \(s_i\) is nonnegative. For the sign-adjusted sequence, the negative limit is impossible. Compactness then gives \(u_i^\lambda\to e_i\), and hence
\[
w_i^\lambda=Su_i^\lambda+Zv_i^\lambda\longrightarrow Se_i=s_i.
\]
Equivalently, retain the original eigenvectors and put the chosen signs into \(\varepsilon_i(\lambda)\) as in the task. No continuity of the original eigenvector choices is required.

The argument covers \(E=1\), \(m=k\), zero compressed eigenvalues, and arbitrary fixed domain tie choices. Repeated compressed eigenvalues are allowed in the hard and projector assertions; simplicity is used only to select individual limiting directions. For \(m=1\), that simplicity condition is automatic. All five theorem-critical obligations are closed.
