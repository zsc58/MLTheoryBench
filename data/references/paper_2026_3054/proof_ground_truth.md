# Reference Proof

## Obligations

The proof must close: (i) the Gaussian-relative density normalization and the endpoint laws; (ii) the entropy-flow identity with its precise quadratic-error coefficient; (iii) Gaussian LSI and its propagation for the full learned drift; (iv) initialization and terminal limits, without assuming entropy continuity; and (v) evaluation in every stated parameter regime, including the singular time-dependent coefficient. All five obligations are derived below. The specialized propagation citation is not used as an unexplained lemma.

## 1. Laws and Normalization

Write g_d for the standard Gaussian Lebesgue density and tilde p_t=p_t/g_d. Let q_r=p_{T-r} and h_r be the true and learned reverse-time Lebesgue densities. Their laws at initialization are p_T(x)dx and gamma^d; their terminal laws are mu and mu_T^theta. Their drifts are

b_r(x)=-x+2 grad log tilde p_{T-r}(x),

b_r^theta(x)=-x+s^theta(T-r,x).

Thus delta b_r=b_r-b_r^theta is exactly the score error vector, not the difference formed with the unnormalized Lebesgue score. Define

D(r)=KL(q_r(x)dx | h_r(x)dx),

e(r)=integral ||delta b_r(x)||^2 q_r(x)dx=E[epsilon_{T-r}^theta(bar X_{T-r})^2].

The public assumptions give integral_0^T e(r)dr<infinity and D(0)=KL(p_T(x)dx|gamma^d)<infinity.

## 2. Entropy Background and Initialization

For probability measures Q,P, the entropy variational formula is

KL(Q|P)=sup_f {integral f dQ-log integral exp(f)dP},

where f ranges over bounded continuous functions. To verify the upper bound, put v=dQ/dP and apply Jensen's inequality under Q to exp(f)/v. Equality follows by truncating log v and approximating by bounded continuous functions; the extended-value case follows by increasing truncations. Smooth bounded tests suffice for the densities considered here. As a supremum of expressions continuous under weak convergence of Q and P, this formula also proves joint lower semicontinuity of KL.

We establish the required upper estimate at small reverse times rather than infer it from weak convergence. Fix 0<R<T and a smooth bounded terminal test f with bounded derivatives. Let P_{r,R} be the learned transition operator, and put

H(r,x)=log P_{r,R}(exp(f))(x).

The backward equation for P gives

partial_r H+Delta H+b_r^theta dot grad H=-||grad H||^2.

The function H is bounded. Applying this equation along the true reversed diffusion, using localization and the stated drift/error integrability, gives

E[f(Y_R)]-E[H(0,Y_0)]
=integral_0^R E[delta b_r(Y_r) dot grad H(r,Y_r)-||grad H(r,Y_r)||^2]dr
<= (1/4)integral_0^R e(r)dr.

Here z dot w-||w||^2<=||z||^2/4. The one-sided drift bound on [0,R] supplies the bounded gradient estimate for these tests, as also derived in Section 3. The initial entropy variational inequality gives

E[H(0,Y_0)]<=D(0)+log integral exp(H(0,x)) gamma^d(dx).

By the learned transition definition, the last integral is integral exp(f(x))h_R(x)dx. Taking the supremum over f therefore proves

D(R)<=D(0)+(1/4)integral_0^R e(r)dr.                 (A)

In particular D is finite at interior times and limsup_{r down to 0}D(r)<=D(0). This argument does not assume entropy continuity at initialization. The backward-equation and localization argument can first be carried out for smooth coefficients; the source's classical density and continuity setup permits its usual local approximation form. Only the bounded-test identity is needed at the initialization.

## 3. Gaussian LSI and Propagation

For a positive function f, write Phi(f)=f log f and G(f)=||grad f||^2/f. An LSI with constant C means Ent_nu(f)<=C/2 integral G(f)dnu.

First verify the Gaussian constant used here. For the OU transition Q_s, its explicit Gaussian representation gives grad Q_s f=e^{-s}Q_s grad f. Weighted Cauchy-Schwarz yields G(Q_s f)<=e^{-2s}Q_s G(f). For bounded positive smooth f bounded away from zero, invariance and the diffusion chain rule give

