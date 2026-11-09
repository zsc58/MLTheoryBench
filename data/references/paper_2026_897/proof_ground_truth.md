# Reference Proof

## Proof Structure

1. Recover the convex-loss implication needed for covariance continuity, without treating a specialized citation as a completed proof.
2. Establish almost-sure consistency and root-n tightness using localized second moments, not an unconditional root-n moment bound.
3. Construct the singular linear diffusion and establish its boundary condition and uniqueness.
4. Verify conditional moment convergence, local Lindeberg, and compact containment for the rescaled chains.
5. Apply diffusion approximation away from zero, extract compatible limits, identify their boundary behavior, and conclude full-sequence convergence.

## Complete Proof

Write e_k=theta_k-theta*, A=nabla^2 Phi(theta*), H=delta A-I, and Q=delta^2 Gamma. Let sigma^2 be a finite uniform bound for the noise second moments. Since delta lambda_1>1, H is symmetric positive definite. Since Phi is differentiable near theta*, its subgradient selection there is G=nabla Phi, and G(theta*)=0. In particular Gamma is a finite positive-semidefinite covariance matrix. No invertibility of Gamma is assumed.

### 1. Convex losses and covariance continuity

We first justify an implication that is essential to the conditional covariance calculation. Let f(theta)=phi(X_1,theta). For a coordinate unit vector v and h>0, convexity gives

D_h=[f(theta*+hv)+f(theta*-hv)-2f(theta*)]/h >= 0.

The expectation of D_h is the same symmetric difference quotient of Phi. It tends to zero as h decreases to zero because Phi is differentiable at theta*. Finite convex functions have finite directional derivatives at interior points, so D_h tends to f'(theta*;v)+f'(theta*;-v). Fatou's lemma shows that this nonnegative limit is zero almost surely. Intersect the resulting probability-one events over the d coordinate directions. For any subgradient z of f at theta*, the supporting inequalities imply

-f'(theta*;-v) <= z^T v <= f'(theta*;v).

The two endpoints coincide in each coordinate. The subdifferential is nonempty for a finite convex function on R^d, so it is a singleton, and f is differentiable at theta* almost surely.

We also spell out the required subgradient continuity. Subgradients of a finite convex function are bounded on any sufficiently small neighborhood of an interior point: apply the supporting inequality in both coordinate directions at a fixed positive distance and use boundedness of the function on a larger compact neighborhood. If theta_m tends to theta*, any cluster point z of subgradients at theta_m satisfies f(u)>=f(theta*)+z^T(u-theta*) for every u, by continuity of f. The singleton subdifferential at theta* therefore implies

g(X_1,theta_m) -> g(X_1,theta*) almost surely.

Choose a ball B(theta*,rho) contained in the neighborhood in the envelope assumption, and set

W=sup_{theta in B(theta*,rho)} ||g(X_1,theta)-G(theta)||^2.

Then E W<infinity and, on that ball,

||g(X_1,theta)||^2 <= 2W+2L^2 rho^2.

Dominated convergence consequently gives

E[g(X_1,theta)g(X_1,theta)^T] -> Gamma as theta -> theta*.

This is continuity at a point, hence also uniform over any sets whose maximum distance from theta* tends to zero. Since G(theta)->0, the noise covariance tends to Gamma as well. This closes the specialized convex-loss dependency used by the source; no continuity assumption on individual stochastic gradients has been added.

### 2. Consistency and localized root-n tightness

Independence and the measurability of the recursion give

E[epsilon_k|F_{k-1}]=0,   E[||epsilon_k||^2|F_{k-1}]<=sigma^2.

The exact squared-distance expansion, convexity, and the growth bound yield

E[||e_k||^2|F_{k-1}]
<= (1+delta^2 L^2/k^2)||e_{k-1}||^2
   -(2delta/k)(Phi(theta_{k-1})-Phi(theta*))
   +delta^2 sigma^2/k^2.                                      (1)

All finite-index second moments are finite by induction. We use the following standard independent almost-supermartingale result: if nonnegative adapted integrable V_k satisfy E[V_k|F_{k-1}]<=(1+a_k)V_{k-1}-b_k+c_k, with nonnegative predictable terms and summable a_k,c_k, then V_k converges almost surely and sum b_k is finite almost surely. Here a_k=delta^2L^2/k^2 and c_k=delta^2sigma^2/k^2 are summable. Thus ||e_k||^2 converges and the objective gaps weighted by 1/k are summable.

If the limiting distance were positive, the iterates would eventually lie in a compact annulus about theta*. Continuity of the finite convex function Phi and uniqueness of its minimizer give a strictly positive objective gap on that annulus. This contradicts the divergent harmonic sum. Hence e_k->0 almost surely.

