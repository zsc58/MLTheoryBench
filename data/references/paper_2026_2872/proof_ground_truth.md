# Reference Proof

## Contract and Obligations

The context sequence is exogenous and independent of demand noises and all seller randomization. Conditioning on that sequence is an analytical device, not permission for the policy to see future contexts. Valuations are bounded at every admissible context, and noise is centered. The structural interval supplied with an instance need only contain its actual utility image; it need not be the conservative interval [0,C_theta]. The lower-bound class uses the additional uniform local radius in its definition. Pilot separation is a property of the constructed upper-bound policy, not a restriction on arbitrary policies in the converse.

The theorem-critical obligations are: oracle regularity and local curvature; uniform coarse localization; a feasible polynomial comparator; an unbiased convex-bandit reduction with a normalized, prefix-valid learner; dimension-free scalar pilot confidence and an exploration-count bound; aggregation and parameter optimization; and a centered, admissible lower-bound family with derived oracle shifts, transcript KL, decoding, and hypercube aggregation. The following sections close all these obligations. No paper-specific lemma is used merely by name.

## 1. Oracle Regularity and Curvature

Let U=[u_min,u_max], V=p_max+max{|u_min|,|u_max|}, and r(u,p)=p g(p-u). Continuity and compactness imply continuity of the unique maximizing price: for any u_n tending to u, every subsequential limit of p*(u_n) maximizes r(u,.) and therefore equals p*(u). At an interior maximizer, r_p(u,p*(u))=0. Taylor expansion in price and the quadratic-growth inequalities give

sigma_r <= -r_pp(u,p*(u)) <= L_r.

Set F(u,p)=g(p-u)+p g'(p-u). Its derivative in p is nonzero at every maximizing pair. The usual local implicit-function theorem, including its Holder version, gives p* regularity of order beta-1. For noninteger beta, the standard Taylor-remainder characterization of Holder regularity is used: a C^s function, s=floor(beta), whose degree-s Taylor remainders are uniformly O(|x-y|^beta) has locally alpha-Holder s-th derivative, alpha=beta-s. This characterization applies to the explicit public assumption. For integer beta, C^beta regularity is already assumed. Applying the implicit-function theorem to F therefore gives C^{beta-1} regularity, interpreted in the Holder sense when noninteger. Finitely many local representations cover U and agree on overlaps.

Consequently, after enlarging a finite constant L_p, p* is L_p-Lipschitz and, with m=ceil(beta-1)-1,

|p*(v)-sum_{l=0}^m (p*)^{(l)}(u)(v-u)^l/l!| <= L_p |v-u|^{beta-1}.

The Taylor degree here is m; the learner can have degree q=floor(beta-1), with its extra coefficient set to zero when beta-1 is an integer.

The continuous positive boundary distance of p* has a positive minimum on U. Uniform continuity of r_pp on U times [0,p_max], together with the curvature inequality at p*, supplies rho_0>0 such that every closed rho_0-neighborhood of an oracle lies inside the price interval and -r_pp>=sigma_r/2 there. This proves the required local geometry rather than assuming it for the upper result.

## 2. Coarse Policy and Localization

For target width h in (0,1], let M=ceil((u_max-u_min)/h), bar h=(u_max-u_min)/M, and use equal-width bins, half-open except for the closed last endpoint. Thus M<=C_U/h. Choose a fixed grid spacing delta>0, independent of the horizon, and the grid G={k delta:0<=k<=floor(p_max/delta)} union {p_max}, with duplicates removed. Put rho=sqrt(delta). Each bin initially plays each grid price m_coarse=ceil(m_0 log(eH)) times, in a predetermined order, and then stores a deterministically tie-broken empirical maximizer b_j. Bins that do not complete this schedule remain coarse.

Fix a complete index-pilot stream (N,(u_s,tilde u_s)_{s<=N}) with N<=H, both indices in U, errors at most eta, and the conditional fresh-noise property. Bin assignments and the coarse/refinement time sets are deterministic given this stream. At any fixed grid price, coarse revenues have independent fresh demand noise, are bounded by p_max, and have means r(u_s,p). Hoeffding, or bounded martingale concentration, followed by a union bound gives, with conditional probability at least 1-C M|G|H^{-5},

