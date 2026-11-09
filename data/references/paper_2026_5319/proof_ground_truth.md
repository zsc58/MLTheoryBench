# Reference Proof

Throughout, constants denoted by c or C are universal and may increase. Fix a deterministic p with d=gamma_min^p>0. If the admissible set of trimming levels is empty, the public right-hand side is infinite. If SAHK=1 there is only one action and regret is zero. Hence assume SAHK>=2, so L>=log 2 and Lambda=200L>=1. Positive contextual gaps are at most H, so 0<d<=H.

The proof uses the same retained/trimmed clipped-surplus architecture throughout. In the count estimate, direct and propagated envelopes must be kept separate. The former assertion log(CSAH^5/d)<=C ell(SAH Lambda/d) is false and is not used.

## 1. Sampling, completed batches, and concentration

Let m_h^k(s,a) be the number of visits before episode k and put n_h^k(s,a)=max{N_h^k(s,a),1}. The completed batch sizes are 1,1,2,4,... . Inspection of consecutive boundaries gives

n_h^k(s,a)>=max{m_h^k(s,a),1}/4.

The cached denominator is a completed-batch size, not a cumulative count.

Represent transitions by independent iid tapes, one for each triple, with law P_h(.|s,a). Visits expose consecutive tape entries; completed batches occupy deterministic consecutive positions. The context sequence is independent of these tapes. Conditional on that sequence, at most K optimal continuation vectors are fixed, and the tapes remain iid. This does not condition on adaptive visit times.

We use these bounded-iid concentration statements. For observations in [0,H], mean mu, variance sigma^2, and sample size n, Bennett's inequality gives

|bar X-mu|<=sqrt(2 sigma^2 u/n)+Hu/n

with failure probability at most 2 exp(-u). For n>=2, empirical Bernstein gives, with the same failure bound,

|bar X-mu|<=sqrt(2 hat sigma^2 u/(n-1))+7Hu/(3(n-1)).

Their boundedness and iid hypotheses hold for each fixed tape batch and conditioned optimal-value vector. A standard-deviation comparison follows locally as well. Apply Bennett to (X-mu)^2, whose variance is at most H^2 sigma^2. The resulting inequality implies

|sqrt(n^{-1}sum_i(X_i-mu)^2)-sigma|<=C H sqrt(u/n).

Indeed, when sigma is at most a constant times H sqrt(u/n), use the upper bound on the empirical second moment; otherwise divide the second-moment error by the sum of square roots. The triangle inequality for empirical L2 norms and |bar X-mu| then give

|hat sigma-sigma|<=C H sqrt(u/n).

For u/n>=1 this also follows directly from boundedness.

Union bounds over triples, coordinates, completed batches, and the at most K conditioned optimal vectors, using a sufficiently large universal multiple of L, give simultaneous coordinate, true-variance, and standard-deviation bounds with failure probability at most delta/4. In particular,

|(hat P-P)V^*|<=C sqrt(v Lambda/n)+C H Lambda/n,

|sqrt(Var(hat P,V^*))-sqrt(v)|<=C H sqrt(Lambda/n),

where v=Var(P,V^*). Centering an arbitrary X in [0,H]^S at PX and using coordinate concentration and Cauchy-Schwarz gives simultaneously for all such X

|(hat P-P)X|<=C sqrt(S Var(P,X)Lambda/n)+C SH Lambda/n.

Consequently this last estimate applies to adaptive optimistic vectors. Analogous bounds for vectors in [0,H^2]^S follow by scaling. Unused kernels and batches with n=1 are covered by boundedness after increasing constants.

For optimism, use empirical Bernstein with u=5L. When n>=2 its error bound is at most

2 sqrt(5 Var(hat P,V^*)L/n)+(70/3)HL/n.

There are at most SAHK^2<=(SAHK)^2 relevant batch/vector/triple combinations. Its total failure probability is at most 2(SAHK)^2 exp(-5L)<=delta/4.

We will also use bounded-adapted comparisons, whose derivation is included here. If X in [0,B] and Y=E[X|F], convexity gives

E[exp(X/B)|F]<=exp((e-1)Y/B),

E[exp(-X/B)|F]<=exp(-(1-e^{-1})Y/B).

