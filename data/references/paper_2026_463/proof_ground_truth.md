# Reference Proof

## Contract and Source Corrections

The posterior in this task is the Bayes posterior of the specified mixture experiment. It is not assumed to be the terminal transition kernel of the CTMC obtained by posterior averaging. The source's backward equation is valid for a genuine CTMC transition kernel, but its identification with this mixture posterior is not generally valid. The proof below uses the stated derivative supremum directly and never assumes L_k^p≤DM_k.

The auxiliary process must floor the entire gated second-stage factor, not merely its posterior component. Otherwise oracle paths with further changes of an already changed coordinate can have zero auxiliary probability. The auxiliary process need not have total rate bounded by DM_k; the two-jump probability below is always evaluated under the oracle law. A floor capped at 1 handles all finite values of L_k^p. These corrections do not change either sampler.

The public task explicitly specifies ε_Est^{LC}∈[0,∞). Together with E_θK(θ)=2(ε_Est^{LC})^2, this selects the nonnegative estimation-error magnitude rather than an arbitrary signed square root.

## Step 001: Initialization and the Oracle Marginal

For fixed u and coordinate d, put f_t^d(b|u^d)=(1-κ_t)ρ_d(b)+κ_t1{b=u^d}. Its conditional generator is

G_t^{u,d}(b,a)=α_t(1{a=u^d}-1{a=b}).

Direct summation gives

∑_b f_t^d(b|u^d)G_t^{u,d}(b,a)=α_t(1{a=u^d}-f_t^d(a|u^d))=κ̇_t(1{a=u^d}-ρ_d(a))=∂_t f_t^d(a|u^d).

Let G_t^u be the sparse joint generator that changes one coordinate using these coordinate generators. Differentiating the finite product c_t(x|u)=∏_d f_t^d(x^d|u^d) proves ∂_t c_t(·|u)=c_t(·|u)G_t^u. This supplies the product-generator argument without relying on an unproved internal proposition.

Now differentiate p_t(z)=∑_u p_1(u)c_t(z|u) and exchange finite sums. Bayes' formula yields

∂_t p_t(z)=∑_x ∑_u p_1(u)c_t(x|u)G_t^u(x,z)=∑_x p_t(x)Q_t(x,z).

When p_t(x)=0, every nonnegative p_1(u)c_t(x|u) is zero, so the same identity is independent of the posterior version chosen there. Also p_{t=0}=p_0. The finite-state forward equation with continuous bounded coefficients has a unique solution: subtracting two solutions and applying the integral inequality for their norm proves uniqueness. Thus the oracle CTMC has marginal p_t. This also explicitly proves the posterior-averaging background fact needed from the external citation.

All actual oracle and sampler rates have total exit rate at most Dα_t≤DM_k on I_k, because each posterior vector is normalized and the second-stage gates only delete rates. Consequently all these processes are nonexplosive on the finite horizon. They all have the same initial law, independent of θ.

## Step 002: Jump-Process and Information Identities

For predictable finite-state rates bounded in total by a deterministic constant C, use a rate-C Poisson process and, at each arrival, choose a jump to z with probability q_s(z)/C and otherwise remain in place. Conditional on the history, thinning gives the specified intensities and the identity

E[∑_{actual jumps s} H_s(Y_s)]=E[∫∑_{z≠Y_{s-}} H_s(z)q_s(z) ds]

for nonnegative predictable H. The Poisson count dominates the actual jump count. This construction and conditional expectation identity recover the uniformization and compensator facts used below. The finite-jump integral identity follows by summing the actual jump increments; no separate specialized stochastic-calculus result is needed.

Before the next jump, the history is fixed. Integrating its total exit intensity λ gives survival probability exp(-∫λ). Multiplying successive survival factors and jump intensities gives the path density, for initial state x_0, jump times s_1<⋯<s_n and successive states x_1,…,x_n:

p_0(x_0) exp(-∫_0^H λ_s ds) ∏_{j=1}^n q_{s_j}(x_{j-1},x_j),

where every rate is evaluated on the corresponding past history. These densities sum and integrate to one because the processes are constructed and nonexplosive.

For two such laws R and S with the same initial law and numerator support contained in denominator support, taking the logarithm of their density ratio and using the compensator identity gives

KL(R||S)=E_R[∫_0^H ∑_{z≠Y_{s-}} D_F(q_s^R(z)||q_s^S(z)) ds].

This also verifies normalization of the likelihood ratio, rather than merely identifying a local martingale. The expectation is under R, not S. The formula extends with the stated zero conventions. For estimation, finiteness of K(θ) implies that numerator-positive, denominator-zero jumps have zero oracle probability: their compensator integral vanishes. Since both processes have bounded total intensities, their survival factors are positive. This supplies the required absolute continuity for almost every θ. Negative parts of the expected jump log ratio are integrable because a log(a/b)≥-b/e; finiteness of the divergence then justifies the remaining expectation.

