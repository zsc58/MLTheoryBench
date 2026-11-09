# Reference Proof

## Audit status and proof obligations

This proof covers every real q>1, including 1<q<2, and h=0. It does not use the source's q>=2 weak triangle inequality outside its range. All theorem-critical endpoint, first-order error, Gaussian integration, coupling, contraction, and bias obligations are derived below. The specialized prior HMC citations are provenance, not black-box proof assumptions.

Write ell=log 2 and gamma_d=N(0,I_d). All vector norms are Euclidean and matrix norms are operator norms.

## 1. Exact invariance and elementary endpoint estimates

The gradient is globally Lipschitz, so the Hamiltonian ODE has a global C^1 flow. Along that flow the derivative of H is zero, and the phase-space vector field (v,-grad f(x)) has zero divergence. The Jacobian determinant therefore stays equal to one. Consequently the flow preserves the density proportional to exp(-H), and independent Gaussian velocity refreshment preserves nu tensor gamma_d. Thus nu P_T=nu.

We establish quantitative facts for both the exact position trajectory and the Verlet positions at grid times. Put C=24/23. The hypothesis gives LT^2<=1/12. For the exact trajectory,

q_t=x+tv-integral_0^t (t-a) grad f(q_a) da.

For t_j=jh, summing the Verlet recurrence gives

x_j=x+t_j v-h^2[j grad f(x)/2+sum_{i=1}^{j-1}(j-i)grad f(x_i)].

The nonnegative weights in the latter expression sum to t_j^2/2. Since grad f(0)=0, the integral equation and recurrence give, for either trajectory, a position bound C(||x||+T||v||). For two trajectories with the same initial velocity, the corresponding position difference is at most C||x-y||.

Let J(t) denote the derivative of position with respect to initial velocity, with the discrete interpretation at grid times. Differentiating the preceding equations and using the weights gives

||J(t)||<=Ct,

because the weighted sum of t_i is at most t_j^3/6, just as integral_0^t(t-a)a da=t^3/6. More explicitly, if S is the maximum of ||J(t)||/t, then S<=1+(LT^2/6)S, and hence S<=72/71<C. For the exact trajectory, the ratio at t=0 is understood by its continuous extension J(t)/t tending to I. Therefore, for the terminal position map F_x(v),

||D_v F_x/T-I||<=CLT^2/6<=1/69.

These estimates are uniform in x and v. The function F_x(v)/T-v is globally 1/69-Lipschitz. For each terminal position, its inverse equation is a contraction mapping on R^d. Thus F_x is a global C^1 diffeomorphism, and its inverse is 69/(68T)-Lipschitz. This proves existence, uniqueness, differentiability, and bijectivity of all endpoint coupling maps used below.

For either exact or discrete dynamics define theta_xy=F_y^{-1}F_x. It matches terminal positions and satisfies

||theta_xy(v)-v||<=b||x-y||,  b=18/(17T),

since (69/68)C=18/17. Comparing the terminal velocity-derivative matrices gives the uniform bound

||D theta_xy-I||<=2(1/69)/(1-1/69)=1/34.

There is also a local bound. Put D=||x-y|| and w=theta_xy(v). The two matched trajectories have position difference at most C(D+T||v-w||)<=C(35/17)D. Their velocity-derivative difference satisfies the differentiated integral equation or recurrence. The Hessian difference is bounded by M times the position difference; absorbing its L times derivative-difference term and using the weighted sum of t_i yields

||J_x(T)-J_y(T)||<=C^3(35/17)MT^3D/6.

Multiplication by the inverse terminal derivative gives

||D theta_xy-I||<=MT^2D,

because (69/68)C^3(35/17)/6<1 and MT^2D>=0. This non-strict bound includes M=0 and D=0. In particular these estimates imply the source's weaker displacement 3D/(2T) and Jacobian bounds min{2/9,(11/2)MT^2D}.

