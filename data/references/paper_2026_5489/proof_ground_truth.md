# Reference Proof

## Proof Structure

The obligations are: establish the model's local differentiability and normalized forward map on the sparse manifold; prove vanishing of every inactive full-parameter gradient and scalarity of the active gradients; derive and dominate the scalar loss derivative; analyze the exact discrete recursion, including its zero initialization; and prove the positive limiting loss, its rate, and the pointwise output limit. Each obligation is derived below. The symmetry fact used in the second step is proved explicitly, including the local correction to the source's real-field Schur justification.

## Complete Proof

### 1. Definition closure, forward reduction, and local differentiability

Write \(S=XX^{\mathsf T}\), \(P=P_X\), and \(r=r(X)\). Unit columns give \(\operatorname{tr}S=n\) and \(\|S\|_2\le n\). The inverse-smallest-eigenvalue assumption implies \(\lambda_d(S)>0\) almost surely, so \(S^La\ne0\) almost surely. The target projector is measurable: since \(\lambda_1(S)>0\), the spectral theorem gives
\[
P=\lim_{m\to\infty}(S/\lambda_1(S))^m.
\]
The eigenvalues are continuous functions of \(S\), so this also establishes measurability of the projector; \(r(X)=\operatorname{tr}P_X\) is measurable. No constant-multiplicity assumption is needed. All losses under consideration are bounded by one wherever their normalizations are defined.

At a sparse point
\[
W(w)=\begin{pmatrix}0&wI_d\\0&0\end{pmatrix},\qquad
V(v)=\begin{pmatrix}0&0\\vI_d&0\end{pmatrix},\qquad \rho=wv\ge0,
\]
suppose a layer input is \(\operatorname{diag}(X,a_\ell)\), with \(\|a_\ell\|=1\). For each data token, \(W(w)(x_j,0)^{\mathsf T}=0\), so its residual update vanishes and normalization leaves it unchanged. For the query, block multiplication gives pre-normalization column
\[
\binom{0}{(I+\rho S)a_\ell}.
\]
Its norm is at least one because \(S\succeq0\) and \(\rho\ge0\). Hence
\[
a_{\ell+1}=\frac{(I+\rho S)a_\ell}{\|(I+\rho S)a_\ell\|}.
\]
Starting with \(a_0=a\), cancellation of the positive normalization factors gives
\[
u_L(X,a;W(w),V(v))=\frac{(I+\rho S)^La}{\|(I+\rho S)^La\|},\qquad
\mathcal L(W(w),V(v))=R_L(wv).
\]
In particular, the extracted prediction is a unit vector at these sparse points; this is not asserted for general parameters.

For each fixed sparse point with \(wv\ge0\), every baseline pre-normalization column has norm at least one, uniformly over the compact input space \((\mathbb S^{d-1})^n\times\mathbb S^{d-1}\). Continuity and induction through the finite number of layers therefore give an open parameter neighborhood in which all these norms are at least \(1/2\), uniformly over the input space. The update is polynomial before normalization, and
\[
D N(z)[h]=\frac{1}{\|z\|}\left(I-\frac{zz^{\mathsf T}}{\|z\|^2}\right)h,
\qquad N(z)=z/\|z\|.
\]
Consequently, on a smaller closed neighborhood, the network's parameter derivatives have a deterministic bound. The sample loss derivative is bounded as well because \(\|P\|_2\le1\) and the extracted output has norm at most one. The bound may depend on \(d,n,L,w,v\), but not on the sample.

We use dominated convergence in the form that almost-sure convergence under a common integrable absolute bound permits exchange of limit and expectation. Applied to parameter difference quotients, with the derivative bounds above and the mean-value formula, it justifies differentiation of the population loss in all parameter directions. Thus the full population gradient exists in a neighborhood of every such sparse point. The inverse-eigenvalue moment is not needed for this local argument; it will be used for the large-\(\rho\) limit.

### 2. Full-gradient invariance and the scalar recursion

