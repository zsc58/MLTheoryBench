# Reference Proof

## Contract and proof obligations

Work in the normalized model of the public task: each centered marginal is 1-sub-Gaussian, the covariance mgf inequality holds on the l1 ball of radius 1/2, and m is the maximum action cardinality. Actions are predictable. All analysis below starts after the fixed finite initialization, whose regret is at most L Delta_max. If all gaps vanish, the conclusion R_T=0 is immediate. Otherwise write d=Delta>0, D=Delta_max, h=1+log(D/d), and

S_i=max_{A contains i} sum_{j in A} max(0,Sigma*_ij),  S=sum_i S_i,

delta(t)=2(log t+log log t)+em.

The obligations are: (1) adaptive covariance concentration with the actual radius; (2) summable one-sided optimal-action confidence failure; (3) finite regret from selected-action mean overestimation; (4) the optimistic radius decomposition; (5) counter integration and reverse amortization; and (6) the small-gap comparison. Each is derived below. The sharper per-bin estimate printed in the source's covering lemma is not assumed.

## 1. Covariance concentration

A centered 1-sub-Gaussian variable Y satisfies P(|Y|>u)<=2 exp(-u^2/2), hence E|Y|^(2p)<=2^(p+1)p!. For two such variables Y,Z, Cauchy-Schwarz gives E|YZ|^p<=2^(p+1)p!, without an independence assumption. Consequently V=YZ-E[YZ] satisfies E|V|^p<=2^(2p+1)p!, and EV=0. For |lambda|<=1/8,

E exp(lambda V)<=1+2 sum_{p>=2}(4|lambda|)^p<=1+64lambda^2<=exp(64lambda^2).

We use the following elementary adaptive-mgf principle throughout. If predictable weights w_u multiply centered observations having conditional mgf at most exp(lambda^2 w_u^2/2), then exp(lambda sum_{u<=s}w_u Y_u-lambda^2 sum_{u<=s}w_u^2/2) is a nonnegative supermartingale of initial value one. This follows by conditioning on the history at each round. The analogous assertion holds for predictable inclusion of centered products with compensator 64lambda^2 times the inclusion count. At a fixed time, Markov's inequality can be applied on an event prescribing terminal counts; one then unions over their possible integer values. This does not condition observations into independent samples.

Fix i,j,t and abbreviate the pre-round counts by N_i,N_j,N_ij. Let Q_ij be the joint-sample average of (X_i-mu_i*)(X_j-mu_j*). For a fixed possible count a, Chernoff with x=3log t gives

P(N_ij=a and |Q_ij-Sigma*_ij|>16 max{x/a,sqrt(x/a)})<=2e^-x.

Indeed, for x/a<=1 take |lambda|=sqrt(x/a)/8; for x/a>=1 take |lambda|=1/8. Union over at most t counts gives failure at most 2t^-2.

Let b_i=overline mu_i-mu_i* and b_j=overline mu_j-mu_j*. Let a_i,a_j be the centered means of coordinates i,j restricted to their joint observations. The exact identity is

overline Sigma_ij-Sigma*_ij=(Q_ij-Sigma*_ij)-b_i(a_j-b_j)-b_j a_i.

The scalar adaptive-mgf principle and a union over one count give

|b_i|<=sqrt(6log t/N_i),  |b_j|<=sqrt(6log t/N_j),  |a_i|<=sqrt(6log t/N_ij),

each with failure probability at most 2t^-2.

For the remaining difference, fix candidate counts a=N_ij and b=N_j, with 1<=a<=b<t. Use predictable weights

w_u=1{i,j in A_u}-(a/b)1{j in A_u}.

On the event of these terminal counts, sum_u w_u=0,

sum_u w_u(X_{u,j}-mu_j*)=a(a_j-b_j),

and sum_u w_u^2=a(1-a/b)<=a. Chernoff therefore bounds the probability of this count event and |a_j-b_j|>sqrt(8log t/a) by 2t^-4. Union over at most t^2 count pairs gives failure at most 2t^-2.

Combining all five bounds with the identity yields exactly the public radius g_ij(t), with entrywise failure at most 10t^-2. Thus, for

S_t={for all i,j, |overline Sigma_ij,t-1-Sigma*_ij|<=g_ij(t)},