-d/ds Ent_gamma(Q_s f)=integral G(Q_s f)dgamma.

The explicit OU transition converges to the Gaussian average, so Ent_gamma(Q_s f) tends to zero. Integration and invariance yield

Ent_gamma(f)<=integral_0^infinity e^{-2s}ds integral G(f)dgamma
=(1/2)integral G(f)dgamma.

Truncation and smoothing extend this to the usual LSI domain. Thus gamma^d has LSI constant 1 in the required normalization.

Now consider dZ_r=a_r(Z_r)dr+sqrt(2)dW_r, with initial law nu_0 satisfying C_0-LSI, and

<a_r(x)-a_r(y),x-y><=L(r)||x-y||^2

on a compact time interval. Set A(s,r)=exp(2 integral_s^r L(u)du). Synchronous solutions initialized at x,y satisfy

d/dr ||Z_r^x-Z_r^y||^2<=2L(r)||Z_r^x-Z_r^y||^2,

and hence ||Z_r^x-Z_r^y||<=sqrt(A(s,r))||x-y||. Applying the difference quotient argument to the transition P_{s,r} gives

||grad P_{s,r}f||<=sqrt(A(s,r))P_{s,r}||grad f||.

Weighted Cauchy-Schwarz consequently gives

G(P_{s,r}f)<=A(s,r)P_{s,r}G(f).                    (B)

These estimates can be interpreted in the weak-gradient sense for continuous one-sided-Lipschitz drifts; the synchronous difference bound gives the same local approximation argument. Nonexplosion and uniqueness on compact time intervals follow from local boundedness, the bound at the origin, and the one-sided inequality.

Using the forward and backward Kolmogorov equations, with the generator at time s, the diffusion chain rule gives the pointwise identity

d/ds P_{0,s}Phi(P_{s,r}f)=P_{0,s}G(P_{s,r}f).

Integrate from 0 to r and apply (B):

P_{0,r}Phi(f)-Phi(P_{0,r}f)
<= [integral_0^r A(s,r)ds] P_{0,r}G(f).

Average under nu_0. The entropy decomposition is

Ent_{nu_r}(f)
=integral [P_{0,r}Phi(f)-Phi(P_{0,r}f)]dnu_0
 +Ent_{nu_0}(P_{0,r}f).

Apply the initial LSI and (B) once more to the second term. This yields

Ent_{nu_r}(f)
<= [integral_0^r A(s,r)ds+(C_0/2)A(0,r)] integral G(f)dnu_r.

Thus the propagated LSI constant is

C(r)=C_0 exp(2 integral_0^r L(u)du)
 +2 integral_0^r exp(2 integral_s^r L(u)du)ds.        (C)

The factor multiplying C_0 is essential. Positive bounded tests bounded away from zero suffice for the interpolation; truncation extends the resulting LSI to positive density ratios with finite relative Fisher information.

For the learned reverse drift, the correct one-sided constant is

L(r)=M_{T-r}-1,

and C_0=1. For constant M, (C) becomes

C(r)=exp(2(M-1)r)+2 integral_0^r exp(2(M-1)s)ds.

For M_t=1+c/t, L(r)=c/(T-r), not 1+c/(T-r). Apply (C) on each [0,S] with S<T; its coefficient is continuous and integrable there. No propagation theorem requiring integrability on the entire closed interval is applied to the singular endpoint.

## 4. Entropy Flow and Endpoint Limits

Put v_r=q_r/h_r. Differentiating the entropy with the two Fokker-Planck equations and integrating by parts gives

D'(r)=-integral q_r||grad log v_r||^2
 +integral q_r delta b_r dot grad log v_r.           (D)

For completeness, the common diffusion terms reduce to -integral h_r||grad v_r||^2/v_r. The drift terms combine to integral h_r grad v_r dot (b_r-b_r^theta). These are precisely the two terms in (D). The interior Fisher-information condition and the error integrability justify Young's inequality; localization gives the same identity or its integrated inequality under the stated classical Fokker-Planck setup.

For alpha in [0,1), Young's inequality gives

D'(r)<=-alpha I(q_r|h_r)+e(r)/(4(1-alpha)).