Consider arbitrary perturbations \(\dot W,\dot V\) satisfying \(\dot W_{12}=\dot V_{21}=0\). At layer \(\ell\), write the first variation around the baseline \(\operatorname{diag}(X,a_\ell)\) as
\[
\dot E^{(\ell)}=\begin{pmatrix}A_\ell&b_\ell\\C_\ell&e_\ell\end{pmatrix}.
\]
Here \(A_\ell,C_\ell\) have \(n\) columns and \(b_\ell,e_\ell\) are query variations. We prove \(A_\ell=0\) and \(e_\ell=0\) for every layer. The other variation blocks need not vanish. Both claimed equalities hold at layer zero.

Let \(U(E;W,V)=E+VEE^{\mathsf T}WE\). Its first variation is
\[
\dot U=\dot E+\dot VEE^{\mathsf T}WE
+V(\dot EE^{\mathsf T}+E\dot E^{\mathsf T})WE
+VEE^{\mathsf T}\dot WE+VEE^{\mathsf T}W\dot E.
\]
For a baseline data token, \(We_j=0\), and the top block row of \(V\) vanishes. Its top pre-normalization variation is therefore \((A_\ell)_{:,j}\). Differentiating normalization at \((x_j,0)^{\mathsf T}\) gives
\[
(A_{\ell+1})_{:,j}=(I-x_jx_j^{\mathsf T})(A_\ell)_{:,j}=0.
\]
For the query, the bottom pre-normalization variation is
\[
e_\ell+w\dot V_{21}Sa_\ell
+\rho(A_\ell X^{\mathsf T}+XA_\ell^{\mathsf T})a_\ell
+vS\dot W_{12}a_\ell+\rho Se_\ell.
\]
It is zero under the induction hypothesis. At the baseline query, the upper block is zero, so its upper-block perturbation does not contribute to the bottom-block normalization derivative. Thus \(e_{\ell+1}=0\). This completes the induction and proves \(\dot u_L=0\) for every inactive perturbation. By the differentiation argument in step 1, every inactive population-gradient block vanishes.

For the active blocks, let \(\mathcal F(A,B)\) denote the loss with \(W_{12}=A\), \(V_{21}=B\), and all inactive blocks zero. For \(Q\in O(d)\), simultaneous transformations
\[
(X,a,A,B)\mapsto(QX,Qa,QAQ^{\mathsf T},QBQ^{\mathsf T})
\]
rotate the prediction by \(Q\), and \(P_{QX}=QP_XQ^{\mathsf T}\). The full-column normalizer commutes with the block rotation \(\operatorname{diag}(Q,Q)\), so this equivariance holds through all shared loops. Independence, spherical uniformity, and the rotation-invariant data law imply
\[
\mathcal F(A,B)=\mathcal F(QAQ^{\mathsf T},QBQ^{\mathsf T}).
\]
At \((A,B)=(wI_d,vI_d)\), differentiation gives \(G=Q^{\mathsf T}GQ\) for either active gradient \(G\).

The specific symmetry fact needed here is: if \(d\ge3\) and a real matrix commutes with every rotation in \(SO(d)\), then it is scalar. To prove it, for any distinct indices \(i,j\), choose \(k\) distinct from both. The diagonal rotation that changes the signs of coordinates \(i,k\) and fixes the others has determinant one. Conjugation by it changes the sign of the \((i,j)\) entry, so that entry must be zero. All off-diagonal entries therefore vanish. Conjugation by a quarter-turn in any coordinate plane then exchanges the corresponding diagonal entries, which must be equal. This proves the fact without the invalid inference that real irreducibility alone implies a scalar commutant.