P(S_t^c)<=10n^2t^-2. On S_t, Sigma*_ij<=Sigma_ij,t<=Sigma*_ij+2g_ij(t).

## 2. One-sided confidence and summable optimism failure

Fix an optimal action A*, and put k=|A*|. If k=0, its objective is always zero and the confidence event below is automatic. Suppose k>0. Set

sigma_i^2=sum_{j in A*}max(0,Sigma*_ij),

u_i=(mu_i*-overline mu_i,t-1)_+,

Z_i=N_i,t-1 u_i^2/[4(sigma_i^2+k u_i)] for i in A*.

If sigma_i^2=0, then Sigma*_ii=0, so that coordinate is deterministic; set Z_i=0. This resolves the only possible zero-over-zero expression in these private statistics.

Define C_t={mu* vee overline mu_t-1 belongs to C_t(A*)}, with coordinatewise maximum. On S_t, failure of C_t implies sum_{i in A*}Z_i>delta(t). We need only this one-sided event, not two-sided confidence for every action or sign pattern.

Here is a complete covering argument with a routine finer peeling than the printed source proof. Let rho=4/3, and partition each positive count into bins [rho^q,rho^(q+1)), q>=0. Fix a joint bin B, and let U_i be its upper endpoint. For any subset J of the non-deterministic coordinates and positive numbers z_i, define epsilon_i>0 by

U_i epsilon_i^2/[4(sigma_i^2+k epsilon_i)]=z_i,

and set lambda_i=epsilon_i/[2(sigma_i^2+k epsilon_i)] for i in J and zero elsewhere. Existence and uniqueness follow from strict monotonicity in epsilon_i. Each lambda_i<=1/(2k), so ||lambda||_1<=1/2.

On B intersect {Z_i>z_i for all i in J}, monotonicity gives mu_i*-overline mu_i>=epsilon_i and N_i>=U_i/rho. Also

lambda_i epsilon_i-sigma_i^2 lambda_i^2>=epsilon_i^2/[4(sigma_i^2+k epsilon_i)].

For every nonnegative vector v supported on A*,

v^T Sigma* v<=sum_{i,j in A*}max(0,Sigma*_ij)(v_i^2+v_j^2)/2=sum_i sigma_i^2 v_i^2.

Take v_u=lambda odot e_{A_u intersect A*}. Predictability and the covariance mgf assumption, applied with -v_u, show that

M_s=exp(sum_{u<=s}[v_u^T(mu*-X_u)-v_u^T Sigma* v_u])

is a nonnegative supermartingale with E M_s<=1. The rectangular event above implies

log M_{t-1}>=sum_{i in J}N_i(lambda_i epsilon_i-sigma_i^2 lambda_i^2)>=sum_{i in J}z_i/rho.

Therefore its probability is at most exp(-sum_{i in J}z_i/rho).

Put W_i=1_B Z_i. The same rectangular bound holds for every nonempty coordinate subset. For 0<s<1/rho, expand the product of the identities exp(sW_i)=1+integral_0^{W_i}s exp(sx)dx. Tonelli's theorem and the subset rectangular bounds give

E exp(s sum_i W_i)<=sum_{J subset A*}(s/(1/rho-s))^|J|=(1-s rho)^-k.

Choosing s=2/3 gives E exp((2/3)sum_i W_i)<=9^k, and hence

P(B and sum_i Z_i>=delta(t))<=9^k exp(-2delta(t)/3).

There are at most (1+log_rho t)^k nonempty joint bins. Thus

P(S_t and C_t^c)<=9^k(1+log_rho t)^k exp(-2delta(t)/3).

For fixed k,m this is a constant times t^-4/3 multiplied by powers of log t, and is summable. This proves precisely the optimism-failure estimate needed by the unchanged confidence threshold. It does not rely on the source's unjustified sharper per-bin exponent.

## 3. Selected-action mean overestimation

Define D_t={e_At^T(overline mu_t-1-mu*)<=Delta(A_t)/2}. On a positive-gap round in D_t^c, some i in A_t has overline mu_i,t-1-mu_i*>d/(2m). Charge that round to such a coordinate. Each selected coordinate increments its count, so any coordinate-count pair (i,s) is charged at most once.

