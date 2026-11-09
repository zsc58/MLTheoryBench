# Reference Proof

## Proof Structure and Obligations

We prove: (1) global existence and compact confinement of the rescaled generation curve; (2) value and posterior-gradient asymptotics; (3) identification of every forward time-shift limit, including measurable weak-* constraint closure; (4) existence, dissipation, and single-critical-point convergence for every autonomous solution; (5) local trapping in both parameter regimes; and (6) conditional convergence of the original curve by bounded bad intervals.

The standard independent nonsmooth facts used below are the finite-maximum Clarke formula, the sign and smooth-addition rules, the general Clarke sum inclusion, and the Fermat condition that a local minimum of a locally Lipschitz function is Clarke-critical. The finite-maximum formula says that the Clarke subdifferential of a finite maximum of continuously differentiable functions is the convex hull of the active gradients. We also use the standard differential-inclusion existence theorem: an upper-semicontinuous multifunction on Euclidean space with nonempty compact convex values and a global bound C(1+||x||) admits a global locally absolutely continuous solution from every initial point. Its hypotheses are verified below. No specialized asymptotically autonomous convergence theorem is assumed.

## 1. Rescaling, Confinement, and Compactness

Write the finite measures as u_{0,i}=sum_{a in A_i} w_{i,a} delta_a, with every w_{i,a}>0 and sum_a w_{i,a}=1. Define

p_{i,a}(x,t)=w_{i,a} exp(-||x-a||^2/(4t))/sum_{b in A_i} w_{i,b} exp(-||x-b||^2/(4t)),

m_i(x,t)=sum_{a in A_i}p_{i,a}(x,t)a,

and F_lambda(x,t)=-4t[lambda log u_1(x,t)+(1-lambda)log u_2(x,t)].

Direct differentiation of the finite Gaussian sums gives

nabla log u_i(x,t)=(m_i(x,t)-x)/(2t),

nabla F_lambda(x,t)=2[x-lambda m_1(x,t)-(1-lambda)m_2(x,t)].

Since dt/dtau=-t, the generation ODE becomes

Y'_tau=-nabla F_lambda(Y_tau,Te^{-tau})/4.

Let K=lambda conv(A_1)+(1-lambda)conv(A_2). This is a nonempty compact convex set, also when 1-lambda is negative. The mixed barycenter belongs to K, so Y'=-(Y-k_tau)/2 for a point k_tau in K. Put L(x)=dist(x,K)^2/2. The projection formula nabla L(x)=x-P_Kx and the projection inequality give

dL(Y_tau)/dtau=-(1/2)<Y_tau-P_KY_tau,Y_tau-k_tau> <= -L(Y_tau).

Consequently L(Y_tau)<=e^{-tau}L(x_T). Thus Y remains in the compact set Omega={L<=L(x_T)}. The vector field is smooth and locally Lipschitz in x on each bounded similarity-time interval. Local ODE existence and continuation, together with this confinement, give a unique global Y and hence X on (0,T].

For every x,t the correct drift estimate is

||nabla F_lambda(x,t)|| <= 2 sup_{k in K}||x-k|| <= 2(||x||+R_K), where R_K=sup_{k in K}||k||.

In particular the drift is uniformly bounded on Omega. The first inequality must use the supremum, not dist(x,K); this is the local source correction recorded for theory_002. All forward time shifts of Y are therefore uniformly bounded and equi-Lipschitz. Arzela-Ascoli and a diagonal extraction on [0,n], n=1,2,..., give local uniform subsequential compactness on [0,infinity).

## 2. Values, Gradients, and Clarke Structures

Let w_i^min=min_{a in A_i}w_{i,a}>0. Factoring out the nearest-distance exponential gives

u_i(x,t)=(4 pi t)^{-d/2} exp(-d_i(x)^2/(4t)) S_i(x,t),

where here nu_i denotes u_i and

S_i(x,t)=sum_{a in A_i}w_{i,a} exp(-[||x-a||^2-d_i(x)^2]/(4t)).

One has w_i^min<=S_i(x,t)<=1. Hence

-4t log u_i(x,t)=d_i(x)^2+2dt log(4 pi t)-4t log S_i(x,t),

