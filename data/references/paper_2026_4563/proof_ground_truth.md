# Reference Proof

## Obligations

We establish: (1) the exact expected-Hessian and batch-fluctuation identities at population minima; (2) selection of minimum fluctuation by every convergent sequence of entropic global minimizers; (3) the minimum-fluctuation value and the effective products of every minimizer, including unused hidden directions; (4) the selected trace; (5) the minimum possible trace and an attaining construction; and (6) orthogonal similarity of the selected expected Hessians. The zero-teacher case is included. No specialized external characterization is assumed.

## 1. Population minima and derivative identities

Put \(X=\Sigma_x^{1/2}\), \(Q=\Sigma_\varepsilon^{1/2}\), and \(P=W_D\cdots W_1\). Independence and zero means give
\[
L(\theta)=\tfrac12\|(P-V)X\|_F^2+\tfrac12E.
\]
Since the widths permit a factorization of \(V\) and \(X\) is invertible, the population minimum manifold is exactly \(\mathcal M=\{\theta:P=V\}\).

Let \(J(x)\) be the output-by-parameter Jacobian. Direct differentiation gives
\[
\nabla\ell=J^\top(f-y),\qquad
\nabla^2\ell=J^\top J+\sum_a(f-y)_a\nabla^2 f_a.
\]
At \(\theta\in\mathcal M\), the residual is \(-\varepsilon\), and the expected second term vanishes. Consequently
\[
H(\theta)=\mathbb E_x[J^\top J],\qquad T(\theta)=\mathbb E_x\|J\|_F^2.
\]
The single-example gradient has zero mean, so independence within an iid batch gives
\[
mS(\theta)=\mathbb E\|\nabla\ell\|^2
=\mathbb E_x\operatorname{Tr}(\Sigma_\varepsilon JJ^\top).
\]
These quantities are finite on \(\mathcal M\) under the given second moments.

For later use set
\[
A_k=W_D\cdots W_{k+1},\qquad B_k=W_{k-1}\cdots W_1,
\]
with \(A_D=I_{d_y}\) and \(B_1=I_{d_x}\). Differentiation with respect to one layer gives
\[
T(\theta)=\sum_{k=1}^D\|A_k\|_F^2\|B_kX\|_F^2.
\]
At a population minimizer it also gives
\[
mS(\theta)=\sum_{k=1}^D\|QA_k\|_F^2\|B_kX\|_F^2.
\]
Indeed, that layer's gradient is \(-A_k^\top\varepsilon(B_kx)^\top\), and independence factors its squared-norm expectation.

## 2. The selection limit needs no fourth-moment assumption

The nonnegative expectation defining \(S\) is allowed to be infinite away from \(\mathcal M\). It is lower semicontinuous: for a convergent parameter sequence, each batch-gradient squared norm converges pointwise, and Fatou's lemma applies. The population loss is continuous.

Suppose \(\eta_n\downarrow0\), \(\theta_n\in\arg\min F_{\eta_n}\), and \(\theta_n\to\bar\theta\). For any \(\theta\in\mathcal M\), its fluctuation is finite, and optimality gives
\[
0\le L(\theta_n)-L(\theta)
\le\frac{\eta_n}{4}\bigl(S(\theta)-S(\theta_n)\bigr)
\le\frac{\eta_n}{4}S(\theta).
\]
It follows that \(L(\bar\theta)=\min L\). The same comparison implies \(S(\theta_n)\le S(\theta)\), whence
\[
S(\bar\theta)\le\liminf_n S(\theta_n)\le S(\theta).
\]
Thus every selected limit minimizes \(S\) on \(\mathcal M\). Coercivity of the factorized loss is neither true nor needed: convergence is part of the definition of a selected point.

## 3. Minimum fluctuation and all effective products

First assume \(G>0\). Write
\[
M=QVX=L\mathsf S R^\top,
\]
where \(\mathsf S\) is positive diagonal of size \(r\). For each internal cut define
\[
P_k=W_k\cdots W_1X,\qquad Z_k=QW_D\cdots W_{k+1},
\]
and set \(P_0=X\), \(Z_D=Q\). On \(\mathcal M\), \(Z_kP_k=M\). Let
\[
u_k=\|Z_k\|_F^2,\quad v_k=\|P_k\|_F^2,\quad q_k=u_kv_{k-1},
\]
so \(u_D=E\), \(v_0=C\), and \(mS=\sum_kq_k\).

