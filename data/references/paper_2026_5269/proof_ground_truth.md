# Reference Proof

## Scope and proof obligations

This proof establishes the public bound under the bounded-reward model. It does not use Gaussian reward observations, a claimed extension to other reward classes, or the separate pure-online leading-constant result. All constants below are numerical and independent of the instance.

The theorem-critical obligations are: (1) a well-defined policy and an O(Delta_i^-2) concentration-failure contribution; (2) the suboptimal-arm median-intersection bound with its stated offline discount; (3) a valid low-index transfer and an optimal-arm accurate-anchor bound with the N_1 subtraction; (4) a uniform joint inverse-tail moment and the poor-anchor bound; and (5) aggregation. Each is proved below. No inherited Thompson-sampling lemma is accepted merely by citation.

Fix i!=1. Write Delta=Delta_i, mu=mu_1^on, x=mu_i^on+Delta/3, y=mu_i^on+2Delta/3=mu-Delta/3, L=log(T Delta^2+e^6), and ell=2L. Then 0<Delta<=1, 0<y<1, and L>=6. Also omega_j>=0 for every arm j, by the assumed shift bound.

For analysis, represent each arm's online observations by an independent infinite sequence Y_{j,1},Y_{j,2},..., revealed in order when that arm is pulled. These are i.i.d. with its online reward law and independent of the offline data. This is an equivalent coupling of the stipulated observation process, not information supplied to the learner. It lets us define every fixed-prefix statistic even if that prefix is not reached before T. We never assert concentration conditional on an adaptive pull count.

Let F_{t-1} denote the pre-round history, including the offline data, previous actions, observations, and any past policy randomness. Fresh Gaussian draws have their specified independent laws conditional on this history.

## Background inequalities used explicitly

For the average M of n>=1 independent [0,1]-valued variables, let m be the average of their means. The supplied Hoeffding bound gives

 P(M-m>=u)<=exp(-2nu^2),   P(M-m<=-u)<=exp(-2nu^2).

The bound also applies when component means differ. Thresholds outside the support give empty events, and endpoint cases follow by limits.

Write bar-Phi(z)=P(Z>z) for Z~Normal(0,1). The supplied Gaussian lower-tail inequality, applied at z>=1 and separately at 1 for 0<=z<=1, implies that a numerical c_0 satisfies

 1/bar-Phi(z) <= c_0(1+z)exp(z^2/2),   z>=0.                 (B1)

We also use the elementary upper bound

 bar-Phi(z)<= (1/2)exp(-z^2/2),   z>=0.                    (B2)

For completeness, substituting v=z+w in the Gaussian density integral gives bar-Phi(z)=exp(-z^2/2) integral_0^infinity exp(-zw) exp(-w^2/2) dw/sqrt(2 pi), which is at most exp(-z^2/2)/2.

Holder's inequality is used with explicitly specified conjugate exponents. Its special case with exponents 2 and 2 is Cauchy-Schwarz.

## Step 1: Concentration and decomposition

For a fixed prefix s of arm i, put n=s+N_i. If n>0, let M_{i,s} be its combined empirical mean and m_{i,s}=(s mu_i^on+N_i mu_i^off)/n. Define, at round t, the following events:

 E_on(t)={hat-mu_i^on(t)<=x};

 E_mu(t)={|hat-mu_i^hyb(t)-m_{i,T_i(t)}|<=sqrt(ell/n_i(t))};

 E_theta(t)={|theta_i^hyb(t)-hat-mu_i^hyb(t)-b_i(t)|<=sqrt(ell/n_i(t))}.

When n_i(t)=0, define E_mu(t) and E_theta(t) to be the whole space. The exceptional selection at that empty prefix will be counted separately when necessary. Put G_i(t)=E_on(t) intersect E_mu(t) intersect E_theta(t). The optimal-arm anchor event is not part of G_i(t).

Whenever arm i is selected with T_i(t)=s, that prefix count is left and cannot be selected again. Thus the number of selected bad online-mean prefixes is bounded pathwise by the sum of their fixed-prefix indicators. The s=0 mean is zero and cannot exceed x. Consequently,

 sum_t P(A(t)=i,E_on(t)^c)
 <= sum_{s=1}^{T-1} P(mean(Y_{i,1},...,Y_{i,s})>mu_i^on+Delta/3)
 <= sum_{s=1}^infinity exp(-2s Delta^2/9)
 <= 9/(2 Delta^2).                                         (1)