|hat r_j(p)-r(u,p)| <= Delta := C_mean p_max[m_0^{-1/2}+L_g(h+eta)]

for every completed bin, p in G, and u in its closure. The deterministic bias follows from |u-u_s|<=h+eta and |partial_u r|<=p_max L_g.

Take a sufficiently small numerical c_0 and fixed delta,m_0 satisfying

delta <= c_0 min{1,rho_0^2,sigma_r/L_r},

m_0 >= p_max^2/(c_0 sigma_r^2 rho^4).

Require, for the current run,

h,eta <= c_0 sigma_r rho^2/(L_g p_max),

h^{beta-1} <= rho/(8L_p), and L_p eta <= rho/8.

These choices ensure Delta<=sigma_r rho^2/512. Any grid point at distance at least rho/8 from p*(u) loses at least sigma_r rho^2/128 in true revenue. A grid point within delta of p*(u) loses at most L_r delta^2/2<=sigma_r rho^2/512. Their empirical values are therefore strictly ordered against the distant point. Uniformity of the concentration event implies |b_j-p*(u)|<=rho/8 for every u in the bin closure. Let E_coarse be the joint event for all bins entering refinement.

All coarse calls, including incomplete bins, cost at most p_max M|G|m_coarse. On E_coarse's complement the policy still projects prices onto [0,p_max], so the total failure contribution is at most C p_max N M|G|H^{-5}.

## 3. Polynomial Comparator and the Convex-Bandit Learner

Let psi(z)=(1,z,...,z^q), q=floor(beta-1). In bin j with midpoint u_j, define

Q_j(v;a)=a^T psi(2(v-u_j)/bar h),

A_j={a:sup_{|z|<=1}|a^T psi(z)-b_j|<=rho/4}.

At each refinement visit a fresh bin-specific learner selects a from A_j using only that bin's past coefficient-feedback pairs and fresh refinement randomization. Post the projected polynomial price and return raw feedback ell=-p y. The learner is not told its eventual visit count.

Use the degree-m Taylor polynomial of p* at u_j, represented in this basis and padded with zeros through degree q. Its error at every v in the bin is at most L_p h^{beta-1}<=rho/8. Localization therefore puts its coefficient vector a_j^cmp in A_j. For a played true-pilot pair,

|Q_j(tilde u;a_j^cmp)-p*(u)| <= L_p(h^{beta-1}+eta),

so its revenue loss is at most C(h^{2beta-2}+eta^2). Its prices are admissible because they are within rho/8 of p*(tilde u).

For any a in A_j, localization and the pilot bound give

|Q_j(tilde u;a)-p*(u)| <= rho/4+rho/8+L_p eta <= rho/2<=rho_0.

Thus projection is inactive on E_coarse, and the coefficient loss L_k^j(a)=-r(u_s,Q_j(tilde u_s;a)) is convex. Finite-dimensional norm equivalence gives constants c_q,C_q>0 with

c_q||a||_2 <= sup_{|z|<=1}|a^T psi(z)| <= C_q||a||_2.

Hence A_j is compact, convex, and contains a ball of radius rho/(4C_q) about a_ctr=(b_j,0,...,0), while lying in the concentric ball of radius rho/(4c_q).

Condition analytically on the whole index-pilot stream and all coarse observations. This fixes the action sets, refinement times, visit counts n_j, and loss sequences. It does not reveal the losses or future indices to any learner. Fresh demand noise and local adaptation imply

E[ell_k^j | this background, past local history, a_k^j]=L_k^j(a_k^j).

All coarse observations may be included even when their global times are later than a refinement call: coarse prices and times are fixed by the pilot stream, and their demand noises are disjoint from refinement noises. The constructed learner does not use other bins' observations.

The independent BCO theorem used here is the following relevant statement. On a compact convex set A in R^{d_b} with B_2(1) contained in A contained in B_2(D), given the required action-set oracle access, fixed or background-measurable convex G-Lipschitz losses A->[0,1] and conditionally unbiased noisy value feedback with a universal conditional sub-Gaussian proxy admit a horizon-n learner with conditional probability at least 1-delta of regret at most C d_b^{7/2}sqrt(n) polylog(n,d_b,D,1+G,1/delta). At delta=(en)^{-2}, expected conditional regret has the corresponding bound without 1/delta: regret is at most n, so the failure contribution n delta is bounded. This general independent result is theory_017, stated in the source at lines 1905-1923. Its use is not an assumption of the public pricing problem.

