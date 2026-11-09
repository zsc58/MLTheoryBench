# Reference Proof

## Contract and obligations

The set of Walsh indices must be chosen as a function of the horizon alone, before choosing the forecaster. Predictions may be arbitrary real values in [0,1], and may adapt to past outcomes. Model all learner randomness by a seed R independent of the signs and use the filtration F_t = sigma(R, xi_1,...,xi_t). The deterministic contexts are already known, and p_t is F_{t-1}-measurable. In particular, E[x^t-y^t | F_{t-1}]=0. Every expectation below includes both sources of randomness.

The proof closes the following obligations: a uniform small Walsh representation of all grid threshold signs; conversion to expected l1 truthfulness; a pathwise spacing/diversity inequality; adaptive noise bucketing with its predictable-subsequence and return-time justifications; and the final constant-group comparison. No paper-specific theorem is assumed without proof.

Take T sufficiently large that m=2^{floor((log_2 T)/3)}>=2. Then T^(1/3)/2<=m<=T^(1/3), and the grid and outcome distribution are exactly those in the problem. Write q=log_2 m.

## 1. Uniform threshold approximation and the fixed family

For r in {0,...,m}, let f_r(i)=1 when i<r and f_r(i)=-1 otherwise. Define

 a_l(r)=(1/m) sum_{i=0}^{m-1} f_r(i)w_l(i),   0<=l<m.

Walsh orthogonality follows by pairing indices differing in a bit on which two characters differ. Consequently f_r=sum_l a_l(r)w_l. Also a_0(r)=(2r-m)/m, so |a_0(r)|<=1.

For l!=0, let d be the number of trailing zero bits of l. The character w_l is constant on blocks of length 2^d, and consecutive blocks in each aligned block of length 2^(d+1) have opposite signs. Complete paired blocks have sum zero, and the remaining portion of any prefix has absolute sum at most 2^d. Since w_l has total sum zero,

 a_l(r)=(2/m) sum_{i<r}w_l(i),

and b_l:=max_r|a_l(r)|<=2^(d+1)/m. There are m/2^(d+1) indices with this trailing-zero count. Therefore

 B:=sum_{l=1}^{m-1}b_l<=q.

Moreover B>0, since a nonconstant threshold cannot have only a constant Fourier coefficient.

Sample K indices J_1,...,J_K independently with probabilities b_l/B, omitting indices with b_l=0. Define

 f_tilde_r(i)=a_0(r)+(1/K)sum_{s=1}^K B a_{J_s}(r)w_{J_s}(i)/b_{J_s}.

For each fixed (r,i), the summands have the correct mean and lie in [-B,B]. The bounded-variable exponential estimate gives

 P(|f_tilde_r(i)-f_r(i)|>epsilon)<=2 exp(-K epsilon^2/(2B^2)).

For completeness, this estimate follows from E exp(lambda(X-EX))<=exp(lambda^2 B^2/2) for X in [-B,B], followed by independence and optimization of the exponential Markov bound. The moment-generating-function inequality follows by observing that the second derivative of its logarithm is a variance under exponential tilting, at most B^2, and integrating twice from zero.

Set epsilon=1/4. A union bound over the m(m+1) pairs (r,i) shows that K=ceil(C_0 B^2 log(m+1)) suffices for positive probability of simultaneous approximation within 1/4. Fix one successful realization, independently of any forecaster. Let S be its set of distinct indices and let k_l be the multiplicity of l. Put

 c_0(r)=a_0(r),   c_l(r)=(B k_l/K)a_l(r)/b_l,

and f_hat_r(i)=c_0(r)+sum_{l in S}c_l(r)w_l(i). Then

 |S|<=C_1 log^3(m+1),
 max_{r,i}|f_hat_r(i)-f_r(i)|<=1/4,
 max_r|c_0(r)|<=1,
 sum_{l in S}max_r|c_l(r)|<=B<=q.

The last inequality follows by summing B k_l/K. Define G_S using this fixed S. Its groups are binary and prediction-independent by their definitions, and it includes the constant group.

## 2. Calibration implies expected l1 truthfulness

Let

 A=sum_{t=1}^T|p_t-x^t|,   M=E[MCerr_T(G_S)].

For every v in [0,1], define r(v)=#{i:x_i<=v} and s_hat_v(x_i)=f_hat_{r(v)}(i). This convention handles equality with a grid point: the product with v-x_i is then zero regardless of the chosen sign. At all grid points,

 f_{r(v)}(i)(v-x_i)=|v-x_i|,
 s_hat_v(x_i)(v-x_i)>=(3/4)|v-x_i|>=(1/2)|v-x_i|.

