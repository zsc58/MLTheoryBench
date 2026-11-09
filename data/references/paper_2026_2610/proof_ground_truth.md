# Reference Proof

## Proof Structure and Obligations

The obligations are: (1) well-defined adapted statistics and stopping rules, including empty and zero-mass cases; (2) fixed-competitor mixture validity and runner-up monotonicity; (3) target LCB and simultaneous unseen-category validity; (4) the null-witness event decomposition; (5) a category-size-free maximal-count bound, pairwise growth and concentration; (6) target LCB growth, unseen-threshold decay and simultaneous fixed-time failure control; (7) tail summation; (8) feasible lower-bound instances, stopped likelihood ratios and their information consequences. Each is closed below. The only imported result is the audited standard-independent Ville inequality: a nonnegative adapted supermartingale with initial value at most one crosses 1/alpha with probability at most alpha. Its hypotheses are checked whenever it is used.

The source-local repair retained in this proof is the replacement of log(1/epsilon) by log(3/epsilon) in the uniform upper rate. This retains the source's equal component budgets rather than incorrectly absorbing their fixed logarithmic offsets near epsilon=1. The unweighted quantity in the LCB growth argument is M_t, not the source's isolated tilde M_t typo.

## Complete Proof

### Definitions and Anytime Validity

Put alpha=epsilon/3. All grids, weights and the significance level are fixed before observing data. Counts are measurable functions of finite observed histories. Runner-up ties do not affect the pairwise statistic, since tied labels have the same count. Each M_t(q) is a nonnegative finite sum of positive products over its admissible grid. For fixed t, its dependence on q is piecewise polynomial with finitely many grid cutoffs. L_t is a bounded, measurable function of N_t(r); alternatively, there are only finitely many possible values of N_t(r) at fixed t. The function f_t(u)=(1-u)^t/u is continuous and strictly decreasing from infinity to zero on (0,1], so U_t is the unique solution of f_t(U_t)=alpha and lies in (0,1). Also U_t decreases with t and tends to zero. These facts establish adaptedness and the stopping-time property. Empty sums are zero, infimum of an empty stopping set is infinity, and p_(2)=0 if there is no non-target label.

A positive supremum of summable nonnegative masses is attained. Indeed, the indices with mass greater than half the supremum form a finite nonempty set; their maximum must equal the supremum. Under H_0,r there is a non-target label and p_(2)>0: otherwise all non-target masses vanish, p_r=1, and the null is false. Choose a deterministic a* with p_a*=p_(2)>=p_r.

For fixed a!=r and lambda in (0,1), each pairwise factor is positive, and its conditional mean is 1+lambda(p_r-p_a). Under p_r<=p_a this is at most one. The product is therefore a nonnegative supermartingale with initial value one. Its fixed positive mixture is a nonnegative supermartingale with initial value at most one. Ville gives

P(sup_t E_t^(r,a)>=1/alpha)<=alpha.

At fixed N_t(r), each component and their mixture decrease with N_t(a). Consequently E_t^(r,a_hat_t)<=E_t^(r,a) for every observed non-target a.

For target LCB validity first handle p_r=0: almost surely N_t(r)=0 and L_t=0 for every t, so the failure event is empty. For p_r>0, every component in Lambda_r(p_r) is positive and has conditional factor mean one. Thus M_t(p_r) is a nonnegative martingale, with initial value at most one. If q_1<q_2, the admissible grid at q_2 is a subset of that at q_1, and each retained positive product decreases with q. Hence M_t(q_1)>=M_t(q_2). If L_t>p_r, the definition of a supremum supplies an accepted q>p_r, so M_t(p_r)>=M_t(q)>=1/alpha. Ville proves

P(exists t:L_t>p_r)<=alpha.

For unseen-category validity, fix a with p_a>0 and let s_a be the first integer t>=1 with U_t<p_a. If no such time exists, its violation event is empty. Otherwise, monotonicity of f_s_a implies

(1-p_a)^s_a<=alpha p_a.