To verify all its hypotheses, transform coefficients by a_bar=4C_q(a-a_ctr)/rho. The transformed set contains the unit ball and lies in B_2(C_q/c_q). It has the required fixed-dimensional oracle access: maximize the explicit univariate polynomial on [-1,1] to check membership; a violating maximizer also gives a separating linear inequality. Shift and scale losses and feedback by (value+p_max)/p_max. Both now lie in [0,1], and their difference is bounded by one and conditionally mean zero, hence conditionally sub-Gaussian. Convexity is preserved. Since |r_p|<=1+p_max L_g and ||psi||<=sqrt(q+1), the normalized Lipschitz constant is at most

G_q=(1+p_max L_g)sqrt(q+1)rho/(4C_q p_max).

It is structural and independent of h, bin number, visit count, and context dimension. Raw regret is exactly p_max times normalized regret.

For an anytime implementation, use independent fresh copies with epoch lengths 1,2,4,... and respective failure levels (e 2^r)^{-2}. Regret against one comparator over all visits is at most the sum of the epoch regrets, because the sum of epochwise minimum losses is no larger than the minimum of their sum. For a final incomplete epoch, append zero losses and deterministic zero feedback to its preset length. This does not change the real prefix actions or its regret, so the horizon guarantee applies to that prefix. Conditional on preceding epochs, losses are still fixed and future feedback is still unbiased. The geometric sum of sqrt(2^r) is O(sqrt(n_j)). Thus every stopped bin has conditional expected raw learning regret at most C sqrt(n_j) polylog(H,beta). This explicitly closes the normalization and unknown-bin-horizon obligations.

Insert the feasible comparator in each bin's regret decomposition. Sum the approximation losses and use sum_j sqrt(n_j)<=sqrt(M sum_j n_j)<=sqrt(MN). Together with the coarse and failure costs, this proves

E[R_N | index-pilot stream] <= C |G|m_0 log(eH)/h + C_BCO sqrt(N/h) polylog(H,beta) + C N(h^{2beta-2}+eta^2).

The failure term is absorbed in the coarse term. If N=0, the pricing regret is zero; empty refinement bins contribute zero throughout.

## 4. Scalar Pilots: the Dimension-Free Source Argument

Use A_t=I+sum_{tau<t, exploration} c_tau c_tau^T and hat theta_t=A_t^{-1}sum_{tau<t, exploration}p_max y_tau c_tau. Put C_w=32(C_theta+p_max)sqrt(log(eT)) and explore exactly when C_w||c_t||_{A_t^{-1}}>eta. Exploration prices are fresh uniforms independent of the past and all demand noises. Otherwise, pass proj_U(c_t^T hat theta_t) to the pricing module. Pricing observations never update the pilot.

For bounded v and independent uniform P, E[p_max 1{v>=P}|v]=v. Centered noise then gives E[z_tau|c_tau]=c_tau^T theta. Write zeta_tau=z_tau-c_tau^T theta; these are bounded centered exploration errors. Conditional on the complete exogenous context sequence, exploration indicators and every A_t are deterministic. Therefore

hat theta_t-theta=-A_t^{-1}theta+A_t^{-1}sum c_tau zeta_tau.

The ridge bias in the c_t prediction is at most C_theta||c_t||_{A_t^{-1}}. For each t, the weights b_tau=c_t^T A_t^{-1}c_tau are deterministic under this conditioning, and

sum b_tau^2=c_t^T A_t^{-1}(A_t-I)A_t^{-1}c_t <= ||c_t||_{A_t^{-1}}^2.

Scalar weighted Hoeffding concentration gives a stochastic prediction error at most C(p_max+C_theta)sqrt(log(eT))||c_t||_{A_t^{-1}} with failure probability O(T^{-4}). Union bound over t gives the simultaneous radius C_w||c_t||_{A_t^{-1}} with failure O(T^{-3}). This is the source's scalar argument; generic self-normalized vector concentration is not substituted, since its usual dimension factor would not establish this claim. Projection cannot increase error because true utility belongs to U. Thus all nonexploration pilots are eta-accurate on the confidence event.

