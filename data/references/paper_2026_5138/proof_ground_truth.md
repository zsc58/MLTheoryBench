# Reference Proof

## Proof Structure and Obligations

The factors and learned field are fixed. This is a population statement about complete matrices, not a finite-sample or missing-observation guarantee. The obligations are: establish finite moments and well-defined invertible flows; justify the weighted chi-square evolution; obtain the terminal divergence bound and transfer it to generated cores; apply the Gaussian transport inequality with verified hypotheses; and lift a core coupling while controlling geometry and noise. All these obligations are closed below.

The proof uses only the expected oracle-core bound. It does not assume a pointwise bound on `S0`, and it does not assume that a Lipschitz flow is an everywhere `C1` diffeomorphism.

## 1. Moments, Marginal Velocity, and Flows

Put `k=min(m,n)`. The assumptions give

`E||E||_F^2 <= k E||E||_2^2 <= k tau^2`,

and therefore

`E||X||_F^2 <= 2r C_S^2 + 2k tau^2 < infinity`.

Encoding is a contraction, so `M_c=E||c||^2` is finite. Set `D=sqrt(M_c+d)`. Independence and the zero mean of `z` give `E||z-c||^2=D^2`. Also, `E||Y_t||^2 <= D^2`.

For any compactly supported continuously differentiable test function `psi`, differentiation under the expectation is justified by `E||z-c||<infinity`, and

`d/dt E[psi(Y_t)] = E[grad psi(Y_t) dot (z-c)] = integral grad psi(x) dot v(x,t) rho_t(x) dx`.

This proves the target continuity equation, with the prescribed endpoints. Conditional Jensen gives

`integral ||v(x,t)||^2 rho_t(x) dx <= D^2`.

For completeness, the conditional-to-marginal regression assertion is the elementary conditional-expectation identity

`E||w(Y_t)-(z-c)||^2 = E||w(Y_t)-v(Y_t,t)||^2 + E||v(Y_t,t)-(z-c)||^2`

whenever the terms are finite. Thus no specialized external flow-matching theorem is needed to close this obligation.

Define `e(t)^2=integral ||v-vhat||^2 rho_t dx`. Spatial Lipschitz continuity and averaging against `rho_t` yield

`||v(0,t)|| <= (1+L_v)D`,

`||vhat(0,t)|| <= e(t)+(1+L_v)D`.

Since `integral_0^1 e(t)^2 dt <= epsilon^2`, both values at the origin are integrable in time. Consequently, each field has an integrable-in-time linear-growth bound.

We use the standard ODE fact that a Borel field with a uniform global spatial Lipschitz constant and an integrable value at the origin has a unique global absolutely continuous flow on a finite time interval. Linear growth prevents finite-time escape. Gronwall applied to two trajectories gives the spatial Lipschitz estimate; applying the same argument backward gives the inverse estimate. In particular, `Phi_t` is a bi-Lipschitz bijection, and

`Lip(Phi_1^(-1)) <= exp(L_v)`.

These assertions require no everywhere differentiability of the flow. The learned density path is its pushforward by definition. Its continuity equation also follows by differentiating a test function along trajectories. Since the inverse flow has finite displacement at the origin and is Lipschitz, its pushforward of a Gaussian has finite second moment. Thus both core laws belong to `P_2(R^d)`.

## 2. A Justified Chi-Square Evolution Calculation

Write `rho=rho_t`, `hatrho=rhohat_t`, and

`j_t=rho_t^2/rhohat_t`,

`F(t)=integral (rho_t/rhohat_t-1)^2 rhohat_t dx = integral j_t dx - 1`.

The ratio assumption and Cauchy--Schwarz imply the useful integrability estimate

`integral (1+||x||) j_t(x) dx`

`= integral sqrt(rho_t) [(1+||x||)rho_t^(3/2)/rhohat_t] dx <= sqrt(C2)`.

In particular, `F(t)` is finite, and `F(0)=0`.

We first justify the local calculus. The common Gaussian upper bound gives a ball containing at least half the mass of either density, uniformly in time. Inside that ball each density has a point where it is bounded below by a fixed positive constant. Integrating the bound on its log-gradient along a line segment then gives a uniform positive lower bound on every fixed compact set. The score and density bounds also give locally bounded spatial derivatives. The continuity equations, the spatial Lipschitz bounds on the fields, and their integrable values at the origin imply locally integrable time derivatives of the densities. Thus product and quotient rules hold locally, using absolutely continuous representatives in time and almost-everywhere spatial derivatives. This avoids assuming extra classical smoothness.

