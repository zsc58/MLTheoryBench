# Reference Proof

## Contract and proof obligations

The operator constraint is nonnegativity of its quadratic form: \(Q+Q^*\succeq0\). It does not impose \(Q=Q^*\). Likewise, the coefficient cone is \(\Lambda+\Lambda^\top\succeq0\). All matrix inner products below are Frobenius inner products. Write \(V=\mathbb R^{d\times m}\) for the output space of the input-map RKHS.

We establish derivative reproduction, the three sample-preserving reductions, existence without Gram invertibility, the coefficient identities, surrogate existence and descent, continuity, the accumulation-set alternative, and coefficient stationarity.

## 1. Derivative reproduction and sample-preserving reductions

For a coordinate \(j\), a point \(y\), and nonzero signed \(t\), put
\[
 q_t=\frac{h(\cdot,y+t e_j)-h(\cdot,y)}{t}\in\mathcal H_h.
\]
The reproducing property and two applications of the fundamental theorem of calculus give
\[
 \langle q_t,q_s\rangle
 =\int_0^1\!\int_0^1
 \partial_{1,j}\partial_{2,j}h(y+u t e_j,y+v s e_j)\,du\,dv.
\]
By the C^2 assumption, this tends to \(\partial_{1,j}\partial_{2,j}h(y,y)\) as \(t,s\to0\). Consequently \(\|q_t-q_s\|^2\to0\), so the full signed family converges in the RKHS. Continuous point evaluation identifies its limit as \(\partial_{2,j}h(\cdot,y)\). Pairing with any \(E\in\mathcal H_h\) proves existence of the derivative and
\[
 \partial_jE(y)=\langle E,\partial_{2,j}h(\cdot,y)\rangle.
\]
The same inner-product identity for derivative sections at two points shows that these sections vary continuously in RKHS norm. Thus every \(E\) is continuously differentiable.

Project \(E\) onto the finite span of \(\partial_{2,j}h(\cdot,x_i)\), for all samples and coordinates. The discarded component has zero sampled derivatives by the identity just proved. This projection preserves all sampled gradients and cannot increase the RKHS norm.

Project \(B\) onto the finite span of \(g(\cdot,x_i)v\), with \(v\in V\). For each \(v\in V\), the reproducing property shows that the discarded component has zero inner product with \(v\) at \(x_i\). Hence the projection preserves \(B(x_i)\), and in particular \(B(x_i)u_i\), and cannot increase the RKHS norm.

Define the sample feature operator
\[
 \Phi:(\mathbb R^d)^N\longrightarrow\mathcal W,
 \qquad \Phi z=\sum_i\psi(x_i)z_i.
\]
Let \(\mathcal W_0=\operatorname{im}\Phi\) and let \(\Pi\) be its orthogonal projection. For any feasible \(Q\), set \(\bar Q=\Pi Q\Pi\). Since \(\Pi\psi(x_i)=\psi(x_i)\), the sampled matrices are unchanged. Moreover,
\[
 \bar Q+\bar Q^*=\Pi(Q+Q^*)\Pi\succeq0,
 \qquad \|\bar Q\|_{\rm HS}\leq\|Q\|_{\rm HS}.
\]
The norm inequality follows by writing the Hilbert-Schmidt norm in orthonormal bases adapted to \(\mathcal W_0\): compression retains only one block of the operator. It also covers \(\mathcal W_0=\{0\}\).

There is a bounded right inverse \(T:\mathcal W_0\to\mathbb R^{dN}\) of \(\Phi\) onto its range. For example, restrict \(\Phi\) to \((\ker\Phi)^\perp\), where it is a finite-dimensional isomorphism onto \(\mathcal W_0\), and invert that restriction. Let \(Q_0\) be the restriction of \(\bar Q\) to \(\mathcal W_0\). Then
\[
 \Lambda=TQ_0T^\top,
 \qquad \Lambda+\Lambda^\top=T(Q_0+Q_0^*)T^\top\succeq0,
 \qquad \Phi\Lambda\Phi^*=\bar Q.
\]
If the range is zero, take \(\Lambda=0\). This proves the required coefficient representation directly, including singular feature Grams.

All three replacements preserve the residuals and do not increase their respective penalties.

## 2. Existence and exact finite reduction

Consider the finite-dimensional spaces consisting of operators supported on \(\mathcal W_0\), derivative-section combinations, and input-kernel-section combinations. In the operator space, impose the closed cone \(Q+Q^*\succeq0\). The restricted objective is continuous. Its sublevel sets satisfy
\[
 \alpha\|Q\|_{\rm HS}^2\leq c,
 \quad \beta\|E\|_{\mathcal H_h}^2\leq c,
 \quad \gamma\|B\|_{\mathcal G}^2\leq c.
\]
They are therefore closed and bounded in finite-dimensional spaces and hence compact. A nonempty sublevel is obtained from the zero tuple. The objective attains its minimum there. The preceding projections show that this is also the global minimum of (I). This argument does not assert that unrestricted coefficient sublevels are bounded when Gram matrices are singular.