For any factorization \(AB=M\),
\[
G=\operatorname{Tr}(L^\top ABR)
=\langle A^\top L,BR\rangle_F
\le\|A^\top L\|_F\|BR\|_F
\le\|A\|_F\|B\|_F.
\]
Therefore \(u_kv_k\ge G^2\), and
\[
\prod_{k=1}^Dq_k=EC\prod_{k=1}^{D-1}u_kv_k
\ge EC G^{2(D-1)}.
\]
AM-GM gives \(mS\ge Dh\), where
\[
h=(ECG^{2(D-1)})^{1/D}.
\]

This bound is attained. Choose column isometries \(U_k\in\mathbb R^{d_k\times r}\), and set
\[
\alpha=G^{-(D-2)/(2D)}C^{(D-1)/(2D)}E^{-1/(2D)},
\quad
\beta=G^{-(D-2)/(2D)}E^{(D-1)/(2D)}C^{-1/(2D)},
\quad
\gamma=G^{1/D}(EC)^{-1/(2D)}.
\]
Take
\[
W_1X=\alpha U_1\mathsf S^{1/2}R^\top,\qquad
QW_D=\beta L\mathsf S^{1/2}U_{D-1}^\top,
\]
\[
W_k=\gamma U_kU_{k-1}^\top\quad(2\le k\le D-1).
\]
The middle list is empty when \(D=2\). Since \(\alpha\beta\gamma^{D-2}=1\), the product is \(V\). The boundary fluctuation terms are
\[
q_1=\beta^2\gamma^{2(D-2)}GC=h,
\qquad
q_D=E\alpha^2\gamma^{2(D-2)}G=h.
\]
For every intermediate layer,
\[
q_k=\alpha^2\beta^2\gamma^{2(D-3)}G^2=\gamma^{-2}G^2=h.
\]
Thus these factors attain \(Dh\).

Now consider any minimizer, not only the constructed representatives. Equality in the lower bound forces \(q_k=h\) for every layer and \(u_kv_k=G^2\) for every cut. Equality in the displayed trace inequalities for \(A=Z_k\), \(B=P_k\) implies
\[
Z_k=LL^\top Z_k,\qquad P_k=P_kRR^\top,
\qquad P_kR=c_kZ_k^\top L
\]
for some \(c_k>0\). Since \(Z_kP_k=L\mathsf S R^\top\),
\[
c_kL^\top Z_kZ_k^\top L=\mathsf S.
\]
Put \(a_k=c_k^{-1/2}\) and
\[
U_k=a_k^{-1}Z_k^\top L\mathsf S^{-1/2}.
\]
Then \(U_k^\top U_k=I_r\), and
\[
Z_k=a_kL\mathsf S^{1/2}U_k^\top,
\qquad
P_k=a_k^{-1}U_k\mathsf S^{1/2}R^\top.
\]
Furthermore, \(q_1=h\) and the intermediate equalities determine
\[
a_1^2=\frac h{GC},\qquad
\frac{a_k^2}{a_{k-1}^2}=\frac h{G^2},\qquad
 a_k^2=\frac h{GC}\left(\frac h{G^2}\right)^{k-1}.
\]
These are universal statements about effective products. They do not assert that unused components of every raw hidden weight vanish.

## 4. Selected sharpness

Let \(K=\operatorname{Tr}(\Sigma_\varepsilon^{-1}L\mathsf S L^\top)\). For \(k<D\), \(A_k=Q^{-1}Z_k\), so \(\|A_k\|_F^2=a_k^2K\). The first layer contributes
\[
a_1^2KC=\frac hG K.
\]
Each intermediate layer contributes
\[
a_k^2K\,a_{k-1}^{-2}G=\frac hG K.
\]
The final layer contributes \(d_yv_{D-1}=d_yh/E\), because \(q_D=Ev_{D-1}=h\). Consequently
\[
T_{\rm sel}=(D-1)\frac hG K+d_y\frac hE
=(D-1)G^{(D-2)/D}(EC)^{1/D}K
+d_y\frac{G^{2(D-1)/D}C^{1/D}}{E^{(D-1)/D}}.
\]