A direct calculation from the two continuity equations gives

`partial_t j_t + div(j_t(2v-vhat))`

`= 2j_t (v-vhat) dot (grad log rho_t-grad log rhohat_t)`.

Choose smooth cutoffs `eta_R`, equal to one on the ball of radius `R`, supported on the ball of radius `2R`, with `0<=eta_R<=1` and `||grad eta_R||<=K/R`. Integrating the local identity against `eta_R` and over time gives

`integral eta_R j_1 dx - integral eta_R j_0 dx`

`= 2 integral_0^1 integral eta_R j_t (v-vhat) dot (grad log rho_t-grad log rhohat_t) dx dt`

`  + integral_0^1 integral j_t(2v-vhat) dot grad eta_R dx dt`.

Set `b(t)=2||v(0,t)||+||vhat(0,t)||`, which is integrable. The spatial Lipschitz estimates give

`||2v(x,t)-vhat(x,t)|| <= b(t)+3L_v||x||`.

Consequently, the absolute value of the cutoff boundary term is at most

`(K/R) sqrt(C2) integral_0^1 [b(t)+3L_v] dt`,

which tends to zero. This is the needed boundary justification: upper bounds on the individual densities alone do not control reciprocal-density factors.

The main integrand is absolutely integrable. Indeed, the score difference is at most `2L(1+||x||)`, and Cauchy--Schwarz gives

`2 integral_0^1 integral ||v-vhat|| j_t ||grad log rho_t-grad log rhohat_t|| dx dt`

`<= 2 [integral_0^1 integral ||v-vhat||^2 rho_t dx dt]^(1/2)`

`   * [integral_0^1 integral ||grad log rho_t-grad log rhohat_t||^2 rho_t^3/rhohat_t^2 dx dt]^(1/2)`

`<= 4L sqrt(C2) epsilon`.

Passing to the limit in the cutoff identity therefore proves

`F(1) = 2 integral_0^1 integral (v-vhat) dot [rho_t^2/rhohat_t] (grad log rho_t-grad log rhohat_t) dx dt`,

and hence

`F(1) <= 4L sqrt(C2) epsilon`.                                      (1)

## 3. Terminal and Generated-Core Divergences

Use `q(x)=(2pi)^(-d/2) exp(-||x||^2/2)` for the Gaussian density. At time one, `rho_1=q`. Put `a=C1(2pi)^(d/2)` and `f=rhohat_1/q`. The Gaussian upper bound gives `0<f<=a`. Therefore

`chi2(rhohat_1||q) = integral q(f-1)^2 dx`

`<= a integral q(f-1)^2/f dx = a chi2(q||rhohat_1) = a F(1)`.

Together with (1), this yields

`chi2(rhohat_1||q) <= C_F epsilon`.                                 (2)

Here and below, for `P` absolutely continuous with respect to `Q`,

`chi2(P||Q)=integral (dP/dQ-1)^2 dQ`.

Let `T=Phi_1`. By construction,

`T_# p_C = rhohat_1(x) dx`,  `T_# p_hatC = q`.

For a measurable bijection with measurable inverse, the Radon--Nikodym derivative transforms as

`d(T_#P)/d(T_#Q) = (dP/dQ) composed with T^(-1)`.

This follows by integrating either side against an arbitrary bounded measurable test function and using the pushforward definition. Absolute continuity in the terminal space implies absolute continuity in the initial space by the same bijection. Substitution in the divergence definition proves invariance without any Jacobian calculation. Applying it here gives

`chi2(p_C||p_hatC) = chi2(rhohat_1||q) <= C_F epsilon`.                (3)

## 4. Transport from Core Divergence to Core Wasserstein Distance

The standard independent Gaussian transport inequality used here has the precise form

`W_2^2(nu,q) <= 2 KL(nu||q)`

for a probability measure `nu` absolutely continuous with respect to the standard Gaussian `q`, with finite relative entropy. For a measure with density ratio `h` relative to its reference law, `log h<=h-1` gives

`KL(P||Q) <= integral h(h-1) dQ = chi2(P||Q)`.

