# Reference Proof

## Verification Status

The public contract has been checked against the complete source and the preceding repairs are retained. Finding F1 correctly identified the previously disclosed local-comparison gap. This replacement closes the homogeneous uniform local comparison directly under the public flat-torus assumptions. It does not assume or claim independent verification of the exact external formula quoted by the source. All theorem-critical obligations below are closed.

## Theorem-Critical Obligations

1. Define and type the torus tangent spaces, weighted projections, endpoint field transfers, and exponential updates. Closed in Section 1 and by the public definitions.
2. Establish the relevant base Jacobi field and its scaling. Closed directly on the flat torus in Section 5.
3. Establish the homogeneous, uniform local projected-base/Wasserstein comparison. Closed in Section 5 using the pulled-back tangent projections.
4. Compose the local approximation estimate and cover every positive integer N. Closed in Section 6.
5. Derive projection estimates, parallel-field H1 propagation, and time regularity from primitive admissibility. Closed in Sections 2 and 3.
6. Prove destination-measure stability of exact transport in the endpoint norm used by the counterfactual update. Closed in Section 4.
7. Derive the one-step counterfactual recurrence with uniform constants and correct control-source measures. Closed in Section 7.
8. Solve and sum the scalar recurrence, including its continuous q=0 interpretation. Closed in Section 8.

## 1. Tangent Spaces and Projections

Write dx for normalized Lebesgue measure on the unit torus. Every relevant density satisfies m<=rho<=M. Thus weighted L2 and H1 norms are uniformly equivalent to their unweighted counterparts, with factors determined by m and M.

The tangent space is the closure of smooth periodic gradients. It equals G={grad psi: psi in H1(T^d)}. Indeed, for a convergent sequence of gradients, subtract the means of their potentials. The periodic Poincare inequality makes those potentials Cauchy in H1. Their limit has the specified gradient. Conversely, smooth periodic functions are dense in H1. In particular G is the same set for every relevant density, although its orthogonal projection depends on the weight. Smooth periodic gradients are also dense in G intersect H1 in the H1 norm, by Fourier truncation of the potential.

For z in L2, Pi_rho z=grad psi, where psi is the mean-zero solution of

integral rho grad psi dot grad xi dx = integral rho z dot grad xi dx.

Here the bilinear form on mean-zero H1 is bounded by M||psi||_H1||xi||_H1 and coercive with constant m/(1+C_P^2), using Poincare. The right side is a bounded linear functional by Cauchy-Schwarz and density bounds. The standard Lax-Milgram statement is: a bounded coercive bilinear form on a real Hilbert space represents each bounded linear functional by a unique solution. Its hypotheses have just been verified. Testing the variational equation against smooth gradients identifies grad psi with the orthogonal projection. Projection is contractive in its own weighted L2 norm.

## 2. Projection Estimates and Time Regularity

Let p=Pi_rho z and p'=Pi_rho' z. Subtracting their variational equations gives

