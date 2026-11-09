# Reference Proof

## 1. Explicit frozen joint surrogate

Use S for the surrogate and G for the Tucker core. Write each prediction as a finite sum of positive contributions z_{i,rho}: for CP, z_{i,r}=product_n A^(n)_{i_n r}; for Tucker, z_{i,j}=G_j product_n A^(n)_{i_n j_n}. At a reference point write

\[
s_i=\widehat X_i(\widetilde\Theta),\quad t_{i\rho}=z_{i\rho}(\widetilde\Theta),\quad \lambda_{i\rho}=t_{i\rho}/s_i,\quad v_{i\rho}=z_{i\rho}(\Theta)/t_{i\rho},
\qquad P_i=X_i s_i^{\beta-2},\quad Q_i=s_i^{\beta-1}.
\]

All these quantities are positive, and the lambda weights sum to one. Define
\[
H_i(v)=\begin{cases}
Q_i(v^\beta-1)/\beta-P_i(v^{\beta-1}-1)/(\beta-1),&1<\beta<2,\\
Q_i(v-1)-P_i\log v,&\beta=1,\\
Q_i(v-1)+P_i(v^{\beta-1}-1)/(1-\beta),&0\le\beta<1.
\end{cases}
\]
Set
\[
S(\Theta\mid\widetilde\Theta)=F(\widetilde\Theta)+\sum_{i,\rho}t_{i\rho}H_i(v_{i\rho}).
\tag{A}
\]
This is a joint function of all blocks with a frozen reference.

For 1<=beta<2, differentiation in the second argument gives
\[
\partial_y^2d_\beta(x\mid y)=(\beta-1)y^{\beta-2}+(2-\beta)xy^{\beta-3}\ge0.
\]
Consequently Jensen gives
\[
d_\beta(X_i\mid\sum_\rho z_{i\rho})\le\sum_\rho\lambda_{i\rho}d_\beta(X_i\mid z_{i\rho}/\lambda_{i\rho}).
\]
Expanding the right-hand side gives (A), including its reference-dependent constant. Equality holds at the reference because every z_{i,rho}/lambda_{i,rho}=s_i.

For 0<beta<1, split the divergence into the convex function X_i y^(beta-1)/(1-beta), the concave function y^beta/beta, and a constant. Apply Jensen to the former and its tangent at s_i to the latter. For beta=0, use the exact decomposition X_i/y+log y-log X_i-1: X_i/y is convex, and log y is concave. The same operations give precisely the last case of (A). Both inequalities are equalities at the reference. Thus, in every regime,
\[
F(\Theta)\le S(\Theta\mid\widetilde\Theta),\qquad S(\widetilde\Theta\mid\widetilde\Theta)=F(\widetilde\Theta).
\tag{B}
\]

These functions are smooth on the positive parameter domain. Moreover H_i'(1)=Q_i-P_i and t_{i,rho} times the derivative of v_{i,rho} is the derivative of z_{i,rho}. Since partial_y d_beta(X_i|s_i)=Q_i-P_i, differentiating (A) proves
\[
\nabla_1S(\widetilde\Theta\mid\widetilde\Theta)=\nabla F(\widetilde\Theta).
\tag{C}
\]

## 2. Contraction coefficients and the actual scalar summands

Define entrywise transforms
\[
\chi_1(Z,a)=a^{2-\beta}Z^{\beta-1}=a(Z/a)^{\beta-1},\qquad
\chi_2(Z,a)=\begin{cases}Z,&\beta<1,\\a(Z/a)^\beta,&\beta\ge1.\end{cases}
\]
The reference tensors P,Q stay fixed throughout a sweep; the transforms use the current other blocks.

For a CP factor, the coefficients are
\[
N^{(n)}_{i_n r}=\sum_{i_{-n}}P_i\prod_{m\ne n}\chi_1(A^{(m)}_{i_mr},\widetilde A^{(m)}_{i_mr}),\qquad
D^{(n)}_{i_n r}=\sum_{i_{-n}}Q_i\prod_{m\ne n}\chi_2(A^{(m)}_{i_mr},\widetilde A^{(m)}_{i_mr}).
\tag{D}
\]
For the Tucker core,
\[
N^{\rm core}_j=\sum_iP_i\prod_n\chi_1(A^{(n)}_{i_nj_n},\widetilde A^{(n)}_{i_nj_n}),\qquad
D^{\rm core}_j=\sum_iQ_i\prod_n\chi_2(A^{(n)}_{i_nj_n},\widetilde A^{(n)}_{i_nj_n}).
\tag{E}
\]
For a Tucker factor,
\[
N^{(n)}_{i_nj_n}=\sum_{i_{-n},j_{-n}}P_i\chi_1(G_j,\widetilde G_j)\prod_{m\ne n}\chi_1(A^{(m)}_{i_mj_m},\widetilde A^{(m)}_{i_mj_m}),
\]
\[
D^{(n)}_{i_nj_n}=\sum_{i_{-n},j_{-n}}Q_i\chi_2(G_j,\widetilde G_j)\prod_{m\ne n}\chi_2(A^{(m)}_{i_mj_m},\widetilde A^{(m)}_{i_mj_m}).
\tag{F}
\]
All sums have finite nonempty index sets. These are tensor contractions with entrywise transforms and require no unfolding.