For completeness, the exploration-count dependency theory_018 has an elementary proof. Let epsilon=eta^2/C_w^2. At selected observation i, leverage x_i=c_i^T A_i^{-1}c_i is greater than epsilon and at most one. For epsilon>=1 no observation is selected. Otherwise the matrix determinant lemma and log(1+x)>=x/2 for 0<=x<=1 imply

n epsilon/2 <= log det A_{n+1} <= d log(1+n/d) <= d log(1+T/d).

The middle inequality follows from trace A_{n+1}<=d+n and arithmetic-geometric mean of its eigenvalues. Hence n<=2d C_w^2 eta^{-2}log(1+T/d)=~O(d eta^{-2}). Repeated observations are included in the sum, as in the ridge design. This suffices without leaving any specialized core-set citation unresolved.

Given the complete contexts, the exploration and pricing noise families are disjoint independent iid families. Exploration uniforms and pricing refinement seeds are independent. The entire pilot stream, its call indices, and its length depend only on contexts and exploration-side variables. Conditional on this stream, the pricing noises therefore retain their iid law and the refinement seeds remain fresh. The confidence event is also exploration-side measurable. Its conditioning does not alter the pricing noise law. This proves the exact conditional separation required above.

## 5. Integrated Upper Bound and Its Regime

Exploration regret is at most p_max n. Apply the conditional pricing bound on the confidence event with H=T and N<=T. Its complement contributes at most O(p_max T^{-2}). With h=T^{-1/(4beta-3)}, the learning and approximation terms balance at T^{(2beta-1)/(4beta-3)}, and the coarse term has the smaller exponent 1/(4beta-3). Therefore

E R_T=~O(T^{(2beta-1)/(4beta-3)}+T eta^2+d eta^{-2}).

Choose eta=(d/T)^{1/4}. The last two terms are both sqrt(dT), up to suppressed logarithms.

To make the public regime explicit without exposing localization machinery, first choose fixed valid delta and m_0 using the positive instance-wise rho_0. Define privately

h_* = min{1, c_0 sigma_r rho^2/(L_g p_max), (rho/(8L_p))^{1/(beta-1)}},

eta_* = min{1/2, c_0 sigma_r rho^2/(L_g p_max), rho/(8L_p)}.

All required inequalities hold when T>=A:=max{1,h_*^{-(4beta-3)}} and T>=Bd with B:=eta_*^{-4}. Increasing A absorbs fixed small-horizon and concentration constants. These positive thresholds depend only on fixed structural tuning, not the context sequence or horizon. This proves the repaired asymptotic upper statement, preserving the source's instance-wise tuning qualification.

On the normalized class, the common radius 1/16 permits common delta,m_0. Bounds on the oracle Lipschitz and Taylor constants are also uniform: implicit differentiation and the stated derivative bounds, together with -r_pp>=sigma_r at the maximizer, control the implicit-function constants. Thus the policy and thresholds are uniform there. For any other fixed dimension, the scalar hard instances embed as contexts (c,0,...,0) and theta=(1,0,...,0); no additional information is conveyed. The fixed-dimensional interpretation of the matching horizon exponent follows.

## 6. Lower-Bound Family and Membership

Work first in auxiliary coordinates x. Let B=31/32 and C_loc=1/32. Start with the truncated-linear tail g_uni(z)=1 for z<=0, 1-z/B on [0,B], and 0 for z>=B. A smooth baseline g_0 can equal this tail on I_glob=[1/8,7/8] and approximate it uniformly within a sufficiently small fixed epsilon_0. To construct it, smooth the constant density near each support endpoint, keeping its integral on each boundary interval equal to that interval's length divided by B. A nonnegative interior smooth bump corrects the lost mass. Keep the density exactly 1/B elsewhere and integrate it to obtain g_0. It is a smooth monotone tail supported on [0,B], with the asserted exact central linearity.