Multiplying these conditional bounds produces nonnegative supermartingales. Markov's inequality yields, with failure probability at most eta for each direction,

sum X<=(e-1)sum Y+B log(1/eta),

sum Y<=(1-e^{-1})^{-1}(sum X+B log(1/eta)).

We use their factor-three versions with universal additive constants. The filtration may alternate between revealing a context and revealing its episode trajectory: insert the context revelation before the conditional step and use the tower property. Allocate the remaining delta/2 among the tail, gap-sum, and finitely many filtered-count comparisons. Their logarithms are bounded by C L.

## 2. Optimism and a refined surplus estimate

We first prove the specialized monotone lower envelope directly. For a probability vector q, v in [0,H]^S, t>0, and a=sqrt(60), set

F(v)=qv+max{a sqrt(Var(q,v)t),a^2 Ht}.

On its constant branch the coordinate derivative is q_i. On the square-root branch sigma=sqrt(Var(q,v))>=aH sqrt(t), and the derivative is

q_i[1+a sqrt(t)(v_i-qv)/sigma]>=0.

Continuity handles the branch boundaries, including zero variance. Thus F is coordinatewise nondecreasing. Also, for z,w>=0,

max{az,60w}>=2sqrt(5)z+(70/3)w,

because 60-2sqrt(300)>70/3. Both public bonus coefficients dominate those in max{sqrt(60) sqrt(Var(q,v)L/n),60HL/n}.

Backward induction now proves tilde V>=V^* and tilde Q>=Q^* for every realized context. For n=1 the additive bonus exceeds H, so the capped estimate is H. Otherwise apply the monotone envelope to the optimistic continuation vector and then the empirical-Bernstein event to the optimal continuation vector. Capping at H preserves optimism since Q^*<=H.

Write D_h=tilde V_h-V_h^*. We first retain the coarse capped Bellman recursion needed below. The uniform bounded-vector transition estimate and the original bonus imply, along the greedy action,

D_h(s)<=P_h D_{h+1}+u(n_h),

u(n)=min{H,C H sqrt(S Lambda/n)}.

For n above a sufficiently large multiple of S Lambda, the inverse-count terms are bounded by the square-root term; below that range use D_h<=H and P_h D_{h+1}>=0. Unfolding gives

D_h(s)<=E[sum_{t=h}^H u(n_t)|s_h=s].

Jensen and Cauchy-Schwarz consequently imply

D_{h+1}(s')^2<=H E[sum_{t=h+1}^H min{H^2,C SH^2 Lambda/n_t}|s_{h+1}=s'].

We now tune the squared-error estimates more carefully than in the original combined-envelope argument. The triangle inequality for centered L2 norms gives

sqrt(Var(hat P,tilde V))<=sqrt(hat P[D^2])+sqrt(Var(hat P,V^*)).

Use the standard-deviation comparison and Young's inequality with squared-error coefficient H^{-2}. This gives

b_h<=H^{-2}hat P_h[D_{h+1}^2]+C sqrt(v_h Lambda/n_h)+C H^2 Lambda/n_h.

The scaled coordinate estimate gives

hat P_h[D_{h+1}^2]<=2P_h[D_{h+1}^2]+C SH^2 Lambda/n_h.

For completeness, its square-root term is at most C H sqrt(S P_h[D_{h+1}^2]Lambda/n_h), because D_{h+1}^4<=H^2D_{h+1}^2; Young's inequality bounds that term by P_h[D_{h+1}^2]+C SH^2 Lambda/n_h.

Similarly, the uniform transition estimate applied to D_{h+1}, again with Young coefficient H^{-2}, yields

|(hat P_h-P_h)D_{h+1}|<=H^{-2}P_h[D_{h+1}^2]+C SH^2 Lambda/n_h.

For the executed greedy action define

e_h=tilde Q_h-r_h-P_h tilde V_{h+1}.

The cap in the update gives an upper inequality, not an equality. Combining the preceding bounds with optimal-value concentration gives

e_h<=C sqrt(v_h Lambda/n_h)+C SH^2 Lambda/n_h+C H^{-2}P_h[D_{h+1}^2].

Substitute the squared Bellman-recursion bound. There are fixed universal constants for which, defining

a_v(n)=min{H,C sqrt(v Lambda/n)},