The information inequalities used here require no paper-specific premise. Mapping a path to its endpoint cannot increase KL, by conditioning the likelihood ratio and Jensen's inequality. For completeness, partitioning any two laws by an event gives binary relative entropy as a lower bound on their KL. For fixed second Bernoulli parameter b, the second derivative of binary relative entropy in its first parameter a is 1/[a(1-a)]≥4; its value and first derivative vanish at a=b. Hence binary KL≥2(a-b)^2. Taking the supremum over events proves TV(R,S)≤sqrt(KL(R||S)/2), including boundary cases by limits.

The interval chain rule follows directly by factoring the path density into its interval conditional densities. If a conditional interval KL is uniformly bounded by C_k for every common interval-start state, the whole-path KL is at most ∑_k C_k. Different numerator laws may induce different interval-start distributions; uniformity makes the bound valid for each of them.

## Step 003: Scalar Bounds and Posterior Variation

For a≥0 and b≥ε>0, write D_F(a||b)=a log(a/b)-a+b. If a≥b, this is at most a log(a/ε); if a<b, it is at most b. This proves the first scalar bound used in the source.

If a,b≥ε, the integral remainder formula and F''(u)=1/u give D_F(a||b)≤(a-b)^2/(2ε). If 0≤a≤ε≤b, then a log(a/b)≤0, so D_F(a||b)≤b-a.

We need the following precise floored version. Let c,d∈[0,1], |c-d|≤r, and b=d∨ε with 0<ε≤1. If c≥ε, then |c-b|≤r and the preceding quadratic estimate applies. If c<ε, then b≥c and b-c≤r+ε. Therefore

D_F(c||d∨ε)≤max{r^2/(2ε),r+ε}.

Also D_F(c||c∨ε)≤ε. When 0≤c≤1 and ε≤b≤1, the first scalar bound yields D_F(c||b)≤1∨log(1/ε). Finally, D_F(c||1)≤1. Homogeneity gives D_F(αc||αb)=αD_F(c||b), with both sides zero when α=0.

For a fixed location and an off-diagonal coordinate value, the mean value theorem and the task's derivative supremum give |r_s^d(a|x)-r_v^d(a|x)|≤L_k^p|s-v| for s,v∈I_k. This is all the posterior time regularity required. The CTMC backward equation is not used for the mixture posterior. At p_t(x)>0 its derivative can instead be obtained directly by differentiating Bayes' formula:

∂_t r_t(u|x)=[p_1(u)∂_t c_t(x|u)-r_t(u|x)∂_t p_t(x)]/p_t(x),

with coordinate posteriors obtained by summation. A genuine terminal CTMC kernel h_t satisfies the separate backward identity by Chapman-Kolmogorov; that identity does not identify h_t with r_t.

## Step 004: A Support-Dominating Auxiliary Process and the Oracle KL

Fix an interval k and a common initial state. Suppress the subscript k temporarily, and put m=|S|, h=τDM and r=τL^p. If M=0, every actual rate on this interval is zero and the interval is exact; omit it from all comparisons. Suppose M>0, so h>0. Define

e=max{h^2,r}, ε=min{1,e}, and ℓ_h=max{1,log(h^(-2))}.

On a canonical history, define auxiliary off-diagonal rates on Hamming-neighbor transitions by

Q_s^ε(x,x^{d→a})=α_s[r_s^d(a|x)∨ε] before its first jump,

Q_s^ε(x,x^{d→a})=α_s[(1{x^d=y^d}r_s^d(a|y))∨ε] after its first jump, with first-jump anchor y.

Other off-diagonal rates vanish and diagonals are row sums with a minus sign. The auxiliary uses the current time s in both stages. The gate is inside the floor. Its total exit rate is at most D(m-1)M, so it exists and is nonexplosive. It dominates every Hamming-neighbor transition whenever α_s>0; when α_s=0, all compared rates vanish.

Let P_k be the oracle interval law and P_k^ε the auxiliary interval law. Under P_k, the number of actual jumps is dominated by a Poisson variable of mean h. If E_k is the event of at least two actual jumps, then

P_k(E_k)≤P(Poisson(h)≥2)≤E[N(N-1)]/2=h^2/2≤h^2.

The Poisson factorial moment equals h^2 by direct summation. This estimate is under P_k, not P_k^ε.

On E_k^c, before the first jump the auxiliary posterior equals the current oracle posterior up to flooring. After the first jump there is no further state change, so x=y and every gate equals one. Thus the same statement remains true throughout the interval. With at most D(m-1)≤Dm neighbor transitions, the integrated divergence is at most τDmMε=mhε on E_k^c.

