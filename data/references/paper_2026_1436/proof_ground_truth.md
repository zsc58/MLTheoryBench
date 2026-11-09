# Reference Proof

## Obligation Status

The public theorem is proved below in full. Its obligations are: well-definedness and continuity of the sphere functions; cross-augmentation comparison and forward stability; injectivity; persistence-tail control; compact-core inverse convergence; the growth-class L2-to-uniform bridge; and the homeomorphism conclusion. Each is closed below.

The stronger quantitative compact-core Holder estimate from the original reference is retained in a separate final section. Its elementary reductions are repaired, but its specialized Sobolev-to-ReLU-variation embedding is not proved in the supplied source. That private quantitative obligation is explicitly unresolved and is not used to prove any public conclusion.

## 1. Well-Definedness, Cross-Augmentation, And Stability

Write P(p)=(d-b)/2, c(p)=(b+d)/2, and r(p)=||(1,p)||_2. Put psi_v(p)=(<v,(1,p)>)_+. Projection satisfies r(pi_Delta(p))<=r(p). Thus every augmentation is integrable, all defining integrals exist, and

|S(eta)(v)-S(eta)(w)| <= 2||v-w||_2 integral r(p) d eta(p).

In particular each sphere is continuous and belongs to L2 for ordinary surface area measure.

For alpha=mu+nu^Delta and beta=nu+mu^Delta, both measures are finite, integrable, and have the same mass mu(X)+nu(X). Linearity gives

S(mu)(v)-S(nu)(v)=integral psi_v d(alpha-beta).

Define W_1 on X union Delta as the infimum of the d_infty cost of positive couplings with the prescribed equal-mass marginals. Restricting any such coupling to X times X gives a partial plan. Its unmatched deletion costs are bounded by the coupling's X-to-Delta and Delta-to-X costs. Consequently POT_1(mu,nu)<=W_1(alpha,beta).

Conversely, let gamma be a partial plan, xi=mu-gamma_1, and zeta=nu-gamma_2. The measure

Gamma=gamma+(Id,pi_Delta)#xi+(pi_Delta,Id)#zeta+(pi_Delta composed with pi_2,pi_Delta composed with pi_1)#gamma

has marginals alpha,beta. The last term costs no more than the matched part of gamma, since pi_Delta is 1-Lipschitz. Therefore

POT_1(mu,nu)<=W_1(alpha,beta)<=2POT_1(mu,nu).

The standard independent Kantorovich-Rubinstein theorem used here states that, on a Polish metric space, finite positive measures of equal mass and finite first moment satisfy W_1(alpha,beta)=sup_{Lip(f)<=1} integral f d(alpha-beta). The space X union Delta is a closed Euclidean half-plane with the equivalent sup metric and is Polish. Equal mass and finite first moments were verified above; zero mass causes no exception.

For v in S^2, psi_v is sqrt(2)-Lipschitz in d_infty, because ||(v_1,v_2)||_1<=sqrt(2). Duality and the comparison give

||S(mu)-S(nu)||_infinity<=sqrt(2)W_1(alpha,beta)<=2sqrt(2)POT_1(mu,nu).

## 2. Injectivity

Suppose S(mu)=S(nu). Positive homogeneity extends equality of the transforms of alpha and beta to every vector in R^3. Hence, for every a in R and u in R^2,

H_alpha(a,u):=integral (a+u dot p)_+ d alpha(p)=H_beta(a,u).

For h>0 the difference quotient in a has integrand between zero and one, converging to the indicator of {a+u dot p>=0}. Dominated convergence, applicable because both measures are finite, gives

partial_a^+ H_alpha(a,u)=alpha({p:u dot p>=-a}),

and the identical formula for beta. Thus all linear pushforward measures of alpha and beta agree, including their total masses.

The standard independent projection-uniqueness result used here is: two finite Borel measures on R^2 whose pushforwards under every linear functional agree are equal. Indeed their characteristic functions agree at each vector, and uniqueness of the Fourier transform of finite measures gives equality. The hypotheses are exactly finiteness, the Borel property, and the pushforward equalities just established. It follows that alpha=beta. Restricting to X yields mu=nu, since the added projected measures are concentrated on Delta.

