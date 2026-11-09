# Reference Proof

## Obligations and Scope

The finite risk is the deterministic expectation over the entire prompt, with query X_1 included in that prompt. The obligations are: (1) Gaussian reduction and the population risk formula; (2) complete population critical-point classification; (3) population gradient-flow convergence; (4) uniform L2 convergence of operator derivatives through order two; (5) deterministic C2 convergence of risks; (6) unique critical-point persistence and common compact confinement; and (7) generic finite-flow convergence and convergence of the minima. All are established below. The exact quantitative concentration exponents and exponential convergence rates are not required by this task.

## 1. Gaussian Reduction and Risk

For X distributed as N(0,Sigma), completing the square gives
\[
\mathbb E e^{v^TX}=e^{v^T\Sigma v/2},\qquad
\mathbb E[Xe^{v^TX}]=\Sigma v\,e^{v^T\Sigma v/2}.
\]
Take v=lambda(mu^Tz)mu. Dividing these expectations yields A_infty(mu)z=lambda Sigma mu(mu^Tz). Thus the specialized prior Gaussian-attention identity is derived here rather than used as an unexplained external dependency.

Put a=mu^T Sigma mu and b=mu^T Sigma^2 mu. Since E[ZZ^T]=Sigma,
\[
\mathbb E[Z^TA_\infty(\mu)Z]=\lambda b,
\qquad
\mathbb E\|A_\infty(\mu)Z\|^2=\lambda^2ab.
\]
Consequently
\[
R_\infty(\mu)=\operatorname{tr}\Sigma-2\lambda b+\lambda^2ab.
\]

## 2. Population Critical Points

Differentiation gives
\[
\nabla R_\infty(\mu)=2\lambda[\lambda b\Sigma\mu+(\lambda a-2)\Sigma^2\mu].
\]
For a nonzero critical point, multiplication by Sigma^{-1} gives
\[
\lambda b\mu+(\lambda a-2)\Sigma\mu=0.
\]
The coefficient lambda a-2 cannot vanish, since b>0. Therefore mu is an eigenvector of Sigma. Equivalently, two nonzero eigencoordinates would imply (lambda a-2)(sigma_j-sigma_k)=0, followed by b=0, a contradiction. Writing mu=t u_j gives lambda sigma_j t^2=1. This proves the stated complete critical set.

The Hessian at zero is -4 lambda Sigma^2. At either point p_j=+/-u_j/sqrt(lambda sigma_j), its eigenvalues are
\[
8\lambda\sigma_j^2\quad\text{in direction }u_j,
\qquad
2\lambda\sigma_k(\sigma_j-\sigma_k)\quad(k\ne j).
\]
Every critical point is nondegenerate. Zero is a strict maximum, j>=2 gives both positive and negative curvature, and j=1 gives positive-definite minima. When d=1 there are no saddle points and the minimum's sole Hessian eigenvalue is 8 lambda sigma_1^2.

Moreover,
\[
R_\infty(\mu)\ge\operatorname{tr}\Sigma-2\lambda\sigma_1^2\|\mu\|^2+\lambda^2\sigma_d^3\|\mu\|^4,
\]
so the risk is coercive and attains a global minimum at a critical point. At p_j its value is tr(Sigma)-sigma_j. Comparing the complete critical set proves that precisely the leading pair are global minima.

## 3. A Bounded-Flow Convergence Argument

We use the following elementary argument for either risk. Let f be C2, and suppose a forward gradient trajectory remains in a compact set K containing only finitely many critical points. Local existence and uniqueness, together with boundedness, extend the trajectory to all nonnegative times. Energy dissipation gives
\[
\frac{d}{dt}f(\mu(t))=-\|\nabla f(\mu(t))\|^2.
\]
Because f is bounded below on K, the squared gradient is integrable in time. Its derivative is -2 grad(f)^T Hessian(f) grad(f), which is bounded on K. Thus the squared gradient is uniformly continuous and tends to zero: otherwise uniformly continuous positive excursions would contradict integrability.

