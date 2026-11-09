# Reference Proof

## Contract and proof obligations

The sensitivity bound s and inner approximation tolerance delta are independent. All gradient updates use the exact expectation under the specified law P_hat(theta). The stable point is for the Lagrangian surrogate: the law is frozen during minimization, but lambda remains a function of the candidate parameter. No identification with the original fixed ambiguity-set problem is needed.

We prove: (1) well-defined objectives and gradients; (2) the five phi gradient bounds; (3) maximizer sensitivity and envelope regularity; (4) envelope strong convexity; (5) strong monotonicity and Lipschitz continuity of the exact expected gradient; (6) contraction and existence and identification of its fixed point; and (7) the approximation-error recurrence. The singleton parameter-domain case is treated separately.

## 1. Well-definedness and the singleton case

Continuity and compactness of Xi imply that the maximum defining f is finite and attained. Strong concavity with mu>0 gives uniqueness of its maximizer. For each fixed theta, the gradients of phi are bounded on Xi x Xi. Thus the expectation defining G exists: its integrand is measurable and bounded. The same observations apply to the exact gradients below. Compact support also gives finite first moments for all Wasserstein comparisons.

If Theta={theta_0}, projection always returns theta_0. This point is the unique feasible minimizer of every frozen objective, so theta_t=theta_s=theta_0 for all t, for any eta>0. No square-root rate or division by beta is needed. Henceforth Theta contains two distinct points.

## 2. Gradient bounds for phi

Write c(xi,zeta)=||xi-zeta||^2. Then

nabla_theta phi = nabla_theta l - nabla lambda(theta)c(xi,zeta),

nabla_zeta phi = nabla_zeta l - 2lambda(theta)(zeta-xi).

The diameter gives c<=D_xi^2. Difference of squares gives

