# Reference Proof

## Contract and obligations

Convergence in the measure space means narrow convergence plus convergence of second moments, equivalently convergence in W_2. The functional is bounded below and Wasserstein differentiable at every measure in the finite-expansion sense specified in the problem. In particular its initial value is finite. The existence argument must work for every real lambda; ordinary convexity must not be silently assumed when lambda is negative.

The theorem-critical obligations are: closedness of the convex-gradient constraint; differentiability and lower semicontinuity of the unconstrained lift; identification of the constrained subdifferential; applicability of the Hilbert existence theorem including initial-time H^1 regularity; energy dissipation for any projected solution; endpoint comparison; the polynomial gap and map bounds; strong map convergence under the stated measure topology; and the exponential bounds. Each is closed below.

## 1. Geometry and transport-map stability

Write H=L^2_{rho_0} and K for the constraint. Convex combinations of convex potentials show that K is convex. Brenier's theorem applies because rho_0 is absolutely continuous and both source and target have finite second moments. It identifies K bijectively with P_2 under pushforward, and gives

    ||id-B_mu||_H^2 = W_2(rho_0,mu)^2.

For arbitrary S,T in H, the coupling (S,T)_#rho_0 yields

    W_2(S_#rho_0,T_#rho_0) <= ||S-T||_H.

Suppose T_n in K converges strongly to T in H. Put mu_n=T_{n#}rho_0 and mu=T_#rho_0. Then W_2(mu_n,mu) tends to zero. The graph plans (id,T_n)_#rho_0 converge narrowly to (id,T)_#rho_0. Their costs converge to ||id-T||_H^2 by strong H convergence, and also to W_2(rho_0,mu)^2 because they are optimal and W_2(rho_0,mu_n) tends to W_2(rho_0,mu). Thus the limiting graph plan is optimal. Brenier uniqueness gives T=B_mu, proving closedness.

We will also need the following stability consequence, whose proof is included rather than inferred from uniqueness alone. If W_2(mu_n,mu) tends to zero, then B_{mu_n} tends strongly in H to B_mu. Indeed, the optimal graph plans q_n=(id,B_{mu_n})_#rho_0 are tight. Every narrowly converging subsequence has a limit q with marginals rho_0 and mu. Lower semicontinuity of quadratic cost gives

    cost(q) <= liminf cost(q_n) = W_2(rho_0,mu)^2.

Since q is a coupling of these marginals, it is optimal. Brenier uniqueness identifies q=(id,B_mu)_#rho_0. All subsequential limits are therefore this graph plan, so the whole sequence converges to it. Convergence to a deterministic graph with fixed first marginal implies B_{mu_n}->B_mu in rho_0-probability: on a compact set of arbitrarily large rho_0-measure where B_mu is continuous, extend its restriction continuously and apply convergence of the graph plans to the bounded function min(1,|y-B_mu(x)|), using that extension. The exceptional set has arbitrarily small measure.

Moreover ||B_{mu_n}||_H^2 is the second moment of mu_n and converges to ||B_mu||_H^2. Probability convergence and boundedness in H imply weak H convergence: they imply L^1 convergence, hence convergence against bounded test fields, and approximation of any H test field by bounded ones finishes the argument. Weak convergence together with convergence of norms gives strong H convergence. This explicitly uses convergence of second moments.

## 2. The unconstrained lift

Define F(T)=D(T_#rho_0) for every T in H. Define separately

    Phi = F + I_K.

The pushforward inequality and the assumed lower semicontinuity of D imply strong lower semicontinuity of F. Since K is closed, Phi is strongly lower semicontinuous. The segment inequality in the problem is exactly lambda-convexity of Phi. The lower bound on D transfers to Phi; Phi is proper and Phi(id)=D(rho_0) is finite.

Here is the forward differentiability argument needed from the source's cited lifting lemma. Fix T, let mu=T_#rho_0, and write g=g_mu. For S approaching T set nu=S_#rho_0, delta=||S-T||_H, q=(T,S)_#rho_0, and choose an optimal coupling pi of mu and nu. Given epsilon>0, choose a smooth compactly supported potential psi such that ||g-grad psi||_{L^2_mu}<epsilon; this is possible by the stipulated tangent-space membership of g.

Taylor's formula gives, for either coupling r=q or r=pi,

    integral grad psi(x)·(y-x) dr
      = integral psi dnu - integral psi dmu + R_r,

where |R_r| <= (1/2)||D^2 psi||_infinity integral |y-x|^2 dr. Cauchy--Schwarz bounds the error from replacing g by grad psi by epsilon times the root-mean-square displacement. The displacement of q is delta and that of pi is W_2(mu,nu)<=delta. Therefore

    | integral g(x)·(y-x) dq - integral g(x)·(y-x) dpi |
      <= 2 epsilon delta + ||D^2 psi||_infinity delta^2.

First letting delta tend to zero and then epsilon tend to zero shows that this difference is o(delta). The Wasserstein differentiability expansion for pi has remainder o(W_2(mu,nu)), hence o(delta). Consequently

    F(S)-F(T) = <g_{T_#rho_0} composed T,S-T>_H + o(||S-T||_H).

Thus F is Frechet differentiable on H, with gradient a(T)=g_{T_#rho_0} composed T. In particular F is continuous. The case nu=mu causes no difficulty: the optimal displacement and its contribution vanish.

## 3. Constrained subdifferential and existence

Let N_K(T)={n:<n,S-T>_H<=0 for all S in K}. The differentiability expansion and the definition of the Frechet subdifferential give

    partial Phi(T) = a(T)+N_K(T).

For completeness, subtract the expansion of F from the subgradient inequality. The remaining local supporting inequality for I_K is equivalent to membership in N_K(T): test along the segment T+s(S-T) and let s decrease to zero. Conversely a normal vector gives the required local inequality immediately.

Put C=Tan_T K and v=-a(T). If p=proj_C(v), the projection characterization, tested at 0 and 2p, gives <v-p,p>=0. It also gives <v-p,z><=0 for every z in C, so n=v-p belongs to N_K(T). For any m in N_K(T),

    ||v-m||^2 = ||p+(n-m)||^2 >= ||p||^2,

because <p,n>=0 and <p,m><=0. Hence the least-norm element of a(T)+N_K(T) is -p. This proves the projected-vector-field identity directly.

The standard-independent Hilbert theorem used here is: a proper, strongly lower-semicontinuous, bounded-below lambda-convex functional on a Hilbert space, initialized at a point of its effective domain, generates a unique global subgradient flow u in H^1 on every finite interval. Its velocity is minus the least-norm subgradient a.e. Implicit Euler resolvents converge to this flow. The energy identity holds, and subgradient monotonicity gives ||u(t)-v(t)||<=e^{-lambda t}||u(0)-v(0)||. Its chain rule applies to an H^1 curve and an L^2 subgradient selection.

All these hypotheses have been checked for Phi with u_0=id. To check the proximal construction explicitly, for tau^{-1}+lambda>0 minimize

    Phi(S)+(1/(2tau))||S-S_k||_H^2.

This objective is strongly convex and strongly lower semicontinuous, hence weakly lower semicontinuous. It is coercive because Phi is bounded below. A bounded minimizing sequence has a weakly convergent subsequence, and the direct method gives its unique minimizer. This argument does not assert weak lower semicontinuity of F when lambda<0.

The Hilbert theorem now gives a global curve with H^1 regularity on every finite interval. The minimum-subgradient identity above identifies its velocity with the projected equation in the problem. Restriction proves the finite-horizon assertion. The uniqueness estimate makes restrictions on different horizons compatible.

For any other H^1 solution of the projected equation, the same projection calculation gives -dot T in partial Phi(T) a.e. Thus the Hilbert chain rule applies with the L^2 selection -dot T. Endpoint energy values agree with the chain-rule representative because F and T are continuous. This also shows uniqueness among the stated projected solutions.

## 4. Projection comparison and dissipation

For a solution write mu_t=T_{t#}rho_0, v_t=-a(T_t), and w_t=dot T_t. Projection onto the tangent cone gives

    <v_t,w_t>_H = ||w_t||_H^2,
    <v_t-w_t,S-T_t>_H <= 0       for every S in K.

The first follows by testing at 0 and 2w_t. For the second, S-T_t is a tangent direction and the residual v_t-w_t is normal. The energy chain rule gives

    d/dt D(mu_t) = -||w_t||_H^2

for almost every t, with an absolutely continuous energy on every finite interval. Therefore the energy is nonincreasing, even without a minimizer assumption.

Now assume the convergence hypotheses and put E_t=F(T_t)-F(T_*)>=0. Differentiating the endpoint segment inequality at s=0 gives

    E_t+(kappa/2)||T_t-T_*||_H^2
      <= <v_t,T_*-T_t>_H
      <= <w_t,T_*-T_t>_H.

The last relation is an inequality, not an equality. This is the corrected comparison used in both regimes.

## 5. Zero endpoint convexity

Let Y_t=(1/2)||T_t-T_*||_H^2. With kappa=0 the comparison gives Y'_t<=-E_t a.e. Hence, for t>0,

    t E_t <= integral_0^t E_s ds <= Y_0-Y_t <= Y_0.

The first inequality uses monotonicity of E. Since Y_0=(1/2)W_2(rho_0,mu_*)^2, the required gap estimate follows. No metrizability or power-growth assumption was used.

If D metrizes convergence to its minimizer in the specified P_2 topology, E_t->0 implies W_2(mu_t,mu_*)->0. Apply the stability result of Section 1 along every sequence of times tending to infinity. Since T_t=B_{mu_t}, this proves T_t->T_* strongly in H.

If the power-growth condition holds along the selected flow, its constants c and alpha are independent of time, and for almost every positive t,

    ||T_t-T_*||_H^2 <= c E_t^alpha
      <= c 2^{-alpha} t^{-alpha} W_2(rho_0,mu_*)^{2alpha}.

Continuity of the map curve and energy extends this inequality to every t>0. This estimate itself gives strong convergence and does not require a separate metrizability assumption.

## 6. Positive endpoint convexity

The comparison and Young's inequality give

    E_t <= <w_t,T_*-T_t>_H-(kappa/2)||T_t-T_*||_H^2
        <= ||w_t||_H^2/(2kappa).

Together with E'_t=-||w_t||_H^2 this implies E'_t<=-2kappa E_t a.e. Gronwall's inequality and continuity yield

    E_t <= e^{-2kappa t} E_0       for every t>=0.

Apply endpoint convexity at s=1/2. Minimality of T_* gives

    0 <= F((T_t+T_*)/2)-F(T_*)
      <= (1/2)E_t-(kappa/8)||T_t-T_*||_H^2.

Thus ||T_t-T_*||_H^2 <= (4/kappa)E_t, and substitution of the exponential gap bound proves the claimed map estimate. This step needs only endpoint convexity and minimality, not an extra projection argument.

All estimates include the degenerate case rho_0=mu_*: the initial gap and distance are then zero and the flow is stationary. The reciprocal-time estimates are asserted only for t>0. No theorem-critical proof obligation remains unresolved.
