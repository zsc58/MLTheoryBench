# Reference Proof

## Audit status and obligations

This proof establishes all theorem-critical obligations: (1) tails and moments from the initial assumptions; (2) correctly scaled score identities and propagated dissipativity; (3) conditional reverse moments and score/Jacobian growth; (4) bounded-ball minorization and a single contracting weighted-TV metric for the finite grid; (5) initialization control in both regimes with the corrected metric normalization; (6) the conditional local KL and weighted-TV error estimates, including the data-time endpoint; and (7) moment integration and telescoping. No obligation is closed merely by a paper-specific citation.

The source-local repairs used here are recorded in provenance. In particular, the unweighted term of rho_b is twice TV, so the mixing prefactor begins with sqrt(2).

## 1. Initial tails, moments, and growth

Because the classical score is defined everywhere, p_0 is strictly positive. For a unit vector omega and r>=1, the initial dissipativity inequality gives

    d/dr log p_0(r omega) <= -gamma_0 r + kappa_0/r.

Integration yields

    p_0(r omega) <= max_{||z||=1}p_0(z) exp[-gamma_0(r^2-1)/2] r^{kappa_0}.

Thus p_0 is bounded and has exponential moments E exp(lambda||X_0||^2)<infinity for lambda<gamma_0/2. This argument does not infer convexity from radial dissipativity.

The Jacobian bound gives

    ||S_0(x)|| <= ||S_0(0)|| + C_0||x|| + C_0||x||^{p+1}/(p+1).

The value at zero can itself be bounded by the displayed parameters: if S_0(0) is nonzero, take a unit vector e in its direction, use <S_0(e),e><=-gamma_0+kappa_0 and ||S_0(e)-S_0(0)||<=2C_0. In particular ||S_0(0)||<=kappa_0+2C_0. Hence, for finite constants A_0,B_0 depending only on the stated parameters,

    ||S_0(x)|| <= A_0(1+||x||^{p+1}),
    ||nabla S_0(x)+S_0(x)S_0(x)^T||_F <= B_0(1+||x||^{2p+2}).

The tail bound and these polynomial bounds justify integration by parts, using cutoffs if necessary. Integrating div(x||x||^{ell-2}p_0) gives, for ell>=2,

    gamma_0 E||X_0||^ell <= (kappa_0+d+ell-2)E||X_0||^{ell-2}.

Consequently the moments needed below have bounds in terms of the displayed parameters. The same is true of forward moments on [0,T] by the Gaussian representation.

## 2. Gaussian identities and propagated dissipativity

Put A(t)=int_0^t beta_u du,

    m_t=exp(-alpha A(t)),
    v_t=2A(t)                     if alpha=0,
    v_t=(1-m_t^2)/alpha           if alpha>0.

Solving the linear SDE gives X_t=m_t X_0+sqrt(v_t)G in distribution, with independent standard Gaussian G. For v_t>0, Gaussian differentiation and integration by parts give

    S_t(x)=-(x-m_t E[X_0|X_t=x])/v_t
          =m_t^{-1}E[S_0(X_0)|X_t=x],

    nabla S_t(x)+S_t(x)S_t(x)^T
      =m_t^{-2}E[nabla S_0(X_0)+S_0(X_0)S_0(X_0)^T|X_t=x],

    nabla S_t(x)=m_t^2 Cov(X_0|X_t=x)/v_t^2-I_d/v_t.

The last identity is for nabla S_t alone. Adding the score outer product to the left also requires adding it to the right. When v_t=0, use deterministic scaling rather than these divisions; here A(t)=0 and m_t=1.

For clarity, derive dissipativity first for Y=X_0+sqrt(v)G with density q and score S. Write D(x)=E[X_0|Y=x] and F(x)=<S(x),x>. The preceding identities imply

    F(x)=E[<S_0(X_0),X_0>|Y=x]-v Delta q(x)/q(x),
    E[||X_0||^2|Y=x]>=||x||^2+2vF(x),
    -v Delta q(x)/q(x)
      =d-Tr(Cov(X_0|Y=x))/v-v||S(x)||^2 <= d.

It follows that

    (1+2gamma_0 v)F(x)<=-gamma_0||x||^2+kappa_0+d.