For w=gamma T^{-1/(4beta-3)}, let M=floor(1/(64w)), x_j=2jw, p_j^0=(B+x_j)/2, and z_j=B/2-jw. Choose a fixed smooth odd bump phi supported in [-1/8,1/8], with phi(0)=0 and phi'(0)=1. Define

g_omega(z)=g_0(z)+kappa w^beta sum_{j=1}^M omega_j phi((z-z_j)/w).

The intervals J_j=[z_j-w/8,z_j+w/8] are disjoint. Derivatives of order k have perturbation sup norm at most C_k kappa w^{beta-k}. If beta=s+alpha is noninteger, the order-s derivative has alpha-Holder seminorm O(kappa): on one bump use scaling; between distinct bumps the separation is at least 3w/4 and use the sup bound. These bounds imply the public Taylor-remainder condition. If beta is integer, a bounded beta-th derivative gives a degree-(beta-1) remainder O(|x-y|^beta), and subtracting the beta-th Taylor term gives the required degree-beta remainder of the same order. Monotonicity and range are preserved by small kappa: on bump supports g_0'=-1/B and g_0 stays a fixed distance from zero and one; outside them nothing changes.

We verify revenue geometry uniformly for auxiliary x in [-1/32,1/32]. The unperturbed truncated-linear revenue has unique optimum (B+x)/2 in [15/32,1/2]. There is a fixed positive revenue gap outside I_curv=[3/8,19/32], by compactness and uniqueness. Inside I_curv, every price-gap lies in the central linear strip, so baseline curvature is -2/B. Choose epsilon_0 below one eighth of the outside gap. The smoothed baseline retains that gap and agrees exactly with the quadratic revenue on I_curv. Derivative perturbation bounds, including w^{beta-2}<=1, imply for small kappa

-4/B <= r_omega,pp(x,p) <= -1/B on I_curv.

Baseline price derivatives at 7/16 and 17/32 have respectively uniformly positive and negative margins. Perturbations preserve these signs, so there is exactly one stationary maximizer in I_sign=(7/16,17/32). Small sup perturbations preserve the outside gap, making it the unique global maximizer. Inside I_curv, integrating curvature twice bounds its loss between (p-p*)^2/(2B) and 2(p-p*)^2/B. Outside I_curv, distance from I_sign is at least 1/16; a fixed positive outside loss gap and the trivial loss bound of one give uniform lower and upper quadratic growth. Its closed 1/16-neighborhood lies inside I_curv and inside (0,1), giving the required common local-concavity radius.

At the baseline optimum, r_omega,p(x,p_0*(x))=O(kappa w^{beta-1}). The curvature mean-value theorem consequently gives a uniform displacement O(kappa w^{beta-1}). At grid point x_j the derivative is exactly

r_omega,p(x_j,p_j^0)=kappa p_j^0 omega_j w^{beta-1}.

The same curvature bounds imply constants a_1,a_2>0, independent of T,j,omega, such that

a_1 w^{beta-1} <= omega_j[p_omega*(x_j)-p_j^0] <= a_2 w^{beta-1}.

Finally, each odd perturbation has zero integral. All auxiliary laws X therefore have the same mean mu_0=int_0^B g_omega(z) dz. Use actual centered noise X-mu_0, actual contexts c_j=mu_0+x_j, theta=1, and iid uniform draws from these M contexts. The centered tail is bar g_omega(z)=g_omega(z+mu_0). Since 0<=mu_0<=B and 0<x_j<=1/32, the actual contexts are in [0,1]. Valuations equal x_j+X and are in [0,1] almost surely. Revenue is unchanged by centering: p bar g_omega(p-c_j)=p g_omega(p-x_j). The supplied interval [mu_0,mu_0+1/32] satisfies all structural conditions uniformly, including the 1/16 radius. Giving the common centering constant and this interval to the policy cannot invalidate a lower bound. This closes membership on the full supplied interval, not only on observed grid points.

## 7. Transcript KL, Decoding, and Aggregation

Continue in the auxiliary coordinates, which are a common observed translation in every environment. Let P_omega be the full transcript law, augmenting it by the policy's independent seeds if necessary. Put Delta_t^omega=r_omega(x_t,p_omega*(x_t))-r_omega(x_t,p_t), and define the deterministic expected local regret