The omega-limit set is nonempty and compact. It is connected, since it is the intersection of the nested compact connected closures of the continuous trajectory tails. Every point in it is critical. A connected subset of a finite set is a singleton, so the trajectory converges to one critical point.

The standard independent stable manifold theorem used here says that for a C1 vector field, the local stable set of a hyperbolic equilibrium is a C1 manifold tangent to the stable eigenspace. If an unstable eigenvalue exists, this manifold has dimension less than d and hence Lebesgue measure zero. For the negative gradient field at a nondegenerate nonminimum, the linearization is minus the Hessian, has no eigenvalue with zero real part, and has at least one positive eigenvalue. All hypotheses therefore hold. Any trajectory converging to that equilibrium eventually lies in its local stable manifold. Its basin is contained in the union, over integer times, of inverse images of that manifold under finite-time flow maps. These maps are local C1 diffeomorphisms on their domains; using countable coordinate covers, their inverse images preserve null sets. The basin is consequently null.

Population coercivity confines every trajectory to its compact initial sublevel set. The preceding convergence argument and the finite population critical set imply convergence for every initialization. Taking the finite union of the null basins of zero and the saddles proves the population almost-everywhere claim. Analyticity or a separate analytic gradient-flow theorem is not needed.

## 4. Compact-Uniform L2 Convergence of Operator Derivatives

Fix rho<infinity. Constants below may depend on rho, d, lambda, Sigma and fixed moment orders, but not on L, mu with ||mu||<=rho, or the conditioned query z. Work with L>=2 and condition on X_1=z. Set
\[
q(\mu,z,x)=\lambda(\mu^Tz)(\mu^Tx),
\]
\[
N_L=\frac1L\left[z e^{q(\mu,z,z)}+\sum_{i=2}^L X_i e^{q(\mu,z,X_i)}\right],\quad
s_L=\frac1L\left[e^{q(\mu,z,z)}+\sum_{i=2}^L e^{q(\mu,z,X_i)}\right].
\]
Let N=E_X[X exp(q(mu,z,X))] and s=E_X[exp(q(mu,z,X))], with X independent and Gaussian. Thus A_L(mu)z=N_L/s_L and A_infty(mu)z=N/s. In particular the self token has been retained exactly.

For each j in {0,1,2} and each fixed even integer p>=2, the derivative-block errors satisfy
\[
\mathbb E[\|D^jN_L-D^jN\|^p+\|D^js_L-D^js\|^p\mid X_1=z]
\le C L^{-p/2}(1+\|z\|^m)e^{C\|z\|^2}. \tag{1}
\]
Here and below a derivative of order zero is the original block, and tensor norms may be any fixed Euclidean coordinate norm.

To verify (1), derivatives through order two of exp(q) are exp(q) times polynomials in x,z,mu; q is quadratic in mu. For p=2h, expand a coordinate's 2h-th moment of a sum of independent centered blocks. A term containing an index exactly once has expectation zero. Every surviving term has at most h distinct indices. There are O(L^h) such terms, and Holder bounds each by the corresponding 2h-th moment. Division by L^{2h} gives O(L^{-h}). Summing over finitely many coordinates gives the tensor estimate. The moments of each block follow by Gaussian tilting:
\[
\mathbb E[\|X\|^m e^{v^TX}]
=e^{v^T\Sigma v/2}\mathbb E\|X+\Sigma v\|^m
\le C(1+\|v\|^m)e^{v^T\Sigma v/2}.
\]
For bounded mu, v is bounded by C||z||. The deterministic self block and the difference between (L-1)/L and 1 contribute L^{-p} times a polynomial in ||z|| times exp(C||z||^2), which also satisfies (1). This explicitly includes the self-token exponential.