Scaling back from X_0+sqrt(v_t/m_t^2)G gives

    <S_t(x),x><=-g_t||x||^2+h_t,
    g_t=gamma_0/(m_t^2+2gamma_0 v_t),
    h_t=(kappa_0+d)m_t^2/(m_t^2+2gamma_0 v_t).

Use g_0=gamma_0 and h_0=kappa_0+d; this is a continuous extension and preserves the original inequality. Both functions are continuous even if beta has jumps, because A is continuous. For alpha>0,

    2g_t-alpha=(2gamma_0-alpha)m_t^2/(m_t^2+2gamma_0 v_t)>0.

The analogous assertion is immediate for alpha=0. Therefore

    c=min_{0<=t<=T}(2g_t-alpha)>0,
    h=max_{0<=t<=T}h_t<infinity.

## 3. Conditional reverse moments and score growth

Let Z be the exact reverse process started from x at reverse time s. Its generator satisfies

    L_u V_ell(x)
      <= beta-bar_u[-ell c ||x||^ell
             +ell(2h+ell-2+d)||x||^{ell-2}].

For ell=2 choose c_2=2c and D_2=2(2h+d). For ell>2 choose c_ell=ell c/2 and

    D_ell=sup_{r>=0}{ell(2h+ell-2+d)r^{ell-2}-c_ell r^ell}<infinity.

Thus L_u V_ell<=beta-bar_u(-c_ell V_ell+D_ell). Apply the stopped Itô formula, then localization and Gronwall. With delta=int_s^t beta-bar_u du,

    Q_{t|s}V_ell(x)
      <= exp(-c_ell delta)||x||^ell
          +(D_ell/c_ell)(1-exp(-c_ell delta)).                 (1)

The localization is justified first by the quadratic bound, which prevents explosion, and then by the same estimates for higher moments. Coefficients containing beta need only be measurable and integrable; no continuity of beta or differentiable inverse clock is needed. Local spatial regularity follows from the positive C^2 initial density and Gaussian smoothing, including local convergence at zero noise.

The posterior law of X_0 given X_t=x is Q_{T|T-t}(x,dy). Apply (1) with ell=p+1 and ell=2p+2 to the conditional identities in Section 2. Since m_t is bounded away from zero on the finite horizon, this gives finite uniform constants A,B,C_H such that

    ||S_t(x)||<=A(1+||x||^{p+1}),
    ||nabla S_t(x)+S_t(x)S_t(x)^T||_F<=B(1+||x||^{2p+2}),
    ||nabla S_t(x)||_F<=C_H(1+||x||^{2p+2}).                 (2)

For the last inequality use the triangle inequality and ||vv^T||_F=||v||^2, enlarging C_H. These constants depend only on the displayed diffusion and initial-score parameters. At zero noise the original growth bounds apply directly.

## 4. Minorization and a common contracting metric

Fix a grid interval [s,t], put a=T-t and z=T-s, and let m=m_{z|a}, v=sigma_{z|a}^2. Positive integrated noise implies v>0. Bayes' formula gives

    Q_{t|s}(x,dy)=p_a(y)phi_v(x-my)dy/p_z(x).

Since p_z(x)<=sup phi_v=(2pi v)^(-d/2), for ||x||<=r and ||y||<=R,

    Q_{t|s}(x,dy)
      >= exp[-(r+mR)^2/(2v)] p_a(y)1_{B_R}(y)dy.

Choose R with p_a(B_R)>=1/2 and normalize the restricted measure. This yields a probability nu and epsilon in (0,1) with Q_{t|s}(x,A)>=epsilon nu(A) for all x in B_r. Forward second-moment bounds from Section 1 allow R to be bounded using the stated parameters. This proof covers a=0 and requires no nondegenerate bridge at that endpoint.

For each grid kernel K_k=Q_{t_k|t_{k-1}}, (1) gives K_k V_2<=lambda_k V_2+K_k^0 with lambda_k<1 and K_k^0>0. Set lambda=max_k lambda_k<1 and K=max_k K_k^0>0. Choose R_*>2K/(1-lambda). Minorization on {V_2<=R_*} gives constants epsilon_k; let epsilon=min_k epsilon_k>0. Choose

    0<b<epsilon/K.

Here is the weighted Harris argument with its hypotheses and common-weight choice made explicit. Define the cost

    d_b(x,y)=0 if x=y, and 2+bV_2(x)+bV_2(y) otherwise.

