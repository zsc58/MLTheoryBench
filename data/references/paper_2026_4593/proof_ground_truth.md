# Reference Proof

## Scope and unresolved implementation dependency

This proof establishes the public statement conditional on its explicit bandit-module assumption. The public task already assumed a high-probability anytime bandit guarantee; the repaired task states exactly the finite-horizon guarantee needed below.

A separate source-specific obligation remains open: the supplied source does not derive, or fully specify the parameters of, the one-half-Tsallis FTRL implementation with implicit exploration and doubling asserted to realize this interface. That specialized implementation theorem is `theory_018`, a nonstandard dependency. It is not certified by citing its name. This is the sole remaining private GT limitation; it is not a gap in the conditional argument below and is not evidence that the implementation claim is false.

Write S=|S| and A=|A| in estimates, and let q=log K. Until the final section assume K>=16H^2 S, so q>=1. Choose the universal confidence multiplier and the universal threshold constant sufficiently large, as permitted in the public statement.

## 1. Simultaneous concentration

We use the following standard independent concentration fact: if X_i is adapted, E[X_i|F_(i-1)]=0, and |X_i|<=a, then P(|sum_(i=1)^n X_i|>a sqrt(2n log(2/epsilon)))<=epsilon. This is applied only to bounded martingale differences, followed by finite union bounds.

For each actual fresh base instance, number its epochs and visits. A visit is selected before its current action and transition. Its table V^k is fixed before episode k. Hence Y_k=r_h^k+V_(h+1)^k(s_(h+1)^k) belongs to [0,H] and its conditional mean is D_(mu_h^k,nu_h^k)[r_h+P_h V_(h+1)^k](s_h^k).

For every fixed nonempty interval I, define V^*_(h,I) by replacing [K] by I in the public empirical recursion. These functions are fixed functions of the game and fixed opponent policy sequence, not functions of the sampled trajectory. Consequently r_h^k+V^*_(h+1,I)(s_(h+1)^k) also has its stated Bellman conditional mean whenever the state is visited.

Apply concentration at all visit prefixes, including partial final epochs, for both kinds of samples. Union over fixed intervals I before choosing any data-dependent interval. There are at most K actual base instances, at most S state modules per instance, at most K+1 created epochs per state, at most K possible positive prefix lengths, and at most K^2 fixed benchmark intervals. Conditional concentration at the start of each actual instance and zero padding after its end justify this finite union despite adaptive restarts. The logarithm in iota, with a sufficiently large universal multiplier, dominates all these union factors. On the resulting event, each epoch prefix of n>0 visits has sampling error at most (1/2)sqrt(iota n).

The bandit module's assumed adaptive conditional-mean guarantee, at its allocated confidence, simultaneously implies normalized pseudo-regret at most sqrt(iota n)/(2H) at every epoch prefix. Its conditional-mean reward vector is exactly g_i(a)=H^(-1)E_(b~nu_h^(t_i)(s))[r_h(s,a,b)+P_h V_(h+1)^(t_i)(s,a,b)]. The predictable vector can depend on earlier observations; obliviousness of the opponent alone does not make this vector oblivious. The adaptive version of the interface is therefore used.

Two further finite unions give:

* For every episode interval T, |sum_(k in T)(sum_h r_h^k-V_1^(mu^k,nu^k)(s_1^k))|<=sqrt(iota|T|).
* For every base-instance prefix and step h, the sum of E[delta_(h+1)^k|F_h^k]-delta_(h+1)^k is O(H sqrt(|T| log(HK/delta))), where delta_h^k=(V_h^k-V_h^(mu^k,nu^k))(s_h^k).

The second assertion conditions on F_h^k, before the current action and transition. Conditioning instead on F_(h+1)^k would be incorrect because the successor state is then already known. The increments have absolute value at most 2H. Episode reward increments have absolute value at most H. Thus all hypotheses of the concentration fact are checked.

With the stated confidence allocation and a sufficiently large multiplier in iota, the intersection of these events has probability at least 1-delta. Work on that intersection throughout.

## 2. Base-instance optimism