If a is unseen at a later violating time, it is unseen at s_a. Therefore its entire time-uniform violation event has probability at most alpha p_a. Zero-mass labels cannot violate the bound. Summing over the countable category set gives

P(exists a,t:N_t(a)=0 and p_a>U_t)<=alpha.

At any certifying time, if a* has appeared, runner-up monotonicity forces E_t^(r,a*)>=1/alpha. If a* is unseen, L_t>U_t and p_a*>=p_r force either L_t>p_r or an unseen-category violation. These three covering events need not be disjoint. Their union has probability at most 3alpha=epsilon. This proves uniform anytime validity. Certification at an externally chosen data-dependent observation time is also contained in the same ever-certifying event.

### Elementary Exponential Bounds Used for the Rate

For a bounded random variable Z whose range has length h, the centered exponential bound is

E exp(s(Z-EZ))<=exp(s^2 h^2/8).

To verify it, let psi(s)=log E exp(sZ). Under exponential tilting, psi''(s) is a variance. Every law supported on an interval of length h has variance at most h^2/4, since its squared distance from the interval midpoint is at most h^2/4. Integrating psi'' twice proves the display, for positive and negative s. The same argument applies conditionally.

If independent observations determine a statistic G and changing coordinate i changes G by at most c_i, its Doob martingale differences have conditional range length at most c_i: averaging over the remaining independent coordinates preserves the coordinate oscillation. Iterating the preceding conditional exponential bound and optimizing Markov's inequality gives

P(G<EG-x)<=exp(-2x^2/sum_i c_i^2).

For Bernoulli Y_i with mean p, independence and log(1+z)<=z give

E exp(s sum_i(Y_i-p))<=exp(tp(e^s-1-s)).

For |s|<=1/8, e^s-1-s<=s^2. Using s=1/8 for the upper deviation and s=-1/8 for the lower deviation yields

P(|sum_i Y_i-tp|>tp/4)<=2exp(-tp/64).

All three estimates have now been derived, rather than invoked as unclosed named methods.

We also use the source's elementary logarithmic inversion: if A,C>0 and t>=2A log((AC) vee e), then t>=A log(Ct). Set u=t/A. The premise gives u>=2, log(CA)<=u/2, and log u<=u/2, so log(Ct)<=u. In particular, fixed multiples of delta^(-2)[B+log(1/delta)] with B>=log 3 enforce fixed multiples of delta^(-2)log(et); analogous thresholds p^(-1)[B+log(1/p)] enforce p^(-1)log(et). Enlarging universal constants absorbs the fixed constants inside these logarithms.

### Category-Size-Free Pairwise Control

Write p=p_r and s=p_(2), and put

R_t=max({0} union {N_t(a):a!=r}),
E_t^circ=sum_lambda w_lambda(1+lambda)^N_t(r)(1-lambda)^R_t.

Define tau^circ by imposing E_t^circ>=1/alpha and L_t>U_t. When an observed competitor exists, its maximal count is R_t; when none exists, the implemented pairwise check is vacuous. Thus tau<=tau^circ pathwise, including the singleton case.

Here is the required maximal-count estimate. Include the zero function in the class f_a(x)=1{x=a}, a!=r. Since every competitor mass is at most s,

E R_t-ts<=E sup_f sum_i(f(X_i)-E f(X_i)).