The same fixed-prefix counting, now with the combined independent observations, gives

 sum_t P(A(t)=i,E_mu(t)^c)
 <= sum_{0<=s<T:s+N_i>0} 2exp(-2ell)
 <= 2T exp(-4L)
 <= 2/Delta^2.                                            (2)

For n_i(t)>0, condition on F_{t-1}. The hybrid draw has variance 1/(n_i(t)+1), so (B2) gives

 P(E_theta(t)^c | F_{t-1})
 <= 2exp(-ell(n_i(t)+1)/(2n_i(t)))
 <= 2exp(-L).

The event is empty when n_i(t)=0. Hence

 sum_t P(A(t)=i,E_theta(t)^c)<=2T exp(-L)<=2/Delta^2.        (3)

Here T exp(-L)=T/(T Delta^2+e^6)<=Delta^-2. These arguments explain why the fixed positive logarithm is sufficient: empirical-mean failures are counted by selected prefixes, not by an additional union over every time and count.

Let H_i be the expected number of selections satisfying G_i(t) and hat-theta_i(t)>y, and let J_i be the expected number satisfying G_i(t) and hat-theta_i(t)<=y. A covering inequality, not an equality for overlapping bad events, now yields

 E[T_i(T+1)] <= C_bad/Delta^2 + H_i + J_i.                 (4)

## Step 2: Suboptimal-arm median intersection

On G_i(t), the anchor is at most x<y. Therefore hat-theta_i(t)>y requires both theta_i^on(t)>y and theta_i^hyb(t)>y.

First use the online sample. On E_on(t), conditional on F_{t-1},

 P(theta_i^on(t)>y | F_{t-1})
 <= exp(-(T_i(t)+1)Delta^2/18).

At most 18L/Delta^2+1 selections occur below the prefix threshold 18L/Delta^2. Above it, the conditional tail is at most exp(-L), so the total expected residual over T rounds is at most Delta^-2. Thus

 H_i <= 18L/Delta^2+1+Delta^-2.                            (5)

The Gaussian sample can still exceed y after this threshold; it is its expected contribution, not its possibility, that is small.

For the hybrid control, write N=N_i and omega=omega_i. At any nonempty prefix n=T_i(t)+N, the two hybrid good events give

 theta_i^hyb(t)-mu_i^on <= 2sqrt(ell/n)+N omega/n.          (6)

If this exceeds 2Delta/3, then n is at most max{36ell/Delta^2,3N omega/Delta}. Counting the eligible selected prefixes, with a unit allowance for integer endpoints and the empty prefix, gives

 H_i <= [max{72L/Delta^2,3N omega/Delta}-N]_+ + C.         (7)

Let a=3omega/Delta>=0. If a<=1, the right side of (7) is at most [72L/Delta^2-N]_++C, hence at most [72L/Delta^2-N(1-a)]_++C. If a>1, use (5); the desired discount is then zero. Since Delta<=1, the fixed counting allowances are absorbed into C/Delta^2. Therefore

 H_i <= [72L/Delta^2-N_i(1-3omega_i/Delta)_+]_+
        + C_high/Delta^2.                                (8)

This preserves the stated positive-part structure without relying on imported posterior bounds or the source's untracked numerical coefficient.

## Step 3: Low-index transfer and the accurate optimal anchor

### Correct conditional comparison

Put p_t=P(hat-theta_1(t)>y | F_{t-1}) and q_t=(1-p_t)/p_t. These are finite: the posterior means are finite, their variances are positive, and the probability of simultaneous successes is strictly positive.

Let D_t be the event that G_i(t) holds and every arm j!=1 has hat-theta_j(t)<=y. Conditional on F_{t-1}, D_t depends only on draws from suboptimal arms and is independent of the draws for arm 1. A selection counted by J_i implies D_t and hat-theta_1(t)<=y. Conversely, D_t together with hat-theta_1(t)>y forces selection of arm 1, retains G_i(t), and retains hat-theta_i(t)<=y. Therefore

 P(A(t)=i,G_i(t),hat-theta_i(t)<=y | F_{t-1})
 <= (1-p_t)P(D_t | F_{t-1})
 <= q_t P(A(t)=1,G_i(t),hat-theta_i(t)<=y | F_{t-1}).       (9)

