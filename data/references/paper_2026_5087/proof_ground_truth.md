# Reference Proof

All constants below are independent of theta. They may depend on the fixed finite grid, the schedule, dimension, coefficient bounds, initial law, and terminal position prior. No uniformity over grid refinement is asserted.

## Obligations

1. Verify that all kernels and the objective are well-defined and have the moments used below.
2. Derive a moment-dependent one-step pair stability estimate and propagate it through finitely many reverse steps.
3. Telescope pair laws, including the correctly sampled terminal momentum.
4. Bound local discrepancies by tangential residuals plus finite theta-independent terms.
5. Control the terminal base-law discrepancy and convert square roots to the stated linear loss.

Each obligation is proved below. No unproved external or paper-specific result is used as a substitute for an obligation.

## Preliminary notation

Put tau_j=sigma_j^2 Delta t and nu_j=tau_j sqrt(1-a_j^2). For an input pair y=(x,x'), let

p_j(y)=Pi(x)(x'-x)/(sigma_{j+1}^2 Delta t).

The reverse first-coordinate update is

F_j^theta(y,z)=x-tau_j a_j Pi(x)p_j(y)-tau_j^2 Pi(x)b_j^theta(x,p_j(y))+tau_j phi(x,p_j(y))+nu_j Pi(x)z.

Its pair output is G_j^theta(y,z)=(F_j^theta(y,z),x). Here and throughout, each Gaussian noise is independent of the input to its update.

The Moore-Penrose formula gives Pi(x)^T=Pi(x), Pi(x)^2=Pi(x), and operator norm at most one. These are pointwise matrix facts, including for empty or rank-deficient constraint matrices. On each of the finitely many active-set regions the selected gradient matrix is Borel, and the pseudoinverse is a Borel matrix function. Consequently Pi and the displayed updates are Borel. No continuity or Lipschitz property of Pi across active-set changes is asserted or needed. The Gaussian covariance nu_j^2 Pi(x) is positive semidefinite, including when it vanishes.

## Step 001: Moment closure and one-step stability

For every r>=1, the growth hypotheses imply, with finite constants depending on r and the fixed grid,

E||F_j^theta(Y,Z)||^{2r} <= C_r[1+E||X||^{2r}+E||p_j(Y)||^{4r}].

Indeed, bound the five summands of F separately, use ||Pi||<=1, use the uniform linear-growth bound for b, apply the stated bound for phi, and use the finite Gaussian 2r-th moment. Terms of order 2r in p can be absorbed using u^{2r}<=1+u^{4r}.

For the output pair Y^-=(X^-,X), its next pseudo-momentum is

p_{j-1}(Y^-)=Pi(X^-)(X-X^-)/(sigma_j^2 Delta t)

whenever another reverse step is to be performed. Direct substitution gives

||p_{j-1}(Y^-)|| <= a_j||p_j(Y)||+tau_j||b_j^theta(X,p_j(Y))||+sqrt(1-a_j^2)||Z||+||phi(X,p_j(Y))||.

Thus, writing

A_j^(r)(eta)=E_eta[||X||^{2r}+||X'||^{2r}+||p_j(X,X')||^{2r}],

we obtain

A_{j-1}^(r)(eta bar R_j^theta) <= C_r[1+A_j^(2r)(eta)].

At the last step only the position-moment estimate is needed. The constants are uniform in theta. A finite number of applications requires only a finite number of successive doublings of the input moment order.

For completeness, the forward update has the same all-order closure. If v_j is its input momentum, its position update satisfies

E||X_{j+1}||^{2r} <= C_r[1+E||X_j||^{2r}+E||v_j||^{4r}].

For j+1<N, its next momentum is Pi(X_{j+1})(X_{j+1}-X_j)/tau_j. Substituting the forward update and using ||Pi||<=1 bounds its norm by

||v_j||+tau_j||u_j(X_j,v_j)||+sqrt(1-a_j^2)||Z_j||+||psi_j(X_j,v_j)||.

The same growth estimate therefore applies to its 2r-th moment. The initial position and Gaussian momentum have all-order moments, so finite induction proves all-order moments for X_0,...,X_N. The terminal auxiliary point also has all-order moments because it is X_N+sigma_{N+1}^2 Delta t Pi(X_N)Z_*. The fixed base pair prior has all-order moments for the same reason. Since Delta t>0 is fixed and the schedule is positive, every pseudo-momentum obtained from an all-order pair law has all-order moments. The reverse recursion consequently gives theta-uniform moments for every law obtained from these finitely many source laws by finitely many reverse updates. This also proves finiteness of the loss.

Now define

M_j(eta)^2=E_eta[||X||^2+||X'||^2+||p_j(X,X')||^2+||p_j(X,X')||^4].

Take any coupling (Y,Y') of eta and xi and use the same independent Gaussian Z in their updates. Set p=p_j(Y), p'=p_j(Y'), and let x,x' denote their first coordinates. Minkowski's inequality gives

||G_j^theta(Y,Z)-G_j^theta(Y',Z)||_{L^2}
<=2||x-x'||_{L^2}
+tau_j a_j(||p||_{L^2}+||p'||_{L^2})
+tau_j^2(||b_j^theta(x,p)||_{L^2}+||b_j^theta(x',p')||_{L^2})
+2nu_j sqrt(d)
+tau_j(||phi(x,p)||_{L^2}+||phi(x',p')||_{L^2}).

The growth assumptions and schedule bounds bound the last four lines by

c_j Delta t[1+M_j(eta)+M_j(xi)].

For an arbitrary fixed positive Delta t this follows with c_j allowed to depend on that grid; no restriction Delta t<=1 is necessary. Taking the infimum over input couplings yields

W_2(eta bar R_j^theta,xi bar R_j^theta)
<=2W_2(eta,xi)+c_j Delta t[1+M_j(eta)+M_j(xi)].

This derivation uses only projector boundedness, not a Lipschitz bound on the projector.

## Step 002: Finite propagation and pair telescoping

Let H_k=bar R_k^theta...bar R_1^theta, with H_0 the identity. For the finitely many comparisons used below, all intermediate M_j moments have theta-uniform finite bounds by Step 001. Iterating the displayed stability inequality gives

W_2(eta H_k,xi H_k)<=2^k W_2(eta,xi)+E_{eta,xi,k} Delta t,

where a theta-independent finite upper bound for E_{eta,xi,k} can be chosen for every comparison in the argument. Explicitly, if the successive additive constants are e_1,...,e_k, the final additive coefficient is a finite sum of the form sum_i 2^{k-i}e_i.

Use the augmented forward path specified in the public task, and write bar Q_k=Law(X_k,X_{k+1}) for 0<=k<=N. Define

bar sigma_0=bar Q_0,
bar sigma_k=bar Q_k H_k for 1<=k<=N.

The generated pair law is bar P_0^theta=bar pi_N H_N. Projection onto the first coordinate cannot increase a coupling's Euclidean cost. Hence triangle inequality and finite propagation give

W_2(Q_0,P_0^theta)
<=sum_{j=1}^N 2^{j-1} W_2(bar Q_{j-1},bar Q_j bar R_j^theta)
+2^N W_2(bar Q_N,bar pi_N)+E Delta t,

for a finite E independent of theta.

This formula also holds for N=1: the initial propagation kernel H_0 is the identity.

## Step 003: A local Gaussian coupling

Fix j. Sample the forward triple (X_{j-1},X_j,X_{j+1}) from the augmented forward experiment, and independently sample Z~N(0,I_d). Let

Y=m_j^theta(X_j,X_{j+1})+nu_j Pi(X_j)Z.

Then (X_{j-1},X_j) has law bar Q_{j-1}, while (Y,X_j) has law bar Q_j bar R_j^theta. This is a measurable coupling even if the Gaussian is singular. Its shared second coordinate has zero cost. Independence and centering of Z give

W_2^2(bar Q_{j-1},bar Q_j bar R_j^theta)
<=E||X_{j-1}-m_j^theta(X_j,X_{j+1})||^2
+nu_j^2 E tr(Pi(X_j)).

This is also a conditional argument: given (X_j,X_{j+1}), it couples the true preceding position and the reverse Gaussian independently. Optimal conditional couplings are unnecessary.

The reference proof's mean/centered-law observation can alternatively be justified directly. For laws with means u,v, every coupling has squared cost ||u-v||^2 plus the cost between the centered variables, since the cross term has expectation zero. Taking infima proves the corresponding centered-law identity. A reverse Gaussian's centered law is independent of theta. However, the explicit coupling above already supplies the required upper bound without a Gelbrich-distance theorem.

## Step 004: Tangential and normal residuals

Put Pi_j=Pi(X_j) and p_j=p_j(X_j,X_{j+1}). Orthogonality gives

||X_{j-1}-m_j^theta||^2
=||Pi_j(X_{j-1}-m_j^theta)||^2
+||(I-Pi_j)(X_{j-1}-X_j-tau_j phi(X_j,p_j))||^2.

All learned terms in m_j^theta are multiplied by Pi_j and disappear from the second term. Define

ell_j(theta)=E||Pi_j(X_{j-1}-m_j^theta(X_j,X_{j+1}))||^2,

D_j=E||(I-Pi_j)(X_{j-1}-X_j-tau_j phi(X_j,p_j))||^2
+nu_j^2 E tr(Pi_j).

Each D_j is nonnegative, finite, and independent of theta by Step 001, the fixed forward experiment, and theta-independence of phi. Therefore

W_2^2(bar Q_{j-1},bar Q_j bar R_j^theta)<=ell_j(theta)+D_j.

Because phi is normal, its inclusion in the full Gaussian mean does not change the tangential objective relative to the tangential mean used in the source.

## Step 005: Terminal experiment and conclusion

The terminal training pair uses X_N from the forward law and fresh momentum Pi(X_N)Z_*. The terminal prior pair uses a position from pi_N and fresh momentum from precisely the same conditional projected Gaussian construction. Both base pair laws are independent of theta and have finite second moments. Thus

B=2^N W_2(bar Q_N,bar pi_N)

is finite and independent of theta. For example, independent coupling bounds this distance by the sum of the two root second moments.

Importantly, the propagated terminal discrepancy itself can depend on theta; it is its upper bound B+E_term Delta t that is theta-independent. No true forward conditional kernel is evaluated under the position prior, and no expectation under that prior is identified with a training expectation.

Let A_j=2^{j-1}. Substitution gives

W_2(Q_0,P_0^theta)<=sum_{j=1}^N A_j sqrt(ell_j(theta)+D_j)+B+E Delta t.

Use sqrt(u+v)<=sqrt(u)+sqrt(v) and sqrt(u)<=(u+1)/2 for u,v>=0. Since L^u(theta)=sum_j ell_j(theta), the required constants can be chosen as

C_1=(1/2)max_j A_j,
C_2=B+sum_{j=1}^N A_j(sqrt(D_j)+1/2),
C_3=E.

They are finite, nonnegative, and independent of theta. This proves the stated inequality. The proof includes gamma=0, zero-rank projectors, empty constraint families, and singular Gaussian kernels.

## Valid alternative proof

The frozen conclusion permits arbitrary finite theta-independent additive constants. Step 001 alone also gives sup_theta E_{P_0^theta}||X||^2<infinity. Independent coupling then gives a theta-uniform upper bound for W_2(Q_0,P_0^theta). Taking that bound as C_2, with C_1=1 and C_3=0, is a complete alternative proof of the literal target. It is less informative about the objective but must not be rejected or penalized for omitting the telescoping presentation.