Choose rho>0 and alpha>1/delta so that nabla^2 Phi>=alpha I on B(theta*,rho). In this ball, Phi(theta)-Phi(theta*)>=(alpha/2)||theta-theta*||^2. For a deterministic N, let A_{N:k} be the event that theta_N,...,theta_k all belong to the ball, and put

V_k=E[||e_k||^2 1_{A_{N:k}}],   k>=N.

Because A_{N:k} is contained in A_{N:k-1} and the latter is F_{k-1}-measurable, (1) implies

V_k <= (1-alpha delta/k+delta^2L^2/k^2)V_{k-1}+delta^2sigma^2/k^2.

Choose 1<beta<alpha delta. Increase N so the coefficient is at most 1-beta/k and this latter coefficient is nonnegative for k>N. With

K_N >= max{NV_N, delta^2sigma^2/(beta-1)},

induction gives V_k<=K_N/k: substituting V_{k-1}<=K_N/(k-1) leaves the sufficient inequality delta^2sigma^2<=K_N(beta-1)k/(k-1).

Let A_{N:infinity} be the event that every iterate from N onward stays in the ball. For k>=N,

P(sqrt(k)||e_k||>R) <= K_N/R^2 + P(A_{N:infinity}^c).

Almost-sure consistency implies P(A_{N:infinity}^c)->0 as N->infinity. First choosing N and then R, and including the finitely many earlier indices, proves

q(R):=sup_{k>=1} P(sqrt(k)||e_k||>R) -> 0 as R->infinity.       (2)

We have proved tightness, not sup_k k E||e_k||^2<infinity. All subsequent arguments use only (2).

### 3. The limiting diffusion

Let mu_1,...,mu_d>0 be the eigenvalues of H with orthonormal eigenvectors v_1,...,v_d. The integral

Y_t=integral_0^t (s/t)^H Q^{1/2}dB_s

is well defined by Ito isometry. In particular,

E||Y_t||^2=t sum_i (v_i^T Q v_i)/(2mu_i+1),                   (3)

which tends to zero as t decreases to zero. On each interval bounded away from zero, variation of constants gives a continuous adapted solution of

dY_t=-t^{-1}HY_t dt+Q^{1/2}dB_t.

Its generator on C_c^2 test functions is

mathcal G_t f(y)=-t^{-1}(Hy)^T nabla f(y)+(1/2)Tr(Q nabla^2 f(y)).

The standard independent SDE facts used here are: continuous coefficients that are globally Lipschitz in the state, with linear growth on a fixed bounded time interval, give a unique nonexplosive solution for each initial law; Ito's formula identifies its martingale problem, and the corresponding linear martingale problem is well posed. On [eta,T] our drift has Lipschitz constant at most ||H||/eta and the diffusion coefficient is constant, so these hypotheses hold, including for singular Q.

For 0<s<t every fixed-driver solution satisfies

Z_t=(s/t)^H Z_s+integral_s^t (u/t)^H Q^{1/2}dB_u.             (4)

If Z_s->0 in probability, the initial term in (4) tends to zero in probability, while the stochastic integral converges in L2 to the integral from zero. This proves uniqueness for a fixed Brownian driver. For the martingale problem, well-posedness on [s,T] gives the same transition law and independence of the driving increments from the initial state at s. Letting s decrease to zero in the joint transition law at any finite collection of positive times proves uniqueness in law under the boundary condition. Processes on different couplings need not be indistinguishable.

For completeness, the source's stronger almost-sure boundary assertion is also available. In each eigen-coordinate write M_t=integral_0^t u^{mu_i}v_i^T Q^{1/2}dB_u. Doob's L2 inequality on a dyadic interval (a/2,a] bounds E sup_{a/2<t<=a}|t^{-mu_i}M_t|^2 by a constant depending on mu_i and Q times a. Sum the resulting probability bounds over a=2^{-m} and use Borel-Cantelli. This gives Y_t->0 almost surely; only convergence in probability is needed for the task.

### 4. Conditional moments and local Lindeberg

For k>=2, condition on the preceding rescaled state y. Put

theta=theta*+sqrt(n)y/(k-1),
m_{n,k}(y)=y/(k-1)-delta G(theta)/sqrt(n).

The exact increment is

Delta=m_{n,k}(y)-delta[g(X_k,theta)-G(theta)]/sqrt(n).          (5)

Take k=floor(nt), t in [eta,T], and ||y||<=R, with n sufficiently large. The queried theta approaches theta* uniformly. Since G(theta*+u)=Au+o(||u||), uniformly as u->0,

n m_{n,k}(y) -> t^{-1}(I-delta A)y=-t^{-1}Hy.

Let C(theta)=E[(g(X_1,theta)-G(theta))(g(X_1,theta)-G(theta))^T]. Conditional centering gives

n E[Delta Delta^T|y]=n m_{n,k}(y)m_{n,k}(y)^T+delta^2 C(theta).