In particular J_i<=E[sum_t q_t 1{A(t)=1}]. The distributions for arm 1 do not change until that arm is pulled again. Define p_k and q_k from its offline observations and first k online observations, whether or not that prefix is reached by time T. Each k can contribute at most one selected-arm-1 term. Nonnegativity gives

 J_i <= sum_{k=0}^{T-1} E[q_k].                           (10)

This formulation avoids undefined stopping times beyond the horizon and avoids conditioning the prefix observations on reaching the prefix.

Let h_k be arm 1's online empirical mean, with h_0=0. Let a_k and b_k be the conditional probabilities that its online and hybrid Gaussian samples, respectively, exceed y. Conditional independence and the elementary median rule give

 p_k=a_k+b_k-a_k b_k when h_k>y;
 p_k=a_k b_k when h_k<=y.                                 (11)

Consequently, on h_k>y,

 q_k <= min{a_k^-1-1,b_k^-1-1}.                           (12)

No pointwise ordering between a_k and b_k is asserted.

### An explicit single-posterior inverse-tail estimate

The following elementary estimate supplies all inverse-tail controls needed here. Let M be the average of n>=1 independent [0,1]-valued observations, let m be their average population mean, and let b be a deterministic shift such that m+b>=mu. Let r be the conditional probability that a Normal(M+b,1/(n+1)) variable exceeds y=mu-delta, where delta=Delta/3. There are universal constants M_* and C_* such that

 E[r^(-5/2)]<=M_*,                                       (13)

 E[r^-1-1]<=C_* exp(-n Delta^2/72).                       (14)

To prove (13), set W=sqrt(n+1)(m-M)_+. Since m+b>=mu>y, r>=bar-Phi(W). For n>=3, Hoeffding gives

 P(W>u)<=exp(-2n u^2/(n+1))<=exp(-3u^2/2).

By (B1), r^(-5/2)<=c_0^(5/2) f(W), where

 f(u)=(1+u)^(5/2) exp(5u^2/4).

The tail integration identity gives

 E[f(W)] = f(0)+integral_0^infinity f'(u)P(W>u) du
 <= 1+integral_0^infinity f'(u)exp(-3u^2/2) du < infinity.

Indeed, the integrand is a polynomially bounded factor times exp(-u^2/4). This is a numerical bound independent of n and the reward laws. For n=1 or 2, W<=sqrt(3) deterministically, giving another numerical bound. This proves (13).

For (14), let B={M+b>=mu-delta/2}. On B, r>=1/2 and (B2) yields

 r^-1-1 <= 2(1-r)<=exp(-(n+1)delta^2/8).

On B^c, Hoeffding gives P(B^c)<=exp(-n delta^2/2). Holder with exponents 5/2 and 5/3, together with (13), gives

 E[(r^-1-1)1{B^c}]
 <= M_*^(2/5) P(B^c)^(3/5)
 <= M_*^(2/5) exp(-3n delta^2/10).

The sum of these two bounds is at most C_*exp(-n Delta^2/72), proving (14).

For the empty prefix n=0, the prescribed sampler is Normal(0,1). Because 0<y<1, its success probability is at least bar-Phi(1)>0. Thus (13) and (14), with the exponential factor interpreted as 1, continue to hold after increasing the same numerical constants.

Apply this estimate to the online sampler using n=k, m=mu, b=0. Apply it to the hybrid sampler using n=k+N_1 and, when n>0,

 m=(k mu+N_1 mu_1^off)/n,
 b=N_1 V_1/n,
 m+b=mu+N_1 omega_1/n>=mu.

All observations used in each average are independent and bounded, although the online and hybrid averages share observations. No independence between these two averages is needed. We obtain, uniformly in k and N_1,

 E[a_k^(-5/2)]<=M_*,   E[b_k^(-5/2)]<=M_*,               (15)

 E[b_k^-1-1]<=C_*exp(-(k+N_1)Delta^2/72).                 (16)

These estimates directly derive the required online and hybrid inverse-tail controls rather than treating specialized imported results as established facts.

### Summing the accurate-anchor contribution

Let B_T=72L/Delta^2. By (12) and (16), each accurate-anchor term is at most C_*. There are at most [B_T-N_1]_++1 integers k>=0 with k+N_1<B_T. For the remaining at most T prefixes, (16) is at most C_*exp(-L), whose total is at most C_*/Delta^2. Thus

 sum_{k=0}^{T-1} E[q_k 1{h_k>y}]
 <= C_*[72L/Delta^2-N_1]_+ + C_accurate/Delta^2.          (17)