Fix a prefix T of one fresh base instance and a fixed interval I containing T. At terminal states V^*_(H+1,I)=V_(H+1)^k=0. Suppose successor estimates dominate V^*_(h+1,I). In the initial epoch the current estimate H-h+1 dominates the benchmark.

For any positive epoch prefix of n visits t_i, every t_i belongs to I. Thus

n V^*_(h,I)(s)
<= max_mu sum_i D_(mu,nu_h^(t_i))[r_h+P_h V^*_(h+1,I)](s)
<= max_mu sum_i D_(mu,nu_h^(t_i))[r_h+P_h V_(h+1)^(t_i)](s).

The bandit inequality replaces the maximum by the learner's conditional mean sum at cost at most (1/2)sqrt(iota n). Sampling concentration adds at most another (1/2)sqrt(iota n). Dividing by n gives the empirical average plus beta_n. Truncation at H-h+1 preserves domination. Backward induction proves optimism both for the estimates used in episodes and for the hypothetical estimate computed from any positive final partial epoch. Empty epochs require no empirical average and contribute zero to all sums.

## 3. Epoch count and widths

If Q epochs have been created at a state and Q>=2, the last completed epoch has at least (1+eta)^(Q-1) visits. Therefore Q<=1+log(K)/log(1+eta), and in particular Q<=1+ceil((1+eta)log(K)/eta). The extra one accounts for initialization and empty final epochs. For eta<=1/H and K>=2, Q=O(q/eta).

At a fixed layer, let W_h=sum_(s,tau:n_tau>0) sqrt(iota n_tau). Since the total visits at that layer equal |T|, two applications of Cauchy-Schwarz give

W_h<=sqrt(iota M |S_h| |T|)<=O(sqrt(iota S |T| q/eta)),

where M=O(q/eta).

## 4. Variance and aggregate optimistic gaps

Fix a minimax selection nu^*_(h,I) for each fixed interval I, using the global selection when I=[K]. Define

C_T(I)=sum_(h,k in T) TV(nu_h^k(s_h^k),nu^*_(h,I)(s_h^k)).

The finite minimax theorem applies because action simplices and the convex hull of finitely many opponent distributions are compact convex sets and the objective is bilinear. Linearity also makes the minimum over the finite empirical set equal to the minimum over its convex hull for fixed learner distribution. It follows that

D_(mu,nu^*_(h,I))[r_h+P_h V^*_(h+1,I)](s)<=V^*_(h,I)(s)

for every learner distribution mu.

For a bounded function g, |E_p g-E_q g|<=2||g||_infinity TV(p,q). Here the relevant function is in [0,H]. Inserting V^*_(h+1,I) into the sampled target, applying its sampling concentration, and then the minimax comparison yields, on an epoch of n visits,

sum_t(r_h^t+V_(h+1)^t(s_(h+1)^t)-V^*_(h,I)(s))
<=2H C_tau(h,s;I)+(1/2)sqrt(iota n)
  +sum_t(V_(h+1)^t-V^*_(h+1,I))(s_(h+1)^t).

Let L_tau denote the truncated estimate from that positive epoch, including a hypothetical estimate for a partial final epoch, and set

Gamma_h=sum_(s,tau:n_tau>0) n_tau(L_tau(h,s)-V^*_(h,I)(s)).

These summands are nonnegative by optimism. Adding the estimation bonuses and summing the preceding inequality gives

Gamma_h<=2H C_T(I)+O(W_h)+sum_(k in T)(V_(h+1)^k-V^*_(h+1,I))(s_(h+1)^k).

At layer h+1 the last sum equals sum n_tau(L_(tau-1)-V^*). Since n_tau<=(1+eta)n_(tau-1)+1, optimism permits multiplication by this upper bound. Shifting the index, retaining the initial term n_0=1, and bounding each rounding term by H yields

sum_(k in T)(V_(h+1)^k-V^*_(h+1,I))(s_(h+1)^k)
<=(1+eta)Gamma_(h+1)+O(H S q/eta).

The terminal quantity is zero. Since (1+eta)^H<=e when eta<=1/H, unrolling gives

Gamma_h<=O(H^2 C_T(I)+H sqrt(iota S |T|q/eta)+H^2 S q/eta).