and therefore

|F_lambda(x,t)-Phi_lambda(x)| <= 2dt|log(4 pi t)|+4t[lambda|log w_1^min|+|1-lambda||log w_2^min|].

This proves value convergence, in particular locally uniformly. It is the finite-support version of the source's Gaussian lower/upper estimates; no additional assumption is needed.

Define Pi_i(x)={a in A_i:||x-a||=d_i(x)}. The finite-maximum rule applied to -d_i^2 yields

partial^C(d_i^2)(x)=conv{2(x-a):a in Pi_i(x)}.

Set G(x)=widehat partial Phi_lambda(x). For any real coefficient 1-lambda, taking the weighted Minkowski sum gives

G(x)=conv{nabla Q_ab(x):a in Pi_1(x), b in Pi_2(x)},

where Q_ab(x)=lambda||x-a||^2+(1-lambda)||x-b||^2. This convex-hull identity follows by expanding products of convex coefficients; negative scalar multiplication does not invalidate it.

For 0<lambda<1, Phi_lambda=min_{a,b}Q_ab and its active pairs are precisely Pi_1(x) times Pi_2(x). Apply the finite-maximum rule to -Phi_lambda and then the sign rule to obtain partial^C Phi_lambda=G. At lambda=0 or 1, omit the inactive term and obtain the same equality. For lambda>1, the general sum rule gives only partial^C Phi_lambda subset G, which is all that is needed.

We next prove the moving-point gradient limit. Suppose x_j->x and t_j->0. Fix i and an atom a not in Pi_i(x), and choose b in Pi_i(x). There is gamma>0 such that, for all sufficiently large j,

||x_j-a||^2-||x_j-b||^2>=gamma.

Using the b term in the posterior denominator gives

p_{i,a}(x_j,t_j) <= (w_{i,a}/w_{i,b})exp(-gamma/(4t_j))->0.

Since the support is finite, the total posterior mass outside Pi_i(x) tends to zero. Thus dist(m_i(x_j,t_j),conv Pi_i(x))->0. The gradient representation implies

dist(nabla F_lambda(x_j,t_j),G(x))->0.

The multifunction G has nonempty compact convex values. It is upper semicontinuous: if x_j->x, any atom active along a subsequence is active at x, and compactness of the convex coefficients shows that every limit of vectors in G(x_j) lies in G(x). Local boundedness follows from the displayed gradient formula, so this closed-graph verification gives upper semicontinuity. Also every g in G(x) satisfies ||g||<=2(||x||+R_K).

## 3. Identification of Every Time-Shift Limit

Take any locally uniformly convergent subsequence Y^j_s=Y_{tau_j+s}->Z_s. The common Lipschitz bound passes to Z. Put

v_j(s)=nabla F_lambda(Y^j_s,Te^{-(tau_j+s)}).

These functions are uniformly bounded. On bounded intervals, weak-* compactness in L-infinity, followed by a diagonal extraction, gives v_j weak-* converging to a measurable v. The integrated equations yield

Z_b-Z_a=-(1/4)integral_a^b v(s) ds.

For each fixed s, the gradient limit from Section 2 implies dist(v_j(s),G(Z_s))->0. We verify the convex-constraint passage explicitly. On a bounded interval I, C(s)=G(Z_s) is measurable with nonempty compact convex uniformly bounded values. Measurability also follows directly from the finite Borel partition by nearest-atom sets. For a fixed direction q, its support function h(s,q)=sup_{c in C(s)}<q,c> is measurable and bounded. Moreover,

<q,v_j(s)> <= h(s,q)+||q||dist(v_j(s),C(s)).

Multiply by an arbitrary nonnegative function in L^1(I) and integrate. The distance term is uniformly bounded and converges pointwise to zero, so dominated convergence removes it; weak-* convergence passes the other term to the limit. Thus <q,v(s)><=h(s,q) almost everywhere. First impose this for the countably many q in Q^d, obtaining one common full-measure set, and then extend to all directions by continuity. Separation of a point from a closed convex set gives v(s) in C(s) almost everywhere.