q_0(n)=min{H,C SH^2 Lambda/n},

q_1(n)=C min{H,C SH Lambda/n},

we obtain

e_h<=a_{v_h}(n_h)+q_0(n_h)+E[sum_{t=h+1}^H q_1(n_t)|s_h,a_h].

Here the current-stage term q_0 is retained explicitly. To justify its cap and the cap on a_v, use e_h<=H and the elementary inequality min{H,A+B+Z}<=min{H,A}+min{H,B}+Z for nonnegative A,B,Z. The future term follows from H^{-2} times the displayed squared-error bound and therefore has inverse-count coefficient C SH Lambda, not C SH^2 Lambda. This factor-H improvement is essential to the repaired integration.

## 3. Variance budget and clipping

Statewise claims involving W are required only at states reachable under an admissible policy in the context under consideration. At such a state, prepend a policy reaching it to any admissible suffix policy. Nonnegativity of earlier variance terms shows that the source full-trajectory conditional complexity bounds the expected suffix variance sum.

That suffix sum is also at most H^2. Write U_t=V_t^{*,c}(s_t). Along an admissible policy,

U_t-P_tV_{t+1}^{*,c}=r_t+gamma_t>=0.

Starting at s_h=s, telescoping gives

E[sum_{t=h}^H v_t]=-U_h^2+E[sum_{t=h}^H (U_t^2-(P_tV_{t+1}^{*,c})^2)]

<=-U_h^2+2H E[sum_{t=h}^H(U_t-P_tV_{t+1}^{*,c})]

=-U_h^2+2HU_h<=H^2.

Thus every relevant suffix variance budget is at most W. Each reachable admissible one-step variance is also at most W, by taking a policy reaching that state and choosing that action.

For W>0 set tau_h=(d/6)max{v_h/W,1/H}. For W=0 set tau_h=d/(6H); then every reachable admissible variance is zero. Define bar e_h=e_h 1{e_h>=tau_h}. Define bar V along the executed policy by the true-kernel recursion with rewards r_h+bar e_h and terminal value zero. Since bar e_h>=e_h-tau_h and max{x,y}<=x+y,

E[sum_{t=h}^H tau_t|s_h]<=d/3.

The Bellman recursions therefore give bar V_h>=tilde V_h-d/3. Negative surpluses are replaced by zero and do not increase the loss in this lower bound.

Let tau be the first strictly suboptimal action time. The performance-difference identity stopped at tau expresses the value loss as the expected continuation loss there. Since bar e is nonnegative, bar V-V^pi is at least the corresponding stopped continuation contribution. At a first mistake with gap g,

bar V-V^pi>=V^*-V^pi-d/3,

V^*-V^pi>=g.

Rearranging and integrating gives

V_1^*(mu)-V_1^pi(mu)<=(3/2)E[sum_h bar e_h]+(1/2)E[(d-gamma_tau)_+ 1{tau<infinity}].

Let E_p denote the sum of the last terms over episodes.

## 4. Lower tail and the separated clipped envelopes

For triples in Z_pos the conditional positive-gap quantile satisfies

Pr(gamma<gamma_h^p|positive admissible gap)<=p.

Indeed, strict-threshold events increase to the event at the supremum as their thresholds increase to it, and continuity from below preserves the probability bound. The conditional positive gaps are bounded, so their p-quantiles are finite for p<1.

Condition on history before c_k is drawn. Its distribution remains rho. An episode's first-mistake defect is at most d/2 times the indicator that some triple has a positive gap below d. Since d<=gamma_h^p for triples in Z_pos, a union bound bounds its conditional mean by (d/2)pSAH. Triples outside Z_pos have zero probability of a positive admissible gap. Each defect lies in [0,d/2], so the bounded-adapted comparison gives

E_p<=C(pK+1)SAH d Lambda.

Define clip[x|t]=x 1{x>=t}. For W>0 set

f_v(n)=clip[a_v(n)|(d/36)max{v/W,1/H}],

and set f_0=0 when W=0. Define two count envelopes

g_0(n)=clip[q_0(n)|d/(36H)],

g_1(n)=clip[q_1(n)|d/(36H^2)].

The constants in a_v,q_0,q_1 are the fixed constants from Section 2. These functions are nonnegative and nonincreasing in n.