To verify the coefficients, fix an active scalar Z with reference a and write u=Z/a. In each contribution involving Z, t=a times the product of the other reference entries and v=u times the product of the other ratios. Substituting in (A) and collecting those terms gives the actual scalar summand
\[
g_Z(u)=a h(u)+\text{constant},\qquad
h(u)=\begin{cases}
D u^\beta/\beta-Nu^{\beta-1}/(\beta-1),&1<\beta<2,\\
Du-N\log u,&\beta=1,\\
Du+Nu^{\beta-1}/(1-\beta),&0\le\beta<1.
\end{cases}
\tag{G}
\]
The factor a is essential in the equality with S. Every contribution involves exactly one entry of the active factor or core block, so this establishes entrywise separability for each active block.

## 3. Exact epsilon updates, feasibility, and descent

Every coefficient N,D is positive. Differentiation gives
\[
h'(u)=\begin{cases}u^{\beta-2}(Du-N),&1<\beta<2,\\D-N/u,&\beta=1,\\D-Nu^{\beta-2},&0\le\beta<1.\end{cases}
\]
The respective second derivatives are
\[
h''(u)=\begin{cases}
D(\beta-1)u^{\beta-2}+N(2-\beta)u^{\beta-3},&1<\beta<2,\\
N/u^2,&\beta=1,\\
N(2-\beta)u^{\beta-3},&0\le\beta<1.
\end{cases}
\tag{H}
\]
They are strictly positive. Also h tends to infinity as u tends to infinity. The unique unconstrained minimizer is (N/D)^gamma, where gamma=1 for beta>=1 and gamma=1/(2-beta) otherwise. The exact minimizer under Z>=epsilon is therefore
\[
Z^+=\max\{\epsilon,\ a(N/D)^\gamma\}.
\tag{I}
\]
It is positive and finite. Thus the recurrence is defined for every positive starting point, independently of whether a separately specified C is invariant.

For the convergence claims, containment of the generated outer iterates in C is assumed. In a single cyclic sweep, every intermediate state combines completed blocks from the next outer iterate with untouched blocks from the current one. The product structure of C puts all such states in C. Each update minimizes over the entrywise epsilon domain; since its output lies in C_b and C_b is contained in that domain, it also minimizes over C_b. No invariance of arbitrary C and no additional projection is asserted.

Every block update decreases the same frozen S. Combining the sweep decrease with (B) gives F(Theta^(k+1))<=F(Theta^k). On feasible iterates Psi equals F.

## 4. Uniform curvature and sufficient decrease

Put U=M/epsilon. All ratios appearing in sweep states lie in [epsilon/M,U]. For the fixed finite tensor problem, reference reconstructions, transforms, and contraction coefficients are continuous and positive on the relevant compact domains. There are therefore constants N_min,D_min>0 and finite upper bounds, independent of k and of the active entry. The upper bounds may depend on the fixed data X and the dimensions; no uniformity over all data sharing only delta_X is needed.

By (H), a positive lower bound mu_0 for h'' is, in the three regimes,
\[
D_{\min}(\beta-1)U^{\beta-2}+N_{\min}(2-\beta)U^{\beta-3},\qquad
N_{\min}/U^2,\qquad
N_{\min}(2-\beta)U^{\beta-3}.
\]
Since a>=epsilon, the actual summand g_Z has second derivative at least mu=epsilon*mu_0. Before the active block is updated its entries still equal their reference values, so their old ratios are 1. Write u* for the clipped minimizer. Both endpoints and their connecting segment lie in the bounded ratio region. Constrained optimality gives g_Z'(u*)(1-u*)>=0, including an active lower bound. Strong convexity on this segment therefore yields
\[
g_Z(1)-g_Z(u^*)\ge\frac\mu2|1-u^*|^2\ge\frac\mu{2M^2}|Z^+-a|^2.
\]
This comparison is only between feasible points; it does not assert a minimizer gap for infeasible ratios below epsilon/a.