The same estimates without L^{-p/2} bound all uncentered derivative blocks. Inverse denominators have bounds without sample-size decay. Indeed, writing n=L-1 and using convexity of x -> x^{-p},
\[
\mathbb E[s_L^{-p}\mid z]
\le (L/n)^p\mathbb E\left[\left(n^{-1}\sum_{i=2}^Le^{q(\mu,z,X_i)}\right)^{-p}\right]
\le 2^p\mathbb E e^{-p q(\mu,z,X)}
\le C e^{C\|z\|^2}. \tag{2}
\]
Also s=exp(lambda^2(mu^T Sigma mu)(mu^Tz)^2/2)>=1.

For a vector numerator N and scalar positive denominator s, the exact derivative formulas are
\[
D(N/s)[h]=DN[h]/s-NDs[h]/s^2,
\]
\[
D^2(N/s)[h,k]=D^2N[h,k]/s
-\{DN[h]Ds[k]+DN[k]Ds[h]+ND^2s[h,k]\}/s^2
+2NDs[h]Ds[k]/s^3.
\]
Subtract the empirical and limiting formulas by telescoping each product. Differences of inverse powers are also telescoped using the factor s_L-s. Every term contains at least one derivative-block error; its other factors are derivative blocks or inverse denominators. Apply Holder with sufficiently large fixed even moment orders, using (1), (2), and the uncentered-block bounds. For k=0,1,2 this proves
\[
\mathbb E[\|D_\mu^k A_L(\mu)z-D_\mu^k A_\infty(\mu)z\|_F^2\mid X_1=z]
\le \frac C L(1+\|z\|^m)e^{C\|z\|^2}. \tag{3}
\]
This bound is uniform in ||mu||<=rho. No assertion of independence among quotient factors is used.

It remains to integrate over the unbounded query. Put M_L=max(1,||X_1||,...,||X_L||). The attention output is a convex combination of the tokens. Furthermore,
\[
\|D_\mu q(\mu,X_1,X_i)\|\le 2\lambda\rho\|X_1\|\|X_i\|,
\qquad
\|D_\mu^2 q(\mu,X_1,X_i)\|\le 2\lambda\|X_1\|\|X_i\|.
\]
Differentiating a softmax weight gives its weight times the score derivative minus its weighted mean. Differentiating once more gives sums of weighted score-Hessian and score-gradient products. Consequently, for k<=2, the output derivatives are bounded uniformly on the parameter ball by C(1+M_L)^5. The limiting derivatives are bounded by C||X_1||.

Gaussian tails and a union bound give E(1+M_L)^p <= C_p(1+log L)^{p/2} for each fixed p. Integrating the Gaussian tail proves this moment estimate directly. Also P(||X_1||>T)<=C exp(-cT^2), after changing constants. Cauchy-Schwarz therefore bounds the contribution of ||X_1||>T to each squared derivative error by
\[
C(1+\log L)^q e^{-cT^2}. \tag{4}
\]
On ||X_1||<=T, (3) bounds the contribution by C L^{-1}(1+T^m)exp(CT^2). Choose T^2=eta log L with eta>0 sufficiently small that C eta<1. Both this bound and (4) tend to zero. Hence
\[
\sup_{\|\mu\|\le\rho}\mathbb E\|D_\mu^k[A_L(\mu)X_1]-D_\mu^k[A_\infty(\mu)X_1]\|_F^2\longrightarrow0,
\qquad k=0,1,2. \tag{5}
\]
The argument includes mu=0 without division by mu^T Sigma mu. L=1 is irrelevant to this eventual assertion; its risk is well defined and identically zero.

## 5. Deterministic C2 Convergence of Risks

For each fixed L, derivatives of the softmax output on compact parameter sets have polynomial bounds in M_L. All these moments are finite. Differentiating the population risk under its whole-prompt expectation is therefore justified through order two, with continuous derivatives.

