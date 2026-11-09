# Reference Proof

## Proof obligations

The proof must establish: (i) a uniform, dimension-independent quadratic reward decomposition with the full rank and nuclear-norm bounds; (ii) conditional unbiasedness and a conditional second-moment bound for the observed gradient estimator; (iii) blockwise hypentropy geometry, including a derivation rather than an unsupported invocation of the specialized strong-convexity result; (iv) the mirror-descent comparator inequality and a divergence bound valid for zero and arbitrarily small comparators; and (v) the source's supremum of expected fixed-comparator regrets, with the stated parameters. All five obligations are closed below.

## 1. Structural representation

Write xi_m^*(a|q) for the law obtained by deleting mu_m(q,a). Its likelihood ratio with the actual law satisfies

`exp(-2epsilon) <= xi_m(a|q)/xi_m^*(a|q) <= exp(2epsilon)`.

Consequently, using the unit action norms and 0<=epsilon<1,

`||E_{xi_m}a-E_{xi_m^*}a||_2 <= sum_a |xi_m(a|q)-xi_m^*(a|q)| <= exp(2epsilon)-1 <= (exp(2)-1)epsilon`.

Define

`A(z)=log sum_{a in A} exp(<z,a>), mu_A=grad A(0), Sigma_A=grad^2 A(0)`.

The finite nonempty action set makes A smooth. Differentiation of the finite sum gives grad A(z) equal to the mean action under exponential tilting by z, and grad^2 A(z) equal to its covariance. In particular, mu_A and Sigma_A are the mean and covariance of the uniform action distribution.

For completeness, the Taylor constant is universal. If E_z denotes expectation under the tilted law and b=a-E_z a, differentiation of that covariance gives

`D^3 A(z)[u,v,w]=E_z[<u,b><v,b><w,b>]`.

Since ||b||_2<=2, its absolute value is at most `8||u||_2||v||_2||w||_2`. Apply the integral Taylor formula to grad A along the segment from zero to z, and test the vector remainder against any unit vector u. This yields

`||grad A(z)-mu_A-Sigma_A z||_2 <= 4||z||_2^2`.

Now z=Psi_m q has norm at most sqrt(epsilon). Combining the Taylor and likelihood-ratio bounds gives

`E_{xi_m(.|q)}a=mu_A+Sigma_A Psi_m q+e_m(q)`,

where `||e_m(q)||_2 <= (exp(2)+3)epsilon`, uniformly in q and m.

Substitute this identity into the reward expectation. Set

`C(q)=q^T(Psi^*)^T mu_A`,

`B_m=(Psi^*)^T Sigma_A Psi_m`,

`W_m^*=(B_m+B_m^T)/2`,

and

`delta_m(q)=q^T(Psi^*)^T e_m(q)+E_{a~xi_m(.|q)}nu(q,a)`.

These definitions give exactly

`E_{a~xi_m(.|q)}r(q,a)=C(q)+q^T W_m^*q+delta_m(q)`.

The residual has absolute value at most `(exp(2)+4)epsilon`, so K can be chosen universally. To control the matrices, for every unit vector u,

`u^T Sigma_A u=Var(<u,a>)<=E< u,a>^2<=1`.

Thus `||Sigma_A||_2<=1`, and

`||W_m^*||_2<=||B_m||_2<=sqrt(epsilon)<=1`.

Rank subadditivity gives `rank(W_m^*)<=2rank(Psi_m)<=2s`. Therefore

`||W_m^*||_*<=rank(W_m^*)||W_m^*||_2<=rank(W_m^*)<=2s`.

All constructions use fixed environment quantities, so W_m^* does not depend on q or on the online trajectory. At epsilon=0, Psi_m=0 and both misspecification functions vanish, and the same proof gives an exact common reward with W_m^*=0 and delta_m=0.

## 2. Gradient estimation and noise conditioning

Let H_t be the interaction history before the current routing draw, including q_t. The iterate W_t and query q_t are H_t-measurable. Set `p_{t,m}=pi_{W_t}(m|q_t)` and `R_m(q)=E_{xi_m(.|q)}r(q,a)`.

Direct differentiation gives

`grad_{W_m} pi_W(j|q)=pi_W(j|q)(1[j=m]-pi_W(m|q))qq^T`.

Hence the m-th block of the true gradient is

`G_{t,m}:=grad_{W_m} L_t(W_t)=-sum_j p_{t,j}R_j(q_t)(1[j=m]-p_{t,m})q_tq_t^T`.