Introduce an independent ghost sample X'_i. Jensen's inequality bounds this by E sup_f sum_i(f(X_i)-f(X'_i)). Independent signs sigma_i in {-1,1} may be inserted because each pair (X_i,X'_i) is exchangeable. Subadditivity of the supremum then bounds the last expectation by

2 E E_sigma sup_f sum_i sigma_i f(X_i).

Conditional on the sample, there are at most t+1 distinct vectors (f(X_1),...,f(X_t)), including zero, and each has squared norm at most t. For a fixed vector v,

E_sigma exp(z sum_i sigma_i v_i)=product_i cosh(zv_i)<=exp(z^2 ||v||^2/2).

The inequality follows, for example, by integrating (log cosh x)''<=1. Bounding the exponential of a maximum by the sum of at most t+1 exponentials and using Jensen gives a conditional expected maximum at most log(t+1)/z+zt/2. Optimize over z>0 to obtain

E R_t<=ts+2sqrt(2t log(t+1)).

Choose the covered point lambda in [delta/8,delta/4], with weight w. Since 0<delta<=1, lambda<=1/4. The inequality log(1+x)>=x-x^2 for |x|<=1/2 follows by differentiating log(1+x)-x+x^2. Consequently

p log(1+lambda)+s log(1-lambda)>=lambda delta-lambda^2(p+s)>=3lambda delta/4>=3delta^2/32,

using p+s<=1. Define S_t=N_t(r)log(1+lambda)+R_t log(1-lambda). Because the second coefficient is negative, the maximal-count estimate and -log(1-lambda)<=4lambda/3 imply

E S_t>=3delta^2 t/32-C_0 delta sqrt(t log(t+1)).

Changing one observation changes each count statistic by at most one, and changes S_t by at most log(1+lambda)-log(1-lambda)<=7lambda/3<=delta. The derived bounded-differences estimate, with x=delta sqrt(t log(et)), therefore gives a failure probability at most (et)^(-2).

Put B_pw=log(1/(alpha w))=log(3/(epsilon w)). The logarithmic inversion above shows that, for a universal sufficiently large C_1,

t>=T_pw=C_1 delta^(-2)[B_pw+log(1/delta)]

implies E S_t-delta sqrt(t log(et))>=B_pw. Since E_t^circ>=w exp(S_t), it follows that

P(E_t^circ<1/alpha)<=(et)^(-2), t>=T_pw.

This includes s=0 and delta=1; B_pw>=log 3 prevents a vanishing threshold.

### Target LCB and Unseen Threshold

Set q_0=p/2 and choose lambda_r in [1/32,1/16], with weight v. It is admissible because q_0<=1/2. Let Y_i=1{X_i=r} and

A_t={3pt/4<=N_t(r)<=5pt/4}.

The derived Bernoulli bound gives P(A_t^c)<=2exp(-pt/64). On A_t, the quadratic logarithmic estimate gives

log M_t(q_0,lambda_r)>=lambda_r(N_t(r)-pt/2)-lambda_r^2 sum_i(Y_i-p/2)^2.

The squared sum is N_t(r)(1-p)+tp^2/4, which is at most 3pt/2 on A_t. Thus

log M_t(q_0,lambda_r)>=lambda_r pt(1/4-3lambda_r/2)>=pt/256.

It follows that M_t(q_0)>=v exp(pt/256)>=1/alpha once pt>=256log(1/(alpha v)).

The empirical-frequency restriction in the definition of L_t must also be verified. For an admissible component, Jensen's inequality gives

t^(-1)log M_t(q,lambda)<=log(1+lambda(p_hat_t(r)-q)).

If p_hat_t(r)<=q, every component is at most one, so their subconvex mixture is at most one. Hence M_t(q)>1 implies p_hat_t(r)>q. In particular, the crossing at q_0 places q_0 in the set defining L_t and implies L_t>=q_0.

At u=p/4,

f_t(p/4)<=4p^(-1)exp(-pt/4).

Therefore U_t<=p/4 once pt>=4log(4/(alpha p))=4log(12/(epsilon p)). At times satisfying these two deterministic requirements, L_t>U_t on A_t. Logarithmic inversion also makes 2exp(-pt/64)<=(et)^(-2) once

t>=T_rare=C_2 p^(-1)[log(3/epsilon)+log(1/v)+log(1/p)].

Thus P(L_t<=U_t)<=(et)^(-2) for all t>=T_rare. This remains valid for p=1, when the count event holds deterministically.

### Tail Summation and the Uniform Upper Rate

Let T=ceil(max{T_pw,T_rare}), increasing constants so T>=2. If tau^circ>t, at least one of its two conditions fails at time t, whether or not either condition crossed at an earlier time. Thus

P(tau^circ>t)<=2(et)^(-2), t>=T.

The tail-sum identity gives E tau^circ<=T+2e^(-2)sum_{t>=T}t^(-2)<=T+1. In particular tau^circ, and hence tau, is almost surely finite. If both selected weights are at least the fixed universal kappa>0, their logarithmic penalties are absorbed into a universal multiplier because log(3/epsilon)>=log 3. Consequently

E_P tau<=C[(log(3/epsilon)+log(1/delta))/delta^2+(log(3/epsilon)+log(1/p_r))/p_r].

The constant depends only on the fixed universal weight floor and numerical constants, not on the distribution, significance level, remaining grid design, or category-set size.

### Stopped Information Argument

For the lower bound let tau' be a single decision-based certifier, applied without changing its rules between the alternative P and a null Q. Assume P(tau'<infinity)=1 and E_P tau'<infinity. For the pairs used below, P is absolutely continuous with respect to Q and the one-sample log likelihood ell(X)=log(P(X)/Q(X)) is bounded on P's support.

