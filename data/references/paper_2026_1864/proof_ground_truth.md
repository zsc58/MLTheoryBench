# Reference Proof

## Proof structure and source alignment

The public horizon consists of K positive-numbered rounds indexed 0,...,K-1. Its T_0 is the source initialization S_{-1}, and T_{k+1} is the source S_k. In particular, the regularizer used to produce y_{k+1} includes the contribution of h_k. Write
\[
Q(z)=\Pi(zz^\top),\qquad U_k=T_{k+1},\qquad A_k(z)=Q(z)+U_k,
\qquad a_k=\operatorname{tr}\sqrt{U_k},\quad a_{-1}=\varepsilon d.
\]
Thus \(\Phi_k(z)=R\operatorname{tr}\sqrt{A_k(z)}\). All \(U_k\) and \(A_k(z)\) are positive definite and belong to \(\mathcal V\).

The proof closes six groups of obligations: operator geometry and convexity; regularizer properties; exact shifted regret; preconditioner-gradient stability; negative-Bregman absorption; and ordinary regret with telescoping. The local source-symbol repairs for theory_004, theory_007, and theory_008 are incorporated below.

## Standard matrix facts used

For positive definite matrices \(A\preceq B\), operator monotonicity gives \(A^{1/2}\preceq B^{1/2}\) and \(B^{-1/2}\preceq A^{-1/2}\). The function \(F(A)=\operatorname{tr}\sqrt A\) is concave, with differential
\[
DF(A)[E]=\tfrac12\operatorname{tr}(A^{-1/2}E).
\]
Consequently,
\[
F(B)\le F(A)+\tfrac12\operatorname{tr}(A^{-1/2}(B-A)).
\]
These are the standard independent matrix facts indexed by theory_018. Every inverse below is applied to a positive definite matrix; every order comparison is between self-adjoint matrices. The remaining uses of Cauchy-Schwarz, trace cyclicity, and Young's inequality are elementary finite-dimensional identities or inequalities, and the needed forms are displayed below.

## 1. Operator geometry, duality, convexity, and differentiation

Since \(I\in\mathcal V\), symmetric multiplication implies \(H^2\in\mathcal V\). Polarizing squares gives \(HF+FH\in\mathcal V\). Induction then gives all powers of any \(H\in\mathcal V\). Polynomial interpolation on its finite spectrum shows that every real spectral function of \(H\) belongs to \(\mathcal V\), whenever that function is defined on its spectrum. In particular, the positive square roots and inverse powers used below belong to \(\mathcal V\).

For \(D\in\mathcal V\) and self-adjoint \(B\),
\[
\Pi(DBD)=D\Pi(B)D. \tag{1}
\]
Indeed, testing both sides against \(F\in\mathcal V\), projection self-adjointness and \(DFD\in\mathcal V\) give
\[
\operatorname{tr}(F\Pi(DBD))=\operatorname{tr}(DFD B)
=\operatorname{tr}(DFD\Pi(B))=\operatorname{tr}(F D\Pi(B)D).
\]
Both sides of (1) are in \(\mathcal V\). Also \(\operatorname{tr}Q(z)=\|z\|^2\), because \(\Pi(I)=I\).

The function q is a norm. In fact,
\[
q(z)=\sup_{\|v\|=1}\sqrt{z^\top\Pi(vv^\top)z},
\]
a supremum of seminorms, and trace preservation makes it positive for nonzero z. In particular \(q(z)\ge\|z\|/\sqrt d\), so its unit ball is compact.

We next prove, rather than assume, the duality needed for regret. Fix z and put \(Q=Q(z)\), \(C_t=(Q+tI)^{1/2}\) for \(t>0\). For \(q(u)\le1\), weighted Cauchy-Schwarz and \(\Pi(uu^\top)\preceq I\) give
\[
|z^\top u|^2\le(z^\top C_t^{-1}z)(u^\top C_tu)
\le\operatorname{tr}(C_t^{-1}Q)\operatorname{tr}C_t.
\]
Letting t decrease to zero bounds \(|z^\top u|\) by \(\operatorname{tr}\sqrt Q=q_*(z)\). Conversely, \(u_t=C_t^{-1}z\) satisfies
\[
\Pi(u_tu_t^\top)=C_t^{-1}QC_t^{-1}\preceq I,
\qquad z^\top u_t=\operatorname{tr}(C_t^{-1}Q)\longrightarrow\operatorname{tr}\sqrt Q.
\]
Thus
\[
\sup_{q(u)\le R}\langle-z,u\rangle=Rq_*(z). \tag{2}
\]
This includes z=0 and singular Q, since the limits are taken eigenvalue by eigenvalue.