The refined surplus estimate implies

bar e_h<=2 f_{v_h}(n_h)+2g_0(n_h)+2E[sum_{t=h+1}^H g_1(n_t)|s_h,a_h].

Here is the complete clipping argument. The discarded part of a_v is less than tau_h/6. The discarded part of q_0 is less than d/(36H)<=tau_h/6. There are at most H future summands, so their total expected discarded part is less than d/(36H)<=tau_h/6. Thus replacing the three components of the surplus upper bound by their retained parts removes at most tau_h/2. If e_h>=tau_h, their retained sum is at least e_h-tau_h/2>=e_h/2; if e_h<tau_h, bar e_h=0. This also proves the W=0 case, where the direct variance term vanishes.

For triples in Z_pos let G be the contexts with positive gap at least gamma_h^p; let G be empty outside Z_pos. Let B be the admissible contexts with gap below gamma_h^p. The public extension gamma_h^p=infinity outside Z_pos includes their zero-gap occurrences in B, while their positive-gap occurrences have probability zero. Therefore G and B cover sampled admissible occurrences almost surely.

Restrict private context/triple variance envelopes to combinations reachable under some admissible policy. This changes no occupancy or visit contribution, ensures v<=W, and avoids making assertions about conditioning on unreachable states. Empty envelope suprema are zero.

Let T_ret and T_trim be three times the episode-conditional expected sums of f on G and B, respectively. Define

T_cnt=3 sum_k E[sum_h g_0(n_h)+sum_h sum_{t=h+1}^H g_1(n_t)|history before the trajectory, including c_k].

The tower property and the preceding clipping comparison give

R_K<=T_ret+T_trim+T_cnt+E_p.

Each g_1 contribution has at most H predecessors, so T_cnt is at most three times the expected sum of g_0 plus 3H times the expected sum of g_1.

## 5. Predictable filtered counting and integration

Fix a deterministic context filter I and a nonincreasing phi:[1,infinity)->[0,B_0]. Let J_k indicate a visit to a given triple with c_k in I, q_k=E[J_k|history before the trajectory, including c_k], and M_k be the number of all prior visits to that triple. The weight

w_k=phi(max{M_k/4,1})

is measurable before the trajectory. The bounded-adapted comparison applied to w_kJ_k gives

sum_k w_kq_k<=3sum_k w_kJ_k+C B_0 Lambda.

If B_0=0 the assertion is immediate. The completed-batch comparison gives phi(n_k)<=w_k. At the j-th filtered visit M_k>=j-1; hence

sum_k w_kJ_k<=sum_{j=1}^{N_I}phi(max{(j-1)/4,1})

<=C B_0+C integral_1^{max{N_I,1}}phi(x)dx.

Consequently

sum_k phi(n_k)q_k<=C[B_0 Lambda+integral_1^{max{N_I,1}}phi(x)dx].

This applies to deterministic retained and trimmed variance envelopes and, separately, to g_0 and g_1. A union bound over at most four such comparisons per triple is covered by the confidence allocation in Section 1. No claim that cached batch counts dominate filtered cumulative counts is used.

For retained contexts put sigma_G=sup_{reachable c in G}v_h^c. Drop clipping and integrate min{H,C sqrt(sigma_G Lambda/x)}. This gives

T_ret<=C U+C SAH^2 Lambda,

U=sum_{Z_pos}sqrt(sigma_G N_G Lambda).

If N_G=0, the initial B_0 Lambda term alone covers the counting bound; if sigma_G=0 the whole variance envelope is zero.

For trimmed contexts, bound their envelope by sup_{0<=v<=W}f_v. When W>0 split the variance range at W/H. In the low range the envelope is bounded by C sqrt(W Lambda/(Hx)) and vanishes beyond C W H Lambda/d^2. Its integral is at most C W Lambda/d. In the high range let a=C W Lambda/d^2. Up to a use C sqrt(W Lambda/x), from a to aH use C W Lambda/(dx), and beyond aH the envelope vanishes. The integral is at most C W Lambda(1+log H)/d. These bounds follow directly by solving the inequality required for the square-root term to exceed its clipping threshold. Integrals can first be bounded over (0,infinity), or the displayed ranges can be intersected with [1,infinity); no negative integral is assigned to an empty range. For W=0 the envelope is zero. Thus