Write T_L=A_L(mu)X_1, J_L=D_mu T_L, and H_L=D_mu^2T_L, and similarly for infinity. Formula (5) and the explicit Gaussian limiting derivatives give uniform L2 bounds for T_L,J_L,H_L on each fixed parameter ball. The identities
\[
R_L=\mathbb E\|T_L-X_1\|^2,
\quad
\nabla R_L=2\mathbb E[J_L^T(T_L-X_1)],
\]
\[
\nabla^2R_L=2\mathbb E[J_L^TJ_L]+2\mathbb E[(T_L-X_1)\mathbin{\cdot}H_L]
\]
use contraction over the output coordinate in the final expression.

For the risk, subtract the two squared norms and apply Cauchy-Schwarz. For the gradient, use
\[
J_L^T(T_L-X_1)-J_\infty^T(T_\infty-X_1)
=(J_L-J_\infty)^T(T_L-X_1)+J_\infty^T(T_L-T_\infty).
\]
For the Hessian, telescope J_L^TJ_L-J_infty^TJ_infty and write the other difference as
\[
(T_L-X_1)\mathbin{\cdot}(H_L-H_\infty)
+(T_L-T_\infty)\mathbin{\cdot}H_\infty.
\]
Each expectation tends to zero uniformly by (5), Cauchy-Schwarz, and the uniform L2 bounds. Thus R_L -> R_infty in C2 on every fixed compact ball, deterministically. No almost-sure risk statement follows from, or is needed in, this argument.

## 6. Persistence and Compact Confinement

Let f=R_infty and f_L=R_L. At a population critical point p, set H=Hessian f(p). Choose a sufficiently small closed ball B(p,r) so that
\[
\sup_{x\in B(p,r)}\|I-H^{-1}\nabla^2f(x)\|<1/4.
\]
For sufficiently large L, C2 convergence makes the corresponding bound for f_L less than 1/2. The map Phi_L(x)=x-H^{-1}grad f_L(x) is a contraction with constant at most 1/2. Since grad f_L(p)->0, it maps B(p,r) into itself for large L. Iteration gives a unique fixed point p_L, hence a unique critical point in that ball. Moreover
\[
\|p_L-p\|\le2\|H^{-1}\nabla f_L(p)\|\longrightarrow0.
\]
Hessian convergence preserves nondegeneracy and inertia.

Choose these balls pairwise disjoint and within the interior of a fixed sufficiently large B_rho. The complement in B_rho of their open interiors is compact and has no population critical point. Its population gradient norm has a positive minimum. Uniform C1 convergence excludes all other finite critical points there. This proves the exact finite critical set and its classifications. Since R_L is even in mu, uniqueness pairs its nonzero critical points and fixes its unique critical point near zero at zero.

For invariance, the population gradient satisfies
\[
\mu^T\nabla R_\infty(\mu)=4\lambda b(\lambda a-1).
\]
Choose rho_0>(lambda sigma_d)^(-1/2). For every fixed rho>=rho_0 this expression has a positive minimum on the sphere ||mu||=rho. Uniform C1 convergence preserves positivity there for all L above a threshold depending on rho, Sigma, and lambda. Along finite gradient flow the derivative of ||mu||^2 is -2 mu^T grad R_L(mu), strictly negative on that boundary. The first-exit argument proves forward invariance of B_rho, including for initial points on its boundary. Increase the same threshold to ensure all persistence conclusions. The limiting critical points lie strictly inside every such ball.

## 7. Generic Finite-Flow Convergence

Fix rho>=rho_0 and L at least the common threshold. The risk is C2, B_rho is forward invariant, and its critical set is finite and nondegenerate. Section 3 proves convergence of every trajectory starting in this ball to one of those critical points. At the maximum and every saddle, the negative gradient linearization has an unstable eigenvalue and is hyperbolic. The audited stable-manifold argument makes the union of their basins Lebesgue null. Almost every initialization in the ball therefore converges to one of the two strict local minima. Section 6 gives convergence of these minima to +/-u_1/sqrt(lambda sigma_1) as L tends to infinity. This completes every public claim.