## 5. Bellman decomposition and the short-prefix repair

Define A_h^k=V_h^k(s_h^k)-D_(mu_h^k,nu_h^k)[r_h+P_h V_(h+1)^k](s_h^k). The Bellman identity and the corrected transition martingale imply

sum_(k in T)delta_h^k<=sum_(k in T)delta_(h+1)^k+sum_(k in T)A_h^k+O(H sqrt(|T| log(HK/delta))).

Sampling concentration and the definition of L_tau give

sum_(k in T)A_h^k<=sum_(s,tau) n_tau(L_(tau-1)-L_tau)+(3/2)W_h.

Summation by parts rewrites the first sum using n_(tau+1)-n_tau. This difference is at most eta n_tau+1, including a truncated final epoch. Optimism makes the final negative term nonpositive. The initial term and the rounding terms are O(H S q/eta). Therefore

sum_(k in T)A_h^k<=eta Gamma_h+O(H S q/eta+W_h).

Substitute the bound for Gamma_h and sum over h. The terminal deltas vanish, the martingale terms are absorbed by the confidence term, and eta<=1/H absorbs H^2 sqrt(eta iota S |T|q). The result is

sum_(k in T)delta_1^k
<=O(eta H^3 C_T(I)+H sqrt(iota S |T|q/eta)+H^2 S q/eta).

It is not legitimate to remove the last term merely from eta>=S/K when |T| may be much smaller than K. Instead split into two cases:

* If |T|>=S/eta, then iota>=constant H^2 q absorbs H^2 S q/eta into H sqrt(iota S |T|q/eta).
* If |T|<S/eta, use sum delta_1^k<=H|T|<=H sqrt(iota S |T|q/eta).

Consequently, for every such prefix and every enclosing interval I,

sum_(k in T)delta_1^k<=c0(eta H^3 C_T(I)+H sqrt(iota S |T|q/eta)).

This is an upper bound on the optimistic gap sum itself, not merely on regret. The constant c0 in the algorithm is fixed sufficiently large to dominate this bound.

## 6. Local benchmarks and the computable statistic

For a nonempty interval T, let S(T) be the set of nonempty contiguous intervals I with T subseteq I subseteq [K], and define tilde C_T=min_(I in S(T)) C_T(I). The concentration event was made uniform over all fixed I, so this minimum can now be selected. For the realized partition into final sub-block intervals, put tilde C=sum_T tilde C_T. Since I=[K] is always allowed, tilde C<=sum_T C_T([K])=C.

This is not the assertion that variances relative to each sub-block's own minimax policy sum to at most C; that assertion is unnecessary and is not generally justified.

Reward concentration gives

sum_(k in T)(V_1^*(s_1^k)-V_1^(mu^k,nu^k)(s_1^k))<=Phi_T

by global optimism, and also

Phi_T<=sum_(k in T)delta_1^k+2sqrt(iota|T|)
<=2c0(eta H^3 tilde C_T+H sqrt(iota S |T|q/eta)).

The latter display is uniform over prefixes. When an eventual sub-block T is considered together with all its prefixes U, choose an enclosing interval I minimizing C_T(I). Then I also encloses U and C_U(I)<=C_T(I). Hence every prefix has the same upper bound with tilde C_T and its own length |U|. This avoids assuming monotonicity of the prefix minimum.

## 7. Geometric balance and unclipped final parameters

Set A0=iota S Kq and lambda_b=max{4^(-b)/H,S/K}. A final calibration sub-block cannot terminate if

lambda_b H^3(1+tilde C)<=H sqrt(A0/lambda_b),

because the preceding prefix bound is then at most its threshold 4c0 H sqrt(A0/lambda_b) at every prefix.

Let b_bar=floor(log_4(K/(SH))). Under K>=16H^2 S this is at least one. At b_bar the unclipped value lies between S/K and 4S/K. Since tilde C<=HK,

lambda_(b_bar) H^3(1+tilde C)<=8S H^4,

whereas

H sqrt(A0/lambda_(b_bar))>=(HK/2)sqrt(iota q)>=(H^2K)/2>=8S H^4.