Consequently Z'=-v/4 belongs to -G(Z)/4 almost everywhere, with the required integral equation on every bounded interval. In 0<=lambda<=1, G=partial^C Phi_lambda; for lambda>1 it is the prescribed outer subdifferential. The argument began with an arbitrary convergent subsequence, so it identifies every subsequential limit.

## 4. Autonomous Existence, Dissipation, and Convergence

The relevant autonomous field is -G/4 in both regimes, since G equals the Clarke subdifferential in the convex-mixture regime. Section 2 verifies upper semicontinuity, nonempty compact convex values, and the global growth bound ||g||<=2(||x||+R_K). The stated standard existence theorem therefore provides a global solution from every initial point.

Partition Euclidean space into the finitely many nonempty strata Sigma_{I,J} on which Pi_1 and Pi_2 are fixed sets I and J. Let M be the affine hull of a stratum and V its direction space. On that stratum all active Q_ab agree with Phi_lambda. Their pairwise differences are affine and vanish on the stratum, hence on M. Thus their restrictions to M are the same quadratic q_M. Because lambda+(1-lambda)=1, every Q_ab has Hessian 2I, and q_M has Hessian 2I on V. All active gradients therefore have the same projection onto V, namely nabla_M q_M.

If x in the stratum is outer-critical, project 0 in G(x) onto V to obtain nabla_M q_M(x)=0. A strictly convex quadratic on an affine space has at most one critical point, including the zero-dimensional case. Hence each stratum contains at most one outer-critical point, and the outer-critical set is finite. Clarke-critical points form a subset and are finite as well.

Now let Z be any global autonomous solution. On every bounded interval, Phi_lambda composed with Z is absolutely continuous. For a fixed stratum, consider times at which Z lies in that stratum. At almost every such time s, this time set has density one at s, Z and Phi_lambda composed with Z are differentiable, and the differential inclusion holds. Difference quotients along times in the same stratum show Z'_s in V. Along those times Phi_lambda(Z) equals Q_ab(Z), so differentiation gives

(Phi_lambda(Z_s))'=<nabla Q_ab(Z_s),Z'_s>=<nabla_M q_M(Z_s),Z'_s>.

Since -4Z'_s in G(Z_s), projecting this inclusion onto V gives -4Z'_s=nabla_M q_M(Z_s). Therefore

(Phi_lambda(Z_s))'=-4||Z'_s||^2

almost everywhere on the time set of each stratum, hence almost everywhere overall. Integration gives

Phi_lambda(Z_b)-Phi_lambda(Z_a)=-4 integral_a^b ||Z'_s||^2 ds.

This argument applies equally to the outer inclusion at simultaneous interfaces; it does not assume an unrestricted Clarke chain-rule identity.

The potential is coercive for every fixed lambda>=0. Indeed, if all support points have norm at most R and B=lambda+|1-lambda|, expansion using nearest atoms gives

Phi_lambda(x)>=||x||^2-2BR||x||-BR^2.

Dissipation therefore confines Z to a compact sublevel set and bounds its velocity. Its omega-limit set is nonempty and compact; it is connected because it is the nested intersection of the compact connected closures of continuous trajectory tails. The energy decreases to a finite limit ell.

Every omega-limit point is outer-critical. Otherwise, upper semicontinuity supplies a ball B(x,r) and eta>0 with ||g||>=eta for every g in G(y), y in B(x,r). Choose a global velocity bound M>0. At arbitrarily late visits to B(x,r/2), the curve stays in B(x,r) for at least r/(4M) units of forward time. During that interval ||Z'||>=eta/4 almost everywhere, so dissipation decreases the energy by at least eta^2 r/(16M). This contradicts convergence of the energy to ell. Thus the connected omega-limit set lies in the finite outer-critical set and is a singleton. Boundedness then gives convergence of Z to that point. In 0<=lambda<=1, equality of the two subdifferentials makes the limiting point Clarke-critical, as required.

## 5. Local Traps in Both Regimes

The set M_min=Min(Phi_lambda) is nonempty by continuity and coercivity. The Clarke Fermat condition and the sum inclusion imply M_min subset Crit_out(Phi_lambda), so M_min is finite.