## 2. First-order cross-map estimates without an external gap

Suppose first h>0. We use a weighted quadrature estimate valid for vector- or matrix-valued C^1 functions b. If sup||b'||<=D_b and t=t_j=jh is a grid time, then

|| integral_0^t(t-a)b(a) da - h^2[j b(0)/2+sum_{i=1}^{j-1}(j-i)b(t_i)] || <=(5/12)h t^2 D_b.

To verify it, replace b by its piecewise linear interpolant I_h b. Its pointwise error is at most h D_b/2, contributing at most h t^2 D_b/4. On each interval [t_i,t_{i+1}], direct integration of the two linear factors shows that the weighted interpolant integral minus the trapezoidal contribution equals +(h^2/6)(b(t_{i+1})-b(t_i)). Summing these differences gives

integral_0^t(t-a)(I_h b)(a) da - h^2[j b(0)/2+sum_{i=1}^{j-1}(j-i)b(t_i)] = +(h^2/6)(b(t)-b(0)).

Its norm is at most h^2 t D_b/6<=h t^2 D_b/6. Combining the two error bounds proves the estimate. At t=0 the estimate is immediate.

For the exact trajectory, integration of its acceleration and the position bound give

sup_{t<=T}||v_t||<=6||v||/5+7LT||x||/6=:V_*.

Applying the quadrature estimate to b(t)=grad f(q_t), whose derivative has norm at most LV_*, and absorbing the position-error term with factor C, gives the grid error

E:=max_j||x_j-q_{t_j}||<=(5/12)ChLT^2 V_*<=h(6||v||/25+7LT||x||/30).

For completeness, the tighter intermediate coefficients are 1/23 for h||v|| and 35/828 for hLT||x||, so the last relaxation is valid.

For exact J(t), the variational equation gives ||J(t)||<=Ct and ||dot J(t)||<=C. Apply weighted quadrature to b(t)=Hessian f(q_t)J(t). Its derivative is bounded by

D_b<=C[L+MT V_*]<=C[L+(6/5)MT||v||+(7/72)M||x||].

The grid derivative error F=max_j||D_v x_j-J(t_j)|| obeys

F<=C[(5/12)hT^2D_b+(MC T^3/2)E].

Substitution and LT^2<=1/12 give

F<=h C^2[5/144+(217/4320)MT^2||x||+(31/50)MT^3||v||]
 <=h[1/20+MT^2||x||/10+MT^3||v||].

Define phi_x=(F_x^exact)^{-1}F_x^discrete. Its displacement is bounded by 69E/(68T), and therefore

||phi_x(v)-v||<=h[p_v||v||+p_x||x||].

Both endpoint derivatives are within T/69 of TI, so ||D phi_x-I||<=1/34<=1/2 globally. For a local bound, two exact trajectories from x with initial velocities v,w satisfy

||J_x(T,v)-J_x(T,w)||<=C^3 MT^4||v-w||/12.

This follows by inserting ||q_t(v)-q_t(w)||<=Ct||v-w|| and ||J(t,w)||<=Ct into the variational difference equation and using integral_0^T(T-t)t^2 dt=T^4/12, followed by the same absorption factor C. Hence

||D phi_x-I||<=69/(68T)[F+C^3MT^4||phi_x(v)-v||/12]
 <=(2/15)h[2/T+(16/5)MT||x||+20MT^2||v||].

The last inequality follows by substituting the preceding F and displacement bounds and LT^2<=1/12; separately, its constant, ||x||, and ||v|| coefficients are no larger than 4/(15T), 32MT/75, and 8MT^2/3.

Now compose phi_x with the exact map theta_xy and call the result Phi_xy. Then

qtilde_{T,h}(x,v)=q_T(y,Phi_xy(v)).

Using the weaker same-kernel bounds recorded at the end of Section 1 gives exactly

||Phi_xy(v)-v||<=p_xy||x-y||+hp_v||v||+hp_x||x||,