Choose alpha=1/2. Applying the propagated LSI to v_r gives 2D(r)<=C(r)I(q_r|h_r), so

D'(r)<=-D(r)/C(r)+(1/2)e(r).                       (E)

For 0<delta<S<T, integrate this linear inequality:

D(S)<=exp(-integral_delta^S du/C(u))D(delta)
 +(1/2)integral_delta^S exp(-integral_r^S du/C(u))e(r)dr.

Let delta decrease to zero using (A). The score-error integral converges because e is integrable and all its multiplying factors lie in [0,1]. This gives

D(S)<=exp(-integral_0^S du/C(u))D(0)
 +(1/2)integral_0^S exp(-integral_r^S du/C(u))e(r)dr.  (F)

The continuous sample paths imply that both marginal laws converge weakly to their respective terminal laws as S increases to T. Joint lower semicontinuity of entropy and dominated convergence in (F) therefore imply

KL(mu|mu_T^theta)
<=Lambda(0)KL(p_T(x)dx|gamma^d)
 +(1/2)integral_0^T Lambda(r)e(r)dr,

where Lambda(r)=exp(-integral_r^T du/C(u)). In the singular case 1/C extends continuously to zero at T, as the calculation below verifies. Thus the same limiting argument applies there.

Set lambda_T(t)=Lambda(T-t) and change variables t=T-r. This is exactly the required forward-time integral and initialization term. The expectation remains under the forward law; it is not replaced by the learned law.

## 5. Explicit Weights and Boundary Cases

For M not equal to 1, put k=M-1. Then

C(r)=(M exp(2kr)-1)/k.

For M>1, an antiderivative of 1/C(r) is (1/2)log(M-exp(-2kr)). Consequently

lambda_T(t)=sqrt((M-exp(-2(M-1)(T-t)))/(M-exp(-2(M-1)T))).

For M=1, C(r)=1+2r, so

lambda_T(t)=sqrt((1+2(T-t))/(1+2T)).

For M<1, put a=1-M>0. Then C(r)=(1-M exp(-2ar))/a, and an antiderivative of 1/C(r) is (1/2)log(exp(2ar)-M). Hence

lambda_T(t)=sqrt((exp(2(1-M)(T-t))-M)/(exp(2(1-M)T)-M)).

Furthermore, C(r)<=1+2 integral_0^infinity exp(-2as)ds=1+1/a. Thus

integral_{T-t}^T du/C(u)>=a t/(1+a),

which proves lambda_T(t)<=exp(-(1-M)t/(2-M)). This includes M=0 and all negative M; no division by M is used. All denominators and radicands in their stated regimes are positive.

For the time-dependent case, fix c>1 and set

A=(2c+1)T^{2c}+2T^{2c+1},

H(r)=A-2(T-r)^{2c+1}.

Evaluating (C) for r<T gives

C(r)=(T/(T-r))^{2c}
 +2 integral_0^r ((T-s)/(T-r))^{2c}ds
 =H(r)/[(2c+1)(T-r)^{2c}].

Since H'(r)=2(2c+1)(T-r)^{2c}, we have

1/C(r)=(1/2)H'(r)/H(r).

The reciprocal tends to zero as r increases to T, and H stays positive. Therefore

Lambda(r)=sqrt(H(r)/H(T)),

lambda_T(t)=sqrt(1-2t^{2c+1}/[(2c+1)T^{2c}+2T^{2c+1}]).

This is the claimed weight. At t=0 all weights equal 1; their values at t=T are positive. The singular one-sided bound is only needed for forward times t>0, and no score value or logarithm at an exceptional t=0 point is needed for the integral.

## Source-Repair Accounting

The public density normalization repairs a formalization error, not the source. The inherited integrability assumption is explicitly corrected for its time index and scalar drift magnitude. The generic upstream alpha denominator is corrected from alpha(t) to alpha(T-t), with no effect on alpha=1/2. The source's propagation interpolation is corrected for gradients, generator index, pointwise averaging, and the initial multiplier. The constant-case integral prefactors and the singular-case reciprocal-C exponent are corrected as recorded in the material records. These are local corrections that leave the flagship statement and proof architecture unchanged.

No unresolved proof obligation remains.