On E_k, every normalized oracle factor lies in [0,1] and every auxiliary factor lies in [ε,1]. The scalar bound controls the entire integrated divergence by mh[1∨log(1/ε)]. Hence, uniformly in the initial state,

A_k:=KL(P_k||P_k^ε)≤mhε+mh^3[1∨log(1/ε)].

If e≤1, then ε=e≥h^2, so A_k≤mhe+mh^3ℓ_h≤mhe(1+ℓ_h). If e>1, then ε=1 and every auxiliary neighbor factor equals one. The sharper direct bound is A_k≤mh≤mhe.

## Step 005: The Location-Corrected KL and the Floor Choice

Let P_k^{LC} be the oracle location-corrected interval law, with the same initial state. Compare its rate with the auxiliary rate on the same canonical history.

Before the first jump, the unfloored factors differ only between t_{k-1} and s, at the same location, so their difference is at most r. After the first jump, if the coordinate gate is one, its current coordinate equals the anchor coordinate. Therefore the candidate a is off-diagonal at the anchor, and the difference between posterior evaluations at T_k and s is again at most r. If the gate is zero, both unfloored factors are zero; the divergence against the auxiliary floor is ε. These statements hold even on paths with multiple later jumps.

Applying the floored scalar inequality, homogeneity, the count of neighbor states, and the likelihood identity gives

B_k:=KL(P_k^{LC}||P_k^ε)≤mh max{r^2/(2ε),r+ε}.

If e≤1, then ε=e≥r and B_k≤2mhe. If e>1, use D_F(c||1)≤1 directly to obtain B_k≤mh≤mhe. In particular, writing u_k=mhe, both cases give

A_k+B_k≤u_k(3+ℓ_h).

The source's uncapped choice is valid in the e≤1 case. The cap and elementary e>1 case are necessary because the mixture construction does not imply the asserted universal bound L_k^p≤DM_k. No such extra hypothesis is imposed.

## Step 006: Interval Assembly, Estimation, and Degenerate Cases

Concatenate the auxiliary interval kernels, starting from p_0. The interval estimates are uniform in the initial state, and each interval restarts its first-jump memory. The path-density chain rule therefore gives

KL(P||P^ε)≤∑_k A_k, and KL(P^{LC}||P^ε)≤∑_k B_k.

Endpoint data processing, Pinsker, and the triangle inequality yield

TV(p_H,p_H^{LC})≤sqrt((∑A_k)/2)+sqrt((∑B_k)/2)≤sqrt(∑(A_k+B_k)).

The last inequality follows by squaring and using 2sqrt(ab)≤a+b. Since h≤log 2<1, J=log(h^(-2))>0 and

3+max{1,J}≤2(2+J).

Also

u_k=|S|h max{h^2,τ_kL_k^p}=|S|(D^3τ_k^3M_k^3∨Dτ_k^2M_kL_k^p).

Consequently the discretization contribution is at most

[2|S|∑_{k:M_k>0}(D^3τ_k^3M_k^3∨Dτ_k^2M_kL_k^p){2+log((τ_kDM_k)^(-2))}]^(1/2).

For almost every estimator realization θ, the common-initial-law likelihood identity established above gives KL(P^{LC}||P̂_θ^{LC})=K(θ). Therefore

E_θ TV(p_H^{LC},p̂_{H,θ}^{LC})≤E_θ sqrt(K(θ)/2)≤sqrt(E_θK(θ)/2)=ε_Est^{LC}.

The second inequality is Jensen's inequality. The final equality follows from E_θK(θ)=2(ε_Est^{LC})^2 and the explicitly stated domain ε_Est^{LC}≥0; without that domain the square root would equal |ε_Est^{LC}|. The oracle law is independent of θ as required by the source experiment. Combining this with the discretization estimate proves the task.

If M_k=0, α vanishes on I_k and both oracle and estimated samplers stay fixed there, so omitting that interval is exact even if a posterior version at a null state varies in time. If every M_k=0, the discretization contribution is zero. If |S|=1, all jump sums and estimation divergences vanish and every terminal distribution is the same point mass. Zero posterior entries require no positivity assumption because the auxiliary floor supplies comparison support and the estimation assumption supplies the required almost-sure support domination.

## Obligation Closure

The mixture-to-oracle marginal identity, initialization, predictable process construction, nonexplosion, likelihood normalization, support conditions, scalar inequalities, both interval KL estimates, clipping cases, interval assembly, information inequalities, estimation expectation order and nonnegative normalization, and zero/empty cases have all been derived or explicitly verified above. There is no unresolved private reference-proof obligation.