## 3. Persistence Identities And Tail Control

For v=(v_0,v_1,v_2), put s=v_1+v_2 and t=v_2-v_1. The integrand of S is

phi_v(p)=(v_0+s c(p)+t P(p))_+-(v_0+s c(p))_+.

It satisfies |phi_v(p)|<=sqrt(2)P(p). Consequently, for every measurable E subset X,

||S(eta)-S(eta|_E)||_infinity<=sqrt(2) integral_{X\E} P d eta.

Also POT_1(eta,0)=integral P d eta, directly from the definition. At v_P=(0,-1/sqrt(2),1/sqrt(2)),

S(eta)(v_P)=sqrt(2) integral P d eta.

Assume S(mu_n) converges uniformly to S(mu), with supp(mu) compact in X. Total persistence converges and is uniformly bounded. If mu=0, the deletion identity immediately proves POT_1(mu_n,0)->0. Hence suppose mu is nonzero. There are finite R_0,M_0>0 and m_0>0 such that supp(mu) lies in {|c|<=R_0, m_0<=P<=M_0}.

For diagonal tails, take s_0=1/(2R_0), t_0=1/(2M_0), and normalize the vector (-1,(s_0-t_0)/2,(s_0+t_0)/2) to a unit vector v. Both ReLU arguments are nonpositive on supp(mu), so S(mu)(v)=0. Its integrand is nonnegative everywhere. For c sufficiently large, the diagonal argument is positive, and phi_v=t(v)P. Uniform convergence therefore forces integral_{c>=R} P dmu_n->0 for a fixed sufficiently large R. Reflecting v to (v_0,-v_2,-v_1) gives the corresponding negative tail. Increase R to include the target support.

For persistence tails, for a>=0 define t_a=sqrt(2/(1+2a^2)) and v_a=(-a t_a,-t_a/2,t_a/2). Direct substitution gives

S(eta)(v_a)=t_a integral (P-a)_+ d eta.

Since P 1_{P>=2a}<=2(P-a)_+, choosing a=M_0 forces integral_{P>=M} P dmu_n->0 for every fixed M>2M_0.

Choose 0<delta<m_0/2 and let g_delta(z)=z-2(z-delta)_++(z-2delta)_+. This function equals z on [0,delta], equals 2delta-z on [delta,2delta], and is zero above 2delta. Thus g_delta>=z 1_{z<delta}. Its integral is a fixed linear combination of the sphere values at v_0,v_delta,v_{2delta}. That combination converges to zero, because g_delta(P) vanishes on the target support. Therefore integral_{P<delta} P dmu_n->0.

The fixed set K={|c|<=R, delta<=P<=M} is compact in X and contains supp(mu). The preceding three estimates imply

T_n:=integral_{X\K} P dmu_n->0.

No r-weighted tail convergence is claimed or required. Put rho_n=mu_n|_K. The truncation inequality gives ||S(rho_n)-S(mu)||_infinity->0. The persistence bound and P>=delta on K give a uniform bound on rho_n(K).

## 4. Qualitative Compact-Core ReLU Approximation

Here is a complete qualitative version of the source's compact-core approximation step. It does not assume the specialized quantitative embedding.

Let rho_n and mu be supported on a fixed nonempty compact K subset X, assume their persistence sums are bounded, and suppose epsilon_n=||S(rho_n)-S(mu)||_infinity->0. Put Kbar=K union pi_Delta(K) and

eta_n=(rho_n+mu^Delta)-(mu+rho_n^Delta).

These signed measures have zero mass, are supported on Kbar, and have uniformly bounded total variation: if delta_K=inf_K P>0, then

||eta_n||_TV<=2[rho_n(K)+mu(K)]<=2[Pers(rho_n)+Pers(mu)]/delta_K.