Here m_{n,k}=O(1/n) uniformly on the indicated compact set, and Section 1 gives C(theta)->Gamma uniformly there. Thus the conditional second moments converge uniformly to Q.

For every r>0 the same compact set satisfies the local Lindeberg condition

sup_{t,y} n E[||Delta||^2 1_{||Delta||>r}|y] -> 0.             (6)

Indeed, for large n the deterministic mean in (5) is at most r/2, and the noise is bounded in squared norm by the integrable variable W introduced in Section 1. The left side is bounded by O(1/n)+C E[W 1_{W>c n}], with positive constants depending on the compact set and r. This tends to zero by integrability. In particular n P(||Delta||>r|y)->0 uniformly. An unrefined second-moment Markov bound alone would not establish this limit.

### 5. Compact containment and approximation away from zero

Fix 0<eta<T. Start at the grid index a_n=floor(n eta), which is positive for large n. By (2), the laws of tilde Y_{a_n}^n are tight. For indices from a_n+1 through ceil(nT), the global growth bound in (5) gives

||m_{n,k}(y)|| <= C_eta ||y||/n,

and the centered increments have conditional second moments at most delta^2sigma^2/n. Let M_j be their partial sums after a_n. Orthogonality of martingale differences and the standard L2 maximal inequality yield

E[max_j ||M_j||^2] <= 4delta^2sigma^2(T+1)

for all sufficiently large n. The sum form of (5) and discrete Gronwall therefore imply

max_{a_n<=j<=ceil(nT)} ||tilde Y_j^n||
<= C_{eta,T}(||tilde Y_{a_n}^n||+max_j||M_j||).

Consequently, for every epsilon>0 there is R<infinity such that the probability of leaving the ball of radius R on this grid interval is at most epsilon, uniformly for large n. The finitely many remaining processes do not affect tightness. This is compact containment.

We use the following standard independent diffusion-approximation result in its localized form. For Markov chains on meshes tending to zero, suppose the scaled first and second conditional moments converge locally uniformly to continuous drift and covariance, the local conditional Lindeberg condition holds, compact containment holds, and initial laws converge. If the limiting continuous martingale problem is nonexplosive and well posed for the limiting initial law, the polygonal interpolations converge weakly to that solution on the bounded time interval. The conclusion also holds when the starting grid time tends to the specified initial time. Tight initial laws permit subsequence extraction before application.

Every hypothesis has now been verified: iid observations give the Markov transition kernel (5); the mesh is 1/n; Sections 4 and 5 give moments, Lindeberg, and compact containment; and Section 3 gives well-posedness and nonexplosion. The grid-to-interpolation passage can also be checked directly: before exit from a fixed ball, the union bound over O(n) transitions and (6) imply that the maximum jump tends to zero in probability; compact containment then removes the stop. Thus restrictions to [eta,T] are tight, and every subsequential limit solves the stated martingale problem on that interval. No initial law is identified at this stage.

### 6. Compatible limits and the boundary at zero

Use the intervals [1/p,p], p>=2. Their restriction laws are tight. For a prescribed error epsilon choose compact sets for each interval with failure probabilities at most epsilon 2^{-p}. Their inverse-image intersection has relatively compact closure in the compact-open topology, by a diagonal Arzela-Ascoli argument. The union bound then establishes tightness on C^0((0,infinity),R^d). This is a Polish space, so the standard Prokhorov theorem gives weakly convergent subsequences. Every limit Z has the required martingale problem on every positive-time compact interval, by the preceding step and the continuity of restriction.

It remains essential to determine its boundary behavior. For fixed t>0 put k=floor(nt), define the index-zero scaled error to be zero, and use the interpolation formula. Since each endpoint equals sqrt(j/n) times sqrt(j)e_j,

||Y_t^n|| <= sqrt(t+1/n) max{sqrt(k)||e_k||,sqrt(k+1)||e_{k+1}||}.

For n>=1/t, (2) and the union bound imply

P(||Y_t^n||>r) <= 2q(r/sqrt(2t)).

Evaluation at t is continuous for the compact-open topology. Portmanteau's open-set inequality, not an equality of tail probabilities at every threshold, therefore gives

P(||Z_t||>r) <= liminf_n P(||Y_t^n||>r)
              <= 2q(r/sqrt(2t)) -> 0 as t downarrow zero.

Thus Z_t->0 in probability. Section 3 now identifies its law with that of Y, jointly on all compact intervals. Every convergent subsequence has this same limit law, and tightness implies convergence of the full sequence in the requested compact-open topology.

All theorem-critical obligations are closed. In particular, no covariance-continuity hypothesis, unconditional root-n second-moment bound, nondegeneracy of Gamma, or specialized citation-only lemma is being assumed.