The scalar exponential supermartingale stopped at the s-th observation of coordinate i gives

P(the s-th observation occurs and its empirical mean exceeds mu_i*+d/(2m))<=exp(-s d^2/(8m^2)).

This follows by applying the nonnegative supermartingale at the stopping time truncated at a deterministic horizon and then taking a limit; no claim of independence conditional on terminal counts is needed. Consequently

E sum_t Delta(A_t)1{Delta(A_t)>0,D_t^c}<=D sum_i sum_{s>=1}exp(-s d^2/(8m^2))<=8nm^2 D/d^2.

Together with Sections 1 and 2, all failure-event contributions are bounded by a finite constant depending on the fixed instance, independent of T. In particular they are o(log T).

## 4. Optimistic radius decomposition

Consider a positive-gap round on C_t intersect D_t intersect S_t. The feasible vector mu* vee overline mu gives an objective at A* at least e_A*^T mu*. Optimality therefore gives Delta_t<=e_At^T(mu_t-mu*). On D_t,

Delta_t<=2x_t, where x_t=e_At^T(mu_t-overline mu_t-1).

An optimizer has nonnegative deviations on its selected coordinates: reflecting any negative selected deviation preserves its constraint and strictly increases its objective. For a nonempty selected action, put q_t=min_{i in A_t}N_i,t-1 and

V_t=sum_{i in A_t}[sum_{j in A_t}max(0,Sigma_ij,t)]/N_i,t-1.

Cauchy-Schwarz and the confidence constraint give x_t^2<=4delta(t)(V_t+m x_t/q_t). Solving this quadratic and using sqrt(a+b)<=sqrt(a)+sqrt(b) yields

Delta_t<=4sqrt(delta(t)V_t)+8m delta(t)/q_t.

An empty selected action cannot have a positive gap on C_t, so it needs no q_t definition.

On S_t, max(0,Sigma_ij,t)<=max(0,Sigma*_ij)+2g_ij(t). Since N_i,N_j>=N_ij, the explicit radius gives, for t<=T,

g_ij(t)/N_i<=C[log(T)/N_ij^2+sqrt(log T)/N_ij^(3/2)]

for an absolute constant C. The factor two in the covariance comparison is retained in the absolute constants. Using delta(T)>=log T and its monotonicity for T>=2, we obtain

Delta_t<=4sqrt(delta(T)sum_{i in A_t}S_i/N_i)
          +C delta(T)sqrt(sum_{i,j in A_t}N_ij^-2)
          +C delta(T)^(3/4)sqrt(sum_{i,j in A_t}N_ij^-3/2)
          +8m delta(T)/min_{i in A_t}N_i.

All counts in this display are pre-round counts. Each term will be charged separately: if their sum is at least Delta_t, at least one term is at least Delta_t/4. Absorbing this factor into its coefficients changes only universal constants.

## 5. Counter integration and reverse amortization

### Counter integral

Consider an initialized counter N_i>=1 that increments whenever i belongs to I_t, and a nonincreasing nonnegative f. Only positive-gap rounds are considered. Let d_i,D_i be the minimum and maximum positive gaps associated with i; omit indices with no such rounds. List their distinct gaps in decreasing order g_1>...>g_K, and set f(g_0)=0. Partition the counter values into intervals (f(g_{r-1}),f(g_r)]. In the interval assigned to g_r, a counted round has gap at most g_r. Each positive integer counter value can be charged at most once. Therefore the total charge is at most

sum_{r=1}^K [floor(f(g_r))-floor(f(g_{r-1}))]g_r
 =floor(f(d_i))d_i+sum_{r=1}^{K-1}floor(f(g_r))(g_r-g_{r+1})
 <=f(d_i)d_i+integral_{d_i}^{D_i}f(x)dx.

The last inequality uses monotonicity on each interval [g_{r+1},g_r]. In particular, for 0<alpha<1 and f(x)=b x^(-1/alpha), this is at most b d_i^(1-1/alpha)/(1-alpha); for f(x)=b/x it equals at most b(1+log(D_i/d_i)).

### l2 charging

Let |I_t|<=M, alpha_i in [1/2,1], beta_i>=0, and