|c(xi,zeta)-c(xi',zeta)|
= |<xi-xi',xi+xi'-2zeta>|
<=2D_xi||xi-xi'||,

and, by the same identity,

|c(xi,zeta)-c(xi,zeta')|<=2D_xi||zeta-zeta'||.

Integration of the bounded gradient of lambda along a parameter segment gives |lambda(theta)-lambda(theta')|<=L_lambda||theta-theta'||. Substitution in the displayed derivatives yields, respectively,

L^phi_{theta theta}=L_{theta theta}+H_lambda D_xi^2,
L^phi_{theta xi}=2L_lambda D_xi,
L^phi_{theta zeta}=L_{theta zeta}+2L_lambda D_xi,
L^phi_{zeta theta}=L_{zeta theta}+2L_lambda D_xi,
L^phi_{zeta xi}=2lambda_max.

For example, variation of nabla_zeta phi in theta is bounded by [L_{zeta theta}+2L_lambda||zeta-xi||]||theta-theta'||, and variation in xi is exactly bounded by 2lambda(theta)||xi-xi'||. No Lipschitz bound on nabla_zeta l in zeta is used.

## 3. Maximizer sensitivity and envelope regularity

Let p=(theta,xi), p'=(theta',xi'), a=zeta*(p), b=zeta*(p'), and v=b-a. Constrained maximizer optimality gives

<nabla_zeta phi(p,a),v><=0,
<nabla_zeta phi(p',b),v>>=0.

Strong concavity at p' gives

<nabla_zeta phi(p',a)-nabla_zeta phi(p',b),v>>=mu||v||^2.

Combining these inequalities yields

mu||v||^2
<=<nabla_zeta phi(p',a)-nabla_zeta phi(p,a),v>
<=[L^phi_{zeta theta}||theta-theta'||+L^phi_{zeta xi}||xi-xi'||]||v||.

If v=0 the desired bound is immediate; otherwise divide by ||v||. Therefore

||zeta*(theta,xi)-zeta*(theta',xi')||
<= (L^phi_{zeta theta}/mu)||theta-theta'||
 + (L^phi_{zeta xi}/mu)||xi-xi'||.

In particular the maximizer is continuous and measurable. The standard compact-domain, unique-maximizer form of Danskin's theorem states that a continuously differentiable objective with a unique maximizer over a fixed compact set has parameter derivative equal to the objective's parameter derivative at that maximizer. Compactness, continuity of phi and its parameter derivative, and uniqueness have all been verified. Thus

u(theta,xi):=nabla_theta f(theta,xi)
=nabla_theta phi(theta,xi,zeta*(theta,xi)).

On boundary points these derivatives have their usual feasible-direction interpretation. Splitting differences in this identity and using the bounds just proved gives

||u(theta,xi)-u(theta',xi')||
<=L^f_{theta theta}||theta-theta'||+L^f_{theta xi}||xi-xi'||,

where

L^f_{theta theta}=L^phi_{theta theta}+L^phi_{theta zeta}L^phi_{zeta theta}/mu,
L^f_{theta xi}=L^phi_{theta xi}+L^phi_{theta zeta}L^phi_{zeta xi}/mu.

## 4. Strong convexity of the envelope and frozen objectives

Put d=theta'-theta. The H_lambda-Lipschitz gradient gives

|lambda(theta')-lambda(theta)-<nabla lambda(theta),d>|
<=H_lambda||d||^2/2.

Combining this with m-strong convexity of l and c<=D_xi^2 gives, for fixed xi,zeta,

phi(theta',xi,zeta)
>=phi(theta,xi,zeta)+<nabla_theta phi(theta,xi,zeta),d>
 +(gamma/2)||d||^2.

Take zeta=zeta*(theta,xi) and bound f(theta',xi) below by phi(theta',xi,zeta). The envelope identity then yields

f(theta',xi)>=f(theta,xi)+<u(theta,xi),d>+(gamma/2)||d||^2.

Adding the versions with theta and theta' interchanged proves

<u(theta,xi)-u(theta',xi),theta-theta'>=gamma||theta-theta'||^2.

For a fixed probability law Q on Xi, let H_Q(x)=E_Q f(x,xi). This is finite and gamma-strongly convex. On any bounded parameter segment, u is uniformly bounded over xi by its established Lipschitz bounds and compactness. Integration along the segment therefore justifies differentiation under the expectation, giving nabla H_Q(x)=E_Q u(x,xi).

## 5. Exact expected-gradient bounds

Define F(theta)=E_{P_hat(theta)}u(theta,xi). This is not a derivative through the distribution map.

For any K-Lipschitz vector-valued function h on Xi and any coupling pi of probability laws P,Q,

||E_P h-E_Q h||
=||E_pi[h(xi)-h(xi')]||
<=K E_pi||xi-xi'||.

Taking the infimum over couplings gives ||E_P h-E_Q h||<=K W_1(P,Q), also when K=0. This directly proves the vector-valued consequence of the source's Kantorovich-Rubinstein estimate without an additional vector duality assumption.

For d=theta-theta', decompose

F(theta)-F(theta')=A+B,

A=E_{P_hat(theta)}[u(theta,xi)-u(theta',xi)],
B=E_{P_hat(theta)}u(theta',xi)-E_{P_hat(theta')}u(theta',xi).

The preceding results give

<A,d>>=gamma||d||^2,
||A||<=L^f_{theta theta}||d||,
||B||<=s L^f_{theta xi}||d||.

Consequently, with alpha=gamma-s L^f_{theta xi}>0,

<F(theta)-F(theta'),d>>=alpha||d||^2,
||F(theta)-F(theta')||<=beta||d||,

where beta=L^f_{theta theta}+s L^f_{theta xi}. These estimates require no differentiation or extra information about P_hat.

## 6. Projected contraction and the stable point

Because Theta has distinct points, applying Cauchy-Schwarz to the two preceding bounds for such a pair gives 0<alpha<=beta. In particular the step-size denominator is positive, and

1-2eta alpha+eta^2 beta^2
=(1-eta alpha)^2+eta^2(beta^2-alpha^2)>=0.

The step-size condition makes this expression strictly less than one. Thus the stated kappa_gd is real and lies in [0,1).

For completeness, projection onto a nonempty closed convex Euclidean set exists and is unique: squared distance is continuous and coercive, and strictly convex on the convex set. Its minimizer p=Proj_Theta(y) is characterized by <y-p,x-p><=0 for every x in Theta. Applying this inequality to two projections and adding yields ||p-p'||^2<=<p-p',y-y'>, hence projection is nonexpansive.

Let T(theta)=Proj_Theta(theta-eta F(theta)). Nonexpansiveness and expansion of the squared norm give

||T(theta)-T(theta')||^2
<=||d-eta(F(theta)-F(theta'))||^2
<= [1-2eta alpha+eta^2 beta^2]||d||^2
=kappa_gd^2||d||^2.

This is an inequality for projected updates, not an equality with their unprojected differences.

To obtain a fixed point explicitly, start x_0 in Theta and set x_{n+1}=T(x_n). Consecutive distances are at most kappa_gd^n||x_1-x_0||, so their geometric tail sum makes (x_n) Cauchy. Closedness of Theta gives a limit theta_s in Theta. Continuity of T gives T(theta_s)=theta_s. Two fixed points would have distance at most kappa_gd times that same distance, so the fixed point is unique. The argument includes kappa_gd=0.

The projection characterization gives

T(theta_s)=theta_s
if and only if <F(theta_s),x-theta_s>>=0 for every x in Theta.

For the frozen law Q=P_hat(theta_s), F(theta_s)=nabla H_Q(theta_s). Convexity makes this variational inequality equivalent to minimizing H_Q; strong convexity makes that minimizer unique. Conversely, every surrogate stable point satisfies this variational inequality and hence is a fixed point of T. Therefore theta_s is precisely the unique stable point required by the task.

## 7. Approximation error and the finite-time bound

Feasibility and the uniform inner-error bound imply

||G(theta)-F(theta)||
<=E_{P_hat(theta)}||nabla_theta phi(theta,xi,z(theta,xi))
 -nabla_theta phi(theta,xi,zeta*(theta,xi))||
<=L^phi_{theta zeta}delta.

Projection nonexpansiveness and T(theta_s)=theta_s now give

||theta_{t+1}-theta_s||
<=kappa_gd||theta_t-theta_s||+eta L^phi_{theta zeta}delta.

Induction, with an empty sum when t=0, gives

||theta_t-theta_s||
<=kappa_gd^t||theta_0-theta_s||
 +eta L^phi_{theta zeta}delta sum_{j=0}^{t-1}kappa_gd^j
=kappa_gd^t||theta_0-theta_s||
 +[eta L^phi_{theta zeta}delta/(1-kappa_gd)](1-kappa_gd^t).

The convention kappa_gd^0=1 includes kappa_gd=0. The bound implies the claimed limiting radius, not convergence to a particular point when delta>0. When delta=0, it gives linear convergence to theta_s for every allowed sensitivity s, including nonzero sensitivity.

All theorem-critical obligations are closed. The source's Wasserstein Lagrangian identity explains the surrogate's origin but is not needed to prove this theorem about the explicitly defined f.