The online version follows from the same calculation with N_1=0. Equation (12) permits taking the better control, but does not require a false pointwise dominance of the hybrid tail.

## Step 4: Joint inverse-tail moment and the poor optimal anchor

Set alpha=5/4 and beta=5. On h_k<=y, (11) gives p_k=a_k b_k. The online and hybrid success probabilities can be dependent as random functions of the data. Nevertheless, Cauchy-Schwarz and (15) imply

 E[(a_k b_k)^(-alpha)]
 <= (E[a_k^(-2alpha)] E[b_k^(-2alpha)])^(1/2)
 <= M_*.                                                (18)

Here 2alpha=5/2, exactly the moment explicitly proved above.

This also closes the source's hitting-time formulation if used: conditionally on the prefix data, independent repeated pairs have a geometric waiting time G with success probability a_k b_k. Its conditional tail is (1-a_k b_k)^r<=exp(-r a_k b_k). Summing the increments of r^alpha against this tail gives E[G^alpha | data]<=C_alpha(a_k b_k)^(-alpha). Equation (18) therefore gives a uniform unconditional alpha moment. Separate maxima of the two component sequences are not used; they do not characterize simultaneous success.

For k>=1, bounded-reward Hoeffding gives

 P(h_k<=y)<=exp(-2k Delta^2/9).

Using q_k<=p_k^-1 on the poor-anchor event and Holder with exponents alpha and beta,

 E[q_k 1{h_k<=y}]
 <= E[(a_k b_k)^(-alpha)]^(1/alpha) P(h_k<=y)^(1/beta)
 <= M_*^(4/5) exp(-2k Delta^2/45).                        (19)

For k=0, (18) bounds the contribution by M_*^(4/5); no empirical-mean concentration claim is made about an empty sample. Summing the geometric series and using Delta<=1 gives

 sum_{k=0}^{T-1} E[q_k 1{h_k<=y}]<=C_poor/Delta^2.         (20)

Thus both branches in (10) are closed, including zero offline data, shared empirical observations, and the initial online prefix.

## Step 5: Aggregation and boundary cases

Combine (4), (8), (10), (17), and (20). For universal constants,

 E[T_i(T+1)]
 <= [72L/Delta_i^2-N_i(1-3omega_i/Delta_i)_+]_+
    +C_*[72L/Delta_i^2-N_1]_+
    +C_0/Delta_i^2.

Multiplying by Delta_i and summing over i!=1 proves the public inequality after choosing universal C,C_1,C_2,C_3 large enough. For example, the two internal logarithmic constants may both be taken as 72 in this proof, with the remaining numerical factors absorbed into C and C_3.

The proof handles N_i=0 through independent draws from the coincident laws, not reuse of one draw. Empty empirical means and shifts are defined explicitly. The cases omega_i=0, 3omega_i=Delta_i, arbitrarily large shift bounds, large offline sample sizes, and T Delta_i^2<=1 are covered by the case split and the positive logarithm. Unique optimality excludes zero suboptimal gaps. No constant depends on a reward law, gap, sample size, shift bound, K, or T.

Finally, each offline subtraction is nonnegative. Dropping both subtractions and using L>=6 gives Reg(T)=O(sum_{i!=1} log(T Delta_i^2+e^6)/Delta_i). This is an order comparison of guarantees, not a claim that realized or expected regret is pointwise monotone in the offline data.

## Source-repair accounting

The source's empirical-mean updates are interpreted as ordinary empirical averages, consistently with its definitions and subsequent weighted-average calculations; the posterior variances retain their +1. Overlapping bad events give a covering inequality. The repaired proof uses pre-round conditioning and fixed-prefix observations, rather than concentration conditional on an adaptive count. Its positive fixed-horizon confidence level replaces the potentially negative schedule and supplies the refined logarithm without an invalid comparison of logarithms. The tail-ratio comparison retains the shared low-index condition. Hybrid concentration uses n=k+N_1 observations and variance 1/(n+1), not the inconsistent pseudo-count normalization. The poor-anchor branch uses its correct complementary event and bounded-reward concentration. Finally, (18) replaces the false separate-maxima inclusion by an explicit joint moment argument. These corrections preserve the frozen theorem and its proof architecture. Every theorem-critical obligation listed at the start is closed.