For the resulting expansions,
\[
 D_\Lambda(x_i)=K_i\Lambda K_i^\top,
 \qquad \nabla E_a(x_i)=L_i a,
 \qquad B_b(x_i)u_i=\mathcal U_i b.
\]
Taking inner products of the kernel-section expansions gives
\[
 \|E_a\|_{\mathcal H_h}^2=a^\top\mathbf L a,
 \qquad \|B_b\|_{\mathcal G}^2=\langle b,\mathbf Rb\rangle.
\]
Also \(\Phi^*\Phi=\mathbf K\). A finite-rank trace calculation gives, without requiring symmetry of \(\Lambda\),
\[
 \|\Phi\Lambda\Phi^*\|_{\rm HS}^2
 =\operatorname{tr}(\Lambda^\top\mathbf K\Lambda\mathbf K)
 =\operatorname{tr}(\mathbf K\Lambda\mathbf K\Lambda^\top).
\]
Thus substitution yields exactly (P). Conversely, any feasible coefficient tuple gives \(Q_\Lambda=\Phi\Lambda\Phi^*\) with
\(Q_\Lambda+Q_\Lambda^*=\Phi(\Lambda+\Lambda^\top)\Phi^*\succeq0\), and gives the same objective in (I). Equality of optimal values, attainment of (P), and reconstruction of every finite minimizer follow.

## 3. The lifted feasible set and surrogate subproblems

Write \(z=(\Lambda,a,b)\),
\[
 r_i(z)=\dot x_i+K_i\Lambda K_i^\top L_i a-\mathcal U_i b,
\]
and let \(J(z)\) be the objective of (P). Direct expansion gives
\[
 F_i(p,z):=\mathsf B_i(\Lambda,a)-\mathsf A_i(\Lambda,a)-Z_i(b)-p_iI
 =-\begin{bmatrix}p_iI_d&r_i(z)\\r_i(z)^\top&p_i\end{bmatrix}.
\]
This is negative semidefinite exactly when \(p_i\geq\|r_i(z)\|\). Indeed, the off-diagonal symmetric block has eigenvalues \(\|r_i\|,-\|r_i\|\), and zeros as applicable; the zero-residual case gives the same condition. In particular, nonnegativity of \(p_i\) is enforced by the LMI, not assumed from \(p_i^2\geq\|r_i\|^2\) alone.

For a base \(\theta\) and a candidate \(\eta\), denote the surrogate residual matrix by \(G_i(\eta;\theta)\). The exact tangent remainder is
\[
 \mathsf A_i(\Lambda',a')-\mathsf A_i^\theta(\Lambda',a')
 =X_i(\Lambda'-\Lambda)^\top X_i(\Lambda'-\Lambda)
 +Y_i(a'-a)^\top Y_i(a'-a)\succeq0.
\]
Therefore \(F_i(\eta)\preceq G_i(\eta;\theta)\), with equality at \(\eta=\theta\). Surrogate feasibility implies lifted feasibility, and a lifted-feasible base is feasible for its own surrogate.

Each \(C(\theta)\) is closed and convex. Convexity follows either from the square of the linear map \(X_i-Y_i\) in the semidefinite order, or from its Schur-complement affine-LMI representation. It is strictly feasible for every base: take \(\Lambda'=I,a'=b'=0\), and choose each \(p_i'\) sufficiently large to make its residual matrix negative definite.

Assume now that all three Gram operators are invertible. They are positive definite: \(\mathbf K=\Phi^*\Phi\), and the other two are Gram operators of the section families used above. Put
\[
 \rho=\min\{1,\alpha\lambda_{\min}(\mathbf K)^2,
 \beta\lambda_{\min}(\mathbf L),\gamma\lambda_{\min}(\mathbf R)\}>0.
\]
Then \(f(\theta)\geq\rho\|\theta\|^2\), and \(f\) is strongly convex with parameter at least \(\rho\). For the matrix term this follows from
\(\operatorname{tr}(\mathbf K\Lambda\mathbf K\Lambda^\top)=\|\mathbf K^{1/2}\Lambda\mathbf K^{1/2}\|_F^2\).
Coercivity and closed nonempty feasibility give attainment; strict convexity gives uniqueness. Thus \(S\) is defined at every base point in the finite-dimensional product space.

If \(y=S(\theta)\) and \(v\in C(\theta)\), optimality on the segment \((1-s)y+sv\) and strong convexity give, after dividing by \(s>0\) and letting \(s\downarrow0\),
\[
 f(y)\leq f(v)-\frac{\rho}{2}\|v-y\|^2.
\]

## 4. Compact invariance and continuity

Let \(T\) be the set of lifted-feasible points satisfying \(f(\theta)\leq f(\theta^0)\). The initialization is strictly feasible: its residual is \(\dot x_i\), and \(s^2+1>s\) for every \(s\geq0\). The cone constraint is also strict at \(I\). Thus \(T\) is nonempty. It is closed and bounded by coercivity, hence compact.

A point in \(T\) belongs to its own surrogate. Applying the descent inequality with \(v=\theta\), together with feasible propagation, proves
\[
 S(T)\subseteq T,
 \qquad f(S(\theta))\leq f(\theta)-\frac{\rho}{2}\|S(\theta)-\theta\|^2.
\]