Condition first on H_t,m_t,a_t. The noise has conditional mean zero under precisely this conditioning, so `E[r_t|H_t,m_t,a_t]=r(q_t,a_t)`. Then average over the stated action law and routing law. This proves

`E[hat G_t|H_t]=grad L_t(W_t)`.

Each estimator block is a scalar multiple of q_tq_t^T and has rank at most one, including when it is zero.

The signal satisfies `|r(q,a)|<=1+epsilon<=2`. Conditional 1-sub-Gaussianity and zero mean imply conditional variance at most one, so

`E[r_t^2|H_t,m_t,a_t]<=5`.

For any probability vector p and selected index j,

`sum_m (1[j=m]-p_m)^2=1-2p_j+sum_m p_m^2<=2`.

Using `||q_tq_t^T||_2^2=||q_t||_2^4<=1`, we obtain

`E[sum_m ||hat G_{t,m}||_2^2|H_t]<=10`.

This is an expected second-moment statement, not an almost-sure bound on noisy gradients. Conditioning only on H_t and a_t would not suffice to remove noise from an expression also involving m_t.

## 3. Hypentropy geometry, with the specialized obligation derived

For a single n-by-n symmetric block, put

`h_beta(x)=x asinh(x/beta)-sqrt(x^2+beta^2)`.

Then `h_beta'(x)=asinh(x/beta)` and `h_beta''(x)=1/sqrt(x^2+beta^2)>0`. The standard spectral gradient formula used here is: if f is differentiable and invariant under coordinate permutations and F(X)=f(lambda(X)), then for an orthogonal eigendecomposition X=U diag(lambda)U^T,

`grad F(X)=U diag(grad f(lambda))U^T`.

Its hypotheses hold because f is the finite sum of the smooth scalar functions h_beta. In particular, `grad Phi_beta(0)=0`.

We now derive the nuclear-norm curvature bound, rather than using the specialized external theorem as an unexplained premise. Work in an eigenbasis of X, write its eigenvalues as lambda_i, and let H be a symmetric direction expressed in that basis. Differentiating the spectral gradient gives

`D^2 Phi_beta(X)[H,H]=sum_{i,j} c_{ij} H_{ij}^2`,

where

`c_{ij}=(h_beta'(lambda_i)-h_beta'(lambda_j))/(lambda_i-lambda_j)`

for unequal eigenvalues and `c_{ij}=h_beta''(lambda_i)` when they are equal. To see the off-diagonal formula, differentiate `(X+tH)u_i(t)=lambda_i(t)u_i(t)` at a simple spectrum: `lambda_i'(0)=H_{ii}` and `u_j^T u_i'(0)=H_{ji}/(lambda_i-lambda_j)` for j unequal to i. Substitution into the derivative of `sum_i h_beta'(lambda_i(t))u_i(t)u_i(t)^T` gives the displayed coefficients. The divided differences extend continuously to repeated eigenvalues, giving the same formula there.

Let `d_i=sqrt(lambda_i^2+beta^2)>0`. The divided-difference integral and convexity of x -> sqrt(x^2+beta^2) give

`c_{ij}=int_0^1 1/sqrt(((1-v)lambda_i+v lambda_j)^2+beta^2) dv >= int_0^1 1/((1-v)d_i+v d_j) dv >= 2/(d_i+d_j)`.

The last inequality is scalar Jensen for the reciprocal function; it also holds for equal eigenvalues.

Let S=sign(H), defined by applying sign to the eigenvalues of H and setting sign(0)=0. Then S is symmetric, `||S||_2<=1`, and `Tr(SH)=||H||_*`. Weighted Cauchy-Schwarz yields

`||H||_*^2 <= (sum_{i,j} 2H_{ij}^2/(d_i+d_j)) (sum_{i,j} (d_i+d_j)S_{ij}^2/2)`.

Because S is symmetric and `S^2<=I`, the second factor is

`sum_i d_i sum_j S_{ij}^2 <= sum_i d_i <= ||X||_*+n beta`.

Thus, whenever `||X||_*<=tau`,

`D^2 Phi_beta(X)[H,H] >= ||H||_*^2/(tau+n beta)`.

The nuclear-norm ball is convex. Integrating this inequality along the segment between any two points X,Y of the ball gives

`D_Phi(X||Y)>=||X-Y||_*^2/[2(tau+n beta)]`.

In particular, the weaker bound needed below holds:

`D_Phi(X||Y)>=||X-Y||_*^2/[4(tau+n beta)]`.

The source imports this weaker assertion as a specialized result. The calculation above closes that dependency directly.