Consequently the active gradients are \(c_AI_d\) and \(c_BI_d\). Differentiating the restricted objective gives
\[
dc_A=\langle c_AI_d,I_d\rangle_F=vR_L'(wv),\qquad
dc_B=wR_L'(wv).
\]
At \(wv=0\), the same identities follow from one-sided differentiation of the restricted formula and differentiability of the ambient loss. Thus
\[
\nabla_{W_{12}}\mathcal L=\frac{v}{d}R_L'(wv)I_d,\qquad
\nabla_{V_{21}}\mathcal L=\frac{w}{d}R_L'(wv)I_d.
\]
Together with the inactive-gradient calculation, these are the asserted full-gradient formulas. Once the sign of \(R_L'\) is established below, induction from \(w_0=0,v_0=1\) proves that the iterates stay in the nonnegative-product sparse manifold and satisfy the exact scalar updates.

### 3. Scalar derivative and discrete dynamics

Condition on \(X\) and choose an orthonormal eigenbasis of \(S\), writing
\[
S=\sum_{i=1}^d\lambda_i v_iv_i^{\mathsf T},\qquad
a=\sum_{i=1}^dc_iv_i,
\]
where \(\lambda_1=\cdots=\lambda_r>\lambda_{r+1}\ge\cdots\ge\lambda_d>0\). The following expressions are independent of the chosen basis within repeated eigenspaces. Set
\[
p_i(\rho)=\frac{c_i^2(1+\rho\lambda_i)^{2L}}{\sum_kc_k^2(1+\rho\lambda_k)^{2L}}.
\]
The sample loss is \(\ell_L(\rho)=1-\sum_{i\le r}p_i(\rho)\). The quotient rule yields
\[
p_i'(\rho)=2Lp_i(\rho)\left(\frac{\lambda_i}{1+\rho\lambda_i}-\sum_kp_k(\rho)\frac{\lambda_k}{1+\rho\lambda_k}\right),
\]
and therefore
\[
\ell_L'(\rho)=-2L\sum_{i\le r}\sum_{j>r}p_i(\rho)p_j(\rho)
\frac{\lambda_1-\lambda_j}{(1+\rho\lambda_1)(1+\rho\lambda_j)}.
\]
For every fixed admissible \(X\), both its principal subspace and its orthogonal complement are nonzero proper subspaces. A uniform spherical vector lies in either proper subspace with probability zero. Thus its projections onto both are nonzero almost surely, and the displayed derivative is strictly negative almost surely.

Because \(\lambda_1\le n\), all denominators are at least one, and \(\sum_{i\le r,j>r}p_ip_j\le1\),
\[
|\ell_L'(\rho)|\le2Ln\qquad(\rho\ge0).
\]
This deterministic bound justifies differentiation under expectation and continuity of the derivative by dominated convergence. Hence \(R_L\in C^1([0,\infty))\), interpreted one-sided at zero, and
\[
R_L'(\rho)<0,\qquad |R_L'(\rho)|\le2Ln.
\]

As \(\rho\to\infty\),
\[
p_i(\rho)\longrightarrow p_i^{(\infty)}:=\frac{c_i^2\lambda_i^{2L}}{\sum_kc_k^2\lambda_k^{2L}}.
\]
Also,
\[
0\le\rho^2\frac{\lambda_1-\lambda_j}{(1+\rho\lambda_1)(1+\rho\lambda_j)}
\le\frac{\lambda_1-\lambda_j}{\lambda_1\lambda_j}
\le\frac1{\lambda_d}.
\]
It follows that \(-\rho^2\ell_L'(\rho)\) is dominated by \(2L/\lambda_d\), whose expectation is finite by the stated assumption. Thus
\[
-\rho^2R_L'(\rho)\longrightarrow
2L\,\mathbb E\left[\sum_{i\le r(X)}\sum_{j>r(X)}p_i^{(\infty)}p_j^{(\infty)}
\frac{\lambda_1-\lambda_j}{\lambda_1\lambda_j}\right]=\Upsilon_1.
\]
The same domination proves finiteness. The strict spectral gap, positive eigenvalues, and the two nonzero query projections make the limiting integrand positive almost surely. Therefore \(0<\Upsilon_1<\infty\), with dependence on \(L\) and the fixed data law, and
\[
R_L'(\rho)=-\Upsilon_1\rho^{-2}+o(\rho^{-2}).
\]

Put \(\kappa=\eta/d\) and \(G_t=R_L'(\rho_t)<0\). The gradient formulas give
\[
w_{t+1}=w_t-\kappa v_tG_t,\qquad v_{t+1}=v_t-\kappa w_tG_t.
\]
Starting with \(w_0=0,v_0=1\), induction gives \(w_t\ge0\), \(v_t\ge1\), and both sequences nondecreasing; moreover \(w_1=-\kappa R_L'(0)>0\). These signs ensure \(\rho_t\ge0\), closing the full-parameter invariance induction. The bounds on \(G_t\) ensure each finite-time update is finite, and step 1 ensures its population gradient is defined.

Expansion gives
\[
\rho_{t+1}-\rho_t=-\kappa G_t(w_t^2+v_t^2)+\kappa^2\rho_tG_t^2>0.
\]
If \(\rho_t\) were bounded by \(B\), continuity and strict negativity of \(R_L'\) would give \(-G_t\ge c_B>0\). Since \(v_t\ge1\), the last display would imply \(\rho_{t+1}-\rho_t\ge\kappa c_B\), a contradiction. Thus \(\rho_t\to\infty\).

Define \(\Delta_t=v_t^2-w_t^2\). The exact recursion gives
\[
\Delta_{t+1}=(1-\kappa^2G_t^2)\Delta_t.
\]
The step-size bound and \(|G_t|\le2Ln\) imply \(0\le\kappa|G_t|\le1\), including the allowed endpoint. Since \(\Delta_0=1\), we have \(0\le\Delta_t\le1\). The divergent product and bounded difference of squares imply that both factors diverge. Hence
\[
1-(w_t/v_t)^2=\Delta_t/v_t^2\longrightarrow0,
\]
so \(w_t/v_t\to1\) and \(w_t^2+v_t^2=2\rho_t+o(\rho_t)\).

Substitution of the derivative asymptotic into the product increment gives
\[
\rho_{t+1}-\rho_t=\frac{2\kappa\Upsilon_1}{\rho_t}+o(\rho_t^{-1}).
\]
Consequently,
\[
\rho_{t+1}^2-\rho_t^2
=2\rho_t(\rho_{t+1}-\rho_t)+(\rho_{t+1}-\rho_t)^2
=4\kappa\Upsilon_1+o(1).
\]
Telescoping and averaging the convergent increments yield
\[
\rho_t\sim(4\eta\Upsilon_1t/d)^{1/2}.
\]
Balancing now gives the stronger individual asymptotics
\[
w_t,v_t=(4\eta\Upsilon_1t/d)^{1/4}(1+o(1)),
\]
which imply the requested quarter-power bounds.

### 4. Positive limiting loss, convergence rate, and learned output

For any fixed unit-column \(X\) with \(S\) positive definite and any unit vector \(a\),
\[
\rho^{-L}(I+\rho S)^La=(\rho^{-1}I+S)^La\longrightarrow S^La\ne0.
\]
Continuity of normalization gives convergence of the normalized vector to \(S^La/\|S^La\|\). The corresponding sample losses are bounded by one, so dominated convergence shows
\[
R_L(\rho)\longrightarrow R_L(\infty).
\]
Under the training law, the query has a nonzero projection on the nonprincipal subspace almost surely. All eigenvalues on that subspace are positive; therefore \(S^La\) retains a nonzero component there. Its squared normalized distance from the principal subspace is positive almost surely, proving \(R_L(\infty)>0\).

The fundamental theorem of calculus on finite intervals, followed by the established loss limit, gives
\[
R_L(\rho)-R_L(\infty)=\int_\rho^\infty -R_L'(s)\,ds.
\]
For any \(\varepsilon>0\), the derivative asymptotic bounds the integrand between \((\Upsilon_1-\varepsilon)s^{-2}\) and \((\Upsilon_1+\varepsilon)s^{-2}\) for all sufficiently large \(s\). Integrating these bounds proves
\[
R_L(\rho)-R_L(\infty)=\frac{\Upsilon_1}{\rho}+o(\rho^{-1}).
\]
Using the exact restricted-loss identity and the product asymptotic,
\[
\mathcal L(W^{(t)},V^{(t)})-R_L(\infty)
=\left(\frac{d\Upsilon_1}{4\eta}\right)^{1/2}t^{-1/2}(1+o(1)).
\]
This proves both stated loss bounds with all parameters and the data law fixed.

Finally, the forward formula holds for every deterministic unit-column input, independently of whether it belongs to the training support. Since the learned scalar sequence satisfies \(\rho_t\to\infty\), the pointwise calculation above proves the asserted prediction limit for every such positive-definite input and every unit query. No nonorthogonality restriction on that fixed query is needed, because positive definiteness ensures \(S^La\ne0\). All theorem-critical obligations are closed.