There is a common strict feasible point \(q=(\bar p,I,0,0)\) for all bases in \(T\). The matrices \(G_i((0,I,0,0);\theta)\) are continuous in \(\theta\), hence uniformly bounded on \(T\). Choose \(\bar p_i\) so that \(G_i(q;\theta)\preceq-I\) for every such base. The cone constraint at \(q\) has a uniform strict margin as well.

We give the continuity argument explicitly. Suppose \(\theta_n\to\theta\) in \(T\). Every subsequence of \(S(\theta_n)\) has a further convergent subsequence by invariance and compactness; let its limit be \(y\). Continuity of the constraint matrices gives \(y\in C(\theta)\). For \(0<\varepsilon<1\), define
\[
 v_\varepsilon=(1-\varepsilon)S(\theta)+\varepsilon q.
\]
Convexity gives a strict margin at least \(\varepsilon\) in all residual constraints, and a strict cone margin. Thus \(v_\varepsilon\in C(\theta_n)\) for all sufficiently large \(n\). Optimality gives \(f(S(\theta_n))\leq f(v_\varepsilon)\). Passing to the convergent subsequence and then letting \(\varepsilon\downarrow0\) yields
\(f(y)\leq f(S(\theta))\).
Uniqueness on \(C(\theta)\) forces \(y=S(\theta)\). This proves continuity of \(S\) on \(T\), and compactness makes it uniformly continuous.

## 5. Fixed points and the accumulation-set alternative

Summing the descent inequality along the orbit gives
\[
 \sum_{t=0}^\infty\|\theta^{t+1}-\theta^t\|^2<\infty,
 \qquad \|\theta^{t+1}-\theta^t\|\to0.
\]
If \(\theta^{t_j}\to\theta^*\), then continuity of \(S\) and vanishing steps imply \(S(\theta^*)=\theta^*\).

The accumulation set \(\Omega\) is nonempty and compact. Also \(\operatorname{dist}(\theta^t,\Omega)\to0\): otherwise a subsequence staying a positive distance away would have a cluster point in \(\Omega\), a contradiction.

To prove connectedness, suppose \(\Omega=A\cup B\) were a separation into nonempty disjoint compact subsets. They have positive distance. Choose disjoint neighborhoods of them whose closures are still positively separated. Eventually every iterate lies in their union, by the distance-to-\(\Omega\) property. Both neighborhoods are visited infinitely often because both parts contain cluster points. But eventually the step size is smaller than the gap between the neighborhoods, making such repeated transitions impossible. Hence \(\Omega\) is connected. If it is a singleton, compactness implies convergence of the full sequence. Otherwise it is a nonempty compact connected nonsingleton set. This derives the needed monotone-iteration conclusion without leaving an external theorem obligation open.

## 6. Stationarity for the coefficient program

Let \(\theta^*=(p^*,z^*)\) be a fixed point. Keeping \(z=z^*\) in its surrogate makes the tangent exact. Minimizing over \(p\) therefore gives
\[
 p_i^*=\|r_i(z^*)\|,
 \qquad f(\theta^*)=J(z^*).
\]
We prove the stated variational inequality without assuming nonzero residuals or appealing to an unexpanded nonlinear-SDP KKT result.

Let \(z=(\Lambda,a,b)\) be any feasible coefficient tuple and set \(\delta z=z-z^*\), \(z(t)=z^*+t\delta z\), for \(0\leq t\leq1\). The coefficient cone is convex, so \(z(t)\) is feasible for it. Define
\[
 H_i=X_i(\delta\Lambda)^\top X_i(\delta\Lambda)
       +Y_i(\delta a)^\top Y_i(\delta a),
 \qquad c_i=\|H_i\|_{\rm op},
\]
and choose
\[
 p_i(t)=\|r_i(z(t))\|+c_i t^2.
\]
The surrogate constraint at base \(\theta^*\) equals the original lifted matrix at \((p(t),z(t))\) plus \(t^2H_i\). The original lifted matrix at \(p_i=\|r_i(z(t))\|\) is negative semidefinite. Increasing \(p_i\) by \(c_it^2\) subtracts \(c_it^2I\), which dominates \(t^2H_i\). Therefore \((p(t),z(t))\in C(\theta^*)\).

Residuals remain bounded for small \(t\), so
\[
 f(p(t),z(t))=J(z(t))+O(t^2).
\]
Fixed-point optimality yields
\[
 0\leq f(p(t),z(t))-f(\theta^*)
 =J(z(t))-J(z^*)+O(t^2).
\]
Divide by \(t>0\) and let \(t\downarrow0\). Since \(J\) is a polynomial in the finite coefficients,
\[
 \langle\nabla J(z^*),z-z^*\rangle\geq0
\]
for every feasible \(z\). This is exactly the stipulated stationarity condition. The proof also applies when any residual is zero.

All accumulation points are fixed points by Section 5, so their coefficient components are stationary. This proves the full convergence alternative and completes both parts of the theorem.