The function v -> s_hat_v(x_i) is measurable and fixed before play. Thus s_hat_{p_t}(x^t) is predictable and bounded. Conditional expectation at each round gives

 E A<=2 E sum_t s_hat_{p_t}(x^t)(p_t-x^t)
     =2 E sum_t s_hat_{p_t}(x^t)(p_t-y^t).

This identity is taken in chronological time; it does not condition on a final prediction bucket or its membership.

Extend the bias/error formulas privately to signed weights by the same finite sums. After the preceding expectation identity, regroup pathwise by the finitely many realized predictions. The right-hand sum becomes

 sum_v c_0(r(v))B_T(v,g_all)
 +sum_{l in S}sum_v c_l(r(v))B_T(v,w_l).

Since w_l=g_l^+-g_l^-, the triangle inequality gives

 Err_T(w_l)<=Err_T(g_l^+)+Err_T(g_l^-)<=2 MCerr_T(G_S).

The constant-group error is at most MCerr_T(G_S). Consequently

 E A<=2(1+2q)M<=K_1 log(m+1)M.                         (1)

All sums here are pathwise finite, so arbitrary real-valued predictions cause no summation problem.

## 3. Truthfulness forces diversity

For each realized value v, let n_v=#{t:p_t=v}, and put N=sum_v sqrt(n_v). We prove

 sum_v n_v^2<=16T(A+T/m+1).                           (2)

Here is a direct spacing proof of the same bucket-size estimate used in the source. Let Delta=1/(2(m-1)) be the grid spacing and b=ceil(T/m). Every grid point occurs at most b times in the entire sequence, hence also within any one prediction bucket.

Order the contexts in a bucket of size n as a_1<=...<=a_n. If j<k and a_k-a_j=Delta d, the interval from a_j through a_k contains at most b(d+1) occurrences. Thus k-j+1<=b(d+1), and in particular

 a_k-a_j>=Delta((k-j)/b-1).

For any prediction value v, pairing the outer terms gives

 sum_{j=1}^n|v-a_j|
 >=sum_{j=1}^{floor(n/2)}(a_{n+1-j}-a_j)
 >=(Delta/b)floor(n^2/4)-Delta floor(n/2)
 >=(Delta/(4b))(n^2-1)-Delta n/2.

Sum over the realized buckets and use sum_v n_v=T and |{v:n_v>0}|<=T. Rearrangement yields

 sum_v n_v^2<=(4b/Delta)A+2bT+T.

Since T>=m and b<=2T/m, we have 4b/Delta<=16T and 2bT<=4T^2/m. This proves (2).

Hölder's inequality applied to n_v=(sqrt(n_v))^(2/3)(n_v^2)^(1/3) gives

 T^3<=(sum_v sqrt(n_v))^2 sum_v n_v^2.

Therefore, pathwise,

 N>=T/[4 sqrt(A+T/m+1)].

The function u -> (u+T/m+1)^(-1/2) is convex for u>=0, so Jensen's inequality gives

 E N>=T/[4 sqrt(E A+T/m+1)].                          (3)

## 4. Adaptive noise bucketing

We derive the needed probabilistic estimate rather than invoke it as a paper-specific black box. Let Z_1,...,Z_L be independent symmetric increments taking values ±h, where h>0 and L>=2. Let H be independent initial randomness, F_t=H join sigma(Z_1,...,Z_t), and let the bucket label v_t be F_{t-1}-measurable. Labels may be real-valued. Define

 U_v(t)=sum_{s<=t:v_s=v}Z_s,
 Phi_t=sum_v|U_v(t)|,
 E_t={U_{v_t}(t-1)=0},
 D=sum_{t=1}^L 1[E_t].

Every sum over buckets is a finite pathwise sum. Only the selected bucket changes at round t. Conditional on F_{t-1}, if its sum is zero the increase in Phi is h. Otherwise its sum is a nonzero multiple of h, and the mean change in absolute value under ±h is zero. Hence

 E Phi_L=h E D.                                      (4)

### Return-time estimate

The audited standard independent input is the first-return distribution of a simple symmetric random walk: its first positive return time tau is finite almost surely, takes even values, and

 P(tau=2k)=(1/(2k-1)) binom(2k,k)4^(-k),   k>=1.

The standard central-binomial estimate gives P(tau=2k)<=C_2 k^(-3/2). Therefore, for integers a>=1,

 P(tau>a)=sum_{k>floor(a/2)}P(tau=2k)<=C_3/sqrt(a).

The floor in this expression corrects the source's ceiling typo; the case a=1 is immediate. The discrete tail identity now gives

 E sqrt(min(tau,L))
 =sum_{a=0}^{L-1}(sqrt(a+1)-sqrt(a))P(tau>a)
 <=1+(C_3/2)sum_{a=1}^{L-1}1/a
 <=C_4 log(L+1).                                    (5)