Fix p in M_min. Choose r_0>0 sufficiently small that the closed ball around p contains no other outer-critical point and is contained in a neighborhood on which Phi_lambda>=Phi_lambda(p). In fact Phi_lambda(x)>Phi_lambda(p) for every x in that closed ball other than p: an equality point would itself be a local minimizer, hence another outer-critical point. For any 0<r<=r_0 the sphere has the positive energy barrier

m_r=min_{||x-p||=r}Phi_lambda(x)>Phi_lambda(p).

By continuity, choose 0<delta<r such that Phi_lambda(z)<m_r whenever ||z-p||<delta. Dissipation prevents every autonomous solution starting in this delta-ball from ever reaching the r-sphere. Its limit, proved to exist in Section 4, is an outer-critical point in the closed r-ball, hence p. This proves trapping for all lambda>=0, including nonsmooth CFG minimizers.

Conversely, if p is a local trap but not a local minimizer, there are arbitrarily close initial points z with Phi_lambda(z)<Phi_lambda(p). Existence gives an autonomous solution from z; trapping forces its convergence to p, while dissipation and continuity make that impossible. Thus local traps and local minimizers coincide.

For completeness, the stronger local quadratic assertion in the convex-mixture regime follows directly from Phi_lambda=min Q_ab. At a local minimum p, each branch active at p also has a local minimum at p, since Q_ab>=Phi_lambda locally and equality holds at p. Its gradient vanishes and its Hessian is 2I, so Q_ab(x)=Phi_lambda(p)+||x-p||^2. The finitely many inactive branches stay inactive nearby. Hence Phi_lambda has this same quadratic form near p. This stronger assertion is not used or asserted for general CFG minimizers.

## 6. Conditional Transfer to the Original Curve

Assume the stated exclusion of non-minimizing critical points from omega(Y). Compact confinement makes omega(Y) nonempty, compact, and connected. Every forward time-shift limit Z has Z_s in omega(Y) for each fixed s; consequently its limiting critical point also belongs to omega(Y), since this set is closed. The exclusion hypothesis and autonomous convergence therefore force that limit to belong to M_min.

Fix epsilon>0. Consider the components of the open set

O_epsilon={s>0:dist(Y_s,M_min)>epsilon}.

Their lengths are uniformly bounded. If not, choose points s_j->infinity inside components with the right endpoints minus s_j tending to infinity. This is possible for either components of unbounded finite lengths or a component with infinite right endpoint. Extract a forward time-shift limit at s_j. On each fixed forward interval the shifted curves stay farther than epsilon from M_min, so the limiting autonomous curve satisfies dist(Z_s,M_min)>=epsilon for every s>=0. But its limiting critical point belongs to omega(Y) and hence to M_min, a contradiction. Denote the resulting length bound by C_epsilon.

Suppose dist(Y_s,M_min) does not tend to zero. There are epsilon_0>0 and tau_j->infinity with dist(Y_{tau_j},M_min)>epsilon_0. Choose a sufficiently small rho in (0,epsilon_0). By the trapping result and finiteness of M_min, there is a common delta_rho in (0,rho/2) such that every autonomous solution starting at distance less than delta_rho from M_min stays at distance less than rho/2 from M_min for all forward times. Set epsilon=min(rho/2,delta_rho/2).

Let (a_j,b_j) be the component of O_epsilon containing tau_j. The length bound implies a_j>=tau_j-C_epsilon->infinity. For large j, continuity gives dist(Y_{a_j},M_min)=epsilon. Extract a time-shift limit Y_{a_j+ .}->Z. Then dist(Z_0,M_min)=epsilon<delta_rho, so dist(Z_s,M_min)<rho/2 for every s>=0. Uniform convergence on [0,C_epsilon] implies dist(Y_{a_j+s},M_min)<=rho throughout that interval for large j. Since tau_j-a_j lies in [0,C_epsilon], this contradicts dist(Y_{tau_j},M_min)>epsilon_0>rho.

Therefore dist(Y_s,M_min)->0. The nonempty connected omega-limit set is contained in the finite set M_min, hence is a singleton {x_*}. Compactness gives Y_s->x_*. Finally t=Te^{-s} is a bijective time change between t down to zero and s tending to infinity, so X_t->x_* as well.

All theorem-critical obligations listed at the start are closed.