Finite affine-ReLU combinations are uniformly dense in continuous functions on a square containing Kbar. To verify the only approximation fact needed, first approximate a continuous function on that square by its two-variable Bernstein polynomials. Uniform convergence follows by expressing the polynomial as an expectation at independent binomial grid points: uniform continuity controls nearby grid points, and the binomial variance bound makes the probability of distant grid points uniformly small. Next, a homogeneous polynomial of degree k in two variables is a linear combination of kth powers of linear forms. This follows by expanding (x+a_j y)^k at k+1 distinct a_j and inverting the resulting Vandermonde matrix. On a bounded interval, each univariate kth power is uniformly approximated by piecewise-linear interpolation. Every continuous piecewise-linear function has a finite representation as an affine function plus a sum of hinges (z-a)_+. Affine functions themselves are finite affine-ReLU combinations, using z=z_+-(-z)_+ and a constant ridge. Composing these representations with the linear forms proves the asserted density. A Lipschitz test initially defined on Kbar extends to the square by the explicit formula inf_{z in Kbar}(f(z)+||x-z||_infinity), so this density applies to all tests below.

Normalize every 1-Lipschitz Kantorovich test by f(u_*)=0 at a fixed u_* in Kbar. These restrictions have a finite uniform q-net for every q>0. Explicitly, choose finitely many points forming a sufficiently fine net of Kbar and quantize the bounded values of f at these points. There are finitely many value patterns, and tests with the same pattern are uniformly close by their Lipschitz property. Choose one representative f_j for each occurring pattern.

For each representative choose a finite affine-ReLU combination h_j with ||f_j-h_j||_{Kbar}<q. Write its ridges as (a+u dot p)_+=||(a,u)||_2 psi_{(a,u)/||(a,u)||_2}(p), omitting zero vectors. It follows that |integral h_j d eta_n|<=C_j epsilon_n for a finite coefficient sum C_j. For any normalized test f choose a representative within q. If V bounds ||eta_n||_TV, then

|integral f d eta_n|<=2qV+max_j C_j epsilon_n.

The bound is uniform over all 1-Lipschitz tests. Kantorovich-Rubinstein duality and the cross-augmentation comparison yield limsup POT_1(rho_n,mu)<=2qV. Letting q decrease to zero proves POT_1(rho_n,mu)->0. Empty K means both measures are zero and needs no approximation.

Apply this result to the truncations in Section 3. A partial plan between rho_n and mu is also a partial plan between mu_n and mu, with additional deletion cost T_n. Taking infima gives

POT_1(mu_n,mu)<=POT_1(rho_n,mu)+T_n->0.

This closes the public compact-target inverse-continuity claim.

## 5. Growth-Class L2-To-Uniform Bridge

Let mu_n,mu belong to M(A,B), with a fixed compatible pair. Suppose d_n=||S(mu_n)-S(mu)||_2->0. For R>=1 set K_R={p in X:r(p)<=R}, S_R(eta)=S(eta|_{K_R}), and

tau_R=(sqrt(2)/R)B(R^2\B_{R-1}),  L_R=2A(B_R).

The set K_R is bounded but need not be compact in X; compactness of this set is not used. If p is outside K_R, then ||p||_2>R-1 and P(p)<=r(p)P(p)/R. The mixed-moment domination and Section 3's truncation bound therefore give ||S(eta)-S_R(eta)||_infinity<=tau_R uniformly in eta. Moreover

Lip(S_R(eta))<=2 integral_{K_R} r d eta<=L_R.

Thus h_{n,R}=S_R(mu_n)-S_R(mu) is 2L_R-Lipschitz, and

||h_{n,R}||_2<=d_n+2sqrt(4pi)tau_R.

In particular, at fixed R its L2 norm need not converge to zero.

For completeness, if f is L-Lipschitz on S^2 with inherited Euclidean distance, Q=||f||_infinity, and N=||f||_2, then

Q<=2 max{pi^{-1/4}sqrt(LN), pi^{-1/2}N}.