||D Phi_xy(v)-I||<=min{15/18,j_xy||x-y||+hj_c+hj_v||v||+hj_x||x||}.

Indeed, the Jacobian product bound is ||A-I||+(1+||A-I||)||B-I||. Its global value is at most 2/9+(11/9)(1/2)=15/18; its local value is (11/2)MT^2||x-y||+(22/135)h[2/T+(16/5)MT||x||+20MT^2||v||]. This is the displayed list of j coefficients.

When h=0, phi_x is the identity and all discretization errors vanish; the same conclusions hold directly. All these maps are C^1 diffeomorphisms and depend continuously on their position parameters.

## 3. Gaussian change of variables and same-kernel regularization

For a C^1 diffeomorphism F and r>1, change of variables gives, with V~gamma_d,

(r-1)R_r(F_#gamma_d||gamma_d)=log E exp((r-1)[(||F(V)||^2-||V||^2)/2-log|det DF(V)|]).

If ||F(v)-v||<=m_1 and ||DF(v)-I||<=m_2<1, singular values give |det DF|>=(1-m_2)^d. The source's standard Gaussian concentration statement is E exp(t(g(V)-Eg(V)))<=exp(t^2/2) for every 1-Lipschitz g. For g(v)=||v||, Jensen gives Eg<=sqrt d, so E exp(t||V||)<=exp(t sqrt d+t^2/2) for t>=0. Substituting in the change-of-variables formula proves

R_r(F_#gamma_d||gamma_d)<=d m_2/(1-m_2)+sqrt(d)m_1+r m_1^2/2.

The endpoint identities and data processing transfer these bounds to position kernels. The weaker same-kernel estimates give

R_r(delta_x P_h||delta_y P_h)<=A D+9r D^2/(8T^2),

where A=8dMT^2+3sqrt(d)/(2T). The stronger estimates actually proved in Section 1 give

R_r(delta_x P_h||delta_y P_h)<=A_*D+(r b^2/2)D^2,

where A_*=34dMT^2/33+18sqrt(d)/(17T) and b=18/(17T).

## 4. Cross-regularization at order 2q

Use the cross map and put s=2q-1, D=||x-y||, X=||x||, and w=1+hp_v. Define

c_0=(p_xy D+hp_x X)^2/2+6d(j_xy D+hj_c+hj_x X),

c_1=w(p_xy D+hp_x X)+6dhj_v,

c_2=hp_v(hp_v+2)/2.

The displacement estimate controls the Gaussian energy difference. The global Jacobian bound implies -log|det D Phi|<=6d||D Phi-I||, so the logarithmic integrand is bounded by s(c_0+c_1||V||+c_2||V||^2).

Cauchy-Schwarz, Gaussian concentration, and the identity E exp(t||V||^2)=(1-2t)^(-d/2) for t<1/2 give

R_{2q}((Phi_xy)_#gamma_d||gamma_d)
 <=c_0+sqrt(d)c_1+s c_1^2-d log(1-4s c_2)/(4s).

The restriction w<=u implies s c_2<=1/8. Thus the Gaussian integral is finite and -log(1-4s c_2)<=8s c_2. Consequently the bound is at most c_0+sqrt(d)c_1+s c_1^2+2dc_2. Using (a+b)^2<=2a^2+2b^2 and (a+b+c)^2<=3(a^2+b^2+c^2) yields

R_{2q}(delta_x P_h||delta_y P_T)<=alpha_0+alpha_1D+alpha_2D^2+alpha_3X+alpha_4X^2,

where

alpha_0=dh[6j_c+6sqrt(d)j_v+108sdh j_v^2+hp_v^2+2p_v],

alpha_1=sqrt(d)[6sqrt(d)j_xy+p_xy w],

alpha_2=p_xy^2(1+3s w^2),

alpha_3=h sqrt(d)[6sqrt(d)j_x+p_x w],

alpha_4=h^2p_x^2(1+3s w^2).

This derivation does not substitute velocity-dependent bounds into a lemma requiring uniform displacement. Keeping the velocity terms inside the Gaussian integral is essential. Squaring the source's alternative quadratic-in-velocity displacement estimate would instead introduce a generally nonintegrable positive quartic exponential.

## 5. Coupling lift and Orlicz facts

For r>1 the perspective function a^r b^{1-r} is jointly convex. Applying this pointwise to mixtures under any coupling Gamma of input laws and integrating gives

exp((r-1)R_r(mu P||pi Q))<=E_Gamma exp((r-1)R_r(delta_X P||delta_Y Q)).

Taking logarithms gives both the same-kernel and cross-kernel coupling lifts. No absolute continuity assumption on the input laws is required.

If ||Z||_psi<=K with K>0, the definition and monotone convergence give E exp(||Z||^2/K^2)<=2. Concavity of t^theta for 0<=theta<=1 then gives

E exp(c||Z||^2)<=2^{cK^2},  0<=c<=K^{-2}.

The needed optimal Orlicz couplings exist: take a minimizing sequence of couplings, use tightness from their fixed marginals, and pass to a weak limit. For each scale strictly above the infimum, the nonnegative continuous exponential cost has expectation at most two in that limit by lower semicontinuity; then decrease the scale to the positive infimum. At zero distance, Jensen gives W_2<=sqrt(ell)W_psi, so the two laws coincide and the diagonal coupling is available.

## 6. Original and strengthened transient bounds

Put W=W_psi(mu,bar nu). If W=infinity there is no eligible finite k. If W=0, mu=bar nu and invariance makes every transient divergence zero. Otherwise let a=c_1 exp(-c_2 k)W. Contraction supplies a coupling of mu Q^k and bar nu with displacement Orlicz norm at most a.

A same-kernel estimate R_r(delta_x P_h||delta_y P_h)<=a_1D+a_2D^2 leads, with e_1=(r-1)a_1 and e_2=(r-1)a_2, to

(r-1)R_r(mu Q^kP_h||bar nu P_h)<=e_1 a sqrt(ell)+e_2 a^2 ell,

provided e_2a^2+e_1a/(2sqrt(ell))<=1. Indeed apply Young's inequality e_1D<=beta^2e_1^2/2+D^2/(2beta^2), choose beta^2=a sqrt(ell)/e_1, and use the Orlicz interpolation just proved.

At r=2q, the weaker same-kernel bound has e_1=delta_1 and e_2=delta_2. Solving delta_2 a^2+delta_1 a/(2sqrt(ell))<=1 gives exactly the public logarithmic threshold. Since k>=0, c_1>=1, ell<=sqrt(ell), and W<=max{1,W^2}, this also reconstructs the original general-kernel transient estimate

R_{2q}(mu Q^kP_h||bar nu P_h)<=G_k,

G_k=((delta_1+delta_2)/s)sqrt(ell)c_1^2 exp(-c_2 k)max{1,W^2}.

For the final all-q argument we use the stronger estimate at r=s=2q-1. Elementary comparisons give

A_*<=3A/4,

r b^2/2<=3[9q/(4T^2)]/4.

Here 18/17<9/8 and 34/33<6 verify the linear comparison; the quadratic comparison follows from b^2=324/(289T^2) and r<2q. The effective exponential coefficients are therefore no larger than (3/4)(r-1)/s times delta_1,delta_2. The same public threshold ensures admissibility. Dividing the resulting Young bound by r-1 yields

R_{2q-1}(mu Q^kP_h||bar nu P_h)<=3G_k/4.

This improvement is private proof machinery, not an added task assumption.

## 7. Invariant-to-target bias and admissibility

Use nu P_T=nu and the cross coupling lift from Section 4. Let lambda=W_psi(bar nu,nu)<=Delta_h and K=K_nu. First suppose lambda>0 and alpha_3>0. Under an optimal coupling put D=||X-Y||, with Y~nu. Apply Young's inequality to alpha_1D and alpha_3||X|| and define

eta_0=beta_1^2 alpha_1^2/2+beta_3^2 alpha_3^2/2,

eta_1=alpha_2+1/(2beta_1^2),  eta_2=alpha_4+1/(2beta_3^2).

Since ||X||^2<=2D^2+2||Y||^2, Cauchy-Schwarz and Orlicz interpolation give

R_{2q}(bar nu P_h||nu)<=alpha_0+eta_0+ell[(eta_1+2eta_2)lambda^2+2eta_2K^2],

provided

2s(eta_1+2eta_2)lambda^2<=1,  4s eta_2K^2<=1.

Choose beta_1^2=lambda sqrt(ell)/alpha_1 and beta_3^2=sqrt(2(lambda^2+K^2)ell)/alpha_3. The bound becomes

alpha_0+alpha_1lambda sqrt(ell)+alpha_3sqrt(2(lambda^2+K^2)ell)+ell[alpha_2lambda^2+2alpha_4(lambda^2+K^2)].

In particular it is at most

alpha_0+2alpha_1lambda+alpha_2lambda^2+2alpha_3(lambda+K+sqrt(lambda^2+K^2))+2alpha_4(lambda^2+K^2).

We verify both moment conditions explicitly. Let

A_1=sqrt(d)(6sqrt(d)j_xy+p_xy u), A_2=p_xy^2(1+3su^2),

A_3=h sqrt(d)(6sqrt(d)j_x+p_x u), A_4=h^2p_x^2(1+3su^2).

Then alpha_i<=A_i for i=1,...,4. A sufficient condition for the displacement moment is

(A_2+2A_4)Delta_h^2+(A_1/sqrt(2)+A_3)Delta_h/sqrt(2ell)<=1/(2s).

The two stated Delta_h bounds make these two terms at most 1/(8s) and 1/(4s), respectively. Their sum is at most 3/(8s)<1/(2s).

A sufficient condition for the target-position moment is

4s A_4K^2+sqrt(2)s A_3K/sqrt(ell)<=1.

The last two stated h bounds make these terms at most 1/4 and 1/2, respectively. Thus this condition holds too. The first h bound was exactly the Gaussian-integrability condition in Section 4.

When lambda=0, use the diagonal coupling, omit the alpha_1D term, and use the same beta_3 choice with lambda=0; its target-position moment is covered by the preceding check. When alpha_3=0, h=0 and alpha_4=0, so omit both position terms instead of dividing by alpha_3. These observations also cover lambda=h=0.

Finally replace lambda by Delta_h and alpha_i by A_i in the last displayed bias bound. The result is precisely the public expression B. Thus R_{2q}(bar nu P_h||nu)<=B.

## 8. Valid final combination for every q>1

We give the needed inequality rather than extending the source's restricted weak triangle inequality. Let p,b,c be densities of laws a,beta,cappa with the finite divergences used below, and put r=2q-1. The identity

p^q c^{1-q}=(p^r b^{1-r})^{q/r}(b^{2q}c^{1-2q})^{(q-1)/r}

and Hölder, whose two weights sum to one, imply

R_q(a||cappa)<=2q R_{2q-1}(a||beta)/(2q-1)+R_{2q}(beta||cappa).

The same inequality holds with extended divergences; if the right side is finite its absolute-continuity requirements hold. Here Sections 6-7 ensure finiteness whenever k is eligible and W is finite.

Apply it with a=mu Q^kP_h, beta=bar nu P_h, and cappa=nu. Since 2q/(2q-1)<=2,

R_q(mu Q^kP_h||nu)<=2(3G_k/4)+B=3G_k/2+B.

Substitution of G_k is exactly the requested conclusion. No condition on q beyond q>1 has been introduced.