The optimal coupling cost for d_b equals rho_b: couple the common part of two measures identically and their mutually singular residuals arbitrarily. Conversely every coupling must pay at least the weighted mass of those residuals.

Write U=V_2(x)+V_2(y) for x!=y. If U>=R_*, any coupling yields the upper bound

    rho_b(K_k(x,.),K_k(y,.))<=2+b lambda U+2bK,

whose ratio to 2+bU is at most

    a_out=(2+b lambda R_*+2bK)/(2+bR_*)<1.

If U<=R_*, both points lie in the minorized ball. Couple the common epsilon nu_k component identically. The residual cost is at most

    2(1-epsilon)+b lambda U+2bK.

Its ratio to 2+bU is at most

    a_in=1-2(epsilon-bK)/(2+bR_*)<1.

Thus each kernel contracts the cost with factor at most a=max(a_in,a_out)<1. Coupling arbitrary input laws proves rho_b(mu K_k,nu K_k)<=a rho_b(mu,nu). Increase a within (0,1), if needed, and denote it by bar-alpha. The same b and bar-alpha work for the whole finite grid. Importantly b was chosen small, not enlarged. The construction is independent of the learned score and sampling randomness.

## 5. Initialization

For densities f,g, let M_4=E_f||X||^4+E_g||X||^4. In the metric convention of the task,

    rho_b(f,g)=2 TV(f,g)+b int ||x||^2|f-g|dx.

Pinsker gives 2TV<=sqrt(2 KL(f||g)). Also

    int ||x||^2|f-g|
      <= [int ||x||^4(sqrt(f)+sqrt(g))^2]^{1/2}
           [int(sqrt(f)-sqrt(g))^2]^{1/2}
      <= sqrt(2M_4) sqrt(KL(f||g)).

The last step uses the supplied Hellinger-versus-KL inequality. Consequently

    rho_b(f,g)<=[sqrt(2)+b sqrt(2M_4)]sqrt(KL(f||g)).          (3)

In VE, convexity of relative entropy and X_T=X_0+sqrt(2I_T)G give

    KL(p_T||pi_infty)
      <= E KL(N(X_0,2I_T I_d)||N(0,2I_T I_d))
      =E||X_0||^2/(4I_T).

For completeness, the VP entropy estimate is proved independently rather than delegated to the companion citation. Let gamma=N(0,alpha^{-1}I_d), L=Delta-alpha x·gradient, and P_r its Gaussian OU semigroup. For a smooth bounded density f relative to gamma bounded away from zero, Gaussian integration by parts gives

    d/dr Ent_gamma(P_r f)=-I_gamma(P_r f),

where Ent_gamma(f)=int f log f dgamma and I_gamma(f)=int ||gradient f||^2/f dgamma. The explicit Gaussian semigroup gives gradient P_r f=e^{-alpha r}P_r gradient f. Pointwise Cauchy-Schwarz, followed by invariance of gamma, yields

    I_gamma(P_r f)<=e^{-2alpha r}I_gamma(f).

The Gaussian representation shows P_r f tends to 1; boundedness permits dominated convergence of entropy. Integrating entropy dissipation to infinity therefore proves

    Ent_gamma(f)<=I_gamma(f)/(2alpha).

Apply this inequality to P_r f in the dissipation identity and use Gronwall:

    Ent_gamma(P_r f)<=e^{-2alpha r}Ent_gamma(f).

To extend this to finite-entropy densities, first truncate f above, add a positive constant, and normalize; these densities converge in L1 and entropy to f. OU smoothing supplies smooth approximants while preserving upper and positive lower bounds. The explicit semigroup is L1-continuous. Passing first through smoothing and then truncation uses entropy lower semicontinuity on the left and entropy convergence on the right. Hence the displayed decay holds for every finite-entropy initial law.

The forward SDE is this OU process at time r=I_T. Thus

    KL(p_T||pi_infty)<=e^{-2alpha I_T}KL(pi_0||pi_infty).

Apply (3) in either regime. The fourth moments are finite by Section 1 and the Gaussian reference. This proves

    rho_b(p_T,pi_infty)<=Lambda(T)C^mix

with exactly the corrected C^mix and the two Lambda(T) expressions in the task.

## 6. Conditional local KL estimate