For a block-diagonal matrix, the eigenvalue multiset is the union of the block eigenvalue multisets. Consequently Phi_beta and the nuclear norm add over blocks, while the spectral norm is the maximum block spectral norm. The gradient is block diagonal by the spectral gradient formula. Expanding the definition of Bregman divergence therefore gives

`D_Phi(W||W')=sum_m D_Phi(W_m||W'_m)`.

On the product radius-tau ball, the preceding curvature bound applies separately to every block with n=d_q.

The feasible set is compact and convex, and the update objective is continuous and strictly convex. Its minimizer exists and is unique. The minimizer depends continuously on the finite-dimensional objective parameters: this follows by taking convergent subsequences of minimizers in the compact feasible set and using continuity and uniqueness. The online iterates are consequently measurable functions of the available history.

## 4. Pathwise mirror-descent inequality and the initial divergence

The update separates over blocks. For a fixed feasible comparator U=diag(U_1,...,U_M), first-order optimality for block m gives

`<eta hat G_{t,m}+grad Phi_beta(W_{t+1,m})-grad Phi_beta(W_{t,m}), U_m-W_{t+1,m}>_F >=0`.

Expanding the three Bregman divergences in the resulting inner product yields

`eta<hat G_{t,m},W_{t+1,m}-U_m>_F <= D_Phi(U_m||W_{t,m})-D_Phi(U_m||W_{t+1,m})-D_Phi(W_{t+1,m}||W_{t,m})`.

Add `eta<hat G_{t,m},W_{t,m}-W_{t+1,m}>_F`. For symmetric matrices G,H, nuclear/spectral duality gives `|<G,H>_F|<=||G||_2||H||_*`: diagonalize H and bound each Rayleigh quotient of G by its spectral norm. With `B=tau+beta d_q`, the curvature bound gives

`eta<hat G_{t,m},W_{t,m}-W_{t+1,m}>_F-D_Phi(W_{t+1,m}||W_{t,m}) <= eta g z-z^2/(4B) <= eta^2 B g^2`,

where `g=||hat G_{t,m}||_2` and `z=||W_{t,m}-W_{t+1,m}||_*`. The last inequality follows by completing the square.

Sum over t and m, telescope, and discard the nonnegative final divergences. Pathwise, for every feasible U,

`sum_t <hat G_t,W_t-U>_F <= D_Phi(U||0)/eta + eta(tau+beta d_q)sum_t sum_m ||hat G_{t,m}||_2^2`.

The initial-divergence estimate must cover zero and small comparator blocks. If rho=||U_m||_*<=tau, then the scalar formula and grad Phi_beta(0)=0 give

`D_Phi(U_m||0)=sum_i [lambda_i asinh(lambda_i/beta)-sqrt(lambda_i^2+beta^2)+beta] <= sum_i |lambda_i| asinh(|lambda_i|/beta) <= rho asinh(rho/beta) <= tau asinh(tau/beta)`.

This is valid at rho=0 and for every beta>0. In contrast, `rho log(3rho/beta)` is not a valid uniform bound when rho is small. Summing the valid estimate gives

`D_Phi(U||0)<=M tau asinh(tau/beta)`.

## 5. Expectation order and parameter substitution

Fix one deterministic comparator U in the product ball. Since W_t-U is H_t-measurable, conditional unbiasedness proves

`E<hat G_t,W_t-U>_F=E<grad L_t(W_t),W_t-U>_F`.

All terms are integrable: iterates and comparators are bounded, and the established conditional second moments control the gradients. Taking expectations of the pathwise inequality therefore yields, for every fixed U,

`E[sum_t <grad L_t(W_t),W_t-U>_F] <= M tau asinh(tau/beta)/eta + 10 eta(tau+beta d_q)T`.

The right side is independent of U. Taking the supremum over fixed U after this expectation proves exactly the public regret bound. No exchange of supremum and expectation, or conditioning on a completed adaptive query sequence, is used.

Set `tau=2s`, `beta=tau/d_q`, and `eta=sqrt(M log d_q/T)`. These are positive because s,T,M are positive and d_q>=2. Since

`asinh(d_q)<=log(3d_q)<=3log d_q`,

the first term is at most `3tau sqrt(MT log d_q)`. The second is `20tau sqrt(MT log d_q)`. Hence

`Reg_T(2s)<=23tau sqrt(MT log d_q)=46s sqrt(MT log d_q)`.

This proves the stated universal-constant upper bound. The argument also covers M=1, zero queries, singleton action sets, zero comparator blocks, and epsilon=0 without division by a vanishing quantity. It proves the linearized regret benchmark only, not exact nonconvex policy regret.