Rescaling the walk by h shows that the bound is independent of h. It also holds conditionally on any sigma-field under which the future increments remain independent symmetric ±h variables.

### Predictable selections and excursion lengths

Append independent increments after L. For strictly increasing finite selection times tau_j satisfying {tau_j=s} in F_{s-1}, selected increments remain independent symmetric ±h variables conditional on the information before the first selection. Indeed, for any bounded variable Y measurable before the first selected time and bounded functions phi_1,...,phi_k, expand the expectation of Y product_j phi_j(Z_{tau_j}) over the value s of the last selected time. The preceding factors multiplied by 1[tau_k=s] are F_{s-1}-measurable. Conditional expectation replaces phi_k(Z_s) by its unconditional mean. Repeating proves the product identity, which establishes the asserted conditional independence.

Index actual excursions by their chronological starting rounds, not by an uncountable collection of possible labels. A new excursion starts precisely on E_t. On this event let ell_t be the number of updates to bucket v_t from round t through its next return to zero, or through its last update by L if no such return occurs. Set ell_t=0 off E_t.

Fix t and condition on F_{t-1}. The label v_t is then known. Starting with round t, select all later visits to this same label through L, and then select every round after L as an auxiliary continuation. These times are predictable and finite: before any round through L, whether the current label equals the stored label is known; after L the number of earlier visits is already known. The preceding predictable-selection argument shows that their increments are conditionally independent symmetric ±h variables.

On E_t the selected walk starts at zero. If tau_t is its first positive return time and M_t is the number of its actual updates from t through L, then

 ell_t=min(tau_t,M_t)<=min(tau_t,L).

There is no need to assume M_t independent of the walk or measurable at the excursion's start. By (5), and because E_t belongs to F_{t-1},

 E[1[E_t]sqrt(ell_t)]<=C_4 log(L+1)P(E_t).             (6)

For each bucket, its actual updates partition into its completed excursions and its final possibly truncated excursion. Subadditivity of the square root therefore gives pathwise

 sum_v sqrt(n_v)<=sum_{t=1}^L 1[E_t]sqrt(ell_t).

Taking expectations, summing (6) over the deterministic set of rounds, and using (4), we obtain

 E sum_v sqrt(n_v)<=C_4 log(L+1)E D
                  =(C_4/h)log(L+1)E sum_v|U_v(L)|.

Equivalently,

 E sum_v|U_v(L)|>=h/[C_4 log(L+1)] E sum_v sqrt(n_v).  (7)

This establishes adaptive bucketing, including random real-valued labels, without conditioning on final bucket sizes.

For the problem, use L=T, h=1/4, Z_t=x^t-y^t=-xi_t/4, H=sigma(R), and v_t=p_t. The required independence and predictability were verified at the beginning. Thus, for U_v=sum_{t:p_t=v}(x^t-y^t),

 E sum_v|U_v|>=c_1 E N/log(T+1).                      (8)

## 5. Constant-group transfer and conclusion

Let B_v=sum_{t:p_t=v}(p_t-x^t). Pathwise, sum_v|B_v|<=A, and the reverse triangle inequality gives

 Err_T(g_all)=sum_v|B_v+U_v|>=sum_v|U_v|-A.

Writing L_T=log(T+1), (8) implies

 M>=c_1 E N/L_T-E A.

Combining with (1), using log(m+1)<=L_T and taking T sufficiently large, yields

 M>=c_2 E N/L_T^2.

Substitute (3) and (1):

 M>=c_3 T/[L_T^2 sqrt(K_1 log(m+1)M+T/m+1)].          (9)

If K_1 log(m+1)M<=T/m+1, the denominator's square-root factor is at most sqrt(2(T/m+1)). Since m>=T^(1/3)/2, for sufficiently large T we have T/m+1<=3T^(2/3). Hence

 M>=c_4 T^(2/3)/L_T^2.

Otherwise, the case assumption itself gives

 M>(T/m+1)/(K_1 log(m+1))>=c_5 T^(2/3)/L_T,

using m<=T^(1/3). This is at least a constant times T^(2/3)/L_T^2 once L_T>=1.

Thus the fixed family satisfies the stronger lower bound M>=c_6 T^(2/3)/log^2(T+1), uniformly over all randomized online forecasters. Choose one universal C large enough for both the size bound on S and the logarithmic exponent in the requested statement, decreasing c and increasing T_0 if necessary. This proves the task with its stipulated quantifier order.

## Closure

All theorem-critical obligations have been derived. The only specialized external input is the stated standard simple-random-walk first-return law, applied to conditionally independent symmetric increments with a strictly positive step size. The source's tail-index typo has been explicitly repaired. There are no unresolved private proof obligations.