Record each finite stopped history together with a cemetery outcome for nontermination. On a finite stopped history, the same decision-rule indicator occurs under both laws and cancels, leaving likelihood ratio product_{i<=tau'}P(X_i)/Q(X_i). The alternative assigns no probability to the cemetery outcome. Absolute integrability follows from boundedness of ell and finite E_P tau'. Since {tau'>=i} depends only on X_1,...,X_{i-1}, independence and Fubini give

D(P^stop||Q^stop)=E_P sum_{i<=tau'}ell(X_i)=E_P tau' D(P||Q).

This identity does not require almost-sure stopping under Q. If beta=Q(tau'<infinity)<=epsilon, restricting and normalizing Q to its finite-stopping event gives

D(P^stop||Q^stop)=log(1/beta)+D(P^stop||Q^stop(.|tau'<infinity))>=log(1/epsilon).

Nonnegativity of the last divergence follows from Jensen applied to the likelihood ratio. If beta=0, absolute continuity would contradict alternative almost-sure stopping; the same information conclusion is interpreted as infinite. Thus every constructed pair yields E_P tau'>=log(1/epsilon)/D(P||Q).

### Feasible Lower-Bound Instances and Combination

Fix p in (0,1/2], 0<delta<p, and let K=ceil((1-p)/(p-delta)). There are at least K+2 non-target labels, or infinitely many.

For the hidden instance choose distinct b_1,...,b_K,h and set P_un(r)=p, P_un(b_j)=(1-p)/K, and all other masses, including h, to zero. Each competing mass is at most p-delta, so P_un belongs to P(p,delta). Obtain Q_un by replacing the target mass by p/2 at each of r and h, leaving the other masses unchanged. This is a null law. On the alternative support the log ratio is log 2 at r and zero elsewhere; its per-sample KL is p log 2. Hence

E_P_un tau'>=log(1/epsilon)/(p log 2).

For the discrimination instance set m=ceil((1-2p+delta)/(p-delta))=K-1. Here K>=2, so m>=1. Choose a*,b_1,...,b_m and set P_pw(r)=p, P_pw(a*)=p-delta, P_pw(b_j)=(1-2p+delta)/m, and all remaining masses to zero. These masses are nonnegative, sum to one, and each remaining mass is at most p-delta. The instance therefore belongs to P(p,delta) and uses only K non-target labels. Swap the masses of r and a* to obtain a null law Q_pw. The bounded log ratio has mean

D(P_pw||Q_pw)=delta log(p/(p-delta)).

Thus E_P_pw tau'>=log(1/epsilon)/[delta log(p/(p-delta))]. If delta<=p/2, then -log(1-delta/p)<=2delta/p, giving E_P_pw tau'>=p log(1/epsilon)/(2delta^2). The supremum over the class is at least the maximum of the two instance bounds, hence at least

(1/4)log(1/epsilon)(p/delta^2+1/p).

If delta>p/2, then p/delta^2+1/p<=5/p, and the hidden instance gives the same conclusion with constant 1/(5log 2)>1/4. Taking c=1/4 proves the unchanged lower bound. All theorem-critical obligations are closed.