For any positive definite \(U\in\mathcal V\), the function \(z\mapsto\operatorname{tr}\sqrt{Q(z)+U}\) is convex. To see this, first note the representation
\[
\operatorname{tr}\sqrt{Q(z)+U}
=\inf_{D\in\mathcal V,\ D\succ0}
\frac12\left(z^\top D^{-1}z+\operatorname{tr}(UD^{-1})+\operatorname{tr}D\right). \tag{3}
\]
For \(A=Q(z)+U\), expanding
\(\|D^{-1/2}A^{1/2}-D^{1/2}\|_F^2\ge0\)
proves the lower bound in (3); equality occurs at \(D=A^{1/2}\in\mathcal V\). Projection self-adjointness identifies \(\operatorname{tr}(Q(z)D^{-1})=z^\top D^{-1}z\).

The objective in (3) is jointly convex in \((z,D)\). Indeed,
\[
z^\top D^{-1}z=\sup_v\{2z^\top v-v^\top Dv\},
\]
which is a supremum of affine functions of \((z,D)\). Writing \(U\) as a sum of outer products proves convexity of \(\operatorname{tr}(UD^{-1})\) in the same way. Partial minimization over the convex positive-definite domain proves the claim.

Finally, trace differentiation, projection self-adjointness, and \(A_k(z)^{-1/2}\in\mathcal V\) give
\[
D\Phi_k(z)[v]
=\frac R2\operatorname{tr}\big(A_k(z)^{-1/2}\Pi(zv^\top+vz^\top)\big)
=R\langle A_k(z)^{-1/2}z,v\rangle.
\]
Hence
\[
\nabla\Phi_k(z)=R A_k(z)^{-1/2}z. \tag{4}
\]
Positive definiteness ensures differentiability everywhere.

## 2. Feasibility, dominance, increment control, and smoothness

Equation (1) gives
\[
\Pi\big(\nabla\Phi_k(z)\nabla\Phi_k(z)^\top\big)
=R^2 A_k(z)^{-1/2}Q(z)A_k(z)^{-1/2}\preceq R^2 I.
\]
Therefore \(q(\nabla\Phi_k(z))\le R\); all iterates, including \(y_0=0\), are feasible. Monotonicity also gives
\[
Rq_*(z)\le\Phi_k(z). \tag{5}
\]

For fixed \(Q\succeq0\), positive definite \(U\), and \(\Delta\succeq0\), integration of the trace derivative gives
\[
\begin{aligned}
0&\le R\operatorname{tr}\sqrt{Q+U+\Delta}-R\operatorname{tr}\sqrt{Q+U}\\
&=\frac R2\int_0^1\operatorname{tr}((Q+U+t\Delta)^{-1/2}\Delta)\,dt\\
&\le\frac R2\int_0^1\operatorname{tr}((U+t\Delta)^{-1/2}\Delta)\,dt\\
&=R\big(\operatorname{tr}\sqrt{U+\Delta}-\operatorname{tr}\sqrt U\big).
\end{aligned} \tag{6}
\]
In particular, for \(k\ge1\),
\[
0\le\Phi_k(z)-\Phi_{k-1}(z)\le R(a_k-a_{k-1}). \tag{7}
\]
This is the corrected difference-and-inequality form of the source upper-stability calculation.

Define \(B_f(u;v)=f(u)-f(v)-\langle\nabla f(v),u-v\rangle\), and \(\|v\|_W^2=v^\top Wv\). Along \(z+tv\), the second derivative of \(R F(Q(z+tv)+U_k)\) is at most
\[
R\operatorname{tr}(A_k(z)^{-1/2}\Pi(vv^\top))
=R v^\top A_k(z)^{-1/2}v
\le R v^\top U_k^{-1/2}v.
\]
The omitted term in this upper estimate is \(R D^2F(A_k(z))[A_k'(z),A_k'(z)]\le0\) by concavity of F. Integrating the second-derivative estimate proves
\[
0\le B_{\Phi_k}(u;v)\le\frac R2\|u-v\|_{U_k^{-1/2}}^2. \tag{8}
\]