R_j^omega=E_omega sum_t Delta_t^omega 1{x_t=x_j or p_t-x_t in J_j}.

Each round belongs to at most one context cell and one bump interval, so sum_j R_j^omega<=2 E_omega R_T.

For paired environments differing only in sign j, the contexts and policy kernels have the same laws. The adaptive KL chain rule therefore gives

KL(P_omega,P_omega^(j))=sum_t E_omega kl(Ber(g_omega(p_t-x_t)),Ber(g_omega^(j)(p_t-x_t))).

The summand is zero outside J_j. Within J_j, both means are bounded away from zero and one. The elementary Bernoulli bound kl(q,q')<=(q-q')^2/[q'(1-q')] gives a constant times squared mean difference.

If x_t=x_j, phi(0)=0 and bounded phi' give a mean difference at most C w^{beta-1}|p_t-p_j^0|. Squaring and inserting the oracle yields

kl_t <= C w^{2beta-2}Delta_t^omega + C w^{4beta-4}.

If x_t=x_k with k!=j and the query gap is in J_j, distinct baseline gap centers differ by at least w. The query price is at least 7w/8 from its baseline optimum; the uniform oracle displacement is at most w/8 after reducing kappa. Thus its distance from its true optimum is at least 3w/4, and Delta_t^omega>=c w^2. The mean difference is at most C w^beta, so kl_t<=C w^{2beta-2}Delta_t^omega. These two cases also cover exploratory queries on other context cells, which cannot be discarded from the transcript.

For large T, M is between 1/(128w) and 1/(64w). Thus E N_j=T/M<=128Tw. Summing the pointwise bounds gives

KL(P_omega,P_omega^(j)) <= C_kl w^{2beta-2}R_j^omega + C_kl T w^{4beta-3},

and the reverse bound holds with R_j^omega^(j).

Decode sign j by the majority of its observed prices relative to p_j^0, assigning +1 on a tie. Its count N_j is Bin(T,1/M); Chernoff gives P(N_j<c_0Tw)<=exp(-c_1Tw). A wrong decoder has at least half of the cell prices on the wrong side of p_j^0. The signed oracle displacement and quadratic growth then charge at least cTw^{2beta-1} regret on the event of a wrong decode and sufficient count. Consequently

P_omega(decoder error) <= exp(-c_1Tw)+C_dec R_j^omega/(Tw^{2beta-1}).

This also handles the opposite sign; zero-count ties are covered by the count failure event.

For any two transcript laws P,Q and event E, the independent testing inequality is P(E)+Q(E^c)>=(1/2)exp(-KL(P,Q)). It follows, for example, from the affinity A(P,Q)>=exp(-KL(P,Q)/2), the Cauchy-Schwarz total-variation bound TV(P,Q)<=sqrt(1-A(P,Q)^2), and 1-sqrt(1-z)>=z/2. Apply it in both directions to the decoder's complementary error events and take their geometric mean.

If S_j=R_j^omega+R_j^omega^(j)<=alpha Tw^{2beta-1}, the sum of directed KLs is at most C_kl(alpha+2)T w^{4beta-3}=C_kl(alpha+2)gamma^{4beta-3}. Take alpha=1/(16C_dec), then gamma small enough to make this at most log 4. The two error probabilities must sum to at least 1/4. The decoder bounds instead give at most 2exp(-c_1Tw)+1/16<=1/8 for large T, since Tw tends to infinity. This contradiction proves S_j>=c_*Tw^{2beta-1} uniformly in j and omega.

Average over all signs. The sign-flip bijection gives average R_j^omega>=c_*Tw^{2beta-1}/2. Sum over M cells and use the factor-two aggregation bound to obtain

2^{-M}sum_omega E_omega R_T >= c M T w^{2beta-1} >= c' T w^{2beta-2}.

Substitution of w gives c_beta T^{(2beta-1)/(4beta-3)}. Hence, for every policy and every sufficiently large T, some normalized instance, which may depend on that policy and T, attains the lower bound. This is exactly the stated supremum and minimax quantifier order. All its constants and structural bounds are independent of T. Together with the uniform upper guarantee on this class, this proves the claimed fixed-dimensional horizon sharpness.