Fix [s,t]=[t_{k-1},t_k], delta=int_s^t beta-bar>0, and a starting state x. The learned interpolation has constant spatial drift coefficient

    a_theta=alpha x+2s_theta(x,T-s)

and satisfies dZ_u^theta=beta-bar_u a_theta du+sqrt(2beta-bar_u)dB_u. Its endpoint is precisely Q_k^theta(x,.).

We use the following finite-energy consequence of Girsanov: for nonexplosive diffusions with the same deterministic diffusion coefficient sqrt(2beta-bar), the same initial state, locally regular drift coefficients, and finite expected squared drift-coefficient mismatch integrated against beta-bar under the first law,

    KL(P||P^theta)
       <=(1/4)E_P int_s^t beta-bar_u||a(u,Z_u)-a_theta||^2du. (4)

For the required inequality, localization suffices: stop when the path leaves a ball or the mismatch energy exceeds n. The stopped exponential is a true martingale, Girsanov identifies the stopped laws, and their entropy equals the stopped energy divided by four. Nonexplosion and finite energy imply convergence of the stopped paths to the original paths. Lower semicontinuity of entropy gives (4). This avoids any unjustified Novikov assertion for polynomial drifts. Intervals on which beta-bar=0 have constant paths and contribute zero energy; equivalently work on the integrated-noise clock, without invoking a differentiable inverse. The spatial regularity and nonexplosion were verified above, and the finite energy follows from (1), (2), and finiteness of a_theta for fixed x. Data processing then bounds endpoint KL by (4).

Let Z_u be the exact reverse path started at x, Y_u=S_{T-u}(Z_u), and J_u=nabla S_{T-u}(Z_u). Differentiating the forward Fokker-Planck equation and applying Itô on positive-noise times gives

    dY_u=-alpha beta-bar_u Y_u du+sqrt(2beta-bar_u)J_u dB_u. (5)

Indeed, writing phi_u=log p_{T-u}, its backward-time equation is

    partial_u phi_u=-beta-bar_u[alpha(d+x·gradient phi_u)
                                    +Delta phi_u+||gradient phi_u||^2].

In Itô's formula for gradient phi_u(Z_u), the Laplacian terms, the Hessian-times-score terms, and the alpha Hessian-times-position terms cancel, leaving (5).

This identity remains valid up to the data endpoint. From (1) and (2), with q=4p+4,

    E_x int_s^t beta-bar_u||J_u||_F^2du
       <=2C_H^2 int_s^t beta-bar_u E_x(1+||Z_u||^q)du<infinity.

The martingale therefore has an L2 endpoint limit. The score drift is integrable by the stronger score bound in (2) and the same conditional moments. Local convergence of the smoothed score to S_0, continuity of Z, and the polynomial bounds identify the limit with S_0(Z_T). Uniform integrability follows by using a higher polynomial moment in (1), available for every Dirac start. Zero-noise plateaus add no increments. Thus this argument is conditional on the starting x, not merely an assertion about the original reverse marginal.

Put E_s(x)=S_{T-s}(x)-s_theta(x,T-s). Combining the reverse SDE with (5) cancels the integrals involving Y:

    alpha(Z_u-x)+2(Y_u-Y_s)
      =alpha^2 int_s^u beta-bar_v Z_v dv
         +int_s^u sqrt(2beta-bar_v)(alpha I_d+2J_v)dB_v.    (6)

Choose finite L_2,K_2,L_q,K_q such that, throughout this interval,

    E_x||Z_u||^ell<=L_ell||x||^ell+K_ell,  ell=2,q.

For example (1) permits L_ell=1 and K_ell=D_ell/c_ell. Let C_H be the uniform bound in (2). Jensen and Itô isometry give

    E_x||alpha^2 int_s^u beta-bar_v Z_v dv||^2
       <=alpha^4 delta^2(L_2||x||^2+K_2),

    E_x||int_s^u sqrt(2beta-bar_v)(alpha I_d+2J_v)dB_v||^2
       <=4delta[alpha^2 d+8C_H^2(1+L_q||x||^q+K_q)].

The full mismatch in (4) is the sum of these two terms and 2E_s(x). Apply ||a+b+c||^2<=3(||a||^2+||b||^2+||c||^2), then ||x||^2<=1+||x||^q. Outer integration in (4) yields

    KL(Q_{t|s}(x,.)||Q_k^theta(x,.))
       <=delta^2(Gamma_0+Gamma_1||x||^q)+3delta||E_s(x)||^2, (7)