We will also need the corresponding lower bound in gradient differences:
\[
B_{\Phi_k}(u;v)\ge\frac1{2R}
\|\nabla\Phi_k(u)-\nabla\Phi_k(v)\|_{U_k^{1/2}}^2. \tag{9}
\]
Here is a direct derivation. More generally, suppose a differentiable convex f satisfies \(B_f(a;b)\le(R/2)\|a-b\|_W^2\). The convex function \(g(w)=f(w)-\langle\nabla f(v),w\rangle\) is minimized at v. Apply its upper quadratic estimate at u to
\(u-R^{-1}W^{-1}(\nabla f(u)-\nabla f(v))\).
The resulting value is at most \(g(u)-(2R)^{-1}\|\nabla f(u)-\nabla f(v)\|_{W^{-1}}^2\), but at least \(g(v)\). This proves (9) with \(W=U_k^{-1/2}\).

## 3. Exact shifted-regret identity

Define
\[
\mathsf{Reg}_K^+=\sup_{q(u)\le R}\sum_{k=0}^{K-1}\langle h_k,y_{k+1}-u\rangle.
\]
By (2), its comparator contribution is \(Rq_*(M_{K-1})\). Since \(h_k=M_k-M_{k-1}\) and \(y_{k+1}=-\nabla\Phi_k(M_k)\),
\[
\langle h_k,y_{k+1}\rangle
=\Phi_k(M_{k-1})-\Phi_k(M_k)-B_{\Phi_k}(M_{k-1};M_k).
\]
Summing gives the exact identity
\[
\begin{aligned}
\mathsf{Reg}_K^+
={}&\Phi_0(0)+Rq_*(M_{K-1})-\Phi_{K-1}(M_{K-1})\\
&+\sum_{k=1}^{K-1}\big[\Phi_k(M_{k-1})-\Phi_{k-1}(M_{k-1})\big]
-\sum_{k=0}^{K-1}B_{\Phi_k}(M_{k-1};M_k).
\end{aligned} \tag{10}
\]
Empty sums here and below vanish, so K=1 is covered.

## 4. Preconditioner-gradient stability

For positive definite \(U\preceq V\) in \(\mathcal V\), fix z and set
\[
Q=Q(z),\quad A=Q+U,\quad B=Q+V,\quad D=B^{-1/2}-A^{-1/2}.
\]
Write \(\Phi_U(z)=R\operatorname{tr}\sqrt{Q(z)+U}\). Using \(V^{1/2}\preceq B^{1/2}\), the gradient formula, and \(DB^{1/2}D\in\mathcal V\), we obtain
\[
\begin{aligned}
R^{-2}\|\nabla\Phi_V(z)-\nabla\Phi_U(z)\|_{V^{1/2}}^2
&\le z^\top DB^{1/2}Dz\\
&=\operatorname{tr}(DB^{1/2}DQ)\\
&\le\operatorname{tr}(DB^{1/2}DA).
\end{aligned}
\]
The last inequality uses \(DB^{1/2}D\succeq0\) and \(Q\preceq A\). Expanding and using trace cyclicity, without assuming commutativity, gives
\[
\operatorname{tr}(DB^{1/2}DA)
=\operatorname{tr}B^{1/2}-2\operatorname{tr}A^{1/2}+\operatorname{tr}(B^{-1/2}A)
\le\operatorname{tr}B^{1/2}-\operatorname{tr}A^{1/2}.
\]
Indeed, \(B^{-1/2}\preceq A^{-1/2}\) implies \(\operatorname{tr}(B^{-1/2}A)\le\operatorname{tr}A^{1/2}\). Applying (6) therefore proves
\[
\|\nabla\Phi_V(z)-\nabla\Phi_U(z)\|_{V^{1/2}}^2
\le R^2\big(\operatorname{tr}\sqrt V-\operatorname{tr}\sqrt U\big). \tag{11}
\]

## 5. Absorbing changes into negative Bregman terms

For \(k\ge1\), set
\[
w_k=\nabla\Phi_k(M_k)-\nabla\Phi_k(M_{k-1}),\qquad
e_k=\nabla\Phi_k(M_{k-1})-\nabla\Phi_{k-1}(M_{k-1}).
\]
Then \(y_{k+1}-y_k=-(w_k+e_k)\). In the \(U_k^{1/2}\) metric,
\[
\|w_k\|^2\ge\tfrac12\|y_{k+1}-y_k\|^2-\|e_k\|^2.
\]
Combining this with (9) and (11) yields
\[
B_{\Phi_k}(M_{k-1};M_k)
\ge\frac1{4R}\|y_{k+1}-y_k\|_{U_k^{1/2}}^2-\frac R2(a_k-a_{k-1}). \tag{12}
\]
For k=0, \(\nabla\Phi_0(0)=0\), so (9) directly gives
\[
B_{\Phi_0}(0;M_0)\ge\frac1{2R}\|y_1-y_0\|_{U_0^{1/2}}^2.
\]
Thus the weaker coefficient \(1/(4R)\) also holds at k=0 without an error term.