Thus balance is reached no later than b_bar. Let b0 be the first balanced index. If reached, its final sub-block cannot terminate, so B<=b0<=b_bar. In particular, every reached final parameter is exactly 4^(-b)/H; clipping has not occurred.

The first balanced geometric index satisfies

2^B<=O(1+(H(1+tilde C)^2/A0)^(1/6)),

and B=O(log K). These statements are pathwise consequences on the common event, although tilde C is itself trajectory dependent.

## 8. Ordinary switch tests and stopping overshoot

If the opponent policy is constant throughout an ordinary sub-block prefix T, choose I=T. Then C_T(T)=0, and eta=1/H gives

Phi_T<=2c0 sqrt(H^3 iota S |T|q),

strictly below the ordinary threshold 3c0 sqrt(H^3 iota S |T|q). Thus every completed ordinary sub-block contains a policy switch.

Define L^(b)=1 plus the number of switches assigned to episodes of block b, including its right-boundary switch when present, as in the source. Then sum_b L^(b)=L-1+B. If Z_b ordinary sub-blocks have been started and no final sub-block is reached, all but possibly the last have completed, so Z_b<=L^(b). If the final sub-block is reached, all 4^b ordinary tests have completed, so 4^b+1<=L^(b).

At a stopping episode the statistic may exceed its threshold. Its one-step increase is at most H+sqrt(iota), because both the initial estimate and total reward are in [0,H], and sqrt(n)-sqrt(n-1)<=1. Thresholds are nondecreasing in n. Hence every stopped or truncated sub-block satisfies its threshold upper bound plus H+sqrt(iota). For K>=16H^2 S this additive amount is absorbed by a universal multiple of the threshold at any positive length.

An ordinary sub-block of length n consequently costs O(sqrt(H^3 iota S nq)). A reached final sub-block costs O(2^b sqrt(H^3 iota S Kq)). Applying Cauchy-Schwarz to ordinary lengths, whose sum is at most K, gives

sum_(ell=1)^(Z_b) Phi_ell^(b)
<=O(sqrt(min{4^b,L^(b)} H^3 iota S Kq)).

For a reached final sub-block, the inequality L^(b)>=4^b+1 justifies the same minimum. No switch charge from the final sub-block itself is needed.

## 9. Both aggregations

Global empirical regret is the sum of its restrictions to the sub-blocks, all using the same benchmark V^*. This is a partition identity, not telescoping of distinct local benchmark values. Therefore

Enr_K<=O(sqrt(H^3 A0) sum_(b=1)^B sqrt(min{4^b,L^(b)})).

Using the geometric alternative and the bound on 2^B yields

Enr_K<=O(sqrt(H^3 A0)+(H^5 A0 C)^(1/3)).

Indeed, the preliminary bound has 1+tilde C in place of C; the contribution of 1 is absorbed into sqrt(H^3 A0), since A0>=H, and tilde C<=C.

Alternatively,

sum_b sqrt(L^(b))<=sqrt(B(L-1+B))<=O(sqrt((L+q)q)),

so

Enr_K<=O(sqrt((L+q)H^3 iota S K q^2)).

Both hold on the same event, giving their minimum and hence the public bound.

## 10. Small K and theorem-critical obligation ledger

For K=1, Enr_K<=H<=H^2 S. For 2<=K<16H^2 S, bounded rewards imply Enr_K<=HK. Since iota>=H^2,

HK/sqrt(H^3 iota S K)=sqrt(K/(H iota S))<=4.

Also log K>=log 2 and L>=1. Thus HK is bounded by a universal multiple of each branch in the claimed minimum. This closes the small-K case using the full right-hand side. It does not assert HK=O(H^2 S).

Closed obligations: public definition closure; fixed-benchmark and predictable-estimate concentration; optimism including partial epochs; epoch count and widths; minimax/TV variance recursion; Bellman decomposition with corrected conditioning; short-prefix applicability; enclosing-interval minimization and prefix use; balance before clipping; ordinary switch accounting; stopping overshoot; both final aggregations; and all K>=1 cases.

Unresolved private instantiation obligation: prove that the source-designated FTRL implementation realizes the assumed bandit interface. No rubric step may treat this specialized external assertion as independently verified merely because it is cited.