integral rho (p-p') dot grad xi dx = integral (rho-rho')(z-p') dot grad xi dx.

Since p-p' is a gradient, it is a permissible test gradient. Coercivity, Cauchy-Schwarz, and projection contractivity yield

||p-p'||_L2(dx) <= C||rho-rho'||_Linfinity ||z||_L2(dx).

For z in H1, the potential equation can be written distributionally as

Delta psi = div z + rho^(-1) grad rho dot (z-grad psi).

Its right side belongs to L2. The torus Fourier identity implies psi in H2: for nonzero frequencies, the Fourier coefficient of Delta psi is proportional to |k|^2 psi_hat(k), so its L2 norm controls the H2 norm of the mean-zero potential. Thus spatial differentiation and testing with partial_k psi are justified. Differentiating the weighted variational equation gives

m||partial_k p||_L2 <= ||partial_k rho||_Linfinity ||z-p||_L2 + M||partial_k z||_L2.

Together with the L2 bound this proves ||Pi_rho z||_H1<=C||z||_H1. Differentiating the difference equation, with H=(rho-rho')(z-p'), similarly gives

m||partial_k(p-p')||_L2 <= ||partial_k rho||_Linfinity ||p-p'||_L2 + ||partial_k H||_L2.

The product rule, the preceding H1 boundedness, and the L2 difference estimate prove

||Pi_rho z-Pi_rho' z||_H1 <= C||rho-rho'||_W1,infinity ||z||_H1.

These are derived conclusions, not extra assumptions.

Absolute continuity of t -> rho_t into L-infinity and its bounded time derivative imply ||rho_t-rho_s||_Linfinity<=K|t-s|. The L2 projection estimate therefore gives

||Pi_rho_t-Pi_rho_s||_operator <= C|t-s|.

For any L2-valued absolutely continuous z_t, split Pi_t z_t-Pi_s z_s into (Pi_t-Pi_s)z_s+Pi_t(z_t-z_s). Uniform operator boundedness and integrability of the derivative of z prove absolute continuity of Pi_t z_t. For almost every t, difference quotients then give

||partial_t(Pi_t z_t)-Pi_t partial_t z_t||_L2 <= C||z_t||_L2.

One may justify simultaneous strong differentiation of the operator on a countable dense set of vectors and extend its derivative by the uniform operator bound. This avoids assuming operator-norm differentiability. The estimate also holds in any relevant weighted L2 norm by norm equivalence.

## 3. Parallel-Field Propagation and Isometry

Let b_t be an admissible geodesic velocity. The exact parallel equation on the flat torus is

Pi_rho_t(partial_t w_t+Dw_t b_t)=0,

with w_t tangent and w_0=v. The velocity and density satisfy the continuity equation. Construct a solution in the H1 class by Fourier-gradient Galerkin approximation, as in the source.

Choose Laplacian eigenfunctions e_k and V_n=span{grad e_1,...,grad e_n}. Fourier truncations v_n of v converge in H1. Require w_n(t) in V_n, w_n(0)=v_n, and

integral rho_t (partial_t w_n+Dw_n b_t) dot xi dx=0 for every xi in V_n.

The mass matrix is positive definite with the lower density bound; the finite-dimensional coefficient equation has bounded measurable coefficients. Its solution is obtained from the integral equation by Picard iteration on intervals sufficiently short for contraction, and continued through [0,1].

Testing with w_n and using partial_t rho_t+div(rho_t b_t)=0 yields

d/dt integral rho_t |w_n|^2 dx=0.

The H1 estimate can be made explicit. Put a_n=Dw_n b_t and E_n=integral rho_t |Dw_n|_F^2 dx. Since -Delta w_n belongs to V_n, testing the Galerkin equation with it and integrating by parts gives

E_n'/2 = (1/2)integral partial_t rho_t |Dw_n|_F^2 dx - integral grad rho_t dot (Dw_n)^T partial_t w_n dx - integral rho_t Da_n:Dw_n dx - integral grad rho_t dot (Dw_n)^T a_n dx.

In Da_n:Dw_n, the term containing D^2w_n b_t is (1/2)b_t dot grad|Dw_n|_F^2. Integrating it by parts cancels the term with partial_t rho_t by the continuity equation. The remaining derivative-of-velocity term is bounded by C K E_n. The two terms involving grad rho_t are bounded using |grad rho_t|<=K rho_t, ||a_n||_L2(rho_t)<=C K E_n^(1/2), and

||partial_t w_n||_L2(rho_t) <= ||a_n||_L2(rho_t).

The last inequality follows because the Galerkin equation identifies partial_t w_n as the negative weighted orthogonal projection of a_n onto V_n. Consequently

E_n' <= C_d(K+2K^2)E_n.

All coefficients depend only on admissibility. The integrating-factor form of Gronwall is: if f is absolutely continuous and f'<=a f+c, then f(t)<=exp(at)f(0)+c integral_0^t exp(a(t-r))dr. Applying it with c=0 proves uniform H1 bounds; the displayed time-derivative estimate gives uniform L-infinity-in-time L2 bounds for partial_t w_n.

The standard compactness statements used here are: bounded sets in H1 on the compact torus are relatively compact in L2; equicontinuity and relatively compact pointwise images give compactness in C([0,1];L2); bounded sequences in these dual Bochner spaces have weak-star convergent subsequences. The uniform H1 and time-derivative bounds verify these hypotheses. Thus a subsequence converges strongly in C([0,1];L2), and its spatial and time derivatives converge weak-star in L-infinity-in-time L2.

Test the Galerkin equation against a fixed Fourier gradient and a smooth compactly supported time test function. Strong convergence handles the field terms, weak-star convergence handles its derivatives, and the bounded density and velocity coefficients allow passage to the limit. Density of Fourier gradients yields the parallel equation. The initial condition passes through C([0,1];L2) convergence. Closedness of G gives tangency. Weak lower semicontinuity preserves the H1 estimate for almost every time. Strong L2 continuity and weak H1 compactness extend it to every time.

The weighted energy identity applies to the difference of two such solutions and proves uniqueness; applied to one solution it proves isometry. The integrations are justified by the resulting H1 spatial and L2 time regularity, bounded density derivative, and periodic integration by parts. Thus this is the exact parallel field characterized by the source's covariant derivative. We obtain

sup_t ||w_t||_H1(dx) + ||partial_t w||_L-infinity_t L2_x <= C||v||_H1(dx).

Density of H1 gradients in G and the isometry extend the transport operator and its isometry to tangent L2 inputs.

## 4. Destination Stability

Consider two admissible geodesics from the same nu to mu and mu', with densities rho_t,rho_t' and velocities b_t,b_t'. Let w_t,w_t' be their exact parallel fields with the same H1 initial field v. All Eulerian tangent spaces equal G, so e_t=w_t-w_t' and partial_t w_t' belong to G. Subtracting the two projected equations gives

partial_t e_t+Pi_rho_t(De_t b_t)=f_t,

where

f_t=-Pi_rho_t(Dw_t'(b_t-b_t'))-(Pi_rho_t-Pi_rho_t')(Dw_t' b_t').

The projection-difference estimate, density and velocity destination-Lipschitz assumptions, and H1 propagation prove

||f_t||_L2(rho_t) <= C||v||_H1(nu) W2(mu,mu').

The weighted energy identity, tangency of e_t, and the continuity equation yield

(1/2)d/dt ||e_t||_L2(rho_t)^2 = integral rho_t e_t dot f_t dx.

Young's inequality gives E'<=E+C||v||_H1(nu)^2 W2(mu,mu')^2, with E(0)=0. Gronwall gives the linear destination-stability bound after taking square roots. Uniform norm equivalence permits comparison in L2(nu), L2(mu), or L2(mu'). In particular choose C_WPT, depending only on d,m,M,K, large enough that

||PT_(nu->mu)v-PT_(nu->mu')v||_L2(mu') <= C_WPT ||v||_H1(dx) W2(mu,mu').

This choice includes every norm-equivalence factor needed later. The fields in this formula are Eulerian fields on the common torus.

## 5. Local Fanning Estimate

We prove the needed comparison directly, without invoking the external formula quoted at source L002297-L002301.

Consider any segment of length h<=1, restart its time at zero, and write rho_r=(F_r)#rho_0 with F_0=id. Its Eulerian velocity b_r obeys the same spatial Lipschitz bound as the full admissible geodesic. Let H=L2(rho_0;R^d). The pullback

R_r w=w composed with F_r

is an isometry from L2(rho_r) onto H. Define the orthogonal projection on H

Q_r=R_r Pi_rho_r R_r^(-1).

We first bound its variation using only flow derivatives and the tangent-space definition.

The bounded spatial Lipschitz velocity gives bi-Lipschitz flow maps. Their weak derivatives satisfy the variational equation

partial_r DF_r=(Db_r composed with F_r)DF_r

almost everywhere. Integrating this equation, and its inverse equation, yields uniform bounds for DF_r and DF_r^(-1) and Lipschitz time dependence in L-infinity. These assertions also follow by spatial difference quotients of the flow integral equation; the velocity's W1,infinity bound controls the quotients and their limits. Thus, with A_r=DF_r^(-T),

||A_r||_Linfinity + ||A_r^(-1)||_Linfinity <= C,

||A_r-A_s||_Linfinity <= C|r-s|,

where C depends only on d,K for r,s in a segment of length at most one.

By the Sobolev chain rule for a bi-Lipschitz map,

(grad psi) composed with F_r = DF_r^(-T) grad(psi composed with F_r).

Composition with F_r is a bijection of periodic H1 potentials. Consequently

range(Q_r)=A_r G,

where G is the fixed closed space of periodic H1 gradients, now viewed in H. Multiplication by A_r is bounded and invertible on H, so A_r G is closed.

For x in range(Q_s), write x=A_s g. Then A_r g belongs to range(Q_r), and

||(I-Q_r)x||_H <= ||(A_s-A_r)g||_H <= C|r-s|||x||_H.

This bounds ||(I-Q_r)Q_s||. Interchanging r and s bounds ||(I-Q_s)Q_r||. The identity

Q_r-Q_s=(I-Q_s)Q_r-Q_s(I-Q_r)

and adjoint symmetry therefore give

||Q_r-Q_s||_(H->H) <= D|r-s|,

with a uniform D depending only on d,K.

For completeness, operator-Lipschitz dependence supplies the strong derivative needed below without assuming norm differentiability. For each vector in a countable dense subset of H, r -> Q_r x is a Lipschitz Hilbert-valued curve and hence has a derivative almost everywhere bounded by D||x||. On a common full-measure set, those derivatives are linear on a dense linear subset and extend to bounded operators Q_r' with ||Q_r'||<=D. The uniform bound on difference quotients then gives strong differentiation for every fixed x. Product differentiation with an absolutely continuous H-valued curve follows by splitting the corresponding difference quotient.

Now take an H1 tangent input z and let w_r be its exact parallel field from Section 3. Put U_r=R_r w_r. This curve is absolutely continuous in H, with

U_r'=R_r(partial_r w_r+Dw_r b_r).

To justify this material chain rule at the available regularity, approximate w in the norm controlling its L2 time derivative and its L2-in-time H1 spatial derivatives by smooth periodic space-time fields. The classical chain rule holds for each approximation. The density bounds make R_r uniformly bounded on unweighted L2, and the velocity bound controls the transported spatial-derivative term. Thus the pulled-back fields and their derivatives converge in the Hilbert-valued W1,2 norm, proving the formula and its absolutely continuous representative.

Tangency and the exact parallel equation become

Q_r U_r=U_r,

Q_r U_r'=0

almost everywhere. Differentiating the first identity and using the second gives

U_r'=Q_r' U_r.

Section 3's isometry gives ||U_r||_H=||z||_H. Hence

||U_r'||_H <= D||z||_H,

and Q_r U_r'=0 says that this derivative is normal to the current pulled-back tangent space.

On the flat torus the base Jacobi equation is J''=0 in the canonical parallel frame. With J(0)=0 and J'(0)=z(y), the scaled terminal field J(h)/h is z(y) after base parallel transport. Thus the one-step fanning output is an isometric endpoint transfer followed by the endpoint weighted projection. Its pullback to H is exactly Q_h z, and the step is contractive.

Since Q_h U_h=U_h and U_0=z,

Q_h z-U_h = -integral_0^h Q_h U_r' dr

= -integral_0^h (Q_h-Q_r)U_r' dr.

The two established bounds give

||Q_h z-U_h||_H <= integral_0^h D(h-r)D||z||_H dr

= (D^2/2)h^2||z||_H.

Pulling forward by the endpoint isometry proves

||A_segment z-P_segment z||_L2(rho_h) <= C h^2||z||_L2(rho_0).

Every constant is uniform over segments of admissible geodesics. No small-step threshold is needed. Finally, approximate any tangent L2 input by H1 gradients. Contractivity of the fanning step and isometry of exact transport pass the inequality to the limit. The homogeneous local estimate therefore holds for every tangent L2 input, not only for H1 fields.

This proves exactly the quantitative consequence needed by the frozen chain. It does not assert that the full external comparison, with its quoted prefactor and original general-manifold scope, has been independently audited.

## 6. Global Composition

Write A_k and P_k for the approximate and exact kth segment maps. Section 5 gives

||A_k z-P_k z|| <= C h^2||z||

for every tangent L2 input, and each A_k is contractive. Let v_k=P_k v_(k-1), let v_hat_k=A_k v_hat_(k-1), and let e_k be the L2 norm of their difference at time t_k. Linearity and the triangle inequality give

e_k <= ||A_k(v_hat_(k-1)-v_(k-1))|| + ||(A_k-P_k)v_(k-1)||

<= e_(k-1)+C h^2||v||_L2(nu),

where exact-transport isometry was used in the last term. Since e_0=0,

e_N <= C N h^2||v||_L2(nu)=C||v||_L2(nu)/N.

This applies to every positive integer N because Section 5 applies to every segment length h=1/N<=1. Since ||v||_L2(nu)<=||v||_H1(nu), it proves the public estimate with C_tr depending only on d,m,M,K.

The source's geometric error recurrence is also valid: splitting instead at P_k v_hat_(k-1) gives e_k<=(1+C h^2)e_(k-1)+C h^2||v||. Its finite sum has indices 0,...,k-1 and yields e_N<=((1+C/N^2)^N-1)||v||<=C exp(C)||v||/N. Either composition argument closes the same obligation, without assuming an intermediate H1 bound for approximate fields.

## 7. Counterfactual Recurrence

At iteration i the input is v_i at the control measure nu_i, not at a common fixed source. Set w_i=PT_(nu_i->mu_i*)v_i and w_hat_i=FAN_N(nu_i->mu_hat_i*)v_i. Let a_i=W2(mu_hat_i*,mu_i*).

On the flat torus the map x -> x+w_i(x) modulo Z^d is (1+L)-Lipschitz. To check this, join x and y by a shortest torus path, use the canonical identification of tangent vectors, and bound the change in x+w_i(x) by the path length plus L times that length. Pushing an optimal coupling forward gives the corresponding (1+L)a_i Wasserstein bound.

For two fields applied to the same measure, coupling their outputs at the same location gives a Wasserstein bound by their L2 field difference, because d_T(exp_x(a),exp_x(b))<=|a-b|. The triangle inequality therefore gives

a_(i+1) <= (1+L)a_i+||w_hat_i-w_i||_L2(mu_hat_i*).

Split the field difference at PT_(nu_i->mu_hat_i*)v_i. Section 4 bounds the exact-transport difference by S C_WPT a_i. Section 6 and ||v_i||_H1(nu_i)<=sqrt(M)S bound the approximation difference by C_tr sqrt(M)S/N. With B=C_tr sqrt(M)S, or any larger constant,

a_(i+1) <= (1+L+S C_WPT)a_i+B/N, a_0=0.

C_tr and C_WPT depend only on d,m,M,K; B also depends on S. The constants are uniform in i,T,N under the public uniformity assumptions.

## 8. Accumulation

Put q=L+S C_WPT. Iteration gives

a_i <= (B/N) sum_(j=0)^(i-1)(1+q)^j.

For q>0 this is (B/N)((1+q)^i-1)/q. At q=0 the sum is i, which is also the continuous limit of the quotient. Since these upper bounds are nondecreasing in i,

sum_(i=1)^T a_i <= (BT/N)((1+q)^T-1)/q.

The continuous q=0 interpretation is BT^2/N. For fixed T, with all admissibility and input bounds fixed, the displayed factor is independent of N. The accumulated error is therefore O(T/N) and tends to zero. This is a fixed-horizon assertion, not a uniform linear-in-T rate for growing horizons.

## Remaining GT Obligations

None. The formerly open local consistency estimate is derived in Section 5, and the approximation-dependent conclusions are no longer conditional.