In (10), discard the nonpositive terminal term using (5), bound the regularizer increments by (7), and apply (12). The trace increments telescope, giving
\[
\begin{aligned}
\mathsf{Reg}_K^+
&\le\Phi_0(0)+\tfrac32R(a_{K-1}-a_0)
-\sum_{k=0}^{K-1}\frac1{4R}\|y_{k+1}-y_k\|_{U_k^{1/2}}^2\\
&\le\Phi_0(0)+\tfrac32R\operatorname{tr}\sqrt{T_K}
-\sum_{k=0}^{K-1}\frac1{4R}\|y_{k+1}-y_k\|_{U_k^{1/2}}^2.
\end{aligned} \tag{13}
\]
The signs in the decomposition follow from the negative-gradient update; in particular substituting for \(\nabla\Phi_k(M_k)\) produces a plus sign before \(y_{k+1}\).

## 6. Ordinary regret and trace telescoping

The correction to shifted regret is independent of the comparator, so
\[
\mathsf{Reg}_K=\mathsf{Reg}_K^++\sum_{k=0}^{K-1}\langle h_k,y_k-y_{k+1}\rangle.
\]
Weighted Young's inequality gives
\[
\langle h_k,y_k-y_{k+1}\rangle
\le R\|h_k\|_{U_k^{-1/2}}^2
+\frac1{4R}\|y_{k+1}-y_k\|_{U_k^{1/2}}^2.
\]
The second sum cancels that in (13). Since \(U_k=T_{k+1}\) contains the current gradient contribution, projection self-adjointness gives
\[
\|h_k\|_{U_k^{-1/2}}^2
=\operatorname{tr}\big(T_{k+1}^{-1/2}\Pi(h_kh_k^\top)\big)
=\operatorname{tr}\big(T_{k+1}^{-1/2}(T_{k+1}-T_k)\big).
\]
Concavity of F at \(T_{k+1}\), with comparison point \(T_k\), implies
\[
\operatorname{tr}\big(T_{k+1}^{-1/2}(T_{k+1}-T_k)\big)
\le2\big(\operatorname{tr}\sqrt{T_{k+1}}-\operatorname{tr}\sqrt{T_k}\big).
\]
Therefore
\[
\sum_{k=0}^{K-1}\|h_k\|_{U_k^{-1/2}}^2
\le2\big(\operatorname{tr}\sqrt{T_K}-\varepsilon d\big). \tag{14}
\]
This is the required square-root telescoping estimate, valid also for noncommuting successive matrices.

Finally, if \(\lambda_i\ge0\) are the eigenvalues of \(Q(h_0)\), then
\[
\Phi_0(0)=R\operatorname{tr}\sqrt{T_1}
=R\sum_i\sqrt{\varepsilon^2+\lambda_i}
\le R\varepsilon d+Rq_*(h_0). \tag{15}
\]
Combining (13)-(15) and discarding the nonpositive term \(-2R\varepsilon d\) gives
\[
\mathsf{Reg}_K\le R\varepsilon d+Rq_*(h_0)+\frac72R\operatorname{tr}\sqrt{T_K}
\le\frac72R\left(\varepsilon d+q_*(h_0)+\operatorname{tr}\sqrt{T_K}\right).
\]
Thus C=7/2 is universal, independent of dimension, horizon, subspace, radius, initialization, and gradient values. No uniform gradient bound was used.

For each fixed dimension and radius, the explicit initialization contribution tends to zero with positive epsilon. Moreover, writing \(G=\sum_{k=0}^{K-1}Q(h_k)\), the same eigenvalue inequality gives \(\operatorname{tr}\sqrt{\varepsilon^2I+G}\le\varepsilon d+\operatorname{tr}\sqrt G\). Thus no hidden blow-up in the terminal trace term obstructs choosing epsilon arbitrarily small. All-zero gradients and the single-round case are included; epsilon=0 itself is not needed.