T_trim<=C SAH^2 Lambda+C |Z_trim^p|W Lambda ell(H)/d.

For the count envelopes use the following elementary integral calculation. If q(x)=min{B,A/x}, epsilon in (0,B], and g(x)=q(x)1{q(x)>=epsilon}, then

integral_1^infinity g(x)dx<=integral_0^{A/epsilon}min{B,A/x}dx

=A[1+log(B/epsilon)].

If epsilon>B the envelope is identically zero. This calculation is valid regardless of whether the flat-to-inverse-count transition A/B lies below or above 1.

For g_0, B=H, A=C SH^2 Lambda, and epsilon=d/(36H). For g_1, B=C H, A=C SH Lambda, and epsilon=d/(36H^2), with fixed universal constants inherited from q_1. Because 0<d<=H,

integral_1^infinity g_0(x)dx<=C SH^2 Lambda ell(H^2/d),

integral_1^infinity g_1(x)dx<=C SH Lambda ell(H^3/d).

Apply filtered counting with the full context filter, sum over SAH triples, and use the at most H propagation multiplicity only for g_1. The initial counting terms total at most C SAH^3 Lambda. The integrated terms therefore give

T_cnt<=C S^2 A H^3 Lambda ell(H^3/d).

This is where the revised proof gains a factor H compared with the old combined envelope.

To compare with the public term, put E=ell(SAH Lambda/d). Since Lambda>=1, SA>=1, and d<=H,

E>=1+log(H/d),

ell(H^3/d)=1+log(H/d)+2log H<=E+2log H<=3H E.

The last step uses E>=1 and log H<=H for H>=1. Thus, without comparing the logarithms alone,

T_cnt<=C S^2 A H^4 Lambda ell(SAH Lambda/d).

The old combined envelope can indeed have a larger integral than previously asserted. This proof replaces that envelope and does not claim its old integral estimate is true.

## 6. Gap charging and self-bounding

Every retained visit satisfies gamma_h^p<=gamma_h^{c_k}. Hence

sum_{Z_pos}gamma_h^p N_G<=sum_{k,h}gamma_h^{c_k}(s_h^k,a_h^k).

Let X_k be the realized gap sum in episode k, and let Y_k be its conditional expectation given the history and current context. Then 0<=X_k<=H^2, and the performance-difference identity gives sum_kY_k=R_K. The exponential comparison from Section 1 yields

sum_kX_k<=2R_K+C H^2 Lambda.

By Cauchy-Schwarz and sigma_G<=W,

U^2<=C_p sum_{Z_pos}gamma_h^p N_G,

C_p=sum_{Z_pos}W Lambda/gamma_h^p.

Write D=T_trim+T_cnt+E_p+C SAH^2 Lambda. The decomposition and retained estimate give R_K<=C U+D, so

U^2<=C_p(C U+C D).

Solving the positive-root inequality and using sqrt(C_pD)<=C_p+D gives U<=C(C_p+D), including C_p=0. Substituting all bounds proves

R_K<=C Lambda[sum_{Z_pos}W/gamma_h^p+|Z_trim^p|W ell(H)/d+(pK+1)SAH d+S^2 A H^4 ell(SAH Lambda/d)+SAH^2].

The allocated failure probabilities total at most delta. Transition concentration is proved conditionally on the complete context sequence and then unconditioned. Tail concentration uses pre-context history; occupancy and realized-gap comparisons use post-context history. These are distinct compatible applications, not an exchange of the conditioning fields.

## 7. Optimization and boundary cases

For each deterministic instance-dependent p the right-hand side is deterministic. If its infimum is finite, choose deterministic p_j approaching it. For every epsilon>0 the fixed-p bound gives Pr(R_K>C infimum+epsilon)<=delta by choosing a sufficiently close p_j. Letting epsilon decrease to zero proves the optimized claim. An infinite infimum is vacuous.

The argument covers W=0, H=1, K=1, unused kernels, zero occupancy, empty private envelope sets, and arbitrary positive integer K. No power-of-two assumption on K or profile-concentration size condition is required. The separate minimax profile and sum-of-bonuses results are not theorem-critical dependencies of this proof.