Indeed a chordal cap of radius a in (0,2) has area pi a^2, and at a maximum point |f| is at least (Q-La)_+ throughout the cap. Hence N>=sqrt(pi)a(Q-La)_+. If 0<Q<=2L use a=Q/(2L); if Q>2L use a=1. Q=0 is immediate, and L=0 is covered by the second case unless Q=0. This proves the estimate including degenerate constants.

Apply it with L=2L_R. Taking limsup in n gives

limsup_n ||h_{n,R}||_infinity<=max{4sqrt(2L_R tau_R),8tau_R}.

Adding the two truncation defects yields

limsup_n ||S(mu_n)-S(mu)||_infinity<=2tau_R+max{4sqrt(2L_R tau_R),8tau_R}.

Now tau_R->0 because B is finite, and L_R tau_R->0 by compatibility. Letting R tend to infinity proves uniform convergence. This preserves the necessary order: first take the limsup in n while retaining the defect, then send R to infinity.

## 6. Hilbert Realization

Ordinary surface area of S^2 is 4pi, so

||S(mu)-S(nu)||_2<=sqrt(4pi)||S(mu)-S(nu)||_infinity<=4sqrt(2pi)POT_1(mu,nu).

Equality as L2 classes is equality everywhere for these continuous sphere functions, since surface measure has full support. Section 2 therefore also gives injectivity into L2.

On M_c(A,B), L2 convergence to any member of the class implies uniform convergence by Section 5, and then POT_1 convergence by Sections 3-4, because the target has compact support in X. Conversely the displayed bound gives forward continuity. Sequential continuity characterizes continuity between metric spaces, proving that the injective restriction is a homeomorphism onto its image. Zero A, zero B, and the zero-measure class are included in the preceding estimates.

## 7. Retained Quantitative Auxiliary Claim: Explicitly Unresolved

The original reference also asserted, on a fixed compact K subset X,

POT_1(rho,mu)<=C_K M^{3/5}epsilon^{2/5},

where M=Pers(rho)+Pers(mu) and epsilon=||S(rho)-S(mu)||_infinity. This stronger rate is not a public target. Its source-grounded conditional reduction is as follows.

Normalize a 1-Lipschitz test by subtracting its value at a fixed point of Kbar, extend it, and mollify at 0<t<=1. The source's derivative estimates give W^{2,2} norm O_K(t^{-1}) and W^{3,2} norm O_K(t^{-2}); Sobolev interpolation gives W^{5/2,2} norm O_K(t^{-3/2}), while the uniform approximation error is O(t). The additive normalization bounds the zeroth-order term. For dilation h_tilde(x)=h(R_K x) in dimension two, the correct identity is ||D^m h_tilde||_{L2(B_1)}=R_K^{m-1}||D^m h||_{L2(B_{R_K})}.

The unresolved specialized input states that the variation norm of g represented on B_1 by ridges (omega dot x+b)_+, omega in S^1, b in [-1,1], is at most A_0||g||_{W^{5/2,2}(B_1)}. The normalized mollification is smooth on a neighborhood of the ball and meets this stated Sobolev hypothesis. Dilation and bias rescaling would give a coefficient norm O_K(t^{-3/2}). Fubini is legitimate on compact parameter and spatial domains with finite coefficient and signed spatial measures. Normalizing ridges to sphere directions and bounding signed total variation by 2M/delta_K would then give

POT_1(rho,mu)<=C_K(epsilon t^{-3/2}+Mt), 0<t<=1.

For 0<epsilon<M choose t=(epsilon/M)^{2/5}. For epsilon>=M use deletion of both measures, POT_1<=M, enlarging C_K as needed. For epsilon=0 let t decrease to zero. For M=0 or empty K both measures vanish. These repairs preserve the rate and K-only constant dependence, conditional on the specialized input.

The supplied paper states and cites that input but does not derive it. Therefore this section is a conditional reduction, not a completed proof of the quantitative auxiliary claim. No full-credit scoring step may be justified solely by this unresolved section. Sections 1-6 already establish every public conclusion without it.