Thus (3) supplies finite relative entropy. The Gaussian inequality applies in dimension `d`, and all measures used here have finite second moments, as already checked.

To verify the claimed transport-inequality transfer explicitly, let `g=T^(-1)` and let `mu` be absolutely continuous with respect to `p_hatC=g_#q`. Set `nu=T_#mu`. Invariance of relative entropy under this bijection follows from the same Radon--Nikodym identity as above. Pushing any coupling of `nu,q` through `g` in both coordinates shows

`W_2^2(mu,p_hatC) <= Lip(g)^2 W_2^2(nu,q)`

`<= 2 exp(2L_v) KL(nu||q) = 2 exp(2L_v) KL(mu||p_hatC)`.

This is exactly the needed `T2(exp(2L_v))` inequality. Apply it to `mu=p_C` and use (3) to obtain

`W_2(p_C,p_hatC) <= exp(L_v) sqrt(2 C_F epsilon)`.                    (4)

## 5. Lift the Coupling and Bound Geometry and Noise

Write `P_A=AA^T` and `P_B=BB^T`. Because the core laws have finite second moments on Euclidean space, an optimal quadratic-cost coupling exists. Let `pi(dc,dchat)` be such a coupling and disintegrate it as `p_C(dc)K(c,dchat)`. Euclidean spaces admit regular conditional probability kernels. Sample the original `(S0,E,X)`, form `c=vec(A^T X B)`, and then sample `chat` from `K(c,.)`. This preserves the original model and the optimal core coupling simultaneously.

Put `Chat=mat(chat)` and `Xhat=A Chat B^T`. Then `(X,Xhat)` is a valid coupling of the required ambient laws, and

`E||C-Chat||_F^2 = W_2^2(p_C,p_hatC)`.

Since `C=A^T X B`,

`X-Xhat = Delta_sub + Delta_core + Delta_noise`,

where

`Delta_sub = A0 S0 B0^T - P_A A0 S0 B0^T P_B`,

`Delta_core = A(C-Chat)B^T`,

`Delta_noise = E-P_A E P_B`.

For the low-rank part,

`Delta_sub = (I-P_A)A0 S0 B0^T + P_A A0 S0 B0^T(I-P_B)`.

For equal-dimensional orthonormal-column factors, the squared residual norm is

`||(I-P_A)A0||_2^2 = 1-sigma_min(A^T A0)^2 = delta_A^2`,

and the corresponding identity holds for `B,B0`. Mixed Frobenius/spectral submultiplicativity therefore gives

`||Delta_sub||_F <= (delta_A+delta_B)||S0||_F`.

Taking its L2 norm and using only the stated moment assumption gives

`[E||Delta_sub||_F^2]^(1/2) <= sqrt(r) C_S(delta_A+delta_B)`.          (5)

The map `H -> P_A H P_B` is self-adjoint and idempotent in the Frobenius inner product, hence is an orthogonal projection. Thus

`||Delta_noise||_F <= ||E||_F`,

and the singular-value norm comparison gives

`[E||Delta_noise||_F^2]^(1/2) <= sqrt(k) tau`.                        (6)

Finally, orthonormality of `A,B` and the definition of vectorization give

`||A(C-Chat)B^T||_F = ||C-Chat||_F = ||c-chat||`.

Consequently, the L2 norm of `Delta_core` is the left side of (4). Minkowski's inequality, (4), (5), and (6) now imply

`[E||X-Xhat||_F^2]^(1/2)`

`<= sqrt(r) C_S(delta_A+delta_B) + exp(L_v)sqrt(2 C_F epsilon) + sqrt(min(m,n))tau`.

The Wasserstein distance is bounded by the cost of this coupling, proving the desired inequality.

## Boundary and Dependency Checks

The proof allows `tau=0`, full-rank factors, zero principal-angle errors, and maximal principal angles whenever the stated density assumptions also hold. Nondegeneracy excludes `C_S=0` for an admissible instance. The public flow-bound constants retain the source's strictly positive domains; an exactly matched field still satisfies the theorem with every positive error tolerance. No finite-sample, missing-data, pointwise oracle-core, or extra differentiability assumption is used. The conditional-mean-zero and positive-definite-moment assumptions are retained from the source even though the final error estimate does not need every part of them. All private proof obligations are closed.