## 5. Minimum sharpness among all population minima

Apply the same lower-bound and attaining-construction argument to the trace functional with \(Q=I_{d_y}\). Now \(E=d_y\), the target product is \(VX=\widehat L\widehat{\mathsf S}\widehat R^\top\), and its nuclear norm is \(g=\operatorname{Tr}\widehat{\mathsf S}\). This gives
\[
T(\theta)\ge D(d_yCg^{2(D-1)})^{1/D}.
\]
For explicit attainment when \(g>0\), use
\[
W_1X=\widehat\alpha U_1\widehat{\mathsf S}^{1/2}\widehat R^\top,
\qquad W_D=\widehat\beta\widehat L\widehat{\mathsf S}^{1/2}U_{D-1}^\top,
\qquad W_k=\widehat\gamma U_kU_{k-1}^\top,
\]
where
\[
\widehat\alpha=g^{-(D-2)/(2D)}C^{(D-1)/(2D)}d_y^{-1/(2D)},\quad
\widehat\beta=g^{-(D-2)/(2D)}d_y^{(D-1)/(2D)}C^{-1/(2D)},\quad
\widehat\gamma=g^{1/D}(d_yC)^{-1/(2D)}.
\]
The preceding product and layer-term verification applies verbatim. Hence
\[
T_{\min}=Dg^{2(D-1)/D}(d_yC)^{1/D}.
\]
Here balance means equality of the layer trace contributions, not an additional claim that the unscaled neighboring weight Gram matrices coincide.

## 6. Orthogonal similarity without a raw-weight orbit assumption

At a population minimizer the Hessian quadratic form is
\[
\langle\Delta,H(\theta)\Delta\rangle
=\left\|\sum_{k=1}^DA_k\Delta_kP_{k-1}\right\|_F^2,
\]
where \(\Delta_k\) has the shape of \(W_k\). This follows from the first variation of the network and the input covariance.

For two minimum-fluctuation population minimizers, the effective-product characterization uses the same \(L,\mathsf S,R\) and the same positive scalars \(a_k\). Extend their cut isometries to orthogonal maps \(O_k\) satisfying \(U_k'=O_kU_k\). Set \(O_0=I_{d_x}\), \(O_D=I_{d_y}\). Then
\[
Z_k'=Z_kO_k^\top,\qquad P_k'=O_kP_k,
\]
and therefore \(A_k'=A_kO_k^\top\) for \(k<D\), with the corresponding boundary identities.

The parameter-perturbation map
\[
(\mathcal O\Delta)_k=O_k\Delta_kO_{k-1}^\top
\]
is orthogonal for the sum of layer Frobenius inner products. Substitution shows
\[
\sum_kA_k'(\mathcal O\Delta)_kP_{k-1}'
=\sum_kA_k\Delta_kP_{k-1}.
\]
Thus \(\mathcal O^\top H(\theta')\mathcal O=H(\theta)\), proving the required similarity. In particular, this conclusion remains valid when the two raw weight collections have different unused components and are not themselves related by internal rotations.

## 7. Zero teacher

If \(G=0\), invertibility of \(Q,X\) implies \(V=0\). All-zero weights have population loss \(E/2\), fluctuation zero, and Hessian zero because \(D\ge2\). Hence the minimum fluctuation on \(\mathcal M\) and the minimum trace are both zero. Every selected limit has zero fluctuation by Section 2. At such a point,
\[
mS=\mathbb E_x\operatorname{Tr}(\Sigma_\varepsilon JJ^\top)
\ge\lambda_{\min}(\Sigma_\varepsilon)\mathbb E_x\|J\|_F^2,
\]
so its positive-semidefinite expected Hessian is zero. Both formulas have the specified zero value, and all selected Hessians are orthogonally similar.

All obligations are closed by the displayed derivations, elementary finite-dimensional linear algebra, AM-GM, Cauchy-Schwarz, and Fatou's lemma. There is no unresolved specialized external dependency.