Let Theta^(k,b) be the state after block b, with Theta^(k,0)=Theta^k and Theta^(k,B)=Theta^(k+1). Sum the preceding estimate over entries and blocks. Since each block changes once, its increments have disjoint supports. Using (B),
\[
\Psi(\Theta^k)-\Psi(\Theta^{k+1})\ge c_{\rm dec}\sum_{b=1}^B\|\Theta^{k,b}-\Theta^{k,b-1}\|^2
=c_{\rm dec}\|\Theta^{k+1}-\Theta^k\|^2,
\quad c_{\rm dec}=\mu/(2M^2)>0.
\tag{J}
\]
This also covers epsilon=M and stationary sweeps.

## 5. Relative error

Exact minimization over C_b gives a normal n_b^(k+1) in N_{C_b}(Theta_b^(k+1)) satisfying
\[
n_b^{k+1}=-\nabla_b S(\Theta^{k,b}\mid\Theta^k).
\]
The updated block is unchanged during the rest of the sweep. For a closed convex product C, its normal cone is the product of the block normal cones. The smooth-plus-indicator subdifferential formula consequently gives
\[
\xi_b^{k+1}=\nabla_bF(\Theta^{k+1})-\nabla_bS(\Theta^{k,b}\mid\Theta^k),\qquad
\xi^{k+1}\in\partial\Psi(\Theta^{k+1}).
\]
Insert gradients at Theta^k and use (C). Uniform Lipschitz continuity on C gives
\[
\|\xi_b^{k+1}\|\le L_F\|\Theta^{k+1}-\Theta^k\|+L_S\|\Theta^{k,b}-\Theta^k\|
\le(L_F+L_S)\|\Theta^{k+1}-\Theta^k\|.
\]
The last inequality follows from disjoint block supports. Hence
\[
\operatorname{dist}(0,\partial\Psi(\Theta^{k+1}))\le\|\xi^{k+1}\|
\le\sqrt B(L_F+L_S)\|\Theta^{k+1}-\Theta^k\|.
\tag{K}
\]
The Lipschitz constants may be enlarged to be positive, so c_err=sqrt(B)(L_F+L_S)>0.

## 6. Objective limits and critical cluster points

The divergence is nonnegative: its derivative in y is y^(beta-2)(y-x), and its value at y=x is zero. Thus (J) implies convergence of Psi(Theta^k) to a finite value ell and square summability of the increments. In particular the increments tend to zero. Compactness supplies cluster points.

For any convergent subsequence Theta^(k_j), the next iterates have the same limit. The explicit residuals in (K) tend to zero. Continuity of F on C gives convergence of the objective values to the objective at that cluster point. The graph-closedness property of the limiting subdifferential under joint point/value/subgradient convergence therefore makes every cluster point critical. Equivalently here, one can use continuity of the gradient and closedness of the convex normal-cone graph. All cluster points have value ell.

## 7. KL finite length

For completeness, the standard KL descent implication used in the source is closed directly here. Let Omega be the compact set of cluster points. The sequence approaches Omega, and Psi is constant with value ell on Omega. At each point of Omega choose a KL neighborhood, a positive height, and a concave desingularizing function from the assumed KL property. A finite subcover exists. Reduce the height to the minimum of the finitely many heights and sum their desingularizing functions on this interval. The resulting concave function phi has derivative at least that of each chosen function. It therefore satisfies the KL inequality for points sufficiently close to Omega with objective in (ell,ell+eta).

Set s_k=||Theta^(k+1)-Theta^k|| and r_k=Psi(Theta^k)-ell. If some r_k=0, (J) forces every later step to vanish. Otherwise, for all sufficiently large k, the uniform KL inequality and (K) imply
\[
1\le\varphi'(r_k)c_{\rm err}s_{k-1}.
\]
In particular s_{k-1}>0. Concavity of phi and (J) yield
\[
\varphi(r_k)-\varphi(r_{k+1})\ge\varphi'(r_k)(r_k-r_{k+1})
\ge\frac{c_{\rm dec}s_k^2}{c_{\rm err}s_{k-1}}.
\]
Consequently, by the arithmetic-geometric mean inequality,
\[
2s_k\le s_{k-1}+\frac{c_{\rm err}}{c_{\rm dec}}[\varphi(r_k)-\varphi(r_{k+1})].
\]
Summing from a sufficiently large K to T and cancelling the shifted step sums bounds sum_{k=K}^T s_k by s_{K-1}+(c_err/c_dec)phi(r_K), uniformly in T. The finite initial portion adds a finite amount. Thus sum_k s_k<infinity.

The iterates are Cauchy and converge to a point Theta* in closed C. It is a cluster point, so the preceding criticality argument gives 0 in partial Psi(Theta*). All claimed conclusions follow.