where one valid choice is

    Gamma_0=(3/4)delta alpha^4(L_2+K_2)
                +3alpha^2 d+24C_H^2(1+K_q),
    Gamma_1=(3/4)delta alpha^4 L_2+24C_H^2 L_q.

These are finite and have only the permitted parameter and interval dependencies.

## 7. Weighted conversion and integration over the learned chain

Put w=1+bV_2 and

    H_k(x)=sqrt(Q_{t_k|t_{k-1}}w^2(x))+sqrt(Q_k^theta w^2(x)).

Cauchy-Schwarz applied to |f-g|=|sqrt(f)-sqrt(g)|(sqrt(f)+sqrt(g)), followed by the supplied Hellinger-versus-KL inequality, gives

    rho_b(Q_{t_k|t_{k-1}}(x,.),Q_k^theta(x,.))
       <=sqrt(KL(Q_x||Q_x^theta))H_k(x).

Both endpoint fourth moments are finite: (1) treats the exact kernel and the frozen learned endpoint is Gaussian for fixed x. Splitting the square root in (7) therefore gives

    rho_b(Q_x,Q_x^theta)
       <=Delta_k sqrt(Gamma_0+Gamma_1||x||^q)H_k(x)
          +sqrt(3Delta_k)||E_{k-1}(x)||H_k(x).              (8)

For mu=hat-pi_{k-1}^theta, the weighted-TV mixture inequality follows directly by testing against |f|<=w and integrating the pointwise kernel discrepancy. Apply it to (8), and then apply Cauchy-Schwarz separately to the two terms. Set

    J_k=int H_k(x)^2 mu(dx),
    C_{k-1}^discr=sqrt(Gamma_0+Gamma_1 mu(V_q))sqrt(J_k),
    C_{k-1}^net=sqrt(3J_k).

These coefficients are finite because

    J_k<=2(mu Q_{t_k|t_{k-1}})(w^2)+2 hat-pi_k^theta(w^2),
    w^2<=2(1+b^2V_4),

and (1) and the assumed chain q-moment bound control the two fourth moments. If desired replace these coefficients by the corresponding upper bounds depending only on the displayed moment bound M and diffusion parameters.

The score-error norm is finite as well. For each step, conditional expectation of the Euler update gives

    2Delta_k s_theta(bar X_{t_{k-1}},T-t_{k-1})
      =E[bar X_{t_k}|bar X_{t_{k-1}}]
          -(1+alpha Delta_k)bar X_{t_{k-1}}.

Conditional Jensen and finite chain second moments imply square integrability of the learned score at that step. The true score is square integrable by (2) and the assumed q-moment. Thus (8) integrates to

    rho_b(hat-pi_{k-1}^theta Q_{t_k|t_{k-1}},hat-pi_k^theta)
       <=Delta_k C_{k-1}^discr
          +sqrt(Delta_k)C_{k-1}^net
               ||E_{k-1}||_{L2(hat-pi_{k-1}^theta)}.       (9)

## 8. Telescoping

Write K_k=Q_{t_k|t_{k-1}} and let an empty product be the identity. Define

    zeta_k=hat-pi_k^theta K_{k+1}...K_N,  0<=k<=N.

Then zeta_0=pi_infty Q_{T|0}, zeta_N=hat-pi_N^theta, and

    rho_b(zeta_{k-1},zeta_k)
      <=bar-alpha^{N-k}
          rho_b(hat-pi_{k-1}^theta K_k,hat-pi_k^theta).

All laws have finite second moments by the established moment estimates. Moreover pi_data=p_TQ_{T|0}, so

    rho_b(pi_data,zeta_0)
       <=bar-alpha^N rho_b(p_T,pi_infty)
       <=bar-alpha^N Lambda(T)C^mix.

The triangle inequality, the consecutive zeta_k laws, and (9) now give exactly the requested geometrically discounted decomposition.

Finally 2TV<=rho_b follows from w>=1. To see the Wasserstein consequence, couple the common part of two laws identically and couple the residuals; ||x-y||^2<=2||x||^2+2||y||^2 gives W_2^2<=2 int ||x||^2d|mu-nu|<=2rho_b/b.