x_i=(beta_i/N_i,t-1)^alpha_i,  Lambda_t=(sum_{i in I_t}x_i^2)^(1/2).

Zero coefficients can be discarded. On a positive-gap round with Delta_t<=Lambda_t, reverse triangle inequality gives

Lambda_t<=||(2x_i-Lambda_t/sqrt(|I_t|))_+:i in I_t||_2.

Indeed, coordinatewise 2x_i is at most Lambda_t/sqrt(|I_t|)+(2x_i-Lambda_t/sqrt(|I_t|))_+, and the norm of the first vector is Lambda_t. It follows that

Lambda_t^2<=sum_{i:2x_i>=Lambda_t/sqrt(|I_t|)}4x_i^2.

Every retained ratio 2x_i/Lambda_t lies in [1/sqrt(M),2]. Partition it into the dyadic intervals [2^-r,2^(1-r)], r=0,...,K, where K=ceil(log_2 sqrt(M)); assign shared endpoints to only one interval. Write L=K+1. Since the sum of the upper bounds 2^(2-2r)Lambda_t^2 times group cardinality is at least Lambda_t^2, some group J_r has |J_r|>=2^(2r-2)/L. For its coordinates,

N_i,t-1<=beta_i(2^(r+1)/Delta_t)^(1/alpha_i).

Distribute Delta_t across this group. Summing rounds and then allowing all groups gives an upper bound

4L sum_i sum_{r=0}^K 2^-2r sum_t Delta_t 1{i in I_t, N_i,t-1<=beta_i(2^(r+1)/Delta_t)^(1/alpha_i)}.

Apply the counter integral to each inner gap-weighted sum. The geometric series gives

sum_t Delta_t 1{Delta_t<=Lambda_t}<=4log_2(4sqrt(M))sum_i beta_i eta_i,

where

eta_i=8log_2(4sqrt(M))/d_i                         if alpha_i=1/2,
eta_i=[(2^(-1/alpha_i)-1/4)(1-alpha_i)d_i^((1-alpha_i)/alpha_i)]^-1  if 1/2<alpha_i<1,
eta_i=4(1+log(D_i/d_i))                         if alpha_i=1.

For alpha=1/2 the geometric sum has L equal terms; for alpha>1/2 its ratio is 2^(1/alpha-2)<1, and for alpha=1 the sum is at most 2. This proves the support bound, including the endpoint alpha=1.

### Application

For the true-covariance term use coordinate counters, M=m, alpha=1/2, and beta_i=C delta(T)S_i. This contributes at most

C delta(T)log^2(m+1)S/d.

For the first pair-counter term use ordered pairs, M=m^2, alpha=1, and beta_ij=C delta(T). It contributes at most C delta(T)log(m+1)n^2 h.

For the second pair-counter term use M=m^2, alpha=3/4, and beta_ij=C delta(T). It contributes at most C delta(T)log(m+1)n^2 d^-1/3.

Finally, bound 1/min_{i in A_t}N_i by sqrt(sum_{i in A_t}N_i^-2). Use M=m, alpha=1, and beta_i=Cm delta(T). This contributes at most C delta(T)log(m+1)nm h, which is at most the corresponding n^2 term because m<=n. Counter charging is valid for the ordered pairs because choosing A_t increments every counter in A_t^2. Indices absent from all positive-gap actions are omitted; bounding their number by n or n^2 is harmless.

## 6. Final comparison

Combining all sections, for a finite fixed-instance constant B and a universal C,

R_T<=B+C delta(T)[log^2(m+1)S/d+log(m+1)n^2(d^-1/3+h)].

Let Q=log(m+1)S/n^2. The public hypothesis is

max{d,(dh)^(3/2)}<=c Q^(3/2).

Taking the power 2/3 gives max{d^(2/3),dh}<=c^(2/3)Q. Dividing by d therefore implies

n^2(d^-1/3+h)<=2c^(2/3)log(m+1)S/d.

Thus the non-covariance terms are absorbed into the first term, with universal constants. Since delta(T)/log T tends to 2 and B/log T tends to zero,

limsup_{T to infinity} d R_T/log T<=c'log^2(m+1)S

for a universal c'. If S=0 and d>0, the hypothesis is impossible, so no additional division-by-zero case arises. Every required proof obligation is closed.
